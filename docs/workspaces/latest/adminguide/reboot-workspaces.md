

# Reboot a WorkSpace in WorkSpaces Personal
<a name="reboot-workspaces"></a>

Occasionally, you might need to reboot (restart) a WorkSpace manually. Rebooting a WorkSpace disconnects the user and then performs a shutdown and reboot of the WorkSpace. To avoid data loss, make sure the user saves any open documents and other application files before you reboot the WorkSpace. The user data, operating system, and system settings are not affected.

**Warning**  
To reboot an encrypted WorkSpace, first make sure that the AWS KMS Key is enabled; otherwise, the WorkSpace becomes unusable. To determine whether a KMS Key is enabled, see [ Displaying KMS Key Details](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys-console.html#viewing-console-details) in the *AWS Key Management Service Developer Guide*.

**To reboot a WorkSpace**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**.

1. Select the WorkSpaces to reboot and choose **Reboot**.

1. When prompted for confirmation, choose **Reboot**.

**To reboot a WorkSpace using the AWS CLI**  
Use the [reboot-workspaces](https://docs.aws.amazon.com/cli/latest/reference/workspaces/reboot-workspaces.html) command.

**To bulk reboot WorkSpaces**  
Use the [amazon-workspaces-admin-module](https://github.com/aws-samples/amazon-workspaces-admin-module/tree/main).