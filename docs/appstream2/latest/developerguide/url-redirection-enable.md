# Enable host-to-client URL redirection

Complete the following steps to enable host-to-client URL redirection on a
new or existing stack.

###### To enable host-to-client URL redirection

1. Open the WorkSpaces Applications AWS Management Console.
2. In the left navigation pane, choose **Stacks**.
3. Do one of the following:
   - To configure a new stack, choose **Create Stack**.
   - To modify an existing stack, select the stack and choose
     **Edit**.

4. In the **Content Redirection** section,
   select **Enable host to client URL redirection**.
5. Configure the URL patterns and optional exception list as described in the
   following sections.
6. Choose **Update** to save your stack configuration.

###### Note

After you save the stack settings, the changes take effect when a new
streaming session is created. Existing sessions are not affected.

After you enable the feature, two configuration fields become available:
**Configure host to client URL patterns** (required) and
**Configure exception list** (optional).
