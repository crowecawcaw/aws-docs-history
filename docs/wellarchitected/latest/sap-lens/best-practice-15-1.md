# Best Practice 15.1 – Follow operating

system guidelines for SAP performance

SAP provides specific guidance on how best to tune for optimal performance for each of
the operating systems that are supported for the SAP software you are deploying. Be sure
to read all of the relevant SAP documentation on the operating system on which you are
deploying both to understand the relevant tuning parameters and to take advantage of any
operating system-specific options to make performance tuning easier and more
dynamic.

**Suggestion 15.1.1 – Review operating system-related SAP notes prior
to installation, version update, or infrastructure change**

When building or updating your operating system (through automation or manually)
confirm that the appropriate performance settings specific to your combination of SAP
software and operating system version are applied.

**Suggestion 15.1.2 – Evaluate operating system vendor-supplied SAP
tuning**

Red Hat and SUSE provide images and repositories which contain tools and configuration
optimized for running SAP. These are available in the AWS Marketplace or in a
bring-your-own-subscription (BYOS) model.

Vendors are invested in ensuring that their operating systems are optimised for the
SAP application. Using vendor-supplied tuning tools such as `saptune` or the
(Ansible) system roles for Red Hat Enterprise Linux can assist in defining a known
baseline for performance tuning. While this does not preclude tuning the operating system
to best accommodate your specific SAP workload, these tools can reduce the effort
associated with researching, calculating and applying the most common requirements.
Configuration associated with the `tuned` daemon can also adjust dynamically
using information it gathers from the system, including CPU count and available memory.

| Operating System             | Guidance                                                                                                                                                                                                          |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SUSE Linux Enterprise Server | SAP Note: [1275776<br>• Linux: Preparing SLES for SAP environments](https://launchpad.support.sap.com/#/notes/1275776 "https://launchpad.support.sap.com/#/notes/1275776") [Requires SAP<br>Portal Access]        |
| Red Hat Enterprise Linux     | SAP Note: [2777782<br>• SAP HANA DB: Recommended OS Settings for RHEL 8](https://launchpad.support.sap.com/#/notes/2777782 "https://launchpad.support.sap.com/#/notes/2777782") [Requires<br>SAP Portal Access]   |
| Microsoft Windows            | (Consult SAP or Vendor documentation for guidance)                                                                                                                                                                |
| Oracle Enterprise Linux      | SAP Note: [2478541<br>• Operating System Requirements for Oracle Database](https://launchpad.support.sap.com/#/notes/2478541 "https://launchpad.support.sap.com/#/notes/2478541") [Requires<br>SAP Portal Access] |

**Suggestion 15.1.3 – Apply relevant network parameters to the
operating system**

SAP system performance can be seriously impacted by network misconfiguration,
particularly in SAP HANA scale-out database designs as well as in communication between
different application server instances and the database instance in a system environment.
While in many cases in AWS, the maximum network throughput of an instance is dictated by
the instance family and size, tuning of the network settings at the operating system level
and in the SAP software itself can have an impact.

Refer to the following AWS and SAP recommendations:

- AWS Documentation: [Benchmarking Network Throughput between Amazon EC2 Linux instances in the same
  Amazon VPC](https://aws.amazon.com/premiumsupport/knowledge-center/network-throughput-benchmark-linux-ec2/ "https://aws.amazon.com/premiumsupport/knowledge-center/network-throughput-benchmark-linux-ec2/")
- AWS Documentation: [Elastic Network Adapter – High Performance Network Interface for Amazon EC2](https://aws.amazon.com/blogs/aws/elastic-network-adapter-high-performance-network-interface-for-amazon-ec2/ "https://aws.amazon.com/blogs/aws/elastic-network-adapter-high-performance-network-interface-for-amazon-ec2/")
- AWS Documentation: [Cluster Placement Groups](../../../AWSEC2/latest/UserGuide/placement-groups.md#placement-groups-cluster "../../../AWSEC2/latest/UserGuide/placement-groups.md#placement-groups-cluster")
- SAP Note: [2198693

* Key Monitoring Metrics for SAP on Amazon Web Services (AWS)](https://launchpad.support.sap.com/#/notes/2198693 "https://launchpad.support.sap.com/#/notes/2198693") [Requires
  SAP Portal Access]

- SAP Note: [1612283

* Hardware Configuration Standards and Guidance](https://launchpad.support.sap.com/#/notes/1612283 "https://launchpad.support.sap.com/#/notes/1612283") [Requires SAP Portal Access]

- SAP Note: [2081065

* Troubleshooting SAP HANA Network](https://launchpad.support.sap.com/#/notes/2081065 "https://launchpad.support.sap.com/#/notes/2081065") [Requires SAP Portal Access]

- SAP Note: [1100926

* FAQ: Network performance](https://launchpad.support.sap.com/#/notes/1100926 "https://launchpad.support.sap.com/#/notes/1100926") [Requires SAP Portal Access]
