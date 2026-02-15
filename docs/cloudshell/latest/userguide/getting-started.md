# Getting started with AWS CloudShell

This introductory tutorial shows you how to launch AWS CloudShell and perform key tasks using
the shell command line interface.

First, you sign in to the AWS Management Console and select an AWS Region. You then launch
CloudShell in a new browser window and a shell type to work with.

Next, you create a new folder in your home directory and upload a file to it from your local
machine. You work on that file using a pre-installed editor before running it as a program
from the command line. Last, you call AWS CLI commands to create an Amazon S3 bucket and add your
file as an object to the bucket.

## Prerequisites

**IAM permissions**

You can obtain permissions for AWS CloudShell by attaching the following AWS managed
policy to your IAM identity (such as a user, role, or group):

- **AWSCloudShellFullAccess**: Provides users with full access to
  AWS CloudShell and its features.

For this tutorial, you also interact with AWS services. More specifically, you
interact with Amazon S3 by creating an S3 bucket and adding an object to that bucket. Your IAM
identity requires a policy that grants, at a minimum, the `s3:CreateBucket` and
`s3:PutObject` permissions.

For more information, see [Amazon S3 Actions](../../../AmazonS3/latest/userguide/security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "../../../AmazonS3/latest/userguide/security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions") in the _Amazon Simple Storage Service User Guide_.

**Exercise file**

This exercise also involves uploading and editing a file that's then run as a program
from the command line interface. Open a text editor on your local machine and add the following code snippet.

```
import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
sum=x+y
print("The sum is",sum)
```

Save the file with the name `add_prog.py`.

## Contents

