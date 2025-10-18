# Get information for each HSM in an AWS CloudHSM cluster
 using CMU

Use the **info** command in the AWS CloudHSM cloudhsm\_mgmt\_util (CMU) to get information about
 each of the hardware security modules (HSM) in the AWS CloudHSM cluster, including the host name, port,
 IP address and the name and type of the user who is logged in to cloudhsm\_mgmt\_util on the HSM.

Before you run any CMU command, you must start CMU and log in to the HSM. Be
 sure that you log in with a user type that can run the commands you plan to
 use.

If you add or delete HSMs, update the
 configuration files for CMU.
 Otherwise, the changes that you make might not be effective for all HSMs in the cluster.


## User type


The following types of users can run this command.



* All users. You do not have to be logged in to run this command.

## Syntax

 Because this command does not have named parameters, you must enter the arguments in the
 order specified in the syntax diagram.



```
info server `<server ID>`
```

## Example


This example uses **info** to get information about an HSM in the cluster.
 The command uses 0 to refer to the first HSM in the cluster. The output shows the IP address,
 port, and the type and name of the current user.



```
`aws-cloudhsm>` `info server 0`
`Id Name Hostname Port State Partition LoginState
0 10.0.0.1 10.0.0.1 2225 Connected hsm-udw0tkfg1ab Logged in as 'testuser(CU)'`
```

## Arguments

 Because this command does not have named parameters, you must enter the arguments in the
 order specified in the syntax diagram.

 
```
info server `<server ID>`
```



**<server id>**

Specifies the server ID of the HSM. The HSMs are assigned ordinal numbers that
 represent the order in which they are added to the cluster, beginning with 0. To find
 the server ID of an HSM, use getHSMInfo.


Required: Yes




## Related topics



* [getHSMInfo](cloudhsm_mgmt_util-getHSMInfo.md "cloudhsm_mgmt_util-getHSMInfo.md")
* [loginHSM and logoutHSM](cloudhsm_mgmt_util-loginLogout.md "cloudhsm_mgmt_util-loginLogout.md")
