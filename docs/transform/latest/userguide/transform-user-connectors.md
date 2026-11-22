

# AWS Transform Connectors

AWS Transform connectors enable you to securely access resources across account boundaries for migration and modernization workflows. This enables you to access and manage resources across account boundaries while maintaining security controls and permissions. A connector represents a connection between your AWS Transform-enabled source account and external resources in AWS target accounts or in third-party systems.

Connectors require requests for access from the *source connector*, and approval from the owner of the target account. You make this request when you are setting up a source connector. Similarly, you may receive requests to approve *destination connectors* to allow other accounts access to your account.
+ **Connector creation:** Create connectors in your AWS Transform-enabled source account, specifying the target account and required permissions
+ **Permission Setup:** AWS Transform requires specific IAM roles and permissions in the destination account to perform migration actions, including:
  + Managing migration data with AWS KMS
  + Making cross-region API calls
  + Installing replication agents on VMware servers
  + Creating network infrastructure (VPCs, subnets, routing)
  + Launching Amazon EC2 instances and deploying CloudFormation stacks
  + Executing migration workflows through Migration Hub
+ **Approval Process:** You must approve destination connector requests before AWS Transform can access your resources.
+ **Active Connection:** Once you approve a connector, it enables AWS Transform jobs to securely access and manage resources in the target account.

## User traceability for agentic operations
<a name="transform-connectors-user-traceability"></a>

By default, AWS CloudTrail records agent actions on your AWS resources under the AWS Transform service identity. User traceability attributes those actions to the specific AWS IAM Identity Center user who initiated or interacted with the job, enabling security auditing and incident investigation at the individual-user level.

**Note**  
User traceability is supported for IAM Identity Center (IDC) users only.

