# Discover source

data

In the **Job Plan** pane expand **Discover source
data**, and then choose **Perform discovery**.

To collect source data, set up one of the two types of AWS collectors. These
collectors gather data that AWS Transform can use to generate Amazon EC2 recommendations and
wave plans for you. If you don't use these AWS collectors, you can upload an
[RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools") file in which you specify
application groupings and waves.

AWS Transform uses all of the data collected in the source AWS account for its
analysis. As a result, you will see all files that were imported with previous jobs
that used the same source account. Importing the same file again will not create
conflicts because AWS Transform automatically handles the de-duplication of servers in
its analysis.

###### Warning

The official RVTools site is [https://www.dell.com/en-us/shop/vmware/sl/rvtools](https://www.dell.com/en-us/shop/vmware/sl/rvtools " https://www.dell.com/en-us/shop/vmware/sl/rvtools"), which
is the site that this guide links to in steps that mention RVTools. Beware of
the scam site (rvtools)(dot)(org).

###### Note

There is a known issue with RVTools 4.7.1. Learn more in [RVTools 4.7.1 bug with VMware Cloud on AWS](https://repost.aws/articles/ARkRdniPpcS_y1eNz6_W1T4w/rvtools-4-7-1-bug-with-vmware-cloud-on-aws "https://repost.aws/articles/ARkRdniPpcS_y1eNz6_W1T4w/rvtools-4-7-1-bug-with-vmware-cloud-on-aws").

To get network translation, you must upload an NSX export or an [RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools") export.

[RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools") file: This type of file is
used for networks that use vSphere constructs. [RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools") is a utility that exports detailed information about your
VMware environment, including vSwitches, port groups, and VLANs. You can upload either a
ZIP of .csv files or an excel file that RVTools produces when you
choose **Export all to Excel** from the RVTools **File** menu.

Import/Export for NSX file: This type of file is required if your network uses
VMware NSX (Network Virtualization and Security Platform). This file is generated
using an open-source tool provided by AWS called [Import/Export for
NSX](https://github.com/awslabs/import-export-for-nsx/ "https://github.com/awslabs/import-export-for-nsx/"). It exports all software-defined network (SDN) resources in JSON
format.

[Export for
vCenter](https://github.com/awslabs/export-for-vcenter "https://github.com/awslabs/export-for-vcenter") file: You may prefer this type of file if your administrative workstation does not run Windows, RVTools is not approved in your
organization, or you want more granular control over the export file's
contents.

After you upload a data file, set up collectors, or do both, choose
**Continue**. The next step is to review discovery
data.

###### To review discovery data

1. In the **Job Plan** pane, choose **Review source
   data for discovery**.
2. If AWS Transform states that more data is needed, choose **Set up
   collectors**, and follow the instructions for setting ups
   collectors.
3. After you set up collectors, we recommend that you let them collect data
   for at least one week. When you are satisfied with the collected data, choose **Continue
   with existing data**, and then choose **Generate
   waves**.
