

# Create a Connect Customer instance

The first step in setting up your Connect Customer contact center is to create a virtual contact center instance. Each instance contains all the resources and settings related to your contact center. 

## Things to know before you begin
<a name="get-started-prerequisites"></a>
+ When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed up for all services in AWS, including Connect Customer. You are charged only for the services that you use. To create an AWS account, see [How/ do I create and activate an AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
+ To allow a user to create an instance, make sure that they have the permissions granted by the **AmazonConnect\_FullAccess** policy.
+ For a list of the minimum IAM permissions required to create an instance, see [Required permissions for using custom IAM policies to manage access to the Connect Customer console](security-iam-amazon-connect-permissions.md).
+ When you create an instance, it is a [Connect Customer](enable-nextgeneration-amazonconnect.md) instance, which has an all-inclusive channel pricing model that covers all optimization features for usage on your platform.
+ Connect Customer is not available to customers in India using Amazon Web Services through Amazon Web Services India Private Limited (AWS India). You will receive an error message if you try to create an instance in Connect Customer.
+ When you create an instance, you must decide how you want to manage users. **You can't change the identity management option after you create the instance**. For more information, see [Plan your identity management in Connect Customer](connect-identity-management.md).

## Step 1: Set identity
<a name="get-started-identity-management"></a>

Permissions to access Connect Customer features and resource are assigned to user accounts within Connect Customer. When you create an instance, you must decide how you want to manage users. You can't change the identity management option after you create the instance. For more information, see [Plan your identity management in Connect Customer](connect-identity-management.md).

**To configure identity management for your instance**

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. Choose **Get started**. If you have previously created an instance, choose **Add an instance** instead.

1. Choose one of the following options:
   + **Store users in Connect Customer** - Use Connect Customer to create and manage user accounts. You cannot share users with other applications.
   + **Link to an existing directory** - Use an Directory Service directory to manage your users. You can use each directory with one Connect Customer instance at a time.
   + **SAML 2.0-based authentication** - Use an existing identity provider (IdP) to federate users with Connect Customer.

1. If you chose **Store users within Connect Customer** or **SAML 2.0-based authentication**, provide the left-most label for **Access URL**. This label must be unique across all Connect Customer instances in all Regions. You can't change the access URL after you create your instance.

1. If you chose **Link to an existing directory**, select the Directory Service directory for **Directory**. The directory name is used as the left-most label for **Access URL**.

1. Choose **Next**.

## Step 2: Add administrator
<a name="get-started-administrator"></a>

After you specify the user name of the administrator for the Connect Customer instance, a user account is created in Connect Customer and the user is assigned the **Admin** security profile.

**To specify the administrator for your instance (Optional)**

1. Do one of the following, based on the option that you chose in the previous step:
   + If you chose **Store users within Connect Customer**, select **Specify an administrator**, and provide a name, password, and email address for the user account in Connect Customer.
   + If you chose **Link to an existing directory**, for **Username**, type the name of an existing user in the Directory Service directory. The password for this user is managed through the directory.
   + If you chose **SAML 2.0-based authentication**, select **Add a new admin** and provide a name for the user account in Connect Customer. The password for this user is managed through the IdP.

1. You can also select **No administrator** if an administrator is not needed for your instance.

1. (Optional) Add tags to your instance. For more information see [Tagging an Connect Customer instance](tagging-connect-instance.md).

1. Choose **Next**.

## Step 3: Set telephony
<a name="get-started-telephony"></a>

Use the options in this section to choose whether you want your agents to receive calls from customers, make outbound calls, and hear early media audio.

### Early media
<a name="early-media"></a>

When early media audio is enabled, for outbound calls your agents can hear pre-connection audio such as busy signals, failure-to-connect errors, or other informational messages provided by telephony providers.

**Note**  
The early media feature is not supported for transfers that are dialed through the [Transfer to phone number](transfer-to-phone-number.md) block in flows.

 **By default, early media is enabled for you. Note the following exception:** 
+ Your instance was created before April 17, 2020, and you weren't enrolled in the preview program. You need to enable early media audio. For instructions, see [Update telephony and chat options](update-instance-settings.md#update-telephony-options).

**To configure telephony options for your instance**

1. To allow inbound calls to your contact center, choose **Receive inbound calls with Connect Customer**.

1. To enable outbound calling from your contact center, choose **Make outbound calls with Connect Customer**.

1. To enable agents to hear pre-connection audio, choose **Enable early media**.

1. To enable up to six participants on a call, choose **Enable Multi-Party Calls and Enhanced Monitoring for Voice**.

1. To enable up to six participants on a chat, choose **Enable Multi-Party Chats and Enhanced Monitoring for Chat**.

1. Choose **Next**.

**Note**  
Chat is enabled by default for all Connect Customer instances.

## Step 4: Data storage
<a name="get-started-data-storage"></a>

**Note**  
Connect Customer does not support Amazon S3 Object Lock in compliance mode to store objects using a write-once-read-many (WORM) model.

When you create an instance, by default we create an Amazon S3 bucket. Data, such as reports and recordings of conversations, is encrypted using AWS Key Management Service, and then stored in the Amazon S3 bucket.

This bucket and key are used for both recordings of conversations and exported reports. Alternatively, you can specify separate buckets and keys for recordings of conversations and exported reports. For instructions, see [Update settings for your Connect Customer instance](update-instance-settings.md).

**Note**  
For voice artifacts (analysis files and redacted audio), conversational analytics uses the recording key. For chat artifacts (analysis files), it uses the chat recording key.

 **By default, Connect Customer creates buckets for storing call recordings, chat transcripts, exported reports, flow logs, and email messages. ** 
+ When a bucket is created to store call recordings, call recording is enabled at the instance level. The next step for setting up this functionality is to [enable contact recording](set-up-recordings.md) in a flow.
+ When a bucket is created to store chat transcripts, chat transcription is enabled at the instance level. Now all chat transcripts will be stored.
+ When a bucket is created to store email messages, a default Connect Customer email domain is created for your instance. This email domain cannot be customized. After your Connect Customer instance is created, you can add up to five custom email domains that have been onboarded to Amazon SES. For more information, see [Enable email for your Connect Customer instance](enable-email1.md). 
**Important**  
 If you choose **Enable Attachments sharing** for your instance, you must configure a CORS policy on your attachments bucket. If you don't do this, the email channel will not work for your instance. For instructions, see [Step 5: Configure a CORS policy on your attachments bucket](enable-email1.md#config-email-attachments-cors1).
+ Live media streaming is not enabled by default.
+ Screen recording is not enabled by default. For more information, see [Enable screen recording for your Connect Customer instance](enable-sr.md).

**By default, Connect Customer creates a Customer Profiles domain**, which stores profiles that combine customer contact history with customer information such as account number, address, billing address, and birth date. Data is encrypted using AWS Key Management Service. You can configure Customer Profiles to use your own customer managed key after your instance is set up. For more information, see [Create a KMS key to be used by Customer Profiles to encrypt data (required)](enable-customer-profiles.md#enable-customer-profiles-awsmanagedkey). 

**By default, Connect Customer enables Cases.** When **Enable Cases** is selected, Connect Customer creates a Cases domain named `amazon-connect-{{instance-alias}}` and associates it with your instance. You can change the domain name under **Customize data storage (advanced)**. To skip Cases, clear **Enable Cases**. You can enable Cases later from the instance's **Cases** page. For more information, see [Enable Cases using the Connect Customer console](enable-cases.md).

**Enable Cases event streams** is selected by default when Cases is enabled. When it's selected, Connect Customer completes the following manual procedures for you:
+ **Enable case event streams.** Connect Customer turns on case event streams for the domain, so an event is published to the default Amazon EventBridge event bus in your account each time a case is created, updated, or deleted. Events include all current and future case fields and related item content. You can also set this up after instance creation by following the steps in [Enable Cases integrations](enable-cases.md#configure-cases-integrations).
+ **Send case updates to conversational analytics rules.** Connect Customer creates the `amazon-connect-cases` event integration and associates it with your instance, so you can create rules that run when a case is created or updated. For instructions on setting this up manually, see [Allow Connect Customer Cases to send updates to conversational analytics rules using the CLI](cases-rules-integration-onboarding.md).
+ **Send case data to Customer Profiles.** If Customer Profiles is also enabled, Connect Customer streams case events to a dedicated event bus and uses Amazon AppIntegrations to forward them to Customer Profiles, so cases appear on customer profiles. For instructions on setting this up manually, see [Set up integration for Connect Customer Cases using the CLI](set-up-integration-for-amazon-connect-cases.md). Connect Customer creates the same resources as that procedure:
  + An event bus named `connect-cases-to-customer-profiles`.
  + A rule named `connect-cases-to-customer-profiles-rule` on the default event bus that matches `CASE.CREATED`, `CASE.UPDATED`, and `CASE.DELETED` events from `aws.cases` and sends them to the dedicated event bus.
  + An IAM role named `service-role/AmazonConnectCasesEventBridgeRole-{{region}}` that the rule uses to send events to the dedicated event bus.
  + An event integration named `Connect-Cases-Event-Integration` on the dedicated event bus, registered with your Customer Profiles domain for the `Connect-case` object type.

**Note**  
The event bus, rule, IAM role, and event integrations are shared by all instances in the account and Region. If you already created them manually, or one of them already exists, Connect Customer reuses it as is and doesn't update or replace it. The IAM role can publish events only to the `connect-cases-to-customer-profiles` event bus in the same Region, and only EventBridge (`events.amazonaws.com`) can assume it.  
To create these resources, the IAM principal that creates the instance needs additional permissions. For more information, see [Enable Cases when you create an instance](required-permissions-iam-cases.md#instance-creation-cases-iam). If a permission is missing, the instance is still created, and the console shows which step failed. You can finish setting up Cases from the instance's **Cases** page.

**Review and copy the location of the S3 bucket, flow logs, and whether you want to enable Customer Profiles and Cases.**

1. If desired, copy the location of the S3 bucket where your data encryption is stored, and the location of the flow logs in CloudWatch.

1. Choose **Next**.

## Step 5: Review and create
<a name="get-started-review"></a>

**To create your instance**

1. Review the configuration choices. Remember that you cannot change the identity management options after you create the instance.

1. If you enabled Cases, review the **Cases** section. It lists the resources that Connect Customer creates or reuses: the Cases domain, the Cases event integration, and, if Customer Profiles is enabled, the dedicated event bus, forwarding rule, EventBridge delivery role, and Customer Profiles integration. After the instance is created, this section shows the ARNs of these resources, which you can copy.

1. (Optional) To change any of the configuration options, choose **Edit**.

1. (Optional) Add tags to your instance. For more information see [Tagging an Connect Customer instance](tagging-connect-instance.md).

1. Choose **Create instance**.

1. (Optional) To continue configuring your instance, choose **Get started** and then choose **Let's go**. If you prefer, you can access your instance and configure it later on. For more information, see [Next steps](#get-started-next-steps).

   If you chose to manage your users directly within Connect Customer or through an Directory Service directory, you can access the instance using its access URL. If you chose to manage your users through SAML-based authentication, you can access the instance using the IdP.

## Next steps
<a name="get-started-next-steps"></a>

After you create an instance, you can assign your contact center a phone number or import your own phone number. For more information, see [Set up contact center phone numbers for your Connect Customer instance](ag-overview-numbers.md).