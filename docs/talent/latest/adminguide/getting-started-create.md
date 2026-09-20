

# Create your Amazon Connect Talent instance
<a name="getting-started-create"></a>

## Start using Amazon Connect Talent
<a name="getting-started-start"></a>

Complete the following high-level steps to start using Amazon Connect Talent:

1. Complete the prerequisites. For more information, see [Prerequisites for Amazon Connect Talent](prerequisites.md).

1. Create an Amazon Connect Talent instance.

1. (Optional) Configure SAML with IAM for single sign-on.

1. Move Amazon SES out of sandbox mode so that you can send email to candidates.

1. Set up your instance for your recruiting team. For more information, see [Set up your instance](getting-started-setup.md).

## Create an Amazon Connect Talent instance
<a name="create-talent-instance"></a>

The instance creation wizard walks you through identity management, administrator setup, permissions, and resource provisioning. The process takes a few minutes.

### Prerequisites
<a name="create-talent-instance-prerequisites"></a>

Before you create an Amazon Connect Talent instance, verify that you have the following:
+ An AWS account with an identity that has permissions to create Amazon Connect Talent resources. Instance creation provisions resources across Connect Customer, Amazon Lex, Connect Customer Cases, Connect Customer Customer Profiles, Amazon Q in Connect, and Amazon SES. For the full list of required permissions, see [IAM permissions and managed policies](prerequisites.md#prerequisites-iam).
+ A valid email address for the administrator account

### To navigate to Amazon Connect Talent
<a name="create-talent-instance-navigate"></a>

You can open Amazon Connect Talent in the AWS Management Console in any of the following ways:
+ Open the [Amazon Connect Talent console](https://console.aws.amazon.com/connect/v2/app/hiring) directly.
+ In the AWS Management Console, enter **Talent** in the search bar, and then choose **Amazon Connect Talent** from the results.
+ In the AWS Management Console, open the [All services](https://console.aws.amazon.com/console/services) page, and then choose **Amazon Connect Talent** under **Business applications**.

The Amazon Connect Talent instances page shows your instances. The page includes the following columns:
+ Instance alias
+ Access URL
+ Create date
+ Status

Choose **Add an instance** to start the creation wizard.

### Step 1: Set identity
<a name="create-talent-instance-identity"></a>

Choose your identity management option:
+ **Store users in Amazon Connect Talent** – Create and manage users directly in Amazon Connect Talent. This is the default option.
+ **SAML 2.0-based authentication** – Use identity federation with SAML 2.0 for single sign-on (SSO).

For **Access URL**, enter a unique alias for your instance. The alias must use lowercase letters, numbers, and hyphens. It must be 1–45 characters and end with `-hiring`.

**Note**  
If you select SAML, users sign in through your organization's identity provider. You must configure SAML integration separately after instance creation.

### Step 2: Add administrator
<a name="create-talent-instance-admin"></a>

Add at least one administrator to your instance.

If you chose **Store users in Amazon Connect Talent**, provide the username, first name, last name, email, and a password (entered twice to verify).

If you chose **SAML 2.0-based authentication**, provide the username, first name, last name, and email.

You can add multiple administrators.

### Step 3: Permissions
<a name="create-talent-instance-permissions"></a>

Review the IAM roles that Amazon Connect Talent creates automatically. These roles allow Amazon Connect Talent to manage its resources and to send email on your behalf. For more information about how Amazon Connect Talent uses IAM, see [Identity and access management for Amazon Connect Talent](security-iam.md).

### Step 4: Review and create
<a name="create-talent-instance-review"></a>

Review your configuration. The review page shows your identity settings, administrator details, and the AWS resources that Amazon Connect Talent provisions for your instance, such as IAM roles, data storage, and email.

Choose **Create instance** to start provisioning.

**Important**  
A progress banner shows the provisioning status. Don't close your browser during instance creation.

### View instance details
<a name="create-talent-instance-details"></a>

After creation completes, choose the instance alias to view details, including the access information for your instance, distribution settings such as the instance ARN, and the AWS resources that Amazon Connect Talent manages for the instance.

## Configure SAML with IAM for Amazon Connect Talent
<a name="configure-saml"></a>

Amazon Connect Talent supports identity federation with SAML 2.0 through AWS IAM. This enables web-based single sign-on (SSO) from your organization's identity provider to your talent instance.

**Important**  
Consider the following when you configure SAML for Amazon Connect Talent:  
Choosing SAML requires IAM federation configuration.
The username must match the `RoleSessionName` SAML attribute.
Amazon Connect Talent doesn't support reverse federation. Authentication must happen from the identity provider (IdP).
Most IdPs use the global AWS sign-in endpoint by default. You must override this to the regional endpoint.
All usernames are case sensitive.
SAML for Amazon Connect Talent is available in supported Regions. For more information, see [Supported Regions and endpoints](what-is-talent.md#talent-regions-endpoints).

### Overview of the SAML authentication flow
<a name="configure-saml-overview"></a>

The following steps describe the SAML authentication flow for Amazon Connect Talent:

1. The user browses to an internal portal that contains a link to Amazon Connect Talent.

1. The federation service requests authentication from the identity store.

1. The identity store authenticates the user and returns the authentication response.

1. The federation service posts the SAML assertion to the browser.

1. The browser posts the assertion to the AWS sign-in SAML endpoint. AWS authenticates the user and redirects to Amazon Connect Talent.

1. Amazon Connect Talent authorizes the user and opens the instance.

### To enable SAML-based authentication
<a name="configure-saml-enable"></a>

Complete the following high-level steps to enable SAML-based authentication:

1. Create an Amazon Connect Talent instance with SAML 2.0 identity management.

1. Enable SAML federation between your IdP and AWS.

1. Add users to your instance. Usernames must match exactly between your IdP and Amazon Connect Talent.

1. Configure your IdP for SAML assertions, authentication response, and relay state.

### To enable SAML federation between your IdP and AWS
<a name="configure-saml-federation"></a>

1. Create a SAML provider in AWS.

1. Create an IAM role for SAML 2.0 federation. Add a permissions policy that uses the `connect:GetFederationToken` action.

1. Configure your network as a SAML provider for AWS.

1. Configure SAML assertions for the authentication response. Leave the **Application Start URL** blank.

1. Override the Assertion Consumer Service (ACS) URL to the regional endpoint.

1. Configure the relay state URL for your Region and instance.

### IAM policy examples
<a name="configure-saml-iam-policies"></a>

The following example shows an IAM policy that allows all users in a specific instance to federate into Amazon Connect Talent.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "connect:GetFederationToken",
            "Resource": "arn:aws:connect:{{region}}:{{123456789012}}:instance/{{instance-id}}/user/${aws:userid}"
        }
    ]
}
```

The following example uses an instance ID condition instead of a resource ARN.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "connect:GetFederationToken",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "connect:InstanceId": "{{instance-id}}"
                }
            }
        }
    ]
}
```

### Configure regional SAML endpoints
<a name="configure-saml-regional-endpoints"></a>

1. Update the ACS URL to the regional endpoint. For example: `https://us-west-2.signin.aws.amazon.com/saml`

1. Update the role trust policy to include the regional endpoint in the `SAML:aud` condition.

1. Configure the relay state for the region-specific console.

The session duration is 12 hours. We recommend that users log out of both Amazon Connect Talent and the identity provider when they finish their session.

## Move Amazon SES out of sandbox mode
<a name="getting-started-ses"></a>

Amazon Connect Talent uses Amazon SES to send evaluation invitations to candidates by email. New Amazon SES accounts start in the sandbox, where you can send email only to verified addresses and lower sending limits apply. To send invitations to candidates who are not verified addresses, request production access for Amazon SES.

**Important**  
Until you move Amazon SES out of sandbox mode, Amazon Connect Talent can't send evaluations to candidates by email or support internal testing.

To request production access:

1. Open the Amazon SES [Get set up](https://console.aws.amazon.com/ses/home#/get-set-up) page.

1. In the **Request production access** card, choose **Request production access**.

1. For **Mail type**, choose **Transactional**.

1. For **Website URL**, enter your organization's website URL.

1. (Optional) For **Additional contacts**, enter up to four email addresses, separated by commas, where you want to receive communications about your request.

1. For **Preferred contact language**, choose **English** or **Japanese**.

1. Under **Acknowledgement**, select the box to agree to the AWS Service Terms and Acceptable Use Policy.

1. Choose **Submit request**.

After you submit, you can't edit your details until the review is complete. The AWS Support team provides an initial response within 24 hours. For more information, see [Request production access (moving out of the Amazon SES sandbox)](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html) in the *Amazon Simple Email Service Developer Guide*.

After you create your instance, see [Set up your instance](getting-started-setup.md) to configure it for your recruiting team.