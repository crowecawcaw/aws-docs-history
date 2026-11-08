

# Troubleshooting self-managed Active Directory for Amazon RDS for Oracle
<a name="oracle-smad-troubleshooting"></a>

Use the following information to resolve common problems with self-managed Active Directory (AD) for Amazon RDS for Oracle. To see the events that Amazon RDS emits for your DB instance, run [describe-events](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-events.html) or open the **Logs & events** tab of the DB instance in the console.

```
aws rds describe-events \
    --source-type db-instance \
    --source-identifier my-oracle-instance \
    --duration 1440
```

## Problems when you join a DB instance to the domain
<a name="oracle-smad-troubleshooting.join-problems"></a>


| Symptom | Likely cause | Action | 
| --- | --- | --- | 
| The API returns InvalidParameterCombination: The domain must have exactly two DNS endpoints. | You passed one address, or more than two, to --domain-dns-ips. | Pass exactly two addresses. If you have one DNS server, enter its address twice. | 
| The API rejects the secret Amazon Resource Name (ARN). | The secret is in a different AWS account or AWS Region than the DB instance. | Create the secret and AWS KMS key in the same account and Region as the DB instance. | 
| The status is enable-kerberos-failed, and the event reports that Amazon RDS can't read the secret. | The secret resource policy doesn't allow rds.amazonaws.com to call secretsmanager:GetSecretValue, the aws:sourceArn condition doesn't match the DB instance, or the AWS KMS key policy doesn't allow rds.amazonaws.com to call kms:Decrypt. | Correct the policies as shown in [Step 4: Create an AWS KMS key](oracle-smad-setting-up.md#oracle-smad-setting-up.step4) and [Step 5: Create a Secrets Manager secret](oracle-smad-setting-up.md#oracle-smad-setting-up.step5), and then retry the join. | 
| The status is enable-kerberos-failed, and the event reports invalid domain credentials. | The secret key names are wrong, the user name includes a domain prefix, the password is wrong, or the account is locked, disabled, or expired. | Make sure that the keys are exactly SELF\_MANAGED\_ACTIVE\_DIRECTORY\_USERNAME and SELF\_MANAGED\_ACTIVE\_DIRECTORY\_PASSWORD, and that the user name has no domain prefix. Unlock or reset the account in AD, update the secret, and retry the join. | 
| The status is enable-kerberos-failed, and the event reports that Amazon RDS can't reach the domain. | The DNS server addresses are wrong, or security groups, network ACLs, routes, or firewalls block traffic between the DB instance and your domain controllers. | Verify the addresses and the rules described in [Configure your network connectivity](oracle-smad-requirements.md#oracle-smad-requirements.configure-network), and then retry the join. | 
| The status is enable-kerberos-failed, and the event reports a permission or authorization error. | The Organizational Unit (OU) doesn't exist, the distinguished name is wrong, or the domain service account lacks one of the delegated permissions. | Verify the OU distinguished name, and complete [Step 3: Delegate control to the AD domain service account](oracle-smad-setting-up.md#oracle-smad-setting-up.step3). Then retry the join. | 

## Problems after the DB instance is joined
<a name="oracle-smad-troubleshooting.post-join-problems"></a>


| Symptom | Likely cause | Action | 
| --- | --- | --- | 
| The status is kerberos-enabled, but Amazon RDS emits an event that it can't reach the domain controllers. | A change to security groups, network ACLs, routes, VPN, or domain controller addresses broke connectivity between the DB instance and your domain. | Verify the addresses and the rules described in [Configure your network connectivity](oracle-smad-requirements.md#oracle-smad-requirements.configure-network). Restore connectivity on ports 53, 88, 464, and 389. If the domain controller addresses changed, modify the DB instance with the new --domain-dns-ips values. | 
| The status is kerberos-enabled, but Amazon RDS emits an event that it can't connect with the domain credentials. | The domain service account password changed in AD but not in the secret, or the account is locked, disabled, or expired. | Update the secret, or unlock the account. For details, see [Rotating the domain service account credentials](oracle-smad-managing.md#oracle-smad-managing.rotate-credentials). | 
| Kerberos sign-in fails on a restored DB instance or read replica. | The new DB instance wasn't joined to the domain. Its DomainMemberships list is empty. | Modify the new DB instance with the four domain parameters. | 
| Kerberos sign-in fails after you moved or deleted the AD user object that Amazon RDS created for the DB instance. | Amazon RDS creates one AD user object for each DB instance in the OU that you specify. The object's name is the first 20 characters of the DB instance resource ID in lowercase (for example, db-abcdefghij1234567). If you delete the object, the domain controller can't issue service tickets for the DB instance. If you move it out of the OU, Amazon RDS can't find it to rotate the Kerberos keys or update the configuration. | Don't move or delete this object. If you already deleted or moved it, modify the DB instance with the four domain parameters so that Amazon RDS recreates the object in the OU. | 

## Client connection errors
<a name="oracle-smad-troubleshooting.client-errors"></a>


| Error | Likely cause | Action | 
| --- | --- | --- | 
| ORA-01017: invalid username/password; logon denied | The Kerberos ticket is valid, but no Oracle user exists for the principal, or the user name doesn't match the principal in uppercase. | Create the user as described in [Step 2: Create Kerberos authentication Oracle logins](oracle-smad-connecting.md#oracle-smad.connecting.step2). In a multitenant DB instance, make sure that you created the user in the pluggable database (PDB) that you connect to. | 
| ORA-18925: Error during Kerberos5 authentication | General client-side Kerberos failure on the JDBC connection. Most often there is no Kerberos ticket in the credential cache, or the ticket has expired. | Run klist to confirm that a valid ticket exists, and run kinit if it doesn't. | 
| ORA-18923: The service in process is not supported: No valid credentials provided (Mechanism level: Clock skew too great (37)) | The client clock differs from the domain controller clock by more than the domain's maximum tolerance, which is 5 minutes by default. Kerberos error `37` is `KRB_AP_ERR_SKEW`.<br />Note that `kinit` can still succeed in this situation, because the MIT Kerberos client reads the Key Distribution Center (KDC)'s time from the `KRB_AP_ERR_SKEW` response and retries with an offset. The failure therefore appears when the application connects, not when the ticket is obtained.<br />The `ORA-18923` message text, *The service in process is not supported: No valid credentials provided*, is generic and doesn't identify the cause on its own. Read the `Mechanism level` clause to determine it. | Synchronize the client clock with your domain and reconnect. The same error can also appear when a ticket is very close to expiry. | 
| kinit: KDC has no support for encryption type | Your domain controllers don't allow an encryption type that the client or the RDS service account supports. | Allow AES128-CTS-HMAC-SHA1-96 or AES256-CTS-HMAC-SHA1-96 on your domain controllers and for the user account. | 