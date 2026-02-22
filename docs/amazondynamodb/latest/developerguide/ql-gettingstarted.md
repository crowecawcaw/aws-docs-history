# Getting started with PartiQL for DynamoDB

This section describes how to use PartiQL for DynamoDB from the Amazon DynamoDB console, the
AWS Command Line Interface (AWS CLI), and DynamoDB APIs.

In the following examples, the DynamoDB table that is defined in the [Getting started with DynamoDB](GettingStartedDynamoDB.md "GettingStartedDynamoDB.md") tutorial is a pre-requisite.

For information about using the DynamoDB console, AWS Command Line Interface, or DynamoDB APIs to access DynamoDB,
see [Accessing
DynamoDB](AccessingDynamoDB.md "AccessingDynamoDB.md").

To [download](workbench.md "workbench.md") and use the [NoSQL workbench](workbench.md "workbench.md") to build [PartiQL for DynamoDB](ql-reference.md "ql-reference.md") statements
choose **PartiQL operations** at the top right corner of the NoSQL Workbench for DynamoDB [Operation builder](workbench.querybuilder.md "workbench.querybuilder.md").

Console

![PartiQL editor interface that shows the result of running the Query operation on the Music table.](images/partiqlgettingstarted.png)

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. In the navigation pane on the left side of the console, choose
   **PartiQL editor**.
3. Choose the **Music** table.
4. Choose **Query table**. This action generates a query that
   will not result in a full table scan.
5. Replace `partitionKeyValue` with the string value `Acme
Band`. Replace `sortKeyValue` with the string value
   `Happy Day`.
6. Choose the **Run** button.
7. You can view the results of the query by choosing the **Table view** or the **JSON view** buttons.

NoSQL workbench

![NoSQL workbench interface. It shows a PartiQL SELECT statement that you can run on the Music table.](images/workbench/partiql.single.png)

1. Choose **PartiQL statement**.
2. Enter the following PartiQL [SELECT statement](ql-reference.md "ql-reference.md")

```
SELECT *
FROM Music
WHERE Artist=? and SongTitle=?
```

3. To specify a value for the `Artist` and `SongTitle` parameters:
   1. Choose **Optional request parameters**.
   2. Choose **Add new parameters**.
   3. Choose the attribute type **string** and value `Acme Band`.
   4. Repeat steps b and c, and choose type **string** and value `PartiQL Rocks`.

4. If you want to generate code, choose **Generate
   code**.

Select your desired language from the displayed tabs. You can now copy this code and use it in your application. 5. If you want the operation to be run immediately, choose
**Run**.

AWS CLI

1. Create an item in the `Music` table using the INSERT
   PartiQL statement.

```
aws dynamodb execute-statement --statement "INSERT INTO Music  \
					    VALUE  \
					    {'Artist':'Acme Band','SongTitle':'PartiQL Rocks'}"
```

2. Retrieve an item from the Music table using the SELECT PartiQL statement.

```
aws dynamodb execute-statement --statement "SELECT * FROM Music   \
                                            WHERE Artist='Acme Band' AND SongTitle='PartiQL Rocks'"
```

3. Update an item in the `Music` table using the UPDATE PartiQL statement.

```
aws dynamodb execute-statement --statement "UPDATE Music  \
                                            SET AwardsWon=1  \
                                            SET AwardDetail={'Grammys':[2020, 2018]}  \
                                            WHERE Artist='Acme Band' AND SongTitle='PartiQL Rocks'"
```

Add a list value for an item in the `Music` table.

```
aws dynamodb execute-statement --statement "UPDATE Music  \
                                            SET AwardDetail.Grammys =list_append(AwardDetail.Grammys,[2016])  \
                                            WHERE Artist='Acme Band' AND SongTitle='PartiQL Rocks'"
```

Remove a list value for an item in the `Music` table.

```
aws dynamodb execute-statement --statement "UPDATE Music  \
                                            REMOVE AwardDetail.Grammys[2]  \
                                            WHERE Artist='Acme Band' AND SongTitle='PartiQL Rocks'"
```

Add a new map member for an item in the `Music` table.

```
aws dynamodb execute-statement --statement "UPDATE Music  \
                                            SET AwardDetail.BillBoard=[2020]  \
                                            WHERE Artist='Acme Band' AND SongTitle='PartiQL Rocks'"
```

Add a new string set attribute for an item in the `Music` table.

```
aws dynamodb execute-statement --statement "UPDATE Music  \
                                            SET BandMembers =<<'member1', 'member2'>>  \
                                            WHERE Artist='Acme Band' AND SongTitle='PartiQL Rocks'"
```

Update a string set attribute for an item in the
`Music` table.

