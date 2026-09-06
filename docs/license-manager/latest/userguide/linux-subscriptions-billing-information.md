

# Billing information for Linux subscriptions in License Manager
<a name="linux-subscriptions-billing-information"></a>

Each commercial Linux subscription running on Amazon EC2 has billing information associated with the Amazon Machine Image (AMI). Commercial Linux subscriptions have Amazon EC2 usage operation, AWS Marketplace product code, or a combination of both. For more information, see [AMI billing information fields](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances* and [AMI product codes](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-getting-started.html#ami-product-codes) in the *AWS Marketplace Seller Guide*.




| Subscription name | Amazon EC2 usage operation | AWS Marketplace product code | Subscription type | 
| --- | --- | --- | --- | 
| Red Hat Enterprise Linux Server BYOS | RunInstances:00g0 | ✗ | Bring Your Own Subscription model (BYOS) | 
| Red Hat Enterprise Linux Server | RunInstances:0010 | ✗ | EC2 subscription-included | 
| Red Hat Enterprise Linux with High Availability Add-on | RunInstances:1010 | ✗ | EC2 subscription-included | 
| Red Hat Enterprise Linux with SQL Server Standard and High Availability | RunInstances:1014 | ✗ | EC2 subscription-included | 
| Red Hat Enterprise Linux with SQL Server Enterprise and High Availability | RunInstances:1110 | ✗ | EC2 subscription-included | 
| Red Hat Enterprise Linux with SQL Server Standard | RunInstances:0014 | ✗ | EC2 subscription-included | 
| Red Hat Enterprise Linux with SQL Server Web | RunInstances:0210 | ✗ | EC2 subscription-included | 
| Red Hat Enterprise Linux with SQL Server Enterprise | RunInstances:0110 | ✗ | EC2 subscription-included | 
| SUSE Linux Enterprise Server | RunInstances:000g | ✗ | EC2 subscription-included | 
| Red Hat Enterprise Linux for SAP with High Availability and Update Services | RunInstances:0010 | ✓ | AWS Marketplace subscription ¹ | 
| SUSE Linux Enterprise Server with SAP | ✗ | ✓ | AWS Marketplace subscription | 
| Ubuntu Pro | RunInstances:0g00 | ✓ | AWS Marketplace subscription | 
| Red Hat Enterprise Linux Workstation | ✗ | ✓ | AWS Marketplace subscription | 

¹ This subscription has both an Amazon EC2 usage operation and AWS Marketplace product code.

## Usage metrics for Linux subscriptions
<a name="linux-subscriptions-usage-metrics"></a>

The following metrics and dimensions are available for Linux subscriptions:


| Metric | Description | 
| --- | --- | 
| RunningInstancesCount | The total number of instances running in the current account that are grouped by the subscription name, or by subscription name and Region.<br />Units: Count<br />Dimensions:<br />`SubscriptionName`: The name of the subscription.<br />`Region`: The Region where the resource using a commercial Linux subscription was discovered. | 