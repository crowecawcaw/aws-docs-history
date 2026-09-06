

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# RDS instance backup and defaults
<a name="rds-instance-backup-defaults"></a>

The Amazon Relational Database Service (RDS) default values are defined in the stack templates:

` Backup: Yes`

` Backup Window: 22:00-23:00 (RDS local time zone)`

` Retention Period: 7 (7 snapshots stored)`