To enable user traceability, enable **Background session** in your AWS Transform profile settings. When enabled, AWS Transform automatically creates an IAM Identity Center [background session](https://docs.aws.amazon.com/singlesignon/latest/userguide/user-background-sessions.html) when you interact with a job and uses it to produce identity-enhanced IAM role sessions for connector operations. These sessions embed your user identity in downstream AWS service calls and AWS CloudTrail events. When background sessions are disabled, AWS Transform falls back to standard assumed-role sessions without user identity context.

New connectors are automatically configured to support user traceability. For existing connectors, you must manually add `sts:SetContext` to the connector role's trust policy:

```JSON
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": ["transform.amazonaws.com"] },
      "Action": ["sts:AssumeRole", "sts:SetContext"],
      "Condition": {
        "StringEquals": { "aws:SourceAccount": "{{your-account-id}}" }
      }
    }
  ]
}
```

You can view and revoke your active background sessions from the **Background sessions** tab on the job page. Revoking a session immediately invalidates it and any connector sessions derived from it.

For more information, see [Trusted identity propagation overview](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html) in the *AWS IAM Identity Center User Guide*.

## Managing connectors
<a name="transform-connectors-manage"></a>

On the Connectors page you can see the:
+ **Source Connectors Tab:** Lists all connectors you've created to connect to other accounts, showing target accounts and connector status
+ **Destination Connectors Tab:** Shows incoming connector requests from other accounts wanting to access your resources, and requiring your approval or rejection

AWS Transform requires confirmation for critical actions such as approving, rejecting, or deleting connectors, to avoid accidental changes that could disrupt your active migration workflows.

**To create a connector**

1. Navigate to the **Source Connectors** tab.

1. Specify the target account and resource type.

1. Configure required permissions and access scope.

**To set up permissions**

1. Choose to create a new IAM role with required permissions, or

1. Select an existing role you previously created for connectors.

1. Ensure the role has all necessary permissions for AWS Transform operations.

**To manage incoming requests**

1. Review connector requests in the **Destination Connectors tab**.

1. Approve legitimate requests to enable cross-account access.

1. Reject unauthorized or unnecessary connection attempts.

**To manage your connectors**

1. Monitor your active connectors for security and compliance.

1. Delete connectors when you no longer need them. Note that this will cause running jobs using the connector to fail.

1. Update permissions as your requirements change.

## Connect AWS Transform to other AWS accounts
<a name="transform-connectors-cross-account"></a>

AWS Transform uses connectors to securely access resources across account boundaries. A connector links your AWS Transform-enabled account (the source account) to a resource in another AWS account (the target account). The target account can be the same account or a different one.

Connectors use a request-and-approve model. In the source account, you request the connector. In the target account, an administrator approves it and chooses the IAM role that defines what AWS Transform can do.

### Choose a connector policy type
<a name="transform-connectors-cross-account-policy-type"></a>

When you create a connector, you choose how its permissions are defined:
+ **Managed Policy connector**: uses an AWS managed policy for the target resource, so you don't write permissions yourself.
+ **Customer Policy connector**: uses a policy you author and control.

Unless a feature's documentation says otherwise, use the Managed Policy connector when an AWS managed policy exists for your target service. A feature might specify one. For example, the AWS Partner Central connector uses the Managed Policy option with [AWSPartnerCentralFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.html).

### Prerequisites
<a name="transform-connectors-cross-account-prerequisites"></a>

Before you create a cross-account connector, make sure that the following is true:
+ AWS Transform is set up in the source account.
+ You have the 12-digit ID of the target account.
+ You can sign in to the target account, or have an administrator who can, with permission to create IAM roles and approve connectors.
+ The target service is available in the target account (for example, Partner Central).

### Choose your scenario
<a name="transform-connectors-cross-account-scenario"></a>

Use the following table to choose the scenario that matches your target resource.


| Scenario | When to use | Extra step | 
| --- | --- | --- | 
| A. Same account | The target resource is in the same account as AWS Transform | None | 
| B. Different account | The target resource is in another account | Add the target to the trusted-access list first | 

### Scenario A: Target resource in the same account
<a name="transform-connectors-cross-account-scenario-a"></a>

**Step 1: Create the connector (source account)**

1. In the AWS Transform web application, open **Connectors**.

1. On the **Source Connectors** tab, create a new connector. Specify the target account (this account) and the connector type.

1. When prompted, choose **Managed Policy** or **Customer Policy**.

1. Confirm the target account.

1. The connector is created with the status **Pending approval**.

**Step 2: Approve the connector (target account)**

1. In AWS Transform, open **Connectors** and choose the **Destination Connectors** tab. The new connector shows **Pending approval**.

1. Choose to create a new IAM role, or select an existing role. For a managed-policy connector, the role carries the managed policy for that service.

1. Choose **Save and Approve**.

1. The connector status changes to **Approved**.

**Note**  
For the generic approval flow, including sharing the verification link with an administrator, see [AWS Transform Connectors](transform-user-connectors.md).

### Scenario B: Target resource in a different account
<a name="transform-connectors-cross-account-scenario-b"></a>

A cross-account connector requires the source account to trust the target account first. At a high level, there are two parts: trust the target account in the source account, then approve the connector in the target account. This step is not needed if both AWS accounts are part of the same AWS Organization.

**Step 1: Add the target account to the trusted-access list (source account)**

1. In the AWS Transform console, go to **Service management**, **Settings**, **Cross-account access**.

1. Add the target account's 12-digit ID to the trusted-access list.

1. Confirm the account appears in the list. The **Cross-account access** count updates (for example, 1).

**Note**  
If the target account is in a different AWS Organization, it must be on this list before you can create the connector.

**Important**  
If you remove an account from the trusted-access list later, the connectors that use it stop working.

**Step 2: Create the connector (source account)**

1. In the AWS Transform web application, open **Connectors**.

1. On the **Source Connectors** tab, create a new connector. Specify the target account's ID and the connector type.

1. Choose **Managed Policy** or **Customer Policy**.

1. The connector is created with the status **Pending approval** in the target account.

**Step 3: Approve the connector (target account)**

1. Sign in to the target account (for example, by federating into it) and open AWS Transform.

1. Go to **Connectors**, **Destination Connectors**. The connector shows **Pending approval**.

1. Create a new IAM role or select an existing one, then choose **Save and Approve**.

**Step 4: Verify**
+ Confirm the connector shows **Approved** in the target account. In the source account, its status should show as active.

### After you connect
<a name="transform-connectors-cross-account-after"></a>

After the connector is approved, the following applies:
+ Your AWS Transform jobs and workflows can now use the connector to access the target account within the permissions of the approved role.
+ Deleting a connector causes running jobs that use it to fail.
+ Review your connectors regularly and remove ones you no longer need.

### Related documentation
<a name="transform-connectors-cross-account-related"></a>
+ [AWS Transform Connectors](transform-user-connectors.md)
+ [Setting up AWS Transform](transform-setup.md)