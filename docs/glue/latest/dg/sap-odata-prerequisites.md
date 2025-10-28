# Prerequisites

Prior to initiating an AWS Glue job for data extraction from SAP OData using the SAP OData connection, complete the following prerequisites:

- The relevant SAP OData Service must be activated in the SAP system, ensuring the data source is available for consumption. If the OData service is not activated, the Glue job will not be able to access or extract data from SAP.
- Appropriate authentication mechanisms such as basic (custom) authentication or OAuth 2.0 must be configured in SAP to ensure that the AWS Glue job can successfully establish a connection with the SAP OData service.
- Configure IAM policies to grant the AWS Glue job appropriate permissions for accessing SAP, Secrets Manager, and other AWS resources involved in the process.
- If the SAP system is hosted within a private network, VPC connectivity must be configured to ensure that the AWS Glue job can securely communicate with SAP without exposing sensitive data over public internet.
  AWS Secrets Manager can be used to securely store sensitive information such as SAP credentials, which the AWS Glue job can dynamically retrieve at runtime. This approach eliminates the need to hard-code credentials, enhancing security and flexibility.

The following prerequisites provide step-by-step guidance on how to set up each component for a smooth integration between AWS Glue and SAP OData.

###### Topics

- [SAP OData activation](sap-odata-activation.md "sap-odata-activation.md")
- [IAM policies](sap-odata-configuring-iam-permissions.md "sap-odata-configuring-iam-permissions.md")
- [Connectivity / VPC Connection](sap-odata-connectivity-vpc-connection.md "sap-odata-connectivity-vpc-connection.md")
- [SAP Authentication](sap-odata-authentication.md "sap-odata-authentication.md")
- [AWS Secrets Manager to store your Auth secret](sap-odata-aws-secret-manager-auth-secret.md "sap-odata-aws-secret-manager-auth-secret.md")
