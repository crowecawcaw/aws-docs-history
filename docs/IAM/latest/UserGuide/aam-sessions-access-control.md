# Sessions and access control

## Understanding sessions

Users who access AWS accounts using assignments in account access manager initiate the following session
types:

1. **IAM role session** - The IAM role a user assumes is a
   temporary credential for access to AWS resources that can be active for up to 12
   hours.
2. **Account access portal session** – Users initiate this
   session when using the account access portal. It is managed as an [application session](../../../singlesignon/latest/userguide/authconcept.md "../../../singlesignon/latest/userguide/authconcept.md") by
   IAM Identity Center.
3. **AWS access portal session (also called [user interactive
   session](../../../singlesignon/latest/userguide/authconcept.md "../../../singlesignon/latest/userguide/authconcept.md"))** – This session is managed by IAM Identity Center.
4. **External identity source (IdP or Microsoft AD) session** –
   This session is applicable when the IAM Identity Center instance is connected to an external identity source
   for authentication.

For more information about user interactive and application sessions in IAM Identity Center including
session duration, see [Understanding authentication sessions in
IAM Identity Center](../../../singlesignon/latest/userguide/authconcept.md "../../../singlesignon/latest/userguide/authconcept.md") in the _AWS IAM Identity Center User Guide_.

###### Important

IAM role sessions operate independently once established. They persist for the duration
configured in the IAM role, which can be up to 12 hours, regardless of the status of the
sessions in the account access portal and AWS access portal. This behavior ensures that
long-running CLI operations or console sessions are not unexpectedly ended.

## Revoke user access

To revoke user access assumed through account access manager role assignments, see [Revoke user access](../../../singlesignon/latest/userguide/revoke-user-permissions.md "../../../singlesignon/latest/userguide/revoke-user-permissions.md") in
the _AWS IAM Identity Center User Guide_.

## Attribute-based access control

Account access manager supports attribute-based access control (ABAC) with IAM role tags and user
attributes configured as session tags in IAM Identity Center. For more information, see [Attribute-based access
control](../../../singlesignon/latest/userguide/abac.md "../../../singlesignon/latest/userguide/abac.md") in the _AWS IAM Identity Center User Guide_.
