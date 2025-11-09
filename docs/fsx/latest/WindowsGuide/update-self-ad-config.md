# Updating a self-managed Active Directory configuration

To help ensure continuous, uninterrupted availability of your Amazon FSx file system, you must update the
file system's Active Directory configuration when any of the following Active Directory properties change:

- The DNS server IP addresses
- The service account credentials of the self-managed Active Directory
  When you update the self-managed Active Directory configuration for your Amazon FSx file system,
  your file system's state switches from **Available** to
  **Updating** while the update is applied. Verify that the state switches back
  to **Available** after the update has been applied – note that the update
  can take up to several minutes to complete. For more information, see [Monitoring self-managed Active Directory updates](monitor-self-ad-update.md "monitor-self-ad-update.md").

If there's an issue with the updated self-managed Active Directory configuration, the file
system state switches to **Misconfigured**. This state shows an error message
and recommended corrective action beside the file system description in the console, API, and
CLI. After taking the recommended corrective action, verify that your file system's state
eventually changes to **Available**.

###### Important

If you update your file system with a new service account, ensure that the
new service account has **Full control** permissions for the existing computer
objects associated with the file system.

For information about troubleshooting possible issues related to self-managed Active Directory
configurations, see [File system is in a misconfigured state](misconfigured-ad-config.md "misconfigured-ad-config.md").

You can use the AWS Management Console, Amazon FSx API, or AWS CLI to update the service account credentials and the DNS server IP addresses of a file system's self-managed Active Directory configuration. You can track the progress of a self-managed Active Directory configuration update at any time using the AWS Management Console, CLI, and API. For more information, see [Monitoring self-managed Active Directory updates](monitor-self-ad-update.md "monitor-self-ad-update.md").

###### To update the self-managed Active Directory configuration (Console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems**, and choose the Windows file system for which
   you want to update self-managed Active Directory configuration.
3. In the **Network & security** tab, then choose **Update**
   for the **DNS server IP addresses**, or for the service account username, depending on
   which Active Directory properties you are updating.
4. Enter the new DNS server IP addresses, or the new service account credentials (username and password) or secret ARN in the dialog that appears. You can use AWS Secrets Manager to store your credentials. For more information, see [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows "self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows").
5. Choose **Update** to initiate the Active Directory configuration update.

You can [monitor the update progress](monitor-self-ad-update.md "monitor-self-ad-update.md") using the AWS Management Console or the AWS CLI.

###### To update the self-managed Active Directory configuration (CLI)

- To update the self-managed Active Directory configuration of an FSx for Windows File Server file system, use the AWS CLI command
  [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md"). Set the following parameters:
  - `--file-system-id` to the ID of the file system you are updating.
  - `UserName` the new username for the self-managed Active Directory service
    account.
  - `Password` the new password for the self-managed Active Directory service
    account.
  - `DomainJoinServiceAccountSecret` the AWS Secrets Manager secret containing the username and password for a service account on your Active Directory domain

  ###### Note

  You can't provide both username/password and a domain join service account secret to connect to your Active Directory. Provide only one set of credentials.
  - `DnsIps` the IP addresses for the self-managed Active Directory DNS servers.

```
aws fsx update-file-system --file-system-id fs-0123456789abcdef0 \
  --windows-configuration 'SelfManagedActiveDirectoryConfiguration={UserName=`username`,Password=`password`,\
     DnsIps=[`192.0.2.0`,`192.0.2.24`]}'
```

If the update action is successful, the service sends back an HTTP 200 response.
The `AdminstrativeActions` object in the response describes the request and its status.
