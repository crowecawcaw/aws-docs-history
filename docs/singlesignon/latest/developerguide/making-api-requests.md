# Making API Requests

IAM Identity Center SCIM implementation supports the bearer HTTP authentication scheme. An access
token (also known as a bearer token) must be passed in the HTTP Authorization header of each
request to your SCIM endpoint. See [Considerations for using automatic provisioning](../userguide/provision-automatically.md#auto-provisioning-considerations "../userguide/provision-automatically.md#auto-provisioning-considerations") in the
_IAM Identity Center User Guide_ for instructions on generating and retrieving your
access token.

Other authentication schemes described in the SCIM specifications are not supported at
this time.
