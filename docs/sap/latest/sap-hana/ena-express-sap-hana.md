# Configure ENA Express

SAP HANA scale-out systems require a minimum of 9 Gbps of single flow network bandwidth between nodes. Amazon EC2 instances now support ENA Express, allowing a single flow bandwidth of up to 25 Gbps between instances, without requiring a cluster placement group. For more information, see [Improve network performance with ENA Express on Linux instances](../../../AWSEC2/latest/UserGuide/ena-express.md "../../../AWSEC2/latest/UserGuide/ena-express.md").

## Prerequisites

Before setting up ENA Express for SAP HANA scale-out systems or SAP NetWeaver workloads, verify the following prerequisites.

- Verify that your chosen instance type is certified for SAP HANA or supported for SAP NetWeaver.
  - For **SAP HANA scale-out workloads**, you can enable ENA Express on a certified and supported Amazon EC2 instance. For information on supported instances, see [Supported instance types for ENA Express](https://docs.aws.amazon.com-AWSEC2/latest/UserGuide/ena-express.html#ena-express-supported-instance-types "https://docs.aws.amazon.com-AWSEC2/latest/UserGuide/ena-express.html#ena-express-supported-instance-types"). For information on certified instances, see [Certified and Supported SAP HANA Hardware](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23;v:b046dad8-7aa0-457a-ade5-286ebaf88a2f;v:963a354b-c138-4c78-b95f-2bca33f1fc0a "https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23;v:b046dad8-7aa0-457a-ade5-286ebaf88a2f;v:963a354b-c138-4c78-b95f-2bca33f1fc0a"). If an Amazon EC2 instance is certified for scale-out but doesn’t support ENA Express, you can continue to use cluster placement group to obtain upto 10 Gbps of single flow network bandwidth.
  - For **SAP NetWeaver workloads**, you can use ENA Express with all of the SAP certified Amazon EC2 instances that support ENA Express. For more information, see the following resources.
    - [SAP NetWeaver supported instances](../general/sap-netweaver-aws-ec2.md "../general/sap-netweaver-aws-ec2.md")
    - [SAP Note 1656099 – SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://me.sap.com/notes/1656099/E "https://me.sap.com/notes/1656099/E")

- Ensure that you are using the minimum required operating system version with the latest kernel version.
  - RHEL for SAP 8.4 and above
  - SLES 12 SP5 for SAP or SLES 15 SP2 for SAP and above

  ###### Note

  Verify that your chosen operating system is certified for SAP HANA. For more information, see [Certified and Supported SAP HANA Hardware](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23;v:b046dad8-7aa0-457a-ade5-286ebaf88a2f;v:963a354b-c138-4c78-b95f-2bca33f1fc0a "https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23;v:b046dad8-7aa0-457a-ade5-286ebaf88a2f;v:963a354b-c138-4c78-b95f-2bca33f1fc0a").

## Configure operating system

You must configure some of the network related parameters at the operating system level to ensure that ENA Express works effectively. This includes configuring the correct maximum transmission unit (mtu) required for ENA Express, and other parameters. For more information, see [Prerequisites](../../../AWSEC2/latest/UserGuide/ena-express.md#ena-express-prereq-linux "../../../AWSEC2/latest/UserGuide/ena-express.md#ena-express-prereq-linux") for ENA Express.

You can also use the [check-ena-express-settings.sh](https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express-settings.sh "https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express-settings.sh") script to check the operating system prerequisites. You can run the script from AWS Systems Manager against multiple instances simultaneously. To run the script with Systems Manager, you must ensure that your system has AWS Systems Manager Agent installed. Use the following steps to run the script.

1. Go to [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Node Management** > **Run Command**.
3. Select **Run a command**, and search for **`AWS-RunRemoteScript`**.
4. Choose **`AWS-RunRemoteScript`**, and input the following parameters.
   - **Source Type** – GitHub
   - **Source Info** – `{ "owner": "amzn", "repository": "amzn-ec2-ena-utilities", "path": "ena-express", "getOptions": "branch: main" }`
   - **Command Line** – `check-ena-express-settings.sh eth0`

   ###### Note

   You must repeat this check for all elastic network interfaces, such as `eth1`, `eth2`, etc.

5. In **Target selection**, specify the instances against which you want to run the script.
6. Select **Run**.

Once the command has completed running, you can review the output, and take corrective actions, if required.

## ENA Express settings

After configuring your operating system, you can enable ENA Express for your target instance via AWS Management Console or AWS CLI. For more information, see [Configure ENA Express settings](../../../AWSEC2/latest/UserGuide/ena-express-configure.md "../../../AWSEC2/latest/UserGuide/ena-express-configure.md"). This setting must be repeated on all nodes in scale-out setup.

You do not need a cluster placement group to obtain minimum required single flow network throughput for SAP HANA scale-out systems after successfully enabling ENA Express. To remove a placement group, see [Working with placement groups](https://docs.aws.amazon.com-AWSEC2/latest/UserGuide/placement-groups.html#concepts-placement-groups "https://docs.aws.amazon.com-AWSEC2/latest/UserGuide/placement-groups.html#concepts-placement-groups").

## Check SAP HANA scale-out performance

After enabling ENA Express, you can use [SAP HANA Hardware and Cloud Measurement Tools](https://help.sap.com/docs/HANA_HW_CLOUD_TOOLS/02bb1e64c2ae4de7a11369f4e70a6394/7e878f6e16394f2990f126e639386333.html "https://help.sap.com/docs/HANA_HW_CLOUD_TOOLS/02bb1e64c2ae4de7a11369f4e70a6394/7e878f6e16394f2990f126e639386333.html") to check its performance. For additional details, see [Measure System Configuration and Performance - Scale-out Systems](https://help.sap.com/docs/HANA_HW_CLOUD_TOOLS/02bb1e64c2ae4de7a11369f4e70a6394/61c3401eff904a349032e450cd031a65.html "https://help.sap.com/docs/HANA_HW_CLOUD_TOOLS/02bb1e64c2ae4de7a11369f4e70a6394/61c3401eff904a349032e450cd031a65.html").
