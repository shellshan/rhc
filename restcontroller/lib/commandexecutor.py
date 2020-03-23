import logging
import subprocess
import shlex

logger = logging.getLogger(__name__)

def execute(cmd, cwd, timeout, user):
    try:
        # Need to look at linux runuser command instead of sudo
        sucmd = shlex.split('sudo su - {}'.format(user))
        with subprocess.Popen(sucmd,
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     #shell=True,
                     universal_newlines=True) as process:
            stdout, stderr = process.communicate("{}\n".format(cmd), timeout=timeout)

            return {'output': {
                        'stdout': stdout,
                        'stderr': stderr,
                        'returncode': process.returncode
                        }
                   }
    except subprocess.CalledProcessError as e:
        return {'output': {
                    'stdout': e.stdout,
                    'stderr': e.stderr,
                    'returncode': e.returncode
                    }
               }
    except subprocess.TimeoutExpired:
        return {'error': 'Timeout'}
    return process
