# Setting Up Accounts and Tools

The following topics describe the tasks you need to perform before you can use
Amazon Mechanical Turk.

###### Topics

- [Step 1: Sign Up for an AWS Account](#setup-aws-account "#setup-aws-account")
- [Step 2: Create a Requester Account](#accountsetup "#accountsetup")
- [Step 3: Link Your AWS account to your MTurk Requester account](#accountlinking "#accountlinking")
- [Step 4: Create an IAM User](#create-iam-user-or-role "#create-iam-user-or-role")
- [Step 5: Set up the Developer Sandbox](#gsg-use-the-sandbox "#gsg-use-the-sandbox")
- [Step 6: Set up an AWS SDK](#toolsinstallation "#toolsinstallation")
- [Step 7: Prepay for Your HITs or Enable AWS Billing](#prepay-for-your-hits "#prepay-for-your-hits")
- [Creating a HIT Tutorial](#creating-a-hit-next "#creating-a-hit-next")

## Step 1: Sign Up for an AWS Account

To develop solutions using the Amazon Mechanical Turk web service, you must first sign up for an AWS
account. An AWS account is an Amazon.com account that enables you to use services from
AWS.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

Using your AWS account, you can view your AWS account activity and usage reports and
manage your security credentials.

### AWS Security Credentials

AWS uses access keys to help protect your data when you access AWS
programmatically. An access key consists of two parts: an access key ID, which is
similar to a user name, and a secret access key, which is similar to a
password.

- Sample access key ID: AKIAIOSFODNN7EXAMPLE
- Sample secret access key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

You use access keys to sign programmatic requests that you make to the Amazon Mechanical Turk
API using [a supported AWS SDK](https://requester.mturk.com/developer/ "https://requester.mturk.com/developer/"). You can use these access
keys in both the sandbox and the production environment.

###### Note

Although you may use your AWS _[root
credentials](../../../glossary/latest/reference/glos-chap.md#root_credentials "../../../glossary/latest/reference/glos-chap.md#root_credentials")_ to access the Mechanical Turk API, we recommend that
instead you create an IAM _[user](../../../glossary/latest/reference/glos-chap.md#AWSUser "../../../glossary/latest/reference/glos-chap.md#AWSUser")_ and use those credentials instead. Please note
that Mechanical Turk does not currently support the use of IAM role credentials.

###### To manage your AWS security credentials

1. Sign in to the Amazon Web Services website at [http://aws.amazon.com/security-credentials](http://aws.amazon.com/security-credentials "http://aws.amazon.com/security-credentials").
2. Do one of the following:
   - If you signed in using your root credentials, choose
     **Continue to Security
     Credentials**.
   - If you signed in as an IAM user, choose **Access
     Keys (Access Key ID and Secret Access
     Key)**.

3. Choose **Create New Access Key**.
4. In **Create Access Key**, choose **Download Key
   File**.
5. The private key file (`rootkey.csv`) is automatically
   downloaded by your browser. Save the private key file in a safe
   place.

###### Important

This is the only chance for you to save the private key file. You will
need these credentials to use the Amazon Mechanical Turk API.

## Step 2: Create a Requester Account

Before you can use Amazon Mechanical Turk, you must have an Amazon Mechanical Turk Requester account.

###### To create and register a Requester account

1. Go to [https://requester.mturk.com](https://requester.mturk.com "https://requester.mturk.com").
2. Click **Create an Account**.
3. Enter your email address.
4. Follow the prompts to complete your Requester account registration.

When prompted, type your mailing address and accept the **Amazon Mechanical Turk
Participation Agreement**.

## Step 3: Link Your AWS account to your MTurk Requester account

Next, you will need to link your AWS Account to your MTurk Requester Account.
This operation grants permission to your AWS Account to access your Requester account using the MTurk APIs.

1. Go to [https://requester.mturk.com/developer](https://requester.mturk.com/developer "https://requester.mturk.com/developer").
2. Click **Link your AWS Account** and sign-in with your AWS Root user email address and password.

## Step 4: Create an IAM User

With [AWS Identity and Access Management](http://aws.amazon.com/iam/ "http://aws.amazon.com/iam/") (IAM) you can
securely control access to AWS services and resources for your users. Creating an
IAM user allows you to use these credentials to access the Amazon Mechanical Turk API instead of
using your [root account
credentials](../../../glossary/latest/reference/glos-chap.md#root_credentials "../../../glossary/latest/reference/glos-chap.md#root_credentials"). Please note that Mechanical Turk does not currently support the use of IAM role credentials.

###### Note

You use IAM credentials only to authenticate Mechanical Turk API requests. You cannot use
them to log in to the Mechanical Turk Requester website.

###### To create an IAM user

1. Sign in to the Amazon Web Services website at [http://aws.amazon.com/security-credentials](http://aws.amazon.com/security-credentials "http://aws.amazon.com/security-credentials").
2. Choose **Get Started With IAM Users**.
3. Choose **Add user**.
4. Under **Set user details**, type the name for your user. To add multiple users with the same access types and permissions, click the **Add another user** link to enter another user name to create.
5. Under **Select AWS access type**, make sure **Programmatic access** is
   selected and choose **Next: Permissions** to move to the next step.
6. Under **Set permissions**, choose **Attach existing policies directly**.
7. Select the **AmazonMechanicalTurkFullAccess** or **AmazonMechanicalTurkReadOnly** policy, depending on the level of control you want to grant.
8. Choose **Next: Tags** to continue.
9. There is no need to add tags. Choose **Next: Review** to continue.
10. Review the settings you selected and choose **Create user** or **Create users** as appropriate.
11. The user is added. To download the user's credentials for use with SDKs or the CLI, either choose **Download .csv** to download the information of the user or users created. Alternatively, click the **Show** link next to the obscured **secret access key**. Copy it somewhere secure as you will only be able to view it once.

###### To set up Amazon Mechanical Turk permissions for previously created IAM users

1. Read [Overview of IAM Policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User
   Guide_.
2. Sign in to the IAM console at [https://console.aws.amazon.com/iam/home#policies](https://console.aws.amazon.com/iam/home#policies "https://console.aws.amazon.com/iam/home#policies").
3. On the **Policies** page, choose
   **AmazonMechanicalTurkFullAccess** or
   **AmazonMechanicalTurkReadOnly**.
4. At the top of the page, choose **Policy Actions** and then
   choose **Attach**.
5. On the **Attach Policy** page, select the IAM user(s) that
   you want to set permissions for. Then choose **Attach Policy**
   to give those users permission to access the Mechanical Turk API.

### What is supported?

|                                                              |     |
| ------------------------------------------------------------ | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| API authentication using IAM credentials                     | Yes |
| Website authentication using IAM credentials                 | No  |
| Action-level permissions for IAM users                       | Yes |
| Resource-level permissions for IAM users                     | No  |
| Tag-based permissions for IAM users                          | No  |
| Authentication using temporary credentials (roles or groups) | No  |
| Authentication using federated user credentials              | No  | ## Step 5: Set up the Developer Sandbox You should test your HITs in the Amazon Mechanical Turk sandbox testing environment to make sure they work as expected before publishing your HITs in the Mechanical Turk marketplace. The sandbox provides a testing environment where you can publish and work on HITs to try them out before publishing them in the Amazon Mechanical Turk Marketplace. The sandbox consists of a Requester sandbox website and a Worker sandbox website. You will need to create a Requester account on the Requester sandbox website, which is located at [https://requestersandbox.mturk.com](https://requestersandbox.mturk.com "https://requestersandbox.mturk.com"). You'll also need to create a Worker account on the Worker sandbox website located at [https://workersandbox.mturk.com](https://workersandbox.mturk.com "https://workersandbox.mturk.com") to view your sandbox created HITs as a Worker. There is no charge for using the Mechanical Turk sandbox sites. ###### Note To create HITs in the sandbox using the MTurk APIs, you will also need to link your AWS account to your sandbox Requester account as per [Link Your AWS account to your MTurk Requester account](#accountlinking "#accountlinking"), on the Requester sandbox website at [https://requestersandbox.mturk.com/developer](https://requestersandbox.mturk.com/developer "https://requestersandbox.mturk.com/developer"). When testing in the sandbox, test each HIT in all the major Internet browsers to make sure your HIT works the same in each browser. If you have links to pictures or videos in your HITs, make sure the links work. Also, your testing should include verifying that the format of the submitted answers is acceptable. ## Step 6: Set up an AWS SDK The MTurk API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/") (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/ "https://aws.amazon.com/sdk-for-node-js/") or [Browser](https://aws.amazon.com/sdk-for-browser/ "https://aws.amazon.com/sdk-for-browser/")), [Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/"), [.NET](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/"), [Go](https://aws.amazon.com/sdk-for-go/ "https://aws.amazon.com/sdk-for-go/"), [Ruby](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/"), [PHP](https://aws.amazon.com/sdk-for-php/ "https://aws.amazon.com/sdk-for-php/") or [C++](https://aws.amazon.com/sdk-for-cpp/ "https://aws.amazon.com/sdk-for-cpp/"). Configure the AWS SDK to use the ‘us-east-1’ region. This is the region in which the MTurk API is available. Then connect to the [MTurk Developer Sandbox](https://requestersandbox.mturk.com "https://requestersandbox.mturk.com") and check your [account balance](../AWSMturkAPI/ApiReference_GetAccountBalanceOperation.md "../AWSMturkAPI/ApiReference_GetAccountBalanceOperation.md") (the Sandbox should always return a balance of $10,000). To connect to the MTurk Developer Sandbox, set the API endpoint in your SDK to **https://mturk-requester-sandbox.us-east-1.amazonaws.com**. You can find [examples here](https://requester.mturk.com/developer "https://requester.mturk.com/developer"). ## Step 7: Prepay for Your HITs or Enable AWS Billing Before you use the production version of Amazon Mechanical Turk you need to prepay for the HITs you create. Otherwise, you can't post your HITs to Workers. To post your HITs to Workers, you must have money in your Prepaid HIT Balance to prepay for all of your HITs. You can use a credit or debit card or debit card to prepay for the HITs. Alternatively, you can enable AWS Billing for your account. You will see rewards and fees associated with your HITs on the AWS Anniversary Bill for your linked AWS account. For instructions on how to prepay for your HITs or to enable AWS Billing, go to the [Requester website](http://requester.mturk.com/mturk/youraccount "http://requester.mturk.com/mturk/youraccount"). ## Creating a HIT Tutorial The [Creating a HIT](CreatingAHIT.md "CreatingAHIT.md") tutorial in the next section takes you step-by-step through using Amazon Mechanical Turk to create a HIT. |
