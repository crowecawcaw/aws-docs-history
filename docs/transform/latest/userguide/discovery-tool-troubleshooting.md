# Troubleshooting

## Verifying discovery tool connectivity to vCenter

When you experience VMware module configuration errors follow these steps to verify connectivity:

###### Access the discovery tool VM

- Log-in to the discovery tool VM, open Remote Console in vCenter

  - Username: discovery
  - Password: password

###### Test vCenter Connectivity

1. Test vCenter API Access:

```
curl -v --insecure -u <username>:<password> https://<vcenter-ip-or-hostname>:443/mob
```

2. Expected Success Output:

```
[ec2-user@discoverytool ~]$ curl -v --insecure -u <user>:<password> https://vcsa/mob > tmp.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 192.168.2.125:443...
* Connected to vcsa (192.168.2.125) port 443 (#0)
...
</xml>
* Connection #0 to host vcsa left intact
```

###### Test SSL Certificate

1. Run this command:

```
openssl s_client -showcerts -servername <hostname> -connect <hostname>:443
```

2. Expected Success Output:

   - Should show vSphere certificate details
   - Verifies SSL/TLS connectivity on port 443

```
[ec2-user@discoverytool ~]$ openssl s_client -showcerts -servername vcsa -connect vcsa:443
CONNECTED(00000003)
depth=0 CN = vcsa.onpremsim.env, C = US
verify error:num=20:unable to get local issuer certificate
verify return:1
depth=0 CN = vcsa.onpremsim.env, C = US
verify error:num=21:unable to verify the first certificate
verify return:1
---
Certificate chain
 0 s:/CN=vcsa.onpremsim.env/C=US
   i:/CN=CA/DC=vsphere/DC=local/C=US/ST=California/O=vcsa.onpremsim.env/OU=VMware Engineering
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
---
Server certificate
subject=/CN=vcsa.onpremsim.env/C=US
issuer=/CN=CA/DC=vsphere/DC=local/C=US/ST=California/O=vcsa.onpremsim.env/OU=VMware Engineering
---
```

## WinRM Troubleshooting

If you're experiencing connectivity issues with WinRM, follow these steps to test the connection. These steps also apply to Hyper-V connectivity issues, because the discovery tool uses WinRM to communicate with Hyper-V hosts.

Test basic WinRM connectivity using ports 5985 (HTTP) and 5986 (HTTPS). We need to make sure that connectivity works on port 5986 (HTTPS)

```
# Check WinRM listener configuration
winrm enumerate winrm/config/listener

# Note: Replace <HOST> with the target computer's hostname or IP address. Adjust the username and password as needed.
# Test WinRM connection on port 5985 (HTTP)
$cred = Get-Credential
Test-WSMan -Computer <HOST> -Authentication Negotiate -Credential $cred -Port 5985

# Test WinRM connection on port 5986 (HTTPS)
Test-WSMan -Computer <HOST> -Authentication Negotiate -Credential $cred -Port 5986
```

If the above tests fail, try establishing a PowerShell session with certificate validation disabled:

```
$cred = Get-Credential
$so = New-PsSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck
Enter-PSSession -ComputerName <HOST> -Credential $cred -Port 5985 -SessionOption $so
```

## Kerberos troubleshooting

If you experience Kerberos authentication failures when collecting data from Windows servers, use the following sections to diagnose and resolve common issues.

### Verify network requirements

Before you troubleshoot Kerberos authentication, verify that the discovery tool can reach the required network endpoints.

###### To verify network requirements for Kerberos

1. Verify DNS resolution to the domain controller. Run the following command from the discovery tool VM:

```
nslookup dc01.example.com
```

Alternatively, you can use `dig`:

```
dig dc01.example.com
```

If DNS resolution fails, verify that the discovery tool VM is configured to use a DNS server that can resolve your Active Directory domain. Check `/etc/resolv.conf` and confirm that the nameserver entries point to your domain DNS servers. 2. Verify connectivity to the Key Distribution Center (KDC) on port 88. Run the following command:

```
nc -zv dc01.example.com 88
```

Expected output:

