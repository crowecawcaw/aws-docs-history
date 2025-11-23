# Access AWS Deadline Cloud using an interface endpoint

(AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and AWS Deadline Cloud.
You can access Deadline Cloud as if it were in your VPC, without the use of an internet gateway, NAT
device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP
addresses to access Deadline Cloud.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface
in each subnet that you enable for the interface endpoint. These are requester-managed
network interfaces that serve as the entry point for traffic destined for Deadline Cloud.

Deadline Cloud also has dual-stack endpoints available. Dual-stack endpoints support requests over
IPv6 and IPv4.

For more information, see [Access AWS services
through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the
_AWS PrivateLink Guide_.

## Considerations for Deadline Cloud

Before you set up an interface endpoint for Deadline Cloud, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the
_AWS PrivateLink Guide_.

Deadline Cloud supports making calls to all of its API actions through the interface
endpoint.

By default, full access to Deadline Cloud is allowed through the interface endpoint.
Alternatively, you can associate a security group with the endpoint network interfaces
to control traffic to Deadline Cloud through the interface endpoint.

Deadline Cloud also supports VPC endpoint policies. For more information, see [Control access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

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

The AWS SDKs and CLI automatically add the `management` and
`scheduling` prefixes to the endpoint. If you want to disable this behavior, see the
[host prefix injection](../../../sdkref/latest/guide/feature-host-prefix.md "../../../sdkref/latest/guide/feature-host-prefix.md")
section in the _AWS SDKs and Tools Reference Guide_.

Deadline Cloud also requires endpoints for the following AWS service endpoints:

- Deadline Cloud uses AWS STS to authenticate workers so that they can access job assets.
  For more information about AWS STS, see [Temporary security
  credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") in the _AWS Identity and Access Management User
  Guide_.
- If you set up your customer-managed fleet in a subnet with no internet
  connection you must create a VPC endpoint for Amazon CloudWatch Logs so that workers can
  write logs. For more information, see [Monitoring
  with CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- If you use job attachments, you must create a VPC endpoint for Amazon Simple Storage Service (Amazon S3)
  so that workers can access the attachments. For more information, see [Job
  attachments in Deadline Cloud](storage-job-attachments.md "storage-job-attachments.md").

## Create endpoints for Deadline Cloud

You can create interface endpoints for Deadline Cloud using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the
_AWS PrivateLink Guide_.

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
