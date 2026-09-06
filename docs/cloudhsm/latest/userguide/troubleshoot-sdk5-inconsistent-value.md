

# AWS CloudHSM Client SDK 5 user or policy contains inconsistent values
<a name="troubleshoot-sdk5-inconsistent-value"></a>

AWS CloudHSM does not automatically synchronize users or policies (such as mTLS settings) across HSMs in a cluster. The CloudHSM CLI performs best-effort synchronization of these operations across HSMs, but inconsistencies can still occur. This page describes how to identify and resolve inconsistencies for both users and policies. 

## Resolve inconsistent user values
<a name="troubleshoot-sdk5-inconsistent-value-users"></a>

The `user list` command in AWS CloudHSM Client SDK 5 returns a list of all users, and user properties, in your cluster. If any of a user's properties have the value "**inconsistent**", this user is not synchronized across your cluster. This means that the user exists with different properties on different HSMs in the cluster. Based on which property is inconsistent, different repair steps can be taken. 

 The following table includes steps to resolve inconsistencies for a single user. If a single user has multiple inconsistencies, resolve them by following these steps from top to bottom. If there are multiple users with inconsistencies, work through this list for each user, fully resolving the inconsistencies for that user before moving on the next. 

**Note**  
To perform these steps you should ideally be logged in as an admin. If your admin account is not consistent, go through these steps logging in with the admin and repeating the steps until all properties are consistent. After your admin account is consistent, you can proceed to use that admin to synchronize other users in the cluster.


| Inconsistent property | Example output of user list | Implication  | Recovery method  | 
| --- | --- | --- | --- | 
| User "role" is "inconsistent" | <pre>{<br />"username": <br />"test_user",    <br />"role": "inconsistent",    <br />"locked": "false",    <br />"mfa": [],     <br />"cluster-coverage": "full"<br />}</pre> | This user is a CryptoUser on some HSMs, and an Admin on other HSMs. This can happen if two SDKs attempt to create the same user, at the same time, with different roles.You must remove this user, and re-create it with the desired role. |  1. Login as an admin.<br />2.  Delete the user on all HSMs: <br />**user delete --username **<user's name>** --role admin** <br />**user delete --username **<user's name>** --role crypto-user** <br />3.  Create the user with the desired role: <br />**user create --username **<user's name>** --role **<desired role>**** <br />****   | 
| User "cluster-coverage" is "inconsistent" | <pre>{<br />"username": "test_user",    <br />"role": "crypto-user",    <br />"locked": "false",    <br />"mfa": [],     <br />"cluster-coverage": "inconsistent"<br />}</pre> | This user exists on a subset of HSMs in the cluster.This can happen if a **user create** partially succeeded, or if a **user delete** partially succeeded.<br />You must finish your previous operation, either creating or removing this user from your cluster. | If the user should not exist, follow these steps:1. Login as an admin.<br />2. Run this command: <br />**user delete --username**<user's name>** --role admin** <br />3. Now, run the following command: <br />**user delete --username**<user's name>** --role crypto-user** <br />If the user should exist, follow these steps:1. Login as an admin.<br />2. Run the following command: <br /> **user create --username **<user's name>** --role **<desired role>****   | 
| User "locked" parameter is "inconsistent" or "true" | <pre>{<br />"username": <br />"test_user",    <br />"role": "crypto-user",    <br />"locked": inconsistent,    <br />"mfa": [],     <br />"cluster-coverage": "full"<br />}</pre> | This user is locked out on a subset of HSMs.<br />This can happen if a user uses the wrong password and only connects to a subset of HSMs in the cluster.<br />You must change the user's credentials to be consistent across the cluster. | If the user has MFA activated, follow these steps:1. Login as an admin.<br />2. Run the following command to temporarily deactivate MFA: <br /> **user change-mfa token-sign --username **<user's name>** --role **<desired role>** --disable**  <br />3. Change the user's password so they can log into all HSMs: <br /> **user change-password --username **<user's name>** --role **<desired role>****  <br />If MFA should be active for the user, follow these steps:1. Have the user log in and re-enable MFA (this will require them to sign tokens and provide their public key in a PEM file):  <br /> **user change-mfa token-sign --username **<user's name>** --role **<desired role>** —token <File>**   | 
| MFA status is "inconsistent" | <pre>{    <br />"username": "test_user",    <br />"role": "crypto-user",    <br />"locked": "false",    <br />"mfa": [<br />  {            <br />   "strategy": "token-sign",<br />   "status": "inconsistent"<br />   }    <br />],     <br />"cluster-coverage": "full"<br />}</pre> | This user has different MFA flags on different HSMs in the cluster.<br />This can happen if an MFA operation only completed on a subset of HSMs.<br />You must reset the user's password, and allow them to re-enable MFA. | If the user has MFA activated, follow these steps:1. Login as an admin.<br />2. Run the following command to temporarily deactivate MFA: <br /> **user change-mfa token-sign --username **<user's name>** --role **<desired role>** --disable**  <br />3.  You will also need to then change the user's password so they can log into all HSMs: <br /> **user change-password --username **<user's name>** --role **<desired role>****  <br />If MFA should be active for the user, follow these steps:1. Have the user log in and re-enable MFA (this will require them to sign tokens and provide their public key in a PEM file):  <br /> **user change-mfa token-sign --username **<user's name>** --role **<desired role>** —token <File>**   | 

## Resolve inconsistent mTLS policy values
<a name="troubleshoot-sdk5-inconsistent-value-policies"></a>

Like users, mTLS policies (trust anchors and enforcement level) are not automatically synchronized across HSMs. The CloudHSM CLI performs best-effort synchronization when you run mTLS commands, but inconsistencies can still occur. You can check the synchronization status of your mTLS configuration using the following commands. 

### Check mTLS trust anchor synchronization
<a name="troubleshoot-sdk5-inconsistent-mtls-trust-anchors"></a>

Run the **cluster mtls list-trust-anchors** command to check the synchronization status of your trust anchors. In the output, each trust anchor has a `cluster-coverage` field. If the value is "**full**", the trust anchor is present on all HSMs. If the value is not "full", the trust anchor is not synchronized across all HSMs in the cluster. 

```
{
  "error_code": 0,
  "data": {
    "trust_anchors": [
      {
        "certificate-reference": "0x01",
        "certificate": "{{<PEM Encoded Certificate>}}",
        "cluster-coverage": "full"
      }
    ]
  }
}
```

If a trust anchor has inconsistent cluster coverage, re-run the registration or deregistration command to complete the operation:
+ To finish registering a trust anchor that is missing from some HSMs:

  **cluster mtls register-trust-anchor --path **<path-to-certificate>****
+ To finish deregistering a trust anchor that should be removed:

  **cluster mtls deregister-trust-anchor --certificate-reference **<certificate-reference>****

For more information about setting up mTLS, see [Set up mutual TLS between client and AWS CloudHSM](getting-started-setup-mtls.md).