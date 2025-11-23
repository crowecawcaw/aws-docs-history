# Using a SAP ASE database as a target for

AWS Database Migration Service

You can migrate data to SAP Adaptive Server Enterprise (ASE)–formerly known as
Sybase–databases using AWS DMS, either from any of the supported database
sources.

For information about versions
of SAP ASE that AWS DMS supports as a target, see [Targets for AWS DMS](CHAP_Introduction.md "CHAP_Introduction.md").

## Prerequisites for using a SAP ASE

database as a target for AWS Database Migration Service

Before you begin to work with a SAP ASE database as a target for AWS DMS, make
sure that you have the following prerequisites:

- Provide SAP ASE account access to the AWS DMS user. This user must have
  read/write privileges in the SAP ASE database.
- In some cases, you might replicate to SAP ASE version 15.7 installed on an
  Amazon EC2 instance on Microsoft Windows that is configured with non-Latin
  characters (for example, Chinese). In such cases, AWS DMS requires SAP ASE
  15.7 SP121 to be installed on the target SAP ASE machine.

## Limitations when using a SAP ASE

database as a target for AWS DMS

The following limitations apply when using an SAP ASE database as a target for
AWS DMS:

- AWS DMS doesn't support tables that include fields with the following data
  types. Replicated columns with these data types show as null.
  - User-defined type (UDT)

## Endpoint settings when

using SAP ASE as a target for AWS DMS

You can use endpoint settings to configure your SAP ASE target database similar to using
extra connection attributes. You specify the settings when you create the target
endpoint using the AWS DMS console, or by using the `create-endpoint` command in the
[AWS CLI](../../../cli/latest/reference/dms/index.md "../../../cli/latest/reference/dms/index.md"), with the
`--sybase-settings '{"`EndpointSetting"`:
 `"value"`, `...`}'` JSON syntax.

The following table shows the endpoint settings that you can use with
SAP ASE as a target.

| Name                             | Description                                                                                                                                                                                                                                             |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Driver`                         | Set this attribute if you want to use TLS for versions of ASE<br>15.7 and higher.<br>Default value: `Adaptive Server Enterprise`<br>Example: `driver=Adaptive Server Enterprise<br>16.03.06;`<br>Valid values: `Adaptive Server Enterprise<br>16.03.06` |
| `AdditionalConnectionProperties` | Any additional ODBC connection parameters that you want to<br>specify.                                                                                                                                                                                  |

## Target data types for SAP ASE

The following table shows the SAP ASE database target data types that are
supported when using AWS DMS and the default mapping from AWS DMS data
types.

For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.md "CHAP_Reference.md").

| AWS DMS data types | SAP ASE data types                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------- |
| BOOLEAN            | BIT                                                                                           |
| BYTES              | VARBINARY (Length)                                                                            |
| DATE               | DATE                                                                                          |
| TIME               | TIME                                                                                          |
| TIMESTAMP          | If scale is => 0 and =< 6, then: BIGDATETIME<br>If scale is => 7 and =< 9, then: VARCHAR (37) |
| INT1               | TINYINT                                                                                       |
| INT2               | SMALLINT                                                                                      |
| INT4               | INTEGER                                                                                       |
| INT8               | BIGINT                                                                                        |
| NUMERIC            | NUMERIC (p,s)                                                                                 |
| REAL4              | REAL                                                                                          |
| REAL8              | DOUBLE PRECISION                                                                              |
| STRING             | VARCHAR (Length)                                                                              |
| UINT1              | TINYINT                                                                                       |
| UINT2              | UNSIGNED SMALLINT                                                                             |
| UINT4              | UNSIGNED INTEGER                                                                              |
| UINT8              | UNSIGNED BIGINT                                                                               |
| WSTRING            | VARCHAR (Length)                                                                              |
| BLOB               | IMAGE                                                                                         |
| CLOB               | UNITEXT                                                                                       |
| NCLOB              | TEXT                                                                                          |
