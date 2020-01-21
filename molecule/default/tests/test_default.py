import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_git_package_installed(host):
    assert host.package("subversion").is_installed


def test_git_binary_exists(host):
    assert host.file('/usr/bin/svn').exists


def test_git_binary_file(host):
    assert host.file('/usr/bin/svn').is_file


def test_git_binary_which(host):
    assert host.check_output('which svn') == '/usr/bin/svn'
