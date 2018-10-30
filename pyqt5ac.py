import glob
import os
import shlex
import subprocess
import sys

try:
    import colorama
    colorama.init()
except ImportError:
    hasColorama = False
else:
    hasColorama = True

# TODO Turn this into a PyPi script
__version__ = '1.0.0'

# Options
# ----------------------------------------------------------------------------------------------------------------------
# List containing source and destination of files to compile
files = \
    [
        [
            'gui/*.ui',
            'generated/'
        ]
    ]

pyrccCmd = 'pyrcc5'
pyrccOptions = ''
pyuicCmd = 'pyuic5'
pyuicOptions = '--from-imports'


# ----------------------------------------------------------------------------------------------------------------------


# Takes command, options, source and destination folders and creates a command from it
# Escapes the src/dst and removes any additional whitespace
def buildCmd(cmd, options, src, dst):
    newCmd = '%s %s %s -o %s' % (cmd, options, shlex.quote(src), shlex.quote(dst))
    args = shlex.split(newCmd)

    return [arg for arg in args if arg]


# Writes a colored message to the screen or falls back to a regular message
def writeMessage(text, color=None):
    if hasColorama:
        colors = {
            'red': colorama.Fore.RED,
            'green': colorama.Fore.GREEN,
            'yellow': colorama.Fore.YELLOW,
            'blue': colorama.Fore.BLUE
        }
        try:
            print(colors[color] + text + colorama.Fore.RESET)
        except KeyError:
            print(text)
    else:
        print(text)


def isOutdated(src, dst, ui, force):
    if force:
        return True

    outdated = (not os.path.exists(dst) or
                (os.path.getmtime(src) > os.path.getmtime(dst)))

    if not outdated and not ui:
        # For qrc files, we need to check each individual resources.
        # If one of them is newer than the dst file, the qrc file must be considered as outdated.
        # File paths are relative to the qrc file path
        qrcParentDir = os.path.dirname(src)

        with open(src, 'r') as f:
            lines = f.readlines()
            lines = [line for line in lines if '<file>' in line]

        cwd = os.getcwd()
        os.chdir(qrcParentDir)

        for line in lines:
            filename = line.replace('<file>', '').replace('</file>', '').strip()
            filename = os.path.abspath(filename)

            if os.path.getmtime(filename) > os.path.getmtime(dst):
                outdated = True
                break

        os.chdir(cwd)

    return outdated


def main():
    for globExpr, dest in files:
        for src in glob.glob(globExpr):
            if not os.path.exists(src):
                writeMessage('skipping target %s, file not found' % src, 'yellow')
                continue

            # Replace any instances of %%DIRNAME%% with the directory that src is contained in
            # Then get the absolute path for dst and src based on current working directory (cwd)
            dst = os.path.join(os.getcwd(), dest.replace('%%DIRNAME%%', os.path.dirname(src)))
            src = os.path.join(os.getcwd(), src)

            # Normalize the src/dst paths by removing any relative directories (../ or ./)
            src, dst = os.path.normpath(src), os.path.normpath(dst)

            if src.endswith('.ui'):
                ui = True
                ext = '_ui.py'
                cmd = pyuicCmd
                options = pyuicOptions
            elif src.endswith('.qrc'):
                ui = False
                ext = '_rc.py'
                cmd = pyrccCmd
                options = pyrccOptions
            else:
                continue

            filename = os.path.split(src)[1]
            filename = os.path.splitext(filename)[0]
            dst = os.path.join(dst, filename + ext)

            os.makedirs(os.path.split(dst)[0], exist_ok=True)

            # TODO: Add force parameter
            if isOutdated(src, dst, ui, False):
                try:
                    cmd = buildCmd(cmd, options, src, dst)
                    cmdString = ' '.join(cmd)
                    subprocess.check_call(cmd, shell=True)
                except subprocess.CalledProcessError as e:
                    if e.output:
                        writeMessage(cmdString, 'yellow')
                        writeMessage(e.output.decode(sys.stdout.encoding), 'red')
                    else:
                        writeMessage(cmdString, 'red')
                except OSError as e:
                    writeMessage(cmdString, 'yellow')
                    writeMessage(str(e), 'red')
                else:
                    writeMessage(cmdString, 'green')
            else:
                writeMessage('skipping %s, up to date' % src)


if __name__ == '__main__':
    main()
