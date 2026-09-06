

# Turning on resource tracking
<a name="turning-on-resource-tracking"></a>

Before you create your first compliance-related framework, you must turn on resource tracking. Doing so allows AWS Config to track your AWS Backup resources. For technical documentation about how to manage resource tracking, see [Setting up AWS Config with the console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html) in the *AWS Config Developer Guide*. 

Charges apply when you turn on resource tracking. For information about resource tracking pricing and billing for AWS Backup Audit Manager, see [Metering, costs, and billing](https://docs.aws.amazon.com/aws-backup/latest/devguide/metering-and-billing.html).

**Topics**
+ [Turning on resource tracking using the console](#turning-on-resource-tracking-console)
+ [Turning on resource tracking using the AWS Command Line Interface (AWS CLI)](#turning-on-resource-tracking-cli)
+ [Turning on resource tracking using a CloudFormation template](#turning-on-resource-tracking-cfn)

## Turning on resource tracking using the console
<a name="turning-on-resource-tracking-console"></a>

**To turn on resource tracking using the console:**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the left navigation pane, under **Audit Manager**, choose **Frameworks**.

1. Turn on resource tracking by choosing **Manage resource tracking**.

1. Choose **Go to AWS Config Settings**.

1. Choose **Enable or disable recording**.

1. Choose **Enable** recording for all of the following resource types, or choose to enable recording for some resource types. Refer to [AWS Backup Audit Manager controls and remediation](https://docs.aws.amazon.com/aws-backup/latest/devguide/controls-and-remediation.html) for which resource types are required for your controls.
   + `AWS Backup: backup plans`
   + `AWS Backup: backup vaults`
   + `AWS Backup: recovery points`
   + `AWS Backup: backup selection`

1. Choose **Close**.

1. Wait for the blue banner with the text **Turning on resource tracking** to transition to the green banner with the text **Resource tracking is on**.

You can check whether you have turned on resource tracking and, if so, which resource types you are recording, in two places in the AWS Backup console. In the left navigation pane, either:
+ Choose **Frameworks**, then choose the text under **AWS Config recorder status**.
+ Choose **Settings**, then choose the text under **AWS Config recorder status**.

## Turning on resource tracking using the AWS Command Line Interface (AWS CLI)
<a name="turning-on-resource-tracking-cli"></a>

If you have not yet onboarded to AWS Config, it might be faster to onboard using the AWS CLI.

**To turn on resource tracking using the AWS CLI:**

1. Type the following command to determine if you already enabled your AWS Config recorder.

   ```
   $ aws configservice describe-configuration-recorders
   ```

   1. If your `ConfigurationRecorders` list is empty like this:

      ```
      {
        "ConfigurationRecorders": []
      }
      ```

      Your recorder is not enabled. Continue to step 2 to create your recorder.

   1. If you already enabled recording for all resources, your `ConfigurationRecorders` output will look like this:

      ```
      {
        "ConfigurationRecorders":[
          {
            "recordingGroup":{
              "allSupported":true,
              "resourceTypes":[
                
              ],
              "includeGlobalResourceTypes":true
            },
            "roleARN":"arn:aws:iam::[account]:role/[roleName]",
            "name":"default"
          }
        ]
      }
      ```

      Because you enabled all resources you already turned on resource tracking. You do not need to complete the rest of this procedure to use AWS Backup Audit Manager.

1. Create a AWS Config recorder with the AWS Backup Audit Manager resource types

   ```
   $ aws configservice put-configuration-recorder --configuration-recorder name={{default}}, \
   roleARN=arn:aws:iam::{{accountId}}:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig \ 
   --recording-group resourceTypes="['AWS::Backup::BackupPlan','AWS::Backup::BackupSelection', \
   'AWS::Backup::BackupVault','AWS::Backup::RecoveryPoint']"
   ```

1. Describe your AWS Config recorder.

   ```
   $ aws configservice describe-configuration-recorders
   ```

   Verify that it has the AWS Backup Audit Manager resource types by comparing your output with the following expected output.

   ```
   {
     "ConfigurationRecorders":[
       {
         "name":"{{default}}",
         "roleARN":"arn:aws:iam::{{accountId}}:role/AWSServiceRoleForConfig",
         "recordingGroup":{
           "allSupported":false,
           "includeGlobalResourceTypes":false,
           "resourceTypes":[
             "AWS::Backup::BackupPlan",
             "AWS::Backup::BackupSelection",
             "AWS::Backup::BackupVault",
             "AWS::Backup::RecoveryPoint"
           ]
         }
       }
     ]
   }
   ```

1. Create an Amazon S3 bucket as the destination to store the AWS Config configuration files.

   ```
   $ aws s3api create-bucket --bucket {{amzn-s3-demo-bucket}} —region {{us-east-1}}
   ```

1. Use {{policy.json}} to grant AWS Config permission to access your bucket. See the following sample {{policy.json}}.

   ```
   $ aws s3api put-bucket-policy --bucket {{amzn-s3-demo-bucket}} --policy {{file://policy.json}}
   ```

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement":[
       {
         "Sid":"AWSConfigBucketPermissionsCheck",
         "Effect":"Allow",
         "Principal":{
           "Service":"config.amazonaws.com"
         },
         "Action":"s3:GetBucketAcl",
         "Resource":"arn:aws:s3:::{{amzn-s3-demo-bucket}}",
         "Condition":{
           "StringEquals":{
             "aws:SourceAccount":"{{111122223333}}"
           }
         }
       },
       {
         "Sid":"AWSConfigBucketExistenceCheck",
         "Effect":"Allow",
         "Principal":{
           "Service":"config.amazonaws.com"
         },
         "Action":"s3:ListBucket",
         "Resource":"arn:aws:s3:::{{amzn-s3-demo-bucket}}",
         "Condition":{
           "StringEquals":{
             "aws:SourceAccount":"{{111122223333}}"
           }
         }
       },
       {
         "Sid":"AWSConfigBucketDelivery",
         "Effect":"Allow",
         "Principal":{
           "Service":"config.amazonaws.com"
         },
         "Action":"s3:PutObject",
         "Resource":"arn:aws:s3:::{{amzn-s3-demo-bucket}}/*",
         "Condition":{
           "StringEquals":{
             "aws:SourceAccount":"{{111122223333}}"
           }
         }
       }
     ]
   }
   ```

------

1. Configure your bucket as an AWS Config delivery channel

   ```
   $ aws configservice put-delivery-channel --delivery-channel name={{default}},s3BucketName={{amzn-s3-demo-bucket}}
   ```

1. Enable AWS Config recording

   ```
   $ aws configservice start-configuration-recorder --configuration-recorder-name {{default}}
   ```

1. Verify that `"FrameworkStatus":"ACTIVE"` in the last line of your `DescribeFramework` output as follows.

   ```
   $ aws backup describe-framework --framework-name {{test}} --region {{us-east-1}}
   ```

   ```
   {
     "FrameworkName":"test",
    "FrameworkArn":"arn:aws:backup:us-east-1:{{accountId}}:framework:{{test-f0001b0a-0000-1111-ad3d-4444f5cc6666}}",
     "FrameworkDescription":"",
     "FrameworkControls":[
       {
         "ControlName":"BACKUP_RECOVERY_POINT_MINIMUM_RETENTION_CHECK",
         "ControlInputParameters":[
           {
             "ParameterName":"requiredRetentionDays",
             "ParameterValue":"1"
           }
         ],
         "ControlScope":{
           
         }
       },
       {
         "ControlName":"BACKUP_PLAN_MIN_FREQUENCY_AND_MIN_RETENTION_CHECK",
         "ControlInputParameters":[
           {
             "ParameterName":"requiredFrequencyUnit",
             "ParameterValue":"hours"
           },
           {
             "ParameterName":"requiredRetentionDays",
             "ParameterValue":"35"
           },
           {
             "ParameterName":"requiredFrequencyValue",
             "ParameterValue":"1"
           }
         ],
         "ControlScope":{
           
         }
       },
       {
         "ControlName":"BACKUP_RESOURCES_PROTECTED_BY_BACKUP_PLAN",
         "ControlInputParameters":[
           
         ],
         "ControlScope":{
           
         }
       },
       {
         "ControlName":"BACKUP_RECOVERY_POINT_ENCRYPTED",
         "ControlInputParameters":[
           
         ],
         "ControlScope":{
           
         }
       },
       {
         "ControlName":"BACKUP_RECOVERY_POINT_MANUAL_DELETION_DISABLED",
         "ControlInputParameters":[
           
         ],
         "ControlScope":{
           
         }
       }
     ],
     "CreationTime":1633463605.233,
     "DeploymentStatus":"COMPLETED",
     "FrameworkStatus":"ACTIVE"
   }
   ```

## Turning on resource tracking using a CloudFormation template
<a name="turning-on-resource-tracking-cfn"></a>

For a CloudFormation template that turns on resource tracking, see [ Using AWS Backup Audit Manager with CloudFormation](https://docs.aws.amazon.com/aws-backup/latest/devguide/bam-cfn-integration.html).