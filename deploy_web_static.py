#!/usr/bin/python3
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists

# Set the remote hosts and the path to your SSH key
env.hosts = ['34.207.62.95', '54.157.179.133']
env.user = 'ubuntu'
env.key_filename = '/root/alx-system_engineering-devops/0x0B-ssh/school'

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        if not exists("versions"):
            local("mkdir versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static app.py templates requirements.txt".format(archive_path))
        return archive_path
    except Exception as e:
        print("Error in do_pack: ", e)
        return None

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        file_no_ext = file_name.split(".")[0]
        release_folder = "/data/web_static/releases/{}/".format(file_no_ext)

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Create the directory where the archive will be unpacked
        run("mkdir -p {}".format(release_folder))

        # Unpack the archive to the release folder
        run("tar -xzf /tmp/{} -C {}".format(file_name, release_folder))

        # Remove the archive from /tmp/
        run("rm /tmp/{}".format(file_name))

        # Move the contents to the correct location
        run("mv {0}web_static/* {0}".format(release_folder))
        run("rm -rf {0}web_static".format(release_folder))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_folder))

        # Move the app files to /var/www/flask_app/
        run("mkdir -p /var/www/flask_app/")
        run("mv -f /data/web_static/releases/{}/app.py /var/www/flask_app/".format(file_no_ext))
        run("mv -f /data/web_static/releases/{}/requirements.txt /var/www/flask_app/".format(file_no_ext))

        # Remove the existing templates directory and move the new one
        run("rm -rf /var/www/flask_app/templates")
        run("mv -f /data/web_static/releases/{}/templates /var/www/flask_app/".format(file_no_ext))

        return True
    except Exception as e:
        print("Error in do_deploy: ", e)
        return False

def deploy():
    """Creates and distributes an archive to the web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

