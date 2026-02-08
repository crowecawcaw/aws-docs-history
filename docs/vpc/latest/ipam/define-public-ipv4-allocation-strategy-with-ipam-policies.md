# Define public IPv4 allocation strategy with IPAM policies

An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations. If you [bring your own IP (BYOIP)](tutorials-byoip-ipam.md "tutorials-byoip-ipam.md"), this helps reduce your AWS public IPv4 costs.

**When to use IPAM policies**

Use IPAM policies to:

- Reduce public IPv4 costs by using BYOIP addresses
- Centrally control which IP pools your AWS resources use
- Ensure consistent IP allocation across your organization
  **How it works**

When you create an AWS resource that needs a public IP address in an account with IPAM policies enforced:

- IPAM checks your policy rules in order.
- If a rule matches the resource type, IPAM allocates an IP from the specified pool.
- If the pool is empty and overflow is enabled, Amazon provides an IP address.
- If no rules match, the default behavior applies.
  **Supported services and resources**

You can create IPAM policies to define how public IPv4 addresses from IPAM pools are allocated to the following AWS services and resources:

- Elastic IP addresses (EIPs)
- Application Load Balancers (ALBs)
- Amazon Relational Database Service (RDS)
- Regional NAT gateways

###### Important

If you choose a specific IPAM pool or EIP allocation ID when creating an AWS resource, that will override the IPAM policy.

**Prerequisites**

- An [IPAM](create-ipam.md "create-ipam.md") in the delegated administrator account with [advanced tier](mod-ipam-tier.md "mod-ipam-tier.md") enabled
- A [public IPAM pool](create-top-ipam.md "create-top-ipam.md") with IPv4 addresses
- [IAM permissions](iam-ipam.md "iam-ipam.md") for IPAM and EC2 operations
  **Terminology**

**IPAM policy**

An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations. A policy can be applied to an individual AWS account or an entity within AWS Organizations.

**Allocation rules**

Optional configurations within an IPAM policy that map AWS resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.

**Target**

An individual AWS account or an entity within an AWS Organization to which an IPAM policy can be applied.

**Step 1: Create an IPAM policy**

###### Using the AWS Console:

Follow these steps to create an IPAM policy using the AWS Console:

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the left navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. Enter a **Name** for your policy (optional).
5. Select the **IPAM** to associate with this policy.
6. (Optional) Add tags.
7. Choose **Create policy**.

###### Using the AWS CLI:

Use the [create-ipam-policy](../../../cli/latest/reference/ec2/create-ipam-policy.md "../../../cli/latest/reference/ec2/create-ipam-policy.md") command.

**Step 2: Add allocation rules**

After creating the policy, you need to add allocation rules that define how IP addresses are allocated:

###### Using the AWS Console:

Follow these steps to add allocation rules using the AWS Console:

1. In the left navigation pane, choose **Policies**.
2. Choose the policy you created in the previous step.
3. In your policy details page, choose the **Allocation rules** tab.
4. Choose **Create allocation rules**.
5. Configure the **Service configuration**:
   - **Locale**: Choose the AWS Region (us-east-1) or Local Zone where you want this policy to apply.
   - **Resource type**: Select the AWS service or resource type for this policy (Elastic IP addresses, RDS database instances, Application Load Balancers, or NAT gateways in regional availability mode).

6. Configure **Rules configuration**:
   - **IPAM pool**: Select the IPAM pool that will provide IP addresses.
   - Review the pool details (locale, public IP source, space available, and CIDR ranges available).

7. (Optional) Choose **Add new rule** to create additional rules.
8. Choose **Create allocation rule**.

###### Using the AWS CLI:

Use the [modify-ipam-policy-allocation-rules](../../../cli/latest/reference/ec2/modify-ipam-policy-allocation-rules.md "../../../cli/latest/reference/ec2/modify-ipam-policy-allocation-rules.md") command.

**Step 3: Enable the policy**

Specify which accounts should use this policy.

###### Using the AWS Console:

Follow these steps to enable the policy using the AWS Console:

1. In your policy details page, choose the **Targets** tab.
2. Choose **Manage policy targets**.
3. Do one of the following:
   - For single account usage (IPAM not integrated with AWS Organizations), choose **Enable for your account**.
   - For IPAM integrated with AWS Organizations (when you're the delegated admin):
     - In the **Organizational structure** section, select the accounts or organizational units where you want to apply this policy.
     - Check the **Enabled** checkbox for each target.
     - Choose **Save Changes**.
     - **Important**: Enabling this policy will replace any active IPAM policies on the selected accounts or organizational units.

###### Using the AWS CLI:

Use the [enable-ipam-policy](../../../cli/latest/reference/ec2/enable-ipam-policy.md "../../../cli/latest/reference/ec2/enable-ipam-policy.md") command based on your setup:

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

###### Important

Enabling this policy will replace any active IPAM policies on the selected accounts or organizational units.

**Step 4: Test your policy**

Create a new resource of the type you configured (like an EIP) in one of the target accounts. The resource will automatically use an IP address from your IPAM pool.

###### Important

If you choose a specific IPAM pool or EIP allocation ID when creating an AWS resource, that will override the IPAM policy.

**Step 5: Monitor usage**

Check your [IPAM pool](monitor-cidr-usage-ipam.md "monitor-cidr-usage-ipam.md") in the console to see IP addresses being allocated to your resources.
