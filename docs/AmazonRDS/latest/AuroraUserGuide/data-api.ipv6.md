

# Using IPv6 with Amazon RDS Data API
<a name="data-api.ipv6"></a>

Amazon RDS Data API supports IPv6 connectivity through dual-stack endpoints. This allows you to connect to Data API using IPv6 addresses while maintaining backward compatibility with IPv4.

## IPv6 endpoint support
<a name="data-api.ipv6.endpoints"></a>

Data API provides dual-stack endpoints that support both IPv4 and IPv6 connections. These endpoints use the `.aws` domain instead of the traditional `.amazonaws.com` domain.

### Available endpoint types
<a name="data-api.ipv6.endpoint-types"></a>

Public dual-stack endpoints  
Format: `rds-data.{{region}}.api.aws`  
Example: `rds-data.us-east-1.api.aws`

FIPS dual-stack endpoints  
Format: `rds-data-fips.{{region}}.api.aws`  
Example: `rds-data-fips.us-east-1.api.aws`

PrivateLink IPv6 endpoints  
Available through VPC endpoints with IPv6 support  
Allows private IPv6 connectivity within your VPC

### Legacy IPv4-only endpoints
<a name="data-api.ipv6.legacy-endpoints"></a>

The existing `.amazonaws.com` endpoints continue to support IPv4-only connections:
+ `rds-data.{{region}}.amazonaws.com`
+ `rds-data-fips.{{region}}.amazonaws.com`

**Note**  
Legacy endpoints remain unchanged to ensure backward compatibility with existing applications.

## Using IPv6 endpoints
<a name="data-api.ipv6.using"></a>

To use IPv6 with Data API, update your application to use the new dual-stack endpoints. Your application will automatically use IPv6 if available, or fall back to IPv4.

For general guidance on setting up IPv6 in your VPC, see [Migrating to IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html) in the *Amazon VPC User Guide*.

You can configure IPv6 endpoints in two ways:
+ **Using environment variable**: Set `AWS_USE_DUALSTACK_ENDPOINT=true` in your IPv6 environment. The AWS CLI and AWS SDKs will automatically construct the appropriate `api.aws` endpoints without requiring you to specify endpoint URLs manually.
+ **Using explicit endpoint URLs**: Specify the dual-stack endpoint URL directly in your AWS CLI commands or SDK configuration as shown in the examples below.

### AWS CLI configuration
<a name="data-api.ipv6.cli"></a>

Configure the AWS CLI to use IPv6 endpoints by specifying the endpoint URL:

For Linux, macOS, or Unix:

```
aws rds-data execute-statement \
	    --endpoint-url https://rds-data.us-east-1.api.aws \
	    --resource-arn "arn:aws:rds:us-east-1:123456789012:cluster:my-cluster" \
	    --secret-arn "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret" \
	    --database "mydb" \
	    --sql "SELECT * FROM users LIMIT 10"
```

For Windows:

```
aws rds-data execute-statement ^
	    --endpoint-url https://rds-data.us-east-1.api.aws ^
	    --resource-arn "arn:aws:rds:us-east-1:123456789012:cluster:my-cluster" ^
	    --secret-arn "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret" ^
	    --database "mydb" ^
	    --sql "SELECT * FROM users LIMIT 10"
```

### AWS SDK configuration
<a name="data-api.ipv6.sdk"></a>

Configure AWS SDKs to use dual-stack endpoints:

------
#### [ Python ]

```
import boto3
	
	# Create RDS Data API client with IPv6 dual-stack endpoint
	client = boto3.client(
	    'rds-data',
	    endpoint_url='https://rds-data.us-east-1.api.aws'
	)
	
	# Execute a SQL statement
	response = client.execute_statement(
	    resourceArn='arn:aws:rds:us-east-1:123456789012:cluster:my-cluster',
	    secretArn='arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret',
	    database='mydb',
	    sql='SELECT * FROM users LIMIT 10'
	)
	
	print(response['records'])
```

------
#### [ Java ]

```
import software.amazon.awssdk.services.rdsdata.RdsDataClient;
	import software.amazon.awssdk.services.rdsdata.model.ExecuteStatementRequest;
	import software.amazon.awssdk.services.rdsdata.model.ExecuteStatementResponse;
	import java.net.URI;
	
	// Create RDS Data API client with IPv6 dual-stack endpoint
	RdsDataClient client = RdsDataClient.builder()
	    .endpointOverride(URI.create("https://rds-data.us-east-1.api.aws"))
	    .build();
	
	// Execute a SQL statement
	ExecuteStatementRequest request = ExecuteStatementRequest.builder()
	    .resourceArn("arn:aws:rds:us-east-1:123456789012:cluster:my-cluster")
	    .secretArn("arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret")
	    .database("mydb")
	    .sql("SELECT * FROM users LIMIT 10")
	    .build();
	
	ExecuteStatementResponse response = client.executeStatement(request);
	System.out.println(response.records());
```

------
#### [ JavaScript ]

```
const { RDSDataClient, ExecuteStatementCommand } = require("@aws-sdk/client-rds-data");
	
	// Create RDS Data API client with IPv6 dual-stack endpoint
	const client = new RDSDataClient({
	    endpoint: "https://rds-data.us-east-1.api.aws"
	});
	
	// Execute a SQL statement
	const command = new ExecuteStatementCommand({
	    resourceArn: "arn:aws:rds:us-east-1:123456789012:cluster:my-cluster",
	    secretArn: "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret",
	    database: "mydb",
	    sql: "SELECT * FROM users LIMIT 10"
	});
	
	const response = await client.send(command);
	console.log(response.records);
```

------

## Using AWS PrivateLink with IPv6
<a name="data-api.ipv6.privatelink"></a>

You can create VPC endpoints for Data API that support IPv6 connectivity within your VPC. For detailed instructions on creating VPC endpoints for Data API, see [Creating an Amazon VPC endpoint for the Amazon RDS Data API (AWS PrivateLink)](data-api.vpc-endpoint.md).

When creating a VPC endpoint for IPv6 support, ensure that:
+ Your VPC and subnets are configured to support IPv6
+ Security groups allow IPv6 traffic on the required ports (typically 443 for HTTPS)
+ Network ACLs are configured to allow IPv6 traffic

## Migration considerations
<a name="data-api.ipv6.migration"></a>

When migrating to IPv6 endpoints, consider the following:
+ **Gradual migration**: You can migrate applications gradually by updating endpoint URLs one application at a time.
+ **Network compatibility**: Ensure your network infrastructure supports IPv6 before migrating.
+ **Security policies**: Update security group rules and network ACLs to allow IPv6 traffic if needed.
+ **Monitoring**: Update monitoring and logging configurations to handle IPv6 addresses.

**Note**  
**Database connection addresses**: When using IPv6 endpoints for Data API, the underlying database connections and database logs will still show IPv4 addresses. This is expected behavior and does not affect the functionality of your IPv6-enabled applications.

## Troubleshooting IPv6 connectivity
<a name="data-api.ipv6.troubleshooting"></a>

If you experience issues with IPv6 connectivity, check the following:

Network configuration  
Verify that your network supports IPv6 and that IPv6 routing is configured correctly.

DNS resolution  
Ensure that your DNS resolver can resolve AAAA records for the dual-stack endpoints.

Security groups  
Update security group rules to allow IPv6 traffic on the required ports (typically 443 for HTTPS).

Client libraries  
Verify that your HTTP client libraries support IPv6 and dual-stack connectivity.