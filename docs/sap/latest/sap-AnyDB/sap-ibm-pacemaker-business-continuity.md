

# Business Continuity
<a name="sap-ibm-pacemaker-business-continuity"></a>

We recommend that you architect your business-critical applications to be fault tolerant. Depending on your availability requirements, there are different ways to achieve this. In this section we will discuss how you can set up highly available IBM Db2 for SAP applications.

## High Availability
<a name="sap-ibm-pacemaker-high-availability"></a>

High availability for IBM Db2 database on AWS can be configured with [IBM HADR](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.1.0/com.ibm.db2.luw.admin.ha.doc/doc/c0011267.html) with [Pacemaker](https://wiki.clusterlabs.org/wiki/Pacemaker):

One of the requirements for automated failover with IBM Db2 HADR on AWS is Pacemaker. Implementing a Pacemaker cluster in AWS is similar to deploying it in an on-premises setting. On AWS, you need to deploy the cluster nodes in separate subnets, and we recommend that you have these subnets in different AZs.

Figure 2 provides an overview of architecture for IBM Db2 HADR with Pacemaker on AWS. This includes the following components:
+ A VPC configured with two private subnets across two AZs. This provides the network infrastructure for your IBM Db2 deployment.
+ In private subnet, Linux servers are configured with Pacemaker to protect the IBM Db2 database.
+ Overlay IP address (similar to a virtual IP address) that is relocatable between the primary and standby Db2 databases.

![IBM Db2 HADR with Pacemaker](http://docs.aws.amazon.com/sap/latest/sap-AnyDB/images/sap-ibm-pacemaker4.png)


 *Figure 2 - IBM Db2 HADR with Pacemaker* 