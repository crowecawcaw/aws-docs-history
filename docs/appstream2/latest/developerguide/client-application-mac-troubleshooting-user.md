# Troubleshooting

Use the following steps to enable diagnostic log uploads and determine your
client version and client ID.

## Enable Diagnostic Log Uploads

To troubleshoot issues with the WorkSpaces Applications client, you can enable diagnostic
logging. The log files that are sent to WorkSpaces Applications include detailed information
about your device and connection to the AWS network. You can enable
diagnostic log uploads before or during WorkSpaces Applications streaming sessions, so these
files are sent to WorkSpaces Applications automatically. As a best practice, we recommend
that you enable log upload to help the WorkSpaces Applications team troubleshoot
issues.

To enable file logging, follow these steps:

1. Choose **AppStream 2.0** from the system menu
   bar, or navigate to the top-right corner of the
   **Connect** page.
2. Choose **Client Options** and **Client
   automatic logging**.

## Collect Logs for WorkSpaces Applications Client for macOS

WorkSpaces Applications logs can be used by your administrator to identify and troubleshoot
configuration issues. They can also help enable AWS Support to diagnose
and troubleshoot cases. To collect and share the logs, choose from the
following options:

- Option 1: Open a terminal and enter `open
~/Library/Containers/com.amazon.appstreamclient/Data/logs`
- Option 2: Open **Finder**, and choose
  **Users**, **User_Name**,
  **Library**, **Containers**,
  **Appstream**, **Data**, and
  **logs**
- Option 3: Open **Finder**, and from the top-left
  system menu bar, choose **Go** and **Go to
  folder**. Enter
  `~/Library/Containers/com.amazon.appstreamclient/Data/logs`

## Determine Client Version and Client ID

If issues occur when you use the WorkSpaces Applications client for macOS, your WorkSpaces Applications
version number and client ID can help your administrator and AWS support
team with troubleshooting. To find the version of the WorkSpaces Applications client that you
have installed, open the WorkSpaces Applications client. On the system menu bar, choose
**Amazon WorkSpaces Applications** and **About Amazon AppStream
2.0**. The client version is displayed below the Amazon WorkSpaces Applications
logo.

To find the client ID of the WorkSpaces Applications client that you have installed, choose
**Amazon WorkSpaces Applications** on the system menu bar, or navigate
to the top-right corner of the **Connect** page and choose
**Client Option**.
