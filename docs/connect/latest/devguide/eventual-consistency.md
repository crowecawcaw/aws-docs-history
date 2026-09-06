

# Connect Customer eventual consistency
<a name="eventual-consistency"></a>

The Connect Customer API follows an [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency) model due to the distributed nature of the system. As a result, changes to Connect Customer resources might not be immediately visible to the subsequent commands you run. 

When you perform Connect Customer API calls, there might be a brief delay before the change is available throughout Connect Customer. It typically takes less than a few seconds for the change to propagate throughout the system, but in some cases it can take several minutes. You might get unexpected errors, such as a `ResourceNotFoundException` or an `InvalidRequestException`, during this time. For example, Connect Customer might return a `ResourceNotFoundException` if you call [DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) immediately after calling [CreateUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateUser.html). 

We recommend that you configure a retry strategy on your Connect Customer clients to automatically retry operations after a brief waiting period. For more information, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide*.