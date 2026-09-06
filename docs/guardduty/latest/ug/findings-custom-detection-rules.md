# Custom Detection Rules finding types

This page lists all finding types that GuardDuty generates from Custom Detection Rules.
Each finding type aggregates one or more signals into a single finding. For more
information about enabling Custom Detection Rules, see
[Custom Detection Rules in GuardDuty](custom-detection-rules.md "custom-detection-rules.md").

###### Note

The availability of individual rules depends on the availability of the
corresponding AWS service and feature in each Region. For example, rules that
target AWS Organizations or Amazon Simple Email Service are available only in Regions where those
services operate. Similarly, rules that target Lambda function URLs or SageMaker AI
notebook instances are available only in Regions where those features are
supported.

## AWS CloudTrail Management Events

The following finding types are generated from AWS CloudTrail management event signals,
organized by MITRE ATT&CK® tactic.

### Credential Access

Attempts to steal credentials such as passwords, tokens, or keys.

| Finding type                                         | Signal name                                                                                     | Severity |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | -------- |
| **CredentialAccess:EC2/UnsecuredCredentials**        | [EC2PasswordDataRetrieved](#cdr-ec2-password-data-retrieved "#cdr-ec2-password-data-retrieved") | MEDIUM   |
| **CredentialAccess:RDS/ModifyAuthenticationProcess** | [RDSMasterPasswordReset](#cdr-rds-master-password-reset "#cdr-rds-master-password-reset")       | HIGH     |

### Defense Impairment

Attempts to disable or degrade security defenses.

| Finding type                                                                  | Signal name                                                                                                          | Severity |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------- |
| **DefenseImpairment:EC2/DisableOrModifyTools**                                | [EC2TerminationProtectionEnabled](#cdr-ec2-termination-protection-enabled "#cdr-ec2-termination-protection-enabled") | LOW      |
| [VPCFlowLogsDeleted](#cdr-vpc-flow-logs-deleted "#cdr-vpc-flow-logs-deleted") | HIGH                                                                                                                 |
| **DefenseImpairment:Organizations/ModifyCloudResourceHierarchy**              | [OrganizationLeaveAttempt](#cdr-organization-leave-attempt "#cdr-organization-leave-attempt")                        | HIGH     |
| **DefenseImpairment:Organizations/DisableOrModifyTools**                      | [OrganizationPolicyDisabled](#cdr-organization-policy-disabled "#cdr-organization-policy-disabled")                  | HIGH     |
| **DefenseImpairment:RDS/ModifyAuthenticationProcess**                         | [RDSIAMAuthDisabled](#cdr-rds-iam-auth-disabled "#cdr-rds-iam-auth-disabled")                                        | MEDIUM   |
| **DefenseImpairment:Route53Resolver/DisableOrModifyTools**                    | [DNSQueryLogsDeleted](#cdr-dns-query-logs-deleted "#cdr-dns-query-logs-deleted")                                     | MEDIUM   |
| **DefenseImpairment:S3/DisableOrModifyTools**                                 | [S3CustomerProvidedKeysEnabled](#cdr-s3-customer-provided-keys-enabled "#cdr-s3-customer-provided-keys-enabled")     | HIGH     |

### Execution

Attempts to run malicious code.

| Finding type                                           | Signal name                                                                                                             | Severity |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | -------- |
| **Execution:SageMaker/CommandAndScriptingInterpreter** | [SageMakerLifecycleConfigModified](#cdr-sagemaker-lifecycle-config-modified "#cdr-sagemaker-lifecycle-config-modified") | MEDIUM   |

### Exfiltration

Attempts to steal data from your environment.

| Finding type                                                                                       | Signal name                                                                                                   | Severity |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------- |
| **Exfiltration:EC2/TransferDataToCloudAccount**                                                    | [AMIExternalAccess](#cdr-ami-external-access "#cdr-ami-external-access")                                      | HIGH     |
| [EBSSnapshotExternalAccess](#cdr-ebs-snapshot-external-access "#cdr-ebs-snapshot-external-access") | HIGH                                                                                                          |
| **Exfiltration:RDS/TransferDataToCloudAccount**                                                    | [RDSSnapshotPubliclyShared](#cdr-rds-snapshot-publicly-shared "#cdr-rds-snapshot-publicly-shared")            | HIGH     |
| **Exfiltration:S3/TransferDataToCloudAccount**                                                     | [S3BucketPolicyExternalAccess](#cdr-s3-bucket-policy-external-access "#cdr-s3-bucket-policy-external-access") | HIGH     |

### Impact

Attempts to manipulate, interrupt, or destroy data and resources.

| Finding type                                                                                          | Signal name                                                                                           | Severity |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| **Impact:S3/DataDestruction**                                                                         | [S3LifecycleRapidExpiration](#cdr-s3-lifecycle-rapid-expiration "#cdr-s3-lifecycle-rapid-expiration") | MEDIUM   |
| **Impact:SES/ResourceHijacking**                                                                      | [SESAccountSendingEnabled](#cdr-ses-account-sending-enabled "#cdr-ses-account-sending-enabled")       | LOW      |
| [SESProductionAccessEnabled](#cdr-ses-production-access-enabled "#cdr-ses-production-access-enabled") | MEDIUM                                                                                                |

### Initial Access

Attempts to gain entry to your environment.

| Finding type                                         | Signal name                                                                               | Severity |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------- |
| **InitialAccess:IAM/ValidAccounts**                  | [ConsoleLoginWithoutMFA](#cdr-console-login-without-mfa "#cdr-console-login-without-mfa") | MEDIUM   |
| **InitialAccess:RDS/ExploitPublicFacingApplication** | [RDSPubliclyAccessible](#cdr-rds-publicly-accessible "#cdr-rds-publicly-accessible")      | HIGH     |

### Lateral Movement

Attempts to move through your environment.

| Finding type                           | Signal name                                                                                    | Severity |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- | -------- |
| **LateralMovement:EC2/RemoteServices** | [EC2InstanceSSHKeyPushed](#cdr-ec2-instance-ssh-key-pushed "#cdr-ec2-instance-ssh-key-pushed") | MEDIUM   |

### Persistence

Attempts to maintain access to your environment.

| Finding type                                                                                            | Signal name                                                                                                          | Severity |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------- |
| **Persistence:EC2/BootOrLogonInitializationScripts**                                                    | [EC2UserDataModified](#cdr-ec2-user-data-modified "#cdr-ec2-user-data-modified")                                     | HIGH     |
| **Persistence:EC2/ExternalRemoteServices**                                                              | [EC2SecurityGroupPublicSSH](#cdr-ec2-security-group-public-ssh "#cdr-ec2-security-group-public-ssh")                 | MEDIUM   |
| **Persistence:IAM/AccountManipulation**                                                                 | [IAMAccessKeyCreated](#cdr-iam-access-key-created "#cdr-iam-access-key-created")                                     | LOW      |
| [IAMRoleTrustPolicyModified](#cdr-iam-role-trust-policy-modified "#cdr-iam-role-trust-policy-modified") | MEDIUM                                                                                                               |
| [IAMUserLoginProfileCreated](#cdr-iam-user-login-profile-created "#cdr-iam-user-login-profile-created") | HIGH                                                                                                                 |
| [IAMUserLoginProfileUpdated](#cdr-iam-user-login-profile-updated "#cdr-iam-user-login-profile-updated") | MEDIUM                                                                                                               |
| **Persistence:Lambda/AccountManipulation**                                                              | [LambdaFunctionPublicAccess](#cdr-lambda-function-public-access "#cdr-lambda-function-public-access")                | HIGH     |
| **Persistence:Lambda/ModifyAuthenticationProcess**                                                      | [LambdaFunctionUrlPublicAccess](#cdr-lambda-function-url-public-access "#cdr-lambda-function-url-public-access")     | HIGH     |
| **Persistence:RolesAnywhere/AccountManipulation**                                                       | [RolesAnywhereTrustAnchorCreated](#cdr-rolesanywhere-trust-anchor-created "#cdr-rolesanywhere-trust-anchor-created") | MEDIUM   |

### Privilege Escalation

Attempts to gain higher-level permissions.

| Finding type                                                                                                                     | Signal name                                                                                          | Severity |
| -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------- |
| **PrivilegeEscalation:IAM/AccountManipulation**                                                                                  | [AdminPolicyAttachedToRole](#cdr-admin-policy-attached-to-role "#cdr-admin-policy-attached-to-role") | HIGH     |
| [AdminPolicyAttachedToUser](#cdr-admin-policy-attached-to-user "#cdr-admin-policy-attached-to-user")                             | HIGH                                                                                                 |
| [BedrockServiceCredentialCreated](#cdr-bedrock-service-credential-created "#cdr-bedrock-service-credential-created")             | MEDIUM                                                                                               |
| [SESFullAccessPolicyAttachedToRole](#cdr-ses-full-access-policy-attached-to-role "#cdr-ses-full-access-policy-attached-to-role") | MEDIUM                                                                                               |
| [SESFullAccessPolicyAttachedToUser](#cdr-ses-full-access-policy-attached-to-user "#cdr-ses-full-access-policy-attached-to-user") | MEDIUM                                                                                               |

### Resource Development

Attempts to establish resources for future attacks.

| Finding type                                   | Signal name                                                                                        | Severity |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------- |
| **ResourceDevelopment:SES/CompromiseAccounts** | [SESDomainIdentityVerified](#cdr-ses-domain-identity-verified "#cdr-ses-domain-identity-verified") | MEDIUM   |
