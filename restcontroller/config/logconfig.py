logconfig = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "general": {
            "format": "[%(asctime)-15s %(process)d %(threadName)s %(levelname)s %(module)s %(funcName)s] %(message)s"
        },
        "audit": {
            "format": "%(message)s"
        }
    },
    "handlers": {
        "all": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "general",
            "filename": "/var/log/rhc/rhc.log",
            "maxBytes": 20971520,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "audit": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "audit",
            "filename": "/var/log/rhc/rhc.audit.log",
            "maxBytes": 20971520,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "error": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "general",
            "filename": "/var/log/rhc/rhc.error.log",
            "maxBytes": 20971520,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },
    "loggers": {
        "audit": {
            "level": "INFO",
            "handlers": ["audit"]
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["all", "error"]
    }
}
