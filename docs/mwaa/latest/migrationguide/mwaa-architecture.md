

# Explore Amazon MWAA network architecture
<a name="mwaa-architecture"></a>

The following section describes the main components that make up an Amazon MWAA environment, and the set of AWS services that each environment integrates with to manage its resources, keep your data secure, and provide monitoring and visibility for your workflows.

**Topics**
+ [Amazon MWAA components](#architecture-components)
+ [Connectivity](#networking-requirements)

## Amazon MWAA components
<a name="architecture-components"></a>

 Amazon MWAA environments consist of the following four main components: 

1.  **Scheduler** — Parses and monitors all of your DAGs, and queues tasks for execution when a DAG's dependencies are met. Amazon MWAA deploys the scheduler as a AWS Fargate cluster with a minimum of 2 schedulers. You can increase the scheduler count up to five, depending on your workload. For more information about Amazon MWAA environment classes, refer to [Amazon MWAA environment class](https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html). 

1.  **Workers** — One or more Fargate tasks that runs your scheduled tasks. The number of workers for your environment is determined by a range between a *minimum* and *maximum* number that you specify. Amazon MWAA starts auto-scaling workers when the number of queued and running tasks is more than your existing workers can handle. When running and queued tasks sum to zero for more than two minutes, Amazon MWAA scales back the number of workers to its minimum. For more information about how Amazon MWAA handles auto-scaling workers, refer to [Amazon MWAA automatic scaling](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-autoscaling.html). 

1.  **Web server** — Runs the Apache Airflow web UI. You can configure the web server with [private or public](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-vpe-access.html#vpc-vpe-about) network access. In both cases, access to your Apache Airflow users is controlled by the access control policy you define in AWS Identity and Access Management (IAM). For more information about configuring IAM access policies for your environment, refer to [Accessing an Amazon MWAA environment](https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html). 

1.  **Database** — Stores metadata about the Apache Airflow environment and your workflows, including DAG run history. The database is a single-tenant Aurora PostgreSQL database managed by AWS, and accessible to the scheduler and worker Fargate containers through a privately-secured Amazon VPC endpoint. 

 Every Amazon MWAA environment also interacts with a set of AWS services to handle a variety of tasks, including storing and accessing DAGs and task dependencies, securing your data at rest, and logging and monitoring you environment. The following diagram demonstrates the different components of an Amazon MWAA environment. 

![This image shows the architecture of an Amazon MWAA environment.](http://docs.aws.amazon.com/mwaa/latest/migrationguide/images/mwaa-architecture.png)


**Note**  
 The service Amazon VPC is not a shared VPC. Amazon MWAA creates an AWS owned VPC for every environment you create. 
+  **Amazon S3** — Amazon MWAA stores all of your workflow resources, such as DAGs, requirements, and plugin files in an Amazon S3 bucket. For more information about creating the bucket as part of environment creation, and uploading your Amazon MWAA resources, refer to [Create an Amazon S3 bucket for Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html) in the *Amazon MWAA User Guide*. 
+  **Amazon SQS** — Amazon MWAA uses Amazon SQS for queueing your workflow tasks with a [Celery executor](https://airflow.apache.org/docs/apache-airflow-providers-celery/stable/celery_executor.html). 
+  **Amazon ECR** — Amazon ECR hosts all Apache Airflow images. Amazon MWAA only supports AWS-managed Apache Airflow images. 
+  **AWS KMS** — Amazon MWAA uses AWS KMS to ensure your data is secure at rest. By default, Amazon MWAA uses [AWS-managed AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk), but you can configure your environment to use your own [customer-managed](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) AWS KMS key. For more information about using your own customer-managed AWS KMS key, refer to [Customer-managed keys for Data Encryption](https://docs.aws.amazon.com/mwaa/latest/userguide/custom-keys-certs.html) in the *Amazon MWAA User Guide*. 
+  **CloudWatch** — Amazon MWAA integrates with CloudWatch and delivers Apache Airflow logs and environment metrics to CloudWatch, allowing you to monitor your Amazon MWAA resources and troubleshoot issues. 

## Connectivity
<a name="networking-requirements"></a>

 Your Amazon MWAA environment needs access to all AWS services it integrates with. The Amazon MWAA [execution role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html) controls how access is granted to Amazon MWAA to connect to other AWS services on your behalf. For network connectivity, you can either provide public internet access to your Amazon VPC or create Amazon VPC endpoints. For more information on configuring Amazon VPC endpoints (AWS PrivateLink) for your environment, refer to [Managing access to VPC endpoints on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-vpe-access.html) in the *Amazon MWAA User Guide*. 

 Amazon MWAA installs requirements on the scheduler and worker. If your requirements are sourced from a public [PyPi](https://pypi.org/) repository, your environment needs connectivity to the internet to download the required libraries. For private environments, you can either use a private PyPi repository, or bundle the libraries in [`.whl` files](https://docs.aws.amazon.com/mwaa/latest/userguide/best-practices-dependencies.html) as custom plugins for your environment. 

 When you configure the Apache Airflow in [private mode](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-vpe-access.html#vpc-vpe-about-private), the Apache Airflow UI can only be accessible to your Amazon VPC though Amazon VPC endpoints. 

 For more information about networking, refer to [Networking](https://docs.aws.amazon.com/mwaa/latest/userguide/networking.html) in the *Amazon MWAA User Guide*. 