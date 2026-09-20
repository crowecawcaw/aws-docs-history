

# Prerequisites for Amazon Connect Talent
<a name="prerequisites"></a>

Before you set up Amazon Connect Talent, review the following requirements.

**Topics**
+ [AWS account requirements](#prerequisites-account)
+ [IAM permissions and managed policies](#prerequisites-iam)
+ [Amazon SES requirements](#prerequisites-ses)

## AWS account requirements
<a name="prerequisites-account"></a>

To create an Amazon Connect Talent instance, you need the following:
+ An active AWS account.
+ Access to a supported AWS Region. For more information, see [Supported Regions and endpoints](what-is-talent.md#talent-regions-endpoints).
+ A valid email address for the first administrator of the instance.

Avoid using your AWS account root user for everyday tasks. Instead, create an administrative user in IAM and use it to set up and manage Amazon Connect Talent.

## IAM permissions and managed policies
<a name="prerequisites-iam"></a>

For details about how Amazon Connect Talent works with IAM, the AWS managed policies that are available, and example policies, see [Identity and access management for Amazon Connect Talent](security-iam.md).

### Managing your Amazon Connect Talent instance
<a name="prerequisites-iam-managing"></a>

The following sections describe the IAM permissions required to create and delete an Amazon Connect Talent instance.

#### Create an instance
<a name="prerequisites-iam-create"></a>

The IAM identity (user or role) that creates an Amazon Connect Talent instance needs permissions across several AWS services, because the setup process provisions resources in Connect Customer, Amazon Lex, Connect Customer Cases, Connect Customer Customer Profiles, Amazon Q in Connect, and Amazon SES.

As a recommended approach, grant the creating identity the following permissions:
+ `AmazonConnect_FullAccess`
+ `AmazonLexFullAccess`
+ Full access to Connect Customer Cases, Connect Customer Customer Profiles, Amazon Q in Connect, and Amazon SES
+ `iam:CreateServiceLinkedRole`, `iam:PassRole`, and AWS KMS grant permissions

For a least-privilege alternative, use action-level policies scoped to only the actions the setup process requires.

An identity with the `AdministratorAccess` managed policy can also create instances. Use the scoped approach when possible to follow the principle of least privilege.

When you create an instance, Amazon Connect Talent also provisions the IAM roles it needs to operate on your behalf.

#### Delete an instance
<a name="prerequisites-iam-delete"></a>

To delete an Amazon Connect Talent instance, the identity performing the deletion needs permissions to remove resources across the same services that were provisioned during creation.

The following permissions are required, grouped by service:
+ **Connect Customer** – `connect:DeleteInstance`, `connect:DeleteIntegrationAssociation`, `connect:DisassociateBot`
+ **Amazon Lex** – `lex:ListBots`, `lex:ListBotAliases`, `lex:DeleteBotAlias`, `lex:DeleteBot`
+ **Connect Customer Customer Profiles** – `profile:DeleteDomain`, `profile:DeleteIntegration`, `profile:DeleteProfileObjectType`
+ **Connect Customer Cases** – `cases:DeleteDomain`
+ **Amazon Q in Connect** – `wisdom:DeleteAssistant`
+ **Amazon SES** – `ses:DeleteEmailIdentity`

An identity with the `AdministratorAccess` managed policy can also delete instances.

##### Clean up resources after deleting an instance
<a name="prerequisites-iam-cleanup"></a>

After you delete an Amazon Connect Talent instance, some resources provisioned during instance creation might not be removed automatically. You need to manually delete these resources from your AWS account in the same AWS Region as the instance.

The following resources might need manual cleanup:


| Resource | Name pattern | How to delete | 
| --- | --- | --- | 
| Amazon Lex bots (up to 3) | {{instance-alias}}-hiring-interview-lex-bot, {{instance-alias}}-hiring-chat-lex-bot, {{instance-alias}}-hiring-assessment-lex-bot | First disassociate the bot from the Connect Customer instance, then delete the bot in the Amazon Lex console. | 
| Connect Customer Customer Profiles domain | amazon-connect-hiring-{{instance-alias}} | Delete in the Connect Customer Customer Profiles console. | 
| Connect Customer Cases domain | Uses the instance alias | Delete in the Connect Customer Cases console. | 
| Amazon Q in Connect assistant | Hiring Interview Assistant | Delete in the Amazon Q in Connect console. | 

If you're unable to identify which resources were left behind, contact [AWS Support](https://aws.amazon.com/premiumsupport/).

## Amazon SES requirements
<a name="prerequisites-ses"></a>

Amazon Connect Talent uses Amazon SES to send email to candidates, such as invitations to complete an evaluation. New Amazon SES accounts start in the Amazon SES sandbox. While your account is in the sandbox, you can send email only to verified addresses, and daily and per-second sending limits apply.

To send email to candidates who are not verified addresses, request production access to move your account out of the sandbox. For instructions, see [Move Amazon SES out of sandbox mode](getting-started-create.md#getting-started-ses).