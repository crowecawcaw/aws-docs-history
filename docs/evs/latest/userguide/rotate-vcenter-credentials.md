

# Rotate vCenter connector credentials

A vCenter connector authenticates with vCenter Server by using the vCenter user credentials that you store in an AWS Secrets Manager secret. When you rotate the password of that vCenter user in VMware Cloud Foundation (VCF), you must give the connector the new credentials so that it can keep authenticating.

**Important**  
If the connector can’t authenticate, its reachability check fails and your Windows Server entitlements enter the `AT_RISK` status. If you don’t restore reachability within 8 hours, Amazon Elastic VMware Service removes the entitlements. To avoid this, give the connector the new credentials as soon as you change the password in vCenter Server.

You have two options:
+  **Update the existing secret.** Put the new credentials in the secret that the connector already uses. You don’t need to update the connector.
+  **Use a different secret.** Store the new credentials in another secret, and then update the connector to point to it.

## Update the existing secret
<a name="rotate-vcenter-credentials-same-secret"></a>

 **In the vSphere Client** 

1. Change the password of the vCenter user that the connector uses.

 **In the AWS console** 

1. In Secrets Manager, update the value of the secret that the connector uses. Keep the keys `username` and `password`, and enter the new password. For the steps, see [Modify an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret.html) in the * AWS Secrets Manager User Guide*.

1. Wait up to 10 minutes for the next reachability check.

1. In the Amazon EVS console, on the **Connectors** tab of your environment, check that the reachability check result is **Passed**. You can also run `aws evs list-environment-connectors --environment-id env-abcde12345`.

You have rotated the credentials when the reachability check result is `PASSED`.

## Use a different secret
<a name="rotate-vcenter-credentials-new-secret"></a>

1. Change the password of the vCenter user in the vSphere Client.

1. Create a secret with the keys `username` and `password` that contain the new credentials. Add the tag `EvsAccess=true` to the secret, and to the AWS KMS key if you encrypted the secret with your own key.

1. Update the connector to use the new secret. For the console and AWS CLI steps, see [Update a connector](evs-env-update-connector.md).

1. Check that the connector state is `ACTIVE` and the reachability check result is `PASSED`.

If the reachability check stays `FAILED`, see [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md).

To rotate the secrets that Amazon EVS creates, see [Manage secrets](evs-env-secret-rotation.md).