

# Custom Detection Rules finding types
<a name="findings-custom-detection-rules"></a>

This page lists all finding types that GuardDuty generates from Custom Detection Rules. Each finding type aggregates one or more signals into a single finding. For more information about enabling Custom Detection Rules, see [Custom Detection Rules in GuardDuty](custom-detection-rules.md).

**Note**  
The availability of individual rules depends on the availability of the corresponding AWS service and feature in each Region. For example, rules that target AWS Organizations or Amazon Simple Email Service are available only in Regions where those services operate. Similarly, rules that target Lambda function URLs or SageMaker AI notebook instances are available only in Regions where those features are supported.

## AWS CloudTrail Management Events
<a name="cdr-cloudtrail-management-events"></a>

The following finding types are generated from AWS CloudTrail management event signals, organized by MITRE ATT&CK® tactic.

### Credential Access
<a name="cdr-credential-access"></a>

Attempts to steal credentials such as passwords, tokens, or keys.


| Finding type | Signal name | Severity | 
| --- | --- | --- | 
| **CredentialAccess:EC2/UnsecuredCredentials** | [EC2PasswordDataRetrieved](#cdr-ec2-password-data-retrieved) | MEDIUM | 
| **CredentialAccess:RDS/ModifyAuthenticationProcess** | [RDSMasterPasswordReset](#cdr-rds-master-password-reset) | HIGH | 

### Defense Impairment
<a name="cdr-defense-impairment"></a>

Attempts to disable or degrade security defenses.



- ****DefenseImpairment:EC2/DisableOrModifyTools****
  - **Signal name:** [EC2TerminationProtectionEnabled](#cdr-ec2-termination-protection-enabled) / **Severity:** LOW
  - **Signal name:** [VPCFlowLogsDeleted](#cdr-vpc-flow-logs-deleted) / **Severity:** HIGH

- ****DefenseImpairment:Organizations/ModifyCloudResourceHierarchy****
  - **Signal name:** [OrganizationLeaveAttempt](#cdr-organization-leave-attempt)
  - **Severity:** HIGH

- ****DefenseImpairment:Organizations/DisableOrModifyTools****
  - **Signal name:** [OrganizationPolicyDisabled](#cdr-organization-policy-disabled)
  - **Severity:** HIGH

- ****DefenseImpairment:RDS/ModifyAuthenticationProcess****
  - **Signal name:** [RDSIAMAuthDisabled](#cdr-rds-iam-auth-disabled)
  - **Severity:** MEDIUM

- ****DefenseImpairment:Route53Resolver/DisableOrModifyTools****
  - **Signal name:** [DNSQueryLogsDeleted](#cdr-dns-query-logs-deleted)
  - **Severity:** MEDIUM

- ****DefenseImpairment:S3/DisableOrModifyTools****
  - **Signal name:** [S3CustomerProvidedKeysEnabled](#cdr-s3-customer-provided-keys-enabled)
  - **Severity:** HIGH



### Execution
<a name="cdr-execution"></a>

Attempts to run malicious code.


| Finding type | Signal name | Severity | 
| --- | --- | --- | 
| **Execution:SageMaker/CommandAndScriptingInterpreter** | [SageMakerLifecycleConfigModified](#cdr-sagemaker-lifecycle-config-modified) | MEDIUM | 

### Exfiltration
<a name="cdr-exfiltration"></a>

Attempts to steal data from your environment.



- ****Exfiltration:EC2/TransferDataToCloudAccount****
  - **Signal name:** [AMIExternalAccess](#cdr-ami-external-access) / **Severity:** HIGH
  - **Signal name:** [EBSSnapshotExternalAccess](#cdr-ebs-snapshot-external-access) / **Severity:** HIGH

- ****Exfiltration:RDS/TransferDataToCloudAccount****
  - **Signal name:** [RDSSnapshotPubliclyShared](#cdr-rds-snapshot-publicly-shared)
  - **Severity:** HIGH

- ****Exfiltration:S3/TransferDataToCloudAccount****
  - **Signal name:** [S3BucketPolicyExternalAccess](#cdr-s3-bucket-policy-external-access)
  - **Severity:** HIGH



### Impact
<a name="cdr-impact"></a>

Attempts to manipulate, interrupt, or destroy data and resources.



- ****Impact:S3/DataDestruction****
  - **Signal name:** [S3LifecycleRapidExpiration](#cdr-s3-lifecycle-rapid-expiration)
  - **Severity:** MEDIUM

- ****Impact:SES/ResourceHijacking****
  - **Signal name:** [SESAccountSendingEnabled](#cdr-ses-account-sending-enabled) / **Severity:** LOW
  - **Signal name:** [SESProductionAccessEnabled](#cdr-ses-production-access-enabled) / **Severity:** MEDIUM



### Initial Access
<a name="cdr-initial-access"></a>

Attempts to gain entry to your environment.


| Finding type | Signal name | Severity | 
| --- | --- | --- | 
| **InitialAccess:IAM/ValidAccounts** | [ConsoleLoginWithoutMFA](#cdr-console-login-without-mfa) | MEDIUM | 
| **InitialAccess:RDS/ExploitPublicFacingApplication** | [RDSPubliclyAccessible](#cdr-rds-publicly-accessible) | HIGH | 

### Lateral Movement
<a name="cdr-lateral-movement"></a>

Attempts to move through your environment.


| Finding type | Signal name | Severity | 
| --- | --- | --- | 
| **LateralMovement:EC2/RemoteServices** | [EC2InstanceSSHKeyPushed](#cdr-ec2-instance-ssh-key-pushed) | MEDIUM | 

### Persistence
<a name="cdr-persistence"></a>

Attempts to maintain access to your environment.



- ****Persistence:EC2/BootOrLogonInitializationScripts****
  - **Signal name:** [EC2UserDataModified](#cdr-ec2-user-data-modified)
  - **Severity:** HIGH

- ****Persistence:EC2/ExternalRemoteServices****
  - **Signal name:** [EC2SecurityGroupPublicSSH](#cdr-ec2-security-group-public-ssh)
  - **Severity:** MEDIUM

- ****Persistence:IAM/AccountManipulation****
  - **Signal name:** [IAMAccessKeyCreated](#cdr-iam-access-key-created) / **Severity:** LOW
  - **Signal name:** [IAMRoleTrustPolicyModified](#cdr-iam-role-trust-policy-modified) / **Severity:** MEDIUM
  - **Signal name:** [IAMUserLoginProfileCreated](#cdr-iam-user-login-profile-created) / **Severity:** HIGH
  - **Signal name:** [IAMUserLoginProfileUpdated](#cdr-iam-user-login-profile-updated) / **Severity:** MEDIUM

- ****Persistence:Lambda/AccountManipulation****
  - **Signal name:** [LambdaFunctionPublicAccess](#cdr-lambda-function-public-access)
  - **Severity:** HIGH

- ****Persistence:Lambda/ModifyAuthenticationProcess****
  - **Signal name:** [LambdaFunctionUrlPublicAccess](#cdr-lambda-function-url-public-access)
  - **Severity:** HIGH

- ****Persistence:RolesAnywhere/AccountManipulation****
  - **Signal name:** [RolesAnywhereTrustAnchorCreated](#cdr-rolesanywhere-trust-anchor-created)
  - **Severity:** MEDIUM



### Privilege Escalation
<a name="cdr-privilege-escalation"></a>

Attempts to gain higher-level permissions.



- ****PrivilegeEscalation:IAM/AccountManipulation****
  - **Signal name:** [AdminPolicyAttachedToRole](#cdr-admin-policy-attached-to-role) / **Severity:** HIGH
  - **Signal name:** [AdminPolicyAttachedToUser](#cdr-admin-policy-attached-to-user) / **Severity:** HIGH
  - **Signal name:** [BedrockServiceCredentialCreated](#cdr-bedrock-service-credential-created) / **Severity:** MEDIUM
  - **Signal name:** [SESFullAccessPolicyAttachedToRole](#cdr-ses-full-access-policy-attached-to-role) / **Severity:** MEDIUM
  - **Signal name:** [SESFullAccessPolicyAttachedToUser](#cdr-ses-full-access-policy-attached-to-user) / **Severity:** MEDIUM



### Resource Development
<a name="cdr-resource-development"></a>

Attempts to establish resources for future attacks.


| Finding type | Signal name | Severity | 
| --- | --- | --- | 
| **ResourceDevelopment:SES/CompromiseAccounts** | [SESDomainIdentityVerified](#cdr-ses-domain-identity-verified) | MEDIUM | 