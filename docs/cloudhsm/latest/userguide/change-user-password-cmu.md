# Change HSM user passwords using AWS CloudHSM
 Management Utility


 Use **changePswd** in the AWS CloudHSM Management Utility (CMU) to change a hardware security module (HSM) user's password. 
 


 User types and passwords are
 case sensitive, but user names are not case sensitive.

 
 CO, Crypto user (CU), and appliance user (AU) can change their own password. To change the 
 password of another user, you must log in as a CO. You cannot change the password of a user who
 is currently logged in.
 

###### To change your own password

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
3. Log in to the HSM.



```
`aws-cloudhsm >` `loginHSM CO admin co12345`
```

Make sure the number of connections CMU lists match the number of HSMs in the cluster. 
 If not, log out and start over.
4. Use **changePswd** to change your own password. 



```
`aws-cloudhsm >` `changePswd CO example_officer `<new password>``
```

CMU prompts you about the change password operation.



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


CMU prompts you about the change password operation.



```
`Changing password for example_officer(CO) on 3 nodes`
```
###### To change the password of another user

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
4. Use **changePswd** to change the password of another user. 
 



```
`aws-cloudhsm >` `changePswd CU example_user `<new password>``
```

CMU prompts you about the change password operation.



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


CMU prompts you about the change password operation.



```
`Changing password for example_user(CU) on 3 nodes`
```
For more information about **changePswd**, see [changePswd](cloudhsm_mgmt_util-changePswd.md "cloudhsm_mgmt_util-changePswd.md").
