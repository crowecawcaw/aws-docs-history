# Create credentials for programmatic access to Amazon Keyspaces

To provide users and applications with credentials for programmatic access to
Amazon Keyspaces resources, you can do either of the following:

- Create service-specific credentials that are similar to the traditional
  username and password that Cassandra uses for authentication and access
  management. AWS service-specific credentials are associated with a
  specific AWS Identity and Access Management (IAM) user and can only be used for the service they
  were created for. For more information, see
  [Using IAM with Amazon Keyspaces (for Apache Cassandra)](../../../IAM/latest/UserGuide/id_credentials_keyspaces.md "../../../IAM/latest/UserGuide/id_credentials_keyspaces.md") in the IAM User Guide.

###### Warning

IAM users have long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed.

- For enhanced security, we recommend to create IAM
  identities that are used across all AWS services and use temporary credentials. The Amazon Keyspaces SigV4
  authentication plugin for Cassandra client drivers enables you to
  authenticate calls to Amazon Keyspaces using IAM access keys instead of user name and
  password. To learn more about how the Amazon Keyspaces SigV4 plugin enables [IAM users, roles, and federated
  identities](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") to authenticate in Amazon Keyspaces API requests, see [AWS Signature Version 4 process (SigV4)](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").

You can download the SigV4 plugins from the following locations.

    + Java: [https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin").
    + Node.js: [https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin").
    + Python: [https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin").
    + Go: [https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin").

For code samples that show how to establish connections using the SigV4 authentication
plugin, see [Using a Cassandra client driver to access
Amazon Keyspaces programmatically](programmatic.md "programmatic.md").

###### Topics

- [Create service-specific credentials](programmatic.credentials.md "programmatic.credentials.md")
- [Create IAM credentials for AWS authentication](access.md "access.md")
