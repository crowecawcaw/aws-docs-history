

# Containment with EC2 Triage
<a name="containment-with-ec2-triage-template"></a>

Use this template if you want both containment capabilities and the ability for AWS Security Incident Response engineers to investigate running instances during an incident.

This template creates everything included in the containment-only template and adds the `AWSSecurityIncidentResponseInvestigationPolicy` to the `AWSSecurityIncidentResponseContainment` role. This policy grants the following permissions:
+ Describe Amazon EC2 instances and their status
+ Retrieve instance profile information
+ Verify Systems Manager Agent connectivity on target instances
+ Execute `ssm:SendCommand` to run investigative commands on instances

EC2 Triage allows AWS Security Incident Response engineers to collect volatile forensic data from running Amazon EC2 instances during an active security incident. This data can include running processes, network connections, logged-in users, and other operating system artifacts that would be lost if the instance were terminated or stopped.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Template for AWS Security Incident Response containment roles'

Resources:
  AWSSecurityIncidentResponseContainment:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: AWSSecurityIncidentResponseContainment
      AssumeRolePolicyDocument:
        {
          'Version': '2012-10-17',
          'Statement':
            [
              {
                'Effect': 'Allow',
                'Principal': { 'Service': 'containment.security-ir.amazonaws.com' },
                'Action': 'sts:AssumeRole',
                'Condition': { 'StringEquals': { 'sts:ExternalId': !Sub '${AWS::AccountId}' } },
              },
              {
                'Effect': 'Allow',
                'Principal': { 'Service': 'containment.security-ir.amazonaws.com' },
                'Action': 'sts:TagSession',
              },
            ],
        }
      Policies:
        - PolicyName: AWSSecurityIncidentResponseContainmentPolicy
          PolicyDocument:
            {
              'Version': '2012-10-17',
              'Statement':
                [
                  {
                    'Effect': 'Allow',
                    'Action': ['ssm:StartAutomationExecution'],
                    'Resource':
                      [
                        !Sub 'arn:${AWS::Partition}:ssm:*::document/AWSSupport-ContainEC2Instance',
                        !Sub 'arn:${AWS::Partition}:ssm:*::document/AWSSupport-ContainS3Resource',
                        !Sub 'arn:${AWS::Partition}:ssm:*::document/AWSSupport-ContainIAMPrincipal',
                        !Sub 'arn:${AWS::Partition}:ssm:*:${AWS::AccountId}:automation-execution/*',
                      ],
                  },
                  {
                    'Effect': 'Allow',
                    'Action':
                      ['ssm:DescribeInstanceInformation', 'ssm:GetAutomationExecution', 'ssm:ListCommandInvocations'],
                    'Resource': '*',
                  },
                  {
                    'Effect': 'Allow',
                    'Action': ['iam:PassRole'],
                    'Resource': !GetAtt AWSSecurityIncidentResponseContainmentExecution.Arn,
                    'Condition': { 'StringEquals': { 'iam:PassedToService': 'ssm.amazonaws.com' } },
                  },
                ],
            }
        - PolicyName: AWSSecurityIncidentResponseInvestigationPolicy
          PolicyDocument:
            {
              'Version': '2012-10-17',
              'Statement': 
                [
                  {
                    'Effect': 'Allow',
                    'Action': [
                      'ec2:DescribeInstanceStatus',
                      'ec2:DescribeInstances',
                      'ec2:DescribeRouteTables',
                      'ec2:DescribeSecurityGroupRules',
                      'iam:GetInstanceProfile',
                      'ssm:DescribeInstanceInformation',
                      'ssm:GetCommandInvocation'
                    ],
                    'Resource': '*'
                  },
                  {
                    'Effect': 'Allow',
                    'Action': [
                      'ssm:SendCommand'
                    ],
                    'Resource': '*'
                  }
                ]
              }
  AWSSecurityIncidentResponseContainmentExecution:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: AWSSecurityIncidentResponseContainmentExecution
      AssumeRolePolicyDocument:
        {
          'Version': '2012-10-17',
          'Statement':
            [{ 'Effect': 'Allow', 'Principal': { 'Service': 'ssm.amazonaws.com' }, 'Action': 'sts:AssumeRole' }],
        }
      ManagedPolicyArns:
        - !Sub arn:${AWS::Partition}:iam::aws:policy/SecurityAudit
      Policies:
        - PolicyName: AWSSecurityIncidentResponseContainmentExecutionPolicy
          PolicyDocument:
            {
              'Version': '2012-10-17',
              'Statement':
                [
                  {
                    'Sid': 'AllowIAMContainment',
                    'Effect': 'Allow',
                    'Action':
                      [
                        'iam:AttachRolePolicy',
                        'iam:AttachUserPolicy',
                        'iam:DeactivateMFADevice',
                        'iam:DeleteLoginProfile',
                        'iam:DeleteRolePolicy',
                        'iam:DeleteUserPolicy',
                        'iam:GetLoginProfile',
                        'iam:GetPolicy',
                        'iam:GetRole',
                        'iam:GetRolePolicy',
                        'iam:GetUser',
                        'iam:GetUserPolicy',
                        'iam:ListAccessKeys',
                        'iam:ListAttachedRolePolicies',
                        'iam:ListAttachedUserPolicies',
                        'iam:ListMfaDevices',
                        'iam:ListPolicies',
                        'iam:ListRolePolicies',
                        'iam:ListUserPolicies',
                        'iam:ListVirtualMFADevices',
                        'iam:PutRolePolicy',
                        'iam:PutUserPolicy',
                        'iam:TagMFADevice',
                        'iam:TagPolicy',
                        'iam:TagRole',
                        'iam:TagUser',
                        'iam:UntagMFADevice',
                        'iam:UntagPolicy',
                        'iam:UntagRole',
                        'iam:UntagUser',
                        'iam:UpdateAccessKey',
                        'identitystore:CreateGroupMembership',
                        'identitystore:DeleteGroupMembership',
                        'identitystore:IsMemberInGroups',
                        'identitystore:ListUsers',
                        'identitystore:ListGroups',
                        'identitystore:ListGroupMemberships',
                      ],
                    'Resource': '*',
                  },
                  {
                    'Sid': 'AllowOrgListAccounts',
                    'Effect': 'Allow',
                    'Action': 'organizations:ListAccounts',
                    'Resource': '*',
                  },
                  {
                    'Sid': 'AllowSSOContainment',
                    'Effect': 'Allow',
                    'Action':
                      [
                        'sso:CreateAccountAssignment',
                        'sso:DeleteAccountAssignment',
                        'sso:DeleteInlinePolicyFromPermissionSet',
                        'sso:GetInlinePolicyForPermissionSet',
                        'sso:ListAccountAssignments',
                        'sso:ListInstances',
                        'sso:ListPermissionSets',
                        'sso:ListPermissionSetsProvisionedToAccount',
                        'sso:PutInlinePolicyToPermissionSet',
                        'sso:TagResource',
                        'sso:UntagResource',
                      ],
                    'Resource': '*',
                  },
                  {
                    'Sid': 'AllowSSORead',
                    'Effect': 'Allow',
                    'Action': ['sso-directory:SearchUsers', 'sso-directory:DescribeUser'],
                    'Resource': '*',
                  },
                  {
                    'Sid': 'AllowS3Read',
                    'Effect': 'Allow',
                    'Action':
                      [
                        's3:GetAccountPublicAccessBlock',
                        's3:GetBucketAcl',
                        's3:GetBucketLocation',
                        's3:GetBucketOwnershipControls',
                        's3:GetBucketPolicy',
                        's3:GetBucketPolicyStatus',
                        's3:GetBucketPublicAccessBlock',
                        's3:GetBucketTagging',
                        's3:GetEncryptionConfiguration',
                        's3:GetObject',
                        's3:GetObjectAcl',
                        's3:GetObjectTagging',
                        's3:GetReplicationConfiguration',
                        's3:ListBucket',
                        's3express:GetBucketPolicy',
                      ],
                    'Resource': '*',
                  },
                  {
                    'Sid': 'AllowS3Write',
                    'Effect': 'Allow',
                    'Action':
                      [
                        's3:CreateBucket',
                        's3:DeleteBucketPolicy',
                        's3:DeleteObjectTagging',
                        's3:PutAccountPublicAccessBlock',
                        's3:PutBucketACL',
                        's3:PutBucketOwnershipControls',
                        's3:PutBucketPolicy',
                        's3:PutBucketPublicAccessBlock',
                        's3:PutBucketTagging',
                        's3:PutBucketVersioning',
                        's3:PutObject',
                        's3:PutObjectAcl',
                        's3express:CreateSession',
                        's3express:DeleteBucketPolicy',
                        's3express:PutBucketPolicy',
                      ],
                    'Resource': '*',
                  },
                  {
                    'Sid': 'AllowAutoScalingWrite',
                    'Effect': 'Allow',
                    'Action':
                      [
                        'autoscaling:CreateOrUpdateTags',
                        'autoscaling:DeleteTags',
                        'autoscaling:DescribeAutoScalingGroups',
                        'autoscaling:DescribeAutoScalingInstances',
                        'autoscaling:DescribeTags',
                        'autoscaling:EnterStandby',
                        'autoscaling:ExitStandby',
                        'autoscaling:UpdateAutoScalingGroup',
                      ],
                    'Resource': '*',
                  },
                  {
                    'Sid': 'AllowEC2Containment',
                    'Effect': 'Allow',
                    'Action':
                      [
                        'ec2:AuthorizeSecurityGroupEgress',
                        'ec2:AuthorizeSecurityGroupIngress',
                        'ec2:CopyImage',
                        'ec2:CreateImage',
                        'ec2:CreateSecurityGroup',
                        'ec2:CreateSnapshot',
                        'ec2:CreateTags',
                        'ec2:DeleteSecurityGroup',
                        'ec2:DeleteTags',
                        'ec2:DescribeImages',
                        'ec2:DescribeInstances',
                        'ec2:DescribeSecurityGroups',
                        'ec2:DescribeSnapshots',
                        'ec2:DescribeTags',
                        'ec2:ModifyNetworkInterfaceAttribute',
                        'ec2:RevokeSecurityGroupEgress',
                      ],
                    'Resource': '*',
                  },
                  {
                    'Sid': 'AllowKMSActions',
                    'Effect': 'Allow',
                    'Action':
                      [
                        'kms:CreateGrant',
                        'kms:DescribeKey',
                        'kms:GenerateDataKeyWithoutPlaintext',
                        'kms:ReEncryptFrom',
                        'kms:ReEncryptTo',
                      ],
                    'Resource': '*',
                  },
                  {
                    'Sid': 'AllowSSMActions',
                    'Effect': 'Allow',
                    'Action': ['ssm:DescribeAutomationExecutions'],
                    'Resource': '*',
                  },
                ],
            }
```