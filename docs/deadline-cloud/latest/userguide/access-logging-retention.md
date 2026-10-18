

# Access, logging, and data retention in Deadline Cloud
<a name="access-logging-retention"></a>

Many of the security controls for a Deadline Cloud farm sit outside Deadline Cloud: in your identity provider (IdP), in your AWS account, or with AWS itself. The following sections describe how authentication, sessions, logging, data retention, and AWS access work for a farm, name the layer that owns each control, and link to where you configure it. Use the sections you need, whether you're answering a security questionnaire or looking for where a setting lives.

For information about components, network ports, protocols, and encryption, see [Data flow, ports, and encryption in Deadline Cloud](security-data-flow.md). For information about permissions, service roles, and workload isolation, see [Security controls in Deadline Cloud](security-controls.md).

## Authentication, sessions, and credentials
<a name="authentication-sessions"></a>

Deadline Cloud holds no user directory and stores no passwords. People sign in to the Deadline Cloud monitor through AWS IAM Identity Center (IAM Identity Center), which either holds your users in its own directory or federates to your existing IdP. Password strength, multi-factor authentication (MFA), account lockout, password reset, and sign-in error handling are therefore properties of the directory that holds your users, not of Deadline Cloud.

The following table lists where each authentication control is configured.


**Authentication and session controls, and where they're configured**  

| Control | Where it's configured | More information | 
| --- | --- | --- | 
| User directory and password storage | The IAM Identity Center directory, or your external IdP. Deadline Cloud never receives or stores a password. | [Understanding your identity source](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/understanding-identity-source.html) in the *Deadline Cloud User Guide* | 
| MFA | IAM Identity Center, or your external IdP when you federate. IAM Identity Center supports authenticator apps, security keys, and built-in authenticators, and you choose whether to prompt every sign-in or only on new devices. | [MFA for Identity Center directory users](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-mfa.html) in the *AWS IAM Identity Center User Guide* | 
| Password policy, lockout, and password reset | The directory that holds your users. When you federate to your own IdP, your existing policy applies without change. | [Password requirements when managing identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/password-requirements.html) in the *AWS IAM Identity Center User Guide* | 
| Sign-in session duration | IAM Identity Center session settings, which control how long a person can work before they sign in again. Deadline Cloud adds no idle timeout of its own. | [Configure IAM Identity Center session duration](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-user-session.html) in the *AWS IAM Identity Center User Guide* | 
| Ending a session early | IAM Identity Center. Ending a person's active sessions signs them out. Removing their farm, queue, and fleet permissions removes their access to those resources. To also prevent them from signing in to the monitor, enable **Require assignments** for the monitor application and remove their assignment, or disable the user in your identity source. Monitor credentials that they already hold stay valid for up to 15 minutes. | [View and end active sessions for your workforce users](https://docs.aws.amazon.com/singlesignon/latest/userguide/end-active-sessions.html) in the *AWS IAM Identity Center User Guide* | 
| Who can see which farm | Deadline Cloud access levels, assigned per farm, queue, and fleet to IAM Identity Center users and groups. A new user sees nothing until you grant access. | [Managing users](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/managing-users.html) in the *Deadline Cloud User Guide* | 
| Programmatic access for pipelines and automation | IAM in your account. Grant an IAM role rather than creating long-lived access keys. | [Identity and Access Management in Deadline Cloud](security-iam.md) | 

After a person signs in through the monitor, Deadline Cloud issues temporary credentials instead of a long-lived secret. Each set of credentials has an expiration time. The monitor keeps these credentials current, and client tools can use its profile, as follows:
+ The Deadline Cloud monitor desktop application creates a named AWS profile on the workstation and keeps the credentials for that profile current while the application runs. When the CLI and integrated submitters use that profile, they read its temporary credentials instead of storing separate credentials. For more information, see [Set up an integrated submitter](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/submitter.html) in the *Deadline Cloud User Guide*.
+ To reach the files and logs for a queue, the client tools call `AssumeQueueRoleForUser` or `AssumeQueueRoleForRead`. Those calls return temporary credentials for the queue role. Workers call `AssumeFleetRoleForWorker` and `AssumeQueueRoleForWorker`. No client or worker holds standing access to the Amazon S3 bucket or the log groups. For more information, see [Service roles](security-iam-service-roles.md).
+ When a submitter uses the monitor-created profile, a check made at sign-in, such as an MFA prompt or a device posture check, isn't repeated for each job submission.

