# Apply hierarchy-based access control in

Amazon Connect

You can restrict access to contacts based on the agent hierarchy assigned to a user.
You do this by using security profile permissions such as [Restrict contact access](contact-search.md#required-permissions-search-contacts "contact-search.md#required-permissions-search-contacts"). In
addition to these permissions, you can also use hierarchies enforce granular access
controls for resources such as users, and use tags.

This topic information about configuring hierarchy-based access controls.

###### Contents

- [Overview](#hierarchy-based-access-control-background "#hierarchy-based-access-control-background")
- [Apply hierarchy-based
  access control using the API/SDK](#hierarchy-based-access-control-api-sdk "#hierarchy-based-access-control-api-sdk")
- [Apply hierarchy-based
  access control using the Amazon Connect admin website](#hierarchy-based-access-control-console "#hierarchy-based-access-control-console")
- [Configuration
  limitations](#hierarchy-based-access-control-config-limitations "#hierarchy-based-access-control-config-limitations")
- [Best practices for applying
  hierarchy-based access controls](#hierarchy-based-access-control-best-practices "#hierarchy-based-access-control-best-practices")

## Overview

Hierarchy-based access control enables you to configure granular access to
specific resources based on the [agent
hierarchy](agent-hierarchy.md "agent-hierarchy.md") that is assigned to a user. You can configure hierarchy-based
access controls by using the API/SDK or the Amazon Connect admin website. 

The only resource that supports hierarchy-based access control is users. This
authorization model works with [tag-based
access control](tag-based-access-control.md "tag-based-access-control.md") so you can restrict access to users, allowing them to see
only other users who belong to their same hierarchy group and who have specific tags
associated to them.

###### Note

After you apply hierarchy-based access control to users, they can access their
hierarchy group and all of its descendants (beyond the child level).

## Apply hierarchy-based

access control using the API/SDK

To use hierarchies to control access to resources within your AWS accounts, you
need to provide the hierarchy's information in the condition element of an IAM
policy. For example, to control access to a user belonging to a specific hierarchy,
use the `connect:HierarchyGroupL3Id/hierarchyGroupId` condition key,
along with a specific operator like `StringEquals` to specify which
hierarchy group the user must belong to, in order to allow given actions for it.

Following are the supported condition keys:

1. `connect:HierarchyGroupL1Id/hierarchyGroupId`
2. `connect:HierarchyGroupL2Id/hierarchyGroupId`
3. `connect:HierarchyGroupL3Id/hierarchyGroupId`
4. `connect:HierarchyGroupL4Id/hierarchyGroupId`
5. `connect:HierarchyGroupL5Id/hierarchyGroupId`

Each key represents the ID of a given hierarchy group in a specific level of the
user's hierarchy structure.

## Apply hierarchy-based

access control using the Amazon Connect admin website

To use hierarchies to control access to resources the Amazon Connect admin website, you configure the
access control section within a given security profile.

For example, to enable granular access control for a given user based on the
hierarchy they belong to, you configure the user as an access controlled resource.
To do this, you have the following two options:

1. Enforce hierarchy-based access control based on **the user's hierarchy**

This option ensures that the user being given access can only manage users
that belong to this hierarchy. For example, enabling this configuration for
a given user enables them to manage other users that either belong to their
hierarchy group or a child hierarchy group. 2. Enforce hierarchy-based access control based on **a
specific hierarchy**

This option ensures that the user being given access can only manage users
that belong to the hierarchy defined in the security profile. For example,
enabling this configuration for a given user enables them to manage other
users that either belong to the hierarchy group specified in the security
profile or a child hierarchy group.

## Configuration

limitations

Granular access control is configured on a security profile. Users can be
assigned a maximum of two security profiles that enforce granular access control. In
this case, the permissions become less restrictive and act as a union of both
permission sets.

For example, if one security profile enforces hierarchy-based access control and
another one enforces tag-based access control, the user is able to manage any user
that belongs to the same hierarchy or tagged with the given tag. If both tag-based
and hierarchy-based access control are configured as part of the same security
profile, both conditions will need to be met. In this case, the user can only manage
users that belong to the same hierarchy and who are tagged with a given tag. 

A user can have more than two security profiles, as long as those additional
security profiles do not enforce granular access control. If multiple security
profiles are present with overlapping resource permissions, the security profile
without hierarchy-based access control is enforced over the one with hierarchy-based
access control.

Service linked roles are required in order to configure hierarchy-based access
control. If your instance was created after October 2018, this is available by
default with your Amazon Connect instance. However, if you have an older instance, refer to
[Use service-linked roles for Amazon Connect](connect-slr.md "connect-slr.md") for
instructions for how to enable service linked roles.

## Best practices for applying

hierarchy-based access controls

- Review the [AWS shared
  responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

Applying hierarchy-based access control is an advanced configuration
feature that is supported by Amazon Connect and that follows the AWS shared
responsibility model. It is important to ensure that you are correctly
configuring your instance to comply with your desired authorization needs.

- Ensure that you have enabled at least _view_
  permissions for the resources that you enable hierarchy-based access control
  for.

This will ensure that you avoid permission inconsistencies that result in
denied access requests. Hierarchy-based access controls are enabled at the
resource level, which means that each resource can be restricted
independently.

- Carefully review the permissions that are granted when hierarchy-based
  access control is enforced.

For example, enabling hierarchy restricted access to users and view/edit
permissions security profiles would allow a user to create/update a security
profile with privileges that supersede the intended user access control
settings.

    + When logged in to the Amazon Connect console with hierarchy-based access
     controls applied, users will not be able to access historical change
     logs for the resources that they are restricted on.
    + When trying to assign a child resource to a parent resource with
     hierarchy-based access control on the child resource, the operation
     will be denied if the child resource does not belong to your
     hierarchy.


    For example, if you try to assign a user to a quick connect but
     you don't have access to the user's hierarchy, the operation fails.
     This is however not true for disassociations. You are able to
     disassociate a user freely even with hierarchy-based access control
     enforced assuming you have access to the quick connect. This is
     because disassociations are about discarding an existing relation
     (as opposed to new associations) between two resources and is
     modeled as part of the parent resource (in this case, the quick
     connect), which the user already has access to.

- Be thoughtful about the permissions granted on parent resources since
  users could be disassociated without their supervisor’s knowledge.
- Disable access to the following functionality when you apply
  hierarchy-based access controls in the Amazon Connect admin website.

| Functionality | Security profile permission that disables access
|
| --- | --- |
| Contact search | Contact search - View |
| Login/Login out report | Login/Login out report - View |
| Rules | Rules - View |
| Saved reports | Saved reports - View |
| Agent Hierarchy | Agent Hierarchy - View |
| Flow/Flow module | Flow modules - View |
| Scheduling | Schedule manager - View | If you do not disable access to these resources, users with hierarchy-based access controls on a particular resource that view these pages in the Amazon Connect admin website may see an unrestricted list of users. For more information about how to manage permissions, see [List of security profile permissions](security-profile-list.md "security-profile-list.md").
