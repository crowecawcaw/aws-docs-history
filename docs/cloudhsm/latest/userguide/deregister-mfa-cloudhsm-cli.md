# Deregister an MFA public key using
 CloudHSM CLI

Follow these steps to deregister a multi-factor authentication (MFA) public key for AWS CloudHSM
 admin users when MFA public key is registered.

1. Use CloudHSM CLI to log in to the HSM as an admin with MFA enabled.
2. Use the **user change-mfa token-sign** command to remove MFA for a user.



```
`aws-cloudhsm >` `user change-mfa token-sign --username `<username>` --role admin --deregister --change-quorum``Enter password:
Confirm password:
{
 "error_code": 0,
 "data": {
 "username": "`<username>`",
 "role": "admin"
 }
}`
```
