

# Common setup for Amazon SageMaker Unified Studio with TIP on Amazon EMR on EC2
<a name="emr-trusted-identity-smus-tip-common-setup"></a>

Complete the following setup steps before configuring either Full Table Access (FTA) or Fine-Grained Access Control (FGAC). These steps are shared across both use cases.

**Domain prerequisite**  
Create the Amazon SageMaker Unified Studio domain through the console **Quick setup** option with AWS IAM Identity Center (IAM Identity Center) enabled. Quick setup provisions the domain Amazon S3 bucket that trusted identity propagation and the Amazon EMR on EC2 blueprint require.

**Note**  
Amazon SageMaker Unified Studio integration with Amazon EMR on EC2 through trusted identity propagation requires Amazon EMR release 7.8.0 or later.

You need the following:
+ A Amazon SageMaker Unified Studio domain. For instructions to create a Amazon SageMaker Unified Studio domain, refer to the [quick setup guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/quick-setup.html) in the Amazon SageMaker Unified Studio documentation.

  1. The domain should be enabled with trusted identity propagation, following the instructions in [Trusted identity propagation](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/trusted-identity-propagation.html).

  1. The domain's project profile should be enabled with Amazon EMR on EC2. You can choose either **General purpose** or **Memory-Optimized profile**. You will need to provide a value for `certificateLocation`. For detailed instructions, refer to [Specify PEM certificate for EmrOnEc2 blueprint](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-emr-on-ec2-blueprint.html). You can use OpenSSL to generate a self-signed X.509 certificate with a 2048-bit RSA private key. Detailed instructions for creating one are at [Create keys and certificates for data encryption with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-encryption-certificates.html).

For a detailed walkthrough of this setup, see the blog post [Use trusted identity propagation for Apache Spark interactive sessions in Amazon SageMaker Unified Studio](https://aws.amazon.com/blogs/big-data/use-trusted-identity-propagation-for-apache-spark-interactive-sessions-in-amazon-sagemaker-unified-studio/).

## Step 1: Set up IAM Identity Center and sync users
<a name="emr-trusted-identity-smus-tip-common-idc"></a>

Create an IAM Identity Center instance and provision users. For detailed instructions, see [Creating an Identity Center instance and syncing users](emr-trusted-identity-prerequisites.md#emr-trusted-identity-create-idc-instance).

## Step 2: Set up Lake Formation
<a name="emr-trusted-identity-smus-tip-common-lf"></a>

Configure Lake Formation with IAM Identity Center integration and register your data locations. For detailed instructions, see [Set up Lake Formation](emr-trusted-identity-prerequisites.md#emr-trusted-identity-lake-formation-setup).

Additionally, configure the Lake Formation location registration role as described in the "1. AWS Lake Formation setup to configure the roles" section. To use AWS Lake Formation with Amazon EMR, create a custom role to register Amazon Simple Storage Service locations for your data source. You need to create a new custom role with Amazon S3 access. Do not use the default role, which is explained in more detail at [Setting up AWS Lake Formation with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-lf.html).

Use the following custom trust policy for the Lake Formation location registration role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "lakeformation.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```
+ If you don't already have a test data source location in Amazon S3, go to the [Amazon S3 console](https://console.aws.amazon.com/s3/) and create a new bucket. For example, you can name it `s3://tip-blog-s3-lf-` followed by your AWS account ID.
+ Navigate to the [AWS Identity and Access Management console](https://console.aws.amazon.com/iam/) and create an IAM role for Lake Formation location registration, for example `LFRole-data-access-permissions-check`. To create an IAM role:

  1. Go to **Roles** → **Create role**

  1. Select **Custom trust policy** and paste the following trust relationship:

     ```
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Effect": "Allow",
                 "Principal": {
                     "Service": [
                         "lakeformation.amazonaws.com"
                     ]
                 },
                 "Action": "sts:AssumeRole"
             }
         ]
     }
     ```

  1. Attach below policies to your newly created role:
     + The following custom Amazon S3 policy (Replace the demo bucket names with your Amazon S3 bucket names that contain underlying data, for example `s3://tip-blog-s3-lf-<your_account_id>/`):

       ```
       {
           "Version": "2012-10-17",
           "Statement": [
               {
                   "Effect": "Allow",
                   "Action": [
                       "s3:PutObject",
                       "s3:GetObject",
                       "s3:DeleteObject",
                       "s3:ListBucket"
                   ],
                   "Resource": [
                       "arn:aws:s3:::amzn-s3-demo-bucket1",
                       "arn:aws:s3:::amzn-s3-demo-bucket2/*"
                   ]
               }
           ]
       }
       ```

  1. Open the [AWS Lake Formation console](https://console.aws.amazon.com/lakeformation/).
     + From the left menu open Data lake locations under **Administration** section then **Register location**.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-data-lake-locations.png)
     + Browse the Amazon S3 path you have created
     + Attach IAM role created above `LFRole-data-access-permissions-check` that has read/write access to the chosen Amazon S3 path.
     + Choose **Lake Formation** for Permission mode and click on **Register location**.  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-data-lake-register.png)

## Step 3: Enable Trusted Identity Propagation in Amazon SageMaker Unified Studio
<a name="emr-trusted-identity-smus-tip-common-enable-tip"></a>

Enable `enableTrustedIdentityPropagationPermissions` in the Tooling blueprint parameters for your Amazon SageMaker Unified Studio domain. For detailed instructions, see [Trusted identity propagation](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/trusted-identity-propagation.html) in the *Amazon SageMaker Unified Studio Administrator Guide*.

1. Navigate to the SageMaker AI management console (this is the SageMaker AI console, not the Amazon SageMaker Unified Studio console) and choose the appropriate AWS Region.

1. Choose the domain that contains the project profile you want to update.

1. Choose the **Project profiles** tab and then choose the project profile (for example, **All capabilities**).

1. Choose **Edit**.

1. In the **Tooling blueprint parameters** section, choose the **enableTrustedIdentityPropagationPermissions** parameter and choose **Edit**.

1. Set the parameter value to **True**.

1. Choose **Save**.

## Step 4: Grant Lake Formation permissions to the IAM Identity Center user
<a name="emr-trusted-identity-smus-tip-common-lf-permissions"></a>

Grant Lake Formation permissions on the database and table to the IAM Identity Center user who will log in to Amazon SageMaker Unified Studio.

1. Open the Lake Formation console and choose **Data permissions** under **Permissions**.

1. Choose **Grant**.

1. Under **Principals**, choose **IAM Identity Center users and groups** and select your IAM Identity Center user.

1. Under **Named Data Catalog resources**, select your database. Under **Database permissions**, select **Create table** and **Describe**. Choose **Grant**.

1. Grant again, this time selecting the table. Under **Table permissions**, select **Select** and **Describe**. Choose **Grant**.

## Step 5: Create a project in Amazon SageMaker Unified Studio
<a name="emr-trusted-identity-smus-tip-common-project"></a>

1. Sign in to the Amazon SageMaker Unified Studio domain with your IAM Identity Center user credentials.

1. Create a new project using the blueprint (for example, **All capabilities**) for which `enableTrustedIdentityPropagationPermissions` is set to `true`.

1. Verify data access: as a project user, check the **Data** section to confirm you can see the database and table using the preview feature.