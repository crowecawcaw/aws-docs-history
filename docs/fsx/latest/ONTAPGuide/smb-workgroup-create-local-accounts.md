# Creating a local user account on the SMB server

You can create a local user account that can be used to authorize access to data contained in the SVM over an SMB connection.
You can also use local user accounts for authentication when creating an SMB session. Local user functionality is enabled by default
when the SVM is created. When you create a local user account, you must specify a user name and you must specify the SVM with which
to associate the account.

###### To create local user accounts on the SMB server

1. Create the local user using the
   [**vserver cifs users-and-groups local-user create**](https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-users-and-groups-local-user-create.html "https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-users-and-groups-local-user-create.html")
   ONTAP CLI command:

```
vserver cifs users-and-groups local-user create -vserver `svm_name` -user-name `user_name` optional_parameters
```

The following optional parameters might be useful:

    * `-full-name` – The user's full name.
    * `-description` – A description for the local user.
    * `-is-account-disabled {true|false}` – Specifies whether the user account is enabled or disabled. If this parameter is not specified,
     the default is to enable the user account.

The command prompts for the local user's password. 2. Enter a password for the local user, and then confirm the password. 3. Verify that the user was successfully created:

```
`vserver cifs users-and-groups local-user show -vserver `svm_name``
```

The following example creates a local user `SMB_SERVER01\sue`, with a full name `Sue Chang`, associated with SVM `svm1`:

```
`FSxIdabcde123456::>` `vserver cifs users-and-groups local-user create -vserver svm1 ‑user-name SMB_SERVER01\sue -full-name "Sue Chang"`

`Enter the password:
Confirm the password:`
```

```
`FSxIdabcde123456::>` `vserver cifs users-and-groups local-user show`
`Vserver User Name Full Name Description
-------- -------------------------- ---------- -------------
svm1 SMB_SERVER01\Administrator Built-in administrator account
svm1 SMB_SERVER01\sue Sue Chang`
```
