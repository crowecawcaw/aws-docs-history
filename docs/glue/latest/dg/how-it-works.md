# AWS Glue: How it works

AWS Glue uses other AWS services to orchestrate your ETL (extract, transform, and load)
jobs to build data warehouses and data lakes and generate output streams. AWS Glue calls API
operations to transform your data, create runtime logs, store your job logic, and create
notifications to help you monitor your job runs. The AWS Glue console connects these services into
a managed application, so you can focus on creating and monitoring your ETL work. The console
performs administrative and job development operations on your behalf. You supply credentials
and other properties to AWS Glue to access your data sources and write to your data targets.

AWS Glue takes care of provisioning and managing the resources that are required to run your
workload. You don't need to create the infrastructure for an ETL tool because AWS Glue does it for
you. When resources are required, to reduce startup time, AWS Glue uses an instance from its warm
pool of instances to run your workload.

With AWS Glue, you create jobs using table definitions in your Data Catalog. Jobs consist of scripts that contain the
instructions that execute the desired data transformation tasks. You use triggers to
initiate jobs either on a schedule or as a result of a specified event. You determine where your
target data resides and which source data populates your target. Based on your inputs, AWS Glue
transforms your data from the source to the target format. Alternatively, you can also
provide custom scripts in the AWS Glue console or API to process your data according to your specific requirements.

###### Data sources and destinations

AWS Glue for Spark allows you to read and write data from multiple systems and databases including:

- Amazon S3
- Amazon DynamoDB
- Amazon Redshift
- Amazon Relational Database Service (Amazon RDS)
- Third-party JDBC-accessible databases
- MongoDB and Amazon DocumentDB (with MongoDB compatibility)
- Other marketplace connectors and Apache Spark plugins

###### Data streams

AWS Glue for Spark can stream data from the following systems:

- Amazon Kinesis Data Streams
- Apache Kafka
  AWS Glue is available in several AWS Regions. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the Amazon Web Services General Reference.

###### Topics

- [Serverless ETL jobs run in isolation](#how-it-works-isolation "#how-it-works-isolation")
- [AWS Glue concepts](components-key-concepts.md "components-key-concepts.md")
- [AWS Glue components](components-overview.md "components-overview.md")
- [AWS Glue for Spark and AWS Glue for Ray](how-it-works-engines.md "how-it-works-engines.md")
- [Converting
  semi-structured
  schemas
  to
  relational
  schemas
  with AWS Glue](schema-relationalize.md "schema-relationalize.md")
- [AWS Glue type systems](glue-types.md "glue-types.md")

## Serverless ETL jobs run in isolation

AWS Glue runs your ETL jobs in a serverless environment with your choice of engine, Spark or Ray.
AWS Glue runs these jobs on virtual resources that it provisions and manages in its own service
account.

AWS Glue is designed to do the following:

- Segregate customer data.
- Protect customer data in transit and at rest.
- Access customer data only as needed in response to customer requests, using temporary,
  scoped-down credentials, or with a customer's consent to IAM roles in their
  account.

During provisioning of an ETL job, you provide input data sources and output data targets
in your virtual private cloud (VPC). In addition, you provide the IAM role, VPC ID, subnet
ID, and security group that are needed to access data sources and targets. For each tuple
(customer account ID, IAM role, subnet ID, and security group), AWS Glue creates a new
environment that is isolated at the network and management level from all other
environments inside your AWS Glue service account.

You create and configure AWS Glue resources, such as Data Catalogs, Jobs, and Crawlers within your AWS account.
These resources are then associated with the IAM role and network settings (subnet and security group) you specify during the
creation process.

AWS Glue creates elastic network interfaces in your subnet using private IP addresses.
Jobs use these elastic network interfaces to access your data sources and data targets.
Traffic in, out, and within the job run environment is governed by your VPC and networking
policies with one exception: Calls made to AWS Glue libraries can proxy traffic to AWS Glue API
operations through the AWS Glue VPC. All AWS Glue API calls are logged; thus, data owners can audit
API access by enabling [AWS CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md"), which delivers audit logs to your account.

AWS Glue managed environments that run your ETL jobs are protected with the same
security practices followed by other AWS services. For an overview of the practices and shared
security responsibilities, see the [Introduction to AWS Security Processes](../../../whitepapers/latest/introduction-aws-security/welcome.md "../../../whitepapers/latest/introduction-aws-security/welcome.md") whitepaper.
