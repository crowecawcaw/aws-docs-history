# AWS Transform Connectors

AWS Transform connectors enable you to securely access resources across account boundaries for migration and modernization workflows. This enables you to access and manage resources across account boundaries
while maintaining security controls and permissions. A connector represents a connection between your AWS Transform-enabled source account and external resources in AWS target accounts or in third-party systems.

Connectors require requests for access from the _source
connector_, and approval from the owner of the target account. You make this
request when you are setting up a source connector. Similarly, you may receive requests to
approve _destination connectors_ to allow other accounts access to your
account.

- **Connector creation:** Create connectors in your AWS Transform-enabled source account, specifying the target account and required permissions
- **Permission Setup:** AWS Transform requires specific
  IAM roles and permissions in the destination account to perform migration actions,
  including:
  - Managing migration data with AWS KMS
  - Making cross-region API calls
  - Installing replication agents on VMware servers
  - Creating network infrastructure (VPCs, subnets, routing)
  - Launching Amazon EC2 instances and deploying CloudFormation stacks
  - Executing migration workflows through Migration Hub

- **Approval Process:** You must approve
  destination connector requests before AWS Transform can access your resources.
- **Active Connection:** Once you approve a
  connector, it enables AWS Transform jobs to securely access and manage resources in the
  target account.

## Managing connectors

On the Connectors page you can see the:

- **Source Connectors Tab:** Lists all
  connectors you've created to connect to other accounts, showing target accounts
  and connector status
- **Destination Connectors Tab:** Shows
  incoming connector requests from other accounts wanting to access your
  resources, and requiring your approval or rejection

AWS Transform requires confirmation for critical actions such as approving, rejecting, or deleting connectors, to avoid accidental changes that could disrupt your active migration workflows.

###### To create a connector

1. Navigate to the **Source Connectors** tab.
2. Specify the target account and resource type.
3. Configure required permissions and access scope.

###### To set up permissions

1. Choose to create a new IAM role with required permissions, or
2. Select an existing role you previously created for connectors.
3. Ensure the role has all necessary permissions for AWS Transform operations.

###### To manage incoming requests

1. Review connector requests in the **Destination Connectors
   tab**.
2. Approve legitimate requests to enable cross-account access.
3. Reject unauthorized or unnecessary connection attempts.

###### To manage your connectors

1. Monitor your active connectors for security and compliance.
2. Delete connectors when you no longer need them. Note that this will cause
   running jobs using the connector to fail.
3. Update permissions as your requirements change.
