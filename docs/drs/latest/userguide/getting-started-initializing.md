# Elastic Disaster Recovery initialization and permissions

In order to use AWS Elastic Disaster Recovery, the service must first be initialized for any AWS Region in which you plan to use Elastic Disaster Recovery.

## Initializing AWS Elastic Disaster Recovery

AWS Elastic Disaster Recovery must be initialized upon first use from within the AWS Elastic Disaster Recovery
Console. The initialization process occurs automatically once a
user accesses the AWS Elastic Disaster Recovery Console. The user is directed to create
the default replication settings, and upon saving the template, the service is
initialized by creating the IAM roles which are required for the service to work.
[Learn more about creating the default
replication settings as part of the quick start guide.](quick-start-guide-gs.md#first-time-setup-gs "quick-start-guide-gs.md#first-time-setup-gs")

###### Important

AWS Elastic Disaster Recovery **is not** compatible with
CloudEndure Disaster Recovery.

AWS Elastic Disaster Recovery can only be initialized by the Admin user of your AWS Account. During
initialization, the following IAM roles are created:

- **AWSServiceRoleForElasticDisasterRecovery**
- **AWSElasticDisasterRecoveryReplicationServerRole**
- **AWSElasticDisasterRecoveryConversionServerRole**
- **AWSElasticDisasterRecoveryRecoveryInstanceRole**
- **AWSElasticDisasterRecoveryAgentRole**
- **AWSElasticDisasterRecoveryFailbackRole**
- **AWSElasticDisasterRecoveryRecoveryInstanceWithLaunchActionsRole**

## Additional policies

You can create roles with granular permission for AWS Elastic Disaster Recovery. The service
comes with the following predefined managed IAM policies:

- AWSElasticDisasterRecoveryConsoleFullAccess
- AWSElasticDisasterRecoveryReadOnlyAccess
- AWSElasticDisasterRecoveryAgentPolicy
- AWSElasticDisasterRecoveryAgentInstallationPolicy
- AWSElasticDisasterRecoveryFailbackPolicy
- AWSElasticDisasterRecoveryFailbackInstallationPolicy
- AWSElasticDisasterRecoveryInstancePolicy
- AWSElasticDisasterRecoveryServiceRolePolicy
- AWSElasticDisasterRecoveryLaunchActionsPolicy

Learn more about [AWS Elastic Disaster Recovery roles and
managed policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Initializing DRS through the API

You can initialize AWS Elastic Disaster Recovery through the API. This can help you automate service
initialization by script when initializing multiple accounts.

###### Note

You need to [create the replication settings template](../APIReference/API_CreateReplicationConfigurationTemplate.md "../APIReference/API_CreateReplicationConfigurationTemplate.md") after initializing the
service.

To initialize AWS Elastic Disaster Recovery manually, create the following IAM roles through
the [IAM CreateRoleAPI](../../../IAM/latest/APIReference/API_CreateRole.md "../../../IAM/latest/APIReference/API_CreateRole.md"). Learn more about [creating IAM roles in the AWS IAM documentation](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md").

Creation of each role must include the following parameters:

| Role name                                                           | Path           | Trusted Entity    |
| ------------------------------------------------------------------- | -------------- | ----------------- |
| **AWSElasticDisasterRecoveryAgentRole**                             | /service-role/ | drs.amazonaws.com |
| **AWSElasticDisasterRecoveryFailbackRole**                          | /service-role/ | drs.amazonaws.com |
| **AWSElasticDisasterRecoveryConversionServerRole**                  | /service-role/ | ec2.amazonaws.com |
| **AWSElasticDisasterRecoveryRecoveryInstanceRole**                  | /service-role/ | ec2.amazonaws.com |
| **AWSElasticDisasterRecoveryReplicationServerRole**                 | /service-role/ | ec2.amazonaws.com |
| **AWSElasticDisasterRecoveryRecoveryInstanceWithLaunchActionsRole** | /service-role/ | ec2.amazonaws.com |

Example using the AWS CLI:

`aws iam create-role --path "/service-role/" --role-name
 AWSElasticDisasterRecoveryReplicationServerRole --assume-role-policy-document
 '{"Version": "2012-10-17", "Statement":[{"Effect":"Allow","Principal":
 {"Service":"ec2.amazonaws.com"},"Action":"sts:AssumeRole"}]}'`

After the roles have been created, attach the following AWS managed policies to the roles
through the [IAM AttachRolePolicy API](../../../IAM/latest/APIReference/API_AttachRolePolicy.md "../../../IAM/latest/APIReference/API_AttachRolePolicy.md"). Learn more about [adding and removing IAM identity permissions in the AWS IAM
documentation](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

1. Attach Managed Policy **AWSElasticDisasterRecoveryAgentPolicy** to Role
   **AWSElasticDisasterRecoveryAgentRole**
2. Attach Managed Policy **AWSElasticDisasterRecoveryFailbackPolicy** to Role
   **AWSElasticDisasterRecoveryFailbackRole**
3. Attach Managed Policy **AWSElasticDisasterRecoveryConversionServerPolicy** to Role
   **AWSElasticDisasterRecoveryConversionServerRole**
4. Attach Managed Policy **AWSElasticDisasterRecoveryRecoveryInstancePolicy** to Role
   **AWSElasticDisasterRecoveryRecoveryInstanceRole**
5. Attach Managed Policy **AWSElasticDisasterRecoveryReplicationServerPolicy** to Role
   **AWSElasticDisasterRecoveryReplicationServerRole**
6. Attach Managed Policy **AWSElasticDisasterRecoveryRecoveryInstancePolicy** and **AmazonSSMManagedInstanceCore** to Role
   **AWSElasticDisasterRecoveryRecoveryInstanceWithLaunchActionsRole**

###### Note

Roles must also have a trust policy defined. The trust policy needs to define source
identity and source account for security reasons, and allow the service to call
SetSourceIdentity and AssumeRole. See the following policy examples.

Example 1: creating a role for the **AWSElasticDisasterRecoveryAgentRole** with trusted entity
relationships via the CreateRole API:

**Role: AWSElasticDisasterRecoveryAgentRole**

```
$ aws iam create-role --path "/service-role/" --role-name
				AWSElasticDisasterRecoveryAgentRole --assume-role-policy-document file://agent-source-drs-trust-policy.json

```

**agent-source-drs-trust-policy.json**

Example 2: creating a role for the **AWSElasticDisasterRecoveryFailbackRole** with trusted entity
relationships via the CreateRole API:

**Role:
AWSElasticDisasterRecoveryFailbackRole**

```
$ aws iam create-role --path "/service-role/" --role-name
				AWSElasticDisasterRecoveryFailbackRole --assume-role-policy-document file://failback-source-drs-trust-policy.json

```

**failback-source-drs-trust-policy.json**

Example 3: creating roles for the **AWSElasticDisasterRecoveryConversionServerRole**, **AWSElasticDisasterRecoveryRecoveryInstanceRole**,
and **AWSElasticDisasterRecoveryReplicationServerRole** with trusted entity relationships via the CreateRole API:

**Role:
AWSElasticDisasterRecoveryConversionServerRole**

```
$ aws iam create-role --path "/service-role/" --role-name
				AWSElasticDisasterRecoveryConversionServerRole --assume-role-policy-document file://source-drs-trust-policy.json

```

**Role:
AWSElasticDisasterRecoveryRecoveryInstanceRole**

```
$ aws iam create-role --path "/service-role/" --role-name
				AWSElasticDisasterRecoveryRecoveryInstanceRole --assume-role-policy-document file://source-drs-trust-policy.json

```

**Role:
AWSElasticDisasterRecoveryReplicationServerRole**

```
$ aws iam create-role --path "/service-role/" --role-name
				AWSElasticDisasterRecoveryReplicationServerRole --assume-role-policy-document file://source-drs-trust-policy.json

```

**source-drs-trust-policy.json**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ec2.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Once the policies are attached to the roles, run the `aws drs initialize-service` command. This automatically creates the service-linked role (**AWSServiceRoleForElasticDisasterRecovery**), creates
instance profiles, adds roles to instance profiles, and finishes service
initialization.

Learn more about [AWS Elastic Disaster Recovery roles and
managed policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Programmatically initializing DRS

To programmatically initialize the service, create an IAM role with the following IAM policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:AttachRolePolicy",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:ArnEquals": {
 "iam:PolicyARN": [
 "arn:aws:iam::aws:policy/service-role/AWSElasticDisasterRecoveryAgentPolicy",
 "arn:aws:iam::aws:policy/service-role/AWSElasticDisasterRecoveryFailbackPolicy",
 "arn:aws:iam::aws:policy/service-role/AWSElasticDisasterRecoveryConversionServerPolicy",
 "arn:aws:iam::aws:policy/service-role/AWSElasticDisasterRecoveryRecoveryInstancePolicy",
 "arn:aws:iam::aws:policy/service-role/AWSElasticDisasterRecoveryReplicationServerPolicy"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "ForAnyValue:StringLike": {
 "iam:PassedToService": [
 "ec2.amazonaws.com",
 "drs.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "drs:InitializeService",
 "drs:ListTagsForResource",
 "drs:GetReplicationConfiguration",
 "drs:CreateLaunchConfigurationTemplate",
 "drs:GetLaunchConfiguration",
 "drs:CreateReplicationConfigurationTemplate",
 "drs:*ReplicationConfigurationTemplate*",
 "iam:TagRole",
 "iam:CreateRole",
 "iam:GetServiceLinkedRoleDeletionStatus",
 "iam:ListAttachedRolePolicies",
 "iam:ListRolePolicies",
 "iam:GetRole",
 "iam:DeleteRole",
 "iam:DeleteServiceLinkedRole",
 "ec2:CreateSecurityGroup",
 "ec2:CreateTags",
 "sts:DecodeAuthorizationMessage",
 "ec2:DescribeSecurityGroups",
 "ec2:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/drs.amazonaws.com/AWSServiceRoleForElasticDisasterRecovery"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateInstanceProfile",
 "iam:ListInstanceProfilesForRole",
 "iam:GetInstanceProfile",
 "iam:ListInstanceProfiles",
 "iam:AddRoleToInstanceProfile"
 ],
 "Resource": [
 "arn:aws:iam::*:instance-profile/*",
 "arn:aws:iam::*:role/*"
 ]
 }
 ]
}`

```

Once the policies are attached to the roles, run the `aws drs
 initialize-service` command. This automatically creates the
service-linked role (**AWSServiceRoleForElasticDisasterRecovery**), creates instance
profiles, adds roles to instance profiles, and finishes service initialization.

Learn more about [AWS Elastic Disaster Recovery roles and
managed policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
