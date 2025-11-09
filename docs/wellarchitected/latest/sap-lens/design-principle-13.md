# 13 – Select the optimal compute solution

**How do you select the optimal compute solution for your SAP
workload?** Evaluate and estimate the performance requirements using metrics from
the SAP tools and existing workloads. Map the compute requirements to the SAP supported
instances best suited to your workload. Consider any specific storage or network requirements
for the instance types as well as the availability of the required instance types in your
chosen AWS Region and Availability Zones.

| ID        | Priority           | Best Practice                                                                           |
| --------- | ------------------ | --------------------------------------------------------------------------------------- |
| ☐ BP 13.1 | Required           | Evaluate or estimate performance requirements                                           |
| ☐ BP 13.2 | Required           | Select EC2 instances suitable for SAP workloads                                         |
| ☐ BP 13.3 | Highly Recommended | Select architectures which allow for independent scaling of<br>systems or components    |
| ☐ BP 13.4 | Highly Recommended | Choose instance location for performance considering network<br>performance and latency |

For more details, see the following information:

- AWS Documentation: [Amazon
  EC2 Instance Types for SAP](https://aws.amazon.com/sap/instance-types/ "https://aws.amazon.com/sap/instance-types/")
- SAP Documentation: [Certified and Supported SAP HANA Hardware](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=v:deCertified;ve:23 "https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=v:deCertified;ve:23")
- SAP Note: [1656099 -
  SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") [Requires
  SAP Portal Access]
- SAP Note: [1656250 -
  SAP on AWS: Support prerequisites](https://launchpad.support.sap.com/#/notes/1656250 "https://launchpad.support.sap.com/#/notes/1656250") [Requires SAP Portal Access]
