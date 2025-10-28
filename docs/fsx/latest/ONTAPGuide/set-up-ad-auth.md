# Configuring Active Directory authentication for ONTAP users

Use the ONTAP CLI to configure the use of Active Directory authentication for ONTAP file system and SVM users.

You must be a file system administrator with the `fsxadmin` role to use the commands in this procedure.

###### To set up Active Directory authentication for ONTAP users (ONTAP CLI)

The commands in this procedure are available to file system users with the `fsxadmin` role.

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Use the [`security login domain-tunnel create`](https://docs.netapp.com/us-en/ontap-cli-9141/security-login-domain-tunnel-create.html "https://docs.netapp.com/us-en/ontap-cli-9141/security-login-domain-tunnel-create.html") command as shown to establish a domain tunnel
for authenticating Windows Active Directory users. Replace `svm_name`
with the name of the SVM you are using for the domain tunnel.

```
`FsxId0123456::>` `security login domain-tunnel create -vserver `svm_name``
```

3. Use the [`security login create`](https://docs.netapp.com/us-en/ontap-cli-9141/security-login-create.html "https://docs.netapp.com/us-en/ontap-cli-9141/security-login-create.html") command to create
   Active Directory domain user accounts that will access the file system.

Specify the following required parameters in the command:

    * `-vserver` – The name of the SVM configured with CIFS and is joined to your Active Directory.
     It will be used as the tunnel for authenticating Active Directory domain users' to the file system.
     which the new role or user will be created.
    * `-user-or-group-name` – The username or Active
     Directory group name of the login method. The Active Directory group
     name can be specified only with the `domain` authentication
     method and `ontapi` and `ssh` application.
    * `-application` – The application of the login
     method. Possible values include http, ontapi, and ssh.
    * `-authentication-method` – The authentication method
     used for login. Possible values include the following:




    	+ domain – for Active Directory authentication
    	+ password – for password authentication
    	+ publickey – for public-key authentication
    * `-role` – The access-control role name for the login
     method. At the file system-level, the only role that can be specified is
     `-role fsxadmin`.

The following example creates an Active Directory domain user account `CORP\Admin` for the `filesystem1` file system.

```
`FSxId012345::>` security login create -vserver filesystem1 -username CORP\Admin -application ssh -authmethod domain -role fsxadmin
```

The following example creates the `CORP\Admin` user account with public key authentication.

```
`FsxId0123456ab::>` `security login create -user-or-group-name "CORP\Admin" -application ssh -authentication-method publickey -role fsxadmin`
`Warning: To use public-key authentication, you must create a public key for user "CORP\Admin".`
```

Create a public key for the `CORP\Admin` user using the following command:

```
`FsxId0123456ab::>` security login publickey create -username "CORP\Admin" -publickey "ecdsa-sha2-nistp256 `SECRET_STRING_HERE_IS_REDACTED`= cwaltham@b0be837a91bf.ant.amazon.com"
```

###### To log in to file system using SSH with Active Directory credentials

- The following example demonstrates how to SSH into your file system with your
  Active Directory credentials if you choose `ssh` for the
  `-application` type. The `username` is in the format
  `"domain-name\user-name"`, which is the domain name and the
  username that you provided when creating the account, separated by a backslash
  and enclosed in quotations.

```
`Fsx0123456::>` `ssh "CORP\user"@management.fs-abcdef01234567892.fsx.us-east-2.aws.com`
```

When prompted to enter a password, use the Active Directory user's password.
