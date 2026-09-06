

# How to Enable Local Printer Redirection
<a name="how-to-enable-disable-local-printer-redirection"></a>

By default, local printer redirection is enabled when the WorkSpaces Applications client is installed. However, if local printer redirection is not enabled on the stack that your users access for streaming sessions, you can enable it in the WorkSpaces Applications console by performing the following steps. 

**To enable local printer redirection by using the WorkSpaces Applications console**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the left navigation pane, choose **Stacks**.

1. Choose the stack for which you want to enable local printer redirection.

1. Choose the **User Settings** tab, and then expand the **Clipboard, file transfer, print to local device, and authentication permissions** section.

1. For **Print to local device**, verify that **Enabled** is selected. If not, choose **Edit**, and then choose **Enabled**.

1. Choose **Update**.

Alternatively, you can enable local printer redirection by using the WorkSpaces Applications API, an AWS SDK, or the AWS Command Line Interface (AWS CLI).