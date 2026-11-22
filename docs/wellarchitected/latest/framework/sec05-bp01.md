

# SEC05-BP01 Create network layers

 Group your workload components into network layers based on their data sensitivity and access needs. Separate components that must accept traffic from the internet, such as public web endpoints, from those that only communicate internally, such as databases. This grouping creates boundaries where you place controls to restrict the paths an unauthorized user can take toward sensitive systems. 

 **Desired outcome:** 
+  Your network layers reflect the data sensitivity, function, and behavior of the components within them. 
+  You keep components that require inbound access from the internet isolated from components that only need internal access. 
+  You place control points at each layer boundary, so only authorized traffic crosses between layers. 
+  Your network design complements the identity and access controls of your workload as part of a defense-in-depth strategy. 

 **Common anti-patterns:** 
+  Teams place all resources in a single VPC or subnet with no internal boundaries. 
+  Teams design network layers without considering data sensitivity, component behavior, or function. 
+  Teams treat VPCs and subnets as the only layering mechanism and overlook how managed services change the topology. 
+  Teams expose internal components directly to the internet because no boundary separates public and private resources. 

 **Benefits of establishing this best practice:** 
+  Restricting the paths through your network makes it harder for an unauthorized user to reach critical systems and data. 
+  Discrete layers narrow the scope that inspection systems must analyze, which lowers false positives and processing overhead. 
+  Isolating components with unusual behavior prevents their traffic from triggering false alerts elsewhere. 
+  Clear boundaries make it easier to reason about which controls apply where. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Network layering is a defense-in-depth technique that works alongside identity controls. While identity answers who can call an action, network layers decide which components can reach each other. When you place boundaries between groups of components, you reduce the number of paths available to someone with unauthorized access to one part of the workload. In a flat network where every resource can reach every other resource, a single point of unauthorized access exposes everything. 

 Function, data sensitivity, and behavior shape how you group components. Presentation, application, and data responsibilities often warrant separate controls. Two services in the same functional tier may process data at different classification levels and belong in separate layers. For example, a service that accepts file uploads, runs submitted scripts, or scans inbound email is riskier than one that does not, and isolating it contains that risk. Balance these aspects against operational cost. 

 Subnets within a single VPC are simple to operate but share the same account boundary and routing domain. Separate VPCs provide stronger separation and independent routing, at the cost of more connectivity to manage. Separate accounts provide the strongest boundary, because account separation limits the reach of exposed credentials and misconfigured policies, but they add the most operational overhead. Match the strength of the boundary to the sensitivity of what it protects. 

 Fully managed data stores and serverless functions do not always run inside your subnets by default, so a topology drawn only around VPCs and subnets can leave gaps. Plan for private connectivity to these services so that traffic stays off public paths. [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) and [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) keep access to services such as [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), and [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) on private addresses, and [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) can simplify how components communicate across layers. Every [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function runs inside an isolated, AWS-managed VPC by default, with access to the public internet and AWS public endpoints. VPC attachment removes that default internet path unless you also provision a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html). Reserve VPC attachment for Lambda functions that need to reach VPC-resident resources, such as an [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) instance in a private subnet. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Group your components into layers:** Review your workload architecture and group components by the function they serve, the sensitivity of the data they process, and how they behave. Decide for each group whether a subnet, a separate [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html), or a separate account provides the right boundary. 

1.  **Front public components with managed endpoints:** For components that respond to internet requests, place a load balancer or proxy in front of them to provide the public endpoint. Use managed services such as [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html), [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html), [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html), and [AWS Amplify](https://docs.aws.amazon.com/amplify/) to shift security controls off your own compute. 

1.  **Place compute in private subnets:** Deploy compute such as Amazon EC2 instances and [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) tasks into private subnets according to the groups you defined, and keep these components off public subnets unless they must accept direct inbound traffic. For AWS Lambda, attach a function to your VPC only when it needs to reach a VPC-resident resource, since functions are isolated by default without any VPC configuration. 

1.  **Reach managed services over private connectivity:** For fully managed services such as Amazon DynamoDB, Amazon Kinesis, and Amazon SQS, use VPC endpoints as the default so access flows over private IP addresses instead of the public internet. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC05-BP02 Control traffic flow within your network layers](sec05-bp02.md) 
+  [SEC05-BP03 Implement inspection-based protection](sec05-bp03.md) 
+  [SEC05-BP04 Automate network protection](sec05-bp04.md) 
+  [FND07-BP01 Define your network and connectivity strategy and centralized resources](fnd07-bp01.md) 
+  [PERF04-BP01 Understand how networking impacts performance](perf04-bp01.md) 

 **Related documents:** 
+  [VPC examples](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-examples-intro.html) 
+  [Giving Lambda functions access to resources in an Amazon VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html) 
+  [Enable internet access for VPC-connected Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-internet.html) 
+  [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - AWS Networking Fundamentals: Connect, secure and scale (NET208)](https://www.youtube.com/watch?v=nXBqxnp5ybY) 

 **Related examples:** 
+  [Access container applications privately on Amazon ECS by using AWS Fargate, AWS PrivateLink, and a Network Load Balancer](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-container-applications-privately-on-amazon-ecs-by-using-aws-fargate-aws-privatelink-and-a-network-load-balancer.html) 
+  [Serve static content in an Amazon S3 bucket through a VPC by using Amazon CloudFront](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront.html) 

 **Related services:** 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 
+  [Amazon VPC Lattice](https://aws.amazon.com/vpc/lattice/) 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 