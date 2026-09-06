

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/). 

# Identity and Access Management in Amazon Cloud Directory
<a name="iam_auth_access"></a>

Access to Amazon Cloud Directory requires credentials that AWS can use to authenticate your requests. Those credentials must have permissions to access AWS resources. The following sections provide details on how you can use [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) and Cloud Directory to help secure your resources by controlling who can access them:

 
+ [Authentication](#authentication)
+ [Access Control](#iam_auth_access_accesscontrol)

## Authentication
<a name="authentication"></a>

Learn how to access AWS using [IAM identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html).

## Access Control
<a name="iam_auth_access_accesscontrol"></a>

You can have valid credentials to authenticate your requests, but unless you have permissions you cannot create or access Cloud Directory resources. For example, you must have permissions to create an Amazon Cloud Directory.

The following sections describe how to manage permissions for Cloud Directory. We recommend that you read the overview first.

 
+ [Overview of Managing Access Permissions to Your Cloud Directory Resources](iam_auth_access_accesscontrol_overview.md)
+  [Using Identity-Based Policies (IAM Policies) for Cloud Directory](iam_auth_access_accesscontrol_identitybased.md) 
+  [Amazon Cloud Directory API Permissions: Actions, Resources, and Conditions Reference](iam_auth_access_usingwith_iam_resourcepermissions.md) 