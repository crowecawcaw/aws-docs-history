# Migrate from Deadline 10 to AWS Deadline Cloud

A Deadline 10 farm consists of a repository file share, a MongoDB
database, and worker hosts that select their own jobs. Pools and groups organize the farm,
limits control shared resources, and event plugins and job scripts extend it. AWS Deadline Cloud
(Deadline Cloud) has equivalents for most of these concepts, but several of them moved, changed names,
or split into more focused features.

Use the tables on this page to find the Deadline Cloud equivalent of each Deadline 10 concept, then
follow the link for details.

Some equivalents depend on the fleet type. With a service-managed fleet (SMF), Deadline Cloud
provisions, scales, and operates the workers. With a customer-managed fleet (CMF), you operate
the worker hosts—in the cloud or on premises—and the service schedules work to
them. For more information, see [Deadline Cloud fleets](../userguide/manage-fleets.md "../userguide/manage-fleets.md") in the
_Deadline Cloud User Guide_.

## Farm components you no longer operate

Deadline Cloud replaces the server components of a Deadline 10 farm with a managed service. There
is no repository file share to mount, no database to back up, and no maintenance server to
run. Your farm's state lives in the service, and every application communicates with it
through authenticated AWS API endpoints over TLS. If your pipeline is built around a
shared file system, you can keep using it for application installs and production
data—the service doesn't require one.

