

# Step 3: Attach a policy to users or groups that access AWS Glue
<a name="attach-policy-iam-user"></a>

The administrator must assign permissions to any users, groups, or roles using the AWS Glue console or AWS Command Line Interface (AWS CLI). You provide those permissions by using AWS Identity and Access Management (IAM), through policies. This step describes assigning permissions to users or groups.

When you finish this step, your user or group has the following policies attached:
+ The AWS managed policy `AWSGlueConsoleFullAccess` or the custom policy **GlueConsoleAccessPolicy**
+ **`AWSGlueConsoleSageMakerNotebookFullAccess`**
+ **`CloudWatchLogsReadOnlyAccess`**
+ **`AWSCloudFormationReadOnlyAccess`**
+ **`AmazonAthenaFullAccess`**

**To attach an inline policy and embed it in a user or group**

You can attach an AWS managed policy or an inline policy to a user or group to access the AWS Glue console. Some of the resources specified in this policy refer to default names that are used by AWS Glue for Amazon S3 buckets, Amazon S3 ETL scripts, CloudWatch Logs, CloudFormation, and Amazon EC2 resources. For simplicity, AWS Glue writes some Amazon S3 objects into buckets in your account prefixed with `aws-glue-*` by default. 
**Note**  
You can skip this step if you use the AWS managed policy **`AWSGlueConsoleFullAccess`**.
**Important**  
AWS Glue needs permission to assume a role that is used to perform work on your behalf. **To accomplish this, you add the `iam:PassRole` permissions to your AWS Glue users or groups.** This policy grants permission to roles that begin with `AWSGlueServiceRole` for AWS Glue service roles, and `AWSGlueServiceNotebookRole` for roles that are required when you create a notebook server. You can also create your own policy for `iam:PassRole` permissions that follows your naming convention.  
Per security best practices, it is recommended to restrict access by tightening policies to further restrict access to Amazon S3 bucket and Amazon CloudWatch log groups. For an example Amazon S3 policy, see [Writing IAM Policies: How to Grant Access to an Amazon S3 Bucket](https://aws.amazon.com/blogs/security/writing-iam-policies-how-to-grant-access-to-an-amazon-s3-bucket/). 

In this step, you create a policy that is similar to `AWSGlueConsoleFullAccess`. You can find the most current version of `AWSGlueConsoleFullAccess` on the IAM console.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Users** or **User groups**.

1. In the list, choose the name of the user or group to embed a policy in.

1. Choose the **Permissions** tab and, if necessary, expand the **Permissions policies** section.

1. Choose the **Add Inline policy** link.

1. On the **Create Policy** screen, navigate to a tab to edit JSON. Create a policy document with the following JSON statements, and then choose **Review policy**.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "glue:*",
           "redshift:DescribeClusters",
           "redshift:DescribeClusterSubnetGroups",
           "iam:ListRoles",
           "iam:ListUsers",
           "iam:ListGroups",
           "iam:ListRolePolicies",
           "iam:GetRole",
           "iam:GetRolePolicy",
           "iam:ListAttachedRolePolicies",
           "ec2:DescribeSecurityGroups",
           "ec2:DescribeSubnets",
           "ec2:DescribeVpcs",
           "ec2:DescribeVpcEndpoints",
           "ec2:DescribeRouteTables",
           "ec2:DescribeVpcAttribute",
           "ec2:DescribeKeyPairs",
           "ec2:DescribeInstances",
           "rds:DescribeDBInstances",
           "rds:DescribeDBClusters",
           "rds:DescribeDBSubnetGroups",
           "s3:ListAllMyBuckets",
           "s3:ListBucket",
           "s3:GetBucketAcl",
           "s3:GetBucketLocation",
           "cloudformation:DescribeStacks",
           "cloudformation:GetTemplateSummary",
           "dynamodb:ListTables",
           "kms:ListAliases",
           "kms:DescribeKey",
           "cloudwatch:GetMetricData",
           "cloudwatch:ListDashboards"
         ],
         "Resource": [
           "*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "s3:GetObject",
           "s3:PutObject"
         ],
         "Resource": [
           "arn:aws:s3:::*/*aws-glue-*/*",
           "arn:aws:s3:::aws-glue-*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "tag:GetResources"
         ],
         "Resource": [
           "*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "s3:CreateBucket",
           "s3:PutBucketPublicAccessBlock"
         ],
         "Resource": [
           "arn:aws:s3:::aws-glue-*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "logs:GetLogEvents"
         ],
         "Resource": [
           "arn:aws:logs:*:*:/aws-glue/*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "cloudformation:CreateStack",
           "cloudformation:DeleteStack"
         ],
         "Resource": "arn:aws:cloudformation:*:*:stack/aws-glue*/*"
       },
       {
         "Effect": "Allow",
         "Action": [
           "ec2:RunInstances"
         ],
         "Resource": [
           "arn:aws:ec2:*:*:instance/*",
           "arn:aws:ec2:*:*:key-pair/*",
           "arn:aws:ec2:*:*:image/*",
           "arn:aws:ec2:*:*:security-group/*",
           "arn:aws:ec2:*:*:network-interface/*",
           "arn:aws:ec2:*:*:subnet/*",
           "arn:aws:ec2:*:*:volume/*"
         ]
       },
       {
         "Action": [
           "iam:PassRole"
         ],
         "Effect": "Allow",
         "Resource": "arn:aws:iam::*:role/AWSGlueServiceRole*",
         "Condition": {
           "StringLike": {
             "iam:PassedToService": [
               "glue.amazonaws.com"
             ]
           }
         }
       },
       {
         "Action": [
           "iam:PassRole"
         ],
         "Effect": "Allow",
         "Resource": "arn:aws:iam::*:role/AWSGlueServiceNotebookRole*",
         "Condition": {
           "StringLike": {
             "iam:PassedToService": [
               "ec2.amazonaws.com"
             ]
           }
         }
       },
       {
         "Action": [
           "iam:PassRole"
         ],
         "Effect": "Allow",
         "Resource": [
           "arn:aws:iam::*:role/service-role/AWSGlueServiceRole*"
         ],
         "Condition": {
           "StringLike": {
             "iam:PassedToService": [
               "glue.amazonaws.com"
             ]
           }
         }
       }
     ]
   }
   ```

------

   The following table describes the permissions granted by this policy.


<table>
<thead>
  <tr><th><b>Action</b></th><th><b>Resource</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><code>"glue:*"</code></td><td><code>"*"</code></td><td>Grants permission to run all AWS Glue API operations. <br />If you had previously created your policy without the <code>"glue:*"</code> action, you must add the following individual permissions to your policy:<ul><li> "glue:ListCrawlers" </li><li> "glue:BatchGetCrawlers" </li><li> "glue:ListTriggers" </li><li> "glue:BatchGetTriggers" </li><li> "glue:ListDevEndpoints" </li><li> "glue:BatchGetDevEndpoints" </li><li> "glue:ListJobs" </li><li> "glue:BatchGetJobs" </li></ul></td></tr>
  <tr><td><code>"redshift:DescribeClusters", "redshift:DescribeClusterSubnetGroups"</code></td><td><code>"*"</code></td><td>Allows creation of connections to Amazon Redshift.</td></tr>
  <tr><td><code>"iam:ListRoles", "iam:ListRolePolicies", "iam:GetRole", "iam:GetRolePolicy", "iam:ListAttachedRolePolicies"</code></td><td><code>"*"</code></td><td>Allows listing IAM roles when working with crawlers, jobs, development endpoints, and notebook servers.</td></tr>
  <tr><td><code>"ec2:DescribeSecurityGroups", "ec2:DescribeSubnets", "ec2:DescribeVpcs", "ec2:DescribeVpcEndpoints", "ec2:DescribeRouteTables", "ec2:DescribeVpcAttribute", "ec2:DescribeKeyPairs", "ec2:DescribeInstances"</code></td><td><code>"*"</code></td><td>Allows setup of Amazon EC2 network items, such as VPCs, when running jobs, crawlers, and development endpoints.</td></tr>
  <tr><td><code>"rds:DescribeDBInstances"</code></td><td><code>"*"</code></td><td>Allows creation of connections to Amazon RDS.</td></tr>
  <tr><td><code>"s3:ListAllMyBuckets", "s3:ListBucket", "s3:GetBucketAcl", "s3:GetBucketLocation"</code></td><td><code>"*"</code></td><td>Allows listing of Amazon S3 buckets when working with crawlers, jobs, development endpoints, and notebook servers.</td></tr>
  <tr><td><code>"dynamodb:ListTables"</code></td><td><code>"*"</code></td><td>Allows listing of DynamoDB tables.</td></tr>
  <tr><td><code>"kms:ListAliases", "kms:DescribeKey"</code></td><td><code>"*"</code></td><td>Allows working with KMS keys.</td></tr>
  <tr><td><code>"cloudwatch:GetMetricData", "cloudwatch:ListDashboards"</code></td><td><code>"*"</code></td><td>Allows working with CloudWatch metrics.</td></tr>
  <tr><td><code>"s3:GetObject", "s3:PutObject"</code></td><td><code>"arn:aws:s3::: aws-glue-*/*", "arn:aws:s3::: */*aws-glue-*/*", "arn:aws:s3::: aws-glue-*"</code></td><td>Allows get and put of Amazon S3 objects into your account when storing objects such as ETL scripts and notebook server locations. <br />Naming convention: Grants permission to Amazon S3 buckets or folders whose names are prefixed with <b>aws-glue-</b>. </td></tr>
  <tr><td><code>"tag:GetResources"</code></td><td><code>"*"</code></td><td>Allows retrieval of AWS tags.</td></tr>
  <tr><td><code>"s3:CreateBucket", "s3:PutBucketPublicAccessBlock"</code></td><td><code>"arn:aws:s3::: aws-glue-*"</code></td><td>Allows creation of an Amazon S3 bucket into your account when storing objects such as ETL scripts and notebook server locations. <br />Naming convention: Grants permission to Amazon S3 buckets whose names are prefixed with <b>aws-glue-</b>.<br />Enables AWS Glue to create buckets that block public access.</td></tr>
  <tr><td><code>"logs:GetLogEvents"</code></td><td><code>"arn:aws:logs:*:*: /aws-glue/*"</code></td><td>Allows retrieval of CloudWatch Logs. <br />Naming convention: AWS Glue writes logs to log groups whose names begin with <b>aws-glue-</b>.</td></tr>
  <tr><td><code>"cloudformation:CreateStack", "cloudformation:DeleteStack"</code></td><td><code>"arn:aws:cloudformation:*:*:stack/ aws-glue*/*"</code></td><td>Allows managing CloudFormation stacks when working with notebook servers. <br />Naming convention: AWS Glue creates stacks whose names begin with <b>aws-glue</b>.</td></tr>
  <tr><td><code>"ec2:RunInstances"</code></td><td><code>"arn:aws:ec2:*:*:instance/*", "arn:aws:ec2:*:*:key-pair/*", "arn:aws:ec2:*:*:image/*", "arn:aws:ec2:*:*:security-group/*", "arn:aws:ec2:*:*:network-interface/*", "arn:aws:ec2:*:*:subnet/*", "arn:aws:ec2:*:*:volume/*"</code></td><td>Allows running of development endpoints and notebook servers.</td></tr>
  <tr><td><code>"iam:PassRole"</code></td><td><code>"arn:aws:iam::*:role/ AWSGlueServiceRole*"</code></td><td>Allows AWS Glue to assume <code>PassRole</code> permission for roles that begin with <code>AWSGlueServiceRole</code>.</td></tr>
  <tr><td><code>"iam:PassRole"</code></td><td><code>"arn:aws:iam::*:role/ AWSGlueServiceNotebookRole*"</code></td><td>Allows Amazon EC2 to assume <code>PassRole</code> permission for roles that begin with <code>AWSGlueServiceNotebookRole</code>.</td></tr>
  <tr><td><code>"iam:PassRole"</code></td><td><code>"arn:aws:iam::*:role/service-role/ AWSGlueServiceRole*"</code></td><td>Allows AWS Glue to assume <code>PassRole</code> permission for roles that begin with <code>service-role/AWSGlueServiceRole</code>.</td></tr>
</tbody>
</table>


1. On the **Review policy** screen, enter a name for the policy, for example **GlueConsoleAccessPolicy**. When you're satisfied with the policy, choose **Create policy**. Ensure that no errors appear in a red box at the top of the screen. Correct any that are reported.
**Note**  
If **Use autoformatting** is selected, the policy is reformatted whenever you open a policy or choose **Validate Policy**.

**To attach the AWSGlueConsoleFullAccess managed policy**

You can attach the `AWSGlueConsoleFullAccess` policy to provide permissions that are required by the AWS Glue console user.
**Note**  
You can skip this step if you created your own policy for AWS Glue console access.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. In the list of policies, select the check box next to the **AWSGlueConsoleFullAccess**. You can use the **Filter** menu and the search box to filter the list of policies.

1. Choose **Policy actions**, and then choose **Attach**.

1. Choose the user to attach the policy to. You can use the **Filter** menu and the search box to filter the list of principal entities. After choosing the user to attach the policy to, choose **Attach policy**.

**To attach the `AWSGlueConsoleSageMakerNotebookFullAccess` managed policy**

You can attach the `AWSGlueConsoleSageMakerNotebookFullAccess` policy to a user to manage SageMaker AI notebooks created on the AWS Glue console. In addition to other required AWS Glue console permissions, this policy grants access to resources needed to manage SageMaker AI notebooks. 

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**. 

1. In the list of policies, select the check box next to the **AWSGlueConsoleSageMakerNotebookFullAccess**. You can use the **Filter** menu and the search box to filter the list of policies.

1. Choose **Policy actions**, and then choose **Attach**.

1. Choose the user to attach the policy to. You can use the **Filter** menu and the search box to filter the list of principal entities. After choosing the user to attach the policy to, choose **Attach policy**.

**To attach the CloudWatchLogsReadOnlyAccess managed policy**

You can attach the **CloudWatchLogsReadOnlyAccess** policy to a user to view the logs created by AWS Glue on the CloudWatch Logs console.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**. 

1. In the list of policies, select the check box next to the **CloudWatchLogsReadOnlyAccess**. You can use the **Filter** menu and the search box to filter the list of policies.

1. Choose **Policy actions**, and then choose **Attach**.

1. Choose the user to attach the policy to. You can use the **Filter** menu and the search box to filter the list of principal entities. After choosing the user to attach the policy to, choose **Attach policy**.

**To attach the AWSCloudFormationReadOnlyAccess managed policy**

You can attach the **AWSCloudFormationReadOnlyAccess** policy to a user to view the CloudFormation stacks used by AWS Glue on the CloudFormation console.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**. 

1. In the list of policies, select the check box next to **AWSCloudFormationReadOnlyAccess**. You can use the **Filter** menu and the search box to filter the list of policies.

1. Choose **Policy actions**, and then choose **Attach**.

1. Choose the user to attach the policy to. You can use the **Filter** menu and the search box to filter the list of principal entities. After choosing the user to attach the policy to, choose **Attach policy**.

**To attach the AmazonAthenaFullAccess managed policy**

You can attach the **AmazonAthenaFullAccess** policy to a user to view Amazon S3 data in the Athena console.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**. 

1. In the list of policies, select the check box next to the **AmazonAthenaFullAccess**. You can use the **Filter** menu and the search box to filter the list of policies.

1. Choose **Policy actions**, and then choose **Attach**.

1. Choose the user to attach the policy to. You can use the **Filter** menu and the search box to filter the list of principal entities. After choosing the user to attach the policy to, choose **Attach policy**.