

# Supported Regions for AWS Transform
<a name="regions"></a>

**Note**  
If you make a request that requires AWS Transform to retrieve information from an opt-in Region not listed on this page, AWS Transform can make calls to that Region. To manage access to Regions AWS Transform can make calls to, see [Security in AWS Transform](security.md).

This topic describes the AWS Regions where you can use AWS Transform. For more information about AWS Regions, see [Specify which AWS Regions your account can use](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) in the *AWS Account Management Reference Guide*.

Your data might be processed in a different Region from the Region where you use AWS Transform. For information on cross-region processing in AWS Transform, see [Cross-region processing](cross-region-processing.md). For information on where data is stored during processing, see [Data protection](data-protection.md).

## Supported AWS Regions (enabled by default)
<a name="default-regions"></a>

You can create AWS Transform workspaces in the following AWS Regions. These Regions are enabled by default - you don't need to enable them before use. For more information, see [Regions that are enabled by default](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#regionthat). 
+ US East (N. Virginia)
+ Europe (Frankfurt)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Europe (London)
+ Asia Pacific (Seoul)
+ Canada (Central)
+ South America (São Paulo) - Mainframe modernization agents only

The workspace in which you create a job determines the AWS Region of the job. To create a job in a different Region, you must use a different workspace that is in your desired Region.

For VMware projects, the Region of the workspace is used for discovery. However, you can specify a different Region as the migration target. That target Region is where your workloads are hosted when the migration is complete. For more information about AWS Region considerations for VMware migrations, including the list of possible target Regions, see [Supported target regions](transform-vmware-connect-target-account.md#transform-vmware-cta-supported-regions).