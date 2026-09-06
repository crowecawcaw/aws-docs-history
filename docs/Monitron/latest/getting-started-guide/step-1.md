

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Setting up a project
<a name="step-1"></a>

The first step with Amazon Monitron is to set up your project in the Amazon Monitron console. A project is where your team sets up gateways, assets, and sensors in the Amazon Monitron mobile app.

**Topics**
+ [Step 1: Create an account](#ags-signup)
+ [Step 2: Create a project](#gsg-projects)
+ [Step 3: Create admin users](#ags-project-admin)
+ [Step 4: (optional) Add Amazon Monitron users to your project](#gsg-sso)
+ [Step 5: Invite users to your project](#gsg-invite)

## Step 1: Create an account
<a name="ags-signup"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

**Important**  
Amazon Monitron supports all IAM Identity Center regions except opt-in and government regions. For a list of supported regions, see [Understanding SSO requirements](https://docs.aws.amazon.com/Monitron/latest/user-guide/mu-adding-user.html#sso-requirements). 

## Step 2: Create a project
<a name="gsg-projects"></a>

Now that you've signed in to the AWS Management Console, you can use the Amazon Monitron console to create your project.

**To create a project**

1. Choose the AWS Region that you want to use in the Region selector. Amazon Monitron is available only in the US East (N. Virginia), Europe (Ireland), and Asia Pacific (Sydney) Regions.  
![Region selector dropdown menu showing available AWS Regions such as US East N. Virginia.](http://docs.aws.amazon.com/Monitron/latest/getting-started-guide/images/gs-project-select-region.png)

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/). 

1. Choose **Create project**.  
![Getting started container with Documentation link and Create project button.](http://docs.aws.amazon.com/Monitron/latest/getting-started-guide/images/gs-project-monitron-create-project.png)

1. Under **Project Details**, for **Project name**, enter a name for the project. 

1. (Optional) Under **Data encryption**, you can check **Custom encryption settings (advanced) ** if you have an AWS KMS key in AWS Key Management Service. Amazon Monitron encrypts all data at rest and in transit. If you don't provide your own CMK, your data is encrypted by a CMK that Amazon Monitron owns and manages.

   For more information about encryption for your project, see [KMS and Data Encryption in Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-protection.html#data-encryption).

1.  (Optional) To add a tag to the project, enter a key-value pair under **Tags** and then choose **Add tag**.

   For more information about tags, see [Tags in Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/tagging.html). 

1. Choose **Next** to create the project.  
![Project details page with Site1 as project name and default data encryption settings.](http://docs.aws.amazon.com/Monitron/latest/getting-started-guide/images/gs-project-monitron-project-details.png)

When you create your first project, the owner of the AWS account will get an email from *AWS Organizations*. No action needs to be taken based on this email.

## Step 3: Create admin users
<a name="ags-project-admin"></a>

Give access to one or more people in your organization (such as reliability managers) as *admin users*. An *admin user* is a person who belongs to an Amazon Monitron project and who can add other users to the project.

When you add an admin user, Amazon Monitron creates an account for that user in AWS IAM Identity Center. IAM Identity Center is a service that helps you manage SSO access to AWS accounts and applications in your organization. Amazon Monitron uses IAM Identity Center to authenticate users for the Amazon Monitron mobile app. 

If you haven't enabled IAM Identity Center in your AWS account, Amazon Monitron enables it for you when you create your first Amazon Monitron admin user. If you are already using IAM Identity Center in your account, then your IAM Identity Center users are shown in the Amazon Monitron console.

Complete the steps in this section to add yourself to your project as an admin user. Repeat them for each additional admin user that you want to create.

**To create an admin user**

Unless you already use IAM Identity Center in your AWS account, use Amazon Monitron to create admin users. If these users are already in IAM Identity Center, you can skip creating the users, and you are ready to assign the admin role to them.

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/). 

1. On the **Add project admin user** page, choose **Create user**.

1.  In the **Create user** section, enter the admin user's email address and name.  
![Create a user form with fields for email address, first name, and last name.](http://docs.aws.amazon.com/Monitron/latest/getting-started-guide/images/create-user.png)

1. Choose **Create user**.

   Amazon Monitron creates a user in IAM Identity Center. IAM Identity Center sends the user an email that contains a link to activate the account. The link is valid for up to seven days. Within this time, each user must open the email and accept the invitation.

**To assign the admin role to the admin users**

1. On the **Add project admin user** page, select the checkbox for each admin user that you created.

1. Choose **Add**.

   You can add admin users to your project even if those people have not yet accepted the invitations to their IAM Identity Center accounts.

## Step 4: (optional) Add Amazon Monitron users to your project
<a name="gsg-sso"></a>

In addition to admin users, you can also add users who lack admin permissions. For example, these users might be technicians who only use the Amazon Monitron mobile app to monitor assets, acknowledge notifications and enter closure codes.

For users who are not admin users:
+ You use IAM Identity Center, not Amazon Monitron, to create their user accounts. 
+ You use the Amazon Monitron mobile app to add the users to projects, not the Amazon Monitron console. 

The following steps are not required if all of your users are admin users.

**To add users to IAM Identity Center**

If your users already have accounts in IAM Identity Center in your AWS account, you can skip these steps. You are ready to add the users to your project in the mobile app. Otherwise, add your users to IAM Identity Center by completing the following steps.

1. Open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/).

1. In the IAM Identity Center console, choose **Users**.

1. Repeat the following steps for each user that will access your project in the Amazon Monitron mobile app.

   1. On the **Users** page choose **Add user**.

   1. In the **User details** section, provide the username and contact information. Leave **Password** set to **Send an email to the user with password setup instructions**.  
![User details form with username, email, name fields, and password setup option selected.](http://docs.aws.amazon.com/Monitron/latest/getting-started-guide/images/gs-project-sso-user-details.png)

   1. Choose **Next: Groups**.

   1. Choose **Add user**. IAM Identity Center sends the user an email that contains a link to activate the IAM Identity Center user. The link is valid for up to seven days. Each user must open the email and accept the invitation before accessing your project in the Amazon Monitron mobile app.

### To add a user using the mobile app
<a name="w2aab7c15c13c13b1"></a>

1. Log into the Amazon Monitron mobile app on your smartphone. 

1. Navigate to the project or site that you want to add a user to, and then to the **Users** list. 

1. Choose **Add user**.   
![Users page with Add user button highlighted in the upper right corner.](http://docs.aws.amazon.com/Monitron/latest/getting-started-guide/images/user-list-add.png)

1. Enter a user name. 

   Amazon Monitron searches the user directory for the user. 

1. Choose the user from the list. 

1. Choose the role that you want to assign the user: **Admin**, **Technician**, or **Viewer**.

1. Choose **Add**. 

   The new user appears on the **Users** list.

1. Send the new user an email invitation with a link for accessing the project and downloading the Amazon Monitron mobile app. For more information, see [Sending an email invitation](https://docs.aws.amazon.com/Monitron/latest/user-guide/resending-email.html).

### How to add a user using the web app
<a name="w2aab7c15c13c13b3"></a>

1. Select **Users** from the navigation pane.

1. Choose **Add user**.  
![Add user button highlighted in the Users page toolbar.](http://docs.aws.amazon.com/Monitron/latest/getting-started-guide/images/webapp_add-user.png)

1. Enter a user name. 

   Amazon Monitron searches the user directory for the user. 

1. Choose the user from the list. 

1. Choose the role that you want to assign the user: **Admin**, **Technician**, or **Read only**.

1. Choose **Add**. 

   The new user appears on the **Users** list.

1. Send the new user an email invitation with a link for accessing the project and downloading the Amazon Monitron mobile app. For more information, see [Sending an email invitation](https://docs.aws.amazon.com/Monitron/latest/user-guide/resending-email.html). 

![Users table showing display names, roles such as Admin and Technician, and site assignments.](http://docs.aws.amazon.com/Monitron/latest/getting-started-guide/images/users-table.png)


## Step 5: Invite users to your project
<a name="gsg-invite"></a>

Invite the users you've added to your Amazon Monitron project.

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/). 

1. In the navigation pane, choose **Projects**.

1. On the **Projects** page, choose your project name to open its details page.

1. Repeat the following steps for each user that you want to invite.

   1. Under **How it works**, choose **Email instructions**.  
![Email instructions icon with envelope and user silhouette, and button to send instructions.](http://docs.aws.amazon.com/Monitron/latest/getting-started-guide/images/gs-project-monitron-email-instructions.png)

      Your email client opens a draft that contains an invitation to your Amazon Monitron project. It contains both a link to download the Amazon Monitron mobile app from the Google Play Store and a link to open the project.

   1. Email this message to the user.