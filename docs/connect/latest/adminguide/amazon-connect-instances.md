# Create an Amazon Connect instance

The first step in setting up your Amazon Connect contact center is to create a virtual contact
center instance. Each instance contains all the resources and settings related to your
contact center.

## Things to know before you begin

- When you sign up for Amazon Web Services (AWS), your AWS account is automatically
  signed up for all services in AWS, including Amazon Connect. You are charged only for
  the services that you use. To create an AWS account, see [How/
  do I create and activate an AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/ "https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/")
- To allow a user to create an instance, ensure that they have the permissions
  granted by the **AmazonConnect_FullAccess** policy.
- For a list of the minimum IAM permissions required to create an instance, see
  [Required permissions for using
  custom IAM policies to manage access to the Amazon Connect console](security-iam-amazon-connect-permissions.md "security-iam-amazon-connect-permissions.md").
- By default when you create an Amazon Connect instance, Next Generation Amazon Connect is
  enabled. It's pricing model includes unlimited AI features in Amazon Connect. It's an
  all-inclusive channel pricing model that covers all optimization features for
  usage on your platform.

After you initially create your Amazon Connect instance, you can choose to disable this
option and instead pay separately for channels and any optimization features you
choose to use. For more information, see [Amazon Connect pricing](enable-nextgeneration-amazonconnect.md "enable-nextgeneration-amazonconnect.md").

- Amazon Connect is not available to customers in India using Amazon Web Services through
  Amazon Web Services India Private Limited (AWS India). You will receive an error
  message if you try to create an instance in Amazon Connect.
- When you create an instance, you must decide how you want to manage users.
  **You can't change the identity management option after
  you create the instance**. For more information, see [Plan your identity management in Amazon Connect](connect-identity-management.md "connect-identity-management.md").

## Step 1: Set identity

Permissions to access Amazon Connect features and resource are assigned to user accounts within
Amazon Connect. When you create an instance, you must decide how you want to manage users. You
can't change the identity management option after you create the instance. For more
information, see [Plan your identity management in Amazon Connect](connect-identity-management.md "connect-identity-management.md").

###### To configure identity management for your instance

