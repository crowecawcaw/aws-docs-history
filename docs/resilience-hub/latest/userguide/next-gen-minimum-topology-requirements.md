

# Minimum topology requirements
<a name="next-gen-minimum-topology-requirements"></a>

To run a failure mode assessment, your service must have a topology with a data flow relationship between at least two resources.

A failure mode assessment analyzes how failures propagate through your architecture by examining the relationships between resources. Without a data flow relationship connecting at least two resources, there is no data flow to analyze. The assessment cannot produce meaningful findings.

**Valid topology (assessment can run)**

Any topology where at least two resources are connected by a data flow relationship is valid. For example:
+ An Application Load Balancer routing traffic to an Amazon ECS cluster.
+ A Lambda function reading from a DynamoDB table.
+ An Amazon SQS queue feeding messages to a Lambda function.

**Invalid topology (assessment cannot run)**

A topology with only isolated resources and no data flow relationships between them is invalid. For example, a service that discovers a single Amazon S3 bucket or several unconnected Amazon EC2 instances has no data flow for the assessment to analyze.