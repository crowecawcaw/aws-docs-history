# Best Practice 18.3 – Evaluate

licensing impact and optimization options

When moving SAP workloads to AWS, there might be commercial impacts with the software
licenses your SAP workloads require. You should understand these impacts and the options
available to you.

###### Disclaimer

Any discussion of Database licensing policies in this document is for informational
purposes only and is based on the information available at the time of publication. For
more specific information, users should consult their own license agreements with the
specific Database Vendor.

**Suggestion 18.3.1 – Understand the impact of CPU and memory on
software license**

Evaluate the different vCPU and memory ratios available with the supported [Amazon EC2 Instance Types](https://aws.amazon.com/sap/instance-types/ "https://aws.amazon.com/sap/instance-types/") for
SAP to optimize license costs.

- SAP Documentation: [SAP HANA Allocated Memory Pools and Allocation Limits](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/bd43f1c0bb571014bf5acf22f379fd3d.html "https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/bd43f1c0bb571014bf5acf22f379fd3d.html")
  For Oracle based environments, review:

- [Oracle License Considerations, Licensing Oracle Software in the Cloud Computing
  Environment](http://www.oracle.com/us/corporate/pricing/cloud-licensing-070579.pdf "http://www.oracle.com/us/corporate/pricing/cloud-licensing-070579.pdf")
- Oracle Premium Support requirements detailed in SAP Note: [2069760 - Oracle Linux 7.x
  SAP Installation and Upgrade](https://launchpad.support.sap.com/#/notes/2069760 "https://launchpad.support.sap.com/#/notes/2069760") [Requires SAP Portal Access]
  For Microsoft Windows and SQL Server environments, review:

- AWS Documentation: [Microsoft Licensing on
  AWS](https://aws.amazon.com/windows/resources/licensing/ "https://aws.amazon.com/windows/resources/licensing/")
- SAP Note: [2139358

* Effect of changes in licensing terms of SQL Server](https://launchpad.support.sap.com/#/notes/2139358 "https://launchpad.support.sap.com/#/notes/2139358") [Requires SAP Portal
  Access]
  For IBM Db2 environments, review:

- [Eligible Public Cloud BYOSL Policy](https://www.ibm.com/software/passportadvantage/eligible_public_cloud_BYOSL_policy.html "https://www.ibm.com/software/passportadvantage/eligible_public_cloud_BYOSL_policy.html")
- AWS Documentation: [Track IBM license usage with AWS License Manager](https://aws.amazon.com/blogs/mt/track-ibm-license-usage-with-aws-license-manager/ "https://aws.amazon.com/blogs/mt/track-ibm-license-usage-with-aws-license-manager/")
  Understand the impact for ISV and third-party products licensed by CPU or memory:

- Consider the use of the [Optimize CPU](../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md "../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md") feature to optimize license costs
- Consider the use of [AWS License Manager](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md") to manage your software licenses and associated costs
- AWS Documentation: [Physical Cores by Amazon EC2 Instance Type](https://aws.amazon.com/ec2/physicalcores/ "https://aws.amazon.com/ec2/physicalcores/")

**Suggestion 18.3.2 – Understand operating system purchasing
options**

For each of the SAP supported operating systems, there is a set of purchasing options
available.

1. Amazon EC2 provided license
2. AWS Marketplace provided license
3. Bring your own licenses (BYOL)
   Not all options are available for each operating system. You should evaluate your
   requirements and licensing agreements to determine which option is the most cost
   effective. You can include the costs of the following operating systems as part of the
   Amazon EC2 cost:

- Windows Server
- Red Hat Enterprise Linux
- SUSE Linux Enterprise Server
  You can purchase the following operating systems via the AWS Marketplace:

- Red Hat Enterprise Linux for SAP (based on Red Hat Enterprise Linux base EC2
  cost)
- SUSE Linux Enterprise Server for SAP (based on Amazon Linux base EC2 cost)
  You use bring your own licenses (BYOL) for the following operating systems:

- Windows Server
- Red Hat Enterprise Linux1
- SUSE Linux Enterprise Server
- Red Hat Enterprise Linux for SAP2
- SUSE Linux Enterprise Server for SAP2
- Oracle Enterprise Linux (Oracle Premium Support requirements are detailed in SAP
  Note: [2069760 - Oracle
  Linux 7.x SAP Installation and Upgrade](https://launchpad.support.sap.com/#/notes/2069760 "https://launchpad.support.sap.com/#/notes/2069760") ) [Requires SAP Portal Access]
  1 Consider SAP Note: [2871484 - SAP supported
  variants of Red Hat Enterprise Linux](https://launchpad.support.sap.com/#/notes/0002871484 "https://launchpad.support.sap.com/#/notes/0002871484") [Requires SAP Portal Access] as SAP no
  longer supports standard Red Hat Enterprise Linux for any SAP workloads as of RHEL 8.

2 These products have a longer term support which might
reduce your operational costs for upgrades – see SUSE Documentation: [SUSE Enterprise Support
Policy](https://www.suse.com/support/policy-products/ "https://www.suse.com/support/policy-products/") and Red Hat Documentation: [Red Hat
Enterprise Support Policy](https://access.redhat.com/support/policy/updates/errata/#Long_Support "https://access.redhat.com/support/policy/updates/errata/#Long_Support") for more details.

**Suggestion 18.3.3 – Consider the use of Amazon EC2 Dedicated Hosts
to mitigate licensing restrictions**

Amazon EC2 offers Dedicated Hosts, which allow you to access hardware that's fully
dedicated for your use. You can use [your own licensed software](https://aws.amazon.com/windows/resources/licensing/#Bring_existing_licenses_to_Dedicated_Hosts "https://aws.amazon.com/windows/resources/licensing/#Bring_existing_licenses_to_Dedicated_Hosts") on dedicated infrastructure. Amazon EC2 Dedicated
Hosts integrate with [AWS License
Manager](https://aws.amazon.com/license-manager/ "https://aws.amazon.com/license-manager/"), a service which helps you manage your software licenses, including
Windows Server and SQL Server licenses.

**Suggestion 18.3.4 – Evaluate the cost benefits of moving away from a
per gigabyte or per core licensing model**

As part of your migration to cloud, consider use of the SAP Runtime database licensing
model.

SAP provides the ability for customers to license SAP HANA, SAP ASE and third-party
databases under their Runtime database license model. Runtime databases licensed from SAP
are solely to support software and SAP named users licensed from SAP. Runtime databases
from SAP are licensed as a percentage of the SAP software fee, commonly referred to as the
SAP Application Value (SAV).

Runtime licenses are not based on number of gigabytes of memory or CPU cores and
therefore can provide a cost benefit over per gigabyte or per core licensing models,
particularly when you have multiple non-production systems, as the SAP Runtime database
license applies to all environments covered under your SAP license agreement.

If you already have the right to use the SAP HANA Database Runtime license within
your SAP license agreement, you should determine if you additionally have the right to use
the SAP ASE Database Runtime license for SAP components that cannot use SAP HANA as the
underlying database or to reduce the infrastructure costs associated with using SAP HANA
for that component.

- Refer to the SAP Documentation: [SAP Product Use and Support Guide](https://www.sap.com/uk/about/trust-center/agreements/on-premise/product-use-and-support-terms.html?sort=latest_desc&tag=agreements:product-use-support-terms/on-premise-software/software-use-rights "https://www.sap.com/uk/about/trust-center/agreements/on-premise/product-use-and-support-terms.html?sort=latest_desc&tag=agreements:product-use-support-terms/on-premise-software/software-use-rights"), or consult with your SAP account
  team
