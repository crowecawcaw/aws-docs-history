# Connect Studio

JupyterLab notebooks to Lake Formation and Athena with trusted identity propagation
enabled

AWS Lake Formation and Amazon Athena work together to provide a comprehensive data lake solution with
fine-grained access control and serverless query capabilities. Lake Formation centralizes permissions
management for your data lake, while Athena provides interactive query services. When
integrated with trusted identity propagation, this combination enables data scientists to
access only the data they're authorized to see, with all queries and data access
automatically logged for compliance and auditing purposes. The following page provides
information and instructions on how to connect trusted identity propagation with
Amazon SageMaker Studio to Lake Formation and Athena

To connect Studio to Lake Formation and Athena with trusted identity propagation enabled,
ensure you have completed the following setups:

- [Setting up trusted identity propagation for
  Studio](trustedidentitypropagation-setup.md "trustedidentitypropagation-setup.md")
- [Create a Lake Formation
  role](../../../lake-formation/latest/dg/prerequisites-identity-center.md "../../../lake-formation/latest/dg/prerequisites-identity-center.md")
- [Connect Lake Formation with
  IAM Identity Center](../../../lake-formation/latest/dg/connect-lf-identity-center.md "../../../lake-formation/latest/dg/connect-lf-identity-center.md")
- Create Lake Formation resources:
  - [Database](../../../lake-formation/latest/dg/creating-database.md "../../../lake-formation/latest/dg/creating-database.md")
  - [Tables](../../../lake-formation/latest/dg/creating-tables.md "../../../lake-formation/latest/dg/creating-tables.md")

- [Create Athena
  workgroup](../../../athena/latest/ug/creating-workgroups.md "../../../athena/latest/ug/creating-workgroups.md")
  - Choose **AthenaSQL** for the engine
  - Choose **IAM Identity Center** for authentication method
  - Create a new service role
    - Ensure that the IAM Identity Center users have access to the query result location using
      Amazon S3 Access Grants

- [Granting database
  permissions using the named resource method](../../../lake-formation/latest/dg/granting-database-permissions.md "../../../lake-formation/latest/dg/granting-database-permissions.md")
