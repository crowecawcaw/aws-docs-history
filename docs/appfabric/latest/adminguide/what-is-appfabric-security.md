

# What is AWS AppFabric for security?
<a name="what-is-appfabric-security"></a>

AWS AppFabric for security quickly connects software as a service (SaaS) applications across your organization, so IT and security teams can easily manage and secure applications using a standard schema.

**Topics**
+ [Benefits](#benefits)
+ [Use cases](#use-cases)
+ [Accessing AppFabric for security](#acessing-appfabric)
+ [Related services](#related-services)
+ [Open Cybersecurity Schema Framework for AWS AppFabric](ocsf-schema.md)
+ [Prerequisites and recommendations to use AWS AppFabric](prerequisites.md)
+ [Get started with AWS AppFabric for security](getting-started-security.md)
+ [Supported applications in AppFabric for security](supported-applications.md)
+ [Compatible security tools and services in AppFabric for security](security-tools.md)
+ [Delete AWS AppFabric for security resources](delete-resources.md)

## Benefits
<a name="benefits"></a>

You can use AppFabric for security to do the following:
+ Connect your applications in minutes, and reduce operational costs.
+ Increase visibility across SaaS application data to elevate your security posture.

## Use cases
<a name="use-cases"></a>

You can use AppFabric for security to:
+ Connect your SaaS applications quickly
  + AppFabric for security natively connects top SaaS productivity and security applications to each other, providing a fully managed SaaS interoperability solution.
+ Elevate your security posture
  + Application data is automatically normalized, enabling administrators to set common policies, standardize security alerts, and easily manage user access across multiple applications.

## Accessing AppFabric for security
<a name="acessing-appfabric"></a>

AppFabric for security is available in the US East (N. Virginia), Europe (Ireland), and Asia Pacific (Tokyo) AWS Regions. For more information about AWS Regions, see [AWS AppFabric endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appfabric.html) in the *AWS General Reference*.

In each Region, you can access AppFabric for security in any of the following ways:

**AWS Management Console**

The AWS Management Console is a browser-based interface that you can use to create and manage AWS resources. The AppFabric console provides access to your AppFabric resources. You can use the AppFabric console to create and manage all AppFabric resources.

**AppFabric API**

To access AppFabric programmatically, use the AppFabric API, and issue HTTPS requests directly to the service. For more information, see the [AWS AppFabric API Reference](https://docs.aws.amazon.com/appfabric/latest/api/Welcome.html).

**AWS Command Line Interface (AWS CLI)**

With the AWS CLI, you can issue commands at your system's command line to interact with AppFabric and other AWS services. If you want to build scripts that perform tasks, the command line tools are also useful. For information about installing and using the AWS CLI, see the [AWS Command Line Interface User Guide for Version 2](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html). For information about the AWS CLI commands for AppFabric, see the [AppFabric section of the AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/appfabric/).

## Related services
<a name="related-services"></a>

You can use the following AWS services with AppFabric for security:

**Amazon Data Firehose**

Amazon Data Firehose is an extract, transform, and load (ETL) service that reliably captures, transforms, and delivers streaming data to data lakes, data stores, and analytics services. When you use AppFabric, you can choose to output your Open Cybersecurity Schema Framework (OCSF) normalized or raw audit logs in JSON format to a Firehose stream as your destination. For more information, see [Create an output location in Firehose](prerequisites.md#output-location-firehose).

**Amazon Security Lake**

Amazon Security Lake automatically centralizes security data from AWS environments, SaaS providers, on premises and cloud sources into a purpose-built data lake stored in your account. You can integrate AppFabric audit log data with Security Lake by selecting Amazon Data Firehose as a destination and configuring Firehose to deliver data in the correct format and path in Security Lake. For more information, see [Collecting data from custom sources](https://docs.aws.amazon.com/security-lake/latest/userguide/custom-sources.html) in the *Amazon Security Lake User Guide*.

**Amazon Simple Storage Service**

Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance. When you use AppFabric, you can choose to output your OCSF normalized (JSON or Apache Parquet) or raw (JSON) audit logs to a new or existing Amazon S3 bucket as your destination. For more information, see [Create an output location in Amazon S3](prerequisites.md#output-location-s3).

**Amazon Quick**

Quick powers data-driven organizations with unified business intelligence (BI) at hyperscale. With Quick, all users can meet varying analytic needs from the same source of truth through modern interactive dashboards, paginated reports, embedded analytics, and natural language queries. You can analyze AppFabric audit log data in Quick, by choosing the Amazon S3 bucket where your AppFabric logs are stored as your source. For more information, see [Creating a dataset using Amazon S3 files](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-s3.html) in the *Quick User Guide*. You can also import AppFabric data in Amazon S3 to Amazon Athena and select Amazon Athena as the data source in Quick. For more information, see [Creating a dataset using Amazon Athena data](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-athena.html) in the *Quick User Guide*.

**AWS Key Management Service**

With AWS Key Management Service (AWS KMS), you can create, manage, and control cryptographic keys across your applications and AWS services. When you create an app bundle in AppFabric, you set up an encryption key to securely protect your authorized application data. This key encrypts your data within the AppFabric service. AppFabric can use an AWS owned key created and managed by AppFabric on your behalf, or a customer managed key that you create and manage in AWS KMS. For more information, see [Create an AWS KMS key](prerequisites.md#create-kms-keys).