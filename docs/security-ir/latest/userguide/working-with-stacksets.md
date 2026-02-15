# Working with CloudFormation stacksets

###### Important

AWS Security Incident Response does not enable containment capabilities by default, to execute these containment actions,
you must first grant the necessary permissions to the service using roles. You can create these roles
individually per account or across your entire organization by deploying CloudFormation StackSets,
which create the required roles.

You can find specific instructions on how to [Create a stack set with service-managed permissions](../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md").

Following are template stacksets to create the _AWSSecurityIncidentResponseContainment_ and
_AWSSecurityIncidentResponseContainmentExecution_ roles.

```



AWSTemplateFormatVersion: '2010-09-09'
Description: 'Deploy containment roles as managed StackSet to all organization accounts'

Resources:
  ContainmentRolesStackSet:
    Type: AWS::CloudFormation::StackSet
    Properties:
      StackSetName: SecurityIRContainmentRoles
      Description: Deploy security incident response containment roles across organization
      PermissionModel: SERVICE_MANAGED
      AutoDeployment:
        Enabled: true
        RetainStacksOnAccountRemoval: false
      Capabilities:
        - CAPABILITY_NAMED_IAM
      OperationPreferences:
        RegionConcurrencyType: PARALLEL
        MaxConcurrentPercentage: 100
        FailureTolerancePercentage: 10
      TemplateBody: |
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
                                !Sub 'arn:${AWS::Partition}:ssm:*:*:automation-definition/AWSSupport-ContainEC2Instance:$DEFAULT',
                                !Sub 'arn:${AWS::Partition}:ssm:*:*:automation-definition/AWSSupport-ContainS3Resource:$DEFAULT',
                                !Sub 'arn:${AWS::Partition}:ssm:*:*:automation-definition/AWSSupport-ContainIAMPrincipal:$DEFAULT',
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

  StackSetDeploymentOperation:
    Type: AWS::CloudFormation::StackInstances
    Properties:
      StackSetName: !Ref ContainmentRolesStackSet
      DeploymentTargets:
        OrganizationalUnitIds:
          - r-xxxx  # Replace with your root OU ID
      Regions:
        - us-east-1
      OperationPreferences:
        RegionConcurrencyType: PARALLEL
        MaxConcurrentPercentage: 100
        FailureTolerancePercentage: 10

Outputs:
  StackSetId:
    Description: ID of the created StackSet
    Value: !Ref ContainmentRolesStackSet
  StackSetArn:
    Description: ARN of the created StackSet
    Value: !GetAtt ContainmentRolesStackSet.StackSetId



```
