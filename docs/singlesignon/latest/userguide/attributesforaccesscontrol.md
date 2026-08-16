# Attributes for access control

**Attributes for access control** is the name of the page in the
IAM Identity Center console where you select user attributes that you want to use in policies to
control access to resources. You can assign users to workloads in AWS based on
existing attributes in the users' identity source.

For example, suppose you want to assign access to S3 buckets based on department
names. While on the **Attributes for access control** page, you
select the **Department** user attribute for use with
attribute-based access control (ABAC). In the IAM Identity Center permission set (or IAM role when using account access manager), you then write a
policy that grants users access only when the **Department**
attribute matches the department tag that you assigned to your S3 buckets. IAM Identity Center
passes the user's department attribute to the account being accessed. The attribute
is then used to determine access based on the policy. When IAM Identity Center passes these
attributes to the account, they are sent as session tags that you can reference
using the `aws:PrincipalTag/`tag-key``
condition key in all relevant AWS IAM policy types. For more information about
ABAC, see [Attribute-based access control](abac.md "abac.md").

## Getting started

How you get started configuring attributes for access control depends on which
identity source you are using. Regardless of the identity source you choose,
after you have selected your attributes you need to create or edit permission
set policies (or IAM role policies when using account access manager). These policies must grant user identities access to AWS
resources.

### Choosing attributes when using IAM Identity Center as your identity source

When you configure IAM Identity Center as the identity source, you first add users and
configure their attributes. Next, navigate to the **Attributes for
access control** page and select the attributes you want to use
in policies. Finally, navigate to the **AWS accounts**
page to create or edit permission sets to use the attributes for
ABAC.

### Choosing attributes when using AWS Managed Microsoft AD as your identity source

When you configure IAM Identity Center with AWS Managed Microsoft AD as your identity source, you
first map a set of attributes from Active Directory to user attributes in
IAM Identity Center. Next, navigate to the **Attributes for access
control** page. Then choose which attributes to use in your
ABAC configuration based on the existing set of SSO attributes mapped from
Active Directory. Finally, author ABAC rules using the access control
attributes in permission sets (or IAM roles when using account access manager) to grant user identities access to AWS
resources. For a list of the default mappings for user attributes in IAM Identity Center
to the user attributes in your AWS Managed Microsoft AD directory, see [Default mappings between IAM Identity Center and Microsoft AD](attributemappingsconcept.md#defaultattributemappings "attributemappingsconcept.md#defaultattributemappings").

### Choosing attributes when using an external identity provider as your identity source

When you configure IAM Identity Center with an external identity provider (IdP) as your
identity source, there are two ways to use attributes for ABAC.

- **Configure attribute mappings in the IAM Identity Center
  console.** You can map attributes from the IAM Identity
  Center directory to session tags on the **Attributes for
  access control** page in the IAM Identity Center console. The
  attribute values that you choose here are sourced from the Identity
  Center directory and replace the values for any matching attributes
  that come from an IdP through a SAML assertion. Depending on whether
  you are using SCIM, consider the following:

  - If using SCIM, the IdP automatically synchronizes the
    attribute values into IAM Identity Center. You can then select these
    synchronized attributes on the **Attributes for
    access control** page to use them as session
    tags.
  - If you are not using SCIM, you must manually add the users
    and set their attributes just as if you were using IAM Identity Center as
    an identity source. Next, navigate to the
    **Attributes for access control** page
    and choose the attributes you want to use in policies.

- **Pass attributes from your IdP through SAML
  assertions.** You can configure your IdP to send
  attributes as session tags through SAML assertions. To do this,
  configure your IdP to send SAML assertions with the attribute name
  set to
  `https://aws.amazon.com/SAML/Attributes/AccessControl:`TagKey``,
  replacing `TagKey` with the session tag key
  you want to populate. IAM Identity Center passes the attribute name and value from
  the IdP through for policy evaluation.

It is not necessary to configure an ABAC attribute mapping on the
**Attributes for access control** page for
attributes that you pass in through SAML assertions from your
external IdP. However, if you configure an ABAC mapping for the same
attribute on the **Attributes for access control**
page, the mapping from the Identity Center directory takes precedence
and replaces the value sent by your IdP in the SAML assertion.

###### Note

Attributes in SAML assertions will not be visible to you on
the **Attributes for access control** page. You
will have to know these attributes in advance and add them to
access control rules when you author policies. If you decide to
trust your external IdPs for attributes, then these attributes
will always be passed when users federate into AWS accounts.
For information about how to configure user attributes for
access control in your IdP to send through SAML assertions, see
the [IAM Identity Center identity source tutorials](tutorials.md "tutorials.md") for
your IdP.

For a complete list of supported attributes for user attributes in IAM Identity Center to
the user attributes in your external IdPs, see [Supported external identity provider attributes](attributemappingsconcept.md#supportedidpattributes "attributemappingsconcept.md#supportedidpattributes").

To get started with ABAC in IAM Identity Center, see the following topics.

###### Topics

- [Enable and configure attributes for access control](configure-abac.md "configure-abac.md")
- [Create permission policies for ABAC in IAM Identity Center](configure-abac-policies.md "configure-abac-policies.md")
