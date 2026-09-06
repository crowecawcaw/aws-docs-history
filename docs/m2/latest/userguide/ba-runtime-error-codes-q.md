

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe Runtime Error Codes related to Queue
<a name="ba-runtime-error-codes-q"></a>

Queue error codes, prefixed with `BA-Q`.


| Key | Severity | Text | Additional details | 
| --- | --- | --- | --- | 
| BA-Q0001 | Warn | Invalid value for mq.connection.pool.share. Only true is supported to enable sharing of the JMS connection pool. The default behavior is that JMS connection pool share is disabled. Set mq.connection.pool.share: true in your configuration if you want to share the JMS connection pool. Remove the property to keep JMS connection pool share disabled. |  | 
| BA-Q1001 | Error | Failed to create connection pool. Check the pool connection configuration and resource availability, and ensure proper credentials are provided. |  | 
| BA-Q1002 | Error | Error closing factory. Verify that the factory is not in use and that all associated resources have been properly released. |  | 