The workstation holds the credential cache for the profile on local disk. Deadline Cloud doesn't encrypt workstation disks, so workstation disk encryption is the control that protects the cache. For related guidance, see [Secure artist workstations](workstations.md).

## Restricting access by network, IP address, or device
<a name="conditional-access"></a>

Deadline Cloud has no IP allowlist or managed-device setting of its own. You have three places to enforce conditional access, and they apply at different moments:
+ **At sign-in, in your IdP or IAM Identity Center** – Device trust, IP address ranges, geographic restrictions, and risk-based policies. Enforcement happens when the person authenticates. This covers the monitor and any CLI or submitter session that uses the monitor-created profile.
+ **On each API call, with IAM policy conditions** – Attach condition keys such as `aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, and `aws:PrincipalOrgID` to the identity-based or role policies that grant Deadline Cloud permissions. Enforcement happens on every request, including requests from pipeline automation. For each key and the circumstances in which it's available, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *AWS Identity and Access Management User Guide*.
+ **On the network path, with AWS PrivateLink** – Interface endpoints keep traffic between your VPC and Deadline Cloud off the public internet. Combine them with an `aws:SourceVpce` condition to require that requests arrive through your endpoint. For more information, see [Access AWS Deadline Cloud using an interface endpoint (AWS PrivateLink)](vpc-interface-endpoints.md).

## Audit and access logging sources
<a name="audit-logging-sources"></a>

Every customer-facing audit and workload log described here lands in your AWS account, under your IAM access control and your retention settings. Some sources are on by default. Others you turn on yourself. The following table lists what each source records, whether it's on by default, and how long it keeps events.


**Audit and access logging sources for a Deadline Cloud farm**  

| Source | What it records | On by default | Retention | 
| --- | --- | --- | --- | 
| AWS CloudTrail management events | The Deadline Cloud control-plane operations that CloudTrail classifies as management events, including `CreateFarm`, `UpdateQueue`, and `DeleteFleet`, with the identity, source IP address, and timestamp. IAM Identity Center records sign-in events the same way. | Yes | 90 days in CloudTrail Event history. Create a trail or an event data store to keep events longer. | 
| CloudTrail data events for Deadline Cloud | High-volume read and write operations on Deadline Cloud job resources, including `CreateJob`, `UpdateJob`, `UpdateStep`, `UpdateTask`, and `UpdateSession`. | No | For a trail, the lifecycle configuration of its destination Amazon S3 bucket. For an event data store, the retention period that you configure. Charges apply. | 
| CloudTrail data events for the job attachments bucket | Per-object reads and writes in the queue's Amazon S3 bucket, which record who downloaded or uploaded which file. | No | For a trail, the lifecycle configuration of its destination Amazon S3 bucket. For an event data store, the retention period that you configure. Charges apply. | 
| Amazon S3 server access logs | An alternative per-request record for the job attachments bucket, delivered to a bucket that you choose. | No | The lifecycle configuration of the destination bucket. | 
| Amazon CloudWatch Logs | Session logs for each job, which hold the output of the processes the job runs, and worker logs for each worker host. | Yes | Logs persist until you set a retention period on the log group. | 

For the Deadline Cloud operations that CloudTrail records and the resource types that support data events, see [Logging Deadline Cloud API calls using AWS CloudTrail](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/logging-using-cloudtrail.html) in the *Deadline Cloud Developer Guide*. For log group retention and the metrics you can alarm on, see [Monitoring with CloudWatch](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/monitoring-cloudwatch.html) in the same guide.

Deadline Cloud doesn't ship alarms for patterns such as repeated sign-in failures or access from an unfamiliar IP address. Build the detections your security team needs on the CloudTrail trail, and consider AWS Security Hub CSPM to cover the account as a whole.

The processes that a job runs write their output to the session log, so a job that prints a secret records the secret. Jobs submitted from the Deadline Cloud submitters and the CLI log job progress rather than credentials. When you write your own jobs, keep secrets out of the output that your processes print.

## Data retention and deletion
<a name="data-retention-deletion"></a>

Your farm's data sits in two places. Deleting a Deadline Cloud resource affects only the first:
+ **Inside the service** – Farm, queue, fleet, job, step, and task records, which are the scheduling data for your farm. Farms, queues, and fleets remain until you delete them. Deadline Cloud removes each job, with its steps and tasks, 120 days after it was submitted. For more information, see [Processing Deadline Cloud jobs](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/jobs-processing.html) in the *Deadline Cloud User Guide*. When you delete a queue, Deadline Cloud also deletes its jobs, steps, and tasks. After a resource is deleted, its records aren't available through the Deadline Cloud APIs. For assurance about AWS-controlled retention after deletion, use the applicable audit reports described in [Service internals, AWS access, and audit reports](#service-internals).
+ **In your AWS account** – The input and output files in the job attachments bucket, and the session and worker logs in CloudWatch Logs. Deleting a queue or a farm doesn't delete the Amazon S3 objects or the log groups, so they remain until you delete them or a retention rule expires them.

To control how long each of the two lives, use the following:
+ For job attachments, apply an Amazon S3 Lifecycle configuration to expire objects. For more information, see [Managing job attachments in S3 buckets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/storage-job-attachments.html#storage-job-attachments-s3-lifecycle) in the *Deadline Cloud User Guide*.
+ For logs, set a retention period on each log group, or export the logs you need to keep to Amazon S3 and expire the log group sooner.
+ To remove a farm's data from the service, delete its queues and fleets, then delete the farm. If you created the farm with a customer managed key, you can also schedule deletion of that key so that any remaining farm data can't be decrypted. Job attachments and log groups use their own encryption settings. For more information, see [Key management](key-management.md).

Deadline Cloud doesn't replicate scheduling data or job attachments to another AWS Region on your behalf. For the resilience characteristics of each, see [Resilience in Deadline Cloud](disaster-recovery-resiliency.md).

## Service internals, AWS access, and audit reports
<a name="service-internals"></a>

Some vendor security questionnaires ask about implementation details of the AWS service rather than settings in your deployment. Examples include the name of the database, the TLS cipher suites, the HTTP security headers, input validation, deserialization, protection against injection, and how AWS patches the fleet that runs the service. These details are part of AWS's responsibility under the shared responsibility model. For implementation details that AWS doesn't publish, use the applicable audit reports and compliance resources.

AWS Deadline Cloud is in scope for SOC 1, SOC 2, and SOC 3. A reviewer who needs assurance about AWS controls for the service should read the SOC reports, which you can download from AWS Artifact with an AWS account. For the reports and the other compliance resources, see [Compliance validation for Deadline Cloud](deadline-compliance.md).

The following points answer the questions that come up most often about the boundary between your account and the service:
+ **Access to your files and logs** – The job attachments bucket and the log groups are resources in your AWS account. Access to them comes from the IAM policies and the queue role that you configure, and you can record that access with the logging sources in [Audit and access logging sources](#audit-logging-sources). For the permissions that each role grants, see [Service roles](security-iam-service-roles.md).
+ **Access to your scheduling data** – The service holds your farm, queue, and job records, and the Deadline Cloud API is the only way to reach them. There's no query interface and no database endpoint. AWS personnel access to production systems is one of the controls covered by the SOC reports.
+ **Onboarding an outside studio or vendor** – Give them access to their own farm or queue, each with its own job attachments bucket. The access they get then covers only the work you're sharing. For the isolation options, see [Isolate workloads with farms, fleets, and queues](farm-structure.md).
+ **Penetration testing** – You can test the resources in your own account, including customer-managed fleet worker hosts, within the AWS customer support policy for penetration testing. That policy also lists the tests that require prior approval. For more information, see [Penetration Testing](https://aws.amazon.com/security/penetration-testing/).
+ **Reporting a vulnerability** – Report a suspected vulnerability in Deadline Cloud, in the submitters, or in the worker agent to AWS security. For more information, see [Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/).