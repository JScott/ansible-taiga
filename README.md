# ansible-taiga

[Taiga](https://taiga.io) - Taiga | Taiga.Io | Agile, Open Source, Free Project Management System

[![Platforms](http://img.shields.io/badge/platforms-ubuntu-lightgrey.svg?style=flat)](#)

Tunables
--------
* `taiga_log_root` (string) - Where Taiga will place its log files.
* `taiga_front_access_log_path` (string) - Where Taiga will place its front-end access log.
* `taiga_front_error_log_path` (string) - Where Taiga will place its front-end error log.
* `taiga_back_access_log_path` (string) - Where Taiga will place its back-end access log.
* `taiga_back_error_log_path` (string) - Where Taiga will place its back-end error log.
* `taiga_runtime_root` (string) - Where Taiga will place its PID files.
* `taiga_back_pidfile_path` (string) - Where Taiga will place its back-end PID file.
* `taiga_install_root` (string) - Where Taiga files will be installed to.
* `taiga_front_install_path` (string) - Where Taiga front-end files will be installed to.
* `taiga_back_install_path` (string) - Where Taiga back-end files will be installed to.
* `taiga_data_install_path` (string) - Where Ansible will store files to record past data migrations.
* `taiga_front_repo` (string) - The git repo to clone the front-end code from.
* `taiga_back_repo` (string) - The git repo to clone the back-end code from.
* `taiga_front_version` (string) - The version of the front-end to clone.
* `taiga_back_version` (string) - The version of the back-end to clone.
* `taiga_import_sample_data` (boolean) - Whether or not to migrate Taiga's sample data on installation.
* `taiga_database_host` (string) - The host Taiga will use for it's database.
* `taiga_database_port` (string) - The port Taiga will use for it's database.
* `taiga_database_password` (string) - The password Taiga will use for it's database.
* `taiga_database_username` (string) - The username Taiga will use for it's database.
* `taiga_public_register_enabled` (string) - Whether or not to allow public user registration.
* `taiga_hostname` (string) - The hostname of the server that Taiga is running on.
* `taiga_port` (integer) - The port that Taiga is running on.
* `taiga_url_scheme` (string) - The URL scheme that Taiga is served on (e.g. "http").
* `taiga_from_email_address` (string) - The email address Taiga will send from.
* `taiga_email_host` (string) - The host of the service that provides that email.
* `taiga_email_port` (integer) - The port of the service that provides that email.

Dependencies
------------
* [telusdigital.upstart](https://github.com/telusdigital/ansible-upstart/)
* [telusdigital.python](https://github.com/telusdigital/ansible-python/)
* [telusdigital.nginx](https://github.com/telusdigital/ansible-nginx/)
* [telusdigital.postgres](https://github.com/telusdigital/ansible-postgres/)
* [telusdigital.logrotate](https://github.com/telusdigital/ansible-logrotate/)

Example Playbook
----------------
```
- hosts: servers
  roles:
    - role: telusdigital.kibana
```

License
-------
[GNU Affero](https://tldrlegal.com/license/gnu-affero-general-public-license-v3-(agpl-3.0))

Contributors
------------
* [Chris Olstrom](https://colstrom.github.io/) | [e-mail](mailto:chris@olstrom.com) | [Twitter](https://twitter.com/ChrisOlstrom)
* [Aaron Pederson](https://aaronpederson.github.io) | [e-mail](mailto:aaronpederson@gmail.com) | [Twitter](https://twitter.com/GunFuSamurai)
* [Justin Scott](https://jvscott.net) | [e-mail](mailto:jvscott@gmail.com) | [Twitter](https://twitter.com/AKindlyOrc)
