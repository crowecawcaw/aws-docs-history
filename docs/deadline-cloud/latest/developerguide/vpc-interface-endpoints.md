# Access AWS Deadline Cloud using an interface endpoint
 (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and AWS Deadline Cloud.
 You can access Deadline Cloud as if it were in your VPC, without the use of an internet gateway, NAT
 device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
 addresses to access Deadline Cloud.

You establish this private connection by creating an *interface
 endpoint*, powered by AWS PrivateLink. We create an endpoint network interface
 in each subnet that you enable for the interface endpoint. These are requester-managed
 network interfaces that serve as the entry point for traffic destined for Deadline Cloud.

Deadline Cloud also has dual-stack endpoints available. Dual-stack endpoints support requests over
 IPv6 and IPv4.

For more information, see [Access AWS services
 through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html "https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html") in the
 *AWS PrivateLink Guide*.


## Considerations for Deadline Cloud


Before you set up an interface endpoint for Deadline Cloud, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html "https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html") in the
 *AWS PrivateLink Guide*.


Deadline Cloud supports making calls to all of its API actions through the interface
 endpoint.


By default, full access to Deadline Cloud is allowed through the interface endpoint.
 Alternatively, you can associate a security group with the endpoint network interfaces
 to control traffic to Deadline Cloud through the interface endpoint. 


Deadline Cloud also supports VPC endpoint policies. For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html") in the
 *AWS PrivateLink Guide*.


## Deadline Cloud endpoints


Deadline Cloud uses four endpoints for access to the service using AWS PrivateLink - two for
 IPv4 and two for IPv6.


Workers use the
 `scheduling.deadline.`region`.amazonaws.com`
 endpoint to get tasks from the queue, report progress to Deadline Cloud, and to send task output
 back. If you are using a customer-managed fleet, the scheduling endpoint is the only
 endpoint that you need to create unless you are using management operations. For
 example, if a job creates more jobs, you need to enable the management endpoint to call
 the `CreateJob` operation.


The Deadline Cloud monitor uses the
 `management.deadline.`region`.amazonaws.com` to
 manage the resources in your farm, such as creating and modifying queues and fleets or
 getting lists of jobs, steps, and tasks.


Deadline Cloud also requires endpoints for the following AWS service endpoints:



* Deadline Cloud uses AWS STS to authenticate workers so that they can access job assets.
 For more information about AWS STS, see [Temporary security
 credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html") in the *AWS Identity and Access Management User
 Guide*.
* If you set up your customer-managed fleet in a subnet with no internet
 connection you must create a VPC endpoint for Amazon CloudWatch Logs so that workers can
 write logs. For more information, see [Monitoring
 with CloudWatch](../userguide/monitoring-cloudwatch.md "../userguide/monitoring-cloudwatch.md").
* If you use job attachments, you must create a VPC endpoint for Amazon Simple Storage Service (Amazon S3)
 so that workers can access the attachments. For more information, see [Job
 attachments in Deadline Cloud](../userguide/storage-job-attachments.md "../userguide/storage-job-attachments.md").

## Create endpoints for Deadline Cloud


You can create interface endpoints for Deadline Cloud using either the Amazon VPC console or the
 AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws "https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws") in the
 *AWS PrivateLink Guide*.


Create management and scheduling endpoints for Deadline Cloud using the following service
 names. Replace `region` with the AWS Region where you've
 deployed Deadline Cloud.



```
com.amazonaws.`region`.deadline.management
```


```
com.amazonaws.`region`.deadline.scheduling
```

Deadline Cloud supports dual-stack endpoints.


If you enable private DNS for the interface endpoints, you can make API requests to
 Deadline Cloud using its default Regional DNS name. For example,
 `scheduling.deadline.us-east-1.amazonaws.com` for
 worker operations, or
 `management.deadline.us-east-1.amazonaws.com` for all
 other operations.


You must also create an endpoint for AWS STS using the following service name:



```
com.amazonaws.`region`.sts
```

If your customer-managed fleet is on a subnet without an internet connection, you must
 create a CloudWatch Logs endpoint using the following service name:



```
com.amazonaws.`region`.logs
```

If you use job attachments to transfer files, you must create an Amazon S3 endpoint using
 the following service name:



```
com.amazonaws.`region`.s3
```
