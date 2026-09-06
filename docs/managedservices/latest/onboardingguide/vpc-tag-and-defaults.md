

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# VPC tag and defaults
<a name="vpc-tag-and-defaults"></a>

For the most current information on AMS backup, see [Continuity management](https://docs.aws.amazon.com/managedservices/latest/userguide/continuity-mgmt.html).

**Important**  
By default, EC2 stack backups are disabled (Backup = False). You can enable EC2 instance backups at the time of creation by adding a tag `Key: Backup, Value: True` when requesting an EC2 stack through an RFC (CT ct-14027q0sjyt1h). If you want to add the tag after the instance has been created, submit an RFC with the Management \| Advanced stack components \| EC2 instance stack \| Update CT (ct-38s4s4tm4ic4u).