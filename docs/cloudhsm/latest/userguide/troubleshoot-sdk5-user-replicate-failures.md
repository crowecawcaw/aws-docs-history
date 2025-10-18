# AWS CloudHSM Client SDK 5 user replicate
 failures

The `user replicate` command in the CloudHSM CLI replicates a user between cloned AWS CloudHSM clusters.
 This guide addresses failures due to user inconsistencies within the source cluster or between the source and destination clusters.
 User replicate verifies that users are consistent by checking the following attributes:
 


* User Role
* Account Lock Status
* Quorum Status
* Multi-Factor Authentication (MFA) Status

## Problem: The selected user is not synchronized throughout the cluster


The user replication process checks for user synchronization throughout the source cluster. 
 If a user's attribute has the value "inconsistent", this means the user isn't synchronized across the cluster. 
 User replication fails with the following error message:
 



```
{
  "error_code": 1,
  "data": "Specified user is inconsistent across the cluster"
}
```

To check for user desynchronization in the source cluster:


* Run the `user list` command in the CloudHSM CLI.


```
`aws-cloudhsm >` `user list``{
 "error_code": 0,
 "data": {
 "users": [
 {
 "username": "admin",
 "role": "admin",
 "locked": "false",
 "mfa": [],
 "quorum": [],
 "cluster-coverage": "full"
 },
 {
 "username": "example-inconsistent-user",
 "role": "admin",
 "locked": "false",
 "mfa": [],
 "quorum": [],
 "cluster-coverage": "inconsistent"
 },
 {
 "username": "app_user",
 "role": "internal(APPLIANCE_USER)",
 "locked": "false",
 "mfa": [],
 "quorum": [],
 "cluster-coverage": "full"
 }
 ]
 }
}`
      
```

###### Resolution: Synchronize user attributes throughout the source cluster

* To synchronize user information throughout the source cluster, refer to the following:
 [AWS CloudHSM Client SDK 5 user contains
 inconsistent values](troubleshoot-sdk5-inconsistent-value.md "troubleshoot-sdk5-inconsistent-value.md").

## Problem: User exists on the destination cluster with different attributes


 If a user already exists with the same reference exists in one or more HSMs in the destination cluster but has different
 user attributes, the following error may occur: 



```
{
  "error_code": 1,
  "data": "User replicate failed on 1 of 3 connections"
}
```

###### Resolution

1. Determine which version of the user should be kept.
2. Delete the unwanted user in the appropirate cluster by running the `user delete` command.
 See [Delete an AWS CloudHSM user with CloudHSM CLI](cloudhsm_cli-user-delete.md "cloudhsm_cli-user-delete.md") for more information.
3. Replicate the user by running the `user replicate` command.
