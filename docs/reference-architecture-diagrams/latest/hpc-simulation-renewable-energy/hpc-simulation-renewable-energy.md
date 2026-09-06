

# HPC Simulation Workload for Renewable Energy Data
<a name="hpc-simulation-renewable-energy"></a>

Publication date: **September 28, 2022 ([Diagram history](#hpc-re-history))**

With this architecture, you can ingest data from on-premises renewable energy assets such as weather stations, wind turbines, and solar panels. You can also run high performance computing (HPC) and artificial intelligence/machine learning (AI/ML) workloads on that data. The solution uses [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) for device connectivity, [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/) for HPC infrastructure, and [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) for dashboarding.

## HPC simulation workload diagram
<a name="hpc-re-diagram"></a>

![Reference architecture diagram showing how to run HPC simulation workloads for renewable energy data by using AWS IoT Core, AWS ParallelCluster, and Amazon Quick Sight.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/hpc-simulation-renewable-energy/images/hpc-simulation-renewable-energy.png)


The following steps describe the data ingestion, compute, and visualization pipeline for this architecture:

1. Connect on-premises assets such as solar panels, wind turbines, or weather stations.

1. Use AWS IoT Core to connect IoT devices and route messages to AWS services. Use [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/) to simplify collecting, organizing, and analyzing industry equipment data.

1. Collect and process large streams of data records in real time by using [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/). Deliver near-real-time data streams from your source destination by using [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/).

1. Store processed data in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/)-based central data lake repositories.

1. Use AWS ParallelCluster with [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/) templates to create HPC infrastructure. Interface directly with the cluster through NICE DCV or Secure Shell (SSH). Use [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/) as a high-performance parallel file system for shared storage between the HPC cluster nodes. Integrate FSx for Lustre with Amazon S3 buckets for accessing simulation input and output data.

1. Use [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) for data preparation and task building views of report data.

1. Use Amazon Quick Sight to query and build visualizations to discover insights into your data. Use an [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) Crawler to discover schemas and store them in the AWS Glue Data Catalog. Classify schemas for common file formats such as JSON and CSV.

## Further reading
<a name="hpc-re-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="hpc-re-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#hpc-re-history) | Reference architecture diagram first published. | September 28, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.