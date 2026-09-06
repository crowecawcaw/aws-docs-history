

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Automatically update code on Linux instances
<a name="auto-config-instance-code"></a>

AMS automatically updates on instance code on Linux instances. This helps to improve operational stability and security of the AMS components and environment altogether.

**FAQ:**

What's included in the On Instance Code (OIC) on Linux?  
OIC includes ams-toolkit package along with some configuration files and cron jobs. AMS require these files and packages for integration (Active Directory, CloudFormation and other dependencies). We pre-bake these files into AMS-provided AMIs or install onto your instance during workload ingestion.

When will AMS update OIC?  
AMS update OIC when we release a new version with bug fixes or other improvements. The workflow to check the OIC version and update runs daily.