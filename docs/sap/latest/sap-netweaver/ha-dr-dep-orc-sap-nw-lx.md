# HA/DR deployment

## Installing SAP Oracle on Amazon EC2 instances and configuring HA/DR

Create an additional Amazon EC2 instance and perform the installation in a secondary Availability Zone. The steps for creating a HA or DR instance in a secondary Availability Zone are the same as described in Standalone deployment. You can simplify this step by using the following methods.

- If you have built any automation using AWS CloudFormation or other tools to create the primary Amazon EC2 instance and install database software, you can use the same automation to build the HA instance.
- You can create an [Amazon Machine Image](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") of the primary Amazon EC2 instance and launch another instance in the secondary Availability Zone.

The configuration of high availability or disaster recovery depends on the tools you use. See the next sections for more details.

###### Note

The preceding steps are not applicable to passive DR.

## Third-party references

To configure the SAP Oracle system with HA/DR using the Oracle Data Guard, refer to the following documents.

- [Setting up Oracle 12c Data Guard for SAP](https://www.sap.com/documents/2016/12/a67bac51-9a7c-0010-82c7-eda71af511fa.html "https://www.sap.com/documents/2016/12/a67bac51-9a7c-0010-82c7-eda71af511fa.html")
- [Setting up Oracle 12c Data Guard for SAP](https://www.sap.com/documents/2016/12/a67bac51-9a7c-0010-82c7-eda71af511fa.html "https://www.sap.com/documents/2016/12/a67bac51-9a7c-0010-82c7-eda71af511fa.html")
- [Oracle Standby Databases](https://help.sap.com/viewer/a2cf03bc73a44b2a87d535cdb35e529e/7.03.29/en-US/4512fab47a447204e10000000a155369.html "https://help.sap.com/viewer/a2cf03bc73a44b2a87d535cdb35e529e/7.03.29/en-US/4512fab47a447204e10000000a155369.html")
- [Configuring Oracle Data Guard](https://docs.oracle.com/database/121/HABPT/config_dg.htm#HABPT4876 "https://docs.oracle.com/database/121/HABPT/config_dg.htm#HABPT4876")

For information about configuring HA/DR using a third-party product, see the vendor-specific documentation, such as the following.

- [SIOS Oracle High Availability](https://us.sios.com/solutions/oracle-high-availability/ "https://us.sios.com/solutions/oracle-high-availability/")
- [Veritas InfoScale™ 7.4.1 Solutions](https://www.veritas.com/content/support/en_US/doc/130803809-130803829-0/v132424202-130803829 "https://www.veritas.com/content/support/en_US/doc/130803809-130803829-0/v132424202-130803829")

###### Note

You need to configure cross-regional [Amazon VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") or [Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/") to enable SAP Oracle asynchronous replication between the two Regions.

**To perform a manual failover or switchover, see [HA/DR operations](hadrops-orc-sap-nw-lx.md "hadrops-orc-sap-nw-lx.md").**
