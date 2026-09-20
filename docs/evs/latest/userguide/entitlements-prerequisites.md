

# Prerequisites for Windows Server entitlements
<a name="entitlements-prerequisites"></a>

Before you set up Windows Server entitlements for the virtual machines (VMs) running in your Amazon EVS environment, make sure that you meet the following requirements:
+ You have an active Amazon EVS environment.
+ You have a dedicated vCenter user for the connector to use. We recommend that you assign this user a ReadOnly role. Avoid using credentials with elevated or administrative permission.
+ You have created a secret in AWS Secrets Manager that contains your appliance credentials. The secret must contain two keys, `username` and `password`, whose values are the login credentials for the dedicated vCenter user.
+ You have added the tag `EvsAccess=true` to your Secrets Manager secret. If you encrypted the secret with your own AWS KMS key, then you have also added the `EvsAccess=true` tag to the AWS KMS key.
+ The VMs that you want to cover are running a supported Windows Server guest operating system.