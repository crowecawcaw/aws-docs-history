# Best practices while using the RFDK

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

## Organizing your stacks - Multi-tiered architecture

Use the lifecycle of your AWS Resources to help you decide what resources should go in each stack. By grouping your resources with common life cycles, you will
be able to modify your farm to take down any components that are not currently in use.

We recommend that you use a multi-tiered architecture for your RFDK apps. A multi-tiered architecture organizes stacks into horizontal tiers that build on
top of one another, with each tier having a dependency on the tier directly below it. You can have one or more stacks in each tier, but your stacks should have
AWS resources with similar lifecycles and ownership within each tier.

### Benefits

Cost

With each tier separated into its own AWS CloudFormation stacks, any tiers that are not actively required can be destroyed. For example you could tear down your Workers
separately from the remainder of your farm.

Ease of modification

Each tier can be modified independently of each other. Making a change in any single tier will not affect any tiers below it. This allows easy
iteration when developing and expanding your render farm.

Deployment Velocity

You are able to reduce the total deployment time when deploying any individual tier by keeping each tier separate. This will reduce the amount of
time it takes while developing your RFDK render farm since you are able to deploy each tier of the farm independently.

### Example

Consider a Deadline render farm that is made up of the following components:

- A VPC
- A Render Queue
- A Database for the Render Queue
- 1 or more network filesystems
- 1 or more Worker Fleets

This farm can be divided into 4 tiers, each with their own lifecycle:

Network Tier

This Tier would be made up of all resources that are required for networking. In this example that would be the VPC. You could also expand the tier to
include VPC Peering or VPN connectivity and the definition VPC Interface Endpoints.

Storage Tier

This Tier would consist of all long term storage that would be beneficial to keep between deployments. In this example that would include the Database
and all of the filesystems.

Service Tier

This Tier would consist of all components of the business logic of the render farm. In this example this includes the Render Queue. It could also include
additional components such as the Usage Based Licensing resources. This tier being deployed is required to be able to connect to your render farm and submit jobs.

Compute Tier

This tier would consist of all of the Worker Fleets or any other form of burst compute. This tier will be the most volatile since it will often change based
on your current workload.

## Managing resources

When managing the resources of your render farm it is useful to think of your resources as Cattle, not pets.

In an on-premise render farm, all resources have to be provisioned manually and have large up front investments. Due to this servers were treated as pets - each was unique
and had its own needs.

Meanwhile all of the resources of a cloud-based render farm are ephemeral, and each component can be swapped out on a whim. This means that you can modify your existing resources
whenever necessary, including changing the type or number of instances to suit your immediate need.

For a given render farm, the only components that should not be torn down at will are the networking, database, and file systems (the Networking and Storage Tiers). You will lose
all of your data, except for backups, when those resources are destroyed.

## Developing on an EC2 Instance

We recommend developing your RFDK applications on a Linux Amazon Elastic Compute Cloud (EC2) instance.
There are multiple advantages of developing on an EC2 instance, including:

- ✓ **Configurable Performance** - EC2 provides a range of instance types to chose from to balance your performance needs and costs. We recommend using a minimum instance type of `t3.small` for RFDK development.
- ✓ **On-demand** - You can start and stop your EC2 instance as needed. You only pay for what you use.
- ✓ **Reliability** - EC2 commits to a SLA of 99.99% availability for each Amazon EC2 region.

[AWS Cloud9](../../../cloud9/latest/user-guide/welcome.md "../../../cloud9/latest/user-guide/welcome.md") is an integrated development environment (IDE) that runs in your browser.
It provides a streamlined experience for developing CDK applications on an EC2 instance.

The following are the major benefits of using AWS Cloud9 for RFDK development:

- An AWS Cloud9 EC2 Environment can be configured to automatically stop the EC2 instance when the IDE is not in use to save costs.
- When using the AWS Cloud9 IDE, IAM permissions are inherited from your AWS Console session. This avoids the need to persist AWS credentials on the instance.

We provide guided instructions for setting up an [Example development environment using Cloud9 and CodeCommit](example-dev-env.md "example-dev-env.md").

## Source control

As with developing any software, CDK applications can benefit from the use of source control.
Source control (or version control) is the practice of tracking and managing changes to code.

Code management systems make it easier to accomplish the following tasks:

- Track changes to your code
- Review revision history
- Revert to previous versions of your source code
- Collaborate as a team to develop your CDK application
- Isolate your work until it is ready
- Trouble-shoot issues by identifying who made changes and what the changes were

We highly recommend that you use of source control when developing CDK applications.
Ideally, the code should be pushed to a central source control repository that is highly-available, secure, and maintains redundant physically-distributed copies of the repository data.

[AWS CodeCommit](https://aws.amazon.com/codecommit/ "https://aws.amazon.com/codecommit/") is a fully managed service that hosts private [git](https://git-scm.com/ "https://git-scm.com/") repositories.
It is designed to be highly-available, secure, and scalable.
We provide guided instructions for setting up an [Example development environment using Cloud9 and CodeCommit](example-dev-env.md "example-dev-env.md") that can be used.

## Additional readings

In addition to the above best practices it is recommended that you take a moment to read the following additional material about the components of the RFDK:

- [AWS Fundamentals](https://aws.amazon.com/getting-started/fundamentals-core-concepts/ "https://aws.amazon.com/getting-started/fundamentals-core-concepts/")
- [Cloud Formation - Best Practices](../../../AWSCloudFormation/latest/UserGuide/best-practices.md "../../../AWSCloudFormation/latest/UserGuide/best-practices.md")
- [Deadline - Render Farm Considerations](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/considerations.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/considerations.html")
