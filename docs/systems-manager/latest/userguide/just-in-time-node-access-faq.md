

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Just-in-time node access frequently asked questions
<a name="just-in-time-node-access-faq"></a>

## How do I move from Session Manager to just-in-time node access?
<a name="migrating"></a>

After setting up the unified console and enabling just-in-time node access, modify your existing IAM policies to complete the transition. This includes adding the required permissions for just-in-time node access and removing permission for the `StartSession` API operation for Session Manager. For more information about IAM policies for just-in-time node access see [Setting up just-in-time access with Systems Manager](systems-manager-just-in-time-node-access-setting-up.md).

## Do I have to set up the unified console to use just-in-time node access?
<a name="prerequisites"></a>

Yes, setting up the unified console is a prerequisite for just-in-time node access. However, after you set up the unified console and enable just-in-time node access, there are several methods for connecting to your nodes. For example, you can start just-in-time node access sessions from the Amazon EC2 console and the AWS CLI. For more information about setting up the unified console, see [Setting up Systems Manager unified console for an organization](systems-manager-setting-up-organizations.md).

## Is there cost associated with just-in-time node access?
<a name="pricing"></a>

Systems Manager provides a 30 day free trial for just-in-time node access. After the trial, just-in-time node access incurs costs. For more information, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/).

## What is the precedence for just-in-time node access approval policies?
<a name="policy-precedence"></a>

Approval policies are evaluated in the following order:

1. Deny-access

1. Auto-approval

1. Manual

## How are manual approval policies evaluated?
<a name="manual-policy-precedence"></a>

Just-in-time node access always favors the more specific policy for a node. Manual approval policies are evaluated in the following order:

1. Tag specific target

1. All nodes target

## What happens if there isn't an approval policy that applies to a node?
<a name="no-policy-error"></a>

To connect to a node using just-in-time node access, an approval policy must apply to the node. If there are no approval policies that apply to a node, users are unable to request access to the node.

## Can multiple approval policies target a tag?
<a name="tag-target"></a>

A tag can only be targeted once in your approval policies.

## What happens if multiple manual approval policies apply to a node as a result of overlapping tags?
<a name="policy-conflict"></a>

When multiple manual approval policies apply to a node, this results in a conflict and users are unable to request access to the node. Keep this in mind when creating your manual approval policies since some instances might have multiple tags depending on your case.

## Can I use just-in-time node access to request access and start sessions on nodes across accounts and Regions?
<a name="cross-account"></a>

Just-in-time node access supports requesting access to and starting sessions on nodes in the same account and Region as the requester.

## Can I use just-in-time node access to request access and start sessions on nodes registered with a hybrid activation?
<a name="hybrid-nodes"></a>

Yes, just-in-time node access supports requesting access to and starting sessions on nodes registered with a hybrid activation. The node must be registered in the same account and Region as the requester.

## Why am I seeing a blank page when trying to connect using just-in-time node access on Session Manager?
<a name="access-request-screen-not-displayed"></a>

A blank screen can have more than one cause. If you access the Systems Manager console through an interface Amazon VPC endpoint with private DNS enabled, your browser might apply its Local Network Access policy. This policy can block the request. The request is also missing from your AWS CloudTrail event history, because your browser stops it before it reaches AWS. For details and workarounds, see [Allowing local network access in your browser](systems-manager-just-in-time-node-access-start-session.md#just-in-time-node-access-local-network-access).

Otherwise, verify that an approval policy applies to the node and that you have the permissions required to create access requests. For more information, see [What happens if there isn't an approval policy that applies to a node?](#no-policy-error) and [Setting up just-in-time access with Systems Manager](systems-manager-just-in-time-node-access-setting-up.md).