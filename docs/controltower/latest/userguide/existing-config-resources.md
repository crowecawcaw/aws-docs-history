# Enroll accounts that have existing AWS Config

resources

This topic provides a step-by-step approach for how to enroll accounts that have existing
AWS Config resources. For examples of how to check your existing resources, see [Enroll accounts with AWS Config resources](enroll-account.md#example-config-cli-commands "enroll-account.md#example-config-cli-commands").

###### Examples of AWS Config resources

Here are some types of AWS Config resources that your account could have already. These
resources may need to be modified so that you can enroll your account into
AWS Control Tower.

- AWS Config recorder
- AWS Config delivery channel
- AWS Config aggregation authorization

###### Limitations

- Enroll account with existing AWS Config resource is not supported for management account or
  service integration account(s) configured in landing zone.
- The account can be enrolled only by using the OU registration or re-registration workflow
  which enables the `AWSControlTowerBaseline`. The account can not be enrolled by
  enabling or resetting the `ConfigBaseline`.
- Account with existing AWS Config resource is not supported by
  [Move and enroll accounts with auto-enrollment](account-auto-enrollment.md "account-auto-enrollment.md").
- If the resources are modified and create drift on the account, AWS Control Tower does not
  update the resources.
- AWS Config resources in Regions that are not governed by AWS Control Tower are not
  changed.

###### Assumptions

- You have deployed an AWS Control Tower landing zone.
- Your account is not enrolled with AWS Control Tower already.
- Your account has at least one pre-existing AWS Config resource in at least one of the
  Regions governed by AWS Control Tower.
- Your account is not in governance drift.

###### Note

If you attempt to enroll an account that has existing Config resources, without having
the account added to the allow list, enrollment will fail. Thereafter, if you
subsequently try to add that same account to the allow list, AWS Control Tower cannot validate
that the account is provisioned correctly. You must deprovision the account from
AWS Control Tower before you can request the allow list and then enroll it. If you only move the
account to a different AWS Control Tower OU, it causes governance drift, which also prevents the
account from being added to the allow list.

For a blog that describes an automated approach to enrolling accounts with existing AWS Config
resources, see [Automate enrollment of accounts with existing AWS Config resources into AWS Control Tower](https://aws.amazon.com//blogs/mt/automate-enrollment-of-accounts-with-existing-aws-config-resources-into-aws-control-tower/ "https://aws.amazon.com//blogs/mt/automate-enrollment-of-accounts-with-existing-aws-config-resources-into-aws-control-tower/").

###### This process has 5 main steps.

1. Add the account(s) to the AWS Control Tower allow list.
2. Create a new IAM role in the account.
3. Modify pre-existing AWS Config resources.
4. Create AWS Config resources in AWS Regions where they don't exist.
5. Enroll the account with AWS Control Tower.

###### Before you proceed, consider the following expectations regarding this

process.

- AWS Control Tower does not create any AWS Config resources in this account.
- After enrollment, AWS Control Tower controls automatically protect the AWS Config resources you
  created, including the new IAM role.
- If any changes are made to the AWS Config resources after enrollment, those resources
  must be updated to align with AWS Control Tower settings before you can re-enroll the
  account.

## Step 1: Contact support to add account(s) to the allow list

**Include this phrase in your ticket subject line:**

_Enroll accounts that have existing AWS Config resources into
AWS Control Tower_

###### Include the following details in the body of your ticket:

- Management account number
- Account numbers of member accounts that have existing AWS Config resources.
  You'll be able to create a support case for all of the accounts you wish to enroll.
- Your selected home Region for AWS Control Tower setup

###### Note

The required time for adding your account to the allow list is 2 business
days.

## Step 2: Create a new IAM role in the member

account

1. Open the CloudFormation console for the member account.
2. Create a new stack using the following template

```
AWSTemplateFormatVersion: 2010-09-09
Description: Configure AWS Config

Resources:
  CustomerCreatedConfigRecorderRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: aws-controltower-ConfigRecorderRole-customer-created
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - config.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWS_ConfigRole
        - arn:aws:iam::aws:policy/ReadOnlyAccess

```

3. Provide the name for the stack as
   **CustomerCreatedConfigRecorderRoleForControlTower**
4. Create the stack.

###### Note

Any SCPs that you create should exclude an
`aws-controltower-ConfigRecorderRole*` role. Do not modify the
permissions that restrict the ability for AWS Config rules to perform evaluations.

Follow these guidelines so that you don't receive an
`AccessDeniedException` when you have SCPs that block
`aws-controltower-ConfigRecorderRole*` from calling Config.

## Step 3: Identify the AWS Regions with

pre-existing resources

For each governed Region (AWS Control Tower governed) in the account, identify and note the
Regions that have at least one of the existing AWS Config resource example types shown
previously.

## Step 4: Identify the AWS Regions without any

AWS Config resources

For each governed Region (AWS Control Tower governed) in the account, identify and note the
Regions in which there are no AWS Config resources of the example types shown
previously.

## Step 5: Modify the existing resources in each

AWS Region

For this step, the following information is needed about your AWS Control Tower setup.

- `AUDIT_ACCOUNT` - the AWS Config service integration account
  (previously known as the Audit account) ID
- `CONFIG_BUCKET` - the AWS S3 bucket to which AWS Config delivers configuration snapshots
  and configuration history files. Locate and confirm that the AWS S3 bucket exists before proceeding
  to the next steps.
  - For landing zone version 3.3 or lower, the AWS S3 bucket is named
    `aws-controltower-logs-LOGGING_ACCOUNT-HOME_REGION`, located in the Logging account.
  - For landing zone version 4.0 or higher, the AWS S3 bucket is named
    `aws-controltower-config-logs-AUDIT_ACCOUNT-<REGION_STRING>-<SUFFIX_STRING>`,
    located in the AWS Config service integration account (previously known as the Audit account).

- `IAM_ROLE_ARN` - the IAM role ARN created in Step 2
- `ORGANIZATION_ID` - the organization ID for the management
  account
- `MEMBER_ACCOUNT_NUMBER` - the member account that is being
  modified
- `HOME_REGION` - the home Region for AWS Control Tower setup.

Modify each existing resource by following the instructions given in sections 5a
through 5c, which follow.

## Step 5a. AWS Config recorder

resources

Only one AWS Config recorder can exist per AWS Region. If one exists, modify the settings
as shown. Replace the item `GLOBAL_RESOURCE_RECORDING` with
**true** in your home Region. Replace the item with
**false** for other Regions where an AWS Config recorder exists.

- **Name:** DON'T CHANGE
- **RoleARN:** `IAM_ROLE_ARN`
  - **RecordingGroup:**
  - **AllSupported:** true
  - **IncludeGlobalResourceTypes:**
    `GLOBAL_RESOURCE_RECORDING`
  - **ResourceTypes:** Empty

This modification can be made through the AWS CLI using the following command.
Replace the string `RECORDER_NAME` with the existing AWS Config recorder
name.

```

aws configservice put-configuration-recorder --configuration-recorder  name=`RECORDER_NAME`,roleARN=arn:aws:iam::`MEMBER_ACCOUNT_NUMBER`:role/aws-controltower-ConfigRecorderRole-customer-created --recording-group allSupported=true,includeGlobalResourceTypes=`GLOBAL_RESOURCE_RECORDING` --region `CURRENT_REGION`

```

## Step 5b. Modify AWS Config delivery

channel resources

Only one AWS Config delivery channel can exist per Region. If another exists, modify the
settings as shown.

- **Name:** DON’T CHANGE
- **ConfigSnapshotDeliveryProperties:** TwentyFour_Hours
- **S3BucketName:**`CONFIG_BUCKET`
- **S3KeyPrefix:** `ORGANIZATION_ID`
- **SnsTopicARN:** The SNS topic ARN from the audit account,
  with the following format:

`arn:aws:sns:`CURRENT_REGION`:`AUDIT_ACCOUNT`:aws-controltower-AllConfigNotifications`

This modification can be made through the AWS CLI using the following command.
Replace the string `DELIVERY_CHANNEL_NAME` with
the existing AWS Config recorder name.

```

aws configservice put-delivery-channel --delivery-channel name=`DELIVERY_CHANNEL_NAME`,s3BucketName=`CONFIG_BUCKET`,s3KeyPrefix="`ORGANIZATION_ID`",configSnapshotDeliveryProperties={deliveryFrequency=TwentyFour_Hours},snsTopicARN=arn:aws:sns:`CURRENT_REGION`:`AUDIT_ACCOUNT`:aws-controltower-AllConfigNotifications --region `CURRENT_REGION`

```

## Step 5c. Modify AWS Config aggregation

authorization resources

###### Note

This step is not required for landing zone version 4.0 or higher.

Multiple aggregation authorizations can exist per Region. AWS Control Tower requires an
aggregation authorization that specifies the audit account as the authorized account,
and has the home Region for AWS Control Tower as the authorized Region. If it doesn’t exist,
create a new one with the following settings:

- **AuthorizedAccountId:** The Audit account ID
- **AuthorizedAwsRegion:** The home Region for the AWS Control Tower
  setup

This modification can be made through the AWS CLI using the following
command:

`aws configservice put-aggregation-authorization --authorized-account-id
 `AUDIT_ACCOUNT_ID`--authorized-aws-region
`HOME_REGION`--region
`CURRENT_REGION``

## Step 6: Create resources where they don’t

exist, in Regions governed by AWS Control Tower

Revise the CloudFormation template, so that in your home Region the
**IncludeGlobalResourcesTypes** parameter has the value
`GLOBAL_RESOURCE_RECORDING`, as shown in the example that follows. Also
update the required fields in the template, as specified in this section.

Replace the item `GLOBAL_RESOURCE_RECORDING` with **true**
in your home Region. Replace the item with **false** for other Regions
where an AWS Config recorder does not exist.

1. Navigate to the management account’s CloudFormation console.
2. Create a new StackSet with the name
   **CustomerCreatedConfigResourcesForControlTower**.
3. Copy and update the following template:

###### Note

The `CustomerCreatedAggregationAuthorization` resource in the template is
not required for landing zone version 4.0 or higher.

```
AWSTemplateFormatVersion: 2010-09-09
Description: Configure AWS Config
Resources:
  CustomerCreatedConfigRecorder:
    Type: AWS::Config::ConfigurationRecorder
    Properties:
      Name: aws-controltower-BaselineConfigRecorder-customer-created
      RoleARN: !Sub arn:aws:iam::${AWS::AccountId}:role/aws-controltower-ConfigRecorderRole-customer-created
      RecordingGroup:
        AllSupported: true
        IncludeGlobalResourceTypes: `GLOBAL_RESOURCE_RECORDING`
        ResourceTypes: []
  CustomerCreatedConfigDeliveryChannel:
    Type: AWS::Config::DeliveryChannel
    Properties:
      Name: aws-controltower-BaselineConfigDeliveryChannel-customer-created
      ConfigSnapshotDeliveryProperties:
        DeliveryFrequency: TwentyFour_Hours
      S3BucketName: `CONFIG_BUCKET`
      S3KeyPrefix: `ORGANIZATION_ID`
      SnsTopicARN: !Sub arn:aws:sns:${AWS::Region}:`AUDIT_ACCOUNT`:aws-controltower-AllConfigNotifications
  CustomerCreatedAggregationAuthorization:
    Type: "AWS::Config::AggregationAuthorization"
    Properties:
      AuthorizedAccountId: `AUDIT_ACCOUNT`
      AuthorizedAwsRegion: `HOME_REGION`

```

###### Update the template with required fields:

    1. In the **S3BucketName** field, replace the
     `CONFIG_BUCKET`
    2. In the **S3KeyPrefix** field, replace the
     `ORGANIZATION_ID`
    3. In the **SnsTopicARN** field, replace the
     `AUDIT_ACCOUNT`
    4. In the **AuthorizedAccountId** field, replace the
     `AUDIT_ACCOUNT`
    5. In the **AuthorizedAwsRegion** field, replace the
     `HOME_REGION`

4. During deployment on the CloudFormation console, add the member account number.
5. Add the AWS Regions that were identified in Step 4.
6. Deploy the stack set.

## Step 7: Register the OU with AWS Control Tower

In the AWS Control Tower dashboard, register the OU.

###### Note

The **Enroll account** workflow will not succeed for this task.
You must choose **Register OU** or **Re-register
OU**.
