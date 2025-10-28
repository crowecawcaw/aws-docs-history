# Updating password requirements for file system and SVM roles

You can update the password requirements for a file system or SVM role using the
[`security login role config modify`](https://docs.netapp.com/us-en/ontap-cli-9141/security-login-role-config-modify.html#description "https://docs.netapp.com/us-en/ontap-cli-9141/security-login-role-config-modify.html#description")
ONTAP CLI command. This command is only available to file system administrator accounts
with the `fsxadmin` role. When modifying password requirements,
the system will warn if there are any existing users with that role that will be impacted by the change.

The following example modifies the minimum length password requirement to 12 characters for users with the
`vsadmin-readonly` role on the `fsx` SVM. In this example, there are existing users with this role.

```
`FsxId0123456::>` `security login role config modify -role vsadmin-readonly -vserver fsx -passwd-minlength 12`
```

The system displays the following warning because of existing users:

```

`Warning: User accounts with this role exist. Modifications to the username/password restrictions on this role could result in non-compliant user
 accounts.
Do you want to continue? {y|n}:`

`FsxId0123456::>`
```
