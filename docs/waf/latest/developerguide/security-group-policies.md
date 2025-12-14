**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using security group policies in Firewall Manager to manage Amazon VPC security groups

This page explains how to use AWS Firewall Manager security group policies to manage Amazon Virtual Private Cloud security groups for
your organization in AWS Organizations. You can apply centrally controlled security group
policies to your entire organization or to a select subset of your accounts and
resources. You can also monitor and manage the security group policies that are in use
in your organization, with auditing and usage security group policies.

Firewall Manager continuously maintains your policies and applies them to accounts and resources as
they are added or updated across your organization. For information about AWS Organizations, see
[AWS Organizations User Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md").

For information about Amazon Virtual Private Cloud security groups, see [Security Groups for Your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in
the _Amazon VPC User Guide_.

You can use Firewall Manager security group policies to do the following across your AWS
organization:

- Apply common security groups to specified accounts and resources.
- Audit security group rules, to locate and remediate noncompliant rules.
- Audit usage of security groups, to clean up unused and redundant security
  groups.
  This section covers how Firewall Manager security groups policies work and provides guidance for using
  them. For procedures to create security group policies, see [Creating an AWS Firewall Manager policy](create-policy.md "create-policy.md").

## Best practices for security group

policies

This section lists recommendations for managing security groups using AWS Firewall Manager.

###### Exclude the Firewall Manager administrator account

When you set the policy scope, exclude the Firewall Manager administrator account. When
you create a usage audit security group policy through the console, this is the
default option.

###### Start with automatic remediation disabled

For content or usage audit security group policies, start with automatic
remediation disabled. Review the policy details information to determine the
effects that automatic remediation would have. When you are satisfied that the
changes are what you want, edit the policy to enable automatic
remediation.

###### Avoid conflicts if you also use outside sources to manage security groups

If you use a tool or service other than Firewall Manager to manage security groups, take care to
avoid conflicts between your settings in Firewall Manager and the settings in your outside
source. If you use automatic remediation and your settings conflict, you can
create a cycle of conflicting remediation that consumes resources on both sides.

For example, say you configure another service to maintain a security group for a set of
AWS resources, and you configure a Firewall Manager policy to maintain a different security
group for some or all of the same of resources. If you configure either side to
disallow any other security group to be associated with the in-scope resources, that
side will remove the security group association that's maintained by the other side.
If both sides are configured in this way, you can end up with a cycle of conflicting
disassociations and associations.

Additionally, say that you create a Firewall Manager audit policy to enforce a security group
configuration that conflicts with the security group configuration from the other
service. Remediation applied by the Firewall Manager audit policy can update or delete that
security group, putting it out of compliance for the other service. If the other
service is configured to monitor and automatically remediate any problems it finds,
it will recreate or update the security group, putting it again out of compliance
with the Firewall Manager audit policy. If the Firewall Manager audit policy is configured with automatic
remediation, it will again update or delete the outside security group, and so
on.

To avoid conflicts like these, create configurations that are mutually exclusive,
between Firewall Manager and any outside sources.

You can use tagging to exclude outside security groups from automatic remediation by your
Firewall Manager policies. To do this, add one or more tags to the security groups or other
resources that are managed by the outside source. Then, when you define the Firewall Manager
policy scope, in your resources specification, exclude resources that have the tag
or tags that you've added.

Similarly, in your outside tool or service, exclude the security groups that Firewall Manager manages
from any management or auditing activities. Either don't import the Firewall Manager resources
or use Firewall Manager-specific tagging to exclude them from outside management.

###### Best practices for usage audit security group policies

Follow these guidelines when you use usage audit security group policies.

- Avoid making multiple changes to the association status of a security
  group in a short amount of time, such as within a 15-minute window. Doing so
  can cause Firewall Manager to miss some or all of the corresponding events. For
  example, don't quickly associate and disassociate a security group with an
  elastic network interface.

## Security group policy caveats and

limitations

This section lists the caveats and limitations for using Firewall Manager security group policies.

###### Resource type: Amazon EC2 instance

This section lists the caveats and limitations for protecting Amazon EC2 instances with Firewall Manager security group policies.

- With security groups that protect Amazon EC2 elastic network interfaces (ENIs), changes to a security group aren't immediately visible to Firewall Manager. Firewall Manager usually detects changes within several hours, but detection can be delayed as much as six hours.
- Firewall Manager doesn't support security groups for Amazon EC2 ENIs that were created by the Amazon Relational Database Service.
- Firewall Manager doesn't support updating security groups for Amazon EC2 ENIs that were created using the
  Fargate service type. You can, however, update security groups
  for Amazon ECS ENIs with the Amazon EC2 service type.
- Firewall Manager doesn't support updating security groups for requester-managed Amazon EC2 ENIs,
  because Firewall Manager doesn't have permission to modify them.
- For common security group policies, these caveats concern the interaction between
  the number of elastic network interfaces (ENIs) that are attached to the EC2 instance
  and the policy option that specifies whether to remediate only EC2 instances with no added
  attachments or to remediate all instances. Every EC2 instance has a default primary ENI, and you can attach
  more ENIs. In the API, the policy option setting for this choice is `ApplyToAllEC2InstanceENIs`.

If an in-scope EC2 instance has additional ENIs attached and the policy is configured to include only EC2 instances with just the primary ENI, then Firewall Manager won't attempt any remediation for the EC2 instance. Additionally, If the instance goes out of policy scope, Firewall Manager doesn't attempt to disassociate any security group associations that it might have established for the instance.

For the following edge cases, during resource cleanup, Firewall Manager can leave replicated security group associations intact, regardless of the policy's resource cleanup specifications:

    + When an instance with additional ENIs was previously remediated by a policy that was configured to include all EC2 instances, and then either the instance went out of policy scope or the policy setting was changed to include only instances without additional ENIs.
    + When an instance with no additional ENIs was remediated by an policy that was configured to include only instances with no additional ENIs, then another ENI was attached to the instance, and then the instance went out of policy scope.

###### Other caveats and limitations

The following are miscellaneous caveats and limitations for Firewall Manager security group policies.

- Firewall Manager security group policies do not support security groups shared through AWS RAM.
- Updating Amazon ECS ENIs is possible only for Amazon ECS services that use the
  rolling update (Amazon ECS) deployment controller. For other Amazon ECS deployment
  controllers such as CODE_DEPLOY or external controllers, Firewall Manager currently can't
  update the ENIs.
- Firewall Manager doesn't support updating security groups in ENIs for Network Load Balancers.
- In common security group policies, if a shared VPC is later unshared with an account Firewall Manager won't delete the replica security groups in the account.
- With usage audit security group policies, if you create multiple policies
  with a custom delay time setting that all have the same scope, the first
  policy with compliance findings will be the policy that reports the
  findings.

## Security group policy use cases

You can use AWS Firewall Manager common security group policies to automate the host firewall
configuration for communication between Amazon VPC instances. This section lists standard
Amazon VPC architectures and describes how to secure each using Firewall Manager common security
group policies. These security group policies can help you apply a unified set of
rules to select resources in different accounts and avoid per-account configurations
in Amazon Elastic Compute Cloud and Amazon VPC.

With Firewall Manager common security group policies, you can tag just the EC2 elastic network
interfaces that you need for communication with instances in another Amazon VPC. The
other instances in the same Amazon VPC are then more secure and isolated.

###### Use case: Monitoring and controlling requests to Application Load Balancers and Classic Load Balancers

You can use a Firewall Manager common security group policy to define which requests your in-scope load balancers should serve.
You can configure this through the Firewall Manager console.
Only requests that comply with the security group's inbound rules can reach your load balancers,
and the load balancers will only distribute requests that meet the outbound rules.

###### Use case: Internet-accessible, public Amazon VPC

You can use a Firewall Manager common security group policy to secure a public Amazon VPC, for example, to
allow only inbound port 443. This is the same as only allowing inbound HTTPS traffic
for a public VPC. You can tag public resources within the VPC (for example, as
"PublicVPC"), and then set the Firewall Manager policy scope to only resources with that tag.
Firewall Manager automatically applies the policy to those resources.

###### Use case: Public and Private Amazon VPC instances

You can use the same common security group policy for public resources as recommended in
the prior use case for internet-accessible, public Amazon VPC instances. You can use a second common
security group policy to limit communication between the public resources and the
private ones. Tag the resources in the public and private Amazon VPC instances with
something like "PublicPrivate" to apply the second policy to them. You can use a
third policy to define the allowed communication between the private resources and
other corporation or private Amazon VPC instances. For this policy, you can use another
identifying tag on the private resources.

###### Use case: Hub and spoke Amazon VPC instances

You can use a common security group policy to define communications between
the hub Amazon VPC instance and spoke Amazon VPC instances. You can use a second policy to
define communication from each spoke Amazon VPC instance to the hub Amazon VPC instance.

###### Use case: Default network interface for Amazon EC2 instances

You can use a common security group policy to allow only standard
communications, for example internal SSH and patch/OS update services, and to
disallow other insecure communication.

###### Use case: Identify resources with open permissions

You can use an audit security group policy to identify all resources within your
organization that have permission to communicate with public IP addresses or that
have IP addresses that belong to third-party vendors.
