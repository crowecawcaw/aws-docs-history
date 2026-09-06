

# Claim phone numbers to Connect Customer instances across multiple AWS Regions
<a name="claim-phone-number-multiple-regions"></a>

**Note**  
**New user?** Check out the [Connect Customer Global Resiliency Workshop](https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US). This online course guides you through the process of onboarding and testing phone number and agent failover using new APIs through the AWS CLI.  
Global Resiliency is available only for Connect Customer instances created in the following AWS Regions: US East (N. Virginia), US West (Oregon), Asia Pacific (Osaka), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (London).  
You can only create a replica in the US East (N. Virginia) Region if your source is US West (Oregon), or the other way around. 
You can only create a replica in the Europe (Frankfurt) Region if your source is Europe (London), or the other way around.
You can only create a replica in Asia Pacific (Osaka) Region if your source is Asia Pacific (Tokyo).
To obtain access to this feature, contact your Connect Customer Solutions Architect or Technical Account Manager.

To place or receive calls to a phone number across instances in multiple AWS Regions, you need to claim a phone number to a traffic distribution group. 

**To claim a phone number to a traffic distribution group**

1. Create a traffic distribution group by using the [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) API.

1. Describe your traffic distribution group by using the [DescribeTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeTrafficDistributionGroup.html) API to determine whether it has been created successfully (`Status` must be `ACTIVE`).

1. After your traffic distribution group has been created successfully (`Status` is `ACTIVE`), you can claim phone numbers to it by using the [ClaimPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html) API. 