```
Connection to dc01.example.com 88 port [tcp/kerberos] succeeded!
```

If the connection fails, verify that no firewall rules block traffic from the discovery tool VM to the domain controller on port 88. 3. Verify connectivity to the target Windows servers on WinRM ports. Run the following commands:

```
nc -zv <windows-server> 5985
nc -zv <windows-server> 5986
```

If the connection fails, verify that WinRM is enabled on the target server and that firewall rules allow inbound traffic on ports 5985 and 5986.

### Common Kerberos issues

The following are common Kerberos issues and their solutions.

**Case sensitivity errors**

Symptom: You receive a "Server not found in Kerberos database" error during authentication.

This error typically occurs when the Kerberos realm name is not in uppercase. Kerberos realms must be specified in uppercase in your `krb5.conf` file. For example, use `EXAMPLE.COM` instead of `example.com`.

**Account lockout prevention**

The discovery tool uses a backoff mechanism to prevent account lockouts from repeated failed authentication attempts. If your service account becomes locked out, you can reset the collection process by stopping and then starting the collection module through the discovery tool web UI at `https://<discovery-tool-vm-ip>:5000`.

**kinit fails from CLI**

The following table lists common `kinit` errors and their solutions.

| Error                                  | Cause                                                                                           | Solution                                                                                                                                             |
| -------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cannot find KDC for realm              | The KDC hostname or IP address is not reachable, or the realm is not configured in `krb5.conf`. | Verify that the `krb5.conf` file contains the correct KDC hostname and realm. Confirm DNS resolution and network connectivity to the KDC on port 88. |
| Preauthentication failed               | The password for the service account is incorrect.                                              | Verify the password and try again. If the account is locked out, unlock it in Active Directory before you retry.                                     |
| Client not found in Kerberos database  | The principal name does not match any account in Active Directory.                              | Verify that the principal name matches the account name exactly, including case. Use the format `username@REALM` with the realm in uppercase.        |
| Cannot resolve network address for KDC | DNS cannot resolve the KDC hostname.                                                            | Verify DNS configuration in `/etc/resolv.conf`. Confirm that the DNS server can resolve the KDC hostname. Test with `nslookup` or `dig`.             |

**Collection fails despite successful kinit**

If `kinit` succeeds but data collection still fails, check the following:

1. Verify that the principal name used for collection matches the case used during `kinit` exactly.
2. Verify that the service account has the required permissions on the target servers.
3. Verify that WinRM is enabled on the target servers.
4. Verify that the hostname used for collection matches the hostname registered in Active Directory.

**Kerberos works for some servers but not others**

If Kerberos authentication succeeds for some servers but fails for others, investigate the following areas:

If your servers span multiple Active Directory domains, configure a separate Kerberos credential for each domain. Make sure that your `/etc/krb5.conf` file includes entries for all realms. Each domain requires its own credential with the correct `username@REALM` principal.

Compare the WinRM configuration on a working server with a failing server. Run the following command on each server:

```
winrm get winrm/config
```

Test connectivity with Remote Desktop to isolate the issue. The discovery tool uses the format `username@DOMAIN`, while Remote Desktop uses the format `DOMAIN\username`.

Verify that the service account is a member of the local Administrators group on the failing server. Run the following command on the target server:

```
net localgroup Administrators
```

WMI requires local administrator privileges to access operating system information. SQL Server collection also requires that the service account has local administrator access on the target server.

### Kerberos configuration checklist

Use the following checklist to verify your Kerberos configuration before you start data collection.

- The `krb5.conf` file exists on the discovery tool VM.
- The realm name is in uppercase in `krb5.conf`.
- Running `kinit` with the service account succeeds without errors.
- Running `klist` shows a valid, non-expired ticket.
- The principal name matches the Active Directory account name exactly.
- DNS resolution works for the KDC hostname.
- Network connectivity to the KDC on port 88 is confirmed.
- Network connectivity to target Windows servers on ports 5985 and 5986 is confirmed.
- (Multi-domain) Each Active Directory domain has its own credential configured in the discovery tool, and `krb5.conf` contains `[realms]` and `[domain_realm]` entries for all domains.

## Oracle Database troubleshooting

