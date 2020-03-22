import logging
import subprocess
import shlex

logger = logging.getLogger(__name__)
        
def execute(cmd, cwd, timeout):
    cmd = shlex.split(cmd)
    try:
        process = subprocess.run(cmd,
                     cwd=cwd,
                     timeout=timeout,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     #shell=True,
                     universal_newlines=True)
        return {'output': {
                    'stdout': process.stdout,  
                    'stderr': process.stderr, 
                    'returncode': process.returncode
                    }
               }
    except subprocess.TimeoutExpired:
        return {'error': 'Timeout'} 
    return process 
