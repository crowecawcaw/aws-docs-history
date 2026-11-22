

# Enable WebAuthn redirection

Complete the following steps to enable WebAuthn redirection on a new or an existing stack.

**To enable WebAuthn redirection**

1. Open the WorkSpaces Applications AWS Management Console.

1. In the left navigation pane, choose **Stacks**.

1. Do one of the following:
   + To configure a new stack, choose **Create Stack**.
   + To modify an existing stack, select the stack and choose **Edit**.

1. In the **User Settings** section, select **Enable WebAuthn redirection**.

1. (Windows fleets only, optional) Under **Process compatibility list**, enter the process names that are allowed to use WebAuthn redirection. For more information, see the following section.

1. Choose **Update** to save your stack configuration.

**Note**  
After you save the stack settings, the changes take effect when a new streaming session is created. Existing sessions are not affected.

**Note**  
If the stack has WebAuthn redirection enabled and you associate a fleet whose image does not support the feature, the association fails with an incompatible image error. Update the fleet to a supported image, or disable WebAuthn redirection on the stack.

You can also enable WebAuthn redirection by using the AWS CLI.

**To enable WebAuthn redirection by using the AWS CLI**

1. Use the `WebAuthnRedirection` parameter with the `create-stack` or `update-stack` command.

   To enable WebAuthn redirection with the default settings:

   ```
   aws appstream update-stack --name MyStack --web-authn-redirection Enabled=true
   ```

   To enable WebAuthn redirection with a custom process compatibility list (Windows fleets only):

   ```
   aws appstream update-stack --name MyStack --web-authn-redirection Enabled=true,ProcessCompatibilityList=chrome.exe,firefox.exe
   ```

1. To disable the feature, set `Enabled=false`. To remove the setting from the stack entirely, use `--attributes-to-delete WEB_AUTHN_REDIRECTION`.