# VPC tag and defaults

For the most current information on AMS backup, see
[Continuity management](../userguide/continuity-mgmt.md "../userguide/continuity-mgmt.md").

###### Important

By default, EC2 stack backups are disabled (Backup = False). You can enable EC2 instance backups at the time of creation
by adding a tag `Key: Backup, Value: True` when requesting an EC2 stack through an RFC (CT ct-14027q0sjyt1h). If you want to add the
tag after the instance has been created, submit an RFC with the
Management | Advanced stack components | EC2 instance stack | Update CT (ct-38s4s4tm4ic4u).
