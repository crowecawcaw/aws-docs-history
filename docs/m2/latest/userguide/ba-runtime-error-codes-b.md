

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe Runtime Error Codes related to Blusam
<a name="ba-runtime-error-codes-b"></a>

Blusam error codes, prefixed with `BA-B`.


| Key | Severity | Text | Additional details | 
| --- | --- | --- | --- | 
| BA-B0001 | Warn | Invalid value for bluesam.disabled. Only true is supported to disable Blusam. The default behavior is that Bluesam is enabled. Set bluesam.disabled: true in your configuration if you want to disable Bluesam. Remove the property to keep Blusam enabled. |  | 
| BA-B0011 | Warn | Bluesam Cache will not be enabled. Set bluesam.cache: ehcache to use EhCache, or bluesam.cache: redis to use Redis. Any other value will disable Bluesam cache. |  | 
| BA-B0021 | Fatal | Blusam is active but blusam datasource is not defined in the configuration. Set datasource.blusamDs configuration keys (subkeys url, username, password...) or use an AWS secret. | See [Blusam configuration](ba-shared-blusam.md#ba-shared-blusam-configuration) | 
| BA-B2000 | Warn | Index with id %s exceeds cache %s memory limits. Bypassing cache and persisting directly to database. | Informational: this is a deliberate size-limit bypass (not an OutOfMemoryError). The index is persisted directly to the database; no action required. | 
| BA-B2001 | Warn | Could not add Index with id %s to cache %s. Bypassing cache and persisting directly to database. | Informational: the index is persisted directly to the database; no action required. | 
| BA-B2002 | Error | Unsupported operation: Page capacity calculation not supported | MetadataPersistence implementation does not support page capacity calculation | 
| BA-B2003 | Error | Couldn't commit indexes correctly on table. Verify that the persistence layer (database or Redis) is accessible and that the index table exists |  | 
| BA-B2004 | Error | The index was not found in persistence. Verify that the persistence layer (database or Redis) is accessible and that the index table exists |  | 
| BA-B2005 | Error | WriteBehind persistence thread interrupted. Check for unexpected thread interruption in the write-behind persistence layer. |  | 
| BA-B2006 | Error | Error processing write-behind batch. Verify the persistence layer (database or Redis) is accessible and operational. |  | 
| BA-B2007 | Error | Error while executing bulk read by filter query on dataset %s: %s. Verify the query syntax and that the persistence layer is accessible. |  | 
| BA-B2008 | Error | Invalid bulk read query: %s. Only SELECT queries with \* or id, record columns targeting the correct dataset are allowed. |  | 
| BA-B2009 | Error | Bulk read query is null. Provide a non-null SELECT query for bulk read operations. |  | 
| BA-B2010 | Error | Bulk read query contains multiple statements: %s. Only a single SELECT statement is allowed; remove semicolons and additional statements. |  | 
| BA-B2011 | Error | Bulk read query contains forbidden keyword: %s. DDL/DML keywords (INSERT, UPDATE, DELETE, DROP, etc.) are not allowed in bulk read queries. |  | 
| BA-B2012 | Error | Error while reading records by ids from cache for dataset %s: %s. Verify the cache (Redis/Ehcache) is accessible and operational. |  | 
| BA-B2013 | Error | Dataset %s is not a Large KSDS. Verify the listcat JSON has isLargeKSDS set to true and the dataset was created with Large KSDS metadata. |  | 
| BA-B2014 | Error | Error building indexes for dataset %s. Check database connectivity and disk space. Retry the loading operation. |  | 