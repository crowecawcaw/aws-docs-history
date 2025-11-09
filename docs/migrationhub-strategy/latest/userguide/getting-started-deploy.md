AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Step 2: Deploy the Strategy Recommendations collector

This section describes how to deploy the Strategy Recommendations application data collector. An
application data collector is an agentless data collector that identifies running
applications on your servers, performs source code analysis, and analyzes your
databases.

###### Note

The Strategy Recommendations for On-prem customers is in KTLO mode. Existing customers can continue to use it.

There are two ways to deploy the collector:

- Deploy as a virtual machine (VM) in your VMware vCenter Server. For more
  information, see [Deploy the Strategy Recommendations collector in
  vCenter](#getting-started-deploy-vm "#getting-started-deploy-vm").
- If you have AWS applications that you want to assess, you can use the
  Strategy Recommendations collector Amazon Machine Image (AMI). For more information, see [Deploy the Strategy Recommendations collector in an
  Amazon EC2 instance](#getting-started-deploy-ec2 "#getting-started-deploy-ec2").

## Deploy the Strategy Recommendations collector in

vCenter

Migration Hub Strategy Recommendations application data collector is a virtual appliance that you can
install in your on-premises VMware environment. This section describes how to deploy
the collector Open Virtualization Archive (OVA) file as a virtual machine (VM) in
your VMware environment.

The following procedure describes how to deploy the Strategy Recommendations collector in your
VMware vCenter Server environment.

###### To deploy the collector in vCenter

1. Sign in to vCenter as a VMware administrator.
2. Deploy the OVA file that you downloaded in Step 1. The OVA ﬁle includes
   the collector and a CLI that can be used to access the Strategy Recommendations API.

You can also download the OVA file from the following link:

[https://application-data-collector-release.s3.us-west-2.amazonaws.com/ova/latest/AWSMHubApplicationDataCollector.ova](https://application-data-collector-release.s3.us-west-2.amazonaws.com/ova/latest/AWSMHubApplicationDataCollector.ova "https://application-data-collector-release.s3.us-west-2.amazonaws.com/ova/latest/AWSMHubApplicationDataCollector.ova")

We recommend the following specifications for the VM.

###### Strategy Recommendations collector VM specifications

- RAM – a minimum of 8 GB
- CPUs – at least 4

###### Note

To ensure that you are using the latest version of the collector with all the
new features and bug fixes, upgrade the collector after you deploy the collector
OVA file. For instructions about how to upgrade, see [Upgrading the Strategy Recommendations collector](application-data-collector.md#upgrade-collector "application-data-collector.md#upgrade-collector").

## Deploy the Strategy Recommendations collector in an

Amazon EC2 instance

If you have AWS applications that you would like to assess, you can use the
Strategy Recommendations application data collector Amazon Machine Image (AMI).

The following procedure describes how to launch an Amazon EC2 instance from the
collector AMI.

###### To deploy the collector Amazon EC2 instance

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation bar at the top of the screen, the current Region is
   displayed (for example, US East (Ohio)). Choose a Region that suits your
   needs from the Regions that Strategy Recommendations uses. For a list of these Regions, see
   [Strategy Recommendations
   endpoints](../../../general/latest/gr/migrationhubstrategy.md "../../../general/latest/gr/migrationhubstrategy.md") in the _AWS General Reference_.
3. In the navigation pane, under **Images** choose
   **AMIs**.
4. Choose **Public images** from the **Owned by
   me** dropdown.
5. Choose the search bar and select **AMI Name** from the
   menu.
6. Enter the name
   **AWSMHubApplicationDataCollector**.
7. To ensure that the AMI is from a secure source, verify that the owner of
   the account is **703163444405**.
8. To launch an instance from this AMI, select it, and then choose
   **Launch**. For more information about launching an
   instance using the console, see [Launching your instance from an AMI](../../../AWSEC2/latest/UserGuide/launching-instance.md#choose-an-instance-type-page "../../../AWSEC2/latest/UserGuide/launching-instance.md#choose-an-instance-type-page") in the
   _Amazon EC2 User Guide_.

We recommend the following specifications for the Amazon EC2 instance.

###### Strategy Recommendations collector Amazon EC2 instance specifications

    * RAM – A minimum of 8
     GB
    * CPUs – At least 4

The Strategy Recommendations AMI includes the collector and a CLI that can be used to access the
Strategy Recommendations API.

###### Note

To ensure that you are using the latest version of the collector with all the
new features and bug fixes, upgrade the collector after you deploy the Strategy Recommendations
collector as an Amazon EC2 instance. For instructions about how to upgrade, see [Upgrading the Strategy Recommendations collector](application-data-collector.md#upgrade-collector "application-data-collector.md#upgrade-collector").

## Next step

[Step 3: Sign in to the Strategy Recommendations
collector](getting-started-login-vm.md "getting-started-login-vm.md")