- [Step 1: Sign in to AWS Management Console](#start-session "#start-session")
- [Step 2: Select a Region, launch AWS CloudShell, and
  choose a shell](#launch-region-shell "#launch-region-shell")
- [Step 3: Download a file from AWS CloudShell](#download-file "#download-file")
- [Step 4: Upload a file to AWS CloudShell](#folder-upload "#folder-upload")
- [Step 5: Remove a file from AWS CloudShell](#remove-files "#remove-files")
- [Step 6: Create a home directory
  backup](#home-directory-backup "#home-directory-backup")
- [Step 7: Restart a shell
  session](#restart-shell-session "#restart-shell-session")
- [Step 8: Delete a shell session home
  directory](#delete-shell-session "#delete-shell-session")
- [Step 9: Edit your file's code and run it from the command
  line](#edit-run "#edit-run")
- [Step 10: Use AWS CLI to add the file as an object in an Amazon S3
  bucket](#s3-put "#s3-put")

## Step 1: Sign in to AWS Management Console

This step involves entering your IAM user information to access the AWS Management Console. If
you're already in the console, skip to [step 2](#launch-region-shell "#launch-region-shell").

- You can access the AWS Management Console by using an IAM users sign-in URL or going to the main sign-in page.

IAM user sign-in URL

    + Open a browser and enter the following sign-in URL. Replace `account_alias_or_id`
     with the account alias or account ID that your administrator
     provided.



    ```
    https://account_alias_or_id.signin.aws.amazon.com/console/
    ```
    + Enter your IAM sign-in credentials and choose **Sign in**.

Main sign-in page

    + Open [https://aws.amazon.com/console/](https://aws.amazon.com/console/ "https://aws.amazon.com/console/").
    + If you didn't sign in previously using this browser, the main sign-in page appears. Choose IAM user, enter the account alias or account ID, and choose **Next**.
    + If you already signed in as an IAM user before. Your browser might remember the account alias or account ID for the AWS account. If so, enter your IAM sign-in credentials and choose **Sign in**.

###### Note

You can also sign in as a [root user](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md"). This identity has complete access to all AWS services and resources in the account. We strongly recommend that you don't use the root user for everyday tasks, even administrative ones. Instead, adhere to the best practice of using the root user only to create your first IAM user.

## Step 2: Select a Region, launch AWS CloudShell, and choose

a shell

In this step, you launch
CloudShell
from the console interface, choose an available AWS Region, and switch to your preferred
shell, such as Bash, PowerShell, or Z shell.

1. To choose an AWS Region to work in, go to the **Select a
   Region** menu and select a [supported AWS Region](supported-aws-regions.md "supported-aws-regions.md") to work in. (Available Regions are
   highlighted.)

###### Important

If you switch Regions, the interface refreshes and the name of the selected
AWS Region is displayed above the command line text. Any files that you add to
persistent storage are available only in this same AWS Region. If you change
Regions, different storage and files are accessible.

###### Important

If CloudShell isn't available in the selected Region when you launch
CloudShell on the Console Toolbar, on the lower left of the
console, then the default Region is set to a Region that's closest to the selected
Region. You can run the command that provides permissions to manage resources in a
different Region than the default Region. For more information, see [Working in AWS Regions](working-with-aws-cloudshell.md#region-selection "working-with-aws-cloudshell.md#region-selection").

###### Example

**Example**

If you choose Europe (Spain) eu-south-2 but
CloudShell isn't available in Europe (Spain) eu-south-2,
then the default Region is set to Europe (Ireland) eu-west-1,
which is closest to the Europe (Spain) eu-south-2.

You will use the service quotas for the default Region, Europe (Ireland)
eu-west-1 and the same CloudShell session will be restored
across all Regions. The default Region might be changed and you will be
notified in the CloudShell browser window. 2. From the AWS Management Console, you can launch CloudShell by choosing one of the following
options:

    1. On the navigation bar, choose the **CloudShell**
     icon.
    2. In the **Search** box, type “CloudShell”, and then choose
     **CloudShell**.
    3. In the **Recently visited** widget, choose
     **CloudShell**.
    4. Choose **CloudShell** on the Console
     Toolbar, on the lower left of the console.




    	* You
    	 can adjust the height of your CloudShell
    	 session
    	 by dragging
    	 `=`.
    	* You
    	 can switch your CloudShell session to a full screen
    	 by clicking
    	 **Open in new browser
    	 tab**.

When the command prompt displays, the shell is ready for interaction.

###### Note

If you encounter issues that prevent you from successfully launching or
interacting with AWS CloudShell, check for information to identify and address those
issues in [Troubleshooting AWS CloudShell](troubleshooting.md "troubleshooting.md"). 3. To choose a pre-installed shell to work with, enter its program name at the
command line prompt.

Bash
`bash`

If you switch to Bash, the symbol at the command prompt
updates to `$`.

###### Note

Bash is the default shell that's running when you
launch AWS CloudShell.

PowerShell
`pwsh`

If you switch to PowerShell, the symbol at the command prompt updates to
`PS>`.

Z shell
`zsh`

If you switch to Z shell, the symbol at the command prompt
updates to `%`.

For information about the versions pre-installed in your shell environment, see
the [shells table](vm-specs.md#installed-shells "vm-specs.md#installed-shells") in the [AWS CloudShell compute environment](vm-specs.md "vm-specs.md") section.

## Step 3: Download a file from AWS CloudShell

###### Note

This option is not available for VPC environments.

This step walks you through the process of downloading a file.

1. To download a file, go to **Actions** and choose
   **Download file** from the menu.

The **Download file** dialog box displays. 2. In the **Download file** dialog box, enter the path for the file
to be downloaded.

###### Note

You can use absolute or relative paths when specifying a file for download.
With relative pathnames, `/home/cloudshell-user/` is added
automatically to the start by default. So, to download a file called
`mydownload-file`, both of the following are valid
paths:

    * **Absolute path:**
    `/home/cloudshell-user/subfolder/mydownloadfile.txt`
    * **Relative path:**
    `subfolder/mydownloadfile.txt`

3. Choose **Download**.

If the file path is correct, a dialog box displays. You can use this dialog box to
open the file with the default application. Or, you can save the file to a folder on
your local machine.

###### Note

The Download option isn't available when you launch CloudShell on the
Console Toolbar. You can download a file from CloudShell console or
using the Chrome web browser.

## Step 4: Upload a file to AWS CloudShell

###### Note

This option is not available for VPC environments.

This step describes how to upload a file and then moving it to a new directory in your home directory.

1. To check your current working directory, at the prompt enter the following command:

`pwd`

When you press **Enter**, the shell returns your
current working directory (for example, `/home/cloudshell-user`). 2. To upload a file to this directory, go to **Actions** and choose
**Upload file** from the menu.

The **Upload file** dialog box displays. 3. Choose **Browse**. 4. In your system's **File upload** dialog box, select the text file that you
created for this tutorial (`add_prog.py`) and choose
**Open**. 5. In the **Upload file** dialog box, choose **Upload**.

A progress bar tracks the upload. If the upload is successful, a message confirms
that `add_prog.py` was added to the root of your home
directory. 6. To create a directory for the file, enter the make directories command: `mkdir
 mysub_dir`. 7. To move the uploaded file from the root of your home directory to the new directory, use the
`mv` command:

`mv add_prog.py mysub_dir`. 8. To change your working directory to the new directory, enter `cd mysub_dir`.

The command prompt updates to indicate you've changed your working directory. 9. To view the contents of the current directory, `mysub_dir`,
enter the `ls` command.

The contents of the working directory are listed. This includes the file that
you just uploaded.

## Step 5: Remove a file from AWS CloudShell

This step describes how to remove a file from AWS CloudShell.

1. To remove a file from AWS CloudShell, use standard shell commands such as
   `rm` (remove).

`rm my-file-for-removal` 2. To remove multiple files that meet specified criteria, run the `find`
command.

The following example removes all the files that include the suffix ".pdf" in
their names.

```
find -type f -name '*.pdf' -delete
```

###### Note

Suppose that you stop using AWS CloudShell in a specific AWS Region. Then, the data
that's in that Region's persistent storage is removed automatically after a specified
period. For more information, see [Persistent Storage](limits.md#persistent-storage-limitations "limits.md#persistent-storage-limitations").

## Step 6: Create a home directory backup

This step
describes how to create a home directory backup.

1. **Create a backup file**

Create a temporary folder outside the home directory.

```
HOME_BACKUP_DIR=$(mktemp --directory)
```

You can use one of the following options to create a backup:

    1. **Create a backup file using tar**


    To create a backup file using tar, enter the following command:



    ```
    tar \
        --create \
        --gzip \
        --verbose \
        --file=${HOME_BACKUP_DIR}/home.tar.gz \
        [--exclude ${HOME}/.cache] \ // Optional
        ${HOME}/
    echo "Home directory backed up to this file: ${HOME_BACKUP_DIR}/home.tar.gz"
    ```
    2. **Create a backup file using zip**


    To create a backup file using zip, enter the following command:



    ```
    zip \
        --recurse-paths \
        ${HOME_BACKUP_DIR}/home.zip \
        ${HOME} \
        [--exclude ${HOME}/.cache/\*] // Optional
    echo "Home directory backed up to this file: ${HOME_BACKUP_DIR}/home.zip"
    ```

2. **Transfer the backup file outside CloudShell**

You can use one of the following options to transfer the backup file outside
CloudShell:

    1. **Download the backup file on your local
     machine**


    You can download the file created in the previous step. For more information
     about how to download a file from CloudShell, see [Download a file from AWS CloudShell](#download-file "#download-file").


    In the download file dialogue box, enter the path for the file to be
     downloaded (for example, `/tmp/tmp.iA99tD9L98/home.tar.gz`).
    2. **Transfer the backup file to S3**


    To generate a bucket, enter the following command:



    ```
    aws s3 mb s3://${BUCKET_NAME}
    ```

    Use AWS CLI to copy the file to the S3 bucket:



    ```
    aws s3 cp ${HOME_BACKUP_DIR}/home.tar.gz s3://${BUCKET_NAME}
    ```

    ###### Note

    Data transfer charges might apply.

3. **Backup directly to an S3 bucket**

To backup directly to an S3 bucket, enter the following command:

```
aws s3 cp \
    ${HOME}/ \
    s3://${BUCKET_NAME} \
    --recursive \
    [--exclude .cache/\*] // Optional
```

## Step 7: Restart a shell session

This step describes how to restart a shell session.

###### Note

As a security measure, if you don't interact with the shell using the keyboard or
pointer for an extended period, the session stops automatically. Long-running sessions
are also automatically stopped. For more information, see [Shell sessions](limits.md#session-lifecycle-limitations "limits.md#session-lifecycle-limitations").

1. To restart a shell session, choose **Actions**,
   **Restart**.

You're notified that restarting AWS CloudShell stops all active sessions in the current
AWS Region. 2. To confirm, choose **Restart**.

An interface displays a message that the CloudShell compute environment is
stopping. After the environment stopped and restarted, you can start working with the
command line in a new session.

###### Note

In some cases, it may take a few minutes for your environment to
restart.

## Step 8: Delete a shell session home

directory

This step describes how to delete a shell
session.

###### Note

This option is not available for VPC environments. When you restart a VPC
environment, its home directory is deleted.

###### Warning

Deleting your home directory is an irreversible action where all the data that's
stored in your home directory is deleted permanently. However, you might want to
consider this option in the following situations:

- You incorrectly modified a file and can't access the AWS CloudShell compute
  environment. Deleting your home directory returns AWS CloudShell to its default
  settings.
- You want to remove all your data from AWS CloudShell immediately. If you stop using
  AWS CloudShell in an AWS Region, persistent storage is [automatically deleted at the end of
  the retention period](limits.md#persistent-storage-limitations "limits.md#persistent-storage-limitations") unless you launch AWS CloudShell again in the
  Region.
  If you require long-term storage for your files, please consider a service such as
  Amazon S3.

1. To delete a shell session, choose **Actions**,
   **Delete**.

You’re notified that deleting AWS CloudShell home directory deletes all data currently
stored in your AWS CloudShell environment.

###### Note

You can't undo this action. 2. To confirm deletion, enter delete in the text input field, and then choose
**Delete**.

AWS CloudShell
stops all active sessions in the current
AWS Region.
You can create a new environment or setup a CloudShell VPC
environment. 3. To create a new environment, choose **Open a tab**. 4. To create a CloudShell VPC environment, choose **Create a VPC
environment**.

**Manually exiting shell sessions**

With the command line, you can leave a shell session and log out using the
`exit` command. You can then press any key to reconnect and continue to
use AWS CloudShell.

## Step 9: Edit your file's code and run it using the command

line

This step demonstrates how to use the pre-installed Vim editor to work
with a file. You then run that file as a program from the command line.

1. To edit the file you uploaded in the previous step, enter the following command:

`vim add_prog.py`

The shell interface refreshes to display the Vim editor. 2. To edit the file in Vim, press the **I** key. Now edit the
contents so the program adds up three numbers instead of two.

```
import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])
sum=x+y+z
print("The sum is",sum)
```

###### Note

If you paste the text into the editor and have the [Safe
Paste feature](customizing-cshell.md#safe-paste-enable "customizing-cshell.md#safe-paste-enable") enabled, a warning is displayed. Multiline text that's
copied can contain malicious scripts. With the Safe Paste feature, you can verify
the complete text before it's pasted in. If you're satisfied that the text is
safe, choose **Paste**. 3. After you edited the program, press **Esc** to enter the
Vim command mode. Then, enter the `:wq` command to save
the file and exit the editor.

###### Note

If you're new to the Vim command mode, you might initially find
it challenging to switch between command mode and insert mode. Command mode is
used when saving files and exiting the application. Insert mode is used when
inserting new text. To enter insert mode, press **I**, and, to
enter command mode, press **Esc**. For more information about
Vim and other tools that are available in AWS CloudShell, see [Development tools and shell utilities](vm-specs.md#utilities-installed "vm-specs.md#utilities-installed"). 4. On the main command line interface, run the following program and specify three
numbers for input. The syntax is as follows.

`python3 add_prog.py 4 5 6`

The command line displays the program output: `The sum is 15`.

## Step 10: Use AWS CLI to add the file as an object in an Amazon S3

bucket

In this step, you create an Amazon S3 bucket and then use the **PutObject** method to add your
code file as an object in that bucket.

###### Note

This
tutorial shows how you can use AWS CLI in AWS CloudShell to interact with other AWS services.
Using this method, you don't need to download or install any additional resource.
Moreover, because you're already authenticated within the shell, you don't need to
configure credentials before making calls.

1. To create a bucket in a specified AWS Region, enter the following command:

```
aws s3api create-bucket --bucket insert-unique-bucket-name-here --region us-east-1
```

###### Note

If you're creating a bucket outside of the `us-east-1` Region, add
`create-bucket-configuration` with the
`LocationConstraint` parameter to specify the Region. The following
is example syntax.

```
$ aws s3api create-bucket --bucket my-bucket --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1
```

If the call is successful, the command line displays a response from the service
similar to the following output.

```
{
    "Location": "/insert-unique-bucket-name-here"
}
```

###### Note

If you don't adhere to the [rules for naming buckets](../../../AmazonS3/latest/userguide/BucketRestrictions.md#bucketnamingrules "../../../AmazonS3/latest/userguide/BucketRestrictions.md#bucketnamingrules"), the following error is displayed:
**`An error occurred (InvalidBucketName) when calling the CreateBucket
 operation: The specified bucket is not valid.`** 2. To upload a file and add the file as an object to the bucket that you just created,
call the **PutObject** method.

```
aws s3api put-object --bucket insert-unique-bucket-name-here --key add_prog --body add_prog.py
```

After the object is uploaded to the Amazon S3 bucket, the command line displays a
response from the service similar to the following output:

```
{"ETag": "\"ab123c1:w:wad4a567d8bfd9a1234ebeea56\""}
```

The `ETag` is the hash of the object that was stored. You can use this
hash to [check the integrity of the object uploaded to Amazon S3](https://repost.aws/knowledge-center/data-integrity-s3 "https://repost.aws/knowledge-center/data-integrity-s3").

## Related topics

- [Manage AWS services from CLI in CloudShell](working-with-aws-cli.md "working-with-aws-cli.md")
- [Copying
  multiple files between your local machine and
  CloudShell](multiple-files-upload-download.md "multiple-files-upload-download.md")
- [AWS CloudShell Concepts](working-with-aws-cloudshell.md "working-with-aws-cloudshell.md")
- [Customizing your AWS CloudShell experience](customizing-cshell.md "customizing-cshell.md")
