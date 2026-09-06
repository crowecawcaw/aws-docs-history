

# Security controls in Deadline Cloud
<a name="security-controls"></a>

A render farm runs jobs from many people on shared infrastructure. Artists submit scenes, worker hosts run them, and the results land in shared storage. AWS Deadline Cloud gives you a set of controls to decide who can see and change farm resources, what jobs can do while they run, and how workloads stay separate from each other.

Three questions organize the controls:
+ **Who can see and manage farm resources?** Monitor users with access levels, and IAM policies for the console and API.
+ **What can the service, workers, and jobs do on your behalf?** The IAM service roles for fleets, worker hosts, queues, and monitors.
+ **How are workloads kept separate?** Farm and queue structure, operating system users for jobs, and per-queue job attachment buckets.

The following table maps each control to what it governs and where to learn more.


**Security controls in Deadline Cloud**  

| Control | What it governs | More information | 
| --- | --- | --- | 
| Monitor users and access levels | Which people can see each farm, queue, and fleet in the monitor, and whether they can view, contribute, manage, or own those resources. Users come from AWS IAM Identity Center (IAM Identity Center). | [Managing users](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/managing-users.html) in the *Deadline Cloud User Guide* | 
| IAM identity-based policies | What people and tools with AWS credentials can do with the Deadline Cloud console and API, such as creating farms or submitting jobs from a pipeline. | [Identity and Access Management in Deadline Cloud](security-iam.md) | 
| Service roles | What Deadline Cloud can do on your behalf. The fleet, worker host, queue, and monitor roles each grant a different part of the service a scoped set of permissions. | [Service roles](security-iam-service-roles.md) | 
| Queue operating system user | The operating system permissions that job processes have on worker hosts. On a customer-managed fleet, give each queue its own OS user. On a service-managed fleet, all jobs run as one service-managed user; separate queues by giving them separate fleets. | [Run jobs as dedicated OS users](job-run-as-user.md) | 
| Farm and queue structure | The isolation boundaries between workloads. Farms don't share Deadline Cloud resources with each other, and queues within a farm can be separated by fleet, OS user, and bucket. | [Isolate workloads with farms, fleets, and queues](farm-structure.md) | 
| Job attachment buckets | Which Amazon S3 data each queue can read and write through its queue role, bucket, and root prefix. | [Secure job attachment and software buckets](job-attachment-queues.md) | 
| Encryption keys | How farm data is encrypted at rest, with an AWS owned key or a customer managed AWS KMS key. | [Key management](key-management.md) | 
| Network controls | How traffic reaches Deadline Cloud: private connectivity with AWS PrivateLink, and the endpoints to allowlist in restricted networks. | [Access AWS Deadline Cloud using an interface endpoint (AWS PrivateLink)](vpc-interface-endpoints.md), [Restricted network environments](network-connectivity.md) | 

## Where to start
<a name="security-controls-choose"></a>

Pick the entry point that matches your role:
+ If you administer a studio and want to control which artists see which projects, start with [Managing users](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/managing-users.html) and the [Isolate workloads with farms, fleets, and queues](farm-structure.md) guidance.
+ If you build pipelines that submit jobs or read results, start with [Identity-based policy examples for Deadline Cloud](security_iam_id-based-policy-examples.md) and [Secure job attachment and software buckets](job-attachment-queues.md).
+ If you want to control what jobs can access while they run, start with [Run jobs as dedicated OS users](job-run-as-user.md) for OS permissions and [Service roles](security-iam-service-roles.md) for the queue role that grants AWS permissions.
+ If you run customer-managed fleets, start with [Service roles](security-iam-service-roles.md) and [Secure worker hosts](worker-hosts.md).