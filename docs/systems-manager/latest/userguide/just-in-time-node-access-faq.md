AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Just-in-time node access frequently asked

questions

## How do I move from Session Manager to just-in-time node

access?

After setting up the unified console and enabling just-in-time node access, you
must modify your existing IAM policies to complete the move to just-in-time node
access. This includes adding the required permissions for just-in-time node access
and removing permission for the `StartSession` API operation for
Session Manager. For more information about IAM policies for just-in-time node access see
[Setting up
just-in-time access with Systems Manager](systems-manager-just-in-time-node-access-setting-up.md "systems-manager-just-in-time-node-access-setting-up.md").

## Do I have to set up the unified console to use

just-in-time node access?

Yes, setting up the unified console is a prerequisite for just-in-time node
access. However, after you set up the unified console and enable just-in-time node
access, there are several methods for connecting to your nodes. For example, you can
start just-in-time node access sessions from the Amazon EC2 console and the AWS CLI. For
more information about setting up the unified console, see [Setting up Systems Manager unified console
for an organization](systems-manager-setting-up-organizations.md "systems-manager-setting-up-organizations.md").

## Is there cost associated with just-in-time node

access?

Systems Manager provides a 30 day free trial for just-in-time node access. After the trial,
just-in-time node access incurs costs. For more information, see [AWS Systems Manager
Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

## What is the precedence for just-in-time node

access approval policies?

Approval policies are evaluated in the following order:

1. Deny-access
2. Auto-approval
3. Manual

## How are manual approval policies

evaluated?

Just-in-time node access always favors the more specific policy for a node. Manual
approval policies are evaluated in the following order:

1. Tag specific target
2. All nodes target

## What happens if there isn't an approval policy

that applies to a node?

To connect to a node using just-in-time node access, an approval policy must apply
to the node. If there are no approval policies that apply to a node, users are
unable to request access to the node.

## Can multiple approval policies target a tag?

A tag can only be targeted once in your approval policies.

## What happens if multiple manual approval policies

apply to a node as a result of overlapping tags?

When multiple manual approval policies apply to a node, this results in a conflict
and users are unable to request access to the node. Keep this in mind when creating
your manual approval policies since some instances might have multiple tags
depending on your case.

## Can I use just-in-time node access to request access

and start sessions on nodes across accounts and Regions?

Just-in-time node access supports requesting access to and starting sessions on
nodes in the same account and Region as the requester.

## Can I use just-in-time node access to request access

and start sessions on nodes registered with a hybrid activation?

Yes, just-in-time node access supports requesting access to and starting sessions
on nodes registered with a hybrid activation. The node must be registered in the
same account and Region as the requester.
