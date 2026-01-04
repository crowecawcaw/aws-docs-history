# Using Amazon RDS for Db2 and IBM Db2 LUW as a target for AWS DMS

You can migrate data to an Amazon RDS for Db2 or an on-premises Db2 database from a Db2 LUW
database using AWS Database Migration Service (AWS DMS).

For information about versions of Db2 LUW that AWS DMS supports as a target,
see [Targets for AWS DMS](CHAP_Introduction.md "CHAP_Introduction.md").

You can use Secure Sockets Layer (SSL) to encrypt connections between your Db2 LUW
endpoint and the replication instance. For more information about using SSL with a Db2 LUW
endpoint, see [Using SSL with AWS Database Migration Service](CHAP_Security.md "CHAP_Security.md").

## Limitations when using Db2 LUW as a

target for AWS DMS

The following limitations apply when using Db2 LUW database as a target for AWS DMS. For
limitations on using Db2 LUW as a source, see
[Limitations when using Db2 LUW as a
source for AWS DMS](CHAP_Source.md#CHAP_Source.DB2.Limitations "CHAP_Source.md#CHAP_Source.DB2.Limitations").

- AWS DMS only supports Db2 LUW as a target when the source is either Db2 LUW or Db2 for z/OS.
- Using Db2 LUW as a target doesn't support replications with full LOB mode.
- Using Db2 LUW as a target doesn't support the XML datatype in the full load phase. This is a limitation
  of the IBM dbload utility. For more information, see
  [The dbload utility](https://www.ibm.com/docs/en/informix-servers/14.10?topic=utilities-dbload-utility "https://www.ibm.com/docs/en/informix-servers/14.10?topic=utilities-dbload-utility")
  in the _IBM Informix Servers_ documentation.
- AWS DMS truncates BLOB fields with values corresponding to the double quote character (").
  This is a limitation of the IBM dbload utility.
- AWS DMS does not support the parallel full load option when migrating to a Db2
  LUW target in DMS version 3.5.3. This option is available from DMS version 3.5.4
  or later.

## Endpoint settings when

using Db2 LUW as a target for AWS DMS

You can use endpoint settings to configure your Db2 LUW target database similar to using
extra connection attributes. You specify the settings when you create the target
endpoint using the AWS DMS console, or by using the `create-endpoint` command in the
[AWS CLI](../../../cli/latest/reference/dms/index.md "../../../cli/latest/reference/dms/index.md"), with the
`--ibm-db2-settings '{"`EndpointSetting"`:
 `"value"`, `...`}'` JSON syntax.

The following table shows the endpoint settings that you can use with
Db2 LUW as a target.

| Name              | Description                                                                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `KeepCsvFiles`    | If true, AWS DMS saves any .csv files to the Db2 LUW target that were used to replicate data. DMS uses these<br>files for analysis and troubleshooting..                    |
| `LoadTimeout`     | The amount of time (in milliseconds) before AWS DMS times out operations performed by DMS on the Db2 target.<br>The default value is 1200 (20 minutes).                     |
| `MaxFileSize`     | Specifies the maximum size (in KB) of .csv files used to transfer data to Db2 LUW.                                                                                          |
| `WriteBufferSize` | The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk<br>on the DMS replication instance. The default value is 1024 (1 MB). |
