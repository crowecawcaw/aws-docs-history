# Troubleshooting

Use the following steps to enable diagnostic log uploads and determine your
client version and client ID.

## Enable Diagnostic Log

Uploads

To troubleshoot issues with the AppStream 2.0 client, you can enable diagnostic
logging. The log files that are sent to AppStream 2.0 include detailed information
about your device and connection to the AWS network. You can enable
diagnostic log uploads before or during AppStream 2.0 streaming sessions, so these
files are sent to AppStream 2.0 automatically. As a best practice, we recommend
that you enable log upload to help the AppStream 2.0 team troubleshoot
issues.

To enable file logging, follow these steps:

1. Choose **AppStream 2.0** from the system menu
   bar, or navigate to the top-right corner of the
   **Connect** page.
2. Choose **Client Options** and **Client
   automatic logging**.

## Collect Logs for AppStream 2.0 Client for macOS

AppStream 2.0 logs can be used by your administrator to identify and troubleshoot
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

If issues occur when you use the AppStream 2.0 client for macOS, your AppStream 2.0
version number and client ID can help your administrator and AWS support
team with troubleshooting. To find the version of the AppStream 2.0 client that you
have installed, open the AppStream 2.0 client. On the system menu bar, choose
**Amazon AppStream 2.0** and **About Amazon AppStream
2.0**. The client version is displayed below the Amazon AppStream 2.0
logo.

To find the client ID of the AppStream 2.0 client that you have installed, choose
**Amazon AppStream 2.0** on the system menu bar, or navigate
to the top-right corner of the **Connect** page and choose
**Client Option**.
