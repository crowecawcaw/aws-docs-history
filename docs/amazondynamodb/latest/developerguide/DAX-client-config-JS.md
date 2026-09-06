

# Default client configuration for Node.js
<a name="DAX-client-config-JS"></a>

When configuring the DAX JavaScript SDK client, you can customize various parameters to optimize performance, connection handling, and error resilience. The following table outlines the default configuration settings that control how your client interacts with the DAX cluster, including timeout values, retry mechanisms, credential management, and health monitoring options. For more information, see [DynamoDBClient Operations](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/dynamodb/).


**DAX JS SDK client defaults**  

| Parameter | Type | Description | 
| --- | --- | --- | 
| `region`<br />optional | `string` | The AWS Region to use for the DAX client (example - 'us-east-1'). This is a required parameter if not provided through the environment variable. | 
| `endpoint`<br />required | `string` | The endpoint of the Cluster to which the SDK connects.<br />Examples:<br />Non-encrypted – dax-cluster-name.region.amazonaws.com<br />Encrypted – daxs://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com | 
| `requestTimeout`<br />default 6000 ms | `number` | This defines the maximum time the client will wait for a response from DAX. | 
| `writeRetries`<br />default 1 | `number` | The number of retries to attempt for write requests that fail. | 
| `readRetries`<br />default 1 | `number` | The number of retries to attempt for read requests that fail. | 
| `maxRetries`<br />default 1 | `number` | The maximum number of retries to attempt on failed requests.<br />If readRetries/writeRetries are set, then the configuration set in readRetries and writeRetries take priority over maxRetries. | 
| `connectTimeout`<br />default 10000 ms | `number` | The timeout (in milliseconds) for establishing a connection to any of the cluster nodes. | 
| `maxConcurrentConnections`<br />default 100 | `number` | Limits the total number of concurrent connections that a client instance can create per node in a DAX cluster. | 
| `maxRetryDelay`<br />default 7000 ms | `number` | When the DAX server indicates recover is needed by setting `waitForRecoveryBeforeRetrying` flag to true, the client will pause before retry attempts. During these recovery periods, the `maxRetryDelay` parameter determines the maximum waiting time between retries. This recovery-specific configuration only applies when the DAX server is in recovery mode. For all other scenarios, retry behavior follows one of two patterns: either an exponential delay based on the retry count (governed by `writeRetries`, `readRetries`, or `maxRetries` parameters), or an immediate retry depending on the exception type. | 
| `credentials`<br />optional | [AwsCredentialIdentity](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/) \| [AwsCredentialIdentityProvider](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/) | The AWS credentials to use for authenticating requests. This can be provided as an AwsCredentialIdentity or an AwsCredentialIdentityProvider. If not provided, the AWS SDK will automatically use the default credentials provider chain. Example: `{ accessKeyId: 'AKIA...', secretAccessKey: '...', sessionToken: '...' }` \* @default Uses default AWS credentials provider chain. | 
| `healthCheckInterval`<br />default 5000 ms | `number` | The interval (in milliseconds) between cluster health checks. A lower interval will check more frequently. | 
| `healthCheckTimeout`<br />default 1000 ms | `number` | The timeout (in milliseconds) for the health check to complete. | 
| `skipHostnameVerification`<br />default false | `boolean` | Skip hostname verification of TLS connections. This has no impact on un-encrypted clusters. The default is to perform hostname verification, setting this to True will skip verification. Be sure you understand the implication of turning it off, which is the inability to authenticate the cluster that you are connecting to.  | 
| `unhealthyConsecutiveErrorCount`<br />default 5 | `number` | Sets the number of consecutive errors required to signal node unhealthy within health check interval. | 
| `clusterUpdateInterval`<br />default 4000 ms | `number` | Returns the interval between polling of cluster members for membership changes. | 
| `clusterUpdateThreshold`<br />default 125 | `number` | Returns the threshold below which the cluster will not be polled for membership changes. | 
| `credentailProvider`<br />optional \| default null | [AwsCredentialIdentityProvider](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/) | User Defined Provider for AWS credentials used to authenticate requests to DAX. | 


**Pagination configuration for DaxDocument**  

| Name | Type | Detail | 
| --- | --- | --- | 
| `client` | DaxDocument | Instance of DaxDocument type. | 
| `pageSize` | number | Determines the number of items per page. | 
| `startingToken`<br />Optional | any | LastEvaluatedKey from previous response can be used for subsequent requests. | 

For usage of pagination, see [TryDax.js](DAX.client.tutorial-TryDax.md).