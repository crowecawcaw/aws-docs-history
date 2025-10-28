# Understanding Amazon EMR on EKS concepts and terminology

Amazon EMR on EKS provides a deployment option for Amazon EMR that allows you to run open-source big data
frameworks on Amazon Elastic Kubernetes Service (Amazon EKS). This topic gives you context on some of the common terminology for it, including namespaces, virtual clusters, and job runs, which are units of
work that you submit for processing.

## Kubernetes namespace

Amazon EKS uses Kubernetes namespaces to divide cluster resources between multiple users
and applications. These namespaces are the foundation for multi-tenant environments. A
Kubernetes namespace can have either Amazon EC2 or AWS Fargate as the compute provider. This
flexibility provides you with different performance and cost options for your jobs to run on.

## Virtual cluster

A virtual cluster is a Kubernetes namespace that Amazon EMR is registered with. Amazon EMR uses
virtual clusters to run jobs and host endpoints. Multiple virtual clusters can be backed by the
same physical cluster. However, each virtual cluster maps to one namespace on an EKS cluster.
Virtual clusters do not create any active resources that contribute to your bill or that require
lifecycle management outside the service.

## Job run

A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that
you submit to Amazon EMR on EKS. One job can have multiple job runs. When you submit a job run, you
include the following information:

- A virtual cluster where the job should run.
- A job name to identify the job.
- The execution role — a scoped IAM role that runs the job and allows you to specify which
  resources can be accessed by the job.
- The Amazon EMR release label that specifies the version of open-source applications to
  use.
- The artifacts to use when submitting your job, such as spark-submit parameters.

By default, logs are uploaded to the Spark History server and are accessible from the
AWS Management Console. You can also push event logs, execution logs, and metrics to Amazon S3 and Amazon
CloudWatch.

## Amazon EMR containers

Amazon EMR containers is the [API name for Amazon EMR on EKS](../../../emr-on-eks/latest/APIReference/Welcome.md "../../../emr-on-eks/latest/APIReference/Welcome.md"). The
`emr-containers` prefix is used in the following scenarios:

- It is the prefix in the CLI commands for Amazon EMR on EKS. For example, `aws
emr-containers start-job-run`.
- It is the prefix before IAM policy actions for Amazon EMR on EKS. For example,
  `"Action": [ "emr-containers:StartJobRun"]`. For more information, see [Policy actions for Amazon EMR on EKS](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions").
- It is the prefix used in Amazon EMR on EKS service endpoints. For example,
  `emr-containers.us-east-1.amazonaws.com`. For more information, see [Amazon EMR
  on EKS Service Endpoints](service-quotas.md#service-endpoints "service-quotas.md#service-endpoints").
