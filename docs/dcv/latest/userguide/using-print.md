

# Printing from a session
<a name="using-print"></a>

You can use Amazon DCV to print content from a Amazon DCV session. The available printing devices depend on the client that you're using.
+ **Windows client, Linux client, and macOS client** – You can print to the physical printer that's connected to your client computer. Or, you can print to a `PDF` document that uses the Amazon DCV virtual printer.
+ **Web browser client** – You can print to a `.PDF` document using the Amazon DCV virtual printer.

When you print to the Amazon DCV virtual printer, the content is exported to a printable file. You can download it to your local computer using the client and then print it using your local printer.

You must be authorized to use this feature. If you are not authorized, the functionality is not available in the client. For more information, see [Configuring Amazon DCV Authorization](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization.html) in the *Amazon DCV Administrator Guide*.

**To print content from the session**

1. From within the session, open the Print window.

1. In the Print window, choose one of the following printing devices and then choose **Print**.
   + (All clients connected to all Windows and Linux server) **DCV Printer** – Prints to the Amazon DCV virtual printer
   + (Windows client connected to Windows and Linux server) **{{<local-printer-name>}}-Redirected** – Prints to the local printer

1. If you print to the Amazon DCV virtual printer, the behavior depends on the client:

------
#### [ Windows ]

1. A notification appears when the file is ready for download.

1. In the top-right corner, choose **Notifications**.

1. Locate the Print notification in the list, and then choose **Download**.
**Note**  
The printer dialog is automatically opened when the file is downloaded.

------
#### [ macOS ]

The print file is downloaded automatically. The **Printer** toolbar button shows a badge with the number of files being downloaded.

![Printer toolbar showing files being downloaded.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-print-list.png)


**To cancel a download**

1. Choose the **Printer** toolbar button.

1. Cancel individual files. When there is more than one file, you can also choose **Cancel All**.

**To open the downloaded file**

1. When the download completes, a notification appears in the **Session** toolbar button.

1. Choose the notification to see the download and open the file.  
![Session toolbar showing a completed print download notification.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-print-notification.png)

**Tip**  
If you have granted notification permission, completed print downloads also trigger a system notification. Clicking the notification opens the downloaded file.

------
#### [ Linux ]

1. A notification appears when the file is ready for download.

1. In the top-right corner, choose **Notifications**.

1. Locate the Print notification in the list, and then choose **Download**.
**Note**  
The downloaded file is automatically opened with the default associated application.

------
#### [ Web browser ]

1. A notification appears when the file is ready for download.

1. After the download has completed, choose **Show in folder**.

------

**Important**  
The file is deleted from the Amazon DCV server after you have downloaded it, and it's no longer available for download.