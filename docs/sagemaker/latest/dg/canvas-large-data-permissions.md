# Grant Users Permissions to Use Large Data

across the ML Lifecycle

Amazon SageMaker Canvas users working with datasets larger than 10 GB in CSV format or 2.5 GB in Parquet format
require specific permissions for large data processing. These permissions are
essential for managing large-scale data throughout the machine learning lifecycle. When
datasets exceed the stated thresholds, or the application's local memory capacity, SageMaker Canvas uses
Amazon EMR Serverless for efficient processing. This applies to:

- Data Import: Importing large datasets with random or stratified sampling.
- Data Preparation: Exporting processed data from Data Wrangler in Canvas to Amazon S3,
  to a new Canvas dataset, or to a Canvas model.
- Model Building: Training models on large datasets.
- Inference: Making predictions on large datasets.
  By default, SageMaker Canvas uses EMR Serverless to run these remote jobs with the following app settings:

- Pre-Initialized capacity: Not configured
- Application limits: Maximum capacity of 400 vCPUs, max concurrent 16
  vCPUs per account, 3000 GB memory, 20000 GB disk
- Metastore configuration: AWS Glue Data Catalog
- Application logs: AWS managed storage (enabled), using an AWS owned encryption key
- Application behavior: Auto-starts on job submission and auto-stops after the application is idle for 15 minutes
  To enable these large data processing capabilities, users need the necessary permissions,
  which can be granted through the Amazon SageMaker AI domain settings. The method for granting these
  permissions depends on how your Amazon SageMaker AI domain was set up initially. We'll cover three main scenarios:

- Quick domain setup
- Custom domain setup (with public internet access/without VPC)
- Custom domain setup (with VPC and without public internet access)
  Each scenario requires specific steps to ensure that users have the required permissions to leverage
  EMR Serverless for large data processing across the entire machine learning lifecycle in SageMaker Canvas.

## Scenario 1: Quick domain setup

If you used the **Quick setup** option when creating
your SageMaker AI domain, follow these steps:

1. Navigate to the Amazon SageMaker AI domain settings:
   1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
   2. In the left navigation pane, choose **Domains**.
   3. Select your domain.
   4. Choose the **App Configurations** tab.
   5. Scroll to the **Canvas** section and choose
      **Edit**.

