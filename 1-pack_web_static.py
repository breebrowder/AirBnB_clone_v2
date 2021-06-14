#!/usr/bin/python3
""" Fabric script tht generates a .tgz ar from contents of web_static folder """

from fabric.api import local
from datetime import datetime

def do_pack():
    """ Return the archive path if the archive has been correctly generated """

    try:
        now = datetime.now()
        ArName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        ArPath = "versions/" + ArName

        local("sudo mkdir -p versions")

        local("tar -czvf " + ArPath + " web_static")

        return ArPath

    except:
        return None
