# Using shared VPC with Runtime Monitoring

GuardDuty Runtime Monitoring supports using shared Amazon Virtual Private Cloud (Amazon VPC) for your AWS accounts that belong to the same organization in AWS Organizations. You can
use shared VPC in two ways:

- **Automated agent configuration (Recommended)** – When GuardDuty automatically manages the security agent, it will also configure
  the Amazon VPC endpoint policy. This policy is based on your organization's shared VPC settings.

You must enable automated agent configuration in the shared VPC owner account and all the participating accounts who will share this VPC.

- **Manually managed agent** – When you manually manage the security agent with shared VPC,
  you must update the VPC endpoint policy to allow corresponding accounts to access shared VPC. To do this, you can use the example policy shared in the following [How it works](#how-shared-vpc-works-runtime-monitoring-auto "#how-shared-vpc-works-runtime-monitoring-auto") section.

For manual management scenarios involving participating accounts for shared VPC,
the coverage status may not be accurate. To ensure up-to-date protection and coverage status
of your resources, GuardDuty recommends enabling automated agent configuration for all the
accounts that will use shared VPC.

###### Topics

- [How it works](#how-shared-vpc-works-runtime-monitoring-auto "#how-shared-vpc-works-runtime-monitoring-auto")
- [Prerequisites for using shared
  VPC](#shared-vpc-prerequisite-runtime-monitoring "#shared-vpc-prerequisite-runtime-monitoring")

## How it works

The AWS accounts that belong to the same organization as the shared Amazon VPC owner
account can also share the same Amazon VPC endpoint. Each of the accounts using the same Amazon VPC endpoint policy is called as the **participant AWS account** of the associated shared Amazon VPC.

The following example shows the default VPC endpoint policy of the shared VPC owner
account and the participant account. The `aws:PrincipalOrgID` will show the
organization ID associated with the shared VPC resource. The use of this policy is limited to
the participant accounts present in the organization of the owner account.

###### Example shared VPC endpoint policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Action": "*",
 "Resource": "*",
 "Effect": "Allow",
 "Principal": "*"
 },
 {
 "Condition": {
 "StringNotEquals": {
 "aws:PrincipalOrgID": "`o-abcdef0123`"
 }
 },
 "Action": "*",
 "Resource": "*",
 "Effect": "Deny",
 "Principal": "*"
 }
 ]
}`

```

### With GuardDuty automatic agent configuration

When the owner account of the shared VPC enables Runtime Monitoring and automated agent
configuration for any of the resources (Amazon EKS or AWS Fargate (Amazon ECS only)), all the shared
VPCs become eligible for automatic installation of the shared Amazon VPC endpoint and the
associated security group in the shared VPC owner account. GuardDuty retrieves the organization ID
that is associated with the shared Amazon VPC.

GuardDuty creates an Amazon VPC endpoint when either the
shared VPC owner account or the participating account needs it. Examples of
needing an Amazon VPC endpoint include enabling GuardDuty, Runtime Monitoring, EKS Runtime Monitoring, or launching a new
Amazon ECS-Fargate task. When these accounts enable Runtime Monitoring and automated agent configuration
for any resource type, GuardDuty creates an Amazon VPC endpoint and sets the endpoint policy with the
same organization ID as that of the shared VPC owner account. GuardDuty adds a
`GuardDutyManaged` tag and sets it to `true` for the Amazon VPC endpoint
that GuardDuty creates. If the shared Amazon VPC owner account has not enabled Runtime Monitoring or automated
agent configuration for any of the resources, GuardDuty will not set the Amazon VPC endpoint policy.
For information about configuring Runtime Monitoring and managing the security agent automatically in
the shared VPC owner account, see [Enabling GuardDuty Runtime Monitoring](runtime-monitoring-configuration.md "runtime-monitoring-configuration.md").

### Using with manually managed agent

When you use shared VPC with manually managed agent, validate that there is no explicit `Deny` endpoint
policy that blocks any account that needs to use the shared VPC. This will prevent the security agent from sending telemetry
to GuardDuty, resulting in an `Unhealthy` coverage status. For setting up the endpoint policy, see
[Example shared VPC endpoint policy](#guardduty-runtime-monitoring-shared-vpc-endpoint-policy-example "#guardduty-runtime-monitoring-shared-vpc-endpoint-policy-example").

Runtime coverage may not be
accurate in scenarios such as missing permissions to the shared VPC. You can continuously monitor resource coverage
by following the steps
for your resource type in [Reviewing runtime coverage statistics and
troubleshooting issues](runtime-monitoring-assessing-coverage.md "runtime-monitoring-assessing-coverage.md").

To ensure continuous Runtime Monitoring protection of your compute resources,
GuardDuty recommends enabling automated agent configuration for the shared VPC owner account and all the participating accounts
for your resources.

## Prerequisites for using shared

VPC

As a part of an
initial setup, perform the following steps in the AWS account that you want to be the owner
of the shared VPC:

1. **Creating an organization** – Create an
   organization by following the steps in [Creating and managing an
   organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the _AWS Organizations User Guide_.

For information about adding or removing member accounts, see [Managing AWS accounts in your organization](../../../organizations/latest/userguide/orgs_manage_accounts.md "../../../organizations/latest/userguide/orgs_manage_accounts.md"). 2. **Creating a shared VPC resource** – You can
create a shared VPC resource from the owner account. For more information, see [Share your VPC subnets with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the
_Amazon VPC User Guide_.

### Prerequisites specific to

GuardDuty Runtime Monitoring

The following list provides the prerequisites that are specific to GuardDuty:

- The owner account of the shared VPC and the participating account can be from
  different organizations in GuardDuty. However, they must belong to the same organization in
  AWS Organizations. This is required for GuardDuty to create an Amazon VPC endpoint and a security group
  for the shared VPC. For information about how shared VPCs work, see [Share your VPC with
  other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in _Amazon VPC User Guide_.
- Enable Runtime Monitoring or EKS Runtime Monitoring, and GuardDuty automated agent configuration for any
  resource in the shared VPC owner account and the participant account. For more
  information, see [Enabling
  Runtime Monitoring](runtime-monitoring-configuration.md "runtime-monitoring-configuration.md").

If you have already completed these configurations, continue with the next
step.

- When working with either an Amazon EKS or an Amazon ECS (AWS Fargate only) task, make sure
  to choose the shared VPC resource associated with the owner account and select its
  subnets.
