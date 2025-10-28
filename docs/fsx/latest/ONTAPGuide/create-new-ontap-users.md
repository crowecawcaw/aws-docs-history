# Creating ONTAP users

###### To create a new SVM or file system user (ONTAP CLI)

Only file system users with the `fsxadmin` role can create new SVM and file system users.

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Use the `security login create` ONTAP CLI command to create a new user account
on your FSx for ONTAP file system or SVM.

Insert your data for the placeholders in the example to define the following required properties:

    * `-vserver` – Specifies the name of the SVM
     where you want to create the new SVM role or user. If you are creating a
     file system role or user, don't specify an SVM.
    * `-user-or-group-name` – Specifies the username or Active
     Directory group name of the login method. The Active Directory group
     name can be specified only with the `domain` authentication
     method and the `ontapi` and `ssh` applications.
    * `-application` – Specifies the application of the login method.
     Possible values include http, ontapi, and ssh.
    * `-authentication-method` – Specifies the authentication method
     for login. Possible values include the following:




    	+ domain – Use for Active Directory authentication
    	+ password – Use for password authentication
    	+ publickey – User for public-key authentication
    * `-role` – Specifies the access-control role name for the login method.
     At the file system-level, the only role that can be specified is `fsxadmin`.

(Optional) You can also use one or more of the following parameters with the
command:

    * `[-comment]` – Use to include a notation or comment for the user
     account. For example, `Guest account`. The maximum
     length is 128 characters.
    * `[-second-authentication-method {none|publickey|password|nsswitch}]` – Specifies
     the second factor authentication method. You can specify the following methods:




    	+ password – Use for password authentication
    	+ publickey – Use for Public-key authentication
    	+ nsswitch – Use for NIS or LDAP authentication
    	+ none – The default value if you don't specify one

```
`Fsx0123456::>` `security login create -vserver `vserver_name` -user-or-group-name `user_or_group_name` -application `login_application` -authentication-method `auth_method` -role `role_or_account_name``
```

The following command creates a new file system user `new_fsxadmin` with the `fsxadmin-readonly`
role assigned, using SSH with a password for logging in. When prompted, provide a password for the user.

```
`Fsx0123456::>` `security login create -user-or-group-name new_fsxadmin -application ssh -authentication-method password -role fsxadmin-readonly`
`Please enter a password for user 'new_fsxadmin':
Please enter it again:

`Fsx0123456::>``
```

3. The following command creates a new SVM user `new_vsadmin` on the `fsx` SVM with the `vsadmin_readonly`
   role, configured to use SSH with a password to login. When prompted, provide a password for the user.

```
`Fsx0123456::>` `security login create -vserver fsx -user-or-group-name new_vsadmin -application ssh -authentication-method password -role vsadmin-readonly`
`Please enter a password for user 'new_vsadmin':
Please enter it again:

`Fsx0123456::>``
```

4. The following command creates a new read-only file system user `harvest2-user` that is to be used by the NetApp Harvest application to collect performance and capacity metrics.
   For more information, see [Monitoring FSx for ONTAP file systems using Harvest and Grafana](monitoring-harvest-grafana.md "monitoring-harvest-grafana.md").

```
`Fsx0123456::>` `security login create -user-or-group-name harvest2-user -application ssh -role fsxadmin-readonly -authentication-method password`
```

###### To view information for all file system and SVM users

- Use the following command to view all login information for your file system and SVMs.

```
`Fsx0123456::>` `security login show`
`Vserver: Fsx0123456
 Second
User/Group Authentication Acct Authentication
Name Application Method Role Name Locked Method
-------------- ----------- ------------- ---------------- ------ --------------
autosupport console password autosupport no none
fsxadmin http password fsxadmin no none
fsxadmin ontapi password fsxadmin no none
fsxadmin ssh password fsxadmin no none
fsxadmin ssh publickey fsxadmin - none
new_fsxadmin ssh password fsxadmin-readonly
 no none

Vserver: fsx
 Second
User/Group Authentication Acct Authentication
Name Application Method Role Name Locked Method
-------------- ----------- ------------- ---------------- ------ --------------
new_vsadmin ssh password vsadmin-readonly no none
vsadmin http password vsadmin yes none
vsadmin ontapi password vsadmin yes none
vsadmin ssh password vsadmin yes none
10 entries were displayed.

`Fsx0123456::>``
```
