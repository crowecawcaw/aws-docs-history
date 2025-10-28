# Create the Infrastructure

This procedure utilizes the High availability two-tier stack CT followed by the Create S3 storage CT.

Gathering the following data before you begin will make the deployment go more quickly.

REQUIRED DATA HA STACK:

- **AutoScalingGroup**:
  - **UserData**: This value is provided in this tutorial. It includes commands to set up the resource for CodeDeploy and start the CodeDeploy agent.
  - **AMI-ID**: This value determines the operating system of EC2 instances your Auto Scaling group (ASG) will spin up. Select an AMI in your account
    that starts with "customer-" and is of the operating system that you want. Find AMI IDs in the AMS Console VPCs -> VPCs details page. This walkthrough is for ASGs configured to
    use an Amazon Linux or RHEL AMI.

- **Database**:
  - These parameters, **DBEngine**, **EngineVersion**, and **LicenseModel** should be set according to your situation
    though the values shown in the example have been tested. The tutorial uses these values, respectively: `MySQL`, `8.0.16`,
    `general-public-license`.
  - These parameters, **DBName**, **MasterUserPassword**, and **MasterUsername** are
    required when deploying the application bundle. The tutorial uses these values, respectively: `wordpressDB`, `p4ssw0rd`,
    `admin`. Note that DBName can only contain alphanumeric characters.
  - When you enter the **MasterUsername** for the RDS DB, it will appear in cleartext, so log in to the database as soon as possible and change the
    password to ensure your security.
  - For **RDSSubnetIds**, use two Private subnets. Enter them one at a time pressing "Enter" after each. Find Subnet IDs with
    the For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (CLI: list-subnet-summaries) or in the AMS Console VPCs -> VPC details page.

- **LoadBalancer**:
  - Set this parameter, **Public** to **true** because the tutorial uses Public ELB subnets.
  - **ELBSubnetIds**: Use two Public subnets. Enter them one at a time pressing "Enter" after each. Find Subnet IDs with the
    For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (CLI: list-subnet-summaries) or in the AMS Console VPCs -> VPC details page.

- **Application**: The **ApplicationName** value sets the CodeDeploy application name and CodeDeploy deployment group name. You use it
  to deploy your application. It must be unique in the account. To check your account for CodeDeploy names, see the CodeDeploy Console. The example uses
  `WordPress` but, if you will use that value, make sure that it is not already in use.

1. Launch the high availability stack.
   1. On the **Create RFC** page, select the category **Deployment**,
      subcategory **Standard Stacks**, item **High availability two-tier stack** and operation **Create**,
      from the list.
   2. IMPORTANT: Choose **Advanced** and set the values as shown.

   You only need to enter values for starred (\*) options, tested values are shown in the example; you can leave not-required empty options blank. 3. For the **RFC Description** section:

   ```
   **Subject**: WP-HA-2-Tier-RFC
   ```

   4. For the **Resource information** section, set parameters for **AutoScalingGroup**, **Database**,
      **LoadBalancer**, **Application**, and **Tags**.

   Also, the purpose of the "AppName" tag key is so you can easily search for the ASG instances in the EC2 console; you can call this tag key "Name" or any other
   key name that you want. Note that you can add up to 50 tags.

   ```
   **UserData**:
       #!/bin/bash
       REGION=$(curl 169.254.169.254/latest/meta-data/placement/availability-zone/ | sed 's/[a-z]$//')
       yum -y install ruby httpd
       chkconfig httpd on
       service httpd start
       touch /var/www/html/status
       cd /tmp
       curl -O https://aws-codedeploy-$REGION.s3.amazonaws.com/latest/install
       chmod +x ./install
       ./install auto
       chkconfig codedeploy-agent on
       service codedeploy-agent start
   **AmiId**:               `AMI-ID`
   **Description**:         WP-HA-2-Tier-Stack

   **Database**:
       **LicenseModel**:    general-public-license (USE RADIO BUTTON)
       **EngineVersion**:   8.0.16
       **DBEngine**:        MySQL
       **RDSSubnetIds**:    `PRIVATE_AZ1 PRIVATE_AZ2` (ENTER ONE AT A TIME PRESSING "ENTER" AFTER EACH)
       **MasterUserPassword**:  p4ssw0rd
       **MasterUsername**:      `admin`
       **DBName**:              `wordpressDB`

   **LoadBalancer**:
       **Public**:              true (USE RADIO BUTTON)
       **ELBSubnetIds**:        `PUBLIC_AZ1 PUBLIC_AZ2`

   **Application**:
       **ApplicationName**:     WordPress

   **Tags**:
       **Name**:                WP-Rhel-Stack
   ```

   5. Click **Submit** when finished.

2. Log in to the database that you created and change the password.
3. Launch an S3 bucket Stack.

Gathering the following data before you begin will make the deployment go more quickly.

REQUIRED DATA S3 BUCKET:

    * **VPC-ID**: This value determines where your S3 Bucket will be. Find VPC IDs with the For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (CLI: list-vpc-summaries)
     or in the AMS Console VPCs page.
    * **BucketName**: This value sets the S3 Bucket name, you use it to upload your application bundle. It must be unique across the region of the account
     and cannot include upper-case letters. Including your account ID as part of the BucketName is not a requirement but makes it easier to identify the bucket later.
     To see what S3 bucket names exist in the account, go to the Amazon S3 Console for your account.
    1. On the **Create RFC** page, select the category **Deployment**,
     subcategory **Advanced Stack Components**, item **S3 storage**, and operation **Create** from the RFC CT
     pick list.
    2. Keep the default **Basic** option and set the values as shown.



    ```
    **Subject**:              S3-Bucket-WP-HA-RFC
    **Description**:          S3BucketForWordPressBundles
    **BucketName**:           `ACCOUNT_ID-BUCKET_NAME`
    **AccessControl**:        Private
    **VpcId**:                `VPC_ID`
    **Name**:                 S3-Bucket-WP-HA-Stack
    **TimeoutInMinutes**:     60
    ```
    3. Click **Submit** when finished. The bucket deployed with this change type allows full read/write access to the whole account.
