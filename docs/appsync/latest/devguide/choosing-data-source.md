

# Choosing between direct data source access and proxying via a Lambda data source
<a name="choosing-data-source"></a>

With AWS AppSync and the `APPSYNC_JS` runtime, you can write your own code that implements your custom business logic by using AWS AppSync functions to access your data sources. This makes it easy for you to directly interact with data sources like Amazon DynamoDB, Aurora Serverless, OpenSearch Service, HTTP APIs, and other AWS services without having to deploy additional computational services or infrastructure. AWS AppSync also makes it easy to interact with an AWS Lambda function by configuring a Lambda data source. Lambda data sources allow you to run complex business logic using AWS Lambda’s full set capabilities to resolve a GraphQL request. In most cases, an AWS AppSync function directly connected to its target data source will provide all of the functionality you need. In situations where you need to implement complex business logic that is not supported by the `APPSYNC_JS` runtime, you can use a Lambda data source as a proxy to interact with your target data source.


|  |  |  | 
| --- |--- |--- |
|  | Direct data source integration | Lambda data source as a proxy | 
| Use case | AWS AppSync functions interact directly with API data sources. | AWS AppSync functions call Lambdas that interact with API data sources. | 
| Runtime | APPSYNC\_JS (JavaScript) | Any supported Lambda runtime | 
| Maximum size of code | 32,000 characters per AWS AppSync function | 50 MB (zipped, for direct upload) per Lambda | 
| External modules | Limited - APPSYNC\_JS supported features only | Yes | 
| Call any AWS service | Yes - Using AWS AppSync HTTP datasource | Yes - Using AWS SDK | 
| Access to the request header | Yes | Yes | 
| Network access | No | Yes | 
| File system access | No | Yes | 
| Logging and metrics | Yes | Yes | 
| Build and test entirely within AppSync | Yes | No | 
| Cold start | No | No - With provisioned concurrency | 
| Auto-scaling | Yes - transparently by AWS AppSync | Yes - As configured in Lambda | 
| Pricing | No additional charge | Charged for Lambda usage | 

AWS AppSync functions that integrate directly with their target data source are ideal for use cases like the following:
+  Interacting with Amazon DynamoDB, Aurora Serverless, and OpenSearch Service
+  Interacting with HTTP APIs and passing incoming headers 
+  Interacting with AWS services using HTTP data sources (with AWS AppSync automatically signing requests with the provided data source role) 
+  Implementing access control before accessing data sources 
+  Implementing the filtering of retrieved data prior to fulfilling a request 
+  Implementing simple orchestration with sequential execution of AWS AppSync functions in a resolver pipeline 
+  Controlling caching and subscription connections in queries and mutations. 

AWS AppSync functions that use a Lambda data source as a proxy are ideal for use cases like the following:
+  Using a language other than JavaScript or Velocity Template Language (VTL) 
+  Adjusting and controlling CPU or memory to optimize performance 
+  Importing third-party libraries or requiring unsupported features in `APPSYNC_JS` 
+  Making multiple network requests and/or getting file system access to fulfill a query 
+  Batching requests using [ batching configuration](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-lambda-js.html). 