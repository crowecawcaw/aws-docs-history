# Explore Amazon MWAA network architecture

The following section describes the main components that make up an Amazon MWAA environment, and the set of AWS services that each environment integrates with
to manage its resources, keep your data secure, and provide monitoring and visibility for your workflows.

###### Topics

- [Amazon MWAA components](#architecture-components "#architecture-components")
- [Connectivity](#networking-requirements "#networking-requirements")

## Amazon MWAA components

Amazon MWAA environments consist of the following four main components:

1. **Scheduler** — Parses and monitors all of your DAGs, and queues tasks for execution when a DAG's dependencies are met. Amazon MWAA deploys the scheduler
   as a AWS Fargate cluster with a minimum of 2 schedulers. You can increase the scheduler count up to five, depending on your workload. For more information about Amazon MWAA environment classes,
   refer to [Amazon MWAA environment class](../userguide/environment-class.md "../userguide/environment-class.md").
2. **Workers** — One or more Fargate tasks that runs your scheduled tasks. The number of workers for your environment is determined by a range between a _minimum_ and _maximum_ number that you specify.
   Amazon MWAA starts auto-scaling workers when the number of queued and running tasks is more than your existing workers can handle. When running and queued tasks sum to zero for more than two minutes, Amazon MWAA scales back the number
   of workers to its minimum. For more information about how Amazon MWAA handles auto-scaling workers, refer to [Amazon MWAA automatic scaling](../userguide/mwaa-autoscaling.md "../userguide/mwaa-autoscaling.md").
3. **Web server** — Runs the Apache Airflow web UI. You can configure the web server with [private or public](../userguide/vpc-vpe-access.md#vpc-vpe-about "../userguide/vpc-vpe-access.md#vpc-vpe-about")
   network access. In both cases, access to your Apache Airflow users is controlled by the access control policy you define in AWS Identity and Access Management (IAM). For more information about configuring IAM access policies for your environment, refer to
   [Accessing an Amazon MWAA environment](../userguide/access-policies.md "../userguide/access-policies.md").
4. **Database** — Stores metadata about the Apache Airflow environment and your workflows, including DAG run history. The database is a single-tenant Aurora PostgreSQL database managed by AWS, and accessible to the scheduler and worker
   Fargate containers through a privately-secured Amazon VPC endpoint.

Every Amazon MWAA environment also interacts with a set of AWS services to handle a variety of tasks, including storing and accessing DAGs and task dependencies, securing your data at rest, and logging and monitoring you environment.
The following diagram demonstrates the different components of an Amazon MWAA environment.

![This image shows the architecture of an Amazon MWAA environment.](images/mwaa-architecture.png)

###### Note

The service Amazon VPC is not a shared VPC. Amazon MWAA creates an AWS owned VPC for every environment you create.

- **Amazon S3** — Amazon MWAA stores all of your workflow resources, such as DAGs, requirements, and plugin files in an Amazon S3 bucket. For more
  information about creating the bucket as part of environment creation, and uploading your Amazon MWAA resources, refer to
  [Create an Amazon S3 bucket for Amazon MWAA](../userguide/mwaa-s3-bucket.md "../userguide/mwaa-s3-bucket.md") in the _Amazon MWAA User Guide_.
- **Amazon SQS** — Amazon MWAA uses Amazon SQS for queueing your workflow tasks with a
  [Celery executor](https://airflow.apache.org/docs/apache-airflow/stable/executor/celery.html "https://airflow.apache.org/docs/apache-airflow/stable/executor/celery.html").
- **Amazon ECR** — Amazon ECR hosts all Apache Airflow images. Amazon MWAA only supports AWS-managed Apache Airflow images.
- **AWS KMS** — Amazon MWAA uses AWS KMS to ensure your data is secure at rest. By default, Amazon MWAA uses
  [AWS-managed AWS KMS keys](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk"),
  but you can configure your environment to use your own [customer-managed](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") AWS KMS key.
  For more information about using your own customer-managed AWS KMS key, refer to
  [Customer-managed keys for Data Encryption](../userguide/custom-keys-certs.md "../userguide/custom-keys-certs.md") in the _Amazon MWAA User Guide_.
- **CloudWatch** — Amazon MWAA integrates with CloudWatch and delivers Apache Airflow logs and environment metrics to CloudWatch, allowing you to monitor your Amazon MWAA
  resources and troubleshoot issues.

## Connectivity

Your Amazon MWAA environment needs access to all AWS services it integrates with. The Amazon MWAA [execution role](../userguide/mwaa-create-role.md "../userguide/mwaa-create-role.md")
controls how access is granted to Amazon MWAA to connect to other AWS services on your behalf. For network connectivity, you can either provide public internet access to your Amazon VPC or create Amazon VPC endpoints.
For more information on configuring Amazon VPC endpoints (AWS PrivateLink) for your environment, refer to
[Managing access to VPC endpoints on Amazon MWAA](../userguide/vpc-vpe-access.md "../userguide/vpc-vpe-access.md") in the _Amazon MWAA User Guide_.

Amazon MWAA installs requirements on the scheduler and worker. If your requirements are sourced from a public [PyPi](https://pypi.org/ "https://pypi.org/") repository,
your environment needs connectivity to the internet to download the required libraries. For private environments, you can either use a private PyPi repository,
or bundle the libraries in [`.whl` files](../userguide/best-practices-dependencies.md "../userguide/best-practices-dependencies.md")
as custom plugins for your environment.

When you configure the Apache Airflow in [private mode](../userguide/vpc-vpe-access.md#vpc-vpe-about-private "../userguide/vpc-vpe-access.md#vpc-vpe-about-private"),
the Apache Airflow UI can only be accessible to your Amazon VPC though Amazon VPC endpoints.

For more information about networking, refer to [Networking](../userguide/networking.md "../userguide/networking.md") in the
_Amazon MWAA User Guide_.
