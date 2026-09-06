

# Account access manager
<a name="account-access-manager"></a>

## What is account access manager?
<a name="what-is-account-access-manager"></a>

Account access manager lets you assign AWS account access to users and groups in your IAM Identity Center organization instance. You assign access using the [IAM roles](id_roles.md) in your AWS accounts. You can use account access manager alongside [IAM Identity Center permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) or on its own. Both account access manager and IAM Identity Center permission sets use the users and groups that you synchronized from your identity source or created directly in [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

## Why use account access manager?
<a name="why-use-account-access-manager"></a>

Account access manager enables you to assign your existing IAM roles to the users and groups you have synchronized into IAM Identity Center from your corporate source of identities. Using your existing IAM roles gives you extra flexibility to tailor user access, including:
+ Configure IAM role tags and use session tags for attribute-based access control (ABAC).
+ Configure IAM role trust policy to restrict role assumption or use IdP-asserted claims as trust policy conditions.
+ Configure IAM role paths to group roles logically and simplify administration. For more information, see [Configure IAM role paths to group roles logically and simplify administration](https://aws.amazon.com/blogs/security/optimize-aws-administration-with-iam-paths/).

The following table compares the three account access options:


|   | IAM roles \+ account access manager | IAM Identity Center permission sets | IAM roles \+ IAM federation (direct role assumption) | 
| --- | --- | --- | --- | 
| Best for | Custom IAM roles that vary across accounts | Uniform baseline human access such as read-only and admin provisioned as immutable IAM roles | Suitable for workloads | 
| Scope | Multiple accounts (AWS organization) | Multiple accounts (AWS organization) | Per account | 
| IAM role provisioning | Requires infrastructure as code (IaC) or manual provisioning through the AWS IAM console | Automatically provisioned | Requires infrastructure as code (IaC) or manual provisioning through AWS IAM and external IdP consoles | 
| Role-to-identity mapping resides in | Account access manager | IAM Identity Center | External IdP | 
| End user experience | Users access AWS accounts through the AWS account access portal URL after signing into AWS as IAM Identity Center users. | Users access AWS accounts through the AWS access portal after signing into AWS as IAM Identity Center users. | Users access AWS accounts through account-specific SAML applications (icons) in their IdP portal. | 
| AWS CLI user experience | 1.  User signs into AWS and then accesses an account with a specific role in a web browser. <br />2.  User types **aws login** on the command line to retrieve the IAM role session credentials from the browser. For the duration of the IAM role session, the user can keep working with the AWS CLI without having to re-authenticate in step 1.  | User configures a profile including the desired account and role pair by typing aws configure sso. User types aws sso login to initiate a new session using a profile. If there is no active IAM Identity Center session, the user authenticates in a browser and authorizes access there. See the [AWS IAM Identity Center User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) for more details. | Custom integrations using AWS SDK credential providers | 

## Key capabilities
<a name="aam-key-capabilities"></a>

**Account access portal**  
Account access manager provides users with an account access portal where they can view and access the AWS accounts assigned to them through account access manager.

**CLI access**  
Your workforce can access AWS accounts through the AWS CLI using the [**aws login** command](https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html#command-line-sign-in-local-development) after signing into AWS in a browser.

**Account access APIs**  
Account access manager has its own API namespace, `account-access`, which is separate from the IAM API. You use this namespace in the AWS CLI and SDKs.