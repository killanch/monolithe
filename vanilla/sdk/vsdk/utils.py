# -*- coding: utf-8 -*-

import logging
vsdk_logger = logging.getLogger('vsdk')


def set_log_level(level, handler=None):
    """ Set both VSDK and Bambou log level to the given level

        Args:
            level: a logging level (ex: logging.DEBUG, logging.ERROR)
            handler: a logging handler (ex: logging.Streamhandler)
    """

    from bambou import bambou_logger

    if handler is None:
        handler = logging.StreamHandler()

    bambou_logger.setLevel(level)
    bambou_logger.addHandler(handler)

    vsdk_logger.setLevel(level)
    vsdk_logger.addHandler(handler)