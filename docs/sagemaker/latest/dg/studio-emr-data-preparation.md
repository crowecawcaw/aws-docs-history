# Data preparation at scale using Amazon EMR Serverless

applications or Amazon EMR clusters in Studio

Amazon SageMaker Studio and its legacy version, Studio Classic, provide data scientists, and machine
learning (ML) engineers with tools to perform data analytics and data preparation at scale.
Analyzing, transforming, and preparing large amounts of data is a foundational step of any
data science and ML workflow. Both Studio and Studio Classic come with built-in integration
with Amazon EMR, allowing users to manage large-scale, interactive data preparation and machine
learning workflows within their JupyterLab notebooks.

[Amazon EMR](../../../emr/latest/ManagementGuide/emr-what-is-emr.md "../../../emr/latest/ManagementGuide/emr-what-is-emr.md") is a managed big data platform with resources to help you run
petabyte-scale distributed data processing jobs using open-source analytics frameworks on
AWS such as [Apache Spark](https://aws.amazon.com/emr/features/spark "https://aws.amazon.com/emr/features/spark"), [Apache Hive](https://aws.amazon.com/emr/features/hive "https://aws.amazon.com/emr/features/hive"), [Presto](https://aws.amazon.com/emr/features/presto "https://aws.amazon.com/emr/features/presto"), HBase, and Flink among others. With
Studio and Studio Classic integration with Amazon EMR, you can create, browse, discover, and
connect to Amazon EMR clusters without leaving your JupyterLab or Studio Classic notebooks. You can
additionally monitor and debug your Spark workloads by accessing the Spark UI directly from
your notebook with one-click.

You should consider Amazon EMR clusters for your data preparation workloads if you have
large-scale, long-running, or complex data processing requirements that involve massive
amounts of data, require extensive customization and integration with other services, need
to run custom applications, or plan to run a diverse range of distributed data processing
frameworks beyond just Apache Spark.

Using [SageMaker distribution image](sagemaker-distribution.md "sagemaker-distribution.md")
`1.10` or higher, you can alternatively connect to interactive [EMR Serverless](../../../emr/latest/EMR-Serverless-UserGuide/emr-serverless.md "../../../emr/latest/EMR-Serverless-UserGuide/emr-serverless.md") applications directly from your JupyterLab notebooks in SageMaker AI
Studio. The integration of Studio with EMR Serverless allows you to run
open-source big data analytics frameworks such as [Apache Spark](https://aws.amazon.com/emr/features/spark "https://aws.amazon.com/emr/features/spark") and [Apache Hive](https://aws.amazon.com/emr/features/hive "https://aws.amazon.com/emr/features/hive") without configuring, managing, or scaling
Amazon EMR clusters. EMR Serverless automatically provisions and manages the underlying compute
and memory resources based on your EMR Serverless application's needs. It scales resources
up and down dynamically, charging you or the amount of vCPU, memory, and storage resources
consumed by your applications. This serverless approach allows you to [run interactive
data preparation workloads](../../../emr/latest/EMR-Serverless-UserGuide/interactive-workloads.md "../../../emr/latest/EMR-Serverless-UserGuide/interactive-workloads.md") from your JupyterLab notebooks without worrying
about cluster management, while achieving high instance utilization and cost
efficiency.

You should consider EMR Serverless for your interactive data preparation workloads if
your workloads are short-lived or intermittent and don't require a persistent cluster; you
prefer a serverless experience with automatic resource provisioning and termination,
avoiding the overhead of managing infrastructure; or your interactive data preparation tasks
primarily revolve around Apache Spark.

###### Content

- [Configure network access for your Amazon EMR cluster](studio-notebooks-emr-networking.md "studio-notebooks-emr-networking.md")
- [Prepare data using EMR Serverless](studio-notebooks-emr-serverless.md "studio-notebooks-emr-serverless.md")
- [Data preparation using Amazon EMR](studio-notebooks-emr-cluster.md "studio-notebooks-emr-cluster.md")
