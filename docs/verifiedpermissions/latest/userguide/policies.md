# Amazon Verified Permissions policies

A _policy_ is a statement that either permits or forbids a
_principal_ to take one or more _actions_ on a
_resource_. Each policy is evaluated independently of every other
policy. For more information about how Cedar policies are structured and evaluated, see
[Cedar policy validation against
schema](https://docs.cedarpolicy.com/policies/validation.html "https://docs.cedarpolicy.com/policies/validation.html") in the Cedar policy language Reference Guide.

###### Important

When you write Cedar policies that reference principals, resources and actions, you
can define the unique identifiers used for each of those elements. We strongly recommend
that you follow these best practices:

- **Use universally unique identifiers (UUIDs)
  for all principal and resource identifiers.**

For example, if user `jane` leaves the company, and you later let
someone else use the name `jane`, then that new user automatically
gets access to everything granted by policies that still reference
`User::"jane"`. Cedar can’t distinguish between the new user
and the old. This applies to both principal and resource identifiers. Always use
identifiers that are guaranteed unique and never reused to ensure that you don’t
unintentionally grant access because of the presence of an old identifier in a
policy.

Where you use a UUID for an entity, we recommend that you follow it with the
// comment specifier and the ‘friendly’ name of your entity. This helps to make
your policies easier to understand. For example: principal ==
Role::"a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111", // administrators

- **Do not include personally identifying, confidential, or
  sensitive information as part of the unique identifier for your principals
  or resources.** These identifiers are included in log entries
  shared in AWS CloudTrail trails.

###### Topics

- [Creating Amazon Verified Permissions static policies](policies-create.md "policies-create.md")
- [Editing Amazon Verified Permissions static policies](policies-edit.md "policies-edit.md")
- [Adding context](context.md "context.md")
- [Using the Amazon Verified Permissions test bench](test-bench.md "test-bench.md")
- [Amazon Verified Permissions example policies](policies-examples.md "policies-examples.md")
