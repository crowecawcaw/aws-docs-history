

# DB cluster parameter group settings for Babelfish
<a name="babelfish-configuration"></a>

When you create an Aurora PostgreSQL DB cluster and choose **Turn on Babelfish**, a DB cluster parameter group is created for you automatically if you choose **Create new**. This DB cluster parameter group is based on the Aurora PostgreSQL DB cluster parameter group for the Aurora PostgreSQL version chosen for the install, for example, Aurora PostgreSQL version 14. It's named using the following general pattern: 

```
custom-aurora-postgresql14-babelfish-compat-3
```

You can change the following settings during the cluster creation process but some of these can't be changed once they're stored in the custom parameter group, so choose carefully:
+ Single database or Multiple databases
+ Default collation locale
+ Collation name
+ DB parameter group

To use an existing Aurora PostgreSQL DB cluster version 13 or higher parameter group, edit the group and set the `babelfish_status` parameter to `on`. Specify any Babelfish options before creating your Aurora PostgreSQL cluster. To learn more, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).

The following parameters control Babelfish preferences. Unless otherwise stated in the Description, parameters are modifiable. The default value is included in the description. To see the allowable values for any parameter, do as follows: 

**Note**  
When you associate a new DB parameter group with a DB instance, the modified static and dynamic parameters are applied only after the DB instance is rebooted. However, if you modify dynamic parameters in the DB parameter group after you associate it with the DB instance, these changes are applied immediately without a reboot.

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Parameter groups** from the navigation menu.

1. Choose the `default.aurora-postgresql14` DB cluster parameter group from the list.

1. Enter the name of a parameter in the search field. For example, enter `babelfishpg_tsql.default_locale` in the search field to display this parameter and its default value and allowable settings. 
**Note**  
Babelfish for Aurora PostgreSQL global databases works in secondary regions only if the following parameters are turned on in those regions.


