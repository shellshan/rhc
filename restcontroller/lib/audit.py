import logging

audit_logger = logging.getLogger("audit")

def audit(*args):
    audit_logger.info('|'.join(map(str,args)))
