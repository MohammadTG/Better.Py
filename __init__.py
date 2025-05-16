#BetterPy/__init__.py
# -*- coding: utf-8 -*-

__version__ = "1.0.0"
__auther__ = "MohammadTaher.GH"

import file as File
import web as Web
import timetool as Time
import mathtool as Math
import sys as Sys
import devtool  as Dev
import security as Security
import game as Game
import methodtool as Method

def is_online(host="8.8.8.8", port=53, timeout=3):
    """Check if the system is online by attempting to connect to a host and port.
    Args:
        host (str): The host to connect to. Default is
        port (int): The port to connect to. Default is 53.
        timeout (int): The timeout for the connection attempt in seconds. Default is 3.
    Returns:
        bool: True if the system is online, False otherwise.
    Raises:
        socket.error: If there is an error connecting to the host and port.
    Example:
        >>> is_online()
        True
        >>> is_online("google.com", 80)
        True
        >>> is_online("invalid.host", 80)
        False
        """
    import socket
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False



