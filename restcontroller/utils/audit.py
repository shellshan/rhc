import logging

audit_logger = logging.getLogger("audit")

def audit(_list):
    audit_logger.info('|'.join(map(str,_list)))
