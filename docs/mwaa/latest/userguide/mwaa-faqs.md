

# Amazon MWAA frequently asked questions
<a name="mwaa-faqs"></a>

This page describes common questions you can encounter when using Amazon Managed Workflows for Apache Airflow.

**Contents**
+ [Supported versions](#q-supported-versions)
  + [What does Amazon MWAA support for Apache Airflow v2?](#airflow-support)
  + [What Python version can I use?](#python-version)
+ [Use cases](#t-common-questions)
  + [Can I use Amazon MWAA with Amazon SageMaker Unified Studio?](#t-use-sagemaker-unified-studio)
  + [When can I use AWS Step Functions vs. Amazon MWAA?](#t-step-functions)
+ [Environment specifications](#q-supported-features)
  + [How much task storage is available to each environment?](#worker-storage)
  + [What is the default operating system used for Amazon MWAA environments?](#default-os)
  + [Can I use a custom image for my Amazon MWAA environment?](#custom-image)
  + [Is Amazon MWAA HIPAA compliant?](#hipaa-compliance)
  + [Does Amazon MWAA support Spot Instances?](#spot-instances)
  + [Does Amazon MWAA support a custom domain?](#custom-dns)
  + [Can I SSH into my environment?](#ssh-dag)
  + [Why is a self-referencing rule required on the VPC security group?](#sg-rule)
  + [Can I hide environments from different groups in IAM?](#hide-environments)
  + [Can I store temporary data on the Apache Airflow worker?](#store-data)
  + [Can I specify more than 25 Apache Airflow workers?](#scaling-quota)
  + [Does Amazon MWAA support shared Amazon VPCs or shared subnets?](#shared-vpc)
  + [Can I create or integrate custom Amazon SQS queues to manage task execution and workflow orchestration in Apache Airflow?](#create-sqs)
+ [Metrics](#q-metrics)
  + [What metrics are used to determine whether to scale workers?](#metrics-workers)
  + [Can I create custom metrics in CloudWatch?](#metrics-custom)
+ [DAGs, Operators, Connections, and other questions](#q-dags)
  + [Can I use the `PythonVirtualenvOperator`?](#virtual-env-dags)
  + [How long does it take Amazon MWAA to recognize a new DAG file?](#recog-dag)
  + [Why is my DAG file not picked up by Apache Airflow?](#dag-file-error)
  + [Can I remove a `plugins.zip` or `requirements.txt` from an environment?](#remove-plugins-reqs)
  + [Why don't my plugins appear in the Apache Airflow v2.0.2 Admin Plugins menu?](#view-plugins-ui)
  + [Can I use AWS Database Migration Service (DMS) Operators?](#ops-dms)
  + [When I access the Airflow REST API using the AWS credentials, can I increase the throttling limit to more than 10 transactions per second (TPS)?](#increase-throttling-limit)
  + [Where does the Airflow Task Execution API server run in Amazon MWAA?](#task-execution-server)

## Supported versions
<a name="q-supported-versions"></a>

### What does Amazon MWAA support for Apache Airflow v2?
<a name="airflow-support"></a>

To learn what Amazon MWAA supports, refer to [Apache Airflow versions on Amazon Managed Workflows for Apache Airflow](airflow-versions.md).

### What Python version can I use?
<a name="python-version"></a>

The following Apache Airflow versions are supported on Amazon Managed Workflows for Apache Airflow.

**Note**  
Effective December 30, 2025, Amazon MWAA will end support for Apache Airflow versions v2.4.3, v2.5.1, and v2.6.3. For more information, refer to [End-of-support versions](airflow-versions.md#airflow-versions-eos).
Beginning with Apache Airflow v2.2.2, Amazon MWAA supports installing Python requirements, provider packages, and custom plugins directly on the Apache Airflow webserver.
 Beginning with Apache Airflow v2.7.2, your requirements file must include a `--constraint` statement. If you don't provide a constraint, Amazon MWAA will specify one for you to ensure the packages listed in your requirements are compatible with the version of Apache Airflow you're using.   
For more information about setting up constraints in your requirements file, refer to [Installing Python dependencies](working-dags-dependencies.md#working-dags-dependencies-syntax-create).
Amazon MWAA does not currently support [multi-team mode](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#multi-team). Enabling this feature is incompatible with Amazon MWAA authentication, the `CeleryExecutor`, and environment-level secrets management.


| Apache Airflow version | Apache Airflow release date | Amazon MWAA availability date | Apache Airflow constraints | Python version | 
| --- | --- | --- | --- | --- | 
| [v3.3.1](https://airflow.apache.org/docs/apache-airflow/3.3.1) | [August 12, 2026](https://airflow.apache.org/docs/apache-airflow/3.3.1/release_notes.html#airflow-3-3-1-2026-08-12) | September 1, 2026 | [v3.3.1 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-3.3.1/constraints-3.12.txt) | [Python 3.12](https://peps.python.org/pep-0693/) | 
| [v3.2.1](https://airflow.apache.org/docs/apache-airflow/3.2.1) | [April 22, 2026](https://airflow.apache.org/docs/apache-airflow/3.2.1/release_notes.html#airflow-3-2-1-2026-04-22) | May 19, 2026 | [v3.2.1 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-3.2.1/constraints-3.12.txt) | [Python 3.12](https://peps.python.org/pep-0693/) | 
| [v2.11.2](https://airflow.apache.org/docs/apache-airflow/2.11.2) | [March 14, 2026](https://airflow.apache.org/docs/apache-airflow/2.11.2/release_notes.html#airflow-2-11-2-2026-03-14) | July 23, 2026 | [v2.11.2 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.11.2/constraints-3.12.txt) | [Python 3.12](https://peps.python.org/pep-0693/) | 
| [v2.11.0](https://airflow.apache.org/docs/apache-airflow/2.11.0) | [May 20, 2025](https://airflow.apache.org/docs/apache-airflow/2.11.0/release_notes.html#airflow-2-11-0-2022-05-20) | January 7, 2026 | [v2.11.0 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.11.0/constraints-3.12.txt) | [Python 3.12](https://peps.python.org/pep-0693/) | 
| [v3.0.6](https://airflow.apache.org/docs/apache-airflow/3.0.6) | [August 29, 2025](https://airflow.apache.org/docs/apache-airflow/3.0.6/release_notes.html#airflow-3-0-6-2025-08-29) | October 1, 2025 | [v3.0.6 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-3.0.6/constraints-3.12.txt) | [Python 3.12](https://peps.python.org/pep-0693/) | 
| [v2.10.3](https://airflow.apache.org/docs/apache-airflow/2.10.3) | [November 4, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.3/release_notes.html#airflow-2-10-3-2024-11-04) | December 18, 2024 | [v2.10.3 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.11.txt) | [Python 3.11](https://peps.python.org/pep-0664/) | 
| [v2.10.1](https://airflow.apache.org/docs/apache-airflow/2.10.1) | [September 5, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-10-1-2024-09-05) | September 26, 2024 | [v2.10.1 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.10.1/constraints-3.11.txt) | [Python 3.11](https://peps.python.org/pep-0664/) | 
| [v2.9.2](https://airflow.apache.org/docs/apache-airflow/2.9.2) | [June 10, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-9-2-2024-06-10) | July 9, 2024 | [v2.9.2 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.11.txt) | [Python 3.11](https://peps.python.org/pep-0664/) | 
| [v2.8.1](https://airflow.apache.org/docs/apache-airflow/2.8.1) | [January 19, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-8-1-2024-01-19) | February 23, 2024 | [v2.8.1 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.11.txt) | [Python 3.11](https://peps.python.org/pep-0664/) | 
| [v2.7.2](https://airflow.apache.org/docs/apache-airflow/2.7.2) | [October 12, 2023](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-7-2-2023-10-12) | November 6, 2023 | [v2.7.2 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.11.txt) | [Python 3.11](https://peps.python.org/pep-0664/) | 

For more information about migrating your self-managed Apache Airflow deployments, or migrating an existing Amazon MWAA environment, including instructions for backing up your metadata database, refer to the [Amazon MWAA Migration Guide](https://docs.aws.amazon.com/mwaa/latest/migrationguide/index.html).

## Use cases
<a name="t-common-questions"></a>

### Can I use Amazon MWAA with Amazon SageMaker Unified Studio?
<a name="t-use-sagemaker-unified-studio"></a>

Yes. With an Amazon SageMaker Unified Studio workflow, you can set up and run a series of tasks in Amazon SageMaker Unified Studio. Amazon SageMaker Unified Studio workflows use Apache Airflow to model data processing procedures and orchestrate your Amazon SageMaker Unified Studio code artifacts. For more information, refer to the [Workflows](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/workflow-orchestration.html) section. To learn more about Amazon SageMaker, refer to [What is Amazon SageMaker?](https://docs.aws.amazon.com/next-generation-sagemaker/latest/userguide/what-is-sagemaker.html)

### When can I use AWS Step Functions vs. Amazon MWAA?
<a name="t-step-functions"></a>

1. You can use Step Functions to process individual customer orders, since Step Functions can scale to meet demand for one order or one million orders.

1. If you’re running an overnight workflow that processes the previous day’s orders, you can use Step Functions or Amazon MWAA. Amazon MWAA gives you an open source option to abstract the workflow from the AWS resources you're using.

## Environment specifications
<a name="q-supported-features"></a>

### How much task storage is available to each environment?
<a name="worker-storage"></a>

The task storage is limited to 20 GB, and is specified by [Amazon ECS Fargate 1.4](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-storage.html#fargate-task-storage-linux-pv). The amount of RAM is determined by the environment class you specify. For more information about environment classes, refer to [Configuring the Amazon MWAA environment class](environment-class.md).

### What is the default operating system used for Amazon MWAA environments?
<a name="default-os"></a>

Amazon MWAA environments are created on instances running Amazon Linux 2 for versions 2.6 and older, and on instances running Amazon Linux 2023 for versions 2.7 and later.

### Can I use a custom image for my Amazon MWAA environment?
<a name="custom-image"></a>

Custom images are not supported. Amazon MWAA uses images that are built on Amazon Linux AMI. Amazon MWAA installs the additional requirements by running `pip3 -r install` for the requirements specified in the requirements.txt file you add to the Amazon S3 bucket for the environment.

### Is Amazon MWAA HIPAA compliant?
<a name="hipaa-compliance"></a>

Amazon MWAA is [Health Insurance Portability and Accountability Act (HIPAA)](https://aws.amazon.com/compliance/hipaa-compliance/) eligible. If you have a HIPAA Business Associate Addendum (BAA) in place with AWS, you can use Amazon MWAA for workflows handling Protected Health Information (PHI) on environments created on, or after, November 14th, 2022.

### Does Amazon MWAA support Spot Instances?
<a name="spot-instances"></a>

Amazon MWAA does not currently support on-demand Amazon EC2 Spot Instance types for Apache Airflow. However, an Amazon MWAA environment can trigger Spot Instances on, for example, Amazon EMR and Amazon EC2.

### Does Amazon MWAA support a custom domain?
<a name="custom-dns"></a>

To be able to use a custom domain for your Amazon MWAA hostname, do one of the following:
+ For Amazon MWAA deployments with public web server access, you can use Amazon CloudFront with Lambda@Edge to direct traffic to your environment, and map a custom domain name to CloudFront. For more information and an example of setting up a custom domain for a public environment, refer to the [Amazon MWAA custom domain for public web server](https://github.com/aws-samples/amazon-mwaa-examples/tree/main/usecases/mwaa-public-webserver-custom-domain) sample in the Amazon MWAA examples GitHub repository.
+ For Amazon MWAA deployments with private web server access, refer to [Setting up a custom domain for the Apache Airflow webserver](configuring-custom-domain.md).

### Can I SSH into my environment?
<a name="ssh-dag"></a>

While SSH is not supported on a Amazon MWAA environment, it's possible to use a DAG to run bash commands using the `BashOperator`. For example:

```
from airflow import DAG
				from airflow.operators.bash_operator import BashOperator
				from airflow.utils.dates import days_ago
				with DAG(dag_id="any_bash_command_dag", schedule_interval=None, catchup=False, start_date=days_ago(1)) as dag:
				cli_command = BashOperator(
				task_id="bash_command",
				bash_command="{{ dag_run.conf['command'] }}"
				)
```

To trigger the DAG in the Apache Airflow UI, use:

```
{ "command" : "your bash command"}
```

### Why is a self-referencing rule required on the VPC security group?
<a name="sg-rule"></a>

By creating a self-referencing rule, you're restricting the source to the same security group in the VPC, and it's not open to all networks. To learn more, refer to [Security in your VPC on Amazon MWAA](vpc-security.md).

### Can I hide environments from different groups in IAM?
<a name="hide-environments"></a>

You can limit access by specifying an environment name in AWS Identity and Access Management, however, access filtering isn't available in the AWS console—if a user can access one environment, they can access all environments.

### Can I store temporary data on the Apache Airflow worker?
<a name="store-data"></a>

Your Apache Airflow Operators can store temporary data on the workers. Apache Airflow workers can access temporary files in the `/tmp` on the Fargate containers for your environment.

**Note**  
Total task storage is limited to 20 GB, according to [Amazon ECS Fargate 1.4](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-storage.html#fargate-task-storage-linux-pv). There's no guarantee that subsequent tasks run on the same Fargate container instance, which can use a different `/tmp` folder.

### Can I specify more than 25 Apache Airflow workers?
<a name="scaling-quota"></a>

Yes. Although you can specify up to 25 Apache Airflow workers on the Amazon MWAA console, you can configure up to 50 on an environment by requesting a quota increase. For more information, refer to [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).

### Does Amazon MWAA support shared Amazon VPCs or shared subnets?
<a name="shared-vpc"></a>

Amazon MWAA does not support shared Amazon VPCs or shared subnets. The Amazon VPC you select when you create an environment must be owned by the account that is attempting to create the environment. However, you can route traffic from an Amazon VPC in the Amazon MWAA account to a shared VPC. For more information and an example of routing traffic to a shared Amazon VPC, refer to [Centralized outbound routing to the internet](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-nat-igw.html) in the *Amazon VPC Transit Gateways Guide*.

### Can I create or integrate custom Amazon SQS queues to manage task execution and workflow orchestration in Apache Airflow?
<a name="create-sqs"></a>

No, you cannot create, modify, or use custom Amazon SQS queues within Amazon MWAA. This is because Amazon MWAA automatically provisions and manages its own Amazon SQS queue for each Amazon MWAA environment.

## Metrics
<a name="q-metrics"></a>

### What metrics are used to determine whether to scale workers?
<a name="metrics-workers"></a>

Amazon MWAA monitors the **QueuedTasks** and **RunningTasks** in CloudWatch to determine whether to scale Apache Airflow workers on your environment. To learn more, refer to [Monitoring and metrics for Amazon Managed Workflows for Apache Airflow](cw-metrics.md).

### Can I create custom metrics in CloudWatch?
<a name="metrics-custom"></a>

Not on the CloudWatch console. However, you can create a DAG that writes custom metrics in CloudWatch. For more information, refer to [Using a DAG to write custom metrics in CloudWatch](samples-custom-metrics.md).

## DAGs, Operators, Connections, and other questions
<a name="q-dags"></a>

### Can I use the `PythonVirtualenvOperator`?
<a name="virtual-env-dags"></a>

With Amazon MWAA, you can use the `PythonVirtualenvOperator`, which comes preinstalled on every environment. Use it to run Python callables in a virtual environment with isolated dependencies. For more information about preinstalled packages, see [Apache Airflow provider packages installed on Amazon MWAA environments](connections-packages.md).

### How long does it take Amazon MWAA to recognize a new DAG file?
<a name="recog-dag"></a>

DAGs are periodically synchronized from the Amazon S3 bucket to your environment. If you add a new DAG file, it takes about 300 seconds for Amazon MWAA to start *using* the new file. If you update an existing DAG, it takes Amazon MWAA about 30 seconds to recognize your updates.

These values, 300 seconds for new DAGs, and 30 seconds for updates to existing DAGs, correspond to Apache Airflow configuration options [`dag_dir_list_interval`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#dag-dir-list-interval), and [`min_file_process_interval`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#min-file-process-interval) respectively.

### Why is my DAG file not picked up by Apache Airflow?
<a name="dag-file-error"></a>

The following are possible solutions for this issue:

1. Check that your execution role has sufficient permissions to your Amazon S3 bucket. To learn more, refer to [Amazon MWAA execution role](mwaa-create-role.md).

1. Check that the Amazon S3 bucket has *Block Public Access* configured, and *Versioning* enabled. To learn more, refer to [Create an Amazon S3 bucket for Amazon MWAA](mwaa-s3-bucket.md).

1. Verify the DAG file itself. For example, be sure that each DAG has a unique DAG ID.

### Can I remove a `plugins.zip` or `requirements.txt` from an environment?
<a name="remove-plugins-reqs"></a>

Currently, there is no way to remove a plugins.zip or requirements.txt from an environment once they’ve been added, but we're working on the issue. In the interim, a workaround is to point to an empty text or zip file, respectively. To learn more, refer to [Deleting files on Amazon S3](working-dags-delete.md).

### Why don't my plugins appear in the Apache Airflow v2.0.2 Admin Plugins menu?
<a name="view-plugins-ui"></a>

For security reasons, the Apache Airflow webserver on Amazon MWAA has limited network egress, and does not install plugins nor Python dependencies directly on the Apache Airflow webserver for version 2.0.2 environments. The plugin that's listed allows Amazon MWAA to authenticate your Apache Airflow users in AWS Identity and Access Management (IAM).

To be able to install plugins and Python dependencies directly on the webserver, we recommend creating a new environemnt with Apache Airflow v2.2 and later. Amazon MWAA installs Python dependencies and and custom plugins directly on the webserver for Apache Airflow v2.2 and later.

### Can I use AWS Database Migration Service (DMS) Operators?
<a name="ops-dms"></a>

Amazon MWAA supports [DMS Operators](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/dms.html). However, this operator cannot be used to perform actions on the Amazon Aurora PostgreSQL metadata database associated with an Amazon MWAA environment.

### When I access the Airflow REST API using the AWS credentials, can I increase the throttling limit to more than 10 transactions per second (TPS)?
<a name="increase-throttling-limit"></a>

Yes, you can. To increase the throttling limit, please contact [AWS Customer Support](https://aws.amazon.com/contact-us/).

### Where does the Airflow Task Execution API server run in Amazon MWAA?
<a name="task-execution-server"></a>

Amazon MWAA runs the Airflow Task Execution API Server in the Webserver component. Task Execution APIs are available only in Apache Airflow v3 and later. For more information about Amazon MWAA architecture, refer to [Architecture](what-is-mwaa.md#architecture-mwaa).