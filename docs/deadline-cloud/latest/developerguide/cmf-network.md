

# Worker host data flow for customer-managed fleets
<a name="cmf-network"></a>

This topic describes the network connections that AWS Deadline Cloud (Deadline Cloud) worker hosts make during operation, including the endpoints contacted, protocols used, and data transmitted. This information applies to customer-managed fleet (CMF) workers, including both Amazon Elastic Compute Cloud (Amazon EC2) instances and on-premises workers. Use this information to configure firewall rules, create VPC endpoints, perform security audits, or plan network policies for your worker hosts. For information about service-managed fleet networking, see [Inter-network traffic privacy](inter-network-traffic-privacy.md).

All worker communication is outbound only. Worker hosts initiate all connections—you don't need to allow any inbound connections. All connections use HTTPS (TLS 1.2 or later) over port 443.

This topic includes the following sections:
+ [Endpoints and protocols](#cmf-network-endpoints)
+ [API operations used by workers](#cmf-network-apis)
+ [Other data transmitted](#cmf-network-other)
+ [Private connectivity options](#cmf-network-private-connectivity)

## Endpoints and protocols
<a name="cmf-network-endpoints"></a>

The following table lists the AWS service endpoints that worker hosts connect to during operation. For the complete list of regional endpoints for each service, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) in the *AWS General Reference*.


**Worker host endpoint reference**  

| AWS service | Endpoint | Port / Protocol | Purpose | Required | 
| --- | --- | --- | --- | --- | 
| [Deadline Cloud](https://docs.aws.amazon.com/general/latest/gr/deadlinecloud.html) (scheduling) | scheduling.deadline.{{[Region]}}.amazonaws.com | 443 / HTTPS | Worker registration, task polling, status updates, credential exchange, job entity retrieval. See [API operations used by workers](#cmf-network-apis). | Always | 
| [Amazon CloudWatch Logs](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html) (CloudWatch Logs) | logs.{{[Region]}}.amazonaws.com | 443 / HTTPS | Worker agent and session log delivery. | Always | 
| [Amazon Simple Storage Service](https://docs.aws.amazon.com/general/latest/gr/s3.html) (Amazon S3) | s3.{{[Region]}}.amazonaws.com | 443 / HTTPS | Job attachment upload and download. | If using job attachments | 

If your jobs use other AWS services, you might also need to allow outbound connections to those service endpoints.

## API operations used by workers
<a name="cmf-network-apis"></a>

All of the following API operations use the `scheduling.deadline.{{[Region]}}.amazonaws.com` endpoint. For the complete request and response schemas of each operation, see the [Deadline Cloud API Reference](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/Welcome.html).

### Bootstrap phase
<a name="cmf-network-bootstrap"></a>

When a worker host starts, the worker agent registers with the fleet. The bootstrap credentials require the permissions in the `AWSDeadlineCloud-WorkerHost` AWS managed policy, or equivalent custom permissions. The bootstrap phase uses the following API operations:
+ [`CreateWorker`](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateWorker.html) – Registers the worker with the fleet. Sends the host name and IP addresses. Receives a worker ID.
+ [`AssumeFleetRoleForWorker`](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeFleetRoleForWorker.html) – Obtains fleet role credentials. Receives temporary AWS credentials that the worker agent uses for subsequent operations.

### Operational phase
<a name="cmf-network-operational"></a>

After bootstrap, the worker agent polls for work and processes sessions. The fleet role requires the permissions in the `AWSDeadlineCloud-FleetWorker` AWS managed policy, or equivalent custom permissions, and uses the following API operations:
+ [`UpdateWorker`](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateWorker.html) – Updates the worker status, for example to `STOPPED` during shutdown.
+ [`UpdateWorkerSchedule`](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateWorkerSchedule.html) – Polls for work assignments. Sends session action status updates including completion status, progress percent, progress message, and output manifest hashes. Receives assigned sessions (job ID, queue ID, session actions, log configuration), cancellation requests, desired worker status, and the update interval.
+ [`BatchGetJobEntity`](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetJobEntity.html) – Fetches job details for assigned work. Sends job entity identifiers. Receives job details, environment details, and job attachment details.
+ [`AssumeFleetRoleForWorker`](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeFleetRoleForWorker.html) – Periodically refreshes fleet role credentials.
+ [`AssumeQueueRoleForWorker`](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeQueueRoleForWorker.html) – Obtains queue role credentials scoped to a specific queue. The worker uses these credentials to access job attachments in Amazon S3.

## Other data transmitted
<a name="cmf-network-other"></a>

In addition to the Deadline Cloud scheduling API operations, worker hosts transmit the following data to other AWS services:

**Log data**  
The worker agent sends worker agent logs and session logs (stdout and stderr from job processes) to CloudWatch Logs using the `PutLogEvents` API operation.

**Job attachments**  
Workers transfer input and output files through Amazon S3 using `GetObject` and `PutObject` API operations. The worker uses queue role credentials obtained through `AssumeQueueRoleForWorker` for this access.

**Telemetry (optional)**  
The worker agent sends operational metrics such as crash reports. You can opt out of telemetry collection. For more information, see [Opt out](opt-out.md).

## Private connectivity options
<a name="cmf-network-private-connectivity"></a>

You can use AWS PrivateLink to keep traffic between CMF worker hosts and Deadline Cloud within your VPC, without traversing the public internet. For on-premises workers, you can combine AWS PrivateLink with AWS Direct Connect (Direct Connect) or a VPN connection. For more information, see [Access AWS Deadline Cloud using an interface endpoint (AWS PrivateLink)](vpc-interface-endpoints.md).