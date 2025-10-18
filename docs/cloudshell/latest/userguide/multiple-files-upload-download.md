# Copying
 multiple files between your local machine and
 CloudShell

This tutorial shows how to copy multiple files between your local machine and CloudShell.

Using the
 AWS CloudShell
 interface, you can upload or download a single file between your local machine and the shell
 environment at a time. To copy multiple files between CloudShell and your local machine at
 the same time, use one of the following options:


* Amazon S3: Use S3 buckets as an intermediary when copying files between your local machine
 and CloudShell.
* Zip files: Compress multiple files in a single zipped folder that can be uploaded or
 downloaded using the CloudShell interface.
###### Note

Because CloudShell doesn't allow incoming internet traffic, it's currently not possible
 to use commands such as `scp` or `rsync` to copy multiple files between
 local machines and the CloudShell compute environment.


## Uploading and downloading multiple files using
 Amazon S3


This step describes
 how to upload and download multiple files using Amazon S3.


### Prerequisites


To work with buckets and objects, you need an IAM policy that grants permissions to
 perform the following Amazon S3 API actions:



* `s3:CreateBucket`
* `s3:PutObject`
* `s3:GetObject`
* `s3:ListBucket`

For a complete list of Amazon S3 actions, see [Actions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html") in the *Amazon Simple Storage Service API Reference*.


## Upload multiple files to AWS CloudShell using Amazon S3

This step describes how to upload multiple files using Amazon S3.

1. In AWS CloudShell, create an S3 bucket by running the following `s3`
 command:



```
aws s3api create-bucket --bucket your-bucket-name --region us-east-1
```

If the call is successful, the command line displays a response from the S3
 service:



```
{
    "Location": "/your-bucket-name"
}          
```
2. Upload the files in a directory from your local machine to the bucket. Choose one of
 the following options to upload files:




	* AWS Management Console: Use drag-and-drop to upload files and folders to a bucket.
	* AWS CLI: With the version of the tool installed on your local machine, use the
	 command line to upload files and folders to the bucket.

Using the console


	* Open the Amazon S3 console at [https://s3.console.aws.amazon.com/s3/]( https://s3.console.aws.amazon.com/s3/ " https://s3.console.aws.amazon.com/s3/").
	
	
	(If you're using AWS CloudShell, you should already be logged in to the
	 console.)
	* In the left navigation pane, choose **Buckets**, and then
	 choose the name of the bucket that you want to upload your folders or files to.
	 You can also create a bucket of your choice by choosing **Create
	 bucket**.
	* To select the files and folders that you want to upload, choose
	 **Upload**. Then, drag and drop your selected files and
	 folders into the console window that lists the objects in the destination
	 bucket, or choose **Add files**, or **Add
	 folders**.
	
	
	The files you chose are listed on the **Upload**
	 page.
	* Select the check boxes to indicate the files to be added.
	* To add the selected files to the bucket, choose
	 **Upload**.
###### Note

For information about the full range of configuration options when using the
 console, see [How do I upload files and folders to an S3 bucket?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html") in the
 *Amazon Simple Storage Service User Guide*.



Using AWS CLI
###### Note

For this option, you need to have the AWS CLI tool installed on your local
 machine and have your credentials configured for calls to AWS services. For more
 information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/ "https://docs.aws.amazon.com/cli/latest/userguide/").




	* Launch the AWS CLI tool and run the following `aws s3` command to
	 sync the specified bucket with the contents of the current directory on your
	 local machine: 
	
	
	
	```
	aws s3 sync folder-path s3://your-bucket-name 
	```
If the sync is successful, upload messages are displayed for every object added
 to the bucket.
3. Return to the CloudShell command line and enter the following command to
 synchronize the directory in the shell environment with the contents of the S3 bucket: 



```
aws s3 sync  s3://your-bucket-name folder-path
```

###### Note

You can also add `--exclude "<value>"` and `--include
 "<value>"` parameters to the `sync` command to perform pattern
 matching to either exclude or include a particular file or object.

 For more information, see [Use of
 Exclude and Include Filters](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters "https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters") in the *AWS CLI Command Reference*.
 


If the sync is successful, download messages are displayed for every file downloaded
 from the bucket to the directory.


###### Note

With the sync command, only new and updated files are recursively copied from the
 source directory to the destination.

## Download multiple files from AWS CloudShell using Amazon S3

This step describes how to download multiple files using Amazon S3.

1. Using the AWS CloudShell command line, enter the following `aws s3` command to
 sync an S3 bucket with contents of the current directory in the shell environment:



```
aws s3 sync folder-path s3://your-bucket-name
```

###### Note

You can also add `--exclude "<value>"` and `--include
 "<value>"` parameters to the `sync` command to perform pattern
 matching to either exclude or include a particular file or object.

 For more information, see [Use of
 Exclude and Include Filters](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters "https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters") in the *AWS CLI Command Reference*.
 


If the sync is successful, upload messages are displayed for every object added to the
 bucket.
2. Download the contents of the bucket to your local machine. Because the Amazon S3
 console doesn't support the downloading of multiple objects, you need to use the AWS CLI
 tool that's installed on your local machine.


From the command line of the AWS CLI tool, run the following command:



```
aws s3 sync s3://your-bucket-name folder-path
```

If the sync is successful, the command line displays a download message for each file
 updated or added in the destination directory.


###### Note

For this option, you need to have the AWS CLI tool installed on your local machine and
 have your credentials configured for calls to AWS services. For more information, see
 the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/ "https://docs.aws.amazon.com/cli/latest/userguide/").

## Uploading and downloading multiple files using zipped
 folders


This step describes how to upload and download multiple files using
 zipped
 folders.


With the zip/unzip utilities, you can compress multiple files in an archive that can be
 treated as a single file. The utilities are pre-installed in the CloudShell compute
 environment.


 For more information about pre-installed tools, see [Development tools and shell utilities](vm-specs.md#utilities-installed "vm-specs.md#utilities-installed").


## Upload multiple files to AWS CloudShell using zipped folders

This step
 describes how to upload multiple files using zipped
 folders.

1. On your local machine, add the files to be uploaded to a zipped folder.
2. Launch CloudShell, and then choose **Actions**, **Upload
 file**.
3. In the **Upload file** dialog box, choose **Select
 file**, and then choose the zipped folder you just created.
4. In the **Upload file** dialog box, choose
 **Upload** to add the selected file to the shell environment.
5. In the CloudShell command line, run the following command to unzip the contents of
 the zip archive to a specified directory:



```
unzip zipped-files.zip -d my-unzipped-folder
```

## Download multiple files from AWS CloudShell using zipped folders

This step describes how to download multiple files using zipped folders.

1. In the CloudShell command line, running the following command to add all the files
 in the current directory to a zipped folder: 



```
zip -r zipped-archive.zip *
```
2. Choose **Actions**, **Download file**.
3. In the **Download file** dialog box, enter the path for the zipped
 folder (`/home/cloudshell-user/zip-folder/zipped-archive.zip`, for
 example), and then choose **Download**. 


If the path is correct, a browser dialog offers the choice of opening the zipped
 folder or saving it to your local machine.
4. On your local machine, you can now unzip the contents of the downloaded zipped
 folder.
