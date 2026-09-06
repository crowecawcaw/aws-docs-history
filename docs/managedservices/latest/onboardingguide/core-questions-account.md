

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS multi-account landing zone account configuration
<a name="core-questions-account"></a>
+ New Account ID

  The AWS account ID that you created for AMS multi-account landing zone. Should not be part of an AWS organization.
+ Service Region

  The primary Region in which the AMS multi-account landing zone environment will be deployed.
+ The core account emails for notifications. (these should all be in the same domain). Provide an email address for each:
  + Shared Services account
  + Networking account
  + Logging account
  + Security account
+ Your service type, Premium or Plus

  This determines the service level agreements (SLAs) for resolving issues in your environment