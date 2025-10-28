# Creating a new VPC

Complete the following steps to create a new VPC with one public subnet and one
private subnet.

###### To create a new VPC

1.  Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2.  In the navigation pane, choose **VPC Dashboard**.
3.  Choose **Launch VPC Wizard**.
4.  In **Step 1: Select a VPC Configuration**, choose **VPC
    with Public and Private Subnets**, and then choose
    **Select**.
5.  In **Step 2: VPC with Public and Private Subnets**, configure
    the VPC as follows:
    - For **IPv4 CIDR block**, specify an IPv4 CIDR block for the
      VPC.
    - For **IPv6 CIDR block**, keep the default value,
      **No IPv6 CIDR Block**.
    - For **VPC name**, enter a unique name for the VPC.
    - Configure the public subnet as follows:
      - For **Public subnet's IPv4 CIDR**, specify the CIDR
        block for the subnet.
      - For **Availability Zone**, keep the default value,
        **No Preference**.
      - For **Public subnet name**, enter a name for the
        subnet. For example, `WorkSpaces Secure Browser Public Subnet`.

    - Configure the first private subnet as follows:
      - For **Private subnet's IPv4 CIDR**, specify the CIDR
        block for the subnet. Make a note of the value that you specify.
      - For **Availability Zone**, select a specific zone and
        make a note of the zone that you select.
      - For **Private subnet name**, enter a name for the
        subnet. For example, `WorkSpaces Secure Browser Private Subnet1`.

    - For the remaining fields, keep the default values where applicable.
    - For **Elastic IP Allocation ID**, enter the value that
      corresponds to the Elastic IP address that you created. This address is then
      assigned to the NAT gateway. If you don't have an Elastic IP address, create one
      by using the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
    - For **Service endpoints**, if an Amazon S3 endpoint is required
      for your environment, specify one.

    To specify an Amazon S3 endpoint, do the following:

        1. Choose **Add Endpoint**.
        2. For **Service**, select the
         **com.amazonaws.`Region`.s3**
         entry, where `Region` is the AWS Region you're
         creating your VPC in.
        3. For **Subnet**, choose **Private
         subnet**.
        4. For **Policy**, keep the default value, **Full
         Access**.

    - For **Enable DNS hostnames**, keep the default value,
      **Yes**.
    - For **Hardware tenancy**, keep the default value,
      **Default**.
    - Choose **Create VPC**.
    - It takes several minutes to set up your VPC. After the VPC is created,
      choose **OK**.
