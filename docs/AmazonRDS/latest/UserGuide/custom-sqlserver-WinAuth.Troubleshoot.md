

# Troubleshooting Active Directory
<a name="custom-sqlserver-WinAuth.Troubleshoot"></a>

The following are issues you might encounter when you set up or modify an AD.


| Error Code | Description | Common causes | Troubleshooting suggestions | 
| --- | --- | --- | --- | 
| Error 2 / 0x2 | The system cannot find the file specified. | The format or location for the Organizational Unit (OU) specified with the `—domain-ou` parameter is invalid. The domain service account specified via AWS Secrets Manager lack the permissions required to join the OU. | Review the `—domain-ou` parameter. Ensure the domain service account has the correct permissions to the OU. | 
| Error 5 / 0x5 | Access is denied. | Misconfigured permissions for the domain service account, or the computer account already exists in the domain. | Review the domain service account permissions in the domain, and verify that the RDS computer account is not duplicated in the domain. You can verify the name of the RDS computer account by running `SELECT @@SERVERNAME` on your RDS Custom for SQL Server DB instance. If you are using Multi-AZ, try rebooting with failover and then verify that the RDS computer account again. For more information, see [Rebooting a DB instance](USER_RebootInstance.md). | 
| Error 87 / 0x57 | The parameter is incorrect. | The domain service account specified via AWS Secrets Manager doesn't have the correct permissions. The user profile may also be corrupted. | Review the requirements for the domain service account. | 
| Error 234 / 0xEA | Specified Organizational Unit (OU) does not exist. | The OU specified with the `—domain-ou` parameter doesn't exist in your AD. | Review the `—domain-ou` parameter and ensure the specified OU exists in your AD. | 
| Error 1326 / 0x52E | The user name or password is incorrect. | The domain service account credentials provided in AWS Secrets Manager contains an unknown username or bad password. The domain account may also be disabled in your AD. | Ensure the credentials provided in AWS Secrets Manager are correct and the domain account is enabled in your Active Directory. | 
| Error 1355 / 0x54B | The specified domain either does not exist or could not be contacted. | The domain is down, the specified set of DNS IPs are unreachable, or the specified FQDN is unreachable. | Review the `—domain-dns-ips` and `—domain-fqdn` parameters to ensure they're correct. Review the networking configuration of your RDS Custom for SQL Server DB instance and ensure your AD is reachable. | 
| Error 1722 / 0x6BA | The RPC server is unavailable. | There was an issue reaching the RPC service of your AD domain. This might be a service or network issue. | Validate that the RPC service is running on your domain controllers and that the TCP ports `135` and `49152-65535` are reachable on your domain from your RDS Custom for SQL Server DB instance. | 
| Error 2224 / 0x8B0 | The user account already exists. | The computer account that's attempting to be added to your AD already exists. | Identify the computer account by running `SELECT @@SERVERNAME` on your RDS Custom for SQL Server DB instance and then carefully remove it from your AD. | 
| Error 2242 / 0x8c2 | The password of this user has expired. | The password for the domain service account specified via AWS Secrets Manager has expired. | Update the password for the domain service account used to join your RDS Custom for SQL Server DB instance to your AD. | 