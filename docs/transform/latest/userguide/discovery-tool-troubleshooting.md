# Troubleshooting

## Verifying discovery tool connectivity to vCenter

When you experience VMware module configuration errors follow these steps to verify connectivity:

###### Access the discovery tool VM

- Log-in to the discovery tool VM, open Remote Console in vCenter
  - Username: discovery
  - Password: collector

###### Test vCenter Connectivity

1. Test vCenter API Access:

```
curl -v --insecure -u <username>:<password> https://<vcenter-ip-or-hostname>:443/mob
```

2. Expected Success Output:

```
[ec2-user@discoverycollector ~]$ curl -v --insecure -u <user>:<password> https://vcsa/mob > tmp.txt
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
[ec2-user@discoverycollector ~]$ openssl s_client -showcerts -servername vcsa -connect vcsa:443
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

If you're experiencing connectivity issues with WinRM, follow these steps to test the connection:

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

## SNMP Troubleshooting

###### Access the discovery tool VM

- Log-in to the discovery tool VM, open Remote Console in vCenter
  - Username: discovery
  - Password: collector

###### Install SNMP Tools (if needed)

- ```
  sudo yum install net-snmp-utils -y
  ```

````

###### Test SNMP Connection to Linux Servers

1. ```
snmptable -v 2c -c <COMMUNITY_STRING> <REMOTE_SERVER_IP> .1.3.6.1.2.1.6.13.1
````

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

## Access issues in Discovered inventory

If you see a message in **Server collection status** such as Missing credentials, or Access denied:

1. Select the server on the table of discovered servers.
2. Choose **Manage access credential** You can choose to:
   1. Select alternative credentials from the **Select credentials** dropdown.
   2. Select **Use new credentials** and provide new credentials.

3. **Save**.

The discovery tool retries the connection after you save your changes.

## Common error messages

This table describes common UI messages and their explanations:

| Message                                        | Location             | Explanation                                                                                                                        |
| ---------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| One or more credentials contain unknown UUIDs  | OS access page       | Race condition when two users edit OS credentials at the same time; try again                                                      |
| A password has already been created            | Create password page | Race condition when two users create passwords at the same time; refresh                                                           |
| Invalid password                               | Sign-in page         | Incorrect password for logging in; contact admin or reach out                                                                      |
| An on-demand collection is already in progress | Inventory page       | Race condition when two users start manual collections at the same time; try again after the current manual collection is finished |
| An internal error occurred                     | Various pages        | Retry or send logs                                                                                                                 |
| Export failed                                  | Inventory page       | Retry or send logs                                                                                                                 |
| Your session has expired. Please log in again. | Sign-in page         | Session has timed out, need to login again                                                                                         |
