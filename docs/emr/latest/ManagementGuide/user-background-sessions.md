# User background sessions

User background sessions enable long-running analytics and machine learning workloads
to continue even after the user has logged off from their notebook interface. Starting
with EMR on EC2 release 7.11, this capability is available through EMR-EC2's trusted
identity propagation feature. The following sections explains the configuration options
and behaviors for user background sessions.

###### Note

User background session settings only affect Spark workloads launched through SageMaker
Unified Studio. Changes to this setting apply to new Livy sessions—existing active
sessions remain unaffected.

## Configure user background sessions

User background sessions must be enabled at two levels for proper functionality:

1. **IAM Identity Center instance level** (configured by IdC administrators)
2. **EMR cluster level** (configured by EMR cluster administrators)

### Enable user background sessions for Amazon EMR

To enable user background sessions for you must set the
`userBackgroundSessionsEnabled` parameter to `true` in
the `identityCenterConfiguration` when creating EMR security
configuration.

**Prerequisites:**

- The IAM role used to create or update EMR Security Configuration requires the `sso:PutApplicationSessionConfiguration`
  permission. This permission enables user background sessions for Amazon EMR managed IAM Identity Center application.
- Create an IAM role for IAM Identity Center
  - To integrate Amazon EMR with IAM Identity Center, create an IAM role that
    authenticates with IAM Identity Center from the EMR cluster.
    Amazon EMR uses SigV4 credentials to relay the IAM Identity
    Center identity to downstream services such as AWS Lake Formation. Your
    role should also have the required permissions to invoke the
    downstream services.
  - [Configure Lake Formation for an IAM Identity Center enabled EMR cluster](emr-idc-lf.md "emr-idc-lf.md").
    For required role permissions see: [Create an IAM role for Identity Center.](emr-idc-start.md#emr-idc-start-role "emr-idc-start.md#emr-idc-start-role")

- Launch your EMR cluster with release 7.11 or later and enable Trusted-Identity Propagation.

**Step 1 - Create an Identity Center
UserBackgroundSession enabled EMR security configuration**

Users
need to set `**EnableUserBackgroundSession**` **flag to
`true`**, which will allow EMR service to enable UserBackgourndSession at EMR
managed IDC application level. If this flag is set to `false` or not
set, EMR will disable IDC UserBackgroundSession by default.

**Example of using the AWS CLI:**

```

aws emr create-security-configuration --name "idc-userBackgroundSession-enabled-secConfig" \
--region `AWS_REGION`  \
--security-configuration ' \
{
	"AuthenticationConfiguration":{
		"IdentityCenterConfiguration":{
		"EnableIdentityCenter":true,
		"IdentityCenterInstanceARN": `"arn:aws:sso:::instance/ssoins-123xxxxxxxxxx789"`,
		"IdentityCenterApplicationAssigmentRequired": false,
		"EnableUserBackgroundSession": true,
		"IAMRoleForEMRIdentityCenterApplicationARN": "arn:aws:iam::`12345678912`:role/`YOUR_ROLE`"
		}
	},\
	"AuthorizationConfiguration": {
	"IAMConfiguration": {
		"EnableApplicationScopedIAMRole": true,
		"ApplicationScopedIAMRoleConfiguration": {
		"PropagateSourceIdentity": true
		}
	},\
	"LakeFormationConfiguration": {
		"AuthorizedSessionTagValue": "Amazon EMR"
	}
	},\
	"EncryptionConfiguration": {
		"EnableInTransitEncryption": true,
		"EnableAtRestEncryption": false,
		"InTransitEncryptionConfiguration": {
			"TLSCertificateConfiguration": {
				"CertificateProviderType": "PEM",
							"S3Object": `"s3://amzn-s3-demo-bucket/cert/my-certs.zip"`
			}
		}
	}
}'

```

**Step 2 - Create and launch an Identity Center enabled cluster**

Now that you've set up the IAM role that authenticates with Identity Center, and created an Amazon EMR security configuration that has Identity Center enabled, you can create and launch your identity-aware cluster. For steps to launch your cluster with the required security configuration, see Specify a security configuration for an Amazon EMR cluster.

### Configuration Matrix

The user background session behavior depends on both the EMR-EC2 setting and the IAM Identity Center instance-level settings:

| User Background Session Configuration Matrix | IAM Identity Center userBackgroundSession Enabled | Amazon EMR userBackgroundSessionsEnabled | Behavior |
| -------------------------------------------- | ------------------------------------------------- | ---------------------------------------- | -------- |
| Yes                                          | TRUE                                              | User background session enabled          |
| Yes                                          | FALSE                                             | Session expires with user logout         |
| No                                           | TRUE                                              | Session expires with user logout         |
| No                                           | FALSE                                             | Session expires with user logout         |

### Default user background session duration

By default, all user background sessions have a duration limit of 7 days in IAM Identity Center. Administrators can modify this duration in the IAM Identity Center console. This setting
applies at the IAM Identity Center instance level, affecting all supported IAM Identity Center applications within that instance.

- Duration can be set to any value from 15 minutes up to 90 days.
- This setting is configured in the IAM Identity Center console under **Settings** →
  **Authentication** →
  **Configure** (See Non-Interactive Jobs
  section)

### Impact of disabling user background sessions

When user background sessions are disabled in IAM Identity Center:

Existing Livy sessions

- Continue to run without interruption if they were started with
  user background sessions enabled. These sessions will continue
  using their existing background session tokens until they
  terminate naturally or are explicitly stopped.

New Livy sessions

- Will use the standard trusted identity propagation flow and
  will terminate when the user logs out or their interactive
  session expires (such as when closing a Amazon SageMaker Unified Studio JupyterLab
  notebook).

### Changing user background sessions duration

When the duration setting for user background sessions is modified
in IAM Identity Center:

Existing Livy sessions

- Continue to run with the same background session duration with
  which they were started.

New Livy sessions

- Will use the new session duration for background
  sessions.

### Considerations

#### Feature Availability

User background sessions for Amazon EMR are available for:

- Spark engine only (Hive engine is not supported)
- Livy interactive sessions only (batch jobs and streaming jobs are not supported)
- Amazon EMR release labels 7.11 and later. With EMR release 7.11, you need to install a
  bootstrap action script to enable user background sessions when
  creating a cluster. Please contact AWS Support for additional
  details.

###### Note

If you are using SageMaker Unified Studio provisioned
cluster, you do not need the bootstrap action script to use
this feature.

#### Cost Implications

- Jobs will continue to run to completion even after users end their Amazon SageMaker Unified Studio JupyterLab session and will incur charges
  for the entire duration of the completed run.
- Monitor your active background sessions to avoid unnecessary costs from forgotten
  or abandoned sessions.

#### Livy Session Termination Conditions

When using user background sessions, a Livy session will continue running until one of the following occurs:

- The user background session expires (based on IdC configuration, up to 90 days).
- The user background session is manually revoked by an administrator.
- The Livy session reaches its idle timeout (default: 8 hours after the last executed statement).
- The user explicitly stops or restarts the notebook kernel.
