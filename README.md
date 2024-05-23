[![build-test](https://github.com/darkwizard242/ansible-role-subversion/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-subversion/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-subversion/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-subversion/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/subversion) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subversion&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-subversion) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subversion&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-subversion) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subversion&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-subversion) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-subversion?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-subversion?color=orange&style=flat-square)

# Ansible Role: subversion

Role to install (_by default_) [subversion](https://subversion.apache.org/) package or uninstall (_if passed as var_) on **Debian**, **Ubuntu** and **CentOS** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
subversion_app: subversion
subversion_desired_state: present
```

### Variables table:

Variable                 | Description
------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------
subversion_app           | Defines the app to install i.e. **subversion**
subversion_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **subversion** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.subversion
```

For customizing behavior of role (i.e. installation of latest **subversion** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.subversion
  vars:
    subversion_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **subversion** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.subversion
  vars:
    subversion_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-subversion/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
