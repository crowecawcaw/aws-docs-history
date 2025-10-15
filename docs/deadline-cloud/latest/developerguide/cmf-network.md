# Configure networking to allow AWS endpoint connections

Deadline Cloud requires secure connectivity to various AWS service endpoints for proper
 operation. To use Deadline Cloud, you must make sure that your network environment allows your Deadline Cloud
 workers to connect to these endpoints.

If you have a network firewall setup that blocks outbound connections, you may need to add
 firewall exceptions for specific endpoints. For Deadline Cloud, you must add exceptions for the
 following services:


* [Deadline Cloud
 endpoints](https://docs.aws.amazon.com/general/latest/gr/deadlinecloud.html "https://docs.aws.amazon.com/general/latest/gr/deadlinecloud.html")
* [Amazon CloudWatch Logs
 endpoints](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html "https://docs.aws.amazon.com/general/latest/gr/cwl_region.html")
* [Amazon Simple Storage Service
 endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html "https://docs.aws.amazon.com/general/latest/gr/s3.html")
If your jobs use other AWS services, you may need to add exceptions for those services
 as well. You can find these endpoints in the [Service endpoints and
 quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html "https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html") chapter of the *AWS General Reference* guide. After
 you identify the required endpoints, create outbound rules in your firewall to permit
 traffic to these specific endpoints.

Making sure that these endpoints are accessible is required for proper operation.
 Additionally, consider implementing appropriate security measures, such as using virtual
 private clouds (VPCs), security groups, and network access control lists (ACLs) to maintain
 a secure environment while allowing the required Deadline Cloud traffic.
