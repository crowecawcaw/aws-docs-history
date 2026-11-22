

# Sharing transformation definitions across AWS accounts

You can share a transformation definition (TD) that your AWS account published, and optionally its lessons, with other AWS accounts, with organizational units (OUs), or with your entire organization in AWS Organizations. Accounts that you share with can run the TD without publishing their own copy. You keep one TD with one identity, one version history, and one set of lessons.

AWS Transform custom uses AWS RAM (AWS RAM) to share TDs. In AWS RAM, a TD is a resource of type `transform-custom:Package`. A *share* (an AWS RAM resource share) is its own resource. It ties together the TD, the principals that get access (accounts, OUs, or your organization), and one managed permission that says what those principals can do.

## How sharing works
<a name="custom-sharing-how-it-works"></a>

Sharing follows the AWS RAM owner and consumer model.
+ **Owner account** – The AWS account that published the TD. Only the owner can publish new versions, change the TD, delete it, share it, change a share's permission, or revoke a share.
+ **Consumer account** – An AWS account that the TD is shared with. Depending on the share's permission, IAM principals in the consumer account can run the TD, use the owner's lessons, contribute new lessons to the owner, or download the TD's content. A consumer can't change, delete, publish, or reshare the TD.

The following table shows who you can share with, and whether the consumer has to accept.


| Share with | How you specify it | Does the consumer accept? | 
| --- | --- | --- | 
| Your entire organization | Organization ARN | No. All current and future accounts in the organization get access right away. Sharing with AWS Organizations must first be turned on in AWS RAM. For more information, see [Prerequisites for sharing](custom-sharing-prerequisites.md). | 
| An OU in your organization | OU ARN | No. All current and future accounts in the OU and its child OUs get access right away. Sharing with AWS Organizations must first be turned on in AWS RAM. | 
| An account in your organization | 12-digit account ID | No, if sharing with AWS Organizations is turned on in AWS RAM. The share is active right away, and no invitation is sent. Otherwise, yes. | 
| An account outside your organization | 12-digit account ID | Yes. The consumer has 12 hours to accept the invitation. | 

When an account leaves your organization or the OU that you shared with, it loses access to the TD. This is standard AWS RAM behavior.

Sharing has these properties:
+ **Regional** – A TD can be shared and run only in the AWS Region where it was published. The consumer must run it in that Region. Cross-Region sharing isn't supported.
+ **Published versions only** – You can share only a published TD. Drafts can't be shared.
+ **New versions go out automatically** – When you publish a new version, consumers get it through the existing share. Runs use the latest version unless the consumer picks a specific version with `--tv`.
+ **The consumer pays** – Usage, in [agent minutes](https://aws.amazon.com/transform/pricing/), is charged to the account that starts the run, not to the owner. In consolidated billing, the usage appears under the consumer's linked account.
+ **The consumer's code stays in the consumer's account** – A shared TD runs on the consumer's repository, in the consumer's environment, with the consumer's credentials. The owner doesn't get access to the consumer's repositories or run transcripts. If the consumer chooses to contribute, the lessons extracted from the run are added to the owner's TD. For more information, see [Lessons and shared transformation definitions](custom-sharing-lessons.md).

**Trust the owner before you accept a share or run a shared TD**  
When you run a shared TD, the owner's instructions, references, and scripts run in your environment, with the tools that you allow and the permissions of your credentials. Unless the share's permission includes `transform-custom:GetTransformationPackageUrl`, as `ExecuteWithLearningsAndPackageDownload` does, you can't download the TD to review it before you run it. Running a shared TD is like running third-party code. When a run starts, the CLI shows `You are using a user-created transformation which has not been reviewed by AWS.` for every TD that isn't an AWS managed transformation, including shared TDs.  
Only accept shares from owners that you trust.
Run shared TDs on repositories and machines where that's acceptable.
Don't use `--trust-all-tools` (`-t`) with shared TDs. Use the [trust settings](custom-workflows.md#custom-trust-settings) file to allow only the tools that the TD needs.
Use least-privilege credentials for the run.

**Note**  
**For owners:** The share's permission controls what consumers can do with your TD. For example, consumers can download the TD with `atx custom def get` only if the share's permission includes `transform-custom:GetTransformationPackageUrl`, as `ExecuteWithLearningsAndPackageDownload` does. As with any content that you share, don't put secrets, credentials, or other sensitive information in a TD that you share.

## Considerations and limitations
<a name="custom-sharing-limitations"></a>
+ Sharing is Regional. Cross-Region sharing isn't supported.
+ Only published TDs can be shared.
+ A consumer can't reshare a TD.
+ A consumer can't leave an accepted share. The owner revokes it.
+ A consumer can't see a pending share's permission before accepting it.
+ Invitations to accounts outside your organization expire after 12 hours.
+ Sharing with IAM roles or users, instead of accounts, isn't supported.
+ The AWS Transform CLI manages shares only with the four AWS managed permissions. Use AWS RAM directly for customer managed permissions.
+ In an organization whose SCP denies sharing with external principals, `atx custom def share create` is denied. Use AWS RAM directly.
+ Deleting a TD doesn't remove its AWS RAM resource shares.
+ Shared TDs are available in the AWS Transform CLI. They aren't available in the AWS Transform web application in this release.
+ Lesson contribution needs an opt-in for each run, even inside an organization.
+ You can't share AWS managed transformations or their lessons.
+ There's no clone command. To adapt a TD, download it and publish it in your account.
+ The owner doesn't get reports on consumers' runs.
+ A shared TD counts toward the owner's quotas for the number and size of transformation definitions, not the consumer's. Runs of a shared TD count toward the monthly conversation request quota of the account that runs it. AWS RAM quotas, such as resource shares per account, also apply. For more information, see [Quotas for AWS Transform](transform-limits.md).

## Monitoring and audit
<a name="custom-sharing-monitoring"></a>

AWS Transform custom logs the sharing operations to AWS CloudTrail. Every call is logged in the account that makes it. For calls on a shared TD that read or change the owner's TD or lessons, the event is also delivered to the owner account.


| Event | Where it's logged | 
| --- | --- | 
| Create, update, or delete a share, or change a permission (ram:\*) | AWS CloudTrail in the owner account | 
| Accept or decline an invitation (ram:\*) | AWS CloudTrail in the consumer account | 
| Run a shared TD (ConverseStream) | AWS CloudTrail in the consumer account only. ExecuteTransformation, the access check before a run, isn't logged. | 
| Read the owner's lessons (ListKnowledgeItems, GetKnowledgeItem) | AWS CloudTrail in the consumer account and the owner account | 
| Download the TD (GetTransformationPackageUrl, GetTransformationPackage) | AWS CloudTrail in the consumer account and the owner account | 
| Contribute lessons (ContributeKnowledgeItems) | AWS CloudTrail in the consumer account and the owner account, as a write on the TD | 

Calls that are denied are also logged, with the error code `AccessDenied`.

For more information, see [Logging AWS Transform API calls using AWS CloudTrail](logging-using-cloudtrail.md).