

# Release: Elastic Beanstalk Windows Server 2012 R2 platform branches retired on December 04, 2023
<a name="release-2023-12-04-windows-2012-retire"></a>

This release announces the retirement of Windows Server 2012 R2 and Windows Server 2012 R2 Core platform branches.

**Release date:** December 04, 2023

## Changes
<a name="release-2023-12-04-windows-2012-retire.changes"></a>

Today we're announcing the retirement of the following platform branches:
+ Windows Server 2012 R2 running IIS 8.5
+ Windows Server Core 2012 R2 running IIS 8.5

Elastic Beanstalk is retiring these platforms branches, because the operating systems that they're based on have reached *end of support* by Microsoft. For more information, see the Microsoft website [Windows Server 2012 R2 – Microsoft Lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2012-r2). 

Once retired, the platform branches are no longer available from the Elastic Beanstalk console. You can continue to operate your existing environments that are based on these retired platform branches until March 4, 2024, which is 90 days after today's December 4 retirement date.

Elastic Beanstalk will make Beanstalk Windows 2012 AMIs private after March 4, 2024. This action will prevent the launching of instances in your Windows 2012 environments that use the default Beanstalk AMI. In order to retain access to the AMIs, you may copy the AMIs into your accounts for use in your Beanstalk environments. For detailed instructions, see [Preserving access to an AMI for a retired platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.customenv-env-copy.html) in the *AWS Elastic Beanstalk Developer Guide*.

If you currently use these retired platform branches, we strongly recommend that you start planning your migration to one of the *Windows Server version 2* platforms, which are current and fully supported:
+ Windows Server 2019 with IIS 10.0 version 2.x
+ Windows Server 2016 with IIS 10.0 version 2.x

For full migration considerations, see [Major Version Migration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html) in the *AWS Elastic Beanstalk Developer Guide*. 

For more information about platform deprecation, see [Elastic Beanstalk platform support policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html) in the *AWS Elastic Beanstalk Developer Guide*.

**Note**  
The retirement of these platform branches may not reflect in all regions at the time these release notes are published. The platform branch status of *retired* will update in all regions throughout this week.