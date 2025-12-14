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
- Avoid using domain administrator or local administrator accounts when Database (SQL Server) Collection is not needed.

## Using Auto-Connect Feature With Caution

The discovery tool uses two mechanisms to assign credentials to servers during _OS level collection_ (Network and Database modules, need to connect to individual server (VM)): auto-connect and manual.

**Manual**: a server can be manually associated with a specific credential. In this case, the discovery tool will use that credential only, failure or success. The user has to manually monitor collection status for that server and make adjustment.

**Auto-connect**: if no credential is manually associated with the server, the discovery tool will use auto-connect mechanism for that server. That means:

- at the start of each collection round, the discovery tool will get a list of credentials available for that server (based on OS types) and also configured to be "auto-connectable".
- The discovery tool will then test all credentials against the server in a loop.
  - If a working credential is found, the collection round for the server is successful, the discovery tool remembers it and will try it first next time.
  - If no working credential is found, the collection round for the server has failed
    - Network module: the server will use a backoff schedule, starting next collection round in 3 min, 30 min, 2 hours, and 6 hours following each failure (similar to exponential backoff).
    - Database collection: there is no retry. The discovery tool will make 1 attempt for each server every day.

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
