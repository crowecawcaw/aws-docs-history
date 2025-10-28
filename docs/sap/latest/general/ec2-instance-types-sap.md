# Amazon EC2 instance types for SAP on AWS

Amazon Elastic Compute Cloud (Amazon EC2) offers a wide selection of [instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") optimized to fit different use cases. The varying combinations of CPU, memory, storage, and networking capacity provide flexibility in selection of resources for your applications. You can choose the instance types that meet the requirements of your workload.

AWS has worked closely with SAP to test and certify Amazon EC2 instance types for SAP on AWS solutions. For more information, see [SAP Note 1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://me.sap.com/notes/1656099 "https://me.sap.com/notes/1656099") (requires SAP Portal access) and [SAP Certified and Supported SAP HANA Hardware Directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23 "https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23").

###### Topics

- [Instance type availability](#region-ec2-sap "#region-ec2-sap")
- [SAP NetWeaver supported instances](sap-netweaver-aws-ec2.md "sap-netweaver-aws-ec2.md")
- [SAP HANA certified and non-certified instances](sap-hana-aws-ec2.md "sap-hana-aws-ec2.md")
- [SAP Business One certified instances, version for SAP HANA](sap-b1-aws-ec2.md "sap-b1-aws-ec2.md")
- [Document history for instance types for SAP on AWS](doc-history-ec2-sap.md "doc-history-ec2-sap.md")

## Instance type availability

The availability of an Amazon EC2 instance type is based on your selected [Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/"). For more information about available instance types in your Region, see [Amazon EC2 instance types by Region](../../../ec2/latest/instancetypes/ec2-instance-regions.md "../../../ec2/latest/instancetypes/ec2-instance-regions.md") in the _Amazon EC2 Instance Types Guide_.

###### Note

Certain Amazon EC2 instance families, such as X1, X2idn, X2iedn, and High Memory might not be available across all Availability Zones in a Region. You must confirm while planning that the instance types required for your SAP workloads are available in your target Availability Zone.

You can also determine the availability of an instance type in a Region and its Availability Zone by using the [describe-instance-type-offerings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-type-offerings.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-type-offerings.html") command. For examples, see [Find an instance type using the AWS CLI](../../../AWSEC2/latest/UserGuide/instance-discovery.md#instance-discovery-cli "../../../AWSEC2/latest/UserGuide/instance-discovery.md#instance-discovery-cli") in the _Amazon EC2 User Guide_.
