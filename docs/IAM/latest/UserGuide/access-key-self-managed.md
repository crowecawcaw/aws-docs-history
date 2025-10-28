# How IAM users can manage their own access

keys

IAM administrators can grant IAM users the permission to self-manage their access
keys by attaching the policy described in [Permissions required to manage access
keys](access-keys_required-permissions.md "access-keys_required-permissions.md").

With these permissions, IAM user can use the following procedures to create, activate,
deactivate, and delete the access keys associated with their username.

###### Topics

- [Create an access key for yourself
  (console)](#Using_CreateAccessKey "#Using_CreateAccessKey")
- [Deactivate your access key
  (console)](#deactivate-access-key-seccreds "#deactivate-access-key-seccreds")
- [Activate your access key
  (console)](#activate-access-key-seccreds "#activate-access-key-seccreds")
- [Delete your access key (console)](#delete-access-key-seccreds "#delete-access-key-seccreds")

## Create an access key for yourself

(console)

If you have been granted the appropriate permissions you can use the AWS Management Console to
create access keys for yourself.

###### To create your own access keys (console)

1. Use your AWS account ID or account alias, your IAM user name, and your password to sign in
   to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").

###### Note

For your convenience, the AWS sign-in page uses a browser cookie to remember your
IAM user name and account information. If you previously signed in as a different user,
choose **Sign in to a different account** near the bottom of the page to
return to the main sign-in page. From there, you can type your AWS account ID or account
alias to be redirected to the IAM user sign-in page for your account.

To get your AWS account ID, contact your administrator. 2. In the navigation bar on the upper right, choose your user name, and then
choose **Security credentials**.

![AWS Management Console Security credentials link](images/security-credentials-user.shared.console.png) 3. In the **Access keys** section, choose **Create access
key**. If you already have two access keys, this button is deactivated
and you must delete an access key before you can create a new one. 4. On the **Access key best practices & alternatives** page,
choose your use case to learn about additional options which can help you avoid
creating a long-term access key. If you determine that your use case still
requires an access key, choose **Other** and then choose
**Next**. 5. (Optional) Set a description tag value for the access key. This adds a tag
key-value pair to your IAM user. This can help you identify and update access
keys later. The tag key is set to the access key id. The tag value is set to the
access key description that you specify. When you are finished, choose
**Create access key**. 6. On the **Retrieve access keys** page, choose either
**Show** to reveal the value of your user's secret access key,
or **Download .csv file**. This is your only opportunity to save
your secret access key. After you've saved your secret access key in a secure
location, choose **Done**.

## Deactivate your access key

(console)

If you have been granted the appropriate permissions you can use the AWS Management Console to
deactivate your access key.

###### To deactivate an access key

1. Use your AWS account ID or account alias, your IAM user name, and your password to sign in
   to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").

###### Note

For your convenience, the AWS sign-in page uses a browser cookie to remember your
IAM user name and account information. If you previously signed in as a different user,
choose **Sign in to a different account** near the bottom of the page to
return to the main sign-in page. From there, you can type your AWS account ID or account
alias to be redirected to the IAM user sign-in page for your account.

To get your AWS account ID, contact your administrator. 2. In the navigation bar on the upper right, choose your user name, and then
choose **Security credentials**.

![AWS Management Console Security credentials link](images/security-credentials-user.shared.console.png) 3. In the **Access keys** section find the key you want to
deactivate, then choose **Actions**, then choose
**Deactivate**. When prompted for confirmation, choose
**Deactivate**. A deactivated access key still counts toward
your limit of two access keys.

## Activate your access key

(console)

If you have been granted the appropriate permissions you can use the AWS Management Console to
activate your access key.

###### To activate an access key

1. Use your AWS account ID or account alias, your IAM user name, and your password to sign in
   to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").

###### Note

For your convenience, the AWS sign-in page uses a browser cookie to remember your
IAM user name and account information. If you previously signed in as a different user,
choose **Sign in to a different account** near the bottom of the page to
return to the main sign-in page. From there, you can type your AWS account ID or account
alias to be redirected to the IAM user sign-in page for your account.

To get your AWS account ID, contact your administrator. 2. In the navigation bar on the upper right, choose your user name, and then
choose **Security credentials**.

![AWS Management Console Security credentials link](images/security-credentials-user.shared.console.png) 3. In the **Access keys** section, find the key to activate, then
choose **Actions**, then choose
**Activate**.

## Delete your access key (console)

If you have been granted the appropriate permissions you can use the AWS Management Console to
delete your access key.

###### To delete an access key when you no longer need it

1. Use your AWS account ID or account alias, your IAM user name, and your password to sign in
   to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").

###### Note

For your convenience, the AWS sign-in page uses a browser cookie to remember your
IAM user name and account information. If you previously signed in as a different user,
choose **Sign in to a different account** near the bottom of the page to
return to the main sign-in page. From there, you can type your AWS account ID or account
alias to be redirected to the IAM user sign-in page for your account.

To get your AWS account ID, contact your administrator. 2. In the navigation bar on the upper right, choose your user name, and then
choose **Security credentials**.

![AWS Management Console Security credentials link](images/security-credentials-user.shared.console.png) 3. In the **Access keys** section, find the key you want to
delete, then choose **Actions**, then choose
**Delete**. Follow the instructions in the dialog to first
**Deactivate** and then confirm the deletion. We recommend
that you verify that the access key is no longer in use before you permanently
delete it.
