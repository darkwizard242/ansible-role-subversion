[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-subversion.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-subversion) ![Ansible Role](https://img.shields.io/ansible/role/45977?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/45977?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/45977?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subversion&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-subversion) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-subversion?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-subversion?color=orange&style=flat-square)

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

Variable                 | Value (default) | Description
------------------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
subversion_app           | subversion      | Defines the app to install i.e. **subversion**
subversion_desired_state | present         | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
