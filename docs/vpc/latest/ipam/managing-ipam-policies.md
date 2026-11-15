

# Managing IPAM policies
<a name="managing-ipam-policies"></a>

This section describes the prerequisites for IPAM policies and how to create and enable them.

## Prerequisites
<a name="ipam-policies-prerequisites"></a>

Before you begin, make sure that you have the following:
+ An [IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html)
+ [AWS Identity and Access Management (IAM) permissions](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam.html) for the IPAM policy operations and for the Amazon Elastic Compute Cloud (Amazon EC2) operations that create the governed resources

## Creating an IPAM policy
<a name="ipam-policies-create"></a>

You can create an IPAM policy by using the AWS Management Console or the AWS CLI.

**To create an IPAM policy (console)**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the left navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. Enter a **Name** for your policy (optional).

1. Select the IPAM to associate with this policy.

1. (Optional) Add tags.

1. Choose **Create policy**.

**To create an IPAM policy (AWS CLI)**
+ Use the [create-ipam-policy](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-ipam-policy.html) command.

After you create the policy, add rules to it. For more information about allocation rules, see [Defining a public IPv4 allocation strategy with IPAM policies](define-public-ipv4-allocation-strategy-with-ipam-policies.md).

## Enabling an IPAM policy
<a name="ipam-policies-enable"></a>

Specify which accounts should use the policy. A policy's targets apply to all of the rules in the policy, and only one policy can be enabled for a given target.

**To enable an IPAM policy (console)**

1. In your policy details page, choose the **Targets** tab.

1. Choose **Manage policy targets**.

1. Do one of the following:
   + For single account usage (IPAM not integrated with AWS Organizations, or an account applying a policy to itself), choose **Enable for your account**.
   + For IPAM integrated with AWS Organizations (when you're the delegated admin):
     + In the **Organizational structure** section, select the accounts or organizational units where you want to apply this policy.
     + Check the **Enabled** checkbox for each target.
     + Choose **Save Changes**.

**To enable an IPAM policy (AWS CLI)**
+ Use the [enable-ipam-policy](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-ipam-policy.html) command based on your setup:
  + For single account usage (IPAM not integrated with AWS Organizations, or an account applying a policy to itself):

    ```
    aws ec2 enable-ipam-policy \
        --ipam-policy-id {{ipam-policy-12345678}}
    ```
  + For IPAM integrated with AWS Organizations (when you're the delegated admin), set a policy to target an account in the organization:

    ```
    aws ec2 enable-ipam-policy \
        --ipam-policy-id {{ipam-policy-12345678}} \
        --organization-target-id {{111122223333}}
    ```
  + For IPAM integrated with AWS Organizations (when you're the delegated admin), set a policy to target an organizational unit:

    ```
    aws ec2 enable-ipam-policy \
        --ipam-policy-id {{ipam-policy-12345678}} \
        --organization-target-id {{ou-123}}
    ```

**Important**  
Enabling a policy for a target replaces any policy that is already enabled for that same target. Policies enabled for different targets coexist. For more information, see [Which policy applies to an account](ipam-policies.md#ipam-policies-precedence).