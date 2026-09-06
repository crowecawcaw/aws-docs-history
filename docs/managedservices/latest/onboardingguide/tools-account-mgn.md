

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AWS Application Migration Service (AWS MGN)
<a name="tools-account-mgn"></a>

[AWS Application Migration Service](https://aws.amazon.com/application-migration-service/) (AWS MGN) can be used in your MALZ Tools account through the `AWSManagedServicesMigrationRole` IAM role that is created automatically during Tools account provisioning. You can use AWS MGN to migrate applications and databases that run on supported versions of Windows and Linux [operating systems](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html).

For the most up-to-date information on AWS Region support, see [the AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

If your preferred AWS Region is not currently supported by AWS MGN, or the operating system on which your applications run is not currently supported by AWS MGN, consider using the [CloudEndure Migration](https://console.cloudendure.com/#/register/register) in your Tools account instead.

**Requesting AWS MGN Initialization**

AWS MGN must be [initialized](https://docs.aws.amazon.com/mgn/latest/ug/mandatory-setup.html) by AMS before first use. To request this for a new Tools account, submit a Management \| Other \| Other RFC from the Tools account with these details:

```
RFC Subject=Please initialize AWS MGN in this account
RFC Comment=Please click 'Get started' on the MGN welcome page here: 
    [ https://console.aws.amazon.com/mgn/home?region={{MALZ\_PRIMARY\_REGION}}\#/welcome](https://console.aws.amazon.com/mgn/home?region=AP-SOUTHEAST-2#/welcome) using all default values 
    to 'Create template' and complete the initialization process.
```

Once AMS successfully completes the RFC and initializes AWS MGN in your Tools account, you can use `AWSManagedServicesMigrationRole` to edit the default template for your requirements.

![AWS MGN, Setup application migration service.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/aws_mgn_firstrun.png)
