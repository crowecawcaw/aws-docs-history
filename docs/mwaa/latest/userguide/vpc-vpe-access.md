# Managing access to service-specific Amazon VPC endpoints on Amazon MWAA

A VPC endpoint (AWS PrivateLink) you can use to privately connect your VPC to services hosted on AWS without requiring an internet gateway, a NAT device, VPN, or firewall proxies. These endpoints are horizontally scalable and highly available virtual devices that allow communication between instances in your VPC and AWS services. This page describes the VPC endpoints created by Amazon MWAA, and how to access the VPC endpoint for your Apache Airflow webserver if you've chosen the **Private network** access mode on Amazon Managed Workflows for Apache Airflow.

###### Contents

- [Pricing](vpc-vpe-access.md#vpc-vpe-pricing "vpc-vpe-access.md#vpc-vpe-pricing")
- [VPC endpoint overview](vpc-vpe-access.md#vpc-vpe-about "vpc-vpe-access.md#vpc-vpe-about")
  - [Public network access mode](vpc-vpe-access.md#vpc-vpe-about-public "vpc-vpe-access.md#vpc-vpe-about-public")
  - [Private network access mode](vpc-vpe-access.md#vpc-vpe-about-private "vpc-vpe-access.md#vpc-vpe-about-private")

- [Permission to use other AWS services](vpc-vpe-access.md#vpc-vpe-permission "vpc-vpe-access.md#vpc-vpe-permission")
- [Accessing VPC endpoints](vpc-vpe-access.md#vpc-vpe-view-all "vpc-vpe-access.md#vpc-vpe-view-all")
  - [Accessing VPC endpoints on the Amazon VPC console](vpc-vpe-access.md#vpc-vpe-view-endpoints "vpc-vpe-access.md#vpc-vpe-view-endpoints")
  - [Identifying the private IP addresses of your Apache Airflow webserver and its VPC endpoint](vpc-vpe-access.md#vpc-vpe-hosts "vpc-vpe-access.md#vpc-vpe-hosts")

- [Accessing the VPC endpoint for your Apache Airflow webserver (private network access)](vpc-vpe-access.md#vpc-vpe-access-endpoints "vpc-vpe-access.md#vpc-vpe-access-endpoints")
  - [Using an AWS Client VPN](vpc-vpe-access.md#vpc-vpe-access-vpn "vpc-vpe-access.md#vpc-vpe-access-vpn")
  - [Using a Linux Bastion Host](vpc-vpe-access.md#vpc-vpe-access-bastion "vpc-vpe-access.md#vpc-vpe-access-bastion")
  - [Using a Load Balancer (advanced)](vpc-vpe-access.md#vpc-vpe-access-load-balancer "vpc-vpe-access.md#vpc-vpe-access-load-balancer")

## Pricing

- [AWS PrivateLink Pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/")

## VPC endpoint overview

When you create an Amazon MWAA environment, Amazon MWAA creates between one to two VPC endpoints for your environment. These endpoints are shown as Elastic Network Interfaces (ENIs) with private IPs in your Amazon VPC. After these endpoints are created, any traffic destined to these IPs is privately or publicly routed to the corresponding AWS services used by your environment.

### Public network access mode

If you chose the **Public network** access mode for your Apache Airflow webserver, network traffic is publicly routed over the internet.

- Amazon MWAA creates a VPC interface endpoint for your Amazon Aurora PostgreSQL metadata database. The endpoint is created in the Availability Zones mapped to your private subnets and is independent from other AWS accounts.
- Amazon MWAA then binds an IP address from your private subnets to the interface endpoints. This is designed to support the best practice of binding a single IP from each Availability Zone of the Amazon VPC.

### Private network access mode

If you chose the **Private network** access mode for your Apache Airflow webserver, network traffic is privately routed _within your Amazon VPC_.

- Amazon MWAA creates a VPC interface endpoint for your Apache Airflow webserver, and an interface endpoint for your Amazon Aurora PostgreSQL metadata database. The endpoints are created in the Availability Zones mapped to your private subnets and is independent from other AWS accounts.
- Amazon MWAA then binds an IP address from your private subnets to the interface endpoints. This is designed to support the best practice of binding a single IP from each Availability Zone of the Amazon VPC.

## Permission to use other AWS services

The interface endpoints use the execution role for your environment in AWS Identity and Access Management (IAM) to manage permission to AWS resources used by your environment. As more AWS services are turned on for an environment, each service requires you to configure permission using your environment's execution role. To add permissions, refer to [Amazon MWAA execution role](mwaa-create-role.md "mwaa-create-role.md").

If you've chosen the **Private network** access mode for your Apache Airflow webserver, you must also allow permission in the VPC endpoint policy for each endpoint. To learn more, refer to [VPC endpoint policies (private routing only)](vpc-security.md#vpc-external-vpce-policies "vpc-security.md#vpc-external-vpce-policies").

## Accessing VPC endpoints

This section describes how to access the VPC endpoints created by Amazon MWAA, and how to identify the private IP addresses for your Apache Airflow VPC endpoint.

### Accessing VPC endpoints on the Amazon VPC console

The following section displays the steps to access the VPC endpoints created by Amazon MWAA, and any VPC endpoints you might have created if you're using _private routing_ for your Amazon VPC.

###### To access the VPC endpoints

1. Open the [Endpoints page](https://console.aws.amazon.com/vpc/home#Endpoints: "https://console.aws.amazon.com/vpc/home#Endpoints:") on the Amazon VPC console.
2. Select your AWS Region.
3. Refer to the VPC interface endpoints created by Amazon MWAA, and any VPC endpoints you might have created if you're using _private routing_ in your Amazon VPC.

To learn more about the VPC service endpoints that are required for an Amazon VPC with _private routing_, refer to [Creating the required VPC service endpoints in an Amazon VPC with private routing](vpc-vpe-create-access.md "vpc-vpe-create-access.md").

### Identifying the private IP addresses of your Apache Airflow webserver and its VPC endpoint

The following steps describe how to retrieve the host name of your Apache Airflow webserver and its VPC interface endpoint, and their private IP addresses.

1. Use the following AWS Command Line Interface (AWS CLI) command to retrieve the host name for your Apache Airflow webserver.

```
aws mwaa get-environment --name `YOUR_ENVIRONMENT_NAME` --query 'Environment.WebserverUrl'
```

You get something similar to the following response:

```
"99aa99aa-55aa-44a1-a91f-f4552cf4e2f5-vpce.c10.us-west-2.airflow.amazonaws.com"
```

2. Run a _dig_ command on the host name returned in the response of the previous command. For example:

```
dig CNAME +short 99aa99aa-55aa-44a1-a91f-f4552cf4e2f5-vpce.c10.us-west-2.airflow.amazonaws.com
```

You get something similar to the following response:

```
vpce-0699aa333a0a0a0-bf90xjtr.vpce-svc-00bb7c2ca2213bc37.us-west-2.vpce.amazonaws.com.
```

3. Use the following AWS Command Line Interface (AWS CLI) command to retrieve the VPC endpoint DNS name returned in the response of the previous command. For example:

```
aws ec2 describe-vpc-endpoints | grep vpce-0699aa333a0a0a0-bf90xjtr.vpce-svc-00bb7c2ca2213bc37.us-west-2.vpce.amazonaws.com.
```

You get something similar to the following response:

```
"DnsName": "vpce-066777a0a0a0-bf90xjtr.vpce-svc-00bb7c2ca2213bc37.us-west-2.vpce.amazonaws.com",
```

4. Run either an _nslookup_ or _dig_ command on your Apache Airflow host name and its VPC endpoint DNS name to retrieve the IP addresses. For example:

```
dig +short `YOUR_AIRFLOW_HOST_NAME` `YOUR_AIRFLOW_VPC_ENDPOINT_DNS`
```

You get something similar to the following response:

```
192.0.5.1
192.0.6.1
```

## Accessing the VPC endpoint for your Apache Airflow webserver (private network access)

If you've chosen the **Private network** access mode for your Apache Airflow webserver, you'll need to create a mechanism to access the VPC interface endpoint for your Apache Airflow webserver. You must use the same Amazon VPC, VPC security group, and private subnets as your Amazon MWAA environment for these resources.

### Using an AWS Client VPN

AWS Client VPN is a managed client-based VPN service that you can use to securely access your AWS resources and resources in your on-premises network. It provides a secure TLS connection from any location using the OpenVPN client.

We recommend following the Amazon MWAA tutorial to configure a Client VPN: [Tutorial: Configuring private network access using an AWS Client VPN](tutorials-private-network-vpn-client.md "tutorials-private-network-vpn-client.md").

### Using a Linux Bastion Host

A bastion host is a server whose purpose is to provide access to a private network from an external network, such as over the internet from your computer. Linux instances are in a public subnet, and they are set up with a security group that allows SSH access from the security group attached to the underlying Amazon EC2 instance running the bastion host.

We recommend following the Amazon MWAA tutorial to configure a Linux Bastion Host: [Tutorial: Configuring private network access using a Linux Bastion Host](tutorials-private-network-bastion.md "tutorials-private-network-bastion.md").

### Using a Load Balancer (advanced)

The following section displays the configurations you'll need to apply to an [Application Load Balancer](../../../elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.md "../../../elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.md").

1. **Target groups**. You'll need to use target groups that point to the private IP addresses for your Apache Airflow webserver, and its VPC interface endpoint.
   We recommend specifying both private IP addresses as your registered targets, as using only one can reduce availability. For more information about how to identify the private IP addresses,
   refer to [Identifying the private IP addresses of your Apache Airflow webserver and its VPC endpoint](#vpc-vpe-hosts "#vpc-vpe-hosts").
2. **Status codes**. We recommend using `200` and `302` status codes in your target group settings. Otherwise, the targets might be flagged as unhealthy if the VPC endpoint for the Apache Airflow webserver responds with a `302 Redirect` error.
3. **HTTPS Listener**. You'll need to specify the target port for the Apache Airflow webserver. For example:

| Protocol | Port |
| -------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTTPS    | 443  | 4. **ACM new domain**. If you want to associate an SSL/TLS certificate in AWS Certificate Manager, you'll need to create a new domain for the HTTPS listener for your load balancer. 5. **ACM certificate region**. If you want to associate an SSL/TLS certificate in AWS Certificate Manager, you'll need to upload to the same AWS Region as your environment. For example: 1. ###### Example region to upload certificate `` aws acm import-certificate --certificate fileb://Certificate.pem --certificate-chain fileb://CertificateChain.pem --private-key fileb://PrivateKey.pem `--region us-west-2` `` |
