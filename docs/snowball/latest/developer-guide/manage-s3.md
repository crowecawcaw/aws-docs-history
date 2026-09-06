

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/). 

# Managing Amazon S3 adapter storage with AWS OpsHub
<a name="manage-s3"></a>

You can use AWS OpsHub to create and manage Amazon Simple Storage Service (Amazon S3) storage on your Snowball Edge using the S3 adapter for import and export jobs.

**Topics**
+ [Accessing Amazon S3 storage with AWS OpsHub](#create-s3-storage)
+ [Uploading files to Amazon S3 storage with AWS OpsHub](#upload-file)
+ [Downloading files from Amazon S3 storage with AWS OpsHub](#download-file)
+ [Deleting files from Amazon S3 storage with AWS OpsHub](#delete-file)

## Accessing Amazon S3 storage with AWS OpsHub
<a name="create-s3-storage"></a>

You can upload files to your device and access the files locally. You can physically move them to another location on the device, or import them back to the AWS Cloud when the device is returned. 

Snowball Edge use Amazon S3 buckets to store and manage files on your device.

**To access an S3 bucket**

1. Open the AWS OpsHub application.

1. In the **Manage file storage** section of the dashboard, choose **Get started**. 

   If your device has been ordered with the Amazon S3 transfer mechanism, they appear in the **Buckets** section of the **File & object storage** page. On the **File & object storage** page, you can see details of each bucket.
**Note**  
If the device was ordered with the NFS transfer mechanism, the bucket name will appear under the mount points section after NFS service is configure and activated. For more information on using the NFS interface, see [Managing the NFS interface with AWS OpsHub](manage-nfs.md).   
![File and object storage page showing Amazon S3 buckets on the Snowball Edge device](http://docs.aws.amazon.com/snowball/latest/developer-guide/images/opshub-access-s3-console.png)

## Uploading files to Amazon S3 storage with AWS OpsHub
<a name="upload-file"></a>

This video shows how to upload files to Amazon S3 storage using AWS OpsHub.

[![AWS Videos](http://img.youtube.com/vi/Bw8rzQhT1nM?start=472/0.jpg)](http://www.youtube.com/watch?v=Bw8rzQhT1nM?start=472)


**To upload a file**

1. In the **Manage file storage** section on the dashboard, choose **Get started**. If you have Amazon S3 buckets on your device, they appear in the **Buckets** section on the **File storage** page. You can see details of each bucket on the page.

1. Choose the bucket that you want to upload files into.

1. Choose **Upload** then **Upload files** or drag and drop the files in the bucket, and choose **OK**.  
![Amazon S3 bucket with Upload files chosen from the Upload menu](http://docs.aws.amazon.com/snowball/latest/developer-guide/images/opshub-upload-s3-console.png)
**Note**  
To upload larger files, you can use the multipart upload feature in Amazon S3 using the AWS CLI. For more information about configuring S3 CLI settings, see [CLI S3 Configuration](https://docs.aws.amazon.com/cli/latest/topic/s3-config.html). For more information on multipart upload, see [Multipart Upload Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html) in the Amazon Simple Storage Service User Guide  
Uploading a folder from a local machine to Snowball Edge using the AWS OpsHub is supported. If the folder size is very large, it takes some time for OpsHub to read the file/folder selection. While OpsHub is reading the files and folders, it does not display a progress tracker. However, it does display a progress tracker is displayed once the upload process begins.

## Downloading files from Amazon S3 storage with AWS OpsHub
<a name="download-file"></a>



**To download a file**

1. In the **Manage file storage** section of the dashboard, choose **Get started**. If you have S3 buckets on your device, they appear in the **Buckets** section on the **File storage** page. You can see details of each bucket on the page.

1. Choose the bucket that you want to download files from and navigate to the file that you want to download. Choose one or more files.  
![File and object storage page showing one file selected and the actions menu open showing Download file option.](http://docs.aws.amazon.com/snowball/latest/developer-guide/images/opshub-download-file-console.png)

1. In the **Actions** menu, choose **Download**.

1. Choose a location to download the file to, and choose **OK**.

## Deleting files from Amazon S3 storage with AWS OpsHub
<a name="delete-file"></a>

If you no longer need a file, you can delete it from your Amazon S3 bucket.

**To delete a file**

1. In the **Manage file storage** section of the dashboard, choose **Get started**. If you have Amazon S3 buckets on your device, they appear in the **Buckets** section on the **File storage** page. You can see details of each bucket on the page.

1. Choose the bucket you want to delete files from, and navigate to the file that you want to delete.

1. On the **Actions** menu, choose **Delete**.

1. In the dialog box that appears, choose **Confirm delete**.