1. Open the Amazon Connect console at
   [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. Choose **Get started**. If you have previously created an
   instance, choose **Add an instance** instead.
3. Choose one of the following options:
   - **Store users in Amazon Connect** - Use Amazon Connect to create and
     manage user accounts. You cannot share users with other
     applications.
   - **Link to an existing directory** - Use an Directory Service
     directory to manage your users. You can use each directory with one
     Amazon Connect instance at a time.
   - **SAML 2.0-based authentication** - Use an existing
     identity provider (IdP) to federate users with Amazon Connect.

4. If you chose **Store users within Amazon Connect** or **SAML
   2.0-based authentication**, provide the left-most label for
   **Access URL**. This label must be unique across all Amazon Connect
   instances in all Regions. You can't change the access URL after you create your
   instance.
5. If you chose **Link to an existing directory**, select the
   Directory Service directory for **Directory**. The directory name is used
   as the left-most label for **Access URL**.
6. Choose **Next**.

## Step 2: Add administrator

After you specify the user name of the administrator for the Amazon Connect instance, a user
account is created in Amazon Connect and the user is assigned the **Admin**
security profile.

###### To specify the administrator for your instance (Optional)

1. Do one of the following, based on the option that you chose in the previous
   step:
   - If you chose **Store users within Amazon Connect**, select
     **Specify an administrator**, and provide a name,
     password, and email address for the user account in Amazon Connect.
   - If you chose **Link to an existing directory**, for
     **Username**, type the name of an existing user in
     the Directory Service directory. The password for this user is managed through the
     directory.
   - If you chose **SAML 2.0-based authentication**,
     select **Add a new admin** and provide a name for the
     user account in Amazon Connect. The password for this user is managed through the
     IdP.

2. You can also select **No administrator** if an administrator
   is not needed for your instance.
3. (Optional) Add tags to your instance. For more information see [Tagging an Amazon Connect
   instance](tagging-connect-instance.md "tagging-connect-instance.md").
4. Choose **Next**.

## Step 3: Set telephony

Use the options in this section to choose whether you want your agents to receive
calls from customers, make outbound calls, and hear early media audio.

### Early media

When early media audio is enabled, for outbound calls your agents can hear
pre-connection audio such as busy signals, failure-to-connect errors, or other
informational messages provided by telephony providers.

###### Note

The early media feature is not supported for transfers that are dialed through
the [Transfer to phone
number](transfer-to-phone-number.md "transfer-to-phone-number.md") block in flows.

**By default, early media is enabled for you. Note the following
exception:**

- Your instance was created before April 17, 2020, and you weren't enrolled
  in the preview program. You need to enable early media audio. For
  instructions, see [Update telephony and chat options](update-instance-settings.md#update-telephony-options "update-instance-settings.md#update-telephony-options").

###### To configure telephony options for your instance

1. To allow inbound calls to your contact center, choose **Receive
   inbound calls with Amazon Connect**.
2. To enable outbound calling from your contact center, choose **Make
   outbound calls with Amazon Connect**.
3. To enable agents to hear pre-connection audio, choose **Enable early
   media**.
4. To enable up to six participants on a call, choose **Enable
   Multi-Party Calls and Enhanced Monitoring for Voice**.
5. To enable up to six participants on a chat, choose **Enable
   Multi-Party Chats and Enhanced Monitoring for Chat**.
6. Choose **Next**.

## Step 4: Data storage

###### Note

Amazon Connect does not support Amazon S3 Object Lock in compliance mode to store objects using
a write-once-read-many (WORM) model.

When you create an instance, by default we create an Amazon S3 bucket. Data, such as
reports and recordings of conversations, is encrypted using AWS Key Management Service, and then stored
in the Amazon S3 bucket.

This bucket and key are used for both recordings of conversations and exported
reports. Alternatively, you can specify separate buckets and keys for recordings of
conversations and exported reports. For instructions, see [Update settings for your Amazon Connect
instance](update-instance-settings.md "update-instance-settings.md").

###### Note

For voice artifacts (analysis files and redacted audio), Contact Lens uses
the recording key. For chat artifacts (analysis files), it uses the chat recording
key.

**By default, Amazon Connect creates buckets for storing call recordings,
chat transcripts, exported reports, flow logs, and email messages.**

- When a bucket is created to store call recordings, call recording is enabled
  at the instance level. The next step for setting up this functionality is to
  [enable contact recording](set-up-recordings.md "set-up-recordings.md") in a
  flow.
- When a bucket is created to store chat transcripts, chat transcription is
  enabled at the instance level. Now all chat transcripts will be stored.
- When a bucket is created to store email messages, a default Amazon Connect email domain
  is created for your instance. This email domain cannot be customized. After your
  Amazon Connect instance is created, you can add up to five custom email domains that have
  been onboarded to Amazon SES. For more information, see [Enable email for your Amazon Connect instance](enable-email1.md "enable-email1.md").

###### Important

If you choose **Enable Attachments sharing** for your
instance, you must configure a CORS policy on your attachments bucket. If
you don't do this, the email channel will not work for your instance. For
instructions, see [Step 5: Configure a CORS policy on
your attachments bucket](enable-email1.md#config-email-attachments-cors1 "enable-email1.md#config-email-attachments-cors1").

- Live media streaming is not enabled by default.
- Screen recording is not enabled by default. For more information, see [Enable screen recording for your Amazon Connect instance](enable-sr.md "enable-sr.md").

**By default, Amazon Connect creates a Customer Profiles domain**, which stores
profiles that combine customer contact history with customer information such as account
number, address, billing address, and birth date. Data is encrypted using AWS Key Management Service. You
can configure Customer Profiles to use your own customer managed key after your instance is set up. For more
information, see [Create a KMS key to
be used by Customer Profiles to encrypt data (required)](enable-customer-profiles.md#enable-customer-profiles-awsmanagedkey "enable-customer-profiles.md#enable-customer-profiles-awsmanagedkey").

###### Review and copy the location of the S3 bucket, flow logs, and whether you want to

enable Customer Profiles.

1. If desired, copy the location of the S3 bucket where your data encryption is
   stored, and the location of the flow logs in CloudWatch.
2. Choose **Next**.

## Step 5: Review and create

###### To create your instance

1. Review the configuration choices. Remember that you cannot change the identity
   management options after you create the instance.
2. (Optional) To change any of the configuration options, choose
   **Edit**.
3. (Optional) Add tags to your instance. For more information see [Tagging an Amazon Connect
   instance](tagging-connect-instance.md "tagging-connect-instance.md").
4. Choose **Create instance**.
5. (Optional) To continue configuring your instance, choose **Get
   started** and then choose **Let's go**. If you
   prefer, you can access your instance and configure it later on. For more
   information, see [Next steps](#get-started-next-steps "#get-started-next-steps").

If you chose to manage your users directly within Amazon Connect or through an Directory Service
directory, you can access the instance using its access URL. If you chose to
manage your users through SAML-based authentication, you can access the instance
using the IdP.

###### Important

Next Generation Amazon Connect is now enabled. It provides Amazon Connect with unlimited AI features
in an all-inclusive pricing model. To switch to paying separately for channels and
any optimization features you choose, [disable Next
Generation Amazon Connect](enable-nextgeneration-amazonconnect.md#how-to-disable-ac "enable-nextgeneration-amazonconnect.md#how-to-disable-ac").

## Next steps

After you create an instance, you can assign your contact center a phone number or
import your own phone number. For more information, see [Set up contact center phone numbers for your Amazon Connect
instance](ag-overview-numbers.md "ag-overview-numbers.md").
