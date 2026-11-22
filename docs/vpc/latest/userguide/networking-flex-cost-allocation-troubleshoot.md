

# Troubleshoot Networking Flexible Cost Allocation

The following topics help you troubleshoot common issues that you might encounter when you use Networking Flexible Cost Allocation (FCA).

## Usage isn't itemized in my report
<a name="networking-flex-cost-allocation-ts-not-itemized"></a>

**Problem**  
You associated a policy with a resource, but your Cost and Usage Reports show a single charge for the resource.

**Cause**  
One of the following is true.
+ The association hasn't reached its expected effective time yet. Allocation doesn't begin before that time.
+ Showback is turned off for the policy.
+ You haven't turned on the **Networking flexible cost allocation** preference, or the report you're viewing doesn't include split cost allocation data. Reports without split cost allocation data always show a single line item for the resource.
+ The traffic isn't covered by the policy. For example, the traffic goes to a virtual private gateway or crosses Regions, or a device such as a transit gateway is between the two instances in an Amazon EC2 instance policy.

**Solution**  
Check the association on the **Associations** tab of the policy details page, and check that showback is turned on for the policy. Confirm that you turned on the **Networking flexible cost allocation** preference and that your report includes split cost allocation data. For more information, see [Turning on the data in your Cost and Usage Reports](networking-flex-cost-allocation-work-with.md#networking-flex-cost-allocation-turn-on) and [Networking Flexible Cost Allocation limitations](networking-flex-cost-allocation-limitations.md).

## Some usage isn't itemized
<a name="networking-flex-cost-allocation-ts-some-not-itemized"></a>

**Problem**  
Some of the usage for a resource is itemized, but part of it remains in the shared resource line item.

**Cause**  
The resource that generated the usage for some flows can't be determined, or some flows aren't covered by the policy. That usage is billed as usual.

**Solution**  
No action is required. The itemized line items and the remaining usage add up to the total for the resource.

## Usage is labeled at a less specific level than I specified
<a name="networking-flex-cost-allocation-ts-less-specific"></a>

**Problem**  
You specified a granularity such as `ec2`, but some usage is labeled with a subnet, VPC, or peering connection.

**Cause**  
The resource that generated the usage can't be resolved at the granularity that you specified. For example, the resource isn't an Amazon EC2 instance, the traffic comes through a transit gateway, or the peer is in a different account.

**Solution**  
No action is required. Usage is itemized at the next less specific level that can be resolved.

## My CIDR labels aren't applied to some usage
<a name="networking-flex-cost-allocation-ts-cidr"></a>

**Problem**  
Some usage isn't labeled with the CIDR labels in your policy.

**Cause**  
The IP address of the traffic doesn't match any CIDR range in the policy, or the policy specifies the other direction. A policy with a `PrefixesType` of `source-prefixes` matches only the source address, and `destination-prefixes` matches only the destination address.

**Solution**  
Check the CIDR ranges and the direction in your policy. Usage that doesn't match any range is billed as usual.

## My policy changes didn't take effect
<a name="networking-flex-cost-allocation-ts-no-effect"></a>

**Problem**  
You modified a policy, but allocation uses an earlier configuration, or allocation stopped.

**Cause**  
Associations use only the latest version of a policy, and the latest version has its own expected effective time. If you create another version before the first one takes effect, the first version is skipped.

**Solution**  
Wait for the latest version to take effect. To view the versions of a policy, use the **Policy** tab on the policy details page, or use the `get-networking-flex-cost-allocation-policy-versions` command.

## I can't create, modify, or delete a policy
<a name="networking-flex-cost-allocation-ts-cant-manage"></a>

**Problem**  
Your request to create, modify, or delete a policy or association is rejected with a message from your administrator.

**Cause**  
A declarative policy applies to your account.

**Solution**  
Contact your organization administrator.