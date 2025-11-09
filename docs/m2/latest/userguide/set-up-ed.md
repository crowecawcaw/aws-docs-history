AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Tutorial: Set up Rocket Enterprise Developer on WorkSpaces Applications

This tutorial describes how to set up Rocket Enterprise Developer (formerly Micro Focus Enterprise Developer) for one or more mainframe
applications in order to maintain, compile, and test them using the Enterprise Developer features. The setup is
based on the WorkSpaces Applications Windows images that AWS Mainframe Modernization shares with the customer and on the creation of
WorkSpaces Applications fleets and stacks as described in [Tutorial: Set up WorkSpaces Applications for use with Rocket Enterprise Analyzer and
Rocket Enterprise Developer](set-up-appstream-mf.md "set-up-appstream-mf.md").

###### Important

The steps in this tutorial assume that you set up WorkSpaces Applications using the downloadable AWS CloudFormation
template [cfn-m2-appstream-fleet-ea-ed.yaml](https://d1vi4vxke6c2hu.cloudfront.net/tutorial/cfn-m2-appstream-fleet-ea-ed.yaml "https://d1vi4vxke6c2hu.cloudfront.net/tutorial/cfn-m2-appstream-fleet-ea-ed.yaml"). For more information, see [Tutorial: Set up WorkSpaces Applications for use with Rocket Enterprise Analyzer and
Rocket Enterprise Developer](set-up-appstream-mf.md "set-up-appstream-mf.md").

You must perform the steps of this setup when the Enterprise Developer fleet and stack are up and
running.

