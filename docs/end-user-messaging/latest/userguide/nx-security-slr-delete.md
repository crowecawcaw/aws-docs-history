

# Deleting a service-linked role for AWS End User Messaging
<a name="nx-security-slr-delete"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you do not have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

To remove the WhatsApp resources used by `AWSServiceRoleForSocialMessaging`, call the `list-linked-whatsapp-business-accounts` API to see the resources you have, call `disassociate-whatsapp-business-account` for each linked WhatsApp Business Account to remove it, then call `list-linked-whatsapp-business-accounts` again to verify no resources remain. You can then use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForSocialMessaging` service-linked role.