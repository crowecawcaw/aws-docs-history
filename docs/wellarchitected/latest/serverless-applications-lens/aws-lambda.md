

# AWS Lambda
<a name="aws-lambda"></a>

Provisioned concurrency initializes a requested number of execution environments so that they are prepared to respond immediately to your function's invocations. To enable your function to scale without fluctuations in latency, use provisioned concurrency. By allocating provisioned concurrency before an increase in invocations, you can ensure that all requests are served by initialized instances with very low latency. AWS Lambda also integrates with [*Application Auto Scaling*](https://docs.aws.amazon.com/autoscaling/application/userguide/). You can configure Application Auto Scaling to manage provisioned concurrency on a schedule or based on utilization. Use scheduled scaling to increase provisioned concurrency in anticipation of peak traffic. 

![Chart of function scaling with provisioned concurrency](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/function-scaling-with-provisioned-concurrency.png)


To optimize latency, you can customize the initialization behavior for functions that use provisioned concurrency. You can run initialization code for provisioned concurrency instances without impacting latency, because the initialization code runs at allocation time. Configure Amazon VPC access to your Lambda functions only when necessary. Set up a NAT gateway if your VPC-enabled Lambda function needs access to the Internet. Be sure to check both the Security Group and network Access Control List (ACL) to allow outbound requests from your Lambda function. As covered in the AWS Well-Architected Framework, configure your NAT gateway, or NAT instances across multiple Availability Zones for high availability and performance. This decision tree can help you decide when to deploy your Lambda function in a VPC. 

![Decision tree for deploying a AWS Lambda function in an Amazon VPC](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/decision-tree-aws-lambda-function-in-amazon-vpc.png)


For Lambda functions in VPC, avoid DNS resolution of public host names for underlying resources in your VPC. For example, if your Lambda function accesses an Amazon RDS DB instance in your VPC, launch the instance with the no-publicly-accessible option. 