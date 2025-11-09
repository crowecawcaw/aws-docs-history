# Getting started with Oracle Database@AWS

To begin using Oracle Database@AWS, you can create the following resources using the Oracle Database@AWS console,
CLI, or APIs:

1. ODB network
2. Oracle Exadata infrastructure
3. Exadata VM cluster or Autonomous VM cluster
4. ODB peering connection
   To create Oracle Exadata databases on your infrastructure, you must use the Oracle Cloud Infrastructure (OCI)
   console or APIs rather than the Oracle Database@AWS dashboard. Thus, you deploy resources in two cloud
   environments: network and infrastructure resources are in AWS, while the database administration
   control plane is in OCI. For more information, see [Oracle Database@AWS](https://docs.oracle.com/en-us/iaas/Content/database-at-aws/oaaws.htm "https://docs.oracle.com/en-us/iaas/Content/database-at-aws/oaaws.htm") in
   the Oracle Cloud Infrastructure documentation.

## Prerequisites for setting up Oracle Database@AWS

Before configuring your Oracle Exadata infrastructure, make sure that you do the following:

- Perform the steps in [Onboarding to Oracle Database@AWS](setting-up.md "setting-up.md"). You must
  have accepted a private offer to use Oracle Database@AWS.
- Grant your IAM principal the policy permissions listed in [Allow users
  to provision Oracle Database@AWS resources](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-full-access "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-full-access"). These permissions are
  necessary to use Oracle Database@AWS.

## Supported OCI services on Oracle Database@AWS

Oracle Database@AWS supports the following Oracle Cloud Infrastructure (OCI) services:

- Oracle Exadata Database Service on Dedicated Infrastructure – Provides a fully
  managed, dedicated Exadata environment accessible within AWS. For more information, see
  [Oracle Cloud Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/index.html "https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/index.html") in the OCI
  documentation.
- Autonomous Database on Dedicated Exadata Infrastructure – Provides a highly
  automated, fully managed database environment running in OCI with committed hardware and
  software resources. For more information, see [About Autonomous Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html "https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html") in the OCI
  documentation.

## Supported Regions for Oracle Database@AWS

You can use Oracle Database@AWS in the following AWS Regions:

**US East (N. Virginia)**

You can use the AZs with the physical IDs `use1-az4` and `use1-az6`.

**US West (Oregon)**

You can use the AZs with the physical IDs `usw2-az3` and
`usw2-az4`.

To find the logical AZ names in your account that map to the preceding physical AZ IDs, run
the following command.

```
aws ec2 describe-availability-zones \
  --region us-east-1 \
  --query "AvailabilityZones[*].{ZoneName:ZoneName, ZoneId:ZoneId}" \
  --output table
```

## Planning IP address space in Oracle Database@AWS

Plan carefully for IP address space in Oracle Database@AWS. Consider the IP address consumption based
on the number of VM clusters, including the number of VMs per cluster that you can provision into the
ODB network. For more information, see [ODB Network Design](https://docs.oracle.com/en-us/iaas/Content/database-at-aws/oaaws-network-odb-network.htm "https://docs.oracle.com/en-us/iaas/Content/database-at-aws/oaaws-network-odb-network.htm") in the Oracle Cloud Infrastructure cocumentation.

###### Topics

- [Restrictions for IP addresses in the
  ODB network](#getting-started-ip-restrict "#getting-started-ip-restrict")
- [Client subnet CIDR requirements for the
  ODB network](#getting-started-client-cidr "#getting-started-client-cidr")
- [Backup subnet CIDR requirements for the
  ODB network](#getting-started-backup-cidr "#getting-started-backup-cidr")
- [IP consumption scenarios for the ODB network](#getting-started-scenarios "#getting-started-scenarios")

### Restrictions for IP addresses in the

ODB network

Note the following restrictions regarding CIDR ranges in the ODB network:

- You can't modify the client or backup subnet CIDR range for the ODB network after you create
  it.
- You can't use the VPC CIDR ranges in the **Restricted associations**
  column in the table in [IPv4 CIDR block association restrictions](../../../vpc/latest/userguide/vpc-cidr-blocks.md#add-cidr-block-restrictions "../../../vpc/latest/userguide/vpc-cidr-blocks.md#add-cidr-block-restrictions").
- For Exadata X9M, IP addresses 100.106.0.0/16 and 100.107.0.0/16 are reserved for the
  cluster interconnect by OCI automation, so you can't do the following:
  - Assign these ranges to the client or backup CIDR range of the ODB network.
  - Use these ranges for a VPC CIDR that is used to connect to the ODB network.

- The following CIDR ranges are reserved for Oracle Cloud Infrastructure and can't be used for the
  ODB network:
  - Oracle Cloud reserved range CIDR 169.254.0.0/16
  - Reserved Class D 224.0.0.0 — 239.255.255.255
  - Reserved Class E 240.0.0.0 — 255.255.255.255

- You can't overlap the IP address CIDR ranges for the client and backup subnets.
- You can't overlap the IP address CIDR ranges allocated for the client and backup subnets
  with the VPC CIDR ranges used to connect to the ODB network.
- You can't provision VMs in a VM cluster into different ODB networks. The network is a property of
  the VM cluster, which means you can only provision the VMs in the VM cluster into the same
  ODB network.

### Client subnet CIDR requirements for the

ODB network

In the following table, you can find the number of IP addresses consumed by the service and
infrastructure for the client subnet CIDR. The minimum CIDR size for the client subnet is /27,
and the maximum size is /16.

| Number of IP addresses | Consumed by         | Notes                                                                                                                                                                                                                                                                             |
| ---------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 6                      | Oracle Database@AWS | These IP addresses are reserved regardless of how many VM clusters you provision in the<br>ODB network. Oracle Database@AWS consumes the following:<br>• 3 IP addresses reserved for the ODB network resources in AWS<br>• 3 IP addresses reserved for the OCI networking service |
| 3                      | Each VM cluster     | These IP addresses are reserved for Single Client Access Names (SCANs) regardless of<br>how many VMs are present in each VM cluster.                                                                                                                                              |
| 4                      | Each VM             | These IP addresses depend solely on the number of VMs in the infrastructure.                                                                                                                                                                                                      |

### Backup subnet CIDR requirements for the

ODB network

In the following table, you can find the number of IP addresses consumed by the service and
infrastructure for the backup subnet CIDR. The minimum CIDR size for the backup subnet is /28,
and the maximum size is /16.

| Number of IP addresses | Consumed by         | Notes                                                                                                                                                                                                                                                     |
| ---------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3                      | Oracle Database@AWS | These IP addresses are reserved regardless of how many VM clusters you provision in the<br>ODB network. Oracle Database@AWS consumes the following:<br>• 2 IP addresses at the beginning of the CIDR range<br>• 1 IP address at the end of the CIDR range |
| 3                      | Each VM             | These IP addresses depend solely on the number of VMs in the infrastructure.                                                                                                                                                                              |

### IP consumption scenarios for the ODB network

In the following table, you can see the IP addresses consumed in the ODB network for different
configurations of VM clusters. Whereas /28 is the technical minimum CIDR range for the client subnet
CIDR to deploy 1 VM cluster with 2 VMs, we recommend that you use at least a /27 CIDR range. In this
case, the IP range isn't fully consumed by the VM clusters and permits allocation of additional IP
addresses.

| Configuration           | Client IPs consumed               | Client IPs minimum  | Backup IPs consumed   | Backup IPs minimum  |
| ----------------------- | --------------------------------- | ------------------- | --------------------- | ------------------- |
| 1 VM cluster with 2 VMs | 17 (6 service + 3 cluster + 4\*2) | 32 (/27 CIDR range) | 9 (3 service + 3\*2)  | 16 (/28 CIDR range) |
| 1 VM cluster with 3 VMs | 21 (6 service + 3 cluster + 4\*3) | 32 (/27 CIDR range) | 12 (3 service + 3\*3) | 16 (/28 CIDR range) |
| 1 VM cluster with 4 VMs | 25 (6 service + 3 cluster + 4\*4) | 32 (/27 CIDR range) | 15 (3 service + 3\*4) | 16 (/28 CIDR range) |
| 1 VM cluster with 8 VMs | 41 (6 service + 3 cluster + 4\*8) | 64 (/26 CIDR range) | 27 (3 service + 3\*8) | 32 (/27 CIDR range) |

The following table shows how many instances of each configuration are possible given a
specific client CIDR range. For example, 1 VM cluster with 4 VMs consumes 24 IP addresses in the
client subnet. If the CIDR range is /25, 128 IP addresses are available. Thus, you can provision
5 VM clusters in the subnet.

| VM cluster configuration               | Number with /27 (32 IPs) | Number with /26 (64 IPs) | Number with /25 (128 IPs) | Number with /24 (256 IPs) | Number when /23 (512 IPs) | Number when /22 (1024 IPs) |
| -------------------------------------- | ------------------------ | ------------------------ | ------------------------- | ------------------------- | ------------------------- | -------------------------- |
| 1 VM cluster with 2 VMs (16 IPs)       | 1                        | 3                        | 7                         | 15                        | 30                        | 60                         |
| 1 VM cluster with 3 VMs (20 IPs)       | 1                        | 3                        | 6                         | 12                        | 24                        | 48                         |
| 1 VM cluster with 4 VMs (24 IPs)       | 1                        | 2                        | 5                         | 10                        | 20                        | 40                         |
| 2 VM clusters with 2 VMs each (27 IPs) | 1                        | 2                        | 4                         | 9                         | 18                        | 36                         |
| 2 VM clusters with 3 VMs each (35 IPs) | 0                        | 1                        | 3                         | 7                         | 14                        | 28                         |
| 2 VM clusters with 4 VMs each (43 IPs) | 0                        | 1                        | 2                         | 5                         | 11                        | 23                         |

## Step 1: Create an ODB network in Oracle Database@AWS

An ODB network is a private isolated network that hosts OCI infrastructure in an Availability
Zone (AZ). An ODB network and an Oracle Exadata infrastructure are preconditions for provisioning VM clusters and creating
Exadata databases. You can create the ODB network and Oracle Exadata infrastructure in either order. For more information,
see [ODB network](how-it-works.md#how-it-works.odb-network "how-it-works.md#how-it-works.odb-network") and [ODB peering](how-it-works.md#how-it-works.peering "how-it-works.md#how-it-works.peering").

This task assumes that you have read [Planning IP address space in Oracle Database@AWS](#getting-started-ip "#getting-started-ip"). To modify or delete the ODB network later, see [Managing Oracle Database@AWS](managing.md "managing.md").

###### To create an ODB network

1. Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. Choose your AWS Region in the upper right. For more information, see [Supported Regions for Oracle Database@AWS](#supported-odb-regions "#supported-odb-regions").
3. From the left pane, choose **ODB networks**.
4. Choose **Create ODB network**.
5. For **ODB network name**, enter a network name. The name must be
   1–255 characters and begin with an alphabetic character or underscore. It can't contain
   consecutive hyphens.
6. For **Availability Zone**, choose an AZ name. For supported AZs, see
   [Supported Regions for Oracle Database@AWS](#supported-odb-regions "#supported-odb-regions").
7. For **Client subnet CIDR**, specify a CIDR range for the client
   connections. For more information, see [Client subnet CIDR requirements for the
   ODB network](#getting-started-client-cidr "#getting-started-client-cidr").
8. For **Backup subnet CIDR**, specify a CIDR range for the backup
   connections. To isolate the backup traffic and improve resiliency, we recommend that you don't
   overlap the backup CIDR and the client CIDR. For more information, see [Backup subnet CIDR requirements for the
   ODB network](#getting-started-backup-cidr "#getting-started-backup-cidr").
9. For **DNS configuration**, choose either of the following options:

**Default**

For **Domain name prefix**, enter a name to use as a prefix to your
domain. The domain name is fixed as **oraclevcn.com**. For example, if you
enter `myhost`, the fully qualified domain name is
**myhost.oraclevcn.com**.

**Custom domain name**

For **Domain name**, enter a complete domain name. For example, you
might enter **myhost.myodb.com**. 10. (Optional) For **Service integrations**, select a service to integrate
with your network using VPC Lattice. Oracle Database@AWS integrates with various AWS services to provide
enhanced functionality and connectivity options for your Oracle databases. Select either of the
following integrations:

**Amazon S3**

Enable direct ODB network access to Amazon S3. Your databases can access S3 for data import/export
or custom backups. You can enter a JSON policy. For more information, see .

**Zero-ETL**

Enable real-time analytics and machine learning on transactional data using
Amazon Redshift.

###### Note

When you create your ODB network, Oracle Database@AWS automatically preconfigures network access for Oracle
managed backups to Amazon S3. You can't enable or disable this integration. For more information,
see [AWS service integrations](how-it-works.md#service-integrations-overview "how-it-works.md#service-integrations-overview"). 11. (Optional) For **Tags**, enter up to 50 tags for the network. A tag is a
key-value pair that you can use to organize and track your resources. 12. Choose **Create ODB network**.

After you have created an ODB network, you can peer it to a VPC. _ODB peering_ is a user-created network connection that enables
traffic to be routed privately between an Amazon VPC and an ODB network. After peering, an Amazon EC2 instance within the VPC can
communicate with resources in the ODB network as if they were within the same network. For more
information, see [Configuring ODB peering to an Amazon VPC in Oracle Database@AWS](configuring.md "configuring.md").

## Step 2: Create an Oracle Exadata infrastructure in Oracle Database@AWS

The Oracle Exadata infrastructure is the underlying architecture of database servers, storage servers, and
networking that run Oracle Exadata databases. Choose either Exadata X9M or X11M as the system model.
You can then create VM clusters on Exadata infrastructure using the AWS console.

You can create the Oracle Exadata infrastructure and the ODB network in either order. You don't need to specify
networking information when you create the infrastructure.

You can't modify an Oracle Exadata infrastructure after you create it. To delete an Exadata infrastructure, see [Deleting an Oracle Exadata infrastructure in Oracle Database@AWS](managing.md#deleting_infra "managing.md#deleting_infra").

###### To create an Exadata infrastructure

1. Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. From the left pane, choose **Exadata infrastructures**.
3. Choose **Create Exadata infrastructure**.
4. For **Exadata infrastructure name**, enter a name. The name must be 1–255
   characters and begin with an alphabetic character or underscore. It can't contain consecutive
   hyphens.
5. For **Availability Zone**, choose one of the supported AZs. Then choose
   **Next**.
6. For **Exadata system model**, choose either
   **Exadata.X9M** or **Exadata.X11M**. For
   **Exadata.X11M**, also choose the following server types:
   - For **Database server type**, choose the database server model type of
     your Exadata infrastructure. Currently, the only choice is **X11M**.
   - For **Storage server type**, choose the storage server model type of
     your Exadata infrastructure. Currently, the only choice is
     **X11M-HC**.

7. For **Database servers**, leave the default of 2 or move the slider to
   choose up to 32 servers. To specify more than 2, request a limit increase from OCI.

Each Exadata X9M database server supports 126 OCPUs. Each Exadata X11M database server
supports 760 ECPUs. The total compute count changes as you change the number of servers. For
more information about OCPUs and ECPUs, see [Compute Models in Autonomous Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-compute-models.html#GUID-7F4EE72A-ABE7-4FC9-B4BE-86802D9AD05A "https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-compute-models.html#GUID-7F4EE72A-ABE7-4FC9-B4BE-86802D9AD05A") in the Oracle documentation. 8. For **Storage servers**, leave the default of 3 or move the slider to
choose up to 64 servers. To specify more than 3, request a limit increase from OCI. Each X9M storage server provides 64 TB.
Each X11m storage server provides 80 TB. The total TB of storage changes as you change the number of
servers. Then choose **Next**. 9. For **Maintenance window**, configure when system maintenance can occur:

    1. For **Scheduling preference**, select one of the following options:




    	* **Oracle-managed schedule** - Oracle determines the optimal time for maintenance activities.
    	* **Customer-managed schedule** - You specify when maintenance activities can occur.
    2. For **Patching mode**, select one of the following options:




    	* **Rolling** - Updates are applied to one node at a time, allowing the database to remain available during patching.
    	* **Non-rolling** - Updates are applied to all nodes simultaneously, which may require downtime.
    3. If you selected **Customer-managed schedule**, configure the following additional settings:




    	* For **Maintenance months**, select the months when maintenance can be performed.
    	* For **Week of the month**, select which week of the month maintenance can be performed (First, Second, Third, Fourth, or Last).
    	* For **Day of week**, select the day when maintenance can be performed (Monday through Sunday).
    	* For **Start hour**, select the hour when the maintenance window begins. The time is in UTC.
    	* For **Notification lead time**, select how many days in advance you want to be notified about upcoming maintenance.###### Note

Oracle Cloud Infrastructure performs system maintenance during this window. During maintenance, your Exadata infrastructure remains available, but you might experience brief periods of higher latency. 10. (Optional) For **OCI maintenance notification contacts**, enter up to
10 email addresses. AWS forwards these email addresses to OCI. When updates occur, OCI
mails notifications to the listed addresses. 11. (Optional) For **Tags**, enter up to 50 tags for the infrastructure. A
tag is a key-value pair that you can use to organize and track your resources. 12. Choose **Next** and review your infrastructure settings. 13. Choose **Create Exadata infrastructure**.

## Step 3: Create an Exadata VM cluster or Autonomous VM cluster in Oracle Database@AWS

An Exadata VM cluster is a set of VMs on which you can create Oracle Exadata databases. You create the VM clusters
on Exadata infrastructure. You can deploy multiple VM clusters with different Oracle Exadata infrastructures in the same ODB network. You have
full administrative control over the databases that you create on Exadata VM clusters.

An Autonomous VM cluster is a preallocated pool of Oracle Exadata compute and storage resources,
virtualized at the VM level, that runs Autonomous Databases (ADB). Unlike user-managed databases
that you create on an Exadata VM cluster, an Autonomous database is self-tuning, self-patching, and managed
by Oracle rather than a database administrator.

Consider the following limitations when you create VM clusters:

- You can deploy a VM cluster only into the AZ where you created your ODB network and Oracle Exadata infrastructure.
- If you don't share a VM cluster across accounts, it must be in the same AWS account as the
  Oracle Exadata infrastructure. If you use AWS RAM to share an ODB network and Oracle Exadata infrastructure from one AWS account with a trusted
  account, the trusted account can create VM clusters in its own account.
- You can deploy only VM clusters in your ODB network. No other resources are permitted.
- You can't change the storage allocation after you create a VM cluster.

###### Important

The creation process can take over 6 hours, depending on the size of the VM cluster.

Exadata VM cluster

###### To create an Exadata VM cluster

1.  Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2.  From the left pane, choose **Exadata VM clusters**.
3.  Choose **Create VM cluster**.
4.  For **VM cluster name**, enter a name. The name must be 1–255
    characters and begin with an alphabetic character or underscore. It can't contain consecutive
    hyphens.
5.  (Optional) For **Grid Infrastructure cluster name**, enter a Grid
    infrastructure version for your VM cluster that matches the Oracle Database version you are using.
    The name must be 1–11 characters and can't contain hyphens.
6.  For **Time zone**, enter a time zone.
7.  For **License options**, choose **Bring Your Own License
    (BYOL)** or **License Included**, and then choose
    **Next**. This license is the OCI license provided by Oracle, not a license
    provided by AWS.
8.  Configure Exadata infrastructure settings as follows:
    1.  For **Infrastructure**, choose the following:
        - For **Exadata infrastructure name**, choose the infrastructure to use
          for this VM cluster.
        - For **Grid Infrastructure version**, choose the version to use for
          this VM cluster.
        - For **Exadata image version**, choose the version to use for this
          VM cluster. We recommend that you choose the version shown, which is the highest version
          available.

    2.  For **Database servers**, select one or more database servers to host
        your VM cluster.
    3.  For **Configuration**, do the following:
        - Choose the **CPU core count**, **Memory**, and
          **Local storage** for each VM, or accept the defaults.
        - Choose the total amount of **Exadata storage** for the VM cluster, or
          accept the default.

    4.  (Optional) For **Storage allocation**, select any of the following
        options:

            * **Enable storage allocation for Exadata sparse snapshots**
            * **Enable storage allocation for local backups**

        The usable storage allocation changes as you select options. You can't change this
        storage allocation later. Review your selection, and then choose
        **Next**.

9.  Configure connectivity as follows:
    1. For **ODB network**, choose an existing ODB network.
    2. For **Host name prefix**, enter a prefix for the VM cluster. Make sure not
       to include the domain name. The prefix forms the first portion of the Oracle Exadata VM cluster host
       name.

    ###### Note

    The **Host domain name** is fixed as
    **oraclevcn.com**. 3. For **SCAN listener port (TCP/IP)**, enter a port number that for TCP
    access to the single client access name (SCAN) listener. The default port is
    **1521**. Or you can enter a custom SCAN port in the range
    **1024–8999**, excluding the following port numbers:
    **2484**, **6100**, **6200**,
    **7060**, **7070**, **7085**, and
    **7879**. Then choose **Next**. 4. For **SSH key pairs**, enter the public key portion of one or more key
    pairs used for SSH access to the VM cluster. Then choose **Next**.

10. (Optional) Choose diagnostics and tags as follows:
    1. Choose whether to enable diagnostic collection for **Diagnostic
       events**, **Health monitor**, and **Incident logs and
       trace collections**. Oracle can use this diagnostic information to identify, track,
       and resolve issues.
    2. For **Tags**, enter up to 50 tags for the VM cluster. A tag is a key-value
       pair that you can use to organize and track your resources. Then choose
       **Next**.

11. Review your settings. Then choose **Create VM cluster**.

Autonomous VM cluster

###### To create an Autonomous VM cluster

1. Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. From the left pane, choose **Autonomous VM clusters**.
3. Choose **Create Autonomous VM cluster**.
4. For **VM cluster name**, enter a name. The name must be 1–255
   characters and begin with an alphabetic character or underscore. It can't contain consecutive
   hyphens.
5. For **Time zone**, enter a time zone.
6. For **License options**, choose **Bring Your Own License
   (BYOL)** or **License Included**, and then choose
   **Next**. This license is the OCI license provided by Oracle, not a
   license provided by AWS.
7. Configure Exadata infrastructure settings as follows:
   1. For **Exadata infrastructure name**, choose the infrastructure to use
      for this Autonomous VM cluster.
   2. For **Database servers**, select one or more database servers to host
      your Autonomous VM cluster.
   3. For **Configuration**, do the following:
      - Choose the **ECPU core count per VM**, **Database memory
        per CPU**, **Database storage**, and **Maximum number
        of Autonomous Container Database** or accept the defaults.
      - Choose the total amount of **Exadata storage** for the Autonomous
        VM cluster, or accept the default.

8. Configure connectivity as follows:
   1. For **ODB network**, choose an existing ODB network.
   2. For **SCAN listener port (TCP/IP)**, enter a port number for Port
      (non-TLS). The default port is **1521**. Or you can enter a Port(TLS) in
      the range **1024–8999**, excluding the following port numbers:
      **2484**, **6100**, **6200**,
      **7060**, **7070**, **7085**, and
      **7879**. Then choose **Next**.

   Select **Enable mutual TLS (mTLS) authentication** to allow mutual
   TLS authentication.

9. (Optional) Choose diagnostics and tags as follows:
   1. Choose whether to schedule modification configuration to **Oracle-managed
      schedule** or **Customer-managed schedule**. If you choose
      **Customer-managed schedule**, set the **Maintenance
      months**, **Weeks of the month**, **Day of the
      week**, and **Start hour (UTC)**.
   2. For **Tags**, enter up to 50 tags for the Autonomous VM cluster. A
      tag is a key-value pair that you can use to organize and track your resources. Then choose
      **Next**.

10. Review your settings. Then choose **Create Autonomous VM cluster**.

## Step 4: Create Oracle Exadata databases in Oracle Cloud Infrastructure

In Oracle Database@AWS, you can create and manage the following resources using the AWS console, CLI,
or APIs:

- ODB networks
- Oracle Exadata infrastructure
- Exadata VM clusters and Autonomous VM clusters
- ODB peering connections

To create and manage Oracle Exadata databases on the infrastructure that you created, you must use
the Oracle Cloud Infrastructure console rather than the Oracle Database@AWS dashboard. You can create a user-managed Exadata
database on an Exadata VM cluster and an Autonomous Database on an Autonomous Exadata VM cluster. For information about
creating Oracle databases in OCI, see [Exadata Database](https://docs.oracle.com/en-us/iaas/Content/database-at-aws-exadata-awscr/awscr-create-exadata-database.html "https://docs.oracle.com/en-us/iaas/Content/database-at-aws-exadata-awscr/awscr-create-exadata-database.html") in the Oracle Cloud Infrastructure documentation.

###### To create Oracle Exadata databases

1. Sign in to the AWS Management Console and open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. From the left pane, choose **Exadata VM clusters** or **Autonomous
   VM clusters**.
3. Choose a VM cluster to see the details page.
4. Choose **Manage in OCI** to be redirected to the Oracle Cloud Infrastructure
   console.
5. Create your user-managed Exadata database or Autonomous Database in OCI.
