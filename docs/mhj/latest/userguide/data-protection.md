AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Data protection in AWS Migration Hub Journeys

The AWS [shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/ "http://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Amazon Elastic
Compute Cloud. As described in this model, AWS is responsible for protecting the global
infrastructure that runs all of the AWS Cloud. You are responsible for maintaining
control over your content that is hosted on this infrastructure. This content includes
the security configuration and management tasks for the AWS services that you use. For
more information about data privacy, see the [Data Privacy FAQ](http://aws.amazon.com/compliance/data-privacy-faq "http://aws.amazon.com/compliance/data-privacy-faq").
For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security Blog_.

## Migration space ownership

Ownership is an attribute that an individual can have in Migration Hub Journeys. When you create a
migration space, you become an owner of that space. You can also mark other individual
members of the space as owners. A space can have up to 5 owners. To become an owner of a
migration space, an individual must have the [MigrationSpaceAdmin](roles.md#migration-space-admin "roles.md#migration-space-admin")
role in that space. Unlike roles, however, ownership doesn't confer any permissions.

For information about roles and permissions in Migration Hub Journeys, see [Roles and permissions](permissions.md "permissions.md").

To learn about how the space ownership attribute is associated with data protection,
see [Deleting your AWS Builder ID](#isolation "#isolation").

## Deleting your AWS Builder ID

When you delete your AWS Builder ID, we delete your personally identifiable information
(PII) and Migration Hub Journeys resources. Because migrations are collaborative, immediately
deleting resources might cause problems for other users of those resources. To mitigate
that concern, account deletion happens in two phases: When you delete your AWS Builder ID, we
send you a notification email and isolate your account for 7 days. During that 7-day
period, you can't log into your account. Other users see you in Migration Hub Journeys as
`[isolated user]`, and can't assign any tasks to you. At the end of the
7-day period, we delete your account. Other users then see you in Migration Hub Journeys as
`[deleted user]`.

If you are the last [owner](#space-ownership "#space-ownership") of a migration space
when you delete your AWS Builder ID, all active members of that migration space receive an
email stating that the migration space will be deleted in 7 days. At the end of the
7-day account isolation period, the space and all the migration journeys it contains
will be deleted. To save a journey from getting deleted at the end of the 7-day
isolation period, any member that has the `JourneyAdmin` role in that journey
can transfer the journey to another migration space before the end of the 7-day
period.