```
aws dynamodb execute-statement --statement "UPDATE Music  \
                                            SET BandMembers =set_add(BandMembers, <<'newmember'>>)  \
                                            WHERE Artist='Acme Band' AND SongTitle='PartiQL Rocks'"
```

4. Delete an item from the `Music` table using the DELETE
   PartiQL statement.

```
aws dynamodb execute-statement --statement "DELETE  FROM Music  \
    WHERE Artist='Acme Band' AND SongTitle='PartiQL Rocks'"
```

Java

```
import java.util.ArrayList;
import java.util.List;

import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import software.amazon.dynamodb.AmazonDynamoDB;
import software.amazon.dynamodb.AmazonDynamoDBClientBuilder;
import software.amazon.dynamodb.model.AttributeValue;
import software.amazon.dynamodb.model.ConditionalCheckFailedException;
import software.amazon.dynamodb.model.ExecuteStatementRequest;
import software.amazon.dynamodb.model.ExecuteStatementResult;
import software.amazon.dynamodb.model.InternalServerErrorException;
import software.amazon.dynamodb.model.ItemCollectionSizeLimitExceededException;
import software.amazon.dynamodb.model.ProvisionedThroughputExceededException;
import software.amazon.dynamodb.model.RequestLimitExceededException;
import software.amazon.dynamodb.model.ResourceNotFoundException;
import software.amazon.dynamodb.model.TransactionConflictException;

public class DynamoDBPartiQGettingStarted {

    public static void main(String[] args) {
        // Create the DynamoDB Client with the region you want
        AmazonDynamoDB dynamoDB = createDynamoDbClient("us-west-1");

        try {
            // Create ExecuteStatementRequest
            ExecuteStatementRequest executeStatementRequest = new ExecuteStatementRequest();
            List<AttributeValue> parameters= getPartiQLParameters();

            //Create an item in the Music table using the INSERT PartiQL statement
            processResults(executeStatementRequest(dynamoDB, "INSERT INTO Music value {'Artist':?,'SongTitle':?}", parameters));

            //Retrieve an item from the Music table using the SELECT PartiQL statement.
            processResults(executeStatementRequest(dynamoDB, "SELECT * FROM Music  where Artist=? and SongTitle=?", parameters));

            //Update an item in the Music table using the UPDATE PartiQL statement.
            processResults(executeStatementRequest(dynamoDB, "UPDATE Music SET AwardsWon=1 SET AwardDetail={'Grammys':[2020, 2018]}  where Artist=? and SongTitle=?", parameters));

            //Add a list value for an item in the Music table.
            processResults(executeStatementRequest(dynamoDB, "UPDATE Music SET AwardDetail.Grammys =list_append(AwardDetail.Grammys,[2016])  where Artist=? and SongTitle=?", parameters));

            //Remove a list value for an item in the Music table.
            processResults(executeStatementRequest(dynamoDB, "UPDATE Music REMOVE AwardDetail.Grammys[2]   where Artist=? and SongTitle=?", parameters));

            //Add a new map member for an item in the Music table.
            processResults(executeStatementRequest(dynamoDB, "UPDATE Music set AwardDetail.BillBoard=[2020] where Artist=? and SongTitle=?", parameters));

            //Add a new string set attribute for an item in the Music table.
            processResults(executeStatementRequest(dynamoDB, "UPDATE Music SET BandMembers =<<'member1', 'member2'>> where Artist=? and SongTitle=?", parameters));

            //update a string set attribute for an item in the Music table.
            processResults(executeStatementRequest(dynamoDB, "UPDATE Music SET BandMembers =set_add(BandMembers, <<'newmember'>>) where Artist=? and SongTitle=?", parameters));

            //Retrieve an item from the Music table using the SELECT PartiQL statement.
            processResults(executeStatementRequest(dynamoDB, "SELECT * FROM Music  where Artist=? and SongTitle=?", parameters));

            //delete an item from the Music Table
            processResults(executeStatementRequest(dynamoDB, "DELETE  FROM Music  where Artist=? and SongTitle=?", parameters));
        } catch (Exception e) {
            handleExecuteStatementErrors(e);
        }
    }

    private static AmazonDynamoDB createDynamoDbClient(String region) {
        return AmazonDynamoDBClientBuilder.standard().withRegion(region).build();
    }

    private static List<AttributeValue> getPartiQLParameters() {
        List<AttributeValue> parameters = new ArrayList<AttributeValue>();
        parameters.add(new AttributeValue("Acme Band"));
        parameters.add(new AttributeValue("PartiQL Rocks"));
        return parameters;
    }

    private static ExecuteStatementResult executeStatementRequest(AmazonDynamoDB client, String statement, List<AttributeValue> parameters ) {
        ExecuteStatementRequest request = new ExecuteStatementRequest();
        request.setStatement(statement);
        request.setParameters(parameters);
        return client.executeStatement(request);
    }

    private static void processResults(ExecuteStatementResult executeStatementResult) {
        System.out.println("ExecuteStatement successful: "+ executeStatementResult.toString());

    }

    // Handles errors during ExecuteStatement execution. Use recommendations in error messages below to add error handling specific to
    // your application use-case.
    private static void handleExecuteStatementErrors(Exception exception) {
        try {
            throw exception;
        } catch (ConditionalCheckFailedException ccfe) {
            System.out.println("Condition check specified in the operation failed, review and update the condition " +
                                       "check before retrying. Error: " + ccfe.getErrorMessage());
        } catch (TransactionConflictException tce) {
            System.out.println("Operation was rejected because there is an ongoing transaction for the item, generally " +
                                       "safe to retry with exponential back-off. Error: " + tce.getErrorMessage());
        } catch (ItemCollectionSizeLimitExceededException icslee) {
            System.out.println("An item collection is too large, you\'re using Local Secondary Index and exceeded " +
                                       "size limit of items per partition key. Consider using Global Secondary Index instead. Error: " + icslee.getErrorMessage());
        } catch (Exception e) {
            handleCommonErrors(e);
        }
    }

    private static void handleCommonErrors(Exception exception) {
        try {
            throw exception;
        } catch (InternalServerErrorException isee) {
            System.out.println("Internal Server Error, generally safe to retry with exponential back-off. Error: " + isee.getErrorMessage());
        } catch (RequestLimitExceededException rlee) {
            System.out.println("Throughput exceeds the current throughput limit for your account, increase account level throughput before " +
                                       "retrying. Error: " + rlee.getErrorMessage());
        } catch (ProvisionedThroughputExceededException ptee) {
            System.out.println("Request rate is too high. If you're using a custom retry strategy make sure to retry with exponential back-off. " +
                                       "Otherwise consider reducing frequency of requests or increasing provisioned capacity for your table or secondary index. Error: " +
                                       ptee.getErrorMessage());
        } catch (ResourceNotFoundException rnfe) {
            System.out.println("One of the tables was not found, verify table exists before retrying. Error: " + rnfe.getErrorMessage());
        } catch (AmazonServiceException ase) {
            System.out.println("An AmazonServiceException occurred, indicates that the request was correctly transmitted to the DynamoDB " +
                                       "service, but for some reason, the service was not able to process it, and returned an error response instead. Investigate and " +
                                       "configure retry strategy. Error type: " + ase.getErrorType() + ". Error message: " + ase.getErrorMessage());
        } catch (AmazonClientException ace) {
            System.out.println("An AmazonClientException occurred, indicates that the client was unable to get a response from DynamoDB " +
                                       "service, or the client was unable to parse the response from the service. Investigate and configure retry strategy. "+
                                       "Error: " + ace.getMessage());
        } catch (Exception e) {
            System.out.println("An exception occurred, investigate and configure retry strategy. Error: " + e.getMessage());
        }
    }

}
```

