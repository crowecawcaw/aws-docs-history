

# Custom Detection Rules finding types
<a name="findings-custom-detection-rules"></a>

This page lists the finding types that GuardDuty generates from Custom Detection Rules, grouped by data source. Each finding type aggregates one or more signals into a single finding. For more information about enabling Custom Detection Rules, see [Custom Detection Rules in GuardDuty](custom-detection-rules.md).

**Note**  
Individual rules are available only in AWS Regions that support the AWS service or feature that they target. For example, rules that target AWS Organizations or Amazon Simple Email Service are available only in Regions where those services operate. Similarly, rules that target Lambda function URLs or SageMaker AI notebook instances are available only in Regions where those features are supported.

**Topics**
+ [Custom Detection Rules for AWS CloudTrail management events](#cdr-cloudtrail-management-events)
+ [Custom Detection Rules for Runtime Monitoring](#cdr-runtime-monitoring)

## Custom Detection Rules for AWS CloudTrail management events
<a name="cdr-cloudtrail-management-events"></a>

The following finding types are generated from AWS CloudTrail management event signals, organized by MITRE ATT&CK® tactic.

### Credential Access
<a name="cdr-credential-access"></a>

These rules attempt to detect operations that retrieve or reset credentials, such as retrieving an Amazon EC2 instance password or resetting an Amazon RDS administrator password.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| **CredentialAccess:EC2/UnsecuredCredentials** | EC2PasswordDataRetrieved | MEDIUM | 
| **CredentialAccess:RDS/ModifyAuthenticationProcess** | RDSMasterPasswordReset | HIGH | 

### Defense Impairment
<a name="cdr-defense-impairment"></a>

These rules attempt to detect changes that disable or weaken security controls, such as deleting VPC flow logs, disabling an organization policy, or removing an account from an organization.



- ****DefenseImpairment:EC2/DisableOrModifyTools****
  - **Rule name:** EC2TerminationProtectionEnabled / **Severity:** LOW
  - **Rule name:** VPCFlowLogsDeleted / **Severity:** HIGH

- ****DefenseImpairment:Organizations/ModifyCloudResourceHierarchy****
  - **Rule name:** OrganizationLeaveAttempt
  - **Severity:** HIGH

- ****DefenseImpairment:Organizations/DisableOrModifyTools****
  - **Rule name:** OrganizationPolicyDisabled
  - **Severity:** HIGH

- ****DefenseImpairment:RDS/ModifyAuthenticationProcess****
  - **Rule name:** RDSIAMAuthDisabled
  - **Severity:** MEDIUM

- ****DefenseImpairment:Route53Resolver/DisableOrModifyTools****
  - **Rule name:** DNSQueryLogsDeleted
  - **Severity:** MEDIUM

- ****DefenseImpairment:S3/DisableOrModifyTools****
  - **Rule name:** S3CustomerProvidedKeysEnabled
  - **Severity:** HIGH



### Execution
<a name="cdr-execution"></a>

These rules attempt to detect changes that run code on a resource, such as modifying a SageMaker AI notebook lifecycle configuration.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| **Execution:SageMaker/CommandAndScriptingInterpreter** | SageMakerLifecycleConfigModified | MEDIUM | 

### Exfiltration
<a name="cdr-exfiltration"></a>

These rules attempt to detect changes that share resources outside your account, such as making an AMI, Amazon EBS snapshot, or Amazon RDS snapshot accessible to other accounts.



- ****Exfiltration:EC2/TransferDataToCloudAccount****
  - **Rule name:** AMIExternalAccess / **Severity:** HIGH
  - **Rule name:** EBSSnapshotExternalAccess / **Severity:** HIGH

- ****Exfiltration:RDS/TransferDataToCloudAccount****
  - **Rule name:** RDSSnapshotPubliclyShared
  - **Severity:** HIGH

- ****Exfiltration:S3/TransferDataToCloudAccount****
  - **Rule name:** S3BucketPolicyExternalAccess
  - **Severity:** HIGH



### Impact
<a name="cdr-impact"></a>

These rules attempt to detect changes that could disrupt or destroy data and resources, such as setting Amazon S3 objects to expire quickly, or enabling Amazon SES sending.



- ****Impact:S3/DataDestruction****
  - **Rule name:** S3LifecycleRapidExpiration
  - **Severity:** MEDIUM

- ****Impact:SES/ResourceHijacking****
  - **Rule name:** SESAccountSendingEnabled / **Severity:** LOW
  - **Rule name:** SESProductionAccessEnabled / **Severity:** MEDIUM



### Initial Access
<a name="cdr-initial-access"></a>

These rules attempt to detect activity that opens access to your environment, such as a console sign-in without MFA or making an Amazon RDS database publicly accessible.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| **InitialAccess:IAM/ValidAccounts** | ConsoleLoginWithoutMFA | MEDIUM | 
| **InitialAccess:RDS/ExploitPublicFacingApplication** | RDSPubliclyAccessible | HIGH | 

### Lateral Movement
<a name="cdr-lateral-movement"></a>

These rules attempt to detect activity that grants access between resources, such as pushing an SSH key to an Amazon EC2 instance.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| **LateralMovement:EC2/RemoteServices** | EC2InstanceSSHKeyPushed | MEDIUM | 

### Persistence
<a name="cdr-persistence"></a>

These rules attempt to detect changes that create or extend access, such as creating IAM access keys, modifying a role trust policy, or making a Lambda function publicly accessible.



- ****Persistence:EC2/BootOrLogonInitializationScripts****
  - **Rule name:** EC2UserDataModified
  - **Severity:** HIGH

- ****Persistence:EC2/ExternalRemoteServices****
  - **Rule name:** EC2SecurityGroupPublicSSH
  - **Severity:** MEDIUM

- ****Persistence:IAM/AccountManipulation****
  - **Rule name:** IAMAccessKeyCreated / **Severity:** LOW
  - **Rule name:** IAMRoleTrustPolicyModified / **Severity:** MEDIUM
  - **Rule name:** IAMUserLoginProfileCreated / **Severity:** HIGH
  - **Rule name:** IAMUserLoginProfileUpdated / **Severity:** MEDIUM

- ****Persistence:Lambda/AccountManipulation****
  - **Rule name:** LambdaFunctionPublicAccess
  - **Severity:** HIGH

- ****Persistence:Lambda/ModifyAuthenticationProcess****
  - **Rule name:** LambdaFunctionUrlPublicAccess
  - **Severity:** HIGH

- ****Persistence:RolesAnywhere/AccountManipulation****
  - **Rule name:** RolesAnywhereTrustAnchorCreated
  - **Severity:** MEDIUM



### Privilege Escalation
<a name="cdr-privilege-escalation"></a>

These rules attempt to detect changes that grant broader permissions, such as attaching an administrator policy to an IAM user or role.



- ****PrivilegeEscalation:IAM/AccountManipulation****
  - **Rule name:** AdminPolicyAttachedToRole / **Severity:** HIGH
  - **Rule name:** AdminPolicyAttachedToUser / **Severity:** HIGH
  - **Rule name:** BedrockServiceCredentialCreated / **Severity:** MEDIUM
  - **Rule name:** SESFullAccessPolicyAttachedToRole / **Severity:** MEDIUM
  - **Rule name:** SESFullAccessPolicyAttachedToUser / **Severity:** MEDIUM



### Resource Development
<a name="cdr-resource-development"></a>

These rules attempt to detect setup of resources that could support later activity, such as verifying an Amazon SES domain identity.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| **ResourceDevelopment:SES/CompromiseAccounts** | SESDomainIdentityVerified | MEDIUM | 

## Custom Detection Rules for Runtime Monitoring
<a name="cdr-runtime-monitoring"></a>

GuardDuty generates the following Custom Detection Rules finding types from Runtime Monitoring signals, organized by MITRE ATT&CK® tactic. These rules require Runtime Monitoring and the GuardDuty security agent on the monitored resource. For more information, see [Data sources and signals](custom-detection-rules-how-it-works.md#custom-detection-rules-how-it-works-data-sources).

### Command and Control
<a name="cdr-runtime-command-and-control"></a>

These rules attempt to detect processes that tunnel network traffic, such as DNS tunneling tools or protocol tunneling.



- **[CommandAndControl:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#commandandcontrol-runtime-suspicious-command)**
  - **Rule name:** DnsTunnelingToolExecuted / **Severity:** HIGH
  - **Rule name:** SuspiciousProtocolTunneling / **Severity:** MEDIUM



### Credential Access
<a name="cdr-runtime-credential-access"></a>

These rules attempt to detect processes that read sensitive data, such as process memory through the `/proc` file system.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [CredentialAccess:Runtime/SensitiveFileRead](findings-runtime-monitoring.md#credaccess-runtime-sensitive-file-read) | DumpProcessMemoryFromProc | HIGH | 

### Defense Impairment
<a name="cdr-runtime-defense-impairment"></a>

These rules attempt to detect processes that weaken host defenses, such as disabling audit logging, modifying firewall rules, or stopping services.



- **[DefenseEvasion:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#defense-evasion-runtime-sensitive-file-modified)**
  - **Rule name:** FirewallConfigModified / **Severity:** MEDIUM
  - **Rule name:** LogManipulation / **Severity:** MEDIUM

- **[DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command)**
  - **Rule name:** AuditDisabled / **Severity:** MEDIUM
  - **Rule name:** FirewallDisablement / **Severity:** MEDIUM
  - **Rule name:** KernelHardeningDisabled / **Severity:** MEDIUM
  - **Rule name:** KillCommandUsage / **Severity:** MEDIUM
  - **Rule name:** ServiceStoppedOrDisabled / **Severity:** MEDIUM



### Discovery
<a name="cdr-runtime-discovery"></a>

These rules attempt to detect processes that gather information about a resource, such as reading password files, searching for credentials or keys, or detecting virtualization.



- **[Discovery:Runtime/SensitiveFileRead](findings-runtime-monitoring.md#discovery-runtime-sensitive-file-read)**
  - **Rule name:** PasswordShadowFileDiscovery
  - **Severity:** MEDIUM

- **[Discovery:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#discovery-runtime-suspicious-command)**
  - **Rule name:** FindCommandReconCloudCredentials / **Severity:** MEDIUM
  - **Rule name:** FindCommandReconKeyMaterial / **Severity:** MEDIUM
  - **Rule name:** PromiscuousModeEnabled / **Severity:** MEDIUM
  - **Rule name:** SSHWithHostKeyCheckingDisabled / **Severity:** MEDIUM
  - **Rule name:** SqliteDatabaseDump / **Severity:** LOW
  - **Rule name:** VirtualizationDetection / **Severity:** LOW



### Execution
<a name="cdr-runtime-execution"></a>

These rules attempt to detect processes that run commands or code that might be malicious, such as downloading and running a script or opening an interactive shell in a container.



- **[Execution:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#execution-runtime-suspiciouscommand)**
  - **Rule name:** ChmodInTmpDirectory / **Severity:** MEDIUM
  - **Rule name:** CurlWgetScriptDownload / **Severity:** MEDIUM
  - **Rule name:** DataEncryptionUsingCommandLineUtilities / **Severity:** MEDIUM
  - **Rule name:** InlinePythonExecution / **Severity:** MEDIUM
  - **Rule name:** InteractiveShellInsideAContainer / **Severity:** MEDIUM
  - **Rule name:** RemoteFileCopy / **Severity:** MEDIUM
  - **Rule name:** ShellFromUtilities / **Severity:** MEDIUM

- **[Execution:Runtime/SuspiciousTool](findings-runtime-monitoring.md#execution-runtime-suspicioustool)**
  - **Rule name:** NetworkSnifferToolExecuted / **Severity:** MEDIUM
  - **Rule name:** RawSocketCreated / **Severity:** MEDIUM



### Exfiltration
<a name="cdr-runtime-exfiltration"></a>

These rules attempt to detect processes that move data out of a resource, such as uploading files with curl, wget, or rclone, or splitting data before transfer.



- **[Exfiltration:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#exfiltration-runtime-suspicious-command)**
  - **Rule name:** CurlWgetExfiltrateData / **Severity:** MEDIUM
  - **Rule name:** DataSplittingForExfiltration / **Severity:** MEDIUM
  - **Rule name:** S3DataExfiltrationWithRclone / **Severity:** MEDIUM



### Persistence
<a name="cdr-runtime-persistence"></a>

These rules attempt to detect changes that keep access to a resource, such as modifying user accounts, SSH authorized keys, scheduled jobs, or system services.



- **[Persistence:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#persistence-runtime-sensitive-file-modified)**
  - **Rule name:** PAMConfigModification / **Severity:** MEDIUM
  - **Rule name:** PasswordModification / **Severity:** MEDIUM
  - **Rule name:** SSHAuthorizedKeysModification / **Severity:** MEDIUM
  - **Rule name:** ScheduledJobManipulation / **Severity:** MEDIUM
  - **Rule name:** ShellRCFileManipulated / **Severity:** MEDIUM
  - **Rule name:** SystemdServiceManipulation / **Severity:** MEDIUM

- **[Persistence:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#persistence-runtime-suspicious-command)**
  - **Rule name:** AuditdKeylogger / **Severity:** MEDIUM
  - **Rule name:** InteractiveLocalAccountCreation / **Severity:** MEDIUM
  - **Rule name:** NobodyUserManipulation / **Severity:** HIGH
  - **Rule name:** SshFromPublicIPAddress / **Severity:** MEDIUM
  - **Rule name:** SystemdTransientServiceCreated / **Severity:** MEDIUM



### Privilege Escalation
<a name="cdr-runtime-privilege-escalation"></a>

These rules attempt to detect changes that grant higher-level permissions, such as modifying sudoers files, setting the setuid flag, or escaping a container with nsenter.



- **[DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command)**
  - **Rule name:** FindCommandReconSetuidSetgidFiles
  - **Severity:** MEDIUM

- **[PrivilegeEscalation:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#privilege-escalation-runtime-sensitive-file-modified)**
  - **Rule name:** SudoerFileLinked / **Severity:** MEDIUM
  - **Rule name:** SudoerFileManipulation / **Severity:** MEDIUM
  - **Rule name:** SudoerFileRenamed / **Severity:** MEDIUM

- **[PrivilegeEscalation:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#privilege-escalation-runtime-suspicious-command)**
  - **Rule name:** AddSetUIDCapability / **Severity:** HIGH
  - **Rule name:** NewUserAddedToRootGroup / **Severity:** HIGH
  - **Rule name:** NsenterContainerEscape / **Severity:** HIGH
  - **Rule name:** SetUidFlagSet / **Severity:** MEDIUM
  - **Rule name:** SudoPrivilegeEnumeration / **Severity:** MEDIUM
  - **Rule name:** SudoerFileRead / **Severity:** MEDIUM



### Stealth
<a name="cdr-runtime-stealth"></a>

These rules attempt to detect processes that hide activity, such as hijacking library functions with LD\_PRELOAD or encoding data with Base64.



- **[DefenseEvasion:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#defense-evasion-runtime-sensitive-file-modified)**
  - **Rule name:** LDPreloadFunctionHijack
  - **Severity:** MEDIUM

- **[DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command)**
  - **Rule name:** Base64EncodeDecode / **Severity:** MEDIUM
  - **Rule name:** BpftoolProgramLoaded / **Severity:** MEDIUM
  - **Rule name:** DebugfsRawDiskAccess / **Severity:** MEDIUM
  - **Rule name:** SuspiciousExecutionPath / **Severity:** MEDIUM

