# TELCOOPS05-BP02 Implement a structured sequence of interface

assignment based on the persistent or ephemeral nature of the interfaces

The order of operations is important as the creation and termination of instances often
creates and destroys interfaces. This is a useful property for ephemeral interfaces. However, it
can lead to problems where other resources are dependent on the persistence of an interface and
IP addressed across network domains. Persistent interfaces should be created prior to the
creation of the EC2 instance with their properties assigned through IaC. Upon EC2 instance
creation ephemeral interfaces and addresses can be created at the initialization of the EC2
instance while persistent interfaces which were previously created can be added to the EC2
instance. Thus, the termination of the instance will remove the ephemeral interfaces while
preserving the persistent interfaces. The persistent interfaces retain their properties and can
be re-assigned to a new EC2 instance without impacting adjacent functions.

**Desired outcome:**

- Clear interface lifecycle management.
- Predictable interface behavior.
- Proper resource dependency handling.
- Efficient interface assignment.
- Minimized service disruption.
- Reliable state management.

**Common anti-patterns:**

- Random interface assignment.
- No lifecycle consideration.
- Missing dependency mapping.
- Improper sequence handling.
- Poor state management.
- Undefined persistence rules.
- Inconsistent cleanup.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Create a structured approach to interface assignment that clearly distinguishes between
persistent and ephemeral interfaces throughout their lifecycle. Develop automated workflows
that handle the creation, attachment, and cleanup of interfaces in the correct sequence,
making sure that persistent interfaces are properly preserved during instance replacements or
updates. Implement state tracking mechanisms that maintain visibility into interface status
and dependencies, enabling proper handling of complex networking scenarios. Establish robust
error handling and rollback procedures to maintain system integrity during interface
operations, while verifying proper cleanup of ephemeral resources.

### Implementation steps

- Use AWS tags for interface type identification and AWS Resource Groups for interface
  categorization.
- Deploy AWS Step Functions for orchestrating interface assignment workflow and AWS Lambda for
  execution logic.
- Implement AWS CloudFormation for defining interface dependencies and AWS Systems Manager Automation for
  sequence execution.
- Use Amazon DynamoDB for interface state tracking and Amazon EventBridge for state change management.
- Configure AWS Systems Manager OpsCenter for interface-related operations and AWS CloudTrail for
  interface activity tracking.

## Resources

**Key AWS services:**

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
