End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# Scheduling AMS backups at the VPC level

AWS Managed Services (AMS) backup scheduling in the VPC, where the target instances are allocated, is created during account onboarding with a
default tag in the VPC creation schema.
The backup system schedules the execution of the snapshots depending on that VPC Tag. Modification of the schedule can be made by creating a
service request. For more
information, see [VPC Tag and Defaults](vpc-tag-and-defaults.md "vpc-tag-and-defaults.md").

For backup defaults, see [Understanding AMS Defaults](backup-defaults.md "backup-defaults.md")
