

# Trino Considerations
<a name="Trino-considerations"></a>

Consider the following when you run Trino on Amazon EMR.

## Non-configurable Trino deployment properties
<a name="emr-trino-deployment-config"></a>

The following table shows the different configuration options for Trino `properties` files.


| File | Configurable | 
| --- | --- | 
| `log.properties` | Trino: Configurable in Amazon EMR versions 6.1.0 and later. Use the `prestosql-log` or `trino-log` configuration classification. | 
| `config.properties` | Trino: Configurable in Amazon EMR versions 6.1.0 and later. Use the `prestosql-config` or `trino-config` configuration classification. | 
| `hive.properties` | Trino: Configurable in Amazon EMR versions 6.1.0 and later. Use the `prestosql-connector-hive` or `trino-connector-hive` configuration classification. | 
| `node.properties` | Trino: Configurable in Amazon EMR versions 6.1.0 and later. Use the `prestosql-node` or `trino-node` configuration classification. | 
| `jvm.config` | Not configurable. | 

## Additional considerations
<a name="emr-trino-deployment-config-additional"></a>
+ For Trino on EMR version 6.1.0 and later, Amazon EMR automatically configures a shared secret key for secure internal communication between cluster nodes. You don't need to do any additional configuration to enable this security feature, and you can override the configuration with your own secret key. For information about Trino internal authentication, see [Trino 353 documentation: Secure internal communication.](https://trino.io/docs/current/security/internal-communication.html)