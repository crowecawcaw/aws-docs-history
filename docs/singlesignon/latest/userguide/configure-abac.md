# Enable and configure attributes for access

control

To use attribute-based access control (ABAC), you must first enable it in
either the **Settings** page of the IAM Identity Center console
or the [IAM Identity Center API](../APIReference/API_CreateInstanceAccessControlAttributeConfiguration.md "../APIReference/API_CreateInstanceAccessControlAttributeConfiguration.md"). Regardless of the identity source, you can always
configure user attributes from the Identity Store for use in ABAC. In the
console, you can do this by navigating to the **Attributes
for access control** tab on the **Settings** page. If you use an external identity provider (IdP) as
the identity source, you also have the option of receiving attributes from the
external IdP in SAML assertions. In this case, you need to configure the
external IdP to send the desired attributes. If an attribute from a SAML
assertion is also defined as an ABAC attribute in IAM Identity Center, IAM Identity Center will send the
value from its Identity Store as a [session tag](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md") on
sign-in to an AWS account.

###### Note

You cannot view attributes configured and sent by an external IdP from the
**Attributes for access control** page in the IAM Identity Center
console. If you are passing access control attributes in the SAML assertions
from your external IdP, then those attributes are directly sent to the
AWS account when users federate in. The attributes won’t be available in
IAM Identity Center for mapping.

###### Topics

- [Enable attributes for access control](enable-abac.md "enable-abac.md")
- [Select your attributes for
  access control](configure-abac-attributes.md "configure-abac-attributes.md")
- [Disable attributes for access control](disable-abac.md "disable-abac.md")