## Using parameterized statements

Instead of embedding values directly in a PartiQL statement string, you can use
question mark (`?`) placeholders and supply the values separately in the
`Parameters` field. Each `?` is replaced by the corresponding
parameter value, in the order they are provided.

Using parameterized statements is a best practice because it separates the statement
structure from the data values, making statements easier to read and reuse. It also
avoids the need to manually format and escape attribute values in the statement
string.

Parameterized statements are supported in `ExecuteStatement`,
`BatchExecuteStatement`, and `ExecuteTransaction`
operations.

The following examples retrieve an item from the `Music` table using
parameterized values for the partition key and sort key.

AWS CLI parameterized

```
aws dynamodb execute-statement \
    --statement "SELECT * FROM \"Music\" WHERE Artist=? AND SongTitle=?" \
    --parameters '[{"S": "Acme Band"}, {"S": "PartiQL Rocks"}]'
```

Java parameterized

```
List<AttributeValue> parameters = new ArrayList<>();
parameters.add(new AttributeValue("Acme Band"));
parameters.add(new AttributeValue("PartiQL Rocks"));

ExecuteStatementRequest request = new ExecuteStatementRequest()
    .withStatement("SELECT * FROM Music WHERE Artist=? AND SongTitle=?")
    .withParameters(parameters);

ExecuteStatementResult result = dynamoDB.executeStatement(request);
```

Python parameterized

```
response = dynamodb_client.execute_statement(
    Statement="SELECT * FROM Music WHERE Artist=? AND SongTitle=?",
    Parameters=[
        {'S': 'Acme Band'},
        {'S': 'PartiQL Rocks'}
    ]
)
```

###### Note

The Java example in the preceding getting started section uses parameterized
statements throughout. The `getPartiQLParameters()` method builds the
parameter list, and each statement uses `?` placeholders instead of
inline values.
