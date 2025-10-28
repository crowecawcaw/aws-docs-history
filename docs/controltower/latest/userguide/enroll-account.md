# About enrolling existing accounts

You can extend AWS Control Tower governance to an individual, existing AWS account when you
_enroll_ it into an organizational unit (OU) that's
already governed by AWS Control Tower. Eligible accounts exist in _unregistered OUs that are part of the same AWS Organizations organization_ as the
AWS Control Tower OU.

Several methods exist for enrolling accounts into AWS Control Tower. **The information on this page applies to all methods of enrollment.**

###### Note

You cannot enroll an existing AWS account to serve as your audit or log archive
account except during initial landing zone setup.

## What happens during account

enrollment

During the enrollment process, AWS Control Tower performs these actions:

- Baselines the account, which includes deploying these stack sets:

      + `AWSControlTowerBP-BASELINE-CLOUDTRAIL`
      + `AWSControlTowerBP-BASELINE-CLOUDWATCH`
      + `AWSControlTowerBP-BASELINE-CONFIG`
      + `AWSControlTowerBP-BASELINE-ROLES`
      + `AWSControlTowerBP-BASELINE-SERVICE-ROLES`
      + `AWSControlTowerBP-BASELINE-SERVICE-LINKED-ROLES`
      + `AWSControlTowerBP-VPC-ACCOUNT-FACTORY-V1`

  It is a good idea to review the templates of these stack sets and make sure
  that they don’t conflict with your existing policies.

- Identifies the account through AWS IAM Identity Center or AWS Organizations.
- Places the account into the OU that you've specified. Be sure to apply all
  SCPs that are applied in the current OU, so that your security posture remains
  consistent.
- Applies mandatory controls to the account by means of the SCPs that apply to
  the selected OU as a whole.
- Enables AWS Config and configures it to record all resources in the account.
- Adds the AWS Config rules that apply the AWS Control Tower detective controls to the
  account.

###### Accounts and organization-level CloudTrail trails

For landing zone versions 3.1 and greater, if you've selected the optional AWS CloudTrail
integration in landing zone settings:

- All member accounts in an OU are governed by the AWS CloudTrail trail for the
  OU, enrolled or not.
- When you enroll an account into AWS Control Tower, your account is governed by the
  AWS CloudTrail trail for the new organization. If you have an existing deployment
  of a CloudTrail trail, you may see duplicate charges unless you delete the
  existing trail for the account before you enroll it in AWS Control Tower.
- If you move an account into a registered OU—for example by means of
  the AWS Organizations console or APIs—you may wish to remove any remaining
  account-level trails for the account. If you have an existing deployment of
  a CloudTrail trail, you will incur duplicate CloudTrail charges.
  If you update your landing zone and choose to opt out of organization-level
  trails, or if your landing zone is older than version 3.0, organization-level CloudTrail
  trails do not apply to your accounts.

## Enroll existing accounts with

VPCs

AWS Control Tower handles VPCs differently when you provision a new account in Account Factory
than when you enroll an existing account.

- When you create a new account, AWS Control Tower automatically removes the AWS
  default VPC and creates a new VPC for that account.
- When you enroll an existing account, AWS Control Tower does not create a new VPC for
  that account.
- When you enroll an existing account, AWS Control Tower does not remove any existing VPC
  or AWS default VPC associated with the account.

###### Tip

You can change the default behavior for new accounts by configuring Account
Factory, so it does not set up a VPC by default for accounts in your organization
under AWS Control Tower. For more information, see [Create an Account in AWS Control Tower Without a VPC](configure-without-vpc.md#create-without-vpc "configure-without-vpc.md#create-without-vpc").

## Enroll accounts with AWS Config resources

The account to be enrolled must not have existing AWS Config resources. See [Enroll accounts that have existing AWS Config resources](existing-config-resources.md "existing-config-resources.md").

Here are some example AWS Config CLI commands you can use to determine the status of your existing account's
AWS Config resources, such as the configuration recorder and delivery channel.

**View commands:**

- `aws configservice describe-delivery-channels`
- `aws configservice describe-delivery-channel-status`
- `aws configservice describe-configuration-recorders`

The normal response is something like `"name": "default"`

**Delete commands:**

- `aws configservice stop-configuration-recorder
--configuration-recorder-name
`NAME-FROM-DESCRIBE-OUTPUT``
- `aws configservice delete-delivery-channel --delivery-channel-name
`NAME-FROM-DESCRIBE-OUTPUT``
- `aws configservice delete-configuration-recorder
--configuration-recorder-name
`NAME-FROM-DESCRIBE-OUTPUT``

**Example for adding the `AWSControlTowerExecution` role**

The following YAML template may assist you in creating the required role in an account, so
that it can be enrolled programmatically.

```
AWSTemplateFormatVersion: 2010-09-09
Description: Configure the AWSControlTowerExecution role to enable use of your
  account as a target account in AWS CloudFormation StackSets.
Parameters:
  AdministratorAccountId:
    Type: String
    Description: AWS Account Id of the administrator account (the account in which
      StackSets will be created).
    MaxLength: 12
    MinLength: 12
Resources:
  ExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: AWSControlTowerExecution
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              AWS:
                - !Ref AdministratorAccountId
            Action:
              - sts:AssumeRole
      Path: /
      ManagedPolicyArns:
        - !Sub arn:${AWS::Partition}:iam::aws:policy/AdministratorAccess
```
