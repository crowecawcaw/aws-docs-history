# Security considerations

## Securing the discovery tool VM

**Discovery tool VM security is crucial** because the discovery tool stores all credentials, logs, and customer data on the discovery tool VM.

The discovery tool VM has ssh access disabled by default and can only be accessed from client `vCenter UI -> "Launch Web Console"`.

The discovery tool VM comes with a default login password "password" for user
"discovery".

- We recommend that you update this password immediately after deployment.
- We **require** you to update the password if you want to enable ssh using the command `enablessh` after logging in using vCenter `Launch Web Console`. Please note, every time this command is called, you need to reset it.

## Securing Credentials

**General best practices for Credential Management**

- Store credentials securely
- Regularly rotate all credentials
- Use password managers or secure vaults
- Monitor credential usage
- Follow the principle of least privilege and only grant the minimum necessary permissions needed

**SNMP v2 Credentials**

- Use complex, non-default community strings
- Avoid common strings like "public" or "private"
- Treat community strings like passwords

**SNMP v3 Credentials**

- Enable both authentication and privacy
- Use strong authentication protocols (SHA preferred over MD5)
- Use strong encryption protocols (AES preferred over DES)
- Use complex passwords for both auth and privacy
- Use unique usernames (avoid common names)

**WinRM Credentials**

- Avoid disabling WinRM certificate check.
- We recommend that you create a dedicated service account with minimal required permissions.
- Avoid using domain administrator or local administrator accounts unless you need SQL Server collection. SQL Server collection requires Local Administrator access because it queries multiple WMI namespaces and uses elevated commands. For OS metrics without SQL Server discovery, a non-administrator account with Remote Management Users, Performance Monitor Users, and WMI read access to `root\cimv2` is sufficient. See [Required permissions for the discovery tool](discovery-tool-permissions.md "discovery-tool-permissions.md") for per-module details.

**Hyper-V credentials**

- Use dedicated service accounts with minimal Hyper-V management permissions.
- Avoid using domain administrator accounts.
- Hyper-V credentials support NTLM (HTTPS only) and Kerberos authentication.
- The discovery tool stores credentials encrypted at rest by using SQLCipher.

**Oracle credentials**

- Use a dedicated read-only service account with only SELECT\_CATALOG\_ROLE. Do not use DBA, SYSDBA, or SYSOPER privileges.
- The discovery tool performs only read operations and never writes to the Oracle database.
- The discovery tool does not access Diagnostics Pack or Tuning Pack views, so no additional Oracle license is required.
- Rotate the Oracle service account password regularly and update the credential in the discovery tool.

## Credential storage

The discovery tool encrypts stored credentials at rest using a database encryption key. On systems with systemd 250 or later, this key is encrypted using systemd-creds. On older systems, the key is stored as a permission-protected file. In both cases, an attacker with root access to the discovery tool host could access the encryption key and decrypt stored credentials. Restrict access to the discovery tool host and treat it as a privileged system in your environment.

## Using Auto-Connect Feature With Caution

The discovery tool uses two mechanisms to assign credentials to servers during _OS-level collection_: auto-connect and manual. OS-level collection includes the Network, SQL Server, Oracle Database, and OS metrics modules. These modules connect to individual servers from all sources, including VMware VMs, Hyper-V VMs, and imported servers.

**Manual**: a server can be manually associated with a specific credential. In this case, the discovery tool uses that credential only, regardless of success or failure. You must manually monitor collection status for that server and make adjustments.

**Auto-connect**: if no credential is manually associated with the server, the discovery tool uses the auto-connect mechanism for that server. That means:

- At the start of each collection round, the discovery tool gets a list of credentials available for that server (based on OS types) and also configured to be "auto-connectable".
- The discovery tool then tests all credentials against the server in a loop.

  - If a working credential is found, the collection round for the server is successful. The discovery tool remembers it and tries it first next time.
  - If no working credential is found, the collection round for the server has failed.

    - Network module: the server uses a backoff schedule, starting next collection round in 3 min, 30 min, 2 hours, and 6 hours following each failure (similar to exponential backoff).
    - SQL Server collection: The discovery tool does not retry. It makes one attempt per server each day.

**Impacts/Risks**:

Only use auto-connect when you are sure that risks are mitigated in your system:

**Risk 1**: With auto-connect configured on multiple wrong credentials, automatically trying them against servers could trigger account lockouts for production environments where lockout policies are configured.
For example, a data center can set its VMs to lock down after 3 failed SSH login attempts. In this case, if auto-connect is configured for 3 wrong SSH credentials, legitimate account lockouts would happen. If lockouts happen across multiple systems, critical business processes could be impacted, potentially causing cascading failures in dependent systems. In addition, Security Operations Centers could experience alert storms from mass authentication failure events, creating false positive security incidents that drain resources and may mask real attacks.

**Risk 2**: Actor with access to the discovery tool (knows discovery tool password) can brute force OS credentials on all servers, by configuring a large number of test credentials and use auto-connect to find the successful ones.

**Mitigations**:

Follow these guidelines:

- Make sure that the discovery tool password is properly secured and known only to authorized actors
- Ensure proper credentials are entered for the environment if lockout policies are in place. We recommend only configure known, working credentials even if account lockout policies are absent to ensure minimal operational load on individual VMs.
- "Auto-connect" is an opt-in feature. Do not select it and use manual credential assignment if account lockouts is a concern to the environment.

## CSV Import Security

When you import servers by using a CSV file, consider the following security implications:

- The CSV file might contain hostnames or IP addresses of internal servers. Treat it as sensitive data.
- The `os_credential_name` and `oracle_credential_name` columns reference preconfigured credentials by friendly name. The CSV does not contain secrets.
- All-or-nothing validation: if any row in the CSV is invalid, the entire upload is rejected. This prevents partial imports that could create a confusing state.
- Imported servers are immediately visible in the inventory and eligible for collection. Ensure that OS and Oracle credentials are correctly scoped before you import.

## Revoking Access Considerations

When you revoke access, deletion is scoped to the specific source:

- Revoking vCenter access deletes only vCenter data. It does not affect Hyper-V or imported server data.
- Revoking Hyper-V access deletes only Hyper-V data. It does not affect VMware or imported server data.
- Deleting imported servers removes them from inventory, but downstream collection data (network, database, OS metrics) is retained.
- To remove all source-specific inventory data, you must revoke or delete each source independently. Downstream collection data (network, database, OS metrics) is retained even after all sources are revoked.
