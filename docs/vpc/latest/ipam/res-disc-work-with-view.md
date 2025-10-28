# View resource discovery details

Viewing the details of a resource discovery in AWS IPAM can provide valuable insights, such as:

- Identifying the specific AWS resources that have been imported and their associated IP address allocations.
- Monitoring the status and progress of the resource discovery process.
- Troubleshooting any issues or discrepancies between IPAM and the discovered resources.
- Analyzing the IP address utilization and trends.
  This information can help you optimize your IP address management and ensure alignment between IPAM and your actual resource deployments.

AWS Management Console

###### To view resource discovery details

1.  Open the IPAM console at
    [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2.  In the navigation pane, choose **Resource discoveries**.
3.  Choose a resource discovery.
4.  Under **Resource discovery details**, view details related to the resource discovery, such as Default, which indicates whether the resource discovery is the default. The default resource discovery is the resource discovery automatically created when you create an IPAM.
5.  In the tabs, view the details of a resource discovery:
    - **Discovered resources** - Resources monitored under a resource
      discovery. IPAM monitors CIDRs from the following resource
      types VPCs, Public IPv4 pools, VPC subnets, and Elastic IP
      addresses.
      - **Name (Resource ID)** – Resource discovery ID.
      - **IPs allocated** – The percentage of IP address space in use. To convert the
        decimal to a percentage, multiply the decimal by
      100. Note the following:


          - For resources that are VPCs, this is the percentage of IP address space in the VPC that's taken up by subnet CIDRs.
          - For resources that are subnets, if the subnet has an IPv4 CIDR provisioned to it, this is the percentage of IPv4 address space in the subnet that's in use. If the subnet has an IPv6 CIDR provisioned to it, the percentage of IPv6 address space in use is not represented. The percentage of IPv6 address space in use cannot currently be calculated.
          - For resources that are public IPv4 pools, this is the percentage of IP address space in the
           pool that's been allocated to Elastic IP addresses
           (EIPs).

      - **CIDR** – Resource CIDR.
      - **Region** – Resource Region.
      - **Owner ID** – Resource owner ID.
      - **Sample time** – The last successful resource discovery
        time.

    - **Discovered accounts**: AWS accounts being monitored under a resource discovery. If you have integrated IPAM with AWS Organizations, all accounts in the organization are discovered accounts.
      - **Account ID** – The account ID.
      - **Region** – The AWS Region that the account information is
        returned from.
      - **Last attempted discovery time** – The last attempted resource
        discovery time.
      - **Last successful discovery time** – The last successful resource
        discovery time.
      - **Status** – Resource discovery failure reason.

    - **Operating regions** – The operating Regions for the resource
      discovery.
    - **Resource sharing** – If the resource discovery has been shared,
      the resource share ARN is listed.
      - **Resource share ARN** – Resource share ARN.
      - **Status** – The current status of the resource share. Possible
        values are:
        - **Active** – Resource share is active and available for
          use.
        - **Deleted** – Resource share is deleted and is no longer
          available for use.
        - **Pending** – An invitation to accept the resource share is
          waiting for a response.

      - **Created at** – When the resource share was created.

    - **Tags** – A tag is a label that you assign to an AWS resource.
      Each tag consists of a key and an optional value. You can
      use tags to search and filter your resources or track your
      AWS costs.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

- View resource discovery details: [describe-ipam-resource-discoveries](../../../cli/latest/reference/ec2/describe-ipam-resource-discoveries.md "../../../cli/latest/reference/ec2/describe-ipam-resource-discoveries.md")