2. Enable large data processing:
   1. In the **Large data processing configuration** section,
      turn on **Enable EMR Serverless for large data processing**.
   2. Create or select an EMR Serverless role:
      1. Choose **Create and use a new execution role** to
         create a new IAM role that has a trust relationship with EMR Serverless
         and the [AWS
         managed policy: AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy") policy attached.
         This IAM role is assumed by Canvas to create EMR Serverless jobs.
      2. Alternatively, if you already have an execution role with a trust relationship
         for EMR Serverless, then select **Use an existing execution role**
         and choose your role from the dropdown.
         - The existing role must have a name that begins with the prefix
           `AmazonSageMakerCanvasEMRSExecutionAccess-`.
         - The role you select should also have at least the permissions described
           in the [AWS
           managed policy: AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasEMRServerlessExecutionRolePolicy") policy.
         - The role should have an EMR Serverless trust policy, as shown below:

         JSON

         ```
         `{
          "Version":"2012-10-17",
          "Statement": [
          {
          "Sid": "EMRServerlessTrustPolicy",
          "Effect": "Allow",
          "Principal": {
          "Service": "emr-serverless.amazonaws.com"
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

3. (Optional) Add Amazon S3 permissions for custom Amazon S3 buckets:
   1. The Canvas managed policy automatically grants read and write permissions for Amazon S3
      buckets with `sagemaker` or `SageMaker AI` in their names. It also grants
      read permissions for objects in custom Amazon S3 buckets with the tag `"SageMaker": "true"`.
   2. For custom Amazon S3 buckets without the required tag, add the following policy to your EMR Serverless role:
   3. JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "s3:GetObject",
    "s3:PutObject",
    "s3:DeleteObject"
    ],
    "Resource": [
    "arn:aws:s3:::*"
    ]
    }
    ]
   }`

   ```

   4. We recommend that you scope down the permissions to specific Amazon S3 buckets that you want Canvas to access.

4. Save your changes and restart your SageMaker Canvas application.

## Scenario 2: Custom domain setup

(with public internet access/without VPC)

If you created or use a custom domain, follow steps 1-3 from Scenario 1, and then
do these additional steps:

1. Add permissions for the Amazon ECR `DescribeImages` operation
   to your Amazon SageMaker AI execution role, as Canvas utilizes public Amazon ECR Docker images
   for data preparation and model training:
   1. Sign in to the AWS console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. Choose **Roles**.
   3. In the search box, search for your SageMaker AI execution role by name and select it.
   4. Add the following policy to your SageMaker AI execution role. This can be done either by adding it
      as a new inline policy or by appending the policy statement to an existing one. Note that an IAM
      role can have a maximum of 10 policies attached.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [{
    "Sid": "ECRDescribeImagesOperation",
    "Effect": "Allow",
    "Action": "ecr:DescribeImages",
    "Resource": [
    "arn:aws:ecr:*:*:repository/sagemaker-data-wrangler-emr-container",
    "arn:aws:ecr:*:*:repository/ap-dataprep-emr"
    ]
    }]
   }`

   ```

2. Save your changes and restart your SageMaker Canvas application.

## Scenario 3: Custom domain setup

(with VPC and without public internet access)

If you created or use a custom domain, follow all steps from Scenario 2, then
follow these additional steps:

1. Ensure your VPC subnets are private:
   1. Verify that the route table for your subnets doesn't have an entry mapping
      `0.0.0.0/0` to an Internet Gateway.

2. Add permissions for creating network interfaces:
   1. When using SageMaker Canvas with EMR Serverless for large-scale data processing, EMR Serverless
      requires the ability to create Amazon EC2 ENIs to enable network communication between
      EMR Serverless applications and your VPC resources.
   2. Add the following policy to your Amazon SageMaker AI execution role. This can be done either by adding
      it as a new inline policy or by appending the policy statement to an existing one. Note that an IAM
      role can have a maximum of 10 policies attached.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "AllowEC2ENICreation",
    "Effect": "Allow",
    "Action": [
    "ec2:CreateNetworkInterface"
    ],
    "Resource": [
    "arn:aws:ec2:*:*:network-interface/*"
    ],
    "Condition": {
    "StringEquals": {
    "aws:CalledViaLast": "ops.emr-serverless.amazonaws.com"
    }
    }
    }
    ]
   }`

   ```

3. (Optional) Restrict ENI creation to specific subnets:
   1. To further secure your setup by restricting the creation of ENIs to certain subnets
      within your VPC, you can tag each subnet with specific conditions.
   2. Use the following IAM policy to ensure that EMR Serverless applications can only
      create Amazon EC2 ENIs within the allowed subnets and security groups:

   ```
   {
       "Sid": "AllowEC2ENICreationInSubnetAndSecurityGroupWithEMRTags",
       "Effect": "Allow",
       "Action": [
           "ec2:CreateNetworkInterface"
       ],
       "Resource": [
           "arn:aws:ec2:*:*:subnet/*",
           "arn:aws:ec2:*:*:security-group/*"
       ],
       "Condition": {
           "StringEquals": {
               "aws:ResourceTag/KEY": "VALUE"
           }
       }
   }
   ```

4. Follow the steps on the page [Configure Amazon SageMaker Canvas in a VPC without internet access](canvas-vpc.md "canvas-vpc.md")
   to set the VPC endpoint for Amazon S3, which is required by EMR Serverless and other AWS services
   that are used by SageMaker Canvas.
5. Save your changes and restart your SageMaker Canvas application.

By following these steps, you can enable large data processing in SageMaker Canvas for various domain setups,
including those with custom VPC configurations. Remember to restart your SageMaker Canvas application after making
these changes to apply the new permissions.
