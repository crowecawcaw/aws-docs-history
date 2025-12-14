# Using the Java client library for RDS

Data API

You can download and use a Java client library for RDS Data API (Data API). This
Java client library provides an alternative way to use Data API. Using this library, you
can map your client-side classes to Data API requests and responses. This mapping
support can ease integration with some specific Java types, such as `Date`,
`Time`, and `BigDecimal`.

## Downloading the Java client library for

Data API

The Data API Java client library is open source in GitHub at the following location:

[https://github.com/awslabs/rds-data-api-client-library-java](https://github.com/awslabs/rds-data-api-client-library-java "https://github.com/awslabs/rds-data-api-client-library-java")

You can build the library manually from the source files, but the best practice is to consume the
library using Apache Maven dependency management. Add the following dependency to your Maven
POM file.

For version 2.x, which is compatible with AWS SDK 2.x, use the
following:

```
<dependency>
   <groupId>software.amazon.rdsdata</groupId>
   <artifactId>rds-data-api-client-library-java</artifactId>
   <version>2.0.0</version>
</dependency>

```

For version 1.x, which is compatible with AWS SDK 1.x, use the
following:

```
<dependency>
    <groupId>software.amazon.rdsdata</groupId>
    <artifactId>rds-data-api-client-library-java</artifactId>
    <version>1.0.8</version>
</dependency>

```

## Java client library examples

Following, you can find some common examples of using the Data API Java client
library. These examples assume that you have a table `accounts` with
two columns: `accountId` and `name`. You also have the
following data transfer object (DTO).

```
public class Account {
    int accountId;
    String name;
    // getters and setters omitted
}
```

The client library enables you to pass DTOs as input parameters. The following example shows how customer DTOs are
mapped to input parameters sets.

```
var account1 = new Account(1, "John");
var account2 = new Account(2, "Mary");
client.forSql("INSERT INTO accounts(accountId, name) VALUES(:accountId, :name)")
         .withParamSets(account1, account2)
         .execute();
```

In some cases, it's easier to work with simple values as input
parameters. You can do so with the following syntax.

```
client.forSql("INSERT INTO accounts(accountId, name) VALUES(:accountId, :name)")
         .withParameter("accountId", 3)
         .withParameter("name", "Zhang")
         .execute();
```

The following is another example that works with simple values as input parameters.

```

client.forSql("INSERT INTO accounts(accountId, name) VALUES(?, ?)", 4, "Carlos")
         .execute();

```

The client library provides automatic mapping to DTOs when a result
is returned. The following examples show how the result is mapped to
your DTOs.

```
List<Account> result = client.forSql("SELECT * FROM accounts")
          .execute()
          .mapToList(Account.class);

Account result = client.forSql("SELECT * FROM accounts WHERE account_id = 1")
          .execute()
          .mapToSingle(Account.class);
```

In many cases, the database result set contains only a single value. In order to simplify
retrieving such results, the client library offers the following API:

```
int numberOfAccounts = client.forSql("SELECT COUNT(*) FROM accounts")
          .execute()
          .singleValue(Integer.class);
```

###### Note

The `mapToList` function converts a SQL result set into a user-defined object list. We don't support using
the `.withFormatRecordsAs(RecordsFormatType.JSON)` statement in an `ExecuteStatement` call for
the Java client library, because it serves the same purpose. For more information, see [Processing Amazon RDS Data API query results in JSON format](data-api-json.md "data-api-json.md").
