

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


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [CommandAndControl:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#commandandcontrol-runtime-suspicious-command) | DnsTunnelingToolExecuted | HIGH | 
| [CommandAndControl:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#commandandcontrol-runtime-suspicious-command) | SuspiciousProtocolTunneling | MEDIUM | 

### Credential Access
<a name="cdr-runtime-credential-access"></a>

These rules attempt to detect processes that read sensitive data, such as process memory through the `/proc` file system.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [CredentialAccess:Runtime/SensitiveFileRead](findings-runtime-monitoring.md#credaccess-runtime-sensitive-file-read) | DumpProcessMemoryFromProc | HIGH | 

### Defense Impairment
<a name="cdr-runtime-defense-impairment"></a>

These rules attempt to detect processes that weaken host defenses, such as disabling audit logging, modifying firewall rules, or stopping services.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [DefenseEvasion:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#defense-evasion-runtime-sensitive-file-modified) | FirewallConfigModified | MEDIUM | 
| [DefenseEvasion:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#defense-evasion-runtime-sensitive-file-modified) | LogManipulation | MEDIUM | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | AuditDisabled | MEDIUM | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | FirewallDisablement | MEDIUM | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | KernelHardeningDisabled | MEDIUM | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | KillCommandUsage | MEDIUM | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | ServiceStoppedOrDisabled | MEDIUM | 

### Discovery
<a name="cdr-runtime-discovery"></a>

These rules attempt to detect processes that gather information about a resource, such as reading password files, searching for credentials or keys, or detecting virtualization.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [Discovery:Runtime/SensitiveFileRead](findings-runtime-monitoring.md#discovery-runtime-sensitive-file-read) | PasswordShadowFileDiscovery | MEDIUM | 
| [Discovery:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#discovery-runtime-suspicious-command) | FindCommandReconCloudCredentials | MEDIUM | 
| [Discovery:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#discovery-runtime-suspicious-command) | FindCommandReconKeyMaterial | MEDIUM | 
| [Discovery:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#discovery-runtime-suspicious-command) | PromiscuousModeEnabled | MEDIUM | 
| [Discovery:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#discovery-runtime-suspicious-command) | SSHWithHostKeyCheckingDisabled | MEDIUM | 
| [Discovery:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#discovery-runtime-suspicious-command) | SqliteDatabaseDump | LOW | 
| [Discovery:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#discovery-runtime-suspicious-command) | VirtualizationDetection | LOW | 

### Execution
<a name="cdr-runtime-execution"></a>

These rules attempt to detect processes that run commands or code that might be malicious, such as downloading and running a script or opening an interactive shell in a container.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [Execution:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#execution-runtime-suspiciouscommand) | ChmodInTmpDirectory | MEDIUM | 
| [Execution:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#execution-runtime-suspiciouscommand) | CurlWgetScriptDownload | MEDIUM | 
| [Execution:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#execution-runtime-suspiciouscommand) | DataEncryptionUsingCommandLineUtilities | MEDIUM | 
| [Execution:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#execution-runtime-suspiciouscommand) | InlinePythonExecution | MEDIUM | 
| [Execution:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#execution-runtime-suspiciouscommand) | InteractiveShellInsideAContainer | MEDIUM | 
| [Execution:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#execution-runtime-suspiciouscommand) | RemoteFileCopy | MEDIUM | 
| [Execution:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#execution-runtime-suspiciouscommand) | ShellFromUtilities | MEDIUM | 
| [Execution:Runtime/SuspiciousTool](findings-runtime-monitoring.md#execution-runtime-suspicioustool) | NetworkSnifferToolExecuted | MEDIUM | 
| [Execution:Runtime/SuspiciousTool](findings-runtime-monitoring.md#execution-runtime-suspicioustool) | RawSocketCreated | MEDIUM | 

### Exfiltration
<a name="cdr-runtime-exfiltration"></a>

These rules attempt to detect processes that move data out of a resource, such as uploading files with curl, wget, or rclone, or splitting data before transfer.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [Exfiltration:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#exfiltration-runtime-suspicious-command) | CurlWgetExfiltrateData | MEDIUM | 
| [Exfiltration:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#exfiltration-runtime-suspicious-command) | DataSplittingForExfiltration | MEDIUM | 
| [Exfiltration:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#exfiltration-runtime-suspicious-command) | S3DataExfiltrationWithRclone | MEDIUM | 

### Persistence
<a name="cdr-runtime-persistence"></a>

These rules attempt to detect changes that keep access to a resource, such as modifying user accounts, SSH authorized keys, scheduled jobs, or system services.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [Persistence:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#persistence-runtime-sensitive-file-modified) | PAMConfigModification | MEDIUM | 
| [Persistence:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#persistence-runtime-sensitive-file-modified) | PasswordModification | MEDIUM | 
| [Persistence:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#persistence-runtime-sensitive-file-modified) | SSHAuthorizedKeysModification | MEDIUM | 
| [Persistence:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#persistence-runtime-sensitive-file-modified) | ScheduledJobManipulation | MEDIUM | 
| [Persistence:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#persistence-runtime-sensitive-file-modified) | ShellRCFileManipulated | MEDIUM | 
| [Persistence:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#persistence-runtime-sensitive-file-modified) | SystemdServiceManipulation | MEDIUM | 
| [Persistence:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#persistence-runtime-suspicious-command) | AuditdKeylogger | MEDIUM | 
| [Persistence:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#persistence-runtime-suspicious-command) | InteractiveLocalAccountCreation | MEDIUM | 
| [Persistence:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#persistence-runtime-suspicious-command) | NobodyUserManipulation | HIGH | 
| [Persistence:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#persistence-runtime-suspicious-command) | SshFromPublicIPAddress | MEDIUM | 
| [Persistence:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#persistence-runtime-suspicious-command) | SystemdTransientServiceCreated | MEDIUM | 

### Privilege Escalation
<a name="cdr-runtime-privilege-escalation"></a>

These rules attempt to detect changes that grant higher-level permissions, such as modifying sudoers files, setting the setuid flag, or escaping a container with nsenter.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | FindCommandReconSetuidSetgidFiles | MEDIUM | 
| [PrivilegeEscalation:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#privilege-escalation-runtime-sensitive-file-modified) | SudoerFileLinked | MEDIUM | 
| [PrivilegeEscalation:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#privilege-escalation-runtime-sensitive-file-modified) | SudoerFileManipulation | MEDIUM | 
| [PrivilegeEscalation:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#privilege-escalation-runtime-sensitive-file-modified) | SudoerFileRenamed | MEDIUM | 
| [PrivilegeEscalation:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#privilege-escalation-runtime-suspicious-command) | AddSetUIDCapability | HIGH | 
| [PrivilegeEscalation:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#privilege-escalation-runtime-suspicious-command) | NewUserAddedToRootGroup | HIGH | 
| [PrivilegeEscalation:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#privilege-escalation-runtime-suspicious-command) | NsenterContainerEscape | HIGH | 
| [PrivilegeEscalation:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#privilege-escalation-runtime-suspicious-command) | SetUidFlagSet | MEDIUM | 
| [PrivilegeEscalation:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#privilege-escalation-runtime-suspicious-command) | SudoPrivilegeEnumeration | MEDIUM | 
| [PrivilegeEscalation:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#privilege-escalation-runtime-suspicious-command) | SudoerFileRead | MEDIUM | 

### Stealth
<a name="cdr-runtime-stealth"></a>

These rules attempt to detect processes that hide activity, such as hijacking library functions with LD\_PRELOAD or encoding data with Base64.


| Finding type | Rule name | Severity | 
| --- | --- | --- | 
| [DefenseEvasion:Runtime/SensitiveFileModified](findings-runtime-monitoring.md#defense-evasion-runtime-sensitive-file-modified) | LDPreloadFunctionHijack | MEDIUM | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | Base64EncodeDecode | MEDIUM | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | BpftoolProgramLoaded | MEDIUM | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | DebugfsRawDiskAccess | MEDIUM | 
| [DefenseEvasion:Runtime/SuspiciousCommand](findings-runtime-monitoring.md#defenseevasion-runtime-suspicious-command) | SuspiciousExecutionPath | MEDIUM | 