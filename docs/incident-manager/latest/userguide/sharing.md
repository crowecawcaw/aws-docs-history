AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Working with shared contacts and response plans in

Incident Manager

With contact sharing, as a contact owner, you can share contact information, escalation
plans, and engagements with other AWS accounts or within an AWS
organization.

With response plan sharing, as a response plan owner, you can share a response plan and the
related incidents with other AWS accounts or within an AWS organization.

A contact or response plan owner can share contacts and response plans with:

- Specific AWS accounts inside or outside of its organization in AWS Organizations
- An organizational unit inside its organization in AWS Organizations
- Its entire organization in AWS Organizations

###### Contents

- [Prerequisites for sharing contacts and response
  plans](#sharing-prereqs "#sharing-prereqs")
- [Related services](#sharing-related "#sharing-related")
- [Sharing a contact or response plan](#sharing-share "#sharing-share")
- [Stop sharing a shared contact or response plan](#sharing-unshare "#sharing-unshare")
- [Identifying a shared contact or response plan](#sharing-identify "#sharing-identify")
- [Shared contact and response plan permissions](#sharing-perms "#sharing-perms")
- [Billing and metering](#sharing-billing "#sharing-billing")
- [Instance limits](#sharing-limits "#sharing-limits")

## Prerequisites for sharing contacts and response

plans

To share a contact or response plan with your organization or organizational unit in
AWS Organizations:

- You must own the resource in your AWS account. You can't share a contact or
  response plan that has been shared with you.
- You must enable sharing with AWS Organizations. For more information, see [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
  _AWS RAM User Guide_.

## Related services

Contact and response plan sharing integrates with AWS Resource Access Manager (AWS RAM). With AWS RAM, you can
share your AWS resources with any AWS account or through AWS Organizations. You share resources
that you own by creating a _resource share_. A resource share specifies
the resources to share, and the consumers with whom to share them. Consumers can be
individual AWS accounts, organizational units, or an entire organization in
AWS Organizations.

For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

## Sharing a contact or response plan

After you share a response plan, the consumers have access to all past, current, and
future incidents created using that response plan.

After you share a contact, the consumers have access to the contact information,
engagement plan, escalation plans, and engagements that occur during an incident. Consumers
can also engage a contact or escalation plan during an incident.

If you're part of an organization in AWS Organizations and sharing within your organization is
enabled, consumers in your organization are automatically granted access to the shared
contact or response plan. Otherwise, consumers receive an invitation to join the resource
share and are granted access to the shared contact or response plan after accepting the
invitation.

You can share a contact or response plan that you own by using the AWS RAM console or the
AWS CLI.

###### Note

Currently, the ability to add a contact that’s shared from another account to a
response plan is not supported.

###### To share a contact or response plan that you own by using the AWS RAM console

See [Creating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create") in the _AWS RAM User Guide_.

###### To share a contact or response plan that you own by using the AWS CLI

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

## Stop sharing a shared contact or response plan

When a resource owner stops sharing a contact or response plan with a consumer, the
contacts, response plans, escalation plans, engagements, and incidents no longer appear in
the consumer's console.

###### Note

The consumer continues to see the contacts, response plans, escalation plans,
engagements, or incidents without updates, if they're viewing them in the console, until
they refresh the page or navigate away from the page.

To stop sharing a shared contact or response plan that you own, you must remove it from
the resource share. You can do this by using the AWS RAM console or the AWS CLI.

###### To stop sharing a shared contact or response plan that you own by using the AWS RAM

console

See [Updating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To stop sharing a shared contact or response plan that you own by using the

AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

## Identifying a shared contact or response plan

Owners and consumers can identify shared contacts and response plans by using the
Incident Manager console and AWS CLI.

To identify a shared contact or response plan by using the Incident Manager console

###### Note

Contacts, response plans, escalation plans, engagements, and incidents are generally
not identifiable as a shared resource in the Incident Manager console. In places where the
Amazon Resource Name (ARN) is visible, the ARN contains the owner's account ID.

###### To identify a shared contact or response plan by using the AWS CLI

Use the [ListResponsePlans](../APIReference/API_ListResponsePlans.md "../APIReference/API_ListResponsePlans.md") or [ListContacts](../APIReference/API_SSMContacts_ListContacts.md "../APIReference/API_SSMContacts_ListContacts.md") commands. The command returns the contacts and
response plans that you own and contacts and response plans that are shared with you. The
ARN shows the AWS account ID of the contact or response plan owner.

## Shared contact and response plan permissions

### Permissions for owners

Owners can update, view, share, stop sharing, and use contacts and response plans.
Contacts and response plans include related engagements and incidents.

### Permissions for consumers

Consumers can use and view only response plans and contacts. Contacts and response
plans include related engagements and incidents.

## Billing and metering

The owner of the resource is billed for the resource. Consumers aren't billed for
resources shared with them. There aren't extra costs associated with sharing a
resource.

## Instance limits

Sharing a resource doesn't affect the limits of the resource in the owner's or
consumer's account. Only the owner's account is used to calculate the limits of the
resource.
