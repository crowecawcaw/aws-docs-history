# Delete an AWS CloudHSM user using CMU

Use the **deleteUser** command in the AWS CloudHSM cloudhsm\_mgmt\_util (CMU) to delete a user
 from the hardware security modules (HSM) in the AWS CloudHSM cluster. Only crypto officers (CO) can run
 this command. You cannot delete a user who is currently logged into an HSM. For more information
 about deleting users, see [How to Delete HSM Users](delete-user.md "delete-user.md").

###### Tip

You can't delete crypto users (CU) that own keys.


## User type


The following types of users can run this command.



* CO

## Syntax

 Because this command does not have named parameters, you must enter the arguments in the
 order specified in the syntax diagram.



```
deleteUser `<user-type>` `<user-name>`
```

## Example


This example deletes a crypto officer (CO) from the HSMs in a cluster. The first command
 uses [listUsers](cloudhsm_mgmt_util-listUsers.md "cloudhsm_mgmt_util-listUsers.md") to list all users on the
 HSMs.


The output shows that user `3`, `alice`, is a CO on the HSMs.



```
`aws-cloudhsm>` `listUsers`
Users on server 0(10.0.0.1):
Number of users found:3

    User Id             User Type       User Name                          MofnPubKey    LoginFailureCnt         2FA
         1              PCO             admin                                   YES               0               NO
         2              AU              app_user                                 NO               0               NO
         3              CO              alice                                    NO               0               NO
Users on server 1(10.0.0.2):
Number of users found:3

    User Id             User Type       User Name                          MofnPubKey    LoginFailureCnt         2FA
         1              PCO             admin                                   YES               0               NO
         2              AU              app_user                                 NO               0               NO
         3              CO              alice                                    NO               0               NO

Users on server 1(10.0.0.3):
Number of users found:3

    User Id             User Type       User Name                          MofnPubKey    LoginFailureCnt         2FA
         1              PCO             admin                                   YES               0               NO
         2              AU              app_user                                 NO               0               NO
         3              CO              alice                                    NO               0               NO
```

The second command uses the **deleteUser** command to delete
 `alice` from the HSMs. 


The output shows that the command succeeded on all three HSMs in the cluster.



```
`aws-cloudhsm>` `deleteUser CO alice`
`Deleting user alice(CO) on 3 nodes
deleteUser success on server 0(10.0.0.1)
deleteUser success on server 0(10.0.0.2)
deleteUser success on server 0(10.0.0.3)`
```

The final command uses the **listUsers** command to verify that
 `alice` is deleted from all three of the HSMs on the cluster.



```
`aws-cloudhsm>` `listUsers`
Users on server 0(10.0.0.1):
Number of users found:2

    User Id             User Type       User Name                          MofnPubKey    LoginFailureCnt         2FA
         1              PCO             admin                                   YES               0               NO
         2              AU              app_user                                 NO               0               NO
Users on server 1(10.0.0.2):
Number of users found:2

    User Id             User Type       User Name                          MofnPubKey    LoginFailureCnt         2FA
         1              PCO             admin                                   YES               0               NO
         2              AU              app_user                                 NO               0               NO
Users on server 1(10.0.0.3):
Number of users found:2

    User Id             User Type       User Name                          MofnPubKey    LoginFailureCnt         2FA
         1              PCO             admin                                   YES               0               NO
         2              AU              app_user                                 NO               0               NO
```

## Arguments

 Because this command does not have named parameters, you must enter the arguments in the
 order specified in the syntax diagram.

 
```
deleteUser `<user-type>` `<user-name>`
```



**<user-type>**

Specifies the type of user. This parameter is required. 


###### Tip

You can't delete crypto users (CU) that own keys.


Valid values are **CO**, **CU**.


To get the user type, use [listUsers](cloudhsm_mgmt_util-listUsers.md "cloudhsm_mgmt_util-listUsers.md"). For detailed information about the user types on an HSM, see [HSM user types for AWS CloudHSM Management Utility](understanding-users-cmu.md "understanding-users-cmu.md").


Required: Yes



**<user-name>**

Specifies a friendly name for the user. The maximum length is 31 characters. The
 only special character permitted is an underscore ( \_ ).


You cannot change the name of a user after it is created. In cloudhsm\_mgmt\_util commands, the
 user type and password are case-sensitive, but the user name is not.


Required: Yes




## Related topics



* [listUsers](cloudhsm_mgmt_util-listUsers.md "cloudhsm_mgmt_util-listUsers.md")
* [createUser](cloudhsm_mgmt_util-createUser.md "cloudhsm_mgmt_util-createUser.md")
* [syncUser](cloudhsm_mgmt_util-syncUser.md "cloudhsm_mgmt_util-syncUser.md")
* [changePswd](cloudhsm_mgmt_util-changePswd.md "cloudhsm_mgmt_util-changePswd.md")
