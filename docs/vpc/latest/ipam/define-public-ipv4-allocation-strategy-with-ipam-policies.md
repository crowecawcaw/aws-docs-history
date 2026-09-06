

# Define public IPv4 allocation strategy with IPAM policies
<a name="define-public-ipv4-allocation-strategy-with-ipam-policies"></a>

An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations. If you [bring your own IP (BYOIP)](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam.html), this helps reduce your AWS public IPv4 costs.

**When to use IPAM policies**

Use IPAM policies to:
+ Reduce public IPv4 costs by using BYOIP addresses
+ Centrally control which IP pools your AWS resources use
+ Ensure consistent IP allocation across your organization

**How it works**

When you create an AWS resource that needs a public IP address in an account with IPAM policies enforced:
+ IPAM checks your policy rules in order.
+ If a rule matches the resource type, IPAM allocates an IP from the specified pool.
+ If the pool is empty and overflow is enabled, Amazon provides an IP address.
+ If no rules match, the default behavior applies.

**Supported services and resources**

You can create IPAM policies to define how public IPv4 addresses from IPAM pools are allocated to the following AWS services and resources:
+ Elastic IP addresses (EIPs)
+ Application Load Balancers (ALBs)
+ Amazon Relational Database Service (RDS)
+ Regional NAT gateways

**Important**  
If you choose a specific IPAM pool or EIP allocation ID when creating an AWS resource, that will override the IPAM policy.

**Prerequisites**
+ An [IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html) in the delegated administrator account with [advanced tier](https://docs.aws.amazon.com/vpc/latest/ipam/mod-ipam-tier.html) enabled
+ A [public IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-top-ipam.html) with IPv4 addresses
+ [IAM permissions](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam.html) for IPAM and EC2 operations

**Terminology**

**IPAM policy**  
An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations. A policy can be applied to an individual AWS account or an entity within AWS Organizations.

**Allocation rules**  
Optional configurations within an IPAM policy that map AWS resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.

**Target**  
An individual AWS account or an entity within an AWS Organization to which an IPAM policy can be applied.

**Step 1: Create an IPAM policy**

**Using the AWS Console:**  
Follow these steps to create an IPAM policy using the AWS Console:

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the left navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. Enter a **Name** for your policy (optional).

1. Select the **IPAM** to associate with this policy.

1. (Optional) Add tags.

1. Choose **Create policy**.

**Using the AWS CLI:**  
Use the [create-ipam-policy](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-ipam-policy.html) command.

**Step 2: Add allocation rules**

After creating the policy, you need to add allocation rules that define how IP addresses are allocated:

**Using the AWS Console:**  
Follow these steps to add allocation rules using the AWS Console:

1. In the left navigation pane, choose **Policies**.

1. Choose the policy you created in the previous step.

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

**Step 3: Enable the policy**

Specify which accounts should use this policy.

**Using the AWS Console:**  
Follow these steps to enable the policy using the AWS Console:

1. In your policy details page, choose the **Targets** tab.

1. Choose **Manage policy targets**.

1. Do one of the following:
   + For single account usage (IPAM not integrated with AWS Organizations), choose **Enable for your account**.
   + For IPAM integrated with AWS Organizations (when you're the delegated admin):
     + In the **Organizational structure** section, select the accounts or organizational units where you want to apply this policy.
     + Check the **Enabled** checkbox for each target.
     + Choose **Save Changes**.
     + **Important**: Enabling this policy will replace any active IPAM policies on the selected accounts or organizational units.

**Using the AWS CLI:**  
Use the [enable-ipam-policy](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-ipam-policy.html) command based on your setup:

For single account usage (IPAM not integrated with AWS Organizations):

```
aws ec2 enable-ipam-policy \
    --ipam-policy-id ipam-policy-12345678
```

For IPAM integrated with AWS Organizations (when you're the delegated admin), set a policy to target an account in the AWS Organization:

```
aws ec2 enable-ipam-policy \
    --ipam-policy-id ipam-policy-12345678 \
    --organization-target-id 123456789012
```

For IPAM integrated with AWS Organizations (when you're the delegated admin), set a policy to target an organizational unit:

```
aws ec2 enable-ipam-policy \
    --ipam-policy-id ipam-policy-12345678 \
    --organization-target-id ou-123
```

**Important**  
Enabling this policy will replace any active IPAM policies on the selected accounts or organizational units.

**Step 4: Test your policy**

 Create a new resource of the type you configured (like an EIP) in one of the target accounts. The resource will automatically use an IP address from your IPAM pool.

**Important**  
If you choose a specific IPAM pool or EIP allocation ID when creating an AWS resource, that will override the IPAM policy.

**Step 5: Monitor usage**

Check your [IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-usage-ipam.html) in the console to see IP addresses being allocated to your resources.