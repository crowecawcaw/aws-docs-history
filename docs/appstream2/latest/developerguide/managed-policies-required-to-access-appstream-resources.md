

# AWS Managed Policies Required to Access WorkSpaces Applications Resources
<a name="managed-policies-required-to-access-appstream-resources"></a>

To provide full administrative or read-only access to WorkSpaces Applications, you must attach one of the following AWS managed policies to the IAM users or groups that require those permissions. An *AWS managed policy* is a standalone policy that is created and administered by AWS. For more information, see [AWS Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

**Note**  
In AWS, IAM roles are used to grant permissions to an AWS service so it can access AWS resources. The policies that are attached to the role determine which AWS resources the service can access and what it can do with those resources. For WorkSpaces Applications, in addition to having the permissions defined in the **AmazonAppStreamFullAccess** policy, you must also have the required roles in your AWS account. For more information, see [Roles Required for WorkSpaces Applications, Application Auto Scaling, and AWS Certificate Manager Private CA](roles-required-for-appstream.md).

**AmazonAppStreamFullAccess**  
This managed policy provides full administrative access to WorkSpaces Applications resources. To manage WorkSpaces Applications resources and perform API actions through the AWS Command Line Interface (AWS CLI), AWS SDK, or AWS Management Console, you must have the permissions defined in this policy.  
If you sign into the WorkSpaces Applications console as an IAM user, you must attach this policy to your AWS account. If you sign in through console federation, you must attach this policy to the IAM role that was used for federation.  
To view the permissions for this policy, see [AmazonAppStreamFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAppStreamFullAccess.html).

**AmazonAppStreamReadOnlyAccess**  
This identity-based policy grants users read-only permissions to view and monitor WorkSpaces Applications resources and related service configurations. Users can access the WorkSpaces Applications console to view streaming applications, fleet status, usage reports, and associated resources, but cannot make any changes. The policy also includes necessary read permissions for supporting services like IAM, Application Auto Scaling, and CloudWatch to enable comprehensive monitoring and reporting capabilities.  
To view the permissions for this policy, see [AmazonAppStreamReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAppStreamReadOnlyAccess.html).

The WorkSpaces Applications console uses an additional action that provides functionality that is not available through the AWS CLI or AWS SDK. The **AmazonAppStreamFullAccess** and **AmazonAppStreamReadOnlyAccess** policies both provide permissions for the following action.


| Action | Description | Access Level | 
| --- | --- | --- | 
| DescribeImageBuilders | Grants permission to retrieve a list that describes one or more specified image builders, if the image builder names are provided. Otherwise, all image builders in the account are described. | Read | 

**AmazonAppStreamPCAAccess**  
This managed policy provides full administrative access to AWS Certificate Manager Private CA resources in your AWS account for certificate-based authentication.  
To view the permissions for this policy, see [AmazonAppStreamPCAAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAppStreamPCAAccess.html).

**AmazonAppStreamServiceAccess**  
This managed policy is the default policy for the WorkSpaces Applications service role.   
This role permissions policy allows WorkSpaces Applications to complete the following actions:  
+ When using subnets in your account for your WorkSpaces Applications fleets, WorkSpaces Applications is able to describe subnets, VPCs, and availability zones, as well as create and manage the lifecycle of all elastic network interfaces associated with the fleet instances in those subnets. This also includes being able to attach Security Groups and IP addresses from those subnets to those elastic network interfaces.
+ When using features such as UPP and HomeFolders, WorkSpaces Applications is able to create and manage Amazon S3 buckets, objects and their lifecyles, policies, and encryption configuration in the account. These buckets include the following naming prefixes:
  + `"arn:aws:s3:::appstream2-36fb080bb8-",`
  + `"arn:aws:s3:::appstream-app-settings-",`
  + `"arn:aws:s3:::appstream-logs-"`
To view the permissions for this policy, see [AmazonAppStreamServiceAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAppStreamServiceAccess.html).

**ApplicationAutoScalingForAmazonAppStreamAccess**  
This managed policy enables application autoscaling for WorkSpaces Applications.  
To view the permissions for this policy, see [ApplicationAutoScalingForAmazonAppStreamAccess ](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ApplicationAutoScalingForAmazonAppStreamAccess.html).

**AWSApplicationAutoscalingAppStreamFleetPolicy**  
This managed policy grants permissions for Application Auto Scaling to access WorkSpaces Applications and CloudWatch .  
To view the permissions for this policy, see [AWSApplicationAutoscalingAppStreamFleetPolicy ](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationAutoscalingAppStreamFleetPolicy.html).

## WorkSpaces Applications updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for WorkSpaces Applications since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document History for Amazon WorkSpaces Applications](doc-history.md) page.




| Change | Description | Date | 
| --- | --- | --- | 
| AmazonAppStreamServiceAccess – Change |  Added allow permissions for `"ec2:DescribeImages"` to the policy JSON policy document | November 17, 2025 | 
| AmazonAppStreamReadOnlyAccess – Change |  Removed `"appstream:Get*",` from the JSON policy document | October 22, 2025 | 
| WorkSpaces Applications started tracking changes | WorkSpaces Applications started tracking changes for its AWS managed policies | October 31, 2022 | 