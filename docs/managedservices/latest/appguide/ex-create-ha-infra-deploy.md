# Create the Infrastructure

Gathering the following data before you begin will make the deployment go more quickly.

REQUIRED DATA HA STACK:

- AutoScalingGroup:
  - `UserData`: This value is provided in this tutorial. It includes commands to set up the resource for CodeDeploy and start the CodeDeploy agent.
  - `AMI-ID`: This value determines what kind of EC2 instances your Auto Scaling group (ASG) will spin up. Be sure to select an AMI in your account
    that starts with "customer-" and is of the operating system that you want. Find AMI IDs with the For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (CLI: list-amis) or in
    the AMS Console VPCs -> VPCs details page. This walkthrough is for ASGs configured to use a Linux AMI.

- Database:
  - These parameters, `DBEngine`, `EngineVersion`, and `LicenseModel` should be set according to your situation
    though the values shown in the example have been tested.
  - These parameters, `RDSSubnetIds`, `DBName`, `MasterUsername`, and `MasterUserPassword` are
    required when deploying the application bundle. For RDSSubnetIds, use two Private subnets.

- LoadBalancer:
  - These parameters, `DBEngine`, `EngineVersion`, and `LicenseModel` should be set according to your situation
    though the values shown in the example have been tested.
  - `ELBSubnetIds`: Use two Public subnets.

- Application: The `ApplicationName` value sets the CodeDeploy application name and CodeDeploy deployment group name. You use it to deploy your
  application. It must be unique in the account. To check your account for CodeDeploy names, see the CodeDeploy Console. The example uses "WordPress" but, if
  you will use that value, make sure that it is not already in use.
  This procedure utilizes the High availability two-tier stack (advanced) CT (ct-06mjngx5flwto) and the Create S3 storage CT (ct-1a68ck03fn98r). From your
  authenticated account, follow these steps at the command line.

1. Launch the infrastructure stack.
   1. Output the execution parameters JSON schema for the HA two tier stack CT to a file in your current folder named CreateStackParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-06mjngx5flwto" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateStackParams.json
   ```

   2. Modify the schema. Replace the `variables` as appropriate. For example, use the OS that you want for the EC2 instances the ASG will create.
      Record the `ApplicationName` as you will use it later to deploy the application. Note that you can add up to 50 tags.

   ```
   {
   "Description":      "HA two tier stack for WordPress",
   "Name":             "WordPressStack",
   "TimeoutInMinutes":  360,
   "Tags": [
           {
               "Key": "ApplicationName",
               "Value": "WordPress"
           }
       ],
   "AutoScalingGroup": {
               "AmiId":    "`AMI-ID`",
               "UserData": "#!/bin/bash \n
               REGION=$(curl 169.254.169.254/latest/meta-data/placement/availability-zone/ | sed 's/[a-z]$//') \n
               yum -y install ruby httpd \n
               chkconfig httpd on \n
               service httpd start \n
               touch /var/www/html/status \n
               cd /tmp \n
               curl -O https://aws-codedeploy-$REGION.s3.amazonaws.com/latest/install \n
               chmod +x ./install \n
               ./install auto \n
               chkconfig codedeploy-agent on \n
               service codedeploy-agent start"
       },
       "LoadBalancer": {
           "Public":               true,
           "HealthCheckTarget":    "HTTP:80/status"
       },
       "Database":     {
           "DBEngine":             "MySQL",
           "DBName":               "wordpress",
           "EngineVersion":        "8.0.16 ",
           "LicenseModel":         "general-public-license",
           "MasterUsername":       "admin",
           "MasterUserPassword":   "p4ssw0rd"
       },
       "Application":  {
       "ApplicationName":  "WordPress"
           }
   }
   ```

   3. Output the CreateRfc JSON template to a file in your current folder named CreateStackRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateStackRfc.json
   ```

   4. Modify the RFC template as follows and save it, you can delete and replace the contents. Note that
      `RequestedStartTime` and `RequestedEndTime` are now optional; excluding them creates an ASAP RFC
      that executes as soon as it is approved (which usually happens automatically). To submit a scheduled RFC, add those values.

   ```
   {
   "ChangeTypeVersion":    "3.0",
   "ChangeTypeId":         "ct-06mjngx5flwto",
   "Title":                "HA-Stack-For-WP-RFC"
   }
   ```

   5. Create the RFC, specifying the CreateStackRfc.json file and the CreateStackParams.json execution parameters file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateStackRfc.json --execution-parameters file://CreateStackParams.json
   ```

   You receive the RFC ID in the response. Save the ID for subsequent steps. 6. Submit the RFC:

   ```
   aws amscm submit-rfc --rfc-id  RFC_ID
   ```

   If the RFC succeeds, you receive no output. 7. To check RFC status, run

   ````
   aws amscm get-rfc --rfc-id `RFC_ID`
   ```Keep note of the RFC ID.
   ````

