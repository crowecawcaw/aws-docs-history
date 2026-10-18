

# Deploying Web Functions
<a name="web-functions-deploying"></a>

You deploy a Web Function by providing your application code as a .zip package in an Amazon S3 bucket. When you deploy a new revision, you control how traffic moves to it with deployment patterns such as canary and blue-green. For global applications, you can deploy across multiple AWS Regions behind a single endpoint, and Lambda routes each request to a Region based on network latency. Lambda doesn't guarantee that every request goes to the lowest-latency Region.

**Topics**
+ [Deploying Web Function code from Amazon S3](web-functions-code-s3.md)
+ [Deployment patterns](web-functions-deployment.md)
+ [Multi-Region deployment](web-functions-endpoint-replication.md)