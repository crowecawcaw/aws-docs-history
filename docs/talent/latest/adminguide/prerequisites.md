

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

**Important**  
Service quotas can block instance creation. The Amazon Connect instance count quota is shared across Amazon Connect Talent and Amazon Connect, so instances of either count toward the same limit. By default, you can create 2 instances per AWS Region, and other account-level quotas limit this further. If you reach one of these quotas, instance creation fails with a generic error that does not name the quota. Before you create an instance, review [Quotas that limit how many instances you can create](endpoints-quotas.md#talent-quotas-instance-count) and request any increases you need.

## IAM permissions and managed policies
<a name="prerequisites-iam"></a>

For details about how Amazon Connect Talent works with IAM, the AWS managed policies that are available, and example policies, see [Identity and access management for Amazon Connect Talent](security-iam.md).

### Managing your Amazon Connect Talent instance
<a name="prerequisites-iam-managing"></a>

The following section describes the IAM permissions required to create an Amazon Connect Talent instance.

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

## Amazon SES requirements
<a name="prerequisites-ses"></a>

Amazon Connect Talent uses Amazon SES to send email to candidates, such as invitations to complete an evaluation. New Amazon SES accounts start in the Amazon SES sandbox. While your account is in the sandbox, you can send email only to verified addresses, and daily and per-second sending limits apply.

To send email to candidates who are not verified addresses, request production access to move your account out of the sandbox. For instructions, see [Move Amazon SES out of sandbox mode](getting-started-create.md#getting-started-ses).

**Important**  
Before you can complete internal testing or send evaluations to candidates, complete both of the following:  
Move Amazon SES out of sandbox mode. See [Move Amazon SES out of sandbox mode](getting-started-create.md#getting-started-ses).
Set your service quotas to the values you need. Review [Service quotas and endpoints for Amazon Connect Talent](endpoints-quotas.md) and use the values in the tables to request any quota increases before you send evaluations.