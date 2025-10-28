# Delete HSM users using AWS CloudHSM Management Utility

Use **deleteUser** in the AWS CloudHSM Management Utility (CMU) to delete a hardware security module (HSM) user. You must log in as a CO to delete another user.

###### Tip

You can't delete crypto users (CU) that own keys.

###### To delete a user

1. Use the configure tool to update the CMU configuration.

Linux

```
`$` `sudo /opt/cloudhsm/bin/configure --cmu `<IP address>``
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\configure.exe" --cmu `<IP address>``
```

2. Start CMU.

Linux

```
`$` `/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\cloudhsm_mgmt_util.exe" C:\ProgramData\Amazon\CloudHSM\data\cloudhsm_mgmt_util.cfg`
```

3. Log in to the HSM as a CO user.

```
`aws-cloudhsm >` `loginHSM CO admin co12345`
```

Make sure the number of connections CMU lists match the number of HSMs in the cluster.
If not, log out and start over. 4. Use **deleteUser** to delete a user.

```
`aws-cloudhsm >` `deleteUser CO example_officer`
```

CMU deletes the user.

```
`Deleting user example_officer(CO) on 3 nodes
deleteUser success on server 0(10.0.2.9)
deleteUser success on server 1(10.0.3.11)
deleteUser success on server 2(10.0.1.12)`
```

For more information about **deleteUser**, see [deleteUser](cloudhsm_mgmt_util-deleteUser.md "cloudhsm_mgmt_util-deleteUser.md").
