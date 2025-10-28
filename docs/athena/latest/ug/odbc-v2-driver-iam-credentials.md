# IAM credentials

You can use your IAM credentials to connect to Amazon Athena with the ODBC driver using the
connection string parameters described in this section.

## Authentication

type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                              |
| -------------------------- | ------------------ | ----------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AuthenticationType         | Required           | `IAM Credentials` | `AuthenticationType=IAM Credentials;`                      | ## User ID Your AWS Access Key ID. For more information about access keys, see [AWS security credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md")in the _IAM User Guide_.                                                                                    |
| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                              |
| ---                        | ---                | ---               | ---                                                        |
| UID                        | Required           | `none`            | `UID=AKIAIOSFODNN7EXAMPLE;`                                | ## Password Your AWS secret key id. For more information about access keys, see [AWS security credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md")in the _IAM User Guide_.                                                                                   |
| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                              |
| ---                        | ---                | ---               | ---                                                        |
| PWD                        | Required           | `none`            | `PWD=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKE;`             | ## Session token If you use temporary AWS credentials, you must specify a session token. For information about temporary credentials, see [Temporary security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") in the _IAM User Guide_. |
| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                              |
| ---                        | ---                | ---               | ---                                                        |
| SessionToken               | Optional           | `none`            | `SessionToken=AQoDYXdzEJr...<remainder of session token>;` |
