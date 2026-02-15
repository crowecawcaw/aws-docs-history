# Change the quorum

minimum value with AWS CloudHSM Management Utility

After you [set the quorum
minimum value](quorum-authentication-crypto-officers-first-time-setup.md#quorum-crypto-officers-set-quorum-minimum-value "quorum-authentication-crypto-officers-first-time-setup.md#quorum-crypto-officers-set-quorum-minimum-value") so that AWS CloudHSM [crypto officers (COs)](understanding-users-cmu.md#crypto-officer "understanding-users-cmu.md#crypto-officer")
can use quorum authentication, you might want to change the quorum minimum value. The HSM allows
you to change the quorum minimum value only when the number of approvers is the same or higher
than the current quorum minimum value. For example, if the quorum minimum value is two, at least
two COs must approve to change the quorum minimum value.

To get quorum approval to change the quorum minimum value, you need a _quorum
token_ for the **setMValue** command (service 4). To get a quorum token
for the **setMValue** command (service 4), the quorum minimum value for service 4
must be higher than one. This means that before you can change the quorum minimum value for COs
(service 3), you might need to change the quorum minimum value for service 4.

The following table lists the HSM service identifiers along with their names,
descriptions, and the commands that are included in the service.

| Service Identifier | Service Name | Service Description      | HSM Commands                                                                                                                  |
| ------------------ | ------------ | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| 3                  | `USER_MGMT`  | HSM user management      | • **createUser**<br>• **deleteUser**<br>• **changePswd** (applies only when changing the password of a<br>different HSM user) |
| 4                  | `MISC_CO`    | Miscellaneous CO service | • **setMValue**                                                                                                               |

###### To change the quorum minimum value for crypto officers

1. Use the following command to start the cloudhsm_mgmt_util command
   line tool.

```
`$` `/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg`
```

2. Use the **loginHSM** command to log in to the HSM as a CO. For more information, see [HSM user management with CloudHSM Management Utility
   (CMU)](manage-hsm-users-cmu.md "manage-hsm-users-cmu.md").
3. Use the **getMValue** command to get the quorum minimum value for
   service 3. For more information, see the following example.
4. Use the **getMValue** command to get the quorum minimum value for
   service 4. For more information, see the following example.
5. If the quorum minimum value for service 4 is lower than the value for service 3, use the
   **setMValue** command to change the value for service 4. Change the value for
   service 4 to one that is the same or higher than the value for service 3. For more
   information, see the following example.
6. [Get a quorum
   token](quorum-authentication-crypto-officers.md#quorum-crypto-officers-get-token "quorum-authentication-crypto-officers.md#quorum-crypto-officers-get-token"), taking care to specify service 4 as the service for which you can
   use the token.
7. [Get approvals
   (signatures) from other COs](quorum-authentication-crypto-officers.md#quorum-crypto-officers-get-approval-signatures "quorum-authentication-crypto-officers.md#quorum-crypto-officers-get-approval-signatures").
8. [Approve the token on the
   HSM](quorum-authentication-crypto-officers.md#quorum-crypto-officers-approve-token "quorum-authentication-crypto-officers.md#quorum-crypto-officers-approve-token").
9. Use the **setMValue** command to change quorum minimum value for
   service 3 (user management operations performed by COs).

###### Example– Get quorum minimum values and change the value for service 4

The following example command shows that the quorum minimum value for service 3 is
currently two.

```
`aws-cloudhsm >` `getMValue 3``MValue of service 3[USER_MGMT] on server 0 : [2]
MValue of service 3[USER_MGMT] on server 1 : [2]`
```

The following example command shows that the quorum minimum value for service 4 is
currently one.

```
`aws-cloudhsm >` `getMValue 4``MValue of service 4[MISC_CO] on server 0 : [1]
MValue of service 4[MISC_CO] on server 1 : [1]`
```

To change the quorum minimum value for service 4, use the **setMValue**
command, setting a value that is the same or higher than the value for service 3. The
following example sets the quorum minimum value for service 4 to two (2), the same value that
is set for service 3.

```
`aws-cloudhsm >` `setMValue 4 2``*************************CAUTION********************************
This is a CRITICAL operation, should be done on all nodes in the
cluster. AWS does NOT synchronize these changes automatically with the
nodes on which this operation is not executed or failed, please
ensure this operation is executed on all nodes in the cluster.
****************************************************************

Do you want to continue(y/n)? `y`
Setting M Value(2) for 4 on 2 nodes`
```

The following commands show that the quorum minimum value is now two for service 3 and
service 4.

```
`aws-cloudhsm >` `getMValue 3``MValue of service 3[USER_MGMT] on server 0 : [2]
MValue of service 3[USER_MGMT] on server 1 : [2]`
```

```
`aws-cloudhsm >` `getMValue 4``MValue of service 4[MISC_CO] on server 0 : [2]
MValue of service 4[MISC_CO] on server 1 : [2]`
```
