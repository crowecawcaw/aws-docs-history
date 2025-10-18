# Change the quorum minimum value for AWS CloudHSM
 using CloudHSM CLI

After [setting the quorum
 minimum value](quorum-auth-chsm-cli-first-time.md#quorum-admin-set-quorum-minimum-value-chsm-cli "quorum-auth-chsm-cli-first-time.md#quorum-admin-set-quorum-minimum-value-chsm-cli") for CloudHSM [admins](understanding-users.md#admin "understanding-users.md#admin"), you might need to adjust
 the quorum minimum value. The HSM allows changes to the quorum minimum value only when the
 number of approvers meets or exceeds the current value. For example, with a quorum minimum value
 of two (2), at least two (2) admins must approve any changes.

###### Note

The quorum value of the user service must always be less than or equal to the quorum value of the
 quorum service. For information on service names, see [Supported AWS CloudHSM service names and types
 for quorum authentication with CloudHSM CLI](quorum-auth-chsm-cli-service-names.md "quorum-auth-chsm-cli-service-names.md").

To get quorum approval to change the quorum minimum value, you need a *quorum
 token* for the **quorum service** using the **quorum token-sign set-quorum-value** command.
 To generate a quorum token for the for the **quorum service** using the **quorum token-sign set-quorum-value** 
 command, the quorum service must be higher than one (1). This means that before you can change the quorum minimum value for 
 *user service*, you might need to change the quorum minimum value for *quorum service*.

###### Steps to change the quorum minimum value for admins

1. Start the CloudHSM CLI interactive mode.



Linux
```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

Windows
```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive`
```
2. Using CloudHSM CLI, log in as an admin.



```
`aws-cloudhsm >` `login --username `<admin>` --role admin``Enter password:
{
 "error_code": 0,
 "data": {
 "username": "`<admin>`",
 "role": "admin"
 }
}`
```
3. Check current quorum minimum values:



```
`aws-cloudhsm >` `quorum token-sign list-quorum-values`
```
4. If the quorum minimum value for the quorum service is lower than the value for the user
 service, change the *quorum service* value:



```
`aws-cloudhsm >` `quorum token-sign set-quorum-value --service quorum --value `<3>``
```
5. [Generate a quorum token](quorum-auth-chsm-cli-admin.md#quorum-admin-gen-token-chsm-cli "quorum-auth-chsm-cli-admin.md#quorum-admin-gen-token-chsm-cli") for the quorum service.
6. [Get approvals (signatures) from other admins](quorum-auth-chsm-cli-admin.md#quorum-admin-get-approval-signatures-chsm-cli "quorum-auth-chsm-cli-admin.md#quorum-admin-get-approval-signatures-chsm-cli").
7. [Approve the token on the CloudHSM cluster and execute a user management operation.](quorum-auth-chsm-cli-admin.md#quorum-admin-approve-token-chsm-cli "quorum-auth-chsm-cli-admin.md#quorum-admin-approve-token-chsm-cli").
8. Change the quorum minimum value for the *user service*:



```
`aws-cloudhsm >` `quorum token-sign set-quorum-value`
```
###### Example Adjusting *quorum service* minimum values


1. **Check current values**. The example shows that the quorum minimum value for *user service* is
 currently two (2).



```
`aws-cloudhsm >` `quorum token-sign list-quorum-values``{
 "error_code": 0,
 "data": {
 "user": 2,
 "quorum": 1
 }
}`
```
2. **Change quorum service value**. Set the quorum minimum value for
 *quorum service* to a value that is the same or higher than the value
 for *user service*. This example sets the quorum minimum value for
 *quorum service* to two (2), the same value that was set for
 *user service* in the previous example.



```
`aws-cloudhsm >` `quorum token-sign set-quorum-value --service quorum --value 2``{
 "error_code": 0,
 "data": "Set quorum value successful"
}`
```
3. **Verify the changes**. This example shows that the quorum minimum value is now two (2) for *user service* and *quorum service*.



```
`aws-cloudhsm >` `quorum token-sign list-quorum-values``{
 "error_code": 0,
 "data": {
 "user": 2,
 "quorum": 2
 }
}`
```
