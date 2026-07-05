End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# EC2 instance tag and defaults

The **EC2 stack backup tag** specifies whether the stack requires a snapshot of the attached EBS volumes or not.

Tag`Key: Backup`

Tag`Value: True, False`

By default, the value is `False` the backup tag is not present, and the stack does not have scheduled backups.

Change the tag `Key: Backup` to `Value: True` to enable backups, which are then done on the schedule set with the VPC backup tag.

###### Note

The casing for the tag value (Value only) is insensitive, so True/true or False/false are all acceptable.