| Deadline 10 component                    | In Deadline Cloud                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Repository (shared file system)          | Nothing to operate. Job files move through job attachments in Amazon Simple Storage Service<br>(Amazon S3). Job bundles and queue environments replace the plugins, scripts, and<br>settings stored in the repository.                                                                                                                                                                                             |
| Database (MongoDB)                       | Nothing to operate. The service stores farm state, which you query<br>through the Deadline Cloud API.                                                                                                                                                                                                                                                                                                              |
| Remote Connection Server (RCS)           | Nothing to operate. All clients connect to the service API endpoints<br>using AWS Identity and Access Management (IAM) credentials over TLS.                                                                                                                                                                                                                                                                       |
| Pulse (house cleaning, pending job scan) | The service performs scheduling and maintenance. On a CMF, you're<br>responsible for worker host health. The [CMF<br>farm templates](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cmf_templates "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cmf_templates") sample includes a health check template. |
| Worker application and Launcher          | The Deadline Cloud worker agent. An SMF runs it for you; on a CMF you install it<br>on your own hosts.                                                                                                                                                                                                                                                                                                             |
| Monitor (desktop application)            | The [AWS Deadline Cloud monitor](../userguide/working-with-deadline-monitor.md "../userguide/working-with-deadline-monitor.md"),<br>available as a desktop application and in the browser.                                                                                                                                                                                                                         |
| `deadlinecommand` and the REST API       | The [deadline<br>CLI](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud"), the [Deadline Cloud API](../APIReference/Welcome.md "../APIReference/Welcome.md"), and the<br>AWS SDKs.                                                                                                                                                                                    |

## Map Deadline 10 concepts to Deadline Cloud

The following table maps the Deadline 10 concepts you use to organize and automate a farm
to their Deadline Cloud equivalents.

| Deadline 10                                                          | Deadline Cloud                                                                                                                                                                                            | For more information                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Pools and groups                                                     | Queue–fleet associations select which fleets serve a queue. Host<br>requirements and fleet capabilities select workers within those fleets.                                                               | [Route jobs to specific workers (pools and groups)](#migrate-from-deadline-10-routing "#migrate-from-deadline-10-routing")                                                                                                                                                                 |
| Job scheduling order (pool, priority, weighted, balanced)            | Queue scheduling configurations: priority first-in-first-out, priority<br>balanced, and weighted balanced.                                                                                                | [Scheduling configurations](build-jobs-scheduling.md#jobs-scheduling-configuration "build-jobs-scheduling.md#jobs-scheduling-configuration")                                                                                                                                               |
| Limits (license limits, resource limits, machine limits)             | Resource limits, acquired per task and associated with queues.                                                                                                                                            | [Create resource limits for jobs](build-job-limits.md "build-job-limits.md")                                                                                                                                                                                                               |
| Job dependencies and pending jobs                                    | Step dependencies within a job. There is no built-in job-to-job<br>dependency. To chain separate jobs, you build your own automation from Amazon EventBridge<br>(EventBridge) events.                     | [Step dependencies](build-jobs-scheduling.md#jobs-scheduling-dependencies "build-jobs-scheduling.md#jobs-scheduling-dependencies"), [Hooks, events, and integration points for jobs](integration-points.md "integration-points.md")                                                        |
| Frame list and ChunkSize                                             | Task parameter ranges and task chunking in the job template.                                                                                                                                              | [Task chunking for job templates](build-job-bundle-chunking.md "build-job-bundle-chunking.md")                                                                                                                                                                                             |
| Auxiliary files                                                      | Job attachments, stored in an Amazon S3 bucket in your account.                                                                                                                                           | [Use job attachments to share files](build-job-attachments.md "build-job-attachments.md")                                                                                                                                                                                                  |
| Path mapping rules                                                   | Storage profiles describe each machine's file system locations, and the<br>service derives path mapping rules from them.                                                                                  | [Storage profiles and path mapping](storage-profiles-and-path-mapping.md "storage-profiles-and-path-mapping.md")                                                                                                                                                                           |
| Application installation (on each host or on shared file<br>storage) | On an SMF, many applications are available as conda packages, and you can<br>package your own. On a CMF, you typically install applications on each host or on<br>shared file storage, as in Deadline 10. | [Deploy and configure custom software on workers](deploy-custom-software.md "deploy-custom-software.md")                                                                                                                                                                                   |
| Application plugins and job files                                    | Open Job Description (OpenJD) job templates, packaged as job bundles.<br>Application adaptors wrap interactive applications such as Maya and Nuke.                                                        | [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md "build-job-bundle.md"), [adaptor<br>runtime](https://github.com/OpenJobDescription/openjd-adaptor-runtime-for-python "https://github.com/OpenJobDescription/openjd-adaptor-runtime-for-python") on GitHub |
| Integrated submitters                                                | Deadline Cloud submitters for supported digital content creation (DCC)<br>applications.                                                                                                                   | [Supported<br>software](../userguide/supported-software.md "../userguide/supported-software.md")                                                                                                                                                                                           |
| Event plugins, and pre and post job and task scripts                 | Integration points: submitter hooks, queue environments, job and step<br>environments, dependent steps, and EventBridge events.                                                                           | [Hooks, events, and integration points for jobs](integration-points.md "integration-points.md")                                                                                                                                                                                            |
| AWS Portal                                                           | An SMF, which includes automatic scaling, usage-based licensing, and job<br>attachments for asset transfer.                                                                                               | [Configure and use Deadline Cloud service-managed fleets](smf.md "smf.md")                                                                                                                                                                                                                 |
| Spot Event Plugin                                                    | An SMF scales automatically. If you need a CMF, use Amazon Elastic Compute Cloud (Amazon EC2)<br>Auto Scaling driven by fleet size recommendation events.                                                 | [Configure and use Deadline Cloud service-managed fleets](smf.md "smf.md"), [Create fleet infrastructure with an Amazon EC2 Auto Scaling group](create-auto-scaling.md "create-auto-scaling.md")                                                                                           |
| Usage-based licensing (UBL) and the License Forwarder                | Usage-based licensing, built into an SMF and available to a CMF through<br>license endpoints.                                                                                                             | [Using software licenses with Deadline Cloud](license.md "license.md")                                                                                                                                                                                                                     |
| User management, Power User mode, and Secrets Management             | IAM policies, AWS IAM Identity Center users and groups, and per-resource access<br>levels.                                                                                                                | [Security in Deadline Cloud](security.md "security.md")                                                                                                                                                                                                                                    |
| Farm statistics and reports                                          | Amazon CloudWatch (CloudWatch) metrics and logs, and session data aggregation for<br>usage queries.                                                                                                       | [Monitoring AWS Deadline Cloud](monitoring-overview.md "monitoring-overview.md"), [Querying session statistics aggregated data using the AWS CLI](query-session-data.md "query-session-data.md")                                                                                           |
| Notifications (email, SQS)                                           | No built-in user notifications. Deadline Cloud delivers EventBridge events to your<br>account's event bus, and you build your own delivery, such as email through<br>Amazon SNS.                          | [Managing Deadline Cloud events using Amazon EventBridge](eventbridge-integration.md "eventbridge-integration.md")                                                                                                                                                                         |
| Idle workstation rendering                                           | CMF workers running on workstations alongside your existing<br>farm.                                                                                                                                      | [Extend your on-premises render farm to the cloud](hybrid-rendering.md "hybrid-rendering.md")                                                                                                                                                                                              |

## Route jobs to specific workers (pools and groups)

In Deadline 10, you assign workers to pools and groups, and each job targets a pool and a
group. Deadline Cloud splits those responsibilities between two resources:

- **Queues organize work and control access.** A queue
  holds jobs, sets their scheduling order, and defines who can submit to it and view it.
  Use queues the way you used pools: to separate shows, departments, or clients.
- **Fleets and host requirements select workers.** A
  fleet declares the capabilities that its workers guarantee: hardware minimums and
  custom attributes such as installed software or a site label. Each step in a job states
  its host requirements. The service routes the step to a compatible fleet associated
  with the queue. Use fleets and host requirements the way you used groups: to make sure
  work only runs on appropriately equipped machines.

To dedicate workers to sensitive work, such as content under a security or privacy
restriction, create a separate fleet for those workers. Associate that fleet only with the
queues that are allowed to use it. The association is the enforcement point:
AWS IAM Identity Center group memberships control who can view and manage a resource, and host
requirements route work at the submitter's request, but neither keeps jobs off a
fleet.

For more information about the scheduling mechanics and the access control distinction,
see [Determine fleet compatibility](build-jobs-scheduling.md#jobs-scheduling-compatibility "build-jobs-scheduling.md#jobs-scheduling-compatibility"). For an end-to-end restricted fleet
setup, see [Organize your
farms, queues, and fleets](../userguide/organize-farms-queues-fleets.md "../userguide/organize-farms-queues-fleets.md") in the _Deadline Cloud User Guide_.

## Features without a direct equivalent

Some Deadline 10 features don't have a named equivalent in Deadline Cloud. In most cases, you can
express the same outcome with a job bundle:

- **Draft and Quick Draft** – To encode rendered
  frames into a movie, add a dependent step that runs an encoding tool. For a worked
  example, see [Encode a movie from another Deadline Cloud job's output with FFmpeg](examples-jb-ffmpeg-from-job.md "examples-jb-ffmpeg-from-job.md").
- **Jigsaw and tile rendering** – Split a frame
  into tiles with a parameterized step and assemble the result in a dependent step. For a
  worked example, see [Tile rendering on Deadline Cloud](examples-jb-tile-rendering.md "examples-jb-tile-rendering.md").
- **Power management** – An SMF starts and stops
  workers automatically. On a CMF, you're responsible for starting and stopping worker
  hosts—by scaling your Amazon EC2 fleet in the cloud, or with your own tooling on
  premises.

## Choose a starting point

Use the following guidance to choose where to start your migration:

- To try Deadline Cloud with a small workload before committing, create a farm with an SMF
  and submit from a supported DCC application. See
  [Getting started with Deadline Cloud resources](getting-started.md "getting-started.md").
- To keep rendering on hardware you already own, connect your render nodes or
  workstations to Deadline Cloud as a CMF. See
  [Extend your on-premises render farm to the cloud](hybrid-rendering.md "hybrid-rendering.md").
- To replace AWS Portal bursting, use an SMF. Automatic scaling, usage-based
  licensing, and asset transfer are built in. See [Configure and use Deadline Cloud service-managed fleets](smf.md "smf.md").
- To port your event plugins and job scripts, start with the integration point map.
  See [Hooks, events, and integration points for jobs](integration-points.md "integration-points.md").
