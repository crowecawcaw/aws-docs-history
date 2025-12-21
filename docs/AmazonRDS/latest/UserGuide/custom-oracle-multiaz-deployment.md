# Deploying RDS Custom for Oracle with AWS CloudFormation

Automate your RDS Custom for Oracle deployment using the provided AWS CloudFormation template.
Complete the following prerequisites before deploying the resources.

## Prerequisites

###### Download required Oracle files

You need specific Oracle installation files before you can create the CloudFormationtemplate. Download these files before you deploy.

1. Navigate to [Oracle Database 19c (19.3)](https://www.oracle.com/database/technologies/oracle19c-linux-downloads.html "https://www.oracle.com/database/technologies/oracle19c-linux-downloads.html")
2. Locate and download the file `LINUX.X64_193000_db_home.zip`
3. Rename the file to`V982063-01.zip`
4. Download the remaining patches, selecting **Platform or Language** as
   `Linux x86-64`

### Latest OPatch

utility

[Patch 6880880](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=6880880 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=6880880")

### January 2023 PSU

Patches

**Database PSU & RU Patches**

- [Patch 34765931](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=34765931 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=34765931")
- [Patch 34786990](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=34786990 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=34786990")

**Additional Required Patches**

- [Patch 35099667](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35099667 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35099667")
- [Patch 35099674](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35099674 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35099674")
- [Patch 28730253](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=28730253 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=28730253")
- [Patch 29213893](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=29213893 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=29213893")
- [Patch 35012866](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35012866 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35012866")

### April 2023 PSU

Patches

**Database PSU & RU Patches**

- [Patch 35042068](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35042068 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35042068")
- [Patch 35050341](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35050341 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35050341")

**Additional Required Patches**

- [Patch 28730253](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=28730253 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=28730253")
- [Patch 29213893](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=29213893 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=29213893")
- [Patch 33125873](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=33125873 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=33125873")
- [Patch 35220732](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35220732 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35220732")
- [Patch 35239280](https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35239280 "https://updates.oracle.com/Orion/PatchDetails/process_form?patch_num=35239280")

### Amazon S3 bucket setup

1. Create an Amazon S3 bucket in your AWS account, or choose an existing bucket.
2. Create a folder structure in the bucket similar to example below.

```
<bucket-name>/
└── oracle_cev/
    ├── V982063-01.zip
    ├── p6880880_190000_Linux-x86-64.zip
    ├── p34765931_190000_Linux-x86-64.zip
    ├── p34786990_190000_Linux-x86-64.zip
    ├── p35099667_190000_Linux-x86-64.zip
    ├── p35099674_190000_Generic.zip
    ├── p28730253_190000_Linux-x86-64.zip
    ├── p29213893_1918000DBRU_Generic.zip
    ├── p35012866_1918000DBRU_Linux-x86-64.zip
    ├── p35042068_190000_Linux-x86-64.zip
    ├── p35050341_190000_Linux-x86-64.zip
    ├── p29213893_1919000DBRU_Generic.zip
    ├── p33125873_1919000DBRU_Linux-x86-64.zip
    ├── p35220732_190000_Linux-x86-64.zip
    └── p35239280_190000_Generic.zip
```

3. Upload all of Oracle files that you previously downloaded to the appropriate folders.

## Deploy RDS Custom for Oracle using AWS CloudFormation

### Step 1: Prepare the CloudFormation template

Before you can deploy RDS Custom for Oracle, you need to download and configure the CloudFormation
template that creates the necessary prerequisites.

**Copy and save the template**

1. Go to [Deploying RDS Custom for Oracle with single and multiple
   Availability Zones](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.md#aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.md#aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones")
2. Copy the template in your preferred format (YAML or JSON)
3. Save the file in YAML or JSON format. For example,
   `rds-custom-oracle-prereqs.yaml`

**Launch the stack in the AWS console**

1. Open the AWS Console and navigate to AWS CloudFormation
2. Choose **Create stack** > **With new resources (standard)**
3. Select **Choose an existing template**
4. Select **Upload a template file** >
   **Choose file**
5. Select the template file you previously downloaded
6. Keep the default parameter values
7. Select **Next** to create the stack

**Alternative: Using AWS CLI**

Instead of using the console, you can create the stack using the AWS CLI:

```
aws cloudformation create-stack \
  --stack-name rds-custom-oracle \
  --template-body file://rds-custom-oracle-prereqs.yaml \
  --capabilities CAPABILITY_NAMED_IAM
```

### Step 2: Create the Custom Engine Versions

(CEVs) and Amazon RDS instances

**Copy and save the template**

1. Go to [Deploying RDS Custom for Oracle with single and multiple
   Availability Zones](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.md#aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.md#aws-resource-rds-dbinstance--examples--Deploying_RDS_Custom_for_Oracle_with_single_and_multiple_Availability_Zones")
2. Copy the template in your preferred format (YAML or JSON)
3. Update the following parameters in the template if needed:
   - `BucketName`
   - `CEVS3Prefix`
   - Database master password (replace \*\*\*\*\*\*\*\*\*\*\*\*\*)

4. Save the file in YAML or JSON format

### Step 3: Deploy using the AWS console

1. Open the AWS Console and navigate to AWS CloudFormation
2. Choose **Create stack** > **With new resources (standard)**
3. Select **Choose an existing template**
4. Select **Upload a template file** >
   **Choose file**
5. Select the template file you previously downloaded
6. Leave the parameters as default values
7. Fill in the parameters as follows:

```
BucketName: `rds-custom-id`
CEVS3Prefix: oracle_cev
CEVCreation: Yes
```

8. Review the configuration and select **Next** to create the stack

**Optional: Deploy Using AWS CLI**

```
aws cloudformation create-stack \
  --stack-name rds-custom-oracle \
  --template-body file://rds-custom-oracle.yaml \
  --parameters \
    ParameterKey=BucketName,ParameterValue=rds-custom-id \
    ParameterKey=CEVS3Prefix,ParameterValue=oracle_cev \
    ParameterKey=CEVCreation,ParameterValue=Yes \
  --capabilities CAPABILITY_NAMED_IAM
```

## Deployment resources

created

The template creates the following resources:

- Amazon VPC with public and private subnets
- Security groups
- Amazon VPC endpoints
- IAM roles and policies
- AWS KMS key for encryption
- Custom Engine Versions (CEVs)
- RDS Custom for Oracle instances for both single-AZ and multi-AZ configurations

## Monitor your deployment progress

After you create the CloudFormation stack, monitor its progress to ensure successful deployment.
The deployment process includes creating Custom Engine Versions (CEVs) and RDS instances.

To monitor deployment progress:

1. Open the CloudFormation console.
2. Choose your stack name.
3. Choose the **Events** tab to view progress and identify any errors.

###### Note

CEV creation typically requires 2-3 hours. After CEV creation completes successfully,
Amazon RDS automatically begins creating the Amazon RDS instance.

## Post-Deployment

After the stack creation process completes, perform the following post-deployment verification and configuration steps:

1. From the Amazon RDS console page, navigate to **Custom engine
   versions** to verify CEV creation.
2. Confirm Amazon RDS instances are created and available
3. Test connectivity to the Amazon RDS instances
4. Set up monitoring and backup strategies as needed

## Cleanup

To remove all resources, run the following AWS CLI command:

```
aws cloudformation delete-stack --stack-name rds-custom-oracle
```

## Troubleshooting

If you encounter issues during deployment, use the following solutions to resolve common problems.

CEV creation fails

- Verify all required patches are uploaded to Amazon S3
- Check IAM permissions
- Verify the patch versions are correct; see the [Prerequisites](#custom-oracle-prerequisites "#custom-oracle-prerequisites")
  for the list of required patches.

Amazon RDS instance creation fails

- Check VPC/subnet configurations
- Verify security group rules
- Confirm CEV is available
