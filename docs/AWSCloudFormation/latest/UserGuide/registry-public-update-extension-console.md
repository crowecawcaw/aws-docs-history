# Update a public

third-party extension in your account

After you activate a third-party public extension, you can update most extension
details from your account.

###### To update a public extension in your account (console)

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your
   AWS Region.
3. From the navigation pane, under **Registry**, choose
   **Activated extensions**.
4. Find the extension you want to update and select it. For more information,
   see [View the available and activated extensions in the
   CloudFormation registry](registry-view.md "registry-view.md").
5. From the **Actions** menu, choose
   **Edit**, and then the appropriate editing
   option:
   - To update the configuration schema, see [Edit configuration data for extensions in
     your account](registry-set-configuration.md "registry-set-configuration.md").
   - To activate or deactivate automatic updates:
     1. Choose **Edit automatic updates**.
     2. Choose **On** or
        **Off**, and then choose
        **Save**. For more information, see
        [Automatically use new versions of
        extensions](registry-public.md#registry-public-enable-auto "registry-public.md#registry-public-enable-auto").

   - To update the execution role:
     1. Choose **Edit execution role**.
     2. Specify the ARN of the IAM role you want CloudFormation to
        use when invoking this extension, and then choose
        **Save**. For more information, see
        [Configure an execution role
        with IAM permissions and a trust policy for public extension access](registry-public.md#registry-public-enable-execution-role "registry-public.md#registry-public-enable-execution-role").

   - To update the logging configuration:
     1. Choose **Edit logging config**.
     2. Edit the logging configuration JSON, and then choose
        **Save**.
