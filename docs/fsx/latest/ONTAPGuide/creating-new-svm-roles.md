# Creating SVM roles

Each SVM that you create has a default SVM administrator that's assigned the
predefined `vsadmin` role. In addition to the set of [predefined SVM roles](roles-and-users.md#svm-admin-roles "roles-and-users.md#svm-admin-roles"),
you can create new SVM roles. If you need to create new roles for your SVM, use the
`security login role create` ONTAP CLI command. This command is available for
file system administrators with the `fsxadmin` role.

###### To create a new SVM role (ONTAP CLI)

1. You can create a new SVM role using the
   [`security login role create`](https://docs.netapp.com/us-en/ontap-cli-9141/security-login-role-create.html "https://docs.netapp.com/us-en/ontap-cli-9141/security-login-role-create.html") ONTAP CLI command:

```
`Fsx0123456::>` `security login role create -vserver `vs1.example.com` -role `vol_role` -cmddirname `volume``
```

2.  Specify the following required parameters in the command:
    - `-vserver` the name of the SVM
    - `-role`
      – The name of the role.
    - `-cmddirname` – The command or command directory to
      which the role gives access. Enclose command subdirectory names in
      double quotation marks. For example,
      `"volume
snapshot"`. Enter `DEFAULT` to
      specify all command directories.

3.  (Optional) You can also add any of the following parameters to the
    command:
    - `-vserver` – The name of the SVM that's associated
      with the role.
    - `-access` – The access level for the role. For
      command directories, this includes:

          + `none` – Denies access to commands in the
           command directory. This is the default value for custom
           roles.
          + `readonly` – Grants access to the show
           commands in the command directory and its subdirectories.
          + `all` – Grants access to all of the commands
           in the command directory and its subdirectories. To grant or deny access to intrinsic commands, you must specify the command
           directory.

      For non-intrinsic commands (commands that don't end in
      `create`, `modify`, `delete`, or
      `show`):

          + `none` – Denies access to commands in the
           command directory. This is the default value for custom
           roles.
          + `readonly` – Not applicable. Don't
           use.
          + `all` – Grants access to the command.

    - `-query` – The query object that's used to filter
      the access level, which is specified in the form of a valid option for
      the command, or for a command in the command directory. Enclose the
      query object in double quotation marks.

4.  Run the `security login role create` command.

The following command creates an access-control role named "admin" for the
vs1.example.com Vserver. The role has all access to the "volume" command but only within the "aggr0" aggregate.

```
`Fsx0123456::>`security login role create -role admin -cmddirname volume -query "-aggr aggr0" -access all -vserver vs1.example.com
```
