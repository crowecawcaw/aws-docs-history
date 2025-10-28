# Neptune does not support

multiple concurrent queries in a transaction

Although the Bolt driver itself allows concurrent queries in a transaction, Neptune
does not support multiple queries in a transaction running concurrently. Instead, Neptune
requires that multiple queries in a transaction be run sequentially, and that the results of
each query be completely consumed before the next query is initiated.

The example below shows how to use Bolt to run multiple queries sequentially in a
transaction, so that the results of each one are completely consumed before the next one
begins:

```
final String query = "MATCH (n) RETURN n";

try (Driver driver = getDriver(HOST_BOLT, getDefaultConfig())) {
  try (Session session = driver.session(readSessionConfig)) {
    try (Transaction trx = session.beginTransaction()) {
      final Result res_1 = trx.run(query);
      Assert.assertEquals(10000, res_1.list().size());
      final Result res_2 = trx.run(query);
      Assert.assertEquals(10000, res_2.list().size());
    }
  }
}
```