| Parameter | Description | Apply Type | Is Modifiable | 
| --- | --- | --- | --- | 
| babelfishpg\_tds.tds\_default\_numeric\_scale | Sets the default scale of numeric type to be sent in the TDS column metadata if the engine doesn't specify one. (Default: 8) (Allowable: 0–38)  | dynamic | true | 
| babelfishpg\_tds.tds\_default\_numeric\_precision | An integer that sets the default precision of numeric type to be sent in the TDS column metadata if the engine doesn't specify one. (Default: 38) (Allowable: 1–38) | dynamic | true | 
| babelfishpg\_tds.tds\_default\_packet\_size | An integer that sets the default packet size for connecting SQL Server clients. (Default: 4096) (Allowable: 512–32767) | dynamic | true | 
| babelfishpg\_tds.tds\_default\_protocol\_version | An integer that sets a default TDS protocol version for connecting clients. (Default: DEFAULT) (Allowable: TDSv7.0, TDSv7.1, TDSv7.1.1, TDSv7.2, TDSv7.3A, TDSv7.3B, TDSv7.4, DEFAULT) | dynamic | true | 
| babelfishpg\_tds.default\_server\_name | A string that identifies the default name of the Babelfish server. (Default: Microsoft SQL Server) (Allowable: null) | dynamic | true | 
| babelfishpg\_tds.tds\_debug\_log\_level | An integer that sets the logging level in TDS; 0 turns off logging. (Default: 1) (Allowable: 0, 1, 2, 3) | dynamic | true | 
| babelfishpg\_tds.listen\_addresses | A string that sets the host name or IP address or addresses to listen for TDS on. This parameter can't be modified after the Babelfish DB cluster is created. (Default: \* ) (Allowable: null)  | – | false | 
| babelfishpg\_tds.port | An integer that specifies the TCP port used for requests in SQL Server syntax. (Default: 1433) (Allowable: 1–65535) | static | true | 
| babelfishpg\_tds.tds\_ssl\_encrypt | A boolean that turns encryption on (0) or off (1) for data traversing the TDS listener port. For detailed information about using SSL for client connections, see [Babelfish SSL settings and client connections](#babelfish-ssl). (Default: 0) (Allowable: 0, 1) | dynamic | true | 
| babelfishpg\_tds.tds\_ssl\_max\_protocol\_version | A string that specifies the highest SSL/TLS protocol version to use for the TDS session. (Default: 'TLSv1.2') (Allowable: 'TLSv1', 'TLSv1.1', 'TLSv1.2') | dynamic | true | 
| babelfishpg\_tds.tds\_ssl\_min\_protocol\_version | A string that specifies the minimum SSL/TLS protocol version to use for the TDS session. (Default: 'TLSv1.2' from Aurora PostgreSQL version 16, 'TLSv1' for versions older than Aurora PostgreSQL version 16) (Allowable: 'TLSv1', 'TLSv1.1', 'TLSv1.2') | dynamic | true | 
| babelfishpg\_tds.unix\_socket\_directories | A string that identifies the TDS server Unix socket directory. This parameter can't be modified after the Babelfish DB cluster is created. (Default: /tmp) (Allowable: null) | – | false | 
| babelfishpg\_tds.unix\_socket\_group | A string that identifies the TDS server Unix socket group. This parameter can't be modified after the Babelfish DB cluster is created. (Default: rdsdb) (Allowable: null) | – | false | 
| babelfishpg\_tsql.default\_locale | A string that specifies the default locale used for Babelfish collations. The default locale is the locale only and doesn't include any qualifiers.<br />Set this parameter when you provision a Babelfish DB cluster. After the DB cluster is provisioned, changes to this parameter are ignored. (Default: en\_US) (Allowable: See [tables](babelfish-collations.md))  | static | true | 
| babelfishpg\_tsql.migration\_mode | A non-modifiable list that specifies support for single- or multiple user databases. Set this parameter when you provision a Babelfish DB cluster. After the DB cluster is provisioned, you can't modify this parameter's value. (Default: multi-db from Aurora PostgreSQL version 16, single-db for versions older than Aurora PostgreSQL version 16) (Allowable: single-db, multi-db,null) | static | true | 
| babelfishpg\_tsql.server\_collation\_name | A string that specifies the name of the collation used for server-level actions. Set this parameter when you provision a Babelfish DB cluster. After the DB cluster is provisioned, don't modify the value of this parameter. (Default: bbf\_unicode\_general\_ci\_as) (Allowable: See [tables](babelfish-collations.md)) | static | true | 
| babelfishpg\_tsql.version | A string that sets the output of @@VERSION variable. Don't modify this value for Aurora PostgreSQL DB clusters. (Default: null) (Allowable: default) | dynamic | true | 
| rds.babelfish\_status | A string that sets the state of Babelfish functionality. When this parameter is set to `datatypesonly`, Babelfish is turned off but SQL Server data types are still available. (Default: off) (Allowable: on, off, datatypesonly) | static | true | 
| unix\_socket\_permissions | An integer that sets the TDS server Unix socket permissions. This parameter can't be modified after the Babelfish DB cluster is created. (Default: 0700) (Allowable: 0–511) | – | false | 

## Babelfish SSL settings and client connections
<a name="babelfish-ssl"></a>

To require SSL/TLS connections to your Babelfish for Aurora PostgreSQL DB cluster, use the `rds.force_ssl` parameter.
+ To require SSL/TLS connections, set the `rds.force_ssl` parameter value to 1 (on).
+ To turn off required SSL/TLS connections, set the `rds.force_ssl` parameter value to 0 (off).

The default value of this parameter depends on the Aurora PostgreSQL version:
+ For Aurora PostgreSQL versions 17 and later: The default value is 1 (on).
+ For Aurora PostgreSQL versions 16 and older: The default value is 0 (off).

**Note**  
When you perform a major version upgrade from Aurora PostgreSQL version 16 or earlier to version 17 or later, the default value of the parameter changes from 0 (off) to 1 (on). This change may cause connectivity failures for applications that are not configured for SSL. You can revert to the previous default behavior by setting this parameter to 0 (off).

For driver-specific details, see [Connecting to a Babelfish DB cluster](babelfish-connect.md).

When a client connects to the TDS port (default `1433`), Babelfish compares the Secure Sockets Layer (SSL) setting sent during the client handshake to the Babelfish SSL parameter setting (`tds_ssl_encrypt`). Babelfish then determines if a connection is allowed. If a connection is allowed, encryption behavior is either enforced or not, depending on your parameter settings and the support for encryption offered by the client.

The table following shows how Babelfish behaves for each combination.


| Client SSL setting | Babelfish SSL setting | rds.force\_ssl | Connection allowed? | Value returned to client | 
| --- | --- | --- | --- | --- | 
| ENCRYPT\_ON | Any | Any | Allowed, the entire connection is encrypted | ENCRYPT\_ON | 
| ENCRYPT\_OFF | tds\_ssl\_encrypt=1 | Any | Allowed, the entire connection is encrypted | ENCRYPT\_REQ | 
| ENCRYPT\_OFF | tds\_ssl\_encrypt=0 | rds.force\_ssl=0 | Allowed, the login packet is encrypted | ENCRYPT\_OFF | 
| ENCRYPT\_OFF | tds\_ssl\_encrypt=0 | rds.force\_ssl=1 | No, connection closed | ENCRYPT\_OFF | 
| ENCRYPT\_NOT\_SUP | tds\_ssl\_encrypt=0 | rds.force\_ssl=0 | Yes | ENCRYPT\_NOT\_SUP | 
| ENCRYPT\_NOT\_SUP | tds\_ssl\_encrypt=1 | Any | No, connection closed  | ENCRYPT\_REQ | 
| ENCRYPT\_NOT\_SUP | tds\_ssl\_encrypt=0 | rds.force\_ssl=1 | No, connection closed | ENCRYPT\_NOT\_SUP | 
| ENCRYPT\_CLIENT\_CERT | Any | Any | No, connection closed | Unsupported | 