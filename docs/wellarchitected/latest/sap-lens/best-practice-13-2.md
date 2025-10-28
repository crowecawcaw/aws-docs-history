# Best Practice 13.2 - Select EC2

instances suitable for SAP workloads

AWS works with SAP to ensure that AWS services are suitable to implement and
operate SAP software across a wide selection of instance types. Use guidance from the
relevant SAP notes and documentation to identify suitable instances. EC2 instance families
offer different ratios of CPU and memory, as well as storage and network throughput
characteristics suitable for running SAP workloads. Map your requirements to the
appropriate instance type using performance metrics, SAPS figures, and compute estimates.
Confirm availability of these instances in your selected Region and Availability
Zone.

**Suggestion 13.2.1 – Follow SAP guidance on supported databases,
operating systems, and AWS services**

AWS offers services that can be used for the deployment of SAP products. SAP Note:
[1656099 - SAP
Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") describes which
SAP products, database and operating system combinations and Amazon EC2 instance types are
currently supported.

You can determine the availability of individual instance types within a specific AZ
using the AWS CLI [to describe instance type offerings](../../../cli/latest/reference/ec2/describe-instance-type-offerings.md "../../../cli/latest/reference/ec2/describe-instance-type-offerings.md").

- AWS Documentation: [Amazon EC2 Instance Types for SAP](https://aws.amazon.com/sap/instance-types/ "https://aws.amazon.com/sap/instance-types/")
- SAP Documentation: [SAP NetWeaver benchmarks](https://www.sap.com/dmc/exp/2018-benchmark-directory/#/sd?filters=v:4a9e824336e2837bf9081e423d576dba "https://www.sap.com/dmc/exp/2018-benchmark-directory/#/sd?filters=v:4a9e824336e2837bf9081e423d576dba")

**Suggestion 13.2.2 – Use hardware metrics and SAPS to guide
selection**

Each SAP supported Amazon EC2 instance family provides a specific vCPU to memory
ratio. You should evaluate each instance family based on your requirements to understand
the performance profile. The current generation of Amazon EC2 instances (based on [AWS Nitro](https://aws.amazon.com/ec2/nitro/ "https://aws.amazon.com/ec2/nitro/") ) offers the best
performance and should be used if available and certified for the deployment scenario.

SAP application servers can use either the general purpose (`m*`) or memory
optimized (`r*`) instances. Where there is a requirement for a higher vCPU to
memory ratio, consider using compute optimized (`c*`) instances. For AnyDB
database servers, memory optimized (`r*`) instances are a good fit for the
required core to memory ratio, but additional analysis should be done to validate the
sizing, especially if your deployment is subject to per-CPU licensing. For SAP HANA
databases that run in memory, memory optimized (`r*`, `x*`,
`u*`) are your only options.

**Suggestion 13.2.3 – Use SAP HANA hardware directory and memory
requirement to select EC2 instances for SAP HANA**

AWS has SAP HANA certification for a subset of Amazon EC2 instances to run SAP HANA
workloads. Details of these instances, and the IaaS application types supported (OLAP, OLTP,
SAP Business One, Scale-Out) can be found in [Certified and Supported SAP HANA Hardware](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23 "https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23") and [Amazon EC2 Instance Types for SAP](https://aws.amazon.com/sap/instance-types/ "https://aws.amazon.com/sap/instance-types/").

Database size and actual working memory usage will determine the memory requirement
and instance selection.

For non-production workloads, additional options exist. Refer to the blog:

- SAP on AWS Blog: [Smaller X1e instances for SAP HANA non-production workloads](https://aws.amazon.com/blogs/awsforsap/smaller-x1e-instances-for-sap-hana-non-production-workloads/ "https://aws.amazon.com/blogs/awsforsap/smaller-x1e-instances-for-sap-hana-non-production-workloads/")

**Suggestion 13.2.4 – Be aware of EC2 instance features and throughput
characteristics**

Amazon EC2 instances have different features and throughput characteristics which
should be evaluated based on your use case, particularly for workloads with high I/O and
throughput requirements. These include enhanced networking capabilities through the [Elastic Network Adapter (ENA)](../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md#ena-performance "../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md#ena-performance"), I/O performance, Amazon EBS optimization, and
suitability for placement groups. For a full list of features, see:

- AWS Documentation: [General Purpose Instances](../../../AWSEC2/latest/UserGuide/general-purpose-instances.md "../../../AWSEC2/latest/UserGuide/general-purpose-instances.md")
- AWS Documentation: [Memory Optimized Instances](../../../AWSEC2/latest/UserGuide/memory-optimized-instances.md "../../../AWSEC2/latest/UserGuide/memory-optimized-instances.md")
- AWS Documentation: [Compute Optimized Instances](../../../AWSEC2/latest/UserGuide/compute-optimized-instances.md "../../../AWSEC2/latest/UserGuide/compute-optimized-instances.md")
