# Querying global secondary indexes with SDK for Java 1.x

You can use Amazon DynamoDB Accelerator (DAX) to query [global secondary indexes](GSI.md "GSI.md")
using DynamoDB [programmatic
interfaces](Programming.SDKs.md "Programming.SDKs.md").

The following example demonstrates how to use DAX to query the
`CreateDateIndex` global secondary index that is created in [Example:
Global secondary indexes using the AWS SDK for Java document API](GSIJavaDocumentAPI.md "GSIJavaDocumentAPI.md").

The `DAXClient` class instantiates the client objects that are needed to
interact with the DynamoDB programming interfaces.

```
import com.amazon.dax.client.dynamodbv2.AmazonDaxClientBuilder;
import software.amazon.dynamodb.datamodeling.DynamoDBMapper;
import software.amazon.dynamodb.document.DynamoDB;
import com.amazonaws.util.EC2MetadataUtils;
import software.amazon.dynamodb.AmazonDynamoDB;

public class DaxClient {

	private static final String region = EC2MetadataUtils.getEC2InstanceRegion();

	DynamoDB getDaxDocClient(String daxEndpoint) {
		System.out.println("Creating a DAX client with cluster endpoint " + daxEndpoint);
		AmazonDaxClientBuilder daxClientBuilder = AmazonDaxClientBuilder.standard();

		daxClientBuilder.withRegion(region).withEndpointConfiguration(daxEndpoint);
		AmazonDynamoDB client = daxClientBuilder.build();

		return new DynamoDB(client);
	}

	DynamoDBMapper getDaxMapperClient(String daxEndpoint) {
		System.out.println("Creating a DAX client with cluster endpoint " + daxEndpoint);
		AmazonDaxClientBuilder daxClientBuilder = AmazonDaxClientBuilder.standard();

		daxClientBuilder.withRegion(region).withEndpointConfiguration(daxEndpoint);
		AmazonDynamoDB client = daxClientBuilder.build();

		return new DynamoDBMapper(client);
	}
}
```

You can query a global secondary index in the following ways:

- Use the `queryIndex` method on the `QueryIndexDax` class
  defined in the following example. The `QueryIndexDax` takes as a
  parameter the client object that is returned by the `getDaxDocClient`
  method on the `DaxClient` class.
- If you are using the [object persistence interface](Programming.SDKs.Interfaces.md "Programming.SDKs.Interfaces.md"), use the `queryIndexMapper`
  method on the `QueryIndexDax` class defined in the following example. The
  `queryIndexMapper` takes as a parameter the client object that is
  returned by the `getDaxMapperClient` method defined on the
  `DaxClient` class.

```
import java.util.Iterator;
import software.amazon.dynamodb.datamodeling.DynamoDBMapper;
import java.util.List;
import software.amazon.dynamodb.datamodeling.DynamoDBQueryExpression;
import software.amazon.dynamodb.model.AttributeValue;
import java.util.HashMap;
import software.amazon.dynamodb.document.Item;
import software.amazon.dynamodb.document.utils.ValueMap;
import software.amazon.dynamodb.document.spec.QuerySpec;
import software.amazon.dynamodb.document.QueryOutcome;
import software.amazon.dynamodb.document.ItemCollection;
import software.amazon.dynamodb.document.Index;
import software.amazon.dynamodb.document.Table;
import software.amazon.dynamodb.document.DynamoDB;

public class QueryIndexDax {

	//This is used to query Index using the low-level interface.
	public static void queryIndex(DynamoDB client, String tableName, String indexName) {
		Table table = client.getTable(tableName);

		System.out.println("\n***********************************************************\n");
		System.out.print("Querying index " + indexName + "...");

		Index index = table.getIndex(indexName);

		ItemCollection<QueryOutcome> items = null;

		QuerySpec querySpec = new QuerySpec();

		if (indexName == "CreateDateIndex") {
			System.out.println("Issues filed on 2013-11-01");
			querySpec.withKeyConditionExpression("CreateDate = :v_date and begins_with(IssueId, :v_issue)")
					.withValueMap(new ValueMap().withString(":v_date", "2013-11-01").withString(":v_issue", "A-"));
			items = index.query(querySpec);
		} else {
			System.out.println("\nNo valid index name provided");
			return;
		}

		Iterator<Item> iterator = items.iterator();

		System.out.println("Query: printing results...");

		while (iterator.hasNext()) {
			System.out.println(iterator.next().toJSONPretty());
		}

	}

	//This is used to query Index using the high-level mapper interface.
	public static void queryIndexMapper(DynamoDBMapper mapper, String tableName, String indexName) {
		HashMap<String, AttributeValue> eav = new HashMap<String, AttributeValue>();
		eav.put(":v_date", new AttributeValue().withS("2013-11-01"));
		eav.put(":v_issue", new AttributeValue().withS("A-"));
		DynamoDBQueryExpression<CreateDate> queryExpression = new DynamoDBQueryExpression<CreateDate>()
				.withIndexName("CreateDateIndex").withConsistentRead(false)
				.withKeyConditionExpression("CreateDate = :v_date and begins_with(IssueId, :v_issue)")
				.withExpressionAttributeValues(eav);

		List<CreateDate> items = mapper.query(CreateDate.class, queryExpression);
		Iterator<CreateDate> iterator = items.iterator();

		System.out.println("Query: printing results...");

		while (iterator.hasNext()) {
			CreateDate iterObj = iterator.next();
			System.out.println(iterObj.getCreateDate());
			System.out.println(iterObj.getIssueId());
		}
	}
}
```

The class definition below represents the Issues table and is used in the
`queryIndexMapper` method.

```
import software.amazon.dynamodb.datamodeling.DynamoDBTable;
import software.amazon.dynamodb.datamodeling.DynamoDBIndexHashKey;
import software.amazon.dynamodb.datamodeling.DynamoDBIndexRangeKey;
import software.amazon.dynamodb.datamodeling.DynamoDBHashKey;

@DynamoDBTable(tableName = "Issues")
public class CreateDate {
	private String createDate;
	@DynamoDBHashKey(attributeName = "IssueId")
	private String issueId;

	@DynamoDBIndexHashKey(globalSecondaryIndexName = "CreateDateIndex", attributeName = "CreateDate")
	public String getCreateDate() {
		return createDate;
	}

	public void setCreateDate(String createDate) {
		this.createDate = createDate;
	}

	@DynamoDBIndexRangeKey(globalSecondaryIndexName = "CreateDateIndex", attributeName = "IssueId")
	public String getIssueId() {
		return issueId;
	}

	public void setIssueId(String issueId) {
		this.issueId = issueId;
	}
}
```
