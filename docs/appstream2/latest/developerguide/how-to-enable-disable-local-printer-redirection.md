# How to Enable

Local Printer Redirection

By default, local printer redirection is enabled when the AppStream 2.0 client is
installed. However, if local printer redirection is not enabled on the stack
that your users access for streaming sessions, you can enable it in the AppStream 2.0
console by performing the following steps.

###### To enable local printer redirection by using the AppStream 2.0 console

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose
   **Stacks**.
3. Choose the stack for which you want to enable local printer
   redirection.
4. Choose the **User Settings** tab, and then expand the
   **Clipboard, file transfer, print to local device, and
   authentication permissions** section.
5. For **Print to local device**, verify that
   **Enabled** is selected. If not, choose
   **Edit**, and then choose
   **Enabled**.
6. Choose **Update**.
   Alternatively, you can enable local printer redirection by using the AppStream 2.0
   API, an AWS SDK, or the AWS Command Line Interface (AWS CLI).
