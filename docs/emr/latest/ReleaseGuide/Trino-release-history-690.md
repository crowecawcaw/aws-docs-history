

# Amazon EMR 6.9.0 - Trino release notes
<a name="Trino-release-history-690"></a>

## Amazon EMR 6.9.0 - Trino new features
<a name="Trino-release-history-features-690"></a>
+ To support long running queries, Trino now includes a fault-tolerant execution mechanism. Fault-tolerant execution mitigates query failures by retrying failed queries or their component tasks.

## Amazon EMR 6.9.0 - Trino changes
<a name="Trino-release-history-changes-690"></a>


**Amazon EMR 6.9.0 - Trino changes**  

| Type | Description | 
| --- | --- | 
| Upgrade | Trino Upgrade to 398  | 
| Upgrade | Support for Hadoop 3.3.3  | 
| Feature | Tardigrade support: Add support for exchange spooling on HDFS and Amazon S3.  | 
| Bug fix | When Trino Iceberg is used and Glue catalog is enabled, avoid adding metastore uri in `iceberg.properties.` | 

## Amazon EMR 6.9.0 - Trino known issues
<a name="Trino-release-history-known-690"></a>
+ For Amazon EMR release 6.9.0, Trino does not work on clusters enabled for Apache Ranger. If you need to use Trino with Ranger, contact [Support](https://console.aws.amazon.com/support/home#/).