# Calling the Amazon RDS Data API from a Java application

You can call the Amazon RDS Data API (Data API) from a Java application.

The following examples use the AWS SDK for Java. For more information, see the
[AWS SDK for Java Developer Guide](../../../sdk-for-java/latest/developer-guide/welcome.md "../../../sdk-for-java/latest/developer-guide/welcome.md").

In each example, replace the DB cluster's Amazon Resource Name (ARN) with the
ARN for your Aurora DB cluster. Also, replace the secret ARN with the
ARN of the secret in Secrets Manager that allows access to the DB cluster.

###### Topics

- [Running a SQL query](#data-api.calling.java.run-query "#data-api.calling.java.run-query")
- [Running a SQL transaction](#data-api.calling.java.run-transaction "#data-api.calling.java.run-transaction")
- [Running a batch SQL operation](#data-api.calling.java.run-batch "#data-api.calling.java.run-batch")

## Running a SQL query

You can run a `SELECT` statement and fetch the results with a Java application.

The following example runs a SQL query.

```
package com.amazonaws.rdsdata.examples;

import com.amazonaws.services.rdsdata.AWSRDSData;
import com.amazonaws.services.rdsdata.AWSRDSDataClient;
import com.amazonaws.services.rdsdata.model.ExecuteStatementRequest;
import com.amazonaws.services.rdsdata.model.ExecuteStatementResult;
import com.amazonaws.services.rdsdata.model.Field;

import java.util.List;

public class FetchResultsExample {
  public static final String RESOURCE_ARN = "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`";
  public static final String SECRET_ARN = "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`";

  public static void main(String[] args) {
    AWSRDSData rdsData = AWSRDSDataClient.builder().build();

    ExecuteStatementRequest request = new ExecuteStatementRequest()
            .withResourceArn(RESOURCE_ARN)
            .withSecretArn(SECRET_ARN)
            .withDatabase("`mydb`")
            .withSql("`select * from mytable`");

    ExecuteStatementResult result = rdsData.executeStatement(request);

    for (List<Field> fields: result.getRecords()) {
      String stringValue = fields.get(0).getStringValue();
      long numberValue = fields.get(1).getLongValue();

      System.out.println(String.format("Fetched row: string = %s, number = %d", stringValue, numberValue));
    }
  }
}
```

## Running a SQL transaction

You can start a SQL transaction, run one or more SQL statements, and then
commit the changes with a Java application.

###### Important

A transaction times out if there are no calls that use its transaction ID
in three minutes. If a transaction times out before it's
committed, it's rolled back automatically.

If you don't specify a transaction ID, changes that result from
the call are committed automatically.

The following example runs a SQL transaction.

```
package com.amazonaws.rdsdata.examples;

import com.amazonaws.services.rdsdata.AWSRDSData;
import com.amazonaws.services.rdsdata.AWSRDSDataClient;
import com.amazonaws.services.rdsdata.model.BeginTransactionRequest;
import com.amazonaws.services.rdsdata.model.BeginTransactionResult;
import com.amazonaws.services.rdsdata.model.CommitTransactionRequest;
import com.amazonaws.services.rdsdata.model.ExecuteStatementRequest;

public class TransactionExample {
  public static final String RESOURCE_ARN = "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`";
  public static final String SECRET_ARN = "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`";

  public static void main(String[] args) {
    AWSRDSData rdsData = AWSRDSDataClient.builder().build();

    BeginTransactionRequest beginTransactionRequest = new BeginTransactionRequest()
            .withResourceArn(RESOURCE_ARN)
            .withSecretArn(SECRET_ARN)
            .withDatabase("`mydb`");
    BeginTransactionResult beginTransactionResult = rdsData.beginTransaction(beginTransactionRequest);
    String transactionId = beginTransactionResult.getTransactionId();

    ExecuteStatementRequest executeStatementRequest = new ExecuteStatementRequest()
            .withTransactionId(transactionId)
            .withResourceArn(RESOURCE_ARN)
            .withSecretArn(SECRET_ARN)
            .withSql("`INSERT INTO test_table VALUES ('hello world!')`");
    rdsData.executeStatement(executeStatementRequest);

    CommitTransactionRequest commitTransactionRequest = new CommitTransactionRequest()
            .withTransactionId(transactionId)
            .withResourceArn(RESOURCE_ARN)
            .withSecretArn(SECRET_ARN);
    rdsData.commitTransaction(commitTransactionRequest);
  }
}
```

###### Note

If you run a data definition language (DDL) statement, we recommend continuing to run the statement after
the call times out. When a DDL statement terminates before it is finished
running, it can result in errors and possibly corrupted data structures. To
continue running a statement after a call exceeds the RDS Data API timeout interval of 45 seconds, set the `continueAfterTimeout`
parameter to `true`.

## Running a batch SQL operation

You can run bulk insert and update operations over an array of data with a Java application.
You can run a DML statement with array of parameter sets.

###### Important

If you don't specify a transaction ID, changes that result from the call
are committed automatically.

The following example runs a batch insert operation.

```
package com.amazonaws.rdsdata.examples;

import com.amazonaws.services.rdsdata.AWSRDSData;
import com.amazonaws.services.rdsdata.AWSRDSDataClient;
import com.amazonaws.services.rdsdata.model.BatchExecuteStatementRequest;
import com.amazonaws.services.rdsdata.model.Field;
import com.amazonaws.services.rdsdata.model.SqlParameter;

import java.util.Arrays;

public class BatchExecuteExample {
  public static final String RESOURCE_ARN = "`arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster`";
  public static final String SECRET_ARN = "`arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret`";

  public static void main(String[] args) {
      AWSRDSData rdsData = AWSRDSDataClient.builder().build();

    BatchExecuteStatementRequest request = new BatchExecuteStatementRequest()
            .withDatabase("test")
            .withResourceArn(RESOURCE_ARN)
            .withSecretArn(SECRET_ARN)
            .withSql("INSERT INTO test_table2 VALUES (:string, :number)")
            .withParameterSets(Arrays.asList(
                    Arrays.asList(
                            new SqlParameter().withName("string").withValue(new Field().withStringValue("Hello")),
                            new SqlParameter().withName("number").withValue(new Field().withLongValue(1L))
                    ),
                    Arrays.asList(
                            new SqlParameter().withName("string").withValue(new Field().withStringValue("World")),
                            new SqlParameter().withName("number").withValue(new Field().withLongValue(2L))
                    )
            ));

    rdsData.batchExecuteStatement(request);
  }
}
```
