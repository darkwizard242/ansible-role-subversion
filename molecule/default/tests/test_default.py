import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'subversion'
PACKAGE_BINARY = '/usr/bin/svn'


def test_subversion_package_installed(host):
    """
    Tests if subversion is installed
    """
    assert host.package(PACKAGE).is_installed


def test_subversion_binary_exists(host):
    """
    Tests if svn binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_subversion_binary_file(host):
    """
    Tests if svn binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_subversion_binary_which(host):
    """
    Tests the output to confirm svn's binary location.
    """
    assert host.check_output('which svn') == PACKAGE_BINARY