To diagnose Oracle Database collection issues, such as missing data or errors, check the following.

**Connection refused or timeout**

Symptom: Oracle collection status shows a connection error for a server.

To troubleshoot this issue, check the following:

- Verify that the Oracle listener is running on the target host: `lsnrctl status`
- Verify network connectivity from the discovery tool to the Oracle host on port 1521 (or your custom port): `nc -zv <oracle-host> 1521`
- Verify that firewall rules allow inbound connections on the Oracle listener port.
- Verify the service name by running `lsnrctl services` on the Oracle host. If the service name is incorrect, the Oracle listener rejects the connection.

**Authentication failures (ORA-01017)**

Symptom: Collection fails with an invalid username or password error.

To troubleshoot this issue, check the following:

- Verify that the Oracle service account exists and is not locked: `SELECT account_status FROM dba_users WHERE username = 'DISCOVERY_USER';`
- Verify the password is correct by connecting manually: `sqlplus discovery_user/<password>@<host>:1521/<service_name>`
- If the account is locked, unlock it: `ALTER USER discovery_user ACCOUNT UNLOCK;`

**Insufficient privileges (ORA-01031)**

Symptom: Connection succeeds but collection returns incomplete data.

To troubleshoot this issue, check the following:

- Verify that SELECT\_CATALOG\_ROLE is granted: `SELECT * FROM dba_role_privs WHERE grantee = 'DISCOVERY_USER';`
- Grant the required role if missing: `GRANT SELECT_CATALOG_ROLE TO discovery_user;`

**Manual credential shows error but auto-connect works**

When you pin a credential manually to a server, the discovery tool does not fall back if the connection fails. Verify that the port and service name that you configured on the credential match the Oracle listener on that specific server. If the server has a non-standard port or service name, update the credential configuration accordingly.

**OS-level fallback not detecting Oracle**

If no database credentials are configured and the OS-level fallback does not detect Oracle:

- Verify that SSH or WinRM OS credentials are configured and working for the server (check OS metrics collection status).
- For Linux hosts, verify that `/etc/oratab` exists or that Oracle process monitor (`pmon`) processes are running.
- For Windows hosts, verify that Oracle registry entries exist under `HKLM\SOFTWARE\Oracle` or that `oracle.exe` processes are running.

## SNMP Troubleshooting

###### Access the discovery tool VM

- Log-in to the discovery tool VM, open Remote Console in vCenter

  - Username: discovery
  - Password: password

###### Install SNMP Tools (if needed)

- `sudo yum install net-snmp-utils -y`

###### Test SNMP Connection to Linux Servers

1. `snmptable -v 2c -c <COMMUNITY_STRING> <REMOTE_SERVER_IP> .1.3.6.1.2.1.6.13.1`
2. Example:

```
#SNMPv2c:
snmptable -v 2c -c public 192.168.1.100 .1.3.6.1.2.1.6.13.1

#SNMPv3 (with authentication):
snmptable -v 3 -u <username> -a MD5 -A <auth_password> 192.168.1.100 .1.3.6.1.2.1.6.13.1

#SNMPv3 (with privacy):
snmptable -v 3 -u <username> -a MD5 -A <auth_password> -x DES -X <priv_password> 192.168.1.100 .1.3.6.1.2.1.6.13.1
```

## Network collection errors

### a terminal is required to read the password

**Error:**

```
ss command failed on <host>: sudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helper sudo: a password is required
```

The ss command is prompting for user password. The configured ssh user must be in the sudoers group and be configured with passwordless sudo for the ss/netstat command. To configure passwordless sudo:

1. Create a new sudoers file:

```
sudo vi -f /etc/sudoers.d/<username>
```

2. Add the line:

```
<username> ALL=(ALL) NOPASSWD: /usr/sbin/ss, /usr/bin/netstat
```

3. After this change, running `sudo ss -tnap` and `sudo netstat -tnap` should execute without prompting for a password

### Network collection ran without sudo

If you see the following warning on the **Discovered inventory** page:

```
Network collection ran without sudo. Process-level connection data may be missing.
```

