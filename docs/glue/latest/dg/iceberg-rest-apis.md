# AWS Glue REST APIs for Apache Iceberg specifications

This section contains specifications about the AWS Glue Iceberg REST catalog and AWS Glue
extension APIs, and considerations when using these APIs.

API requests to the AWS Glue Data Catalog endpoints are authenticated using AWS Signature Version 4
(SigV4). See [AWS
Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") section to learn more about AWS SigV4.

When accessing the AWS Glue service endpoint, and AWS Glue metadata, the application assumes an
IAM role which requires `glue:getCatalog` IAM action.

Access to the Data Catalog, and its objects can be managed using IAM, Lake Formation, or Lake Formation hybrid mode permissions.

Federated catalogs in the Data Catalog have Lake Formation registered data locations. Lake Formation works with the
Data Catalog to provide database-style permissions to manage user access to Data Catalog objects.

You can use IAM, AWS Lake Formation, or Lake Formation hybrid mode permissions to manage access to the default
Data Catalog and its objects.

To create, insert, or delete data in Lake Formation managed objects, you must set up specific
permissions for the IAM user or role.

- CREATE_CATALOG – Required to create catalogs
- CREATE_DATABASE – Required to create databases
- CREATE_TABLE – Required to create tables
- DELETE – Required to delete data from a table
- DESCRIBE – Required to read metadata
- DROP – Required to drop/delete a table or database
- INSERT – Needed when the principal needs to insert data into a table
- SELECT – Needed when the principal needs to select data from a table
  For more information, see [Lake Formation permissions
  reference](../../../lake-formation/latest/dg/lf-permissions-reference.md "../../../lake-formation/latest/dg/lf-permissions-reference.md") in the AWS Lake Formation Developer Guide.

General information| **Operation name** | GetConfig |
| **Type** | Iceberg REST Catalog API |
| **REST path** | GET /iceberg/v1/config |
| **IAM action** | glue:GetCatalog |
| **Lake Formation permissions** | Not applicable |
| **CloudTrail event** | glue:GetCatalog |
| **Open API definition** | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L67 |

###### **Considerations and limitations**

- The `warehouse` query parameter must be set to the AWS Glue catalog ID. If not
  set, the root catalog in the current account is used to return the response. For more
  information, see [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters").

General information| **Operation name** | GetCatalog |
| **Type** | AWS Glue extension API |
| **REST path** | GET/extensions/v1/catalogs/{catalog} |
| **IAM action** | glue:GetCatalog |
| **Lake Formation permissions** | DESCRIBE |
| **CloudTrail event** | glue:GetCatalog |
| **Open API definition** | https://github.com/awslabs/glue-extensions-for-iceberg/blob/main/glue-extensions-api.yaml#L40 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.

General information| **Operation name** | ListNamespaces |
| **Type** | Iceberg REST Catalog API |
| **REST path** | GET/iceberg/v1/catalogs/{catalog}/namespaces |
| **IAM action** | glue:GetDatabase |
| **Lake Formation permissions** | ALL, DESCRIBE, SELECT |
| **CloudTrail event** | glue:GetDatabase |
| **Open API definition** | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L205 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- Only namespaces of the next level is displayed. To list namespaces in deeper levels,
  specify the nested catalog ID in the catalog path parameter.

General information| **Operation name** | CreateNamespace |
| **Type** | Iceberg REST Catalog API |
| **REST path** | POST/iceberg/v1/catalogs/{catalog}/namespaces |
| **IAM action** | glue:CreateDatabase |
| **Lake Formation permissions** | ALL, DESCRIBE, SELECT |
| **CloudTrail event** | glue:CreateDatabase |
| **Open API definition** | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L256 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- Only single level namespace can be created. To create a multi-level namespace, you must iteratively create each level, and connect to the level using the catalog path parameter.

General information| **Operation name** | StartCreateNamespaceTransaction |
| **Type** | AWS Glue extensions API |
| **REST path** | POST/extensions/v1/catalogs/{catalog}/namespaces |
| **IAM action** | glue:CreateDatabase |
| **Lake Formation permissions** | ALL, DESCRIBE, SELECT |
| **CloudTrail event** | glue:CreateDatabase |
| **Open API definition** | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L256 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can create only single-level namespace. To create a multi-level namespaces, you
  must iteratively create each level, and connect to the level using the catalog path
  parameter.
- The API is asynchronous, and returns a transaction ID that that you can use for tracking using the `CheckTransactionStatus` API call.
- You can call this API, only if the `GetCatalog` API call contains the
  parameter `use-extensions=true` in the response.

General information| **Operation name** | LoadNamespaceMetadata |
| **Type** | Iceberg REST Catalog API |
| **REST path** | GET/iceberg/v1/catalogs/{catalog}/namespaces/{ns} |
| **IAM action** | glue:GetDatabase |
| **Lake Formation permissions** | ALL, DESCRIBE, SELECT |
| **CloudTrail event** | glue:GetDatabase |
| **Open API definition** | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L302 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.

General information| **Operation name** | UpdateNamespaceProperties |
| **Type** | Iceberg REST Catalog API |
| **REST path** | POST /iceberg/v1/catalogs/{catalog}/namespaces/{ns}/properties |
| **IAM action** | glue:UpdateDatabase |
| **Lake Formation permissions** | ALL, ALTER |
| **CloudTrail event** | glue:UpdateDatabase |
| **Open API definition** | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L400 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.

General information| **Operation name** | DeleteNamespace |
| **Type** | Iceberg REST Catalog API |
| **REST path** | DELETE/iceberg/v1/catalogs/{catalog}/namespces/{ns} |
| **IAM action** | glue:DeleteDatabase |
| **Lake Formation permissions** | ALL, DROP |
| **CloudTrail event** | glue:DeleteDatabase |
| **Open API definition** | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L365 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- If there are objects in the database, the operation will fail.
- The API is asynchronous, and returns a transaction ID that that you can use for tracking using the `CheckTransactionStatus` API call.
- The API can only be used if
  the `GetCatalog` API call indicates `use-extensions=true` in
  response.

General information| **Operation name** | StartDeleteNamespaceTransaction |
| **Type** | AWS Glue extensions API |
| **REST path** | DELETE /extensions/v1/catalogs/{catalog}/namespces/{ns} |
| **IAM action** | glue:DeleteDatabase |
| **Lake Formation permissions** | ALL, DROP |
| **CloudTrail event** | glue:DeleteDatabase |
| **Open API definition** | https://github.com/awslabs/glue-extensions-for-iceberg/blob/main/glue-extensions-api.yaml#L85 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify a only single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- If there are objects in the database, the operation will fail.
- The API is asynchronous, and returns a transaction ID that that you can use for tracking using the `CheckTransactionStatus` API call.
- The API can only be used if
  the `GetCatalog` API call indicates `use-extensions=true` in
  response.

General information| **Operation name** | ListTables |
| **Type** | Iceberg REST Catalog API |
| **REST path** | GET /iceberg/v1/catalogs/{catalog}/namespaces/{ns}/tables |
| **IAM action** | glue:GetTables |
| **Lake Formation permissions** | ALL, SELECT, DESCRIBE |
| **CloudTrail event** | glue:GetTables |
| **Open API definition** | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L463 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- All tables including non-Iceberg tables will be listed. To determine if a table can be loaded as an Iceberg table or not, call `LoadTable` operation.

General information| **Operation name** | CreateTable |
| **Type** | Iceberg REST Catalog API |
| **REST path** | GET /iceberg/v1/catalogs/{catalog}/namespaces/{ns}/tables |
| **IAM action** | glue:CreateTable |
| **Lake Formation permissions** | ALL, CREATE_TABLE |
| **CloudTrail event** | glue:CreateTable |
| **Open API definition** | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L497 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- `CreateTable` with staging is not supported. If the
  `stageCreate` query parameter is specified, the operation will fail.This
  means operation like `CREATE TABLE AS SELECT` is not supported, and you can
  use a combination of `CREATE TABLE` and `INSERT INTO` as a
  workaround.
- The
  `CreateTable` API operation doesn't support the option `state-create =
TRUE`.

General information| **Operation name** | CreateTable |
| **Type** | AWS Glue extensions API |
| **REST path** | POST/extensions/v1/catalogs/{catalog}/namespaces/{ns}/tables |
| **IAM action** | glue:CreateTable |
| **Lake Formation permissions** | ALL, CREATE_TABLE |
| **CloudTrail event** | glue:CreateTable |
| **Open API definition** | https://github.com/awslabs/glue-extensions-for-iceberg/blob/main/glue-extensions-api.yaml#L107 |

###### **Considerations and limitations**

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- `CreateTable` with staging is not supported. If the `stageCreate` query parameter is specified, the operation will fail.This means operation like `CREATE TABLE AS SELECT` is not supported, and user should use a combination of `CREATE TABLE` and `INSERT INTO` to workaround.
- The API is asynchronous, and returns a transaction ID that that you can use for tracking using the `CheckTransactionStatus` API call.
- The API can only be used if
  the `GetCatalog` API call indicates `use-extensions=true` in
  response.

General information| Operation name | LoadTable |
| Type | Iceberg REST Catalog API |
| REST path | GET /iceberg/v1/catalogs/{catalog}/namespaces/{ns}/tables/{table} |
| IAM action | glue:GetTable |
| Lake Formation permissions | ALL, SELECT, DESCRIBE |
| CloudTrail event | glue:GetTable |
| Open API definition | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L616 |

###### Considerations

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- `CreateTable` with staging is not supported. If the `stageCreate` query parameter is specified, the operation will fail.This means operation like `CREATE TABLE AS SELECT` is not supported, and user should use a combination of `CREATE TABLE` and `INSERT INTO` to workaround.
- The API is asynchronous, and returns a transaction ID that that you can use for tracking using the `CheckTransactionStatus` API call.
- The API can only be used if
  the `GetCatalog` API call indicates `use-extensions=true` in
  response.

General information| Operation name | LoadTable |
| Type | AWS Glue extensions API |
| REST path | GET /extensions/v1/catalogs/{catalog}/namespaces/{ns}/tables/{table} |
| IAM action | glue:GetTable |
| Lake Formation permissions | ALL, SELECT, DESCRIBE |
| CloudTrail event | glue:GetTable |
| Open API definition | https://github.com/awslabs/glue-extensions-for-iceberg/blob/main/glue-extensions-api.yaml#L134 |

###### Considerations

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- Only `all` mode is supported for snapshots query parameter.
- Compared to `LoadTable` API, the `ExtendedLoadTable` API differs in the following ways:
  - Doesn't strictly enforce that all the fields to be available.
  - provides the following additional parameters in the config field of the
    response:

  | Additional parameters                      | Config key                                                                                                                                            | Description |
  | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
  | aws.server-side-capabilities.scan-planning | Indiactes if the table can be scanned using the PreparePlan table<br>and PlanTable APIs.                                                              |
  | aws.server-side-capabilities.data-commit   | Indicates if the table can be committed using the StartUpdateTable<br>transaction.                                                                    |
  | aws.glue.staging.location                  | Used for server side scan planning or data commit, a<br>service-managed staging location that can be used for engine to write<br>temporary data files |
  | aws.glue.staging.access-key-id             | Used for server side scan planning or data commit, a part of the<br>temporary AWS credentials to access the service-managed staging<br>location       |
  | aws.glue.staging.secret-access-key         | Used for server side scan planning or data commit, a part of the<br>temporary AWS credentials to access the service-managed staging<br>location.      |
  | aws.glue.staging.session-token             | Used for server side scan planning or data commit, a part of the<br>temporary AWS credentials to access the service-managed staging<br>location.      |
  | aws.glue.staging.expiration-ms             | Used for server side scan planning or data commit, expiration time<br>of the credentials to access the service-managed staging.<br>location.          |
  | aws.glue.staging.data-transfer-role-arn    | Used for server side scan planning or data commit, an IAM role<br>that can be assumed to taccess the service-managed staging<br>location.             |

General information| Operation name | PreplanTable |
| Type | AWS Glue extensions API |
| REST path | POST /extensions/v1/catalogs/{catalog}/namespaces/{ns}/tables/{table}/preplan |
| IAM action | glue:GetTable |
| Lake Formation permissions | ALL, SELECT, DESCRIBE |
| CloudTrail event | glue:GetTable |
| Open API definition | https://github.com/awslabs/glue-extensions-for-iceberg/blob/main/glue-extensions-api.yaml#L211 |

###### Considerations

- The catalog path parameter should follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- Caller of this API should always determine if there are remaining results to fetch based on the page token. A response with empty page item but a pagination token is possible if the server side is still processing but is not able to produce any result in the given response time.
- You can use this API only if the `ExtendedLoadTable` API response contains `aws.server-side-capabilities.scan-planning=true`.

General information| Operation name | PlanTable |
| Type | AWS Glue extensions API |
| REST path | POST /extensions/v1/catalogs/{catalog}/namespaces/{ns}/tables/{table}/plan |
| IAM action | glue:GetTable |
| Lake Formation permissions | ALL, SELECT, DESCRIBE |
| CloudTrail event | glue:GetTable |
| Open API definition | https://github.com/awslabs/glue-extensions-for-iceberg/blob/main/glue-extensions-api.yaml#L243 |

###### Considerations

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- Caller of this API should always determine if there are remaining results to fetch based on the page token. A response with empty page item but a pagination token is possible if the server side is still processing but is not able to produce any result in the given response time.
- You can use this API only if the `ExtendedLoadTable` API response contains `aws.server-side-capabilities.scan-planning=true`.

General information| Operation name | TableExists |
| Type | Iceberg REST Catalog API |
| REST path | HEAD/iceberg/v1/catalogs/{catalog}/namespaces/{ns}/tables/{table} |
| IAM action | glue:GetTable |
| Lake Formation permissions | ALL, SELECT, DESCRIBE |
| CloudTrail event | glue:GetTable |
| Open API definition | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L833 |

###### Considerations

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.

General information| Operation name | UpdateTable |
| Type | Iceberg REST Catalog API |
| REST path | POST /iceberg/v1/catalogs/{catalog}/namespaces/{ns}/tables/{table} |
| IAM action | glue:UpdateTable |
| Lake Formation permissions | ALL, ALTER |
| CloudTrail event | glue:UpdateTable |
| Open API definition | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L677 |

###### Considerations

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.

General information| Operation name | StartUpdateTableTransaction |
| Type | AWS Glue extension API |
| REST path | POST/extensions/v1/catalogs/{catalog}/namespaces/{ns}/tables/{table} |
| IAM action | glue:UpdateTable |
| Lake Formation permissions | ALL, ALTER |
| CloudTrail event | glue:UpdateTable |
| Open API definition | https://github.com/awslabs/glue-extensions-for-iceberg/blob/main/glue-extensions-api.yaml#L154 |

###### Considerations

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- The API is asynchronous, and returns a transaction ID that that you can use for
  tracking using the `CheckTransactionStatus` API call.
- A `RenamTable` operation can also be performed through this API. When that happens, the caller must also ahve glue:CreateTable or LakeFormation CREATE_TABLE permission for the table to be renamed to.
- You can use this API only if the `ExtendedLoadTable` API response contains `aws.server-side-capabilities.scan-planning=true`.

General information| Operation name | DeleteTable |
| Type | Iceberg REST Catalog API |
| REST path | DELETE/iceberg/v1/catalogs/{catalog}/namespaces/{ns}/tables/{table} |
| IAM action | glue:DeleteTable |
| Lake Formation permissions | ALL, DROP |
| CloudTrail event | glue:DeleteTable |
| Open API definition | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L793 |

###### Considerations

- The catalog path parameter should follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- `DeleteTable` API operation supports a purge option. When purge is set to `true`, the table data is
  deleted, otherwise data is not deleted. For tables in Amazon S3, the operation does not delete
  table data. The operation fails when table is stored in Amazon S3, and `purge =
TRUE,` .

For tables stored in Amazon Redshift managed storage, the operation will delete table data, similar to `DROP TABLE`behavior in Amazon Redshift.
The operation fails when table is stored in Amazon Redshift and `purge = FALSE`.

- `purgeRequest=true` is not supported.

General information| Operation name | StartDeleteTableTransaction |
| Type | AWS Glue extensions API |
| REST path | DELETE /extensions/v1/catalogs/{catalog}/namespaces/{ns}/tables/{table} |
| IAM action | glue:DeleteTable |
| Lake Formation permissions | ALL, DROP |
| CloudTrail event | glue:DeleteTable |
| Open API definition | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml#L793 |

###### Considerations

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
- You can specify only a single-level namespace in the REST Path parameter. For more in
  formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param "connect-glu-iceberg-rest.md#ns-path-param") section.
- `purgeRequest=false` is not supported.
- The API is asynchronous, and returns a transaction ID that can be tracked through `CheckTransactionStatus`.

General information| Operation name | CheckTransactionStatus |
| Type | AWS Glue extensions API |
| REST path | POST/extensions/v1/transactions/status |
| IAM action | The same permission as the action that initiates the transaction |
| Lake Formation permissions | The same permission as the action that initiates the transaction |
| Open API definition | https://github.com/awslabs/glue-extensions-for-iceberg/blob/main/glue-extensions-api.yaml#L273 |

###### Considerations

- The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters "connect-glu-iceberg-rest.md#prefix-catalog-path-parameters") section.
