

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# How AMS logging works
<a name="getting-started-log-mgmt"></a>

AMS single-account landing zone (SALZ) log management uses a variety of pre-installed agents and tools that are implemented when instances and applications are onboarded or provisioned.

Logging is configured during the account onboarding process and when a stack is launched.

AMS multi-account landing zone (MALZ) logs produced by instances and AWS services are available in CloudWatch Logs or Amazon Simple Storage Service (Amazon S3), within each account managed by AMS. AMS multi-account landing zone provides a central Logging Account that acts as a central aggregation location for some logs produced by individual application accounts.

The tables in the [Accessing your logs](access-to-logs.md) subsections describe which logs are available in individual accounts, and which are available in the central Logging Account.