This warning indicates that the SSH user account does not have sudo access on the target server. Without sudo, the discovery tool can still collect network connection data, but it cannot determine which process owns each connection. To collect complete process-level connection data, ensure the SSH user has sudo access on the target server.

## OS metrics collection errors

### Missing server UUID for Linux servers

If the discovery tool is unable to collect the server UUID (showing as empty or missing) for Linux servers, verify that the SSH credentials configured for those servers have sudo privileges. The tool uses `dmidecode` to read the server UUID. If `dmidecode` is not installed, the tool falls back to reading `/sys/class/dmi/id/product_uuid`, which also requires sudo access. Without sudo, neither method can retrieve the UUID.

**Resolution:** Ensure the SSH user account provided to the discovery tool has sudo access on the target Linux servers.

## Access issues in Discovered inventory

If you see a message in **Server collection status** such as Missing credentials, or Access denied:

1. Select the server on the table of discovered servers.
2. Choose **Manage access credential** You can choose to:

   1. Select alternative credentials from the **Select credentials** dropdown.
   2. Select **Use new credentials** and provide new credentials.

3. **Save**.

The discovery tool retries the connection after you save your changes.

## SSH key authentication troubleshooting

**Testing SSH key connectivity from the discovery tool**

If SSH key authentication fails, verify connectivity from the discovery tool to the target server:

1. Log in to the discovery tool (via vSphere console or SSH to the Linux host).
2. Test SSH connectivity using your private key:

```
ssh -i /path/to/private_key -o StrictHostKeyChecking=no <username>@<target_ip>
```

3. If the connection succeeds, the issue is with how the key was uploaded to the discovery tool. Re-upload the key and verify the username matches.
4. If the connection fails, check the error message in the following table.

| Error message                             | Cause                                                                                                  | Resolution                                                                                                                                                                 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Permission denied (publickey)`           | The public key is not in the target server's `authorized_keys` file, or the username is wrong.         | Add the public key to `~/.ssh/authorized_keys` on the target server for the correct user. Verify file permissions: `chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys`. |
| `Connection timed out after 20s`          | Port 22 is not reachable from the discovery tool.                                                      | Verify that port 22 is open between the discovery tool and the target server. Check firewalls and security groups.                                                         |
| `Connection refused`                      | SSH service is not running on the target server.                                                       | Start the SSH service: `sudo systemctl start sshd`.                                                                                                                        |
| `Invalid SSH key for credential '`name`'` | The key format is not supported, the key data is corrupted, or the passphrase is missing or incorrect. | Verify the key format is RSA, ECDSA, or Ed25519 in PEM, OpenSSH, or PKCS#8 format. If the key is encrypted, make sure the passphrase is correct.                           |

## Linux installer troubleshooting

**Port 5000 is already in use**

**Symptom:** The discovery tool service fails to start after installation.

**Resolution:** Identify and stop the process using port 5000:

```
sudo ss -tlnp | grep :5000
```

Stop the conflicting process, then restart the discovery tool:

```
sudo ./AWS-Transform-discovery-tool.sh start
```

## Common error messages

This table describes common error messages and their explanations:

| Message                                        | Location                 | Explanation                                                                                                                                                                |
| ---------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A password has already been created            | Create password page     | Race condition when two users create passwords at the same time; refresh                                                                                                   |
| Export failed                                  | Inventory page           | Retry or send logs                                                                                                                                                         |
| An on-demand collection is already in progress | Inventory page           | Race condition when two users start manual collections at the same time; try again after the current manual collection is finished                                         |
| `Command timed out after 60s`                  | Server collection status | A command on the target server did not complete within 60 seconds. This can occur on heavily loaded servers. Retry the collection or investigate the target server's load. |
| One or more credentials contain unknown UUIDs  | OS access page           | Race condition when two users edit OS credentials at the same time; try again                                                                                              |
| Invalid password                               | Sign-in page             | Incorrect password for logging in; contact admin or reach out                                                                                                              |
| Your session has expired. Please log in again. | Sign-in page             | Session has timed out, need to login again                                                                                                                                 |
| An internal error occurred                     | Various pages            | Retry or send logs                                                                                                                                                         |
