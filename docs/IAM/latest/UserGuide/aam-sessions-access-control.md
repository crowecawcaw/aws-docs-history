

# Sessions and access control
<a name="aam-sessions-access-control"></a>

## Understanding sessions
<a name="aam-understanding-sessions"></a>

Users who access AWS accounts using assignments in account access manager initiate the following session types:

1. **IAM role session** - The IAM role a user assumes is a temporary credential for access to AWS resources with a default duration of 1 hour.

1. **Account access portal session** – Users initiate this session when using the account access portal. It is managed as an [application session](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html) by IAM Identity Center.

1. **AWS access portal session (also called [user interactive session](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html))** – This session is managed by IAM Identity Center.

1. **External identity source (IdP or Microsoft AD) session** – This session is applicable when the IAM Identity Center instance is connected to an external identity source for authentication.

For more information about user interactive and application sessions in IAM Identity Center including session duration, see [Understanding authentication sessions in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html) in the *AWS IAM Identity Center User Guide*.

**Important**  
Sessions of IAM roles assigned by account access manager operate based on the default session duration of 1 hour, regardless of the maximum session duration set in the IAM role, the status of the sessions in the account access portal and AWS access portal.

## Revoke user access
<a name="aam-revoke-user-access"></a>

To revoke user access assumed through account access manager role assignments, see [Revoke user access](https://docs.aws.amazon.com/singlesignon/latest/userguide/revoke-user-permissions.html) in the *AWS IAM Identity Center User Guide*.

## Attribute-based access control
<a name="aam-abac"></a>

You can configure your identity provider (IdP) to send attributes as session tags through SAML assertions by setting the attribute name to `https://aws.amazon.com/SAML/Attributes/AccessControl:TagKey`, where {{TagKey}} is the session tag key you want to populate. IAM Identity Center passes the attribute name and value from the IdP through for policy evaluation.