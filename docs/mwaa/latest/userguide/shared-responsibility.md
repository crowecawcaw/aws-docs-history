# AWS shared responsibility model for Amazon MWAA

This guidance applies to Amazon MWAA Provisioned environments. In a Provisioned environment,
you select the environment class and configure the worker and web server scaling
limits.

Security and compliance is a shared responsibility between AWS and you. The [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
describes this as security _of_ the cloud and security
_in_ the cloud. For Amazon MWAA, this model extends beyond security into
operational responsibility. We operate, manage, and control the underlying components.
These range from the host operating system and virtualization layer down to the physical
security of the facilities in which the service operates.

You are responsible for managing the content that you deploy to your environment. On Amazon MWAA,
that content includes your DAG code and the Python dependencies that you declare
in `requirements.txt`. It also includes your custom plugins and any startup script
that you supply. Your responsibility covers the configuration, network, and permissions that
you choose. You are also responsible for the day-to-day operation of the workflows that run on
the environment. Amazon MWAA runs the content that you supply as you supply it. Amazon MWAA does not
inspect, validate, or modify it.

###### Note

Although AWS operates the infrastructure for your environment, the data that your
workflows write to the metadata database directly affects how the service performs.
Unbounded metadata growth can degrade scheduler and webserver response times. You are
responsible for managing the volume of data in your environment.

## Infrastructure that AWS manages

We are responsible for protecting the infrastructure that runs AWS services in the
AWS Cloud. For Amazon MWAA, this includes the following:

- **Apache Airflow setup** – Amazon MWAA sets up Apache Airflow for you. It
  uses the same Apache Airflow user interface and open-source code available on the internet. For
  more information, see [What Is Amazon Managed Workflows for Apache Airflow?](what-is-mwaa.md "what-is-mwaa.md").
- **Compute for the managed components** – Amazon MWAA
  provisions and operates the AWS Fargate compute for your environment. This compute
  runs the Apache Airflow scheduler, workers, and webserver. Amazon MWAA also provisions and operates the
  Apache Airflow metadata database. For each environment, Amazon MWAA creates an AWS owned Amazon VPC
  that hosts the webserver and the metadata database. The scheduler and workers connect to
  the
  private subnets in the Amazon VPC for your environment, which you own and configure. For more
  information, see [Explore Amazon MWAA network
  architecture](../migrationguide/mwaa-architecture.md "../migrationguide/mwaa-architecture.md") in the _Amazon MWAA Migration Guide_.
- **The Apache Airflow metadata database** – Amazon MWAA provisions
  and operates the Apache Airflow metadata database for each environment. You remain responsible for
  the
  volume of data that your workflows write to it. For more information, see [Operational excellence that you manage](#shared-responsibility-operations "#shared-responsibility-operations").
- **Version images and patching** – Amazon MWAA builds
  container images that bundle Apache Airflow releases with other common binaries and
  Python libraries. Amazon MWAA patches those images. An environment keeps
  using its specified image version until you issue an update environment action to move it
  to a later version. For more information, see [About Amazon MWAA versions](airflow-versions.md#airflow-versions-image "airflow-versions.md#airflow-versions-image"). The image definitions are available in the
  [amazon-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") repository on the GitHub
  website.
- **Version support lifecycle** – Amazon MWAA publishes
  the availability and end of support dates for each Apache Airflow version. Amazon MWAA notifies you
  through the Health Dashboard when an environment in your account runs a version that is nearing the
  end of support. For the current support commitment and dates, see [End-of-support versions](airflow-versions.md#airflow-versions-eos "airflow-versions.md#airflow-versions-eos").
- **Automatic scaling of the managed components** –
  Amazon MWAA scales workers and the webserver in response to demand. Scaling stays within
  the limits that you configure. You choose the environment class, the worker and webserver
  scaling settings, and the scheduler count. For more information, see [Configuring Amazon MWAA worker automatic scaling](mwaa-autoscaling.md "mwaa-autoscaling.md"), [Configuring Amazon MWAA webserver automatic scaling](mwaa-web-server-autoscaling.md "mwaa-web-server-autoscaling.md"),
  and [Configuring the Amazon MWAA environment class](environment-class.md "environment-class.md").
- **Data encryption** – Amazon MWAA encrypts your data at
  rest and in transit. Amazon MWAA also attaches the required grants to a customer-managed
  KMS key on your behalf. For more information, see [Data Protection in Amazon Managed Workflows for Apache Airflow](data-protection.md "data-protection.md").
- **Metrics and logs** – Amazon MWAA publishes
  environment metrics to Amazon CloudWatch. Amazon MWAA delivers Apache Airflow logs to CloudWatch Logs for the log types
  that you enable. For more information, see [Monitoring overview on Amazon MWAA](monitoring-overview.md "monitoring-overview.md").
- **Compliance programs** – Third-party auditors
  regularly test and verify the effectiveness of AWS security. For more information, see
  [Compliance Validation for Amazon Managed Workflows for Apache Airflow](compliance-validation.md "compliance-validation.md").

## Workflow code and content that you manage

You are responsible for maintaining control over the content that you host on this
infrastructure. This content includes the following:

- **DAG code** – The DAG definitions that you copy
  to the `dags` folder in your Amazon S3 bucket. You are responsible for what those
  DAGs access and the operations that they perform. For more information, see [Adding or updating DAGs](configuring-dag-folder.md "configuring-dag-folder.md").
- **Python dependencies** – The
  libraries that you install by uploading a `requirements.txt` file to your
  Amazon S3 bucket. This includes the security and compatibility of every package that your
  workflows require. Incompatible or resource-intensive packages can degrade scheduler and
  worker performance or prevent containers from starting. For more information, see [Installing Python dependencies](working-dags-dependencies.md "working-dags-dependencies.md") and
  [Managing Python dependencies in requirements.txt](best-practices-dependencies.md "best-practices-dependencies.md").
- **Custom plugins** – The contents of the
  `plugins.zip` file that you upload to your Amazon S3 bucket. We recommend
  verifying the contents of the file before you upload it. For more information, see [Installing custom plugins](configuring-dag-import-plugins.md "configuring-dag-import-plugins.md").
- **Startup scripts** – The shell script that
  Amazon MWAA runs on each component at startup. You also specify the Amazon S3 version ID for
  the script. For more information, see [Using a startup script with Amazon MWAA](using-startup-script.md "using-startup-script.md").
- **Testing** – Validating your DAGs, custom
  plugins, and Python dependencies before you deploy them to an
  environment. We recommend testing Apache Airflow version upgrades in a development environment
  before you apply them to production. You can use the [amazon-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") container image on the GitHub
  website to develop and test locally.
- **Your Amazon S3 bucket and its contents** – The bucket
  policy and object ACLs for the bucket associated with your environment. Amazon MWAA does not
  back up the bucket contents on your behalf. We recommend enabling versioning and
  configuring cross-region replication if your DAGs, plugins, and requirements files
  require a disaster recovery posture. We also recommend that you don't store other objects
  in the bucket or use the bucket with another service.
- **Data that you enter** – We strongly recommend
  that you never put confidential or sensitive information into tags or free-form fields
  such as a **Name** field.

## Operational excellence that you manage

Amazon MWAA operates the managed infrastructure. You retain responsibility for the workflows
that run on that infrastructure. The code, dependencies, and configuration that you deploy
determine how your environment performs. Amazon MWAA publishes the metrics and logs that describe
environment health. Interpreting that data, setting alarms on it, and acting on what it
reports **are your responsibility**.

- **Monitoring environment health** – Reviewing the
  CloudWatch metrics that Amazon MWAA publishes for your environment. These include container,
  queue, and database metrics that help you detect saturation and degradation. For more
  information, see [Monitoring and metrics for Amazon Managed Workflows for Apache Airflow](cw-metrics.md "cw-metrics.md") and [Container, queue, and database metrics for Amazon MWAA](accessing-metrics-cw-container-queue-db.md "accessing-metrics-cw-container-queue-db.md").
- **Dashboards and alarms** – Creating the CloudWatch
  dashboards and alarms that notify you when your environment approaches its limits. For
  more information, see [Monitoring dashboards and alarms on Amazon MWAA](monitoring-dashboard.md "monitoring-dashboard.md").
- **Log analysis** – Enabling the Apache Airflow log types
  that you need. You then analyze scheduler, worker, webserver, and task logs to diagnose
  workflow failures. For more information, see [Accessing Airflow logs in Amazon CloudWatch](monitoring-airflow.md "monitoring-airflow.md") and [Troubleshooting: CloudWatch Logs and CloudTrail errors](t-cloudwatch-cloudtrail-logs.md "t-cloudwatch-cloudtrail-logs.md").
- **CloudWatch service quotas** – Ensuring that the CloudWatch
  quotas in your account can handle the log volume that your environment produces.
  Exceeding CloudWatch Logs quotas such as `CreateLogStream` can cause worker
  degradation. For more information, see [CloudWatch Logs
  quotas](../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md "../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md").
- **Metadata database maintenance** – Keeping the Apache Airflow
  metadata database light. Regularly remove metadata that your workflows no longer
  need. An unbounded metadata database can degrade scheduler and webserver performance.
  For more
  information, see [Aurora PostgreSQL database cleanup on an Amazon MWAA environment](samples-database-cleanup.md "samples-database-cleanup.md").
- **DAG design and scheduling frequency** – Your
  DAG count, tasks per DAG, and schedule intervals directly determine load on the managed
  scheduler. Amazon MWAA does not throttle or reject workloads that exceed the environment's
  capacity. You must design your DAGs to fit within the resources that you
  configure.
- **Task resource governance** – Setting task-level
  timeouts, Apache Airflow pool sizes, and per-DAG concurrency limits. Amazon MWAA does not enforce
  per-task guardrails on your behalf. Without these settings, a single long-running or
  high-concurrency DAG can consume all available workers.
- **Capacity and performance tuning** – Choosing the
  environment class, the worker and webserver scaling limits, and the Apache Airflow configuration
  options that suit your workload. Automatic scaling operates within the bounds that you
  configure and does not compensate for workloads that exceed the environment's design
  capacity. You must right-size the environment class for your workload profile. For more
  information, see [Performance tuning for Apache Airflow on Amazon MWAA](best-practices-tuning.md "best-practices-tuning.md") and [Configuring the Amazon MWAA environment class](environment-class.md "environment-class.md").
- **Changes that you make through a startup script**
  – A startup script runs on every component in your environment. It can change the
  configuration of those components. You are responsible for the changes that you make this
  way, including any effect they have on environment stability. We recommend testing a
  startup script before you apply it to a production environment. For more information, see
  [Using a startup script with Amazon MWAA](using-startup-script.md "using-startup-script.md").
- **Environment updates** – Initiating an
  environment update is your action. Updates trigger container restarts and can affect
  running workflows. You are responsible for choosing when to update and for assessing the
  effect on in-progress tasks. We recommend updating during a time window that you choose,
  when no critical DAGs are running. To update without pausing and unpausing your DAGs,
  consider graceful updates, which let workers finish in-progress tasks before they shut
  down. Conditions and limits apply; for more information, see [Update an Amazon MWAA environment](update-environment.md "update-environment.md").
- **First-level triage** – Using available metrics
  and logs to diagnose issues before you engage AWS Support. The level of detail that
  AWS Support can use to help you depends on the logging level that you enabled for your
  environment.
- **Cross-environment orchestration** – Coordinating
  workflows across multiple Amazon MWAA environments. If you use mechanisms such as the Apache Airflow
  REST API or external sensors to link environments, you are responsible for that
  coordination logic.
- **Following the Amazon MWAA best practices** – Applying
  the documented guidance for performance, dependency management, and environment
  configuration. For more information, see [Best practices for Amazon Managed Workflows for Apache Airflow](best-practices.md "best-practices.md").

## Configuration and access that you manage

You choose how your environment is configured and who can reach it. You are responsible
for the following:

- **Keeping your version current** – You are
  responsible for keeping your Amazon MWAA versions current. Upgrading an environment to a newer
  Apache Airflow version is an action that you initiate. For more information, see [Changing the Apache Airflow version](upgrading-environment.md "upgrading-environment.md") and [End-of-support versions](airflow-versions.md#airflow-versions-eos "airflow-versions.md#airflow-versions-eos").
- **The execution role** – Amazon MWAA can't add or edit
  permission policies on an existing execution role after an environment is created. You
  must update the execution role with the additional permissions that your environment
  needs. For more information, see [Amazon MWAA execution role](mwaa-create-role.md "mwaa-create-role.md").
- **IAM access control** – The policies that
  determine who can access your environment and the Apache Airflow UI. Grant permissions to only the
  resources and actions that users need. For more information, see [AWS Identity and Access Management](security-iam.md "security-iam.md") and [Accessing an Amazon MWAA environment](access-policies.md "access-policies.md").
- **Apache Airflow user privileges** – Apache Airflow is not
  multi-tenant. DAG authors can write DAGs that change Apache Airflow user privileges and interact
  with the underlying metadata database. We recommend using separate environments for
  separate
  teams that have DAG writing access. For more information, see [Security best practices in Apache Airflow](security-best-practices.md#security-best-practices-for-airflow "security-best-practices.md#security-best-practices-for-airflow").
- **Webserver access mode** – Choosing
  `PUBLIC_ONLY` or `PRIVATE_ONLY` for access to the Apache Airflow UI.
  This is a security decision that determines whether the webserver endpoint is reachable
  from the internet. For more information, see [Security in your VPC on Amazon MWAA](vpc-security.md "vpc-security.md").
- **Network configuration** – Your Amazon VPC, subnets,
  security groups, and network ACLs. This includes the inbound and outbound rules that
  direct traffic on your NAT gateways. If you choose to manage your own Amazon VPC endpoints,
  you're responsible for creating those endpoints. For more information, see [Security in your VPC on Amazon MWAA](vpc-security.md "vpc-security.md") and [Managing your own Amazon VPC endpoints on Amazon MWAA](vpc-endpoint-management.md "vpc-endpoint-management.md").
- **Encryption key choice** – Whether to use an
  AWS owned KMS key or a customer-managed KMS key. If you use a customer-managed
  KMS key, you must attach the required policy statements to the key. For more
  information, see [Data Protection in Amazon Managed Workflows for Apache Airflow](data-protection.md "data-protection.md").
- **Secrets and connections** – The credentials that
  your workflows use. We recommend storing secrets in Secrets Manager. For more information, see
  [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").
- **Apache Airflow configuration options** – The configuration
  options that you override on your environment. For more information, see [Using Apache Airflow configuration options on Amazon MWAA](configuring-env-variables.md "configuring-env-variables.md").

## Related resources

- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
- [Shared
  responsibility](../../../wellarchitected/latest/security-pillar/shared-responsibility.md "../../../wellarchitected/latest/security-pillar/shared-responsibility.md") in the _AWS Well-Architected Framework_
- [Best practices for Amazon Managed Workflows for Apache Airflow](best-practices.md "best-practices.md")
- [Performance tuning for Apache Airflow on Amazon MWAA](best-practices-tuning.md "best-practices-tuning.md")
- [Monitoring dashboards and alarms on Amazon MWAA](monitoring-dashboard.md "monitoring-dashboard.md")
- [Container, queue, and database metrics for Amazon MWAA](accessing-metrics-cw-container-queue-db.md "accessing-metrics-cw-container-queue-db.md")
- [Security best practices on Amazon MWAA](security-best-practices.md "security-best-practices.md")
