

# End user instructions for Transfer Family web apps
<a name="webapp-end-users"></a>

**Note**  
In this topic, the information is meant for the end users that are interacting with the web app. All instances of *you* in this topic refer to end users.

This topic describes how to access an AWS Transfer Family web app that you are authorized to use, and describes how you can interact with it.

## Web app quotas
<a name="end-user-quotas"></a>

Note the following limitations when using web apps.
+ Maximum number of search results per query: 10,000
+ The Amazon S3 buckets that are used by the Transfer Family web app must be in the same account as the web app itself. Cross-account buckets are not currently supported.
+ Maximum search breadth per query: 10,000 searched files
+ Maximum upload size per file: 160 GB (149 GiB)
+ Maximum size file for copying: 5.36 GB (5 GiB)
+ Folder names starting or ending with dots (.) are not supported

## User experience for IAM Identity Center users
<a name="end-user-identity-center"></a>

This section describes the user experience if your organization used IAM Identity Center to configure its users.

**To access a Transfer Family web app**

1. You should receive an email from **no-reply@login.awsapps.com** titled “Invitation to join AWS IAM Identity Center.” Accept the invitation to activate your user account.

1. In the message, choose the URL below **Your AWS access portal URL**.

   This takes you to the AWS sign in screen.  
![Screen showing the AWS sign-in screen.](http://docs.aws.amazon.com/transfer/latest/userguide/images/webapp-enduser-signin.png)

1. Enter your credentials and choose **Sign in**.

   This takes you to the AWS access portal, which shows a list of your available applications.

1. Choose the application for your Transfer Family web app.

## User experience for third-party identity provider users
<a name="end-user-3p"></a>

If your organization did not use AWS IAM Identity Center to configure its users, your onboarding experience will depend upon the identity provider application that they used to configure their end users. After you authenticate and sign in, your web app interface is the same as that described in the next section.

**Note**  
If a user belongs to multiple Active Directory groups that have grants to the same Amazon S3 bucket, the bucket appears multiple times in the web app interface. This occurs because the web app lists all top-level grants associated with the user's UID or GID, including duplicate grants to the same bucket. To prevent duplicate listings, administrators can consolidate multiple grants so that each user has only one grant per Amazon S3 location.

## Transfer Family end user interface
<a name="end-user-interface"></a>

After you have authenticated and signed in, you can interact with the web app.

There are four main views.
+ **Home page:** Your home page lists the S3 locations, which you can access, as well as the permissions for each. An S3 *location* is an S3 bucket or prefix, which you can define when using S3 Access Grants. This is the initial view for users that shows the root level S3 resources that your end users have access to and the permissions for each S3 location.  
![Screen showing the home location for a web app end user.](http://docs.aws.amazon.com/transfer/latest/userguide/images/webapp-enduser-home.png)
+ **Location details:** This view allows users to browse files and folders in S3, and upload or download files.
+ **Location action:** After you choose an action (such as **Upload**), it opens up another view of the file location.
+ **Vertical ellipsis:** The vertical ellipsis icon opens the **Actions** menu.

## Available actions
<a name="end-user-actions"></a>

Most of the actions are available from the **Actions** menu. For the other main action, downloading files, you use the download icon after you select a file (currently, you can only download one file at a time).

![Screen showing files and their corresponding download icons.](http://docs.aws.amazon.com/transfer/latest/userguide/images/webapp-enduser-download.png)


From a folder, use the **Actions** menu to perform any of the following tasks:
+ Copy one or more files to another location.
+ Create a folder.
+ Delete one or more files.
+ Upload one or more files.
+ Upload an entire folder (including subfolders if any).
+ Select a folder and navigate to it. You can then perform any of the previously listed actions.
+ Sort by page.
+ Filter by file or folder name per folder and subfolders.

![Screen showing an example folder for a web app end user.](http://docs.aws.amazon.com/transfer/latest/userguide/images/webapp-enduser-actions.png)
