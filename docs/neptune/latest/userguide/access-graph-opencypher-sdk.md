

# Using the AWS SDK to run openCypher queries
<a name="access-graph-opencypher-sdk"></a>

With the AWS SDK, you can run openCypher queries against your Neptune graph using a programming language of your choice. The Neptune data API SDK (service name `neptunedata`) provides the [ExecuteOpenCypherQuery](https://docs.aws.amazon.com/neptune/latest/data-api/API_ExecuteOpenCypherQuery.html) action for submitting openCypher queries.

You must run these examples from an Amazon EC2 instance in the same virtual private cloud (VPC) as your Neptune DB cluster, or from a location that has network connectivity to your cluster endpoint.

Direct links to the API reference documentation for the `neptunedata` service in each SDK language can be found below:


| Programming language | neptunedata API reference | 
| --- | --- | 
| C\+\+ | [https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-neptunedata/html/annotated.html](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-neptunedata/html/annotated.html) | 
| Go | [https://docs.aws.amazon.com/sdk-for-go/api/service/neptunedata/](https://docs.aws.amazon.com/sdk-for-go/api/service/neptunedata/) | 
| Java | [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/neptunedata/package-summary.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/neptunedata/package-summary.html) | 
| JavaScript | [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-neptunedata/](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-neptunedata/) | 
| Kotlin | [https://sdk.amazonaws.com/kotlin/api/latest/neptunedata/index.html](https://sdk.amazonaws.com/kotlin/api/latest/neptunedata/index.html) | 
| .NET | [https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Neptunedata/NNeptunedata.html](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Neptunedata/NNeptunedata.html) | 
| PHP | [https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.Neptunedata.html](https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.Neptunedata.html) | 
| Python | [https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata.html](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata.html) | 
| Ruby | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Neptunedata.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Neptunedata.html) | 
| Rust | [https://crates.io/crates/aws-sdk-neptunedata](https://crates.io/crates/aws-sdk-neptunedata) | 
| CLI | [https://docs.aws.amazon.com/cli/latest/reference/neptunedata/](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/) | 

## openCypher AWS SDK examples
<a name="access-graph-opencypher-sdk-examples"></a>

The following examples show how to set up a `neptunedata` client, run an openCypher query, and print the results. Replace {{YOUR\_NEPTUNE\_HOST}} and {{YOUR\_NEPTUNE\_PORT}} with the endpoint and port of your Neptune DB cluster.

**Client-side timeout and retry configuration**  
The SDK client timeout controls how long the *client* waits for a response. It does not control how long the query runs on the server. If the client times out before the server finishes, the query may continue running on Neptune while the client has no way to retrieve the results.  
We recommend setting the client-side read timeout to `0` (no timeout) or to a value that is at least a few seconds longer than the server-side [neptune\_query\_timeout](parameters.md#parameters-db-cluster-parameters-neptune_query_timeout) setting on your Neptune DB cluster. This lets Neptune control when queries time out.  
We also recommend setting the maximum retry attempts to `1` (no retries). If the SDK retries a query that is still running on the server, it can result in duplicate operations. This is especially important for mutation queries, where a retry could cause unintended duplicate writes.

------
#### [ Python ]

1. Follow the [installation instructions](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) to install Boto3.

1. Create a file named `openCypherExample.py` and paste the following code:

   ```
   import boto3
   import json
   from botocore.config import Config
   
   # Disable the client-side read timeout and retries so that
   # Neptune's server-side neptune_query_timeout controls query duration.
   client = boto3.client(
       'neptunedata',
       endpoint_url=f'https://{{YOUR_NEPTUNE_HOST}}:{{YOUR_NEPTUNE_PORT}}',
       config=Config(read_timeout=None, retries={'total_max_attempts': 1})
   )
   
   response = client.execute_open_cypher_query(
       openCypherQuery='MATCH (n) RETURN n LIMIT 1'
   )
   
   print(json.dumps(response['results'], indent=2))
   ```

1. Run the example: `python openCypherExample.py`

------
#### [ Java ]

1. Follow the [installation instructions](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html) to set up the AWS SDK for Java.

1. Use the following code to set up a `NeptunedataClient`, run an openCypher query, and print the result:

   ```
   import java.net.URI;
   import java.time.Duration;
   import software.amazon.awssdk.core.client.config.ClientOverrideConfiguration;
   import software.amazon.awssdk.core.retry.RetryPolicy;
   import software.amazon.awssdk.services.neptunedata.NeptunedataClient;
   import software.amazon.awssdk.services.neptunedata.model.ExecuteOpenCypherQueryRequest;
   import software.amazon.awssdk.services.neptunedata.model.ExecuteOpenCypherQueryResponse;
   
   // Disable the client-side timeout and retries so that
   // Neptune's server-side neptune_query_timeout controls query duration.
   NeptunedataClient client = NeptunedataClient.builder()
       .endpointOverride(URI.create("https://{{YOUR_NEPTUNE_HOST}}:{{YOUR_NEPTUNE_PORT}}"))
       .overrideConfiguration(ClientOverrideConfiguration.builder()
           .apiCallTimeout(Duration.ZERO)
           .retryPolicy(RetryPolicy.none())
           .build())
       .build();
   
   ExecuteOpenCypherQueryRequest request = ExecuteOpenCypherQueryRequest.builder()
       .openCypherQuery("MATCH (n) RETURN n LIMIT 1")
       .build();
   
   ExecuteOpenCypherQueryResponse response = client.executeOpenCypherQuery(request);
   
   System.out.println(response.results().toString());
   ```

------
#### [ JavaScript ]

1. Follow the [installation instructions](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-nodejs.html) to set up the AWS SDK for JavaScript. Install the neptunedata client package: `npm install @aws-sdk/client-neptunedata`.

1. Create a file named `openCypherExample.js` and paste the following code:

   ```
   import { NeptunedataClient, ExecuteOpenCypherQueryCommand } from "@aws-sdk/client-neptunedata";
   import { NodeHttpHandler } from "@smithy/node-http-handler";
   
   const config = {
       endpoint: "https://{{YOUR_NEPTUNE_HOST}}:{{YOUR_NEPTUNE_PORT}}",
       // Disable the client-side request timeout so that
       // Neptune's server-side neptune_query_timeout controls query duration.
       requestHandler: new NodeHttpHandler({
           requestTimeout: 0
       }),
       maxAttempts: 1
   };
   
   const client = new NeptunedataClient(config);
   
   const input = {
       openCypherQuery: "MATCH (n) RETURN n LIMIT 1"
   };
   
   const command = new ExecuteOpenCypherQueryCommand(input);
   const response = await client.send(command);
   
   console.log(JSON.stringify(response, null, 2));
   ```

1. Run the example: `node openCypherExample.js`

------