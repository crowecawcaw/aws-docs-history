

# EUCSEC06 BP02 Strengthen SAML federation to reduce security risks
<a name="eucsec06-bp02"></a>

 To help prevent an opportunity for SAML assertions to be misused when using Certificate Based Authentication by incorrectly associating with Active Directory user security objects, strong mapping should be used. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-26"></a>

 Use strong mapping between SAML IdP and Active Directory. You can use certificate-based authentication (CBA) with Amazon WorkSpaces, which you can use to remove the user password prompt when using a SAML 2.0 identity provider. To establish a strong mapping between Active Directory users and SAML assertions, ObjectSid must be configured within the SAML assertion. CBA will fail if the attribute does not match the Active Directory security identifier (SID) for the user in the `SAML\_Subject NameID`. For more detail, see [Certificate-based authentication](https://docs.aws.amazon.com/workspaces/latest/adminguide/certificate-based-authentication.html). 