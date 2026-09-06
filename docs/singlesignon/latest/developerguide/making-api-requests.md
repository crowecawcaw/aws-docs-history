

# Making API Requests
<a name="making-api-requests"></a>

IAM Identity Center SCIM implementation supports the bearer HTTP authentication scheme. An access token (also known as a bearer token) must be passed in the HTTP Authorization header of each request to your SCIM endpoint. See [Considerations for using automatic provisioning](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html#auto-provisioning-considerations) in the *IAM Identity Center User Guide* for instructions on generating and retrieving your access token.

Other authentication schemes described in the SCIM specifications are not supported at this time.