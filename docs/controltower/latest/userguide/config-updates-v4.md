

# AWS Config Updates
<a name="config-updates-v4"></a>
+  **Dedicated resources for AWS Config and AWS CloudTrail: ** AWS Config and AWS CloudTrail now use separate dedicated S3 buckets and SNS topics instead of shared resources. Customers have restricted flexibility to use a single or separate accounts for multiple integrations. 
  +  When upgrading to AWS Control Tower landing zone version 4.0, existing data and S3 buckets are not moved. AWS CloudTrail integration continues to use the existing S3 bucket with prefix `aws-controltower-logs`. The new AWS Config data post the update operation will be stored in a new S3 bucket with prefix `aws-controltower-config` that AWS Control Tower creates in the account designated for the CentralConfigBaseline. 
**Note**  
 Enabling AWS CloudTrail integration on landing zone 4.0 for the first time will create new S3 buckets each time with prefix `aws-controltower-cloudtrail` 
  +  Data Location Changes: Existing customers upgrading from previously shared to dedicated resources will have AWS Config and AWS CloudTrail data in different S3 buckets. Established customer workflows and tools may need updates to access data from new bucket locations. 
  +  AWS CloudTrail will continue to stay in the same existing bucket, but AWS Config data will be in a new S3 bucket created by AWS Control Tower. 
  +  Customers can set-up cross-bucket replication if they wish to centralize different logs to a single bucket. Please see [ S3 documentation ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) for more information. 
  +  If you have enrolled accounts with pre-existing AWS Config Delivery Channels not created by AWS Control Tower in Regions governed by AWS Control Tower, update the Delivery Channels' S3 bucket name to the new S3 bucket with prefix `aws-controltower-config-logs-` in the AWS Config integration account to be consistent with AWS Control Tower configurations on landing zone 4.0. See more details in [Enroll accounts that have existing AWS Config resources](existing-config-resources.md). 
+  **AWS Config integration on landing zone version 4.0: ** When migrating to landing zone 4.0 with AWS Config integration enabled, customers would see the following changes - 

  1.  The existing Audit account is registered as a delegated admin for AWS Config. 

  1.  Service-Linked Config Aggregator is deployed into the Audit account (AWS Config central aggregator account for new customers and Audit account for existing customers). The new aggregator can aggregate data from any AWS Config Recorder in the organization, including non-Control Tower managed accounts. 

  1.  Existing aggregators will be deleted - Organization aggregator in management account (`aws-controltower-ConfigAggregatorForOrganizations`) and account aggregator in Audit account (`aws-controltower-GuardRailsComplianceAggregator`) will be deleted. 

  1.  Since Configuration Aggregator is service-linked, controls associated with deleted aggregators will be automatically removed. 

     1. [Disallow Changes to Tags Created by AWS Control Tower for AWS Config Resources](https://docs.aws.amazon.com/controltower/latest/controlreference/mandatory-controls.html#cloudwatch-disallow-config-changes)

     1. [Disallow Deletion of AWS Config Aggregation Authorizations Created by AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/mandatory-controls.html#config-aggregation-authorization-policy)
+  **New `ConfigBaseline` baseline: ** There is now a separate `ConfigBaseline` at the OU level for detective controls support without requiring the comprehensive `AWSControlTowerBaseline`. See list of [ baseline types at the OU level](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html#ou-baseline-types) for more information. For existing customers that are using the default landing zone, all service integrations are now optional, with the caveat of dependency requirements outlined in [Key changes](key-changes-lz-v4.md). 
+  **Service-Linked Config Aggregator: **Replaces organization and account aggregators in the AWS Config central aggregator account. 
  +  When upgrading to landing zone 4.0 with AWS Config integration enabled, customers need to have `organizations:ListDelegatedAdministrators` permissions 

    ```
    {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
          {
             "Effect": "Allow",
             "Action": [
               "backup:UpdateGlobalSettings",
               "controltower:CreateLandingZone",
               "controltower:UpdateLandingZone",
               "controltower:ResetLandingZone",
               "controltower:DeleteLandingZone",
               "controltower:GetLandingZoneOperation",
               "controltower:GetLandingZone",
               "controltower:ListLandingZones",
               "controltower:ListLandingZoneOperations",
               "controltower:ListTagsForResource",
               "controltower:TagResource",
               "controltower:UntagResource",
                "servicecatalog:*",
                "organizations:*",
                "organizations:RegisterDelegatedAdministrator",
                "organizations:EnableAWSServiceAccess",
                "organizations:DeregisterDelegatedAdministrator",
                "organizations:ListDelegatedAdministrators",
                "sso:*",
                "sso-directory:*",
                "logs:*",
                "cloudformation:*",
                "kms:*",
                "iam:GetRole",
                "iam:CreateRole",
                "iam:GetSAMLProvider",
                "iam:CreateSAMLProvider",
                "iam:CreateServiceLinkedRole",
                "iam:ListRolePolicies",
                "iam:PutRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:AttachRolePolicy",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy"
             ],
             "Resource": "*"
          }
       ]
    }
    ```

**Important**  
 After you upgrade to landing zone version 4.0 and enable the AWS Config integration, you must complete the enablement process. Update or enable the `ConfigBaseline` on all OUs where you want to deploy AWS Config resources. Until you complete this process, your AWS Config Aggregator will not receive data from recorders. Each account continues to record and store data. After you finish updating the `ConfigBaseline`, the recorded data automatically backfills into the aggregator.   
 We recommend that you re-register your OUs or enable the `ConfigBaseline` as soon as possible after enabling the AWS Config integration. The landing zone update removes AWS Config delivery permissions from the previous S3 bucket policy, but delivery channels are redirected to the new bucket only after you complete re-registration. Until then, configuration snapshots and configuration history are not delivered to S3.   
 If re-registration is delayed, some of this data may not be delivered to S3 after re-registration completes. You can retrieve all data recorded within your configured retention period using the `config:GetResourceConfigHistory` API. 