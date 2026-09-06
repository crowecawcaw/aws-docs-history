

# AWS Transform Connectors
<a name="transform-user-connectors"></a>

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

```
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