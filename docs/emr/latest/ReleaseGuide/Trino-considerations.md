# Trino Considerations

Consider the following when you run Trino on Amazon EMR.

## Non-configurable Trino deployment

properties

The following table shows
the different configuration options for Trino `properties` files.

| File                | Configurable                                                                                                                                                    |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `log.properties`    | Trino: Configurable in Amazon EMR versions 6.1.0 and<br>later. Use the `prestosql-log` or<br>`trino-log` configuration classification.                          |
| `config.properties` | Trino: Configurable in Amazon EMR versions 6.1.0 and<br>later. Use the `prestosql-config` or<br>`trino-config` configuration<br>classification.                 |
| `hive.properties`   | Trino: Configurable in Amazon EMR versions 6.1.0 and<br>later. Use the `prestosql-connector-hive` or<br>`trino-connector-hive` configuration<br>classification. |
| `node.properties`   | Trino: Configurable in Amazon EMR versions 6.1.0 and<br>later. Use the `prestosql-node` or<br>`trino-node` configuration classification.                        |
| `jvm.config`        | Not configurable.                                                                                                                                               |

## Additional considerations

- For Trino on EMR version 6.1.0 and later, Amazon EMR automatically
  configures a shared secret key for secure internal communication between cluster
  nodes. You don't need to do any additional configuration to enable this security
  feature, and you can override the configuration with your own secret key. For
  information about Trino internal authentication, see [Trino 353 documentation: Secure internal communication.](https://trino.io/docs/current/security/internal-communication.html "https://trino.io/docs/current/security/internal-communication.html")
