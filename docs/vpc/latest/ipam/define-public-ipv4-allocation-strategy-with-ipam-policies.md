

# Define public IPv4 allocation strategy with IPAM policies
<a name="define-public-ipv4-allocation-strategy-with-ipam-policies"></a>

Allocation rules in an [IPAM policy](https://docs.aws.amazon.com/vpc/latest/ipam/ipam-policies.html) define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to the IPAM pools that the service uses to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If an IPAM pool runs out of addresses, the service falls back to Amazon-provided IP addresses. If you [bring your own IP (BYOIP)](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam.html), this helps reduce your AWS public IPv4 costs.

## When to use allocation rules
<a name="when-to-use-ipam-policies"></a>

Use allocation rules to:
+ Reduce public IPv4 costs by using BYOIP addresses
+ Centrally control which IP pools your AWS resources use
+ Ensure consistent IP allocation across your organization

## How it works
<a name="how-it-works"></a>

The following occurs when you create an AWS resource that needs a public IP address in an account with IPAM policies enforced:
+ IPAM checks your policy rules in order.
+ If a rule matches the resource type, IPAM allocates an IP from the specified pool.
+ If the pool is empty and overflow is enabled, Amazon provides an IP address.
+ If no rules match, the default behavior applies.

## Supported services and resources
<a name="supported-services-and-resources"></a>

You can create IPAM policies to define how public IPv4 addresses from IPAM pools are allocated to the following AWS services and resources:
+ Elastic IP addresses (EIPs)
+ Application Load Balancers (ALBs)
+ Amazon Relational Database Service (RDS)
+ Regional NAT gateways

**Important**  
If you choose a specific IPAM pool or EIP allocation ID when creating an AWS resource, that will override the IPAM policy.

## Prerequisites
<a name="prerequisites"></a>
+ An IPAM policy. For the IPAM requirements and how to create a policy, see [IPAM policies](ipam-policies.md).
+ A [public IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-top-ipam.html) with IPv4 addresses
+ If you enable the policy for accounts other than the pool owner, you must share the pool with those accounts by using AWS Resource Access Manager (AWS RAM). For more information, see [Share an IPAM pool using AWS RAM](share-pool-ipam.md).

## Terminology
<a name="terminology"></a>

**Allocation rules**  
Optional configurations within an IPAM policy that map AWS resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.

## Step 1: Add allocation rules
<a name="add-allocation-rules"></a>

After you create the policy (see [Create an IPAM policy](ipam-policies.md#ipam-policies-create)), add allocation rules that define how IP addresses are allocated:

**Using the AWS Console:**  
Follow these steps to add allocation rules by using the AWS Console:

1. In the left navigation pane, choose **Policies**.

1. Choose the policy that you created.

1. In your policy details page, choose the **Allocation rules** tab.

1. Choose **Create allocation rules**.

1. Configure the **Service configuration**:
   + **Locale**: Choose the AWS Region (us-east-1) or Local Zone where you want this policy to apply.
   + **Resource type**: Select the AWS service or resource type for this policy (Elastic IP addresses, RDS database instances, Application Load Balancers, or NAT gateways in regional availability mode).

1. Configure **Rules configuration**:
   + **IPAM pool**: Select the IPAM pool that will provide IP addresses.
   + Review the pool details (locale, public IP source, space available, and CIDR ranges available).

1. (Optional) Choose **Add new rule** to create additional rules.

1. Choose **Create allocation rule**.

**Using the AWS CLI:**  
Use the [modify-ipam-policy-allocation-rules](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-ipam-policy-allocation-rules.html) command.

## Step 2: Share the pools with target accounts
<a name="share-pools-with-target-accounts"></a>

An allocation rule only specifies which pool to use. To get an address from the pool, the target account must own the pool, or you must share the pool with it by using AWS RAM. If the target account can't access the pool, the request still succeeds, but the resource gets an Amazon-provided IP address.

You can skip this step if you enable the policy only for the account that owns the pools in its allocation rules.

If you enable the policy for an organization, an organizational unit (OU), or member accounts, share each pool in the allocation rules with those targets. For more information, see [Share an IPAM pool using AWS RAM](share-pool-ipam.md).

**Note**  
After you share a pool, wait several minutes before you test the policy. Until the share takes effect, resources might get Amazon-provided IP addresses. If you add a pool to an allocation rule later, share that pool too.

## Step 3: Enable the policy
<a name="enable-the-policy"></a>

Specify which accounts should use this policy. See [Enable an IPAM policy](ipam-policies.md#ipam-policies-enable). If an account is in the scope of more than one enabled policy, see [Which policy applies to an account](ipam-policies.md#ipam-policies-precedence).

## Step 4: Test your policy
<a name="test-your-policy"></a>

 Create a new resource of the type you configured (like an EIP) in one of the target accounts. The resource will automatically use an IP address from your IPAM pool.

**Important**  
If you choose a specific IPAM pool or EIP allocation ID when creating an AWS resource, that will override the IPAM policy.

## Step 5: Monitor usage
<a name="monitor-usage"></a>

Check your [IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-usage-ipam.html) in the console to see IP addresses being allocated to your resources.