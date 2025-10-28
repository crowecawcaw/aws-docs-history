# Options for implementing the trusted

entity

There are two options for setting up the trusted entity role in AWS Elemental MediaLive: a simple option
and a complex option.

Your organization must decide which option to use. This decision must be made by a person in
your organization who understands your organization's requirements for access to resources. This
person must understand whether there is a requirement that AWS Elemental MediaLive channels should be
restricted in their access to resources in other AWS services. For example, this person should
determine whether channels should be restricted in their access to buckets in Amazon S3 so that a
specified channel can access some buckets and not others.

###### Topics

- [Simple option](#about-simple-scenario "#about-simple-scenario")
- [Complex option](#about-complex-scenarios "#about-complex-scenarios")

## Simple option

The simple option typically applies when both these situations apply:

- Users in your organization are using AWS Elemental MediaLive to encode the organization's own assets
  (not assets belonging to customers).
- Your organization doesn't have rigorous rules about accessing assets. For example, you
  don't have video assets that can be handled only by specific users or departments.

With the simple option, there is only one role: `MediaLiveAccessRole`. All
channels use this role and all users in your organization can attach that role to the channels
that they work with.

The `MediaLiveAccessRole` role grants broad access to operations and complete
access to all resources. It allows either read-only access or read/write access to all the
services that MediaLive must access when a channel is running. And most significantly, it allows
full access to all the resources associated with those services.

If the simple option is suitable to your deployment, follow the steps in [Create the trust entity – simple option](setup-trusted-entity-simple.md "setup-trusted-entity-simple.md").

## Complex option

The complex option applies when the `MediaLiveAccessRole` role is too broad for
your use, given that it allows broad access to operations and complete access to all resources.

For example, you might have the following requirements:

- A requirement that a given channel should be allowed to access only specific resources,
  and another channel should be allowed to access only specific, different resources. In a
  situation like this, you need to create several access roles. Each role narrows down
  permissions to a different set of resources.
- A requirement that each user should be allowed to display only specific roles on the
  console, to prevent a user from viewing a role they should not know about or to prevent a user
  from selecting the wrong role. For example, you might want to set up so that only user A can
  work with workflow X, and you might further require that only user A knows about workflow
  X.

If the complex option is applicable to your deployment, follow the steps in [Create the trusted entity - complex option](setup-trusted-entity-complex.md "setup-trusted-entity-complex.md").
