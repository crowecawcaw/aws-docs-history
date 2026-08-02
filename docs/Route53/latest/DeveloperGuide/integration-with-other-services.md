# Integration with other services

You can integrate Amazon Route 53 with other AWS services to log requests sent to the Route 53 API, monitor the status of your
resources, and assign tags to your resources. You can also use Route 53 to route internet traffic to your
AWS resources.

###### Topics

- [Logging, monitoring, and tagging](#integration-logging-monitoring-tagging "#integration-logging-monitoring-tagging")
- [Routing traffic to other AWS resources](#integration-routing-traffic "#integration-routing-traffic")

## Logging, monitoring, and tagging

**AWS CloudTrail**
Amazon Route 53 is integrated with AWS CloudTrail, a service that captures information about every request sent to the
Route 53 API by your AWS account. You can use the CloudTrail log files to see which requests were made to Route 53,
the source IP address, who made the request, and when.

For more information, see [Logging Amazon Route 53 API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**Amazon CloudWatch**
You can use Amazon CloudWatch to monitor the status—healthy or unhealthy—of your Route 53 health checks.
Health checks monitor the health and performance of your web applications, web servers, and other resources.
At regular intervals that you specify, Route 53 sends requests over the internet to your resource to verify that it's reachable and functional.

For more information, see [Monitoring health checks using CloudWatch](monitoring-health-checks.md "monitoring-health-checks.md").

**Tag Editor**
A tag is a label that you assign to an AWS resource, including Route 53 domains, hosted zones, and health checks.
Each tag consists of a key and a value, both of which you define. For example, you might assign a tag to a domain registration
that has the key "Customer" and the value "Example Corp." Tags serve many purposes. One common use
is to categorize and track your AWS costs.

For more information, see [Tagging Amazon Route 53 resources](tagging-resources.md "tagging-resources.md").

## Routing traffic to other AWS resources

You can use Amazon Route 53 to route traffic to a variety of AWS resources.

**Amazon API Gateway**
Amazon API Gateway lets you create, publish, maintain, monitor, and secure APIs at any scale. You can create APIs that access AWS
or other web services, and data stored in the AWS Cloud.

You can use Route 53 to route traffic to an API Gateway API. For more information, see
[Routing traffic to an Amazon API Gateway API by using your domain name](routing-to-api-gateway.md "routing-to-api-gateway.md").

**Amazon CloudFront**
To speed up delivery of your web content, you can use Amazon CloudFront, the AWS content delivery network (CDN).
CloudFront can deliver your entire website—including dynamic, static, streaming, and interactive content—by using
a global network of edge locations. CloudFront routes requests for your content to the edge location that gives your users
the lowest latency. You can use Route 53 to route traffic for your domain to your CloudFront distribution. For more information,
see [Routing traffic to an Amazon CloudFront distribution by using your domain name](routing-to-cloudfront-distribution.md "routing-to-cloudfront-distribution.md").

**Amazon EC2**
Amazon EC2 provides scalable computing capacity in the AWS Cloud. You can launch an EC2 instance
using a preconfigured template (an Amazon Machine Image, or AMI). The AMI includes the operating system (Linux or Microsoft Windows) and software
such as a web server or database.

If you host a website or run a web application on an EC2 instance, you can route traffic for your domain
to your server by using Route 53. For more information, see
[Routing traffic to an Amazon EC2 instance](routing-to-ec2-instance.md "routing-to-ec2-instance.md").

**AWS Elastic Beanstalk**
If you use AWS Elastic Beanstalk to deploy and manage applications in the AWS Cloud, you can use Route 53 to route DNS traffic
for your domain to an Elastic Beanstalk environment. For more information, see
[Routing traffic to an AWS Elastic Beanstalk environment](routing-to-beanstalk-environment.md "routing-to-beanstalk-environment.md").

**Elastic Load Balancing**
If you host a website on multiple Amazon EC2 instances, you can distribute traffic across the
instances by using an Elastic Load Balancing (ELB) load balancer. ELB scales the load balancer as traffic
to your website changes over time. The load balancer also monitors the health of its registered instances and
routes traffic only to healthy instances.

You can use Route 53 to route traffic for your domain to your Classic, Application, or Network Load Balancer.
For more information, see [Routing traffic to an ELB load balancer](routing-to-elb-load-balancer.md "routing-to-elb-load-balancer.md").

**Amazon Lightsail**
Amazon Lightsail provides compute, storage, and networking to deploy and manage websites,
web apps, and databases in the cloud for a low monthly price.

If you use Lightsail, you can use Route 53 to route traffic to your instance. For more information,
see [Using
Route 53 to point a domain to an Amazon Lightsail instance](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-using-route-53-to-point-a-domain-to-an-instance "https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-using-route-53-to-point-a-domain-to-an-instance").

**Amazon S3**
Amazon Simple Storage Service (Amazon S3) provides secure, durable, highly scalable cloud storage. You can configure an S3 bucket
to host a static website that can include web pages and client-side scripts. (S3 doesn't support server-side scripting.)
You can use Route 53 to route traffic to an Amazon S3 bucket. For more information, see the following topics:

- For information about routing traffic to a bucket, see
  [Routing traffic to a website that is hosted in an Amazon S3 bucket](RoutingToS3Bucket.md "RoutingToS3Bucket.md").
- For a more detailed explanation of how to host a static website in an S3 bucket, see
  [Getting started with Amazon Route 53](getting-started.md "getting-started.md").

**Amazon Virtual Private Cloud (Amazon VPC)**
An interface endpoint lets you connect to services powered by AWS PrivateLink.
These services include some AWS services, services hosted by other AWS customers and partners in their own VPCs (called
_endpoint services_), and supported AWS Marketplace partner services.

You can use Route 53 to route traffic to an interface endpoint. For more information, see
[Routing traffic to an Amazon Virtual Private Cloud interface endpoint by using your domain name](routing-to-vpc-interface-endpoint.md "routing-to-vpc-interface-endpoint.md").

**Amazon WorkMail**
If you use Amazon WorkMail for business email and Route 53 as your DNS service, you can use
Route 53 to route traffic to your Amazon WorkMail email domain. For more information, see
[Routing traffic to Amazon WorkMail](routing-to-workmail.md "routing-to-workmail.md").

For more information see [Routing internet traffic to your AWS resources](routing-to-aws-resources.md "routing-to-aws-resources.md").
