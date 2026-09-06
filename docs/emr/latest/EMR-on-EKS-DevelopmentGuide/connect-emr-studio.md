

# Running interactive workloads on Amazon EMR on EKS
<a name="connect-emr-studio"></a>

An *interactive endpoint* is a gateway that connects Amazon EMR Studio to Amazon EMR on EKS so that you can run interactive workloads. You can use interactive endpoints with EMR Studio to run interactive analytics with datasets in data stores like [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/gettingstartedguide/).

**Use cases**
+ Create an ETL script with the EMR Studio IDE experience. The IDE ingests on-premises data and stores it in Amazon S3 after transformations for subsequent analysis.
+ Use notebooks to explore datasets and train a machine-learning model to detect anomalies in the datasets.
+ Create scripts that generate daily reports for analytic applications like business dashboards.

**Topics**
+ [Overview of interactive endpoints](how-it-works.md)
+ [Prerequisites to create an interactive endpoint on Amazon EMR on EKS](prereqs-for-studio.md)
+ [Creating an interactive endpoint for your virtual cluster](create-managed-endpoint.md)
+ [Configuring settings for interactive endpoints](managed-endpoint-parameters.md)
+ [Monitoring interactive endpoints](managed-endpoints-customer-metrics.md)
+ [Using self-hosted Jupyter notebooks](managed-endpoints-self-hosted.md)
+ [Getting information about interactive endpoints with CLI commands](other-operations.md)