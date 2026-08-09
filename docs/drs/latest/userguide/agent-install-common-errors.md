# Common agent installation errors

This topic covers platform-agnostic installation errors related to AWS credentials, account
configuration, IAM, and agent lifecycle. These errors occur on both Linux and Windows.

###### Topics

- [Error: Outdated agent installer version](#error-outdated-installer "#error-outdated-installer")
- [Error: Account not initialized](#error-uninitialized-account "#error-uninitialized-account")
- [Error: Failed to validate AWS credentials](#error-invalid-credentials "#error-invalid-credentials")
- [Error: Request signature mismatch](#error-request-signature "#error-request-signature")
- [Error: Missing agent installation policy](#error-missing-installer-policy "#error-missing-installer-policy")
- [Error: Agent IAM role missing](#error-agent-role-missing "#error-agent-role-missing")
- [Error: Server registered to different Region or account](#error-account-region-mismatch "#error-account-region-mismatch")
- [Error: Reboot required after uninstallation](#error-reboot-after-uninstall "#error-reboot-after-uninstall")
- [Error: Volume exceeds size limit](#error-volume-too-large "#error-volume-too-large")
- [Error: Source server already exists](#error-source-server-exists "#error-source-server-exists")
- [Error: Missing marketplace license permissions](#error-marketplace-permissions "#error-marketplace-permissions")
- [Error: Secure connection failed while downloading installation files](#error-download-ssl-failure "#error-download-ssl-failure")
- [Error: Operating system is not supported](#error-unsupported-os "#error-unsupported-os")
- [Error: Invalid endpoint](#error-invalid-endpoint "#error-invalid-endpoint")
- [Error: Connection attempt failed on port 443](#error-connection-timeout "#error-connection-timeout")

## Error: Outdated agent installer version

**Error:** Installation fails with version-related errors
or unexpected behavior.

**Cause:** You are using an old version of the installer.
The installer does not self-update in all scenarios.

**Resolution:**

1. Download the latest installer from the AWS Elastic Disaster Recovery console. Choose
   **Source servers**, then choose
   **Add server**.
2. On Linux, check the installed agent version:

```
cat /var/lib/aws-replication-agent/agent.version
```

3. If a previous agent is installed, uninstall it first, reboot the server, then
   install the new version.
4. For download instructions, see [Adding source
   servers](adding-servers.md "adding-servers.md").

## Error: Account not initialized

**Error:**
`AWS Replication Agent installation failed due to the account not being initialized`

**Cause:** AWS Elastic Disaster Recovery has not been initialized in the
target Region. Initialization creates the required service-linked roles and replication
infrastructure.

**Resolution:**

1. Initialize AWS Elastic Disaster Recovery by following
   [Elastic Disaster Recovery initialization and permissions](getting-started-initializing.md "getting-started-initializing.md").
2. Run the installer again after initialization completes.

## Error: Failed to validate AWS credentials

**Error:**
`Failed to validate AWS credentials`

**Cause:** The AWS Access Key ID or Secret Access Key
provided during installation is incorrect, expired, or malformed.

**Resolution:**

1. Verify that the credentials are active in the IAM console.
2. If you are using temporary credentials (STS), check the expiration time.
3. Test the credentials independently:

```
aws sts get-caller-identity --region `region`
```

4. On Windows, use PowerShell instead of CMD to avoid special character pasting
   issues with secret keys.
5. Ensure that the Region specified during installation matches the Region where
   AWS Elastic Disaster Recovery is initialized.

## Error: Request signature mismatch

**Error:**
**`InvalidSignatureException... The request signature we calculated does not match the signature you provided`**

**Cause:** The installer signed the request with a corrupted AWS Secret
Access Key, so the computed signature does not match. This commonly occurs when a command shell interprets
special characters in the key and alters it during entry. A significantly skewed system clock can also cause
this error.

**Resolution:**

1. Re-enter the Secret Access Key and make sure you paste it exactly. On Windows, use PowerShell
   instead of CMD, or enclose the key in double quotes.
2. Make sure the system clock is accurate. For example, synchronize with Network Time Protocol
   (NTP).
3. Verify the credentials with the following command:

```
aws sts get-caller-identity
```

Then run the installer again.

## Error: Missing agent installation policy

**Error:**
`User is not authorized to perform` or access denied errors during
installation.

**Cause:** The IAM user or role used for installation does
not have the required permissions.

**Resolution:**

1. Attach the `AWSElasticDisasterRecoveryAgentInstallationPolicy`
   managed policy to the IAM user or role.

Policy ARN:
`arn:aws:iam::aws:policy/AWSElasticDisasterRecoveryAgentInstallationPolicy` 2. Verify the policy attachment for an IAM user:

```
aws iam list-attached-user-policies --user-name `username`
```

3. If you are using an IAM role, verify the policy attachment:

```
aws iam list-attached-role-policies --role-name `role-name`
```

## Error: Agent IAM role missing

**Error:** Installation fails because required service
roles do not exist.

**Cause:** The AWS Elastic Disaster Recovery service roles were not created
during initialization or were manually deleted. These roles are:

- `AWSElasticDisasterRecoveryReplicationServerRole`
- `AWSElasticDisasterRecoveryConversionServerRole`
- `AWSElasticDisasterRecoveryRecoveryInstanceRole`

**Resolution:**

1. Reinitialize AWS Elastic Disaster Recovery from the console. This recreates the roles.
2. For more information, see
   [Elastic Disaster Recovery initialization and permissions](getting-started-initializing.md "getting-started-initializing.md").

## Error: Server registered to different Region or account

**Error:**
`Cannot install agent, as this server was previously installed to replicate into another region or account`

**Cause:** The source server's agent configuration file
references a previous AWS Elastic Disaster Recovery Region or account.

**Resolution:**

###### Important

Resolving this requires disconnecting and deleting the existing source server from
the AWS Elastic Disaster Recovery console. This removes the server from AWS Elastic Disaster Recovery and terminates its
replication resources. Consult your DR administrator before proceeding.

1. Disconnect and delete the source server from the AWS Elastic Disaster Recovery console in the
   previously configured Region or account.
2. Run the installer again with the correct Region and credentials.

## Error: Reboot required after uninstallation

**Error:**
`The server has not been restarted since agent uninstallation`

**Cause:** The previous agent was uninstalled but the
kernel driver is still loaded in memory. A reboot is required to fully remove it.

**Resolution:**

1. Reboot the source server.
2. Run the installer again after the reboot completes.

## Error: Volume exceeds size limit

**Error:** Error indicating a volume is too large for
replication.

**Cause:** A source volume exceeds the AWS Elastic Disaster Recovery size
limits.

AWS Elastic Disaster Recovery volume limits:

- Maximum volume size: 16 TiB per volume
- Maximum boot volume size: 16 TiB
- Maximum volumes per source server: 63

**Resolution:**

1. Exclude the oversized volume by using the `--devices` installer
   parameter (Linux) or replication settings.
2. Alternatively, reduce the volume size on the source server before
   installing.

## Error: Source server already exists

**Error:**
`already exists` during installation.

**Cause:** The source server is already registered with
AWS Elastic Disaster Recovery in this Region and account.

**Resolution:**

- If reinstalling on the same server: run the installer again without providing
  tags. You cannot update tags during installation. Use the AWS Elastic Disaster Recovery console or API
  to modify tags.
- If registering as a new source server: disconnect and delete the existing
  source server from the AWS Elastic Disaster Recovery console first.

## Error: Missing marketplace license permissions

**Error:**
`Missing permissions to retrieve marketplace licenses from the source account`

**Cause:** The IAM credentials used for installation do
not have permission to access AWS Marketplace product codes. This error only occurs when
replicating Amazon EC2 instances that use Marketplace AMIs.

**Resolution:**

1. Add the `ec2:DescribeInstances` permission to the IAM user or
   role.
2. This permission is needed to retrieve Marketplace product codes from the source
   instance for license compliance.

## Error: Secure connection failed while downloading installation files

**Error:**
**`Failed to establish a secure connection while downloading the AWS Replication Agent installation files.`**

**Cause:** The installer could not complete a TLS
handshake when it downloaded the agent installation files from Amazon S3. An
intercepting proxy or a TLS-inspecting firewall might present a certificate that the
installer does not trust. The certificate authority (CA) trust store on the source
server might also be missing or outdated.

**Resolution:** Complete the following steps:

1. Allow direct HTTPS egress from the source server to the Amazon S3 endpoints
   in your target Region, without TLS inspection.
2. If you use a proxy, verify that the operating system trust store on the
   source server trusts the proxy CA certificate.
3. Verify that the system time on the source server is correct. Clock skew
   invalidates certificates that are otherwise valid.

## Error: Operating system is not supported

**Error:**
**`The operating system is not supported by the AWS Replication Agent.`**

**Cause:** The operating system of the source server is
not on the AWS Elastic Disaster Recovery supported list. Elastic Disaster Recovery checks the operating system during
installation.

**Resolution:** Verify that Elastic Disaster Recovery supports the
operating system of the source server, then run the installer again. For the supported versions,
see [Supported Linux operating
systems](Supported-Operating-Systems-Linux.md "Supported-Operating-Systems-Linux.md") or [Supported Windows
operating systems](Supported-Operating-Systems-Windows.md "Supported-Operating-Systems-Windows.md").

## Error: Invalid endpoint

**Error:** The AWS SDK returns this error:
**`Invalid endpoint: `value``**

**Cause:** The value that you provided for the
`--endpoint` parameter, or a malformed `--region` value, is not a
well-formed endpoint URL.

**Resolution:** Use one of the following options:

- Omit the `--endpoint` parameter so that the installer uses the
  default Regional endpoint.
- If you must set the `--endpoint` parameter, provide a valid HTTPS
  URL.
- Verify that the `--region` value is a valid AWS Region code, for
  example `us-east-1`.

## Error: Connection attempt failed on port 443

**Error:** The installer cannot reach the AWS Elastic Disaster Recovery
endpoint and returns this error:
**`Connection attempt to `region` on port 443
 failed.`**

**Cause:** The source server cannot open an outbound TCP
connection on port 443 to the AWS Elastic Disaster Recovery endpoints. This error is usually caused by one of
the following:

- A missing route from the source server to the AWS Elastic Disaster Recovery endpoints
- A firewall that blocks outbound connections, either on the source server or on
  a network appliance
- An incorrect web proxy configuration on the source server, for example a proxy
  that does not pass HTTPS traffic

**Resolution:** Verify that your firewall, security group,
and web proxy configuration allow outbound traffic on port 443 to the following
endpoints:

- `drs.`region`.amazonaws.com`
- `s3.`region`.amazonaws.com`

To test connectivity on Linux, run the following command on the source server:

```
`$` curl -v https://drs.`region`.amazonaws.com
```

To test connectivity on Windows, run the following command on the source server:

```
Test-NetConnection drs.`region`.amazonaws.com -Port 443
```

To avoid this error, verify connectivity to these endpoints from the source server
before you run the AWS Elastic Disaster Recovery agent installer.
