#coding=uft-8
from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['ip地址', ]
env.password = '你的密码'

@runs_once
@task
def local_update():
    with lcd('文件本地路径'):
        local("git add .")
        local("git commit -m 'update'")
        local("git pull origin master")
        local("git push origin master")


@task
def remote_update():
    with cd("服务器文件路径"):
        run("git checkout master")
        run("git pull origin master")

@task
def deploy():
    local_update()
    remote_update()
