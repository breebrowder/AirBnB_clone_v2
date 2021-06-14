#!/usr/bin/python3
""" Fabric script tht generates .tgz ar from contents of web_static """

from fabric.api import local
from datetime import datetime
import os.path

env.hosts = ['35.231.119.75', '34.207.111.89']


def do_deploy(archive_path):
    """ Deploy to web_static """

    if not os.path.exists(archive_path):
        return False

    try:
        arName = archive_path[9:]
        archiveNameWithoutExtension = arName[:-4]
        put(archive_path, '/tmp/' + arName)
        run("mkdir -p /data/web_static/releases/" +
            archiveNameWithoutExtension)
        run('tar -xzvf /tmp/' + arName +
            " -C /data/web_static/releases/" +
            archiveNameWithoutExtension + " --strip-components=1")
        run("rm -rf /tmp/" + arName)
        run("rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/" +
            archiveNameWithoutExtension + " /data/web_static/current")

        return True
    except:
        return False


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
