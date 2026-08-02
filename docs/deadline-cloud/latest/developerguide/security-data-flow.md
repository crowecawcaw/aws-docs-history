# Data flow, ports, and encryption in Deadline Cloud

Content security reviews, such as studio security audits and vendor onboarding
questionnaires, ask for a data flow diagram. The diagram covers the components of the
render farm, where each component runs, how data moves between them, and how connections
and stored data are encrypted. The diagram and tables on this page answer those questions
for a typical AWS Deadline Cloud deployment. For more information about the security controls that
you can configure for each part of the farm, see [Security controls in Deadline Cloud](security-controls.md "security-controls.md").

![Data flow between your network and the AWS Cloud, where your AWS account and Deadline Cloud sit side by side. Numbered flows show sign-in, job submission, file upload and download, task scheduling and credential requests, and job and worker logs. Customer-managed fleet workers span your network and your AWS account because they can run in either location. All flows are outbound HTTPS connections on TCP port 443, and the tables on this page describe each component and flow.](images/deadline-cloud-data-flow.png)

## Components and where they run

A Deadline Cloud render farm spans three locations: your network, your AWS account, and
Deadline Cloud itself, which AWS manages. Customer-managed fleet workers are the exception: you
choose where they run.

The following table describes each component and where it runs.

| Component                                                                 | Where it runs                                                                                   | Purpose                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deadline Cloud monitor, integrated submitters, and the Deadline Cloud CLI | Your network                                                                                    | Client tools on artist workstations that submit jobs, upload and download<br>files, and track job progress.                                                                                                                                                                                                    |
| AWS IAM Identity Center                                                   | Your AWS account                                                                                | Sign-in and access levels for monitor users. For more information, see<br>[Managing users](../userguide/managing-users.md "../userguide/managing-users.md").                                                                                                                                                   |
| Amazon Simple Storage Service job attachments bucket                      | Your AWS account                                                                                | Input and output files for jobs. Each queue has its own bucket and root<br>prefix, so queue permission boundaries also apply to files.                                                                                                                                                                         |
| Amazon CloudWatch Logs                                                    | Your AWS account                                                                                | Job logs and worker logs.                                                                                                                                                                                                                                                                                      |
| AWS Key Management Service key                                            | Your AWS account, or AWS managed                                                                | The key that encrypts your farm data inside Deadline Cloud. By default, Deadline Cloud uses<br>an AWS owned key that you don't manage. You can supply a customer managed key from<br>your account when you create the farm. For more information, see [Key management](key-management.md "key-management.md"). |
| Customer-managed fleet workers                                            | Your choice: machines on your network, or Amazon Elastic Compute Cloud instances in your<br>VPC | Worker hosts that you manage, running your software and the Deadline Cloud worker<br>agent. A customer-managed fleet only needs outbound HTTPS access. If workers run in<br>your VPC, optional AWS PrivateLink endpoints keep their traffic inside the<br>VPC.                                                 |
| Deadline Cloud service                                                    | AWS managed                                                                                     | The service endpoints<br>`management.deadline.`region`.amazonaws.com` and<br>`scheduling.deadline.`region`.amazonaws.com`,<br>and the farm, queue, and job scheduling data behind them.                                                                                                                        |
| Service-managed fleet workers                                             | AWS managed                                                                                     | Amazon EC2 instances on an isolated network for each fleet. The instances are<br>dedicated to your account and accept no inbound connections.                                                                                                                                                                  |

## Data flows, ports, and protocols

Every client and worker in the diagram initiates its connections outbound to an
AWS endpoint over HTTPS on TCP port 443. We require TLS 1.2 to encrypt connections in
transit, and we recommend TLS 1.3. Deadline Cloud doesn't make inbound connections to your
network. The flow numbers in the following table match the numbers in the
diagram.

| Flow | Connection                                   | Description                                                                                                                                                                 |
| ---- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Monitor to IAM Identity Center               | Monitor users sign in through AWS IAM Identity Center with OpenID Connect<br>(OIDC).                                                                                        |
| 2    | Workstation to the management endpoint       | Submitters, the CLI, and the monitor submit jobs, manage farm resources, and<br>request temporary role credentials through<br>`management.deadline.`region`.amazonaws.com`. |
| 3    | Workstation to Amazon S3                     | Job attachments uploads input files to the queue's Amazon S3<br>bucket.                                                                                                     |
| 4    | Workers to the scheduling endpoint           | Workers in both fleet types poll for tasks, report progress and status, and<br>request temporary role credentials through<br>`scheduling.deadline.`region`.amazonaws.com`.  |
| 5    | Workers to Amazon S3                         | Workers download input files from the queue's bucket and upload output<br>files to it.                                                                                      |
| 6    | Workers to CloudWatch Logs                   | The worker agent writes job and worker logs.                                                                                                                                |
| 7    | Workstation to CloudWatch Logs and Amazon S3 | The monitor reads job logs, and the monitor and CLI download output<br>files.                                                                                               |

Neither the client tools nor the workers hold long-lived credentials for the queue's
resources. Both request temporary credentials from Deadline Cloud and receive the permissions that
you attach to the queue and fleet roles:

- The monitor, the CLI, and the submitters call
  `AssumeQueueRoleForUser` to upload and download job
  attachments, and `AssumeQueueRoleForRead` for read-only access
  such as reading job logs.
- A worker calls `AssumeFleetRoleForWorker` for the fleet
  role, then `AssumeQueueRoleForWorker` for the queue role of the
  job it runs.

For more information about the roles and what each one grants, see [Service roles](security-iam-service-roles.md "security-iam-service-roles.md").

If your studio filters outbound web traffic, see [Restricted network environments](network-connectivity.md "network-connectivity.md") for the full list of endpoints to allowlist. To
keep traffic between your VPC and Deadline Cloud off the public internet, use AWS PrivateLink
interface endpoints. For more information, see [Access AWS Deadline Cloud using an interface endpoint (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

## Encryption summary

Each data store is encrypted at rest independently. The farm AWS KMS key applies only
to the data that Deadline Cloud holds; your Amazon S3 bucket and your log groups use their own
encryption settings.

- **In transit** – All connections use HTTPS with
  TLS 1.2 required and TLS 1.3 recommended. For more information, see [Encryption in transit](encryption-transit.md "encryption-transit.md").
- **Farm data** – The Deadline Cloud service encrypts your
  farm, queue, and job data at rest with the farm's AWS KMS key. You can use the default
  AWS owned key or supply a customer managed key when you create the farm. For more
  information, see [Key management](key-management.md "key-management.md").
- **Job attachments** – Amazon Simple Storage Service encrypts your
  input and output files at rest with the server-side encryption configured on the
  bucket. By default, Amazon S3 uses Amazon S3 managed keys (SSE-S3). To use your own AWS KMS key
  instead, configure the bucket for SSE-KMS and grant the queue role access to the key.
  For more information, see [Job attachments in
  Deadline Cloud](../userguide/storage-job-attachments.md "../userguide/storage-job-attachments.md").
- **Worker volumes** – In service-managed fleets,
  Deadline Cloud encrypts the Amazon Elastic Block Store volumes attached to worker instances and deletes the
  volumes when instances terminate. For more information, see [Encryption at rest](encryption-rest.md "encryption-rest.md").
- **Logs** – Amazon CloudWatch Logs encrypts job logs and
  worker logs at rest with its own server-side encryption. To use your own AWS KMS key
  instead, associate the key with the log group. For more information, see [Encrypt log data in CloudWatch Logs using AWS KMS](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the
  _Amazon CloudWatch Logs User Guide_.
