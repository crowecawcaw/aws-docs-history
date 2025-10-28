# Adding local users to the local group

You can manage local group membership by adding and removing local or domain users, or adding and removing domain groups. This is useful if
you want to control access to data based on access controls placed on the group, or if you want users to have privileges associated with that group.
If you no longer want a local user, domain user, or domain group to have access rights or privileges based on membership in a group, you can remove
the member from the group.

When adding members to a local group, keep the following in mind:

- You cannot add users to the special _Everyone_ group.
- You cannot add a local group to another local group.
- To add a domain user or group to a local group, ONTAP must be able to resolve the name to a SID.
  When removing members from a local group, keep the following in mind:

- You cannot remove members from the special _Everyone_ group.
- To remove a member from a local group, ONTAP must be able to resolve their name to a SID.
  You need to have the `fsxadmin` role to run the commands used in this procedure. For more information, see [ONTAP roles and users](roles-and-users.md "roles-and-users.md").

###### To manage the local group membership

- Add a member to or remove a member from a group using the
  [**vserver cifs users-and-groups local-group add-members**](https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-users-and-groups-local-group-add-members.html "https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-users-and-groups-local-group-add-members.html")
  and
  [vserver cifs users-and-groups local-group remove-members](https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-users-and-groups-local-group-remove-members.html "https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-users-and-groups-local-group-remove-members.html")
  ONTAP CLI commands.

      + To add members to a workgroup:



      ```
      vserver cifs users-and-groups local-group add-members ‑vserver `svm_name` -group-name `group_name` ‑member-names name[,...]
      ```

      You can specify a comma-delimited list of local users, domain users, or domain groups to add to the specified local group.
      + To view members of a workgroup:



      ```
      vserver cifs users-and-groups local-group show-members -vserver `svm_name` -group-name `group_name`
      ```
      + To remove members from a workgroup:



      ```
      vserver cifs users-and-groups local-group remove-members ‑vserver `svm_name` -group-name `group_name` ‑member-names name[,...]
      ```

      You can specify a comma-delimited list of local users, domain users, or domain groups to remove from the specified local group.

  The following example adds a local user `SMB_SERVER01\sue` to the local group `SMB_SERVER01\engineering` on SVM `svm1`:

```
`FSxIdabcde123456::>` `vserver cifs users-and-groups local-group add-members -vserver svm1 -group-name SMB_SERVER01\engineering -member-names SMB_SERVER01\sue`
```

The following example removes the local user `SMB_SERVER01\sue` and `SMB_SERVER01\james` from the local group `SMB_SERVER01\engineering` on SVM `svm1`:

```
`FSxIdabcde123456::>` `vserver cifs users-and-groups local-group remove-members -vserver svm1 -group-name SMB_SERVER01\engineering -member-names SMB_SERVER01\sue,SMB_SERVER01\james`
```

The following example lists the members of the local group `SMB_SERVER01\engineering`:

```
`FsxIdabcdef01234::>` `vserver cifs users-and-groups local-group show-members -vserver `svm_name` -group-name `group_name``
`Vserver: svm1
 Domain Name: SMB_SERVER01
 Group Name: SMB_SERVER01\engineering
 Member Name: SMB_SERVER01\anita
 SMB_SERVER01\james
 SMB_SERVER01\liang`
```
