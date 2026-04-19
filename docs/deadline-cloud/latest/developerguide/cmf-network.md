# Worker host data flow for customer-managed fleets

This topic describes the network connections that AWS Deadline Cloud (Deadline Cloud) worker hosts make during
operation, including the endpoints contacted, protocols used, and data transmitted. This
information applies to customer-managed fleet (CMF) workers, including both Amazon Elastic Compute Cloud (Amazon EC2)
instances and on-premises workers. Use this information to configure firewall rules, create VPC
endpoints, perform security audits, or plan network policies for your worker hosts. For
information about service-managed fleet networking, see
[Inter-network traffic privacy](inter-network-traffic-privacy.md "inter-network-traffic-privacy.md").

All worker communication is outbound only. Worker hosts initiate all
connections—you don't need to allow any inbound connections. All connections use HTTPS
(TLS 1.2 or later) over port 443.

This topic includes the following sections:

- [Endpoints and protocols](#cmf-network-endpoints "#cmf-network-endpoints")
- [API operations used by workers](#cmf-network-apis "#cmf-network-apis")
- [Other data transmitted](#cmf-network-other "#cmf-network-other")
- [Private connectivity options](#cmf-network-private-connectivity "#cmf-network-private-connectivity")

## Endpoints and protocols

The following table lists the AWS service endpoints that worker hosts connect to during
operation. For the complete list of regional endpoints for each service, see the [Service endpoints and
quotas](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md") in the _AWS General Reference_.

| Worker host endpoint reference                                                                                                  | AWS service                                    | Endpoint    | Port / Protocol                                                                                                                                                               | Purpose                  | Required |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | -------- |
| [Deadline Cloud](../../../general/latest/gr/deadlinecloud.md "../../../general/latest/gr/deadlinecloud.md") (scheduling)        | `scheduling.deadline.`[Region]`.amazonaws.com` | 443 / HTTPS | Worker registration, task polling, status updates, credential exchange, job entity<br>retrieval. See [API operations used by workers](#cmf-network-apis "#cmf-network-apis"). | Always                   |
| [Amazon CloudWatch Logs](../../../general/latest/gr/cwl_region.md "../../../general/latest/gr/cwl_region.md") (CloudWatch Logs) | `logs.`[Region]`.amazonaws.com`                | 443 / HTTPS | Worker agent and session log delivery.                                                                                                                                        | Always                   |
| [Amazon Simple Storage Service](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md") (Amazon S3)                | `s3.`[Region]`.amazonaws.com`                  | 443 / HTTPS | Job attachment upload and download.                                                                                                                                           | If using job attachments |

If your jobs use other AWS services, you might also need to allow outbound connections to
those service endpoints.

## API operations used by workers

All of the following API operations use the
`scheduling.deadline.`[Region]`.amazonaws.com` endpoint. For
the complete request and response schemas of each operation, see the
[Deadline Cloud API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

### Bootstrap phase

When a worker host starts, the worker agent registers with the fleet. The bootstrap
credentials require the permissions in the
`AWSDeadlineCloud-WorkerHost` AWS managed policy, or equivalent custom
permissions. The bootstrap phase uses the following API operations:

- [`CreateWorker`](../APIReference/API_CreateWorker.md "../APIReference/API_CreateWorker.md")
  – Registers the worker with the fleet. Sends the host name and IP addresses. Receives
  a worker ID.
- [`AssumeFleetRoleForWorker`](../APIReference/API_AssumeFleetRoleForWorker.md "../APIReference/API_AssumeFleetRoleForWorker.md")
  – Obtains fleet role credentials. Receives temporary AWS credentials that the worker
  agent uses for subsequent operations.

### Operational phase

After bootstrap, the worker agent polls for work and processes sessions. The fleet role
requires the permissions in the `AWSDeadlineCloud-FleetWorker` AWS managed policy,
or equivalent custom permissions, and uses the following API operations:

- [`UpdateWorker`](../APIReference/API_UpdateWorker.md "../APIReference/API_UpdateWorker.md")
  – Updates the worker status, for example to `STOPPED` during
  shutdown.
- [`UpdateWorkerSchedule`](../APIReference/API_UpdateWorkerSchedule.md "../APIReference/API_UpdateWorkerSchedule.md")
  – Polls for work assignments. Sends session action status updates including
  completion status, progress percent, progress message, and output manifest hashes. Receives
  assigned sessions (job ID, queue ID, session actions, log configuration), cancellation
  requests, desired worker status, and the update interval.
- [`BatchGetJobEntity`](../APIReference/API_BatchGetJobEntity.md "../APIReference/API_BatchGetJobEntity.md")
  – Fetches job details for assigned work. Sends job entity identifiers. Receives job
  details, environment details, and job attachment details.
- [`AssumeFleetRoleForWorker`](../APIReference/API_AssumeFleetRoleForWorker.md "../APIReference/API_AssumeFleetRoleForWorker.md")
  – Periodically refreshes fleet role credentials.
- [`AssumeQueueRoleForWorker`](../APIReference/API_AssumeQueueRoleForWorker.md "../APIReference/API_AssumeQueueRoleForWorker.md")
  – Obtains queue role credentials scoped to a specific queue. The worker uses these
  credentials to access job attachments in Amazon S3.

## Other data transmitted

In addition to the Deadline Cloud scheduling API operations, worker hosts transmit the following
data to other AWS services:

**Log data**

The worker agent sends worker agent logs and session logs
(stdout and stderr from job processes) to CloudWatch Logs using the
`PutLogEvents` API operation.

**Job attachments**

Workers transfer input and output files
through Amazon S3 using `GetObject` and `PutObject` API
operations. The worker uses queue role credentials obtained through
`AssumeQueueRoleForWorker` for this access.

**Telemetry (optional)**

The worker agent sends
operational metrics such as crash reports. You can opt out of telemetry collection. For more
information, see [Opt out](opt-out.md "opt-out.md").

## Private connectivity options

You can use AWS PrivateLink to keep traffic between CMF worker hosts and Deadline Cloud within your VPC,
without traversing the public internet. For on-premises workers, you can combine AWS PrivateLink
with AWS Direct Connect (Direct Connect) or a VPN connection. For more information, see
[Access AWS Deadline Cloud using an interface endpoint (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
