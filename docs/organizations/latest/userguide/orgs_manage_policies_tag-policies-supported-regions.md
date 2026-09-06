

# Supported Regions
<a name="orgs_manage_policies_tag-policies-supported-regions"></a>

Tag policy features are available in the following Regions: 


| Region name | Region parameter | 
| --- | --- | 
| US East (N. Virginia) Region¹ | **`us-east-1`** | 
| US East (Ohio) Region | `us-east-2` | 
| US West (N. California) Region | `us-west-1` | 
| US West (Oregon) Region | `us-west-2` | 
| Africa (Cape Town) Region² | `af-south-1` | 
| Asia Pacific (Hong Kong) Region² | `ap-east-1` | 
| Asia Pacific (Taipei)² | `ap-east-2` | 
| Asia Pacific (Mumbai) Region | `ap-south-1` | 
| Asia Pacific (Hyderabad)² | `ap-south-2` | 
| Asia Pacific (Tokyo) Region | `ap-northeast-1` | 
| Asia Pacific (Seoul) Region | `ap-northeast-2` | 
| Asia Pacific (Osaka) Region | `ap-northeast-3` | 
| Asia Pacific (Singapore) Region | `ap-southeast-1` | 
| Asia Pacific (Sydney) Region | `ap-southeast-2` | 
| Asia Pacific (Jakarta) Region² | `ap-southeast-3` | 
| Asia Pacific (Melbourne)² | `ap-southeast-4` | 
| Asia Pacific (Malaysia) Region | `ap-southeast-5` | 
| Asia Pacific (New Zealand)² | `ap-southeast-6` | 
| Asia Pacific (Thailand) | `ap-southeast-7` | 
| Canada (Central) Region | `ca-central-1` | 
| Canada West (Calgary)² | `ca-west-1` | 
| China (Beijing) Region | `cn-north-1` | 
| China (Ningxia) Region | `cn-northwest-1` | 
| Europe (Frankfurt) Region | `eu-central-1` | 
| Europe (Zurich) Region² | `eu-central-2` | 
| Europe (Milan) Region² | `eu-south-1` | 
| Europe (Spain)² | `eu-south-2` | 
| Europe (Ireland) Region | `eu-west-1` | 
| Europe (London) Region | `eu-west-2` | 
| Europe (Paris) Region | `eu-west-3` | 
| Europe (Stockholm) Region | `eu-north-1` | 
| Mexico (Central) Region | `mx-central-1` | 
| Middle East (UAE) Region² | `me-central-1` | 
| Middle East (Bahrain) Region² | `me-south-1` | 
| South America (São Paulo) Region | `sa-east-1` | 
| Israel (Tel Aviv)² | `il-central-1` | 
| AWS GovCloud (US-East) | `us-gov-east-1` | 
| AWS GovCloud (US-West) | `us-gov-west-1` | 

**¹You must specify the `us-east-1` Region when calling the following Organizations operations:**
+ [DeletePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeletePolicy.html)
+ [DisablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisablePolicyType.html)
+ [EnablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html)
+ Any other operations on an organization root, such as [ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html).

**You must also specify the `us-east-1` Region when calling the following Resource Groups Tagging API operations that are part of the tag policies feature:**
+ [DescribeReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.html)
+ [GetComplianceSummary](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.html)
+ [StartReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_StartReportCreation.html)

**Note**  
To evaluate organization-wide compliance with tag policies, you must also have access to an Amazon S3 bucket in the US East (N. Virginia) Region for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/ARG/latest/userguide/tag-policies-prereqs.html#bucket-policy) in the *Tagging AWS Resources User Guide*.

²These Regions must be manually enabled. To learn more about enabling and disabling AWS Regions, see [Specify which AWS Regions your account can use](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) in the *AWS Account Management Reference Guide*. The Resource Groups console isn't available in these Regions.