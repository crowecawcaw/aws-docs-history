# Create HSM users using AWS CloudHSM Management
 Utility

Use **createUser** in AWS CloudHSM Management Utility (CMU) to create new
 users on the hardware security module (HSM). You must log in as a CO to create a user.

###### To create a new CO user

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
 If not, log out and start over.
4. Use **createUser** to create a CO user named
 `example_officer` with a password of
 `password1`.



```
`aws-cloudhsm >` `createUser CO example_officer password1`
```

CMU prompts you about the create user operation.



```
`*************************CAUTION********************************
This is a CRITICAL operation, should be done on all nodes in the
cluster. AWS does NOT synchronize these changes automatically with the
nodes on which this operation is not executed or failed, please
ensure this operation is executed on all nodes in the cluster.
****************************************************************

Do you want to continue(y/n)?`
```
5. Type `y`.
###### To create a new CU user

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
 If not, log out and start over.
4. Use **createUser** to create a CU user named
 `example_user` with a password of
 `password1`.



```
`aws-cloudhsm >` `createUser CU example_user password1`
```

CMU prompts you about the create user operation.



```
`*************************CAUTION********************************
This is a CRITICAL operation, should be done on all nodes in the
cluster. AWS does NOT synchronize these changes automatically with the
nodes on which this operation is not executed or failed, please
ensure this operation is executed on all nodes in the cluster.
****************************************************************

Do you want to continue(y/n)?`
```
5. Type `y`.
For more information about **createUser**, see [createUser](cloudhsm_mgmt_util-createUser.md "cloudhsm_mgmt_util-createUser.md").