For a complete description of Enterprise Developer v7 features and deliverables, check out its [up-to-date online documentation (v7.0)](https://www.microfocus.com/documentation/enterprise-developer/ed70/ED-Eclipse/GUID-8D6B7358-AC35-4DAF-A445-607D8D97EBB2.html "https://www.microfocus.com/documentation/enterprise-developer/ed70/ED-Eclipse/GUID-8D6B7358-AC35-4DAF-A445-607D8D97EBB2.html") on the Rocket Software (formerly Micro Focus) site.

## Image contents

In addition to Enterprise Developer itself, the image contains the image contains Rumba (a TN3270 emulator). It also contains the following tools and libraries.

Third-party tools

- [Python](https://www.python.org/ "https://www.python.org/")
- [Rclone](https://rclone.org/ "https://rclone.org/")
- [pgAdmin](https://www.pgadmin.org/ "https://www.pgadmin.org/")
- [git-scm](https://git-scm.com/ "https://git-scm.com/")
- [PostgreSQL ODBC driver](https://odbc.postgresql.org/ "https://odbc.postgresql.org/")

Libraries in `C:\Users\Public`

- BankDemo source code and project definition for Enterprise Developer:
  `m2-bankdemo-template.zip`.
- MFA install package for the mainframe: `mfa.zip`. For more information,
  see [Mainframe Access Overview](https://www.microfocus.com/documentation/enterprise-developer/30pu12/ED-VS2012/BKMMMMINTRS001.html "https://www.microfocus.com/documentation/enterprise-developer/30pu12/ED-VS2012/BKMMMMINTRS001.html") in the _Micro Focus Enterprise Developer_ documentation.
- Command and config files for Rclone (instructions for their use in the tutorials):
  `m2-rclone.cmd` and `m2-rclone.conf`.

If you need to access source code that is not yet loaded into CodeCommit repositories, but that is
available in an Amazon S3 bucket, for example to perform the initial load of the source code into git,
follow the procedure to create a virtual Windows disk as described in [Tutorial: Set up Enterprise Analyzer on WorkSpaces Applications](set-up-ea.md "set-up-ea.md").

###### Topics

- [Prerequisites](#tutorial-ed-prerequisites "#tutorial-ed-prerequisites")
- [Step 1: Setup by individual Enterprise Developer users](#tutorial-ed-step1 "#tutorial-ed-step1")
- [Step 2: Create the Amazon S3-based virtual folder on Windows
  (optional)](#tutorial-ed-step2 "#tutorial-ed-step2")
- [Step 3: Clone the repository](#tutorial-ed-step3 "#tutorial-ed-step3")
- [Subsequent sessions](#tutorial-ed-step4 "#tutorial-ed-step4")
- [Clean up resources](#tutorial-ed-clean "#tutorial-ed-clean")

## Prerequisites

- One or more CodeCommit repositories loaded with the source code of the application to be
  maintained. The repository setup should match the requirements of the CI/CD pipeline above to
  create synergies by combination of both tools.
- Each user must have credentials to the CodeCommit repository or repositories defined by the
  account administrator according to the information in [Authentication and access control for AWS CodeCommit](../../../codecommit/latest/userguide/auth-and-access-control.md "../../../codecommit/latest/userguide/auth-and-access-control.md"). The structure of those
  credentials is reviewed in [Authentication and access
  control for AWS CodeCommit](../../../codecommit/latest/userguide/auth-and-access-control.md "../../../codecommit/latest/userguide/auth-and-access-control.md") and the complete reference for IAM authorizations for
  CodeCommit is in the [CodeCommit permissions reference](../../../codecommit/latest/userguide/auth-and-access-control-permissions-reference.md "../../../codecommit/latest/userguide/auth-and-access-control-permissions-reference.md"): the administrator may define distinct IAM
  policies for distinct roles having credentials specific to the role for each repository and
  limiting its authorizations of the user to the specific set of tasks that he has to to
  accomplish on a given repository. So, for each maintainer of the CodeCommit repository, the account
  administrator will generate a primary user and grant this user permissions to access the
  required repository or repositories via selecting the proper IAM policy or policies for CodeCommit
  access.

## Step 1: Setup by individual Enterprise Developer users

1. Obtain your IAM credentials:
   1. Connect to the AWS console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. Follow the procedure described in step 3 of [Setup for HTTPS users using Git
      credentials](../../../codecommit/latest/userguide/setting-up-gc.md "../../../codecommit/latest/userguide/setting-up-gc.md") in the _AWS CodeCommit User Guide_.
   3. Copy the CodeCommit-specific sign-in credentials that IAM generated for you, either by
      showing, copying, and then pasting this information into a secure file on your local
      computer, or by choosing **Download credentials** to download this
      information as a .CSV file. You need this information to connect to CodeCommit.

2. Start a session with WorkSpaces Applications based on the url received in the welcome email. Use your email
   as user name and create your password.
3. Select your Enterprise Developer stack.
4. On the menu page, choose **Desktop** to reach the Windows desktop streamed
   by the fleet.

## Step 2: Create the Amazon S3-based virtual folder on Windows

(optional)

If there is a need for Rclone (see above), create the Amazon S3-based virtual folder on Windows:
(optional if all application artefacts exclusively come from CodeCommit access).

###### Note

If you already used Rclone during the AWS Mainframe Modernization preview, you must update
`m2-rclone.cmd` to the newer version located in
`C:\Users\Public`.

1. Copy the `m2-rclone.conf` and `m2-rclone.cmd` files
   provided in `C:\Users\Public` to your home folder
   `C:\Users\PhotonUser\My Files\Home Folder` using File Explorer.
2. Update the `m2-rclone.conf` config parameters with your AWS access
   key and corresponding secret, as well as your AWS Region.

```
[m2-s3]
type = s3
provider = AWS
access_key_id = YOUR-ACCESS-KEY
secret_access_key = YOUR-SECRET-KEY
region = YOUR-REGION
acl = private
server_side_encryption = AES256
```

3. In `m2-rclone.cmd`, make the following changes:
   - Change `amzn-s3-demo-bucket` to your Amazon S3 bucket name. For example,
     `m2-s3-mybucket`.
   - Change `your-s3-folder-key` to your Amazon S3 bucket key. For example,
     `myProject`.
   - Change `your-local-folder-path` to the path of the directory where you want
     the application files synced from the Amazon S3 bucket that contains them. For example,
     `D:\PhotonUser\My Files\Home Folder\m2-new`. This synced directory must be a
     subdirectory of the Home Folder in order for WorkSpaces Applications to properly back up and restore it on
     session start and end.

```
:loop
timeout /T 10
"C:\Program Files\rclone\rclone.exe" sync m2-s3:`amzn-s3-demo-bucket`/`your-s3-folder-key` "D:\PhotonUser\My Files\Home Folder\`your-local-folder-path`" --config "D:\PhotonUser\My Files\Home Folder\m2-rclone.conf"
goto :loop
```

4. Open a Windows command prompt, cd to `C:\Users\PhotonUser\My Files\Home
Folder` if needed and run `m2-rclone.cmd`. This command script
   runs a continuous loop, syncing your Amazon S3 bucket and key to the local folder every 10 seconds.
   You can adjust the time out as needed. You should see the source code of the application
   located in the Amazon S3 bucket in Windows File Explorer.

To add new files to the set that you are working on or to update existing ones, upload the
files to the Amazon S3 bucket and they will be synced to your directory at the next iteration defined
in `m2-rclone.cmd`. Similarly, if you want to delete some files, delete them
from the Amazon S3 bucket. The next sync operation will delete them from your local directory.

## Step 3: Clone the repository

1. Navigate to the application selector menu in the top left corner of the browser window and
   select Enterprise Developer.
2. Complete the workspace creation required by Enterprise Developer in your Home folder by choosing
   `C:\Users\PhotonUser\My Files\Home Folder` (aka `D: \PhotonUser\My
Files\Home Folder`) as location for the workspace.
3. In Enterprise Developer, clone your CodeCommit repository by going to the Project Explorer, right click and
   choose **Import**, **Import …**, **Git**,
   **Projects** from **Git**
   **Clone URI**. Then, enter your CodeCommit-specific sign-in credentials and
   complete the Eclipse dialog to import the code.

The CodeCommit git repository in now cloned in your local workspace.

Your Enterprise Developer workspace is now ready to start the maintenance work on your application. In
particular, you can use the local instance of Enterprise Server (ES) integrated with Enterprise Developer to
interactively debug and run your application to validate your changes locally.

###### Note

The local Enterprise Developer environment, including the local Enterprise Server instance, runs under
Windows while AWS Mainframe Modernization runs under Linux. We recommend that you run complementary tests in the Linux
environment provided by AWS Mainframe Modernization after you commit the new application to CodeCommit and rebuild it for
this target and before you roll out the new application to production.

## Subsequent sessions

As you select a folder that is under WorkSpaces Applications management like the home folder for the cloning
of your CodeCommit repository, it will be saved and restored transparently across sessions. Complete
the following steps the next time you need to work with the application:

1. Start a session with WorkSpaces Applications based on the url received in the welcome email.
2. Login with your email and permanent password.
3. Select the Enterprise Developer stack.
4. Launch `Rclone` to connect (see above) to the Amazon S3-backed disk when
   this option is used to share the workspace files.
5. Launch Enterprise Developer to do your work.

## Clean up resources

If you no longer need the resources you created for this tutorial, delete them so that you
won't continue to be charged for them. Complete the following steps:

- Delete the CodeCommit repository you created for this tutorial. For more information, see
  [Delete an CodeCommit repository](../../../codecommit/latest/userguide/how-to-delete-repository.md "../../../codecommit/latest/userguide/how-to-delete-repository.md") in the _AWS CodeCommit User Guide_.
- Delete the database you created for this tutorial. For more information, see [Deleting a DB instance](../../../AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.md#CHAP_GettingStarted.Deleting.PostgreSQL "../../../AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.md#CHAP_GettingStarted.Deleting.PostgreSQL").
