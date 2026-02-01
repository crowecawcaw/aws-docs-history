• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Creating a custom service role to export

diagnosis reports to S3

When you are viewing filtered or unfiltered lists of managed nodes for your AWS
organization or account in the Systems Manager **Explore nodes** page, you
can export the list as a report to an Amazon S3 bucket as a `CSV` file.

To do so, you must specify a service role with the necessary permissions and trust
policy for the operation. You can choose for Systems Manager to create the role for you during
the process of downloading the report. Optionally, you can create the role and its
required policy yourself.

###### To create a custom service role to export diagnosis reports to S3

1. Follow the steps in [Creating policies using the JSON editor](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") in the
   _IAM User Guide_.
   - Use the following for the policy content, making sure to replace
     the `placeholder values` with your own
     information.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "s3:GetObject",
    "s3:PutObject"
    ],
    "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
    "Condition": {
    "StringEquals": {
    "aws:ResourceAccount": "`111122223333`"
    }
    }
    },
    {
    "Effect": "Allow",
    "Action": [
    "s3:GetBucketAcl",
    "s3:ListBucket",
    "s3:PutLifecycleConfiguration",
    "s3:GetLifecycleConfiguration"
    ],
    "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
    "Condition": {
    "StringEquals": {
    "aws:ResourceAccount": "`111122223333`"
    }
    }
    },
    {
    "Effect": "Allow",
    "Action": [
    "ssm:ListNodes"
    ],
    "Resource": "*"
    }
    ]
   }`

   ```

   - Give the policy a name to help you recognize it easily in the next
     step.

2. Follow the steps in [Creating an
   IAM role using a custom trust policy (console)](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the
   _IAM User Guide_.
   - For step 4, enter the following trust policy, making sure to
     replace the `placeholder values` with your
     own information.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "SSMAssumeRole",
    "Effect": "Allow",
    "Principal": {
    "Service": "ssm.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
    "StringEquals": {
    "aws:SourceAccount": "`111122223333`"
    }
    }
    }
    ]
   }`

   ```

3. For step 10, choose **Step 2: Add permissions** and
   select the name of the policy you created in the previous step.
   After you create the role, you can select it when following the steps in [Downloading or exporting a managed node
   report](explore-nodes-download-report.md "explore-nodes-download-report.md").
