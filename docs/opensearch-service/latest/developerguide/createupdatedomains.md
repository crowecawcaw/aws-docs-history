# Creating and managing Amazon OpenSearch Service domains

This chapter describes how to create and manage Amazon OpenSearch Service domains. A domain is the
AWS-provisioned equivalent of an open source OpenSearch cluster. When you create a domain,
you specify its settings, instance types, instance counts, and storage allocation. For more
information about open source clusters, see [Creating a cluster](https://opensearch.org/docs/latest/tuning-your-cluster/ "https://opensearch.org/docs/latest/tuning-your-cluster/")
in the OpenSearch documentation.

Unlike the brief instructions in the [Getting started tutorial](gsg.md "gsg.md"),
this chapter describes all options and provides relevant reference information. You can
complete each procedure by using instructions for the OpenSearch Service console, the AWS Command Line Interface (AWS CLI),
or the AWS SDKs.

## Creating OpenSearch Service domains

This section describes how to create OpenSearch Service domains by using the OpenSearch Service console or by
using the AWS CLI with the `create-domain` command.

### Creating OpenSearch Service domains (console)

Use the following procedure to create an OpenSearch Service domain by using the console.

###### To create an OpenSearch Service domain (console)

1. Go to [https://aws.amazon.com](https://aws.amazon.com "https://aws.amazon.com")
   and choose **Sign In to the Console**.
2. Under **Analytics**, choose
   **Amazon OpenSearch Service**.
3. Choose **Create domain**.
4. For **Domain name**, enter a domain name. The name must
   meet the following criteria:
   - Unique to your account and AWS Region
   - Starts with a lowercase letter
   - Contains between 3 and 28 characters
   - Contains only lowercase letters a-z, the numbers 0-9, and the
     hyphen (-)

5. For the domain creation method, choose **Standard
   create**.
6. For **Templates**, choose the option that best matches
   the purpose of your domain:
   - **Production** domains for workloads that need
     high-availability and performance. These domains use Multi-AZ (with
     or without standby) and dedicated master nodes for higher
     availability.
   - **Dev/test** for development or testing. These
     domains can use Multi-AZ (with or without standby) or a single
     Availability Zone.

   ###### Important

   Different deployment types present different options on
   subsequent pages. These steps include all options.

7. For **Deployment Option(s)**, choose **Domain
   with standby** to configure a 3-AZ domain, with nodes in one of
   the zones are reserved as standby. This option enforces a number of best
   practices, such as a specified data node count, master node count, instance
   type, replica count, and software update settings.
8. For **Version**, choose the version of OpenSearch or
   legacy Elasticsearch OSS to use. We recommend that you choose the latest
   version of OpenSearch. For more information, see [Supported versions of Elasticsearch and
   OpenSearch](what-is.md#choosing-version "what-is.md#choosing-version").

(Optional) If you chose an OpenSearch version for your domain, select
**Enable compatibility mode** to make OpenSearch
report its version as 7.10, which allows certain Elasticsearch OSS clients
and plugins that check the version before connecting to continue working
with the service. 9. For **Instance type**, choose an instance type for your
data nodes. For more information, see [Supported instance types in Amazon OpenSearch Service](supported-instance-types.md "supported-instance-types.md").

###### Note

Not all Availability Zones support all instance types. If you choose
Multi-AZ with or without Standby, we recommend choosing
current-generation instance types, such as R5 or I3. 10. For **Number of nodes**, choose the number of data
nodes.

For maximum values, see [OpenSearch Service domain and instance quotas](../../../general/latest/gr/opensearch-service.md#opensearch-limits-domain "../../../general/latest/gr/opensearch-service.md#opensearch-limits-domain"). Single-node clusters are fine
for development and testing, but should not be used for production
workloads. For more guidance, see [Sizing Amazon OpenSearch Service domains](sizing-domains.md "sizing-domains.md") and [Configuring a multi-AZ domain in Amazon OpenSearch Service](managedomains-multiaz.md "managedomains-multiaz.md").

###### Note

(Optional)Dedicated coordinator nodes support all OpenSearch versions
and ElasticSearch versions 6.8 through 7.10. Dedicated coordinator nodes
are available for use with domains that have a dedicated cluster manager
enabled. To enable dedicated coordinator nodes, you will select the
instance type and count. As a best practice, you should keep the
instance family for your dedicated coordinator node the same as your
data nodes (Intel based instances or Graviton based instances). 11. For **Storage type**, select Amazon EBS. The volume types
available in the list depend on the instance type that you've chosen. For
guidance on creating especially large domains, see [Petabyte scale in Amazon OpenSearch Service](petabyte-scale.md "petabyte-scale.md"). 12. For **EBS** storage, configure the following additional
settings. Some settings might not appear depending on the type of volume you
choose.

| Setting                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EBS volume type**           | Choose between [General Purpose (SSD)<br>• gp3](../../../AWSEC2/latest/UserGuide/general-purpose.md#gp3-ebs-volume-type "../../../AWSEC2/latest/UserGuide/general-purpose.md#gp3-ebs-volume-type") and [General Purpose (SSD)<br>• gp2](../../../AWSEC2/latest/UserGuide/general-purpose.md#EBSVolumeTypes_gp2 "../../../AWSEC2/latest/UserGuide/general-purpose.md#EBSVolumeTypes_gp2"), or the<br>previous generation [Provisioned IOPS (SSD)](../../../AWSEC2/latest/UserGuide/provisioned-iops.md#EBSVolumeTypes_piops "../../../AWSEC2/latest/UserGuide/provisioned-iops.md#EBSVolumeTypes_piops"), and [Magnetic](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes_standard.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes_standard.md") (standard). |
| **EBS storage size per node** | Enter the size of the EBS volume that you want to<br>attach to each data node.<br>EBS volume size is per node. You can calculate the<br>total cluster size for the OpenSearch Service domain by multiplying<br>the number of data nodes by the EBS volume size. The<br>minimum and maximum size of an EBS volume depends on<br>both the specified EBS volume type and the instance type<br>that it's attached to. To learn more, see [EBS volume size<br>limits](limits.md#ebsresource "limits.md#ebsresource").                                                                                                                                                                                                                                               |
| **Provisioned IOPS**          | If you selected a Provisioned IOPS SSD volume type,<br>enter the number of I/O operations per second (IOPS)<br>that the volume can support.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

13. (Optional) If you selected a `gp3` volume type, expand
    **Advanced settings** and specify additional IOPS (up
    to 16,000 for every 3 TiB volume size provisioned per data node) and
    throughput (up to 1,000 MiB/s for every 3 TiB volume size provisioned per
    data node) beyond what is included with the price of storage, for an
    additional cost. For more information, see the [Amazon
    OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").
14. (Optional) To enable [UltraWarm storage](ultrawarm.md "ultrawarm.md"),
    choose **Enable UltraWarm data nodes**. Each instance type
    has a [maximum amount of storage](limits.md#limits-ultrawarm "limits.md#limits-ultrawarm") that
    it can address. Multiply that amount by the number of warm data nodes for
    the total addressable warm storage.
15. (Optional) To enable [cold storage](cold-storage.md "cold-storage.md"),
    choose **Enable cold storage**. You must enable
    UltraWarm to enable cold storage.
16. If you use Multi-AZ with Standby, three [dedicated master
    nodes](managedomains-dedicatedmasternodes.md "managedomains-dedicatedmasternodes.md") are aleady enabled. Choose the type of master nodes that
    you want. If you chose a Multi-AZ without Standby domain, select
    **Enable dedicated master nodes** and choose the type
    and number of master nodes that you want. Dedicated master nodes increase
    cluster stability and are required for domains that have instance counts
    greater than 10. We recommend three dedicated master nodes for production
    domains.

###### Note

You can choose different instance types for your dedicated master
nodes and data nodes. For example, you might select general purpose or
storage-optimized instances for your data nodes, but compute-optimized
instances for your dedicated master nodes. 17. (Optional) For domains running OpenSearch or Elasticsearch 5.3 and later,
the **Snapshot configuration** is irrelevant. For more
information about automated snapshots, see [Creating index snapshots in Amazon OpenSearch Service](managedomains-snapshots.md "managedomains-snapshots.md"). 18. If you want to use a custom endpoint rather than the standard one of
`https://search-`mydomain`-`1a2a3a4a5a6a7a8a9a0a9a8a7a`.`us-east-1`.es.amazonaws.com`
, choose **Enable custom endpoint** and provide a name and
certificate. For more information, see [Creating a custom endpoint for Amazon OpenSearch Service](customendpoint.md "customendpoint.md"). 19. Under **Network**, choose either **VPC
access** or **Public access**. If you choose
**Public access**, skip to the next step. If you choose
**VPC access**, make sure you meet the [prerequisites](vpc.md#prerequisites-vpc-endpoints "vpc.md#prerequisites-vpc-endpoints"), then
configure the following settings:

| Setting             | Description                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VPC**             | Choose the ID of the virtual private cloud (VPC) that<br>you want to use. The VPC and domain must be in the same<br>AWS Region, and you must select a VPC with tenancy set<br>to **Default**. OpenSearch Service does not yet<br>support VPCs that use dedicated tenancy.                                                                                                                                                                |
| **Subnet**          | Choose a subnet. If you enabled Multi-AZ, you must<br>choose two or three subnets. OpenSearch Service will place a VPC<br>endpoint and \*elastic network<br>interfaces<br>• in the subnets.<br>You must reserve sufficient IP addresses for the<br>network interfaces in the subnet(s). For more<br>information, see [Reserving IP<br>addresses in a VPC subnet](vpc.md#reserving-ip-vpc-endpoints "vpc.md#reserving-ip-vpc-endpoints"). |
| **Security groups** | Choose one or more VPC security groups that allow your<br>required application to reach the OpenSearch Service domain on the<br>ports (80 or 443) and protocols (HTTP or HTTPS) exposed<br>by the domain. For more information, see [Launching your Amazon OpenSearch Service domains within a VPC](vpc.md "vpc.md").                                                                                                                    |
| **IAM Role**        | Keep the default role. OpenSearch Service uses this predefined role<br>(also known as a _service-linked<br>role_) to access your VPC and to place a<br>VPC endpoint and network interfaces in the subnet of the<br>VPC. For more information, see [Service-linked role for VPC<br>access](vpc.md#enabling-slr "vpc.md#enabling-slr").                                                                                                    |
| **IP Address Type** | Choose either dual stack or IPv4 as your IP address<br>type. Dual stack allows you to share domain resources<br>across IPv4 and IPv6 address types, and is the<br>recommended option. If you set your IP address type to<br>dual stack, you can't change your address type<br>later.                                                                                                                                                     |

20. Enable or disable fine-grained access control:

        * If you want to use IAM for user management, choose **Set
         IAM ARN as master user** and specify the ARN for an
         IAM role.
        * If you want to use the internal user database, choose
         **Create master user** and specify a username
         and password.

    Whichever option you choose, the master user can access all indexes in the
    cluster and all OpenSearch APIs. For guidance on which option to choose, see
    [Key concepts](fgac.md#fgac-concepts "fgac.md#fgac-concepts").

If you disable fine-grained access control, you can still control access
to your domain by placing it within a VPC, applying a restrictive access
policy, or both. You must enable node-to-node encryption and encryption at
rest to use fine-grained access control.

###### Note

We _strongly_ recommend enabling fine-grained
access control to protect the data on your domain. Fine-grained access
control provides security at the cluster, index, document, and field
levels. 21. (Optional) If you want to use SAML authentication for OpenSearch Dashboards,
choose **Enable SAML authentication** and configure SAML
options for the domain. For instructions, see [SAML authentication for OpenSearch Dashboards](saml.md "saml.md"). 22. (Optional) If you want to use Amazon Cognito authentication for OpenSearch Dashboards,
choose **Enable Amazon Cognito authentication**. Then choose the
Amazon Cognito user pool and identity pool that you want to use for OpenSearch Dashboards
authentication. For guidance on creating these resources, see [Configuring Amazon Cognito authentication for OpenSearch
Dashboards](cognito-auth.md "cognito-auth.md"). 23. (Optional) If you want to use IAM Identity Center (IDC) authentication
to connect your existing identity source and give your AWS applications a
common view of your users, choose **Enable API access authenticated
with IAM Identity Center** . For more information, see [Trusted identity propagation overview](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") in the _IAM Identity Center User Guide._ 24. (Optional) In the **Advanced features** section, leave
**Enable Natural Language Query Generation and Amazon Q Developer
features** selected, if you want to use these features.

    1. Choose **Enable S3 Vectors as an engine option**
     for enhanced vector search options. For more information, see [Advanced search
     capabilities with an Amazon S3 vector engine](s3-vector-opensearch-integration-engine.md "s3-vector-opensearch-integration-engine.md").
    2. Choose **Enable GPU acceleration for enhanced vector
     search options. For more information, see [GPU-acceleration for vector indexing](gpu-acceleration-vector-index.md "gpu-acceleration-vector-index.md").**

25. For **Access policy**, choose an access policy or
    configure one of your own. If you choose to create a custom policy, you can
    configure it yourself or import one from another domain. For more
    information, see [Identity and Access Management in Amazon OpenSearch Service](ac.md "ac.md").

###### Note

If you enabled VPC access, you can't use IP-based policies. Instead,
you can use [security
groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") to control which IP addresses can access the domain.
For more information, see [About access policies on VPC domains](vpc.md#vpc-security "vpc.md#vpc-security"). 26. (Optional) To require that all requests to the domain arrive over HTTPS,
select **Require HTTPS for all traffic to the domain**. To
enable node-to-node encryption, select **Node-to-node
encryption**. For more information, see [Node-to-node encryption for Amazon OpenSearch Service](ntn.md "ntn.md").
To enable encryption of data at rest, select **Enable encryption of
data at rest**. These options are pre-selected if you chose the
Multi-AZ with Standby deployment option. 27. (Optional) Select **Use AWS owned key** to have OpenSearch Service
create an AWS KMS encryption key on your behalf (or use the one that it
already created). Otherwise, choose your own KMS key. For more
information, see [Encryption of data at rest for Amazon OpenSearch Service](encryption-at-rest.md "encryption-at-rest.md"). 28. For **Off-peak window**, select a start time to schedule
service software updates and Auto-Tune optimizations that require a
blue/green deployment. Off-peak updates help to minimize strain on a
cluster's dedicated master nodes during high traffic periods. 29. For **Auto-Tune**, choose whether to allow OpenSearch Service to
suggest memory-related configuration changes to your domain to improve speed
and stability. For more information, see [Auto-Tune for Amazon OpenSearch Service](auto-tune.md "auto-tune.md").

(Optional) Select **Off-peak window** to schedule a
recurring window during which Auto-Tune updates the domain. 30. (Optional) Select **Automatic software update** to enable
automatic software updates. 31. (Optional) Add tags to describe your domain so you can categorize and
filter on that information. For more information, see [Tagging Amazon OpenSearch Service domains](managedomains-awsresourcetagging.md "managedomains-awsresourcetagging.md"). 32. (Optional) Expand and configure **Advanced cluster
settings**. For a summary of these options, see [Advanced cluster
settings](#createdomain-configure-advanced-options "#createdomain-configure-advanced-options"). 33. Choose **Create**.

### Creating OpenSearch Service domains (AWS CLI)

Instead of creating an OpenSearch Service domain by using the console, you can use the AWS CLI.
For syntax, see Amazon OpenSearch Service in the [AWS CLI command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html")a.

#### Example commands

This first example demonstrates the following OpenSearch Service domain
configuration:

- Creates an OpenSearch Service domain named _mylogs_ with
  OpenSearch version 1.2
- Populates the domain with two instances of the
  `r6g.large.search` instance type
- Uses a 100 GiB General Purpose (SSD) `gp3` EBS volume for
  storage for each data node
- Allows anonymous access, but only from a single IP address:
  192.0.2.0/32

```
aws opensearch create-domain \
    --domain-name mylogs \
    --engine-version OpenSearch_1.2 \
    --cluster-config  InstanceType=r6g.large.search,InstanceCount=2 \
    --ebs-options EBSEnabled=true,VolumeType=gp3,VolumeSize=100,Iops=3500,Throughput=125 \
    --access-policies '{"Version": "2012-10-17",		 	 	  "Statement": [{"Action": "es:*", "Principal":"*","Effect": "Allow", "Condition": {"IpAddress":{"aws:SourceIp":["192.0.2.0/32"]}}}]}'
```

The next example demonstrates the following OpenSearch Service domain configuration:

- Creates an OpenSearch Service domain named _mylogs_ with
  Elasticsearch version 7.10
- Populates the domain with six instances of the
  `r6g.large.search` instance type
- Uses a 100 GiB General Purpose (SSD) `gp2` EBS volume for
  storage for each data node
- Restricts access to the service to a single user, identified by the
  user's AWS account ID: 555555555555
- Distributes instances across three Availability Zones

```
aws opensearch create-domain \
    --domain-name mylogs \
    --engine-version Elasticsearch_7.10 \
    --cluster-config  InstanceType=r6g.large.search,InstanceCount=6,ZoneAwarenessEnabled=true,ZoneAwarenessConfig={AvailabilityZoneCount=3} \
    --ebs-options EBSEnabled=true,VolumeType=gp2,VolumeSize=100 \
    --access-policies '{"Version": "2012-10-17",		 	 	  "Statement": [ { "Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::`555555555555`:root" }, "Action":"es:*", "Resource": "arn:aws:es:us-east-1:`555555555555`:domain/mylogs/*" } ] }'
```

The next example demonstrates the following OpenSearch Service domain configuration:

- Creates an OpenSearch Service domain named _mylogs_ with
  OpenSearch version 1.0
- Populates the domain with ten instances of the
  `r6g.xlarge.search` instance type
- Populates the domain with three instances of the
  `r6g.large.search` instance type to serve as dedicated
  master nodes
- Uses a 100 GiB Provisioned IOPS EBS volume for storage, configured
  with a baseline performance of 1000 IOPS for each data node
- Restricts access to a single user and to a single subresource, the
  `_search` API

```
aws opensearch create-domain \
    --domain-name mylogs \
    --engine-version OpenSearch_1.0 \
    --cluster-config  InstanceType=r6g.xlarge.search,InstanceCount=10,DedicatedMasterEnabled=true,DedicatedMasterType=r6g.large.search,DedicatedMasterCount=3 \
    --ebs-options EBSEnabled=true,VolumeType=io1,VolumeSize=100,Iops=1000 \
    --access-policies '{"Version": "2012-10-17",		 	 	  "Statement": [ { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::`555555555555`:root" }, "Action": "es:*", "Resource": "arn:aws:es:us-east-1:`555555555555`:domain/mylogs/_search" } ] }'
```

###### Note

If you attempt to create an OpenSearch Service domain and a domain with the same name
already exists, the CLI does not report an error. Instead, it returns
details for the existing domain.

### Creating OpenSearch Service domains (AWS SDKs)

The AWS SDKs (except the Android and iOS SDKs) support all the actions defined
in the [Amazon OpenSearch Service API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md"), including `CreateDomain`. For sample code, see
[Using the AWS SDKs to interact with
Amazon OpenSearch Service](configuration-samples.md "configuration-samples.md"). For more information about installing
and using the AWS SDKs, see [AWS Software
Development Kits](http://aws.amazon.com/code "http://aws.amazon.com/code").

### Creating OpenSearch Service domains

(AWS CloudFormation)

OpenSearch Service is integrated with AWS CloudFormation, a service that helps you to
model and set up your AWS resources so that you can spend less time creating and
managing your resources and infrastructure. You create a template that describes the
OpenSearch domain you want to create, and CloudFormation provisions and configures the
domain for you. For more information, including examples of JSON and YAML templates
for OpenSearch domains, see the [Amazon OpenSearch Service resource type reference](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.md") in the
_AWS CloudFormation User Guide_.

## Configuring access

policies

Amazon OpenSearch Service offers several ways to configure access to your OpenSearch Service domains. For more
information, see [Identity and Access Management in Amazon OpenSearch Service](ac.md "ac.md") and [Fine-grained access control in Amazon OpenSearch Service](fgac.md "fgac.md").

The console provides preconfigured access policies that you can customize for the
specific needs of your domain. You also can import access policies from other OpenSearch Service
domains. For information about how these access policies interact with VPC access, see
[About access policies on VPC domains](vpc.md#vpc-security "vpc.md#vpc-security").

###### To configure access policies (console)

1. Go to [https://aws.amazon.com](https://aws.amazon.com "https://aws.amazon.com"), and
   then choose **Sign In to the Console**.
2. Under **Analytics**, choose
   **Amazon OpenSearch Service**.
3. In the navigation pane, under **Domains**, choose the domain
   you want to update.
4. Choose **Actions** and **Edit security
   configuration**.
5. Edit the access policy JSON, or import a preconfigured option.
6. Choose **Save changes**.

## Migrating to OpenSearch Service with Migration Assistant

Migration Assistant for Amazon OpenSearch Service is a comprehensive solution that simplifies the
process of migrating from self-managed Elasticsearch or OpenSearch clusters to OpenSearch Service.
This toolkit addresses the operational complexity of migrations while ensuring data
integrity and validating performance post-migration.

### Overview

Whether you're setting up a proof-of-concept in AWS, transitioning production
workloads, or upgrading to the latest OpenSearch versions, Migration Assistant
provides step-by-step guidance, best practices, and tools to leverage the full
potential of OpenSearch migrations.

The Migration Assistant offers the following key benefits:

- **Metadata migration** - Migrates cluster
  metadata, including index settings, type mappings, index templates, and
  aliases
- **Data migration** - Migrates existing data
  from legacy clusters to OpenSearch Service domains
- **Live traffic handling** - Intercepts and
  redirects live traffic from self-managed clusters to OpenSearch Service domains with
  minimal latency
- **Traffic replication** - Replicates
  production traffic on target clusters to validate accuracy and
  performance
- **Performance testing** - Simulates
  real-world traffic by capturing and replaying request patterns to fine-tune
  system performance
- **Global availability** - Deploys across the
  most common AWS Regions for global reach and scalability

Migration Assistant supports migrating from Elasticsearch versions 6.x and 7.x,
and OpenSearch 1.x and 2.x. For more information, see [Supported migration paths](https://docs.opensearch.org/latest/migration-assistant/is-migration-assistant-right-for-you/#supported-migration-paths "https://docs.opensearch.org/latest/migration-assistant/is-migration-assistant-right-for-you/#supported-migration-paths").

###### Note

Note the following additional information about Migration Assistant.

- The tool supports multi-hop migrations (for example, migration from
  Elasticsearch 5.x to OpenSearch Service 3.x in one hop).
- You can roll back a migration.
- For some use cases, the tool requires little or no downtime.
- The tool provides high-performance backfill without impacting a source
  cluster.

### Migration scenarios

The Migration Assistant is designed to handle the following migration
scenarios:

**Metadata migration**

Migrates cluster metadata such as index settings, aliases, and
templates from your source cluster to the target OpenSearch Service domain.

**Backfill migration**

Migrates existing or historical data from a source cluster to a target
OpenSearch Service domain, ensuring that all your important data is preserved during
the transition.

**Live traffic migration**

Replicates ongoing live traffic from your source cluster to the target
OpenSearch Service domain, allowing you to maintain service availability during
migration.

###### Important

Migration strategies aren't universally applicable. The Migration Assistant
provides guidance based on engineering best practices, but you should evaluate
your specific requirements and test thoroughly before migrating production
workloads.

### Getting started with Migration

Assistant

Migration Assistant for Amazon OpenSearch Service is available as an AWS Solution with
comprehensive documentation, deployment templates, and source code. To get started
with Migration Assistant:

###### To access Migration Assistant resources

1. Review the complete solution documentation at [Migration Assistant for Amazon OpenSearch Service solution overview](../../../solutions/latest/migration-assistant-for-amazon-opensearch-service/solution-overview.md "../../../solutions/latest/migration-assistant-for-amazon-opensearch-service/solution-overview.md").
2. Understand the costs and requirements by reading the [deployment planning guide](../../../solutions/latest/migration-assistant-for-amazon-opensearch-service/plan-your-deployment.md "../../../solutions/latest/migration-assistant-for-amazon-opensearch-service/plan-your-deployment.md").
3. Deploy the solution using the [deployment instructions](https://docs.opensearch.org/latest/migration-assistant/migration-phases/ "https://docs.opensearch.org/latest/migration-assistant/migration-phases/") and follow the [usage guide](../../../solutions/latest/migration-assistant-for-amazon-opensearch-service/use-the-solution.md "../../../solutions/latest/migration-assistant-for-amazon-opensearch-service/use-the-solution.md") to perform your migration.

For developers and advanced users, Migration Assistant source code and additional
documentation are available in the [OpenSearch
migrations GitHub repository](https://github.com/opensearch-project/opensearch-migrations "https://github.com/opensearch-project/opensearch-migrations").

### Solution architecture

When deployed in AWS, Migration Assistant uses several AWS services to provide
a comprehensive migration solution:

- **AWS CloudFormation** - Provides Infrastructure as
  Code (IaC) templates to deploy and configure Migration Assistant
- **OpenSearch Service** - The target service for your
  migrated search and analytics workloads
- **Amazon Managed Streaming for Apache Kafka** - Provides stream processing
  capabilities for durable storage and reuse of HTTP traffic
- **Amazon Elastic Container Service** - Runs the Migration Management
  Console and Traffic Replayer in secure, scalable containers
- **Amazon Elastic File System** - Provides scalable persistent
  storage for request and response data from both source and target
  clusters
- **Amazon Simple Storage Service** - Stores snapshots for
  historical backfill tasks and Infrastructure as Code content

For detailed architecture information, see [Migration Assistant architecture details](https://docs.opensearch.org/latest/migration-assistant/architecture/ "https://docs.opensearch.org/latest/migration-assistant/architecture/").

## Advanced cluster

settings

Use advanced options to configure the following:

**Indices in request bodies**

Specifies whether explicit references to indexes are allowed inside the
body of HTTP requests. Setting this property to `false` prevents
users from bypassing access control for subresources. By default, the value
is `true`. For more information, see [Advanced options and API considerations](ac.md#ac-advanced "ac.md#ac-advanced").

**Fielddata cache allocation**

Specifies the percentage of Java heap space that is allocated to field
data. By default, this setting is 20% of the JVM heap.

###### Note

Many customers query rotating daily indices. We recommend that you
begin benchmark testing with `indices.fielddata.cache.size`
configured to 40% of the JVM heap for most of these use cases. For very
large indices, you might need a large field data cache.

**Max clause count**

Specifies the maximum number of clauses allowed in a Lucene boolean query.
The default is 1,024. Queries with more than the permitted number of clauses
result in a `TooManyClauses` error. For more information, see
[the Lucene documentation](https://lucene.apache.org/core/6_6_0/core/org/apache/lucene/search/BooleanQuery.html "https://lucene.apache.org/core/6_6_0/core/org/apache/lucene/search/BooleanQuery.html").
