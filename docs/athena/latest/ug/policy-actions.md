# Control access through JDBC and ODBC

connections

To gain access to AWS services and resources, such as Athena and the Amazon S3 buckets,
provide the JDBC or ODBC driver credentials to your application. If you are using the
JDBC or ODBC driver, ensure that the IAM permissions policy includes all of the
actions listed in [AWS managed policy:
AWSQuicksightAthenaAccess](managed-policies.md#awsquicksightathenaaccess-managed-policy "managed-policies.md#awsquicksightathenaaccess-managed-policy").

Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Authentication

methods

The Athena JDBC and ODBC drivers support SAML 2.0-based authentication, including
the following identity providers:

- Active Directory Federation Services (AD FS)
- Azure Active Directory (AD)
- Okta
- PingFederate

For more information, see the installation and configuration guides for the
respective drivers, downloadable in PDF format from the [JDBC](connect-with-jdbc.md "connect-with-jdbc.md") and
[ODBC](connect-with-odbc.md "connect-with-odbc.md")
driver pages. For additional related information, see the following:

- [Enable federated access to the Athena API](access-federation-saml.md "access-federation-saml.md")
- [Use Lake Formation and JDBC or ODBC drivers for
  federated access to Athena](security-athena-lake-formation-jdbc.md "security-athena-lake-formation-jdbc.md")
- [Configure single sign-on using ODBC, SAML 2.0, and the Okta
  Identity Provider](okta-saml-sso.md "okta-saml-sso.md")

For information about the latest versions of the JDBC and ODBC drivers and their
documentation, see [Connect to Amazon Athena with JDBC](connect-with-jdbc.md "connect-with-jdbc.md") and [Connect to Amazon Athena with ODBC](connect-with-odbc.md "connect-with-odbc.md").