2. Launch an S3 bucket

Gathering the following data before you begin will make the deployment go more quickly.

REQUIRED DATA S3 BUCKET:

    * `VPC-ID`: This value determines where your S3 Bucket will be. Use the same VPC ID that you used previously.
    * `BucketName`: This value sets the S3 Bucket name, you use it to upload your application bundle. It must be unique across the region of the account
     and cannot include upper-case letters. Including your account ID as part of the BucketName is not a requirement but makes it easier to identify the bucket later.
     To see what S3 bucket names exist in the account, go to the Amazon S3 Console for your account.
    1. Output the execution parameters JSON schema for the S3 storage create CT to a JSON file named CreateS3StoreParams.json.



    ```
    aws amscm get-change-type-version --change-type-id "ct-1a68ck03fn98r" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateS3StoreParams.json
    ```
    2. Modify the schema as follows, you can delete and replace the contents. Replace `VPC_ID` appropriately.
     The values in the example have been tested, but may not be right for you.


    ###### Tip

    The `BucketName` must be unique across the region of the account and cannot include upper-case letters.
     Including your account ID as part of the BucketName is not a requirement but makes it easier to identify the bucket later.
     To see what S3 bucket names exist in the account, go to the Amazon S3 Console for your account.



    ```
    {
    "Description":      "S3BucketForWordPressBundle",
    "VpcId":            "`VPC_ID`",
    "StackTemplateId":  "stm-s2b72beb000000000",
    "Name":             "S3BucketForWP",
    "TimeoutInMinutes":  60,
    "Parameters":   {
        "AccessControl":    "Private",
        "BucketName":       "`ACCOUNT_ID-BUCKET_NAME`"
        }
    }
    ```
    3. Output the JSON template for CreateRfc to a file, in your current folder, named CreateS3StoreRfc.json:



    ```
    aws amscm create-rfc --generate-cli-skeleton > CreateS3StoreRfc.json
    ```
    4. Modify and save the CreateS3StoreRfc.json file, you can delete and replace the contents. Note that
     `RequestedStartTime` and `RequestedEndTime` are now optional; excluding them creates an ASAP RFC
     that executes as soon as it is approved (which usually happens automatically). To submit a scheduled RFC, add those values.



    ```
    {
    "ChangeTypeVersion":    "1.0",
    "ChangeTypeId":         "ct-1a68ck03fn98r",
    "Title":                "S3-Stack-For-WP-RFC"
    }
    ```
    5. Create the RFC, specifying the CreateS3StoreRfc.json file and the CreateS3StoreParams.json execution parameters file:



    ```
    aws amscm create-rfc --cli-input-json file://CreateS3StoreRfc.json  --execution-parameters file://CreateS3StoreParams.json
    ```

    You receive the RfcId of the new RFC in the response. Save the ID for subsequent steps.
    6. Submit the RFC:



    ```
    aws amscm submit-rfc --rfc-id `RFC_ID`
    ```

    If the RFC succeeds, you receive no output.
    7. To check RFC status, run



    ```
    aws amscm get-rfc --rfc-id `RFC_ID`
    ```
