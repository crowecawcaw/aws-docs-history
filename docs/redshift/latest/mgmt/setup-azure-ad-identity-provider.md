Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting up JDBC or ODBC single

sign-on authentication

You can leverage external identity providers (IdPs) to authenticate and authorize
users accessing your Amazon Redshift cluster, simplifying user management and enhancing
security. This enables centralized user management, role-based access control, and
auditing capabilities across multiple services. Common use cases include
streamlining authentication for diverse user groups, enforcing consistent access
policies, and meeting regulatory requirements.

The following pages guide you through configuring IdP integration with your
Redshift cluster. For more information about configuring AWS as a service provider
for the IdP, see [Configuring Your SAML 2.0 IdP with Relying Party Trust and Adding
Claims](../../../IAM/latest/UserGuide/id_roles_providers_create_saml_relying-party.md#saml_relying-party "../../../IAM/latest/UserGuide/id_roles_providers_create_saml_relying-party.md#saml_relying-party") in the _IAM User Guide_.
