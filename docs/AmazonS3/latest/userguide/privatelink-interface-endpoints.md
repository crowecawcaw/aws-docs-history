

# AWS PrivateLink for Amazon S3
<a name="privatelink-interface-endpoints"></a>

With AWS PrivateLink for Amazon S3, you can provision *interface VPC endpoints* (interface endpoints) in your virtual private cloud (VPC). These endpoints are directly accessible from applications that are on premises over VPN and Direct Connect, or in a different AWS Region over VPC peering.

Interface endpoints are represented by one or more elastic network interfaces (ENIs) that are assigned private IP addresses from subnets in your VPC. Requests to Amazon S3 over interface endpoints stay on the Amazon network. You can also access interface endpoints in your VPC from on-premises applications through AWS Direct Connect or AWS Virtual Private Network (Site-to-Site VPN). For more information about how to connect your VPC with your on-premises network, see the [Direct Connect User Guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) and the [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).

For general information about interface endpoints, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) in the *AWS PrivateLink Guide*.

**Topics**
+ [Types of VPC endpoints for Amazon S3](#types-of-vpc-endpoints-for-s3)
+ [Restrictions and limitations of AWS PrivateLink for Amazon S3](#privatelink-limitations)
+ [Creating a VPC endpoint](#s3-creating-vpc)
+ [Accessing Amazon S3 interface endpoints](#accessing-s3-interface-endpoints)
+ [IP Address types for VPC endpoints](#privatelink-ip-address-types)
+ [DNS record IP types for VPC endpoints](#privatelink-dns-record-types)
+ [Private DNS](#private-dns)
+ [Accessing buckets, access points, and Amazon S3 Control API operations from S3 interface endpoints](#accessing-bucket-and-aps-from-interface-endpoints)
+ [Updating an on-premises DNS configuration](#updating-on-premises-dns-config)
+ [Creating a VPC endpoint policy for Amazon S3](#creating-vpc-endpoint-policy)

## Types of VPC endpoints for Amazon S3
<a name="types-of-vpc-endpoints-for-s3"></a>

You can use two types of VPC endpoints to access Amazon S3: *gateway endpoints* and *interface endpoints* (by using AWS PrivateLink). A *gateway endpoint* is a gateway that you specify in your route table to access Amazon S3 from your VPC over the AWS network. *Interface endpoints* extend the functionality of gateway endpoints by using private IP addresses to route requests to Amazon S3 from within your VPC, on premises, or from a VPC in another AWS Region by using VPC peering or AWS Transit Gateway. For more information, see [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) and [Transit Gateway vs VPC peering](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway-vs-vpc-peering.html).

Interface endpoints are compatible with gateway endpoints. If you have an existing gateway endpoint in the VPC, you can use both types of endpoints in the same VPC.


<table>
<thead>
  <tr><th>Gateway endpoints for Amazon S3</th><th>Interface endpoints for Amazon S3</th></tr>
</thead>
<tbody>
  <tr><td colspan="2">In both cases, your network traffic remains on the AWS network.</td></tr>
  <tr><td>Use Amazon S3 public IP addresses</td><td>Use private IP addresses from your VPC to access Amazon S3</td></tr>
  <tr><td>Use the same Amazon S3 DNS names</td><td><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html#accessing-s3-interface-endpoints">Require endpoint-specific Amazon S3 DNS names</a></td></tr>
  <tr><td>Do not allow access from on premises</td><td>Allow access from on premises</td></tr>
  <tr><td>Do not allow access from another AWS Region</td><td>Allow access from a VPC in another AWS Region by using VPC peering or AWS Transit Gateway</td></tr>
  <tr><td>Not billed</td><td>Billed</td></tr>
</tbody>
</table>


For more information, see [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html) and [interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

## Restrictions and limitations of AWS PrivateLink for Amazon S3
<a name="privatelink-limitations"></a>

VPC limitations apply to AWS PrivateLink for Amazon S3. For more information, see [Interface endpoint considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) and [AWS PrivateLink quotas](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-limits-endpoints.html) in the *AWS PrivateLink Guide*. In addition, the following restrictions apply.

Interface endpoints for Amazon S3 does not support the following:
+ [Website endpoints](WebsiteEndpoints.md)
+ [Legacy global endpoints](VirtualHosting.md#deprecated-global-endpoint)
+ [S3 dash Region endpoints ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html)
+ Using [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) or [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html) between buckets in different AWS Regions
+ Transport Layer Security (TLS) 1.0
+ Transport Layer Security (TLS) 1.1
+ Transport Layer Security (TLS) 1.3
+ Hybrid post-quantum Transport Layer Security (TLS)

## Creating a VPC endpoint
<a name="s3-creating-vpc"></a>

To create a VPC interface endpoint, see [ Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*. To create a VPC gateway endpoint, see [Create a gateway endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3) in the *AWS PrivateLink Guide*.

**FIPS endpoints for Amazon S3**  
To connect to Amazon S3 over AWS PrivateLink with FIPS 140-3 validated cryptographic modules, create an interface endpoint. Use the FIPS service name `com.amazonaws.{{region}}.s3-fips`. For example, use `com.amazonaws.us-east-1.s3-fips`. FIPS interface endpoints are available in all AWS Regions that offer [FIPS endpoints](https://aws.amazon.com/compliance/fips/) for Amazon S3. These endpoints support access to buckets, access points, and Amazon S3 Control API operations. You can configure FIPS interface endpoints to use IPv4, IPv6, or dual-stack IP addressing.

## Accessing Amazon S3 interface endpoints
<a name="accessing-s3-interface-endpoints"></a>

When you create an interface endpoint, Amazon S3 generates two types of endpoint-specific, S3 DNS names: *Regional* and *zonal*. 
+ A *Regional* DNS name includes a unique VPC endpoint ID, a service identifier, the AWS Region, and `vpce.amazonaws.com` in its name. For example, for VPC endpoint ID `{{vpce-1a2b3c4d}}`, the DNS name generated might be similar to `{{vpce-1a2b3c4d-5e6f}}.s3.us-east-1.vpce.amazonaws.com`.
+ A *Zonal* DNS name includes the Availability Zone—for example, `{{vpce-1a2b3c4d-5e6f}}-us-east-1a.s3.us-east-1.vpce.amazonaws.com`. You might use this option if your architecture isolates Availability Zones. For example, you could use it for fault containment or to reduce Regional data transfer costs.

Endpoint-specific S3 DNS names can be resolved from the S3 public DNS domain.

If you create an interface endpoint that uses the FIPS service name `com.amazonaws.{{region}}.s3-fips`, Amazon S3 generates endpoint-specific DNS names. These names include the `s3-fips` service identifier. For example, `{{vpce-1a2b3c4d-5e6f}}.s3-fips.us-east-1.vpce.amazonaws.com`.

VPC endpoints for Amazon S3 support different types of IP addressing, including: IPv4, IPv6, and Dualstack. See [IP Address types for VPC endpoints](#privatelink-ip-address-types) and [DNS record IP types for VPC endpoints](#privatelink-dns-record-types). 

## IP Address types for VPC endpoints
<a name="privatelink-ip-address-types"></a>

VPC endpoints for Amazon S3 support different types of IP addressing, including:
+ **IPv4**

  VPC endpoints can be configured to use only IPv4 addresses for connectivity.
+ **IPv6**

  VPC endpoints can be configured to use only IPv6 addresses for connectivity.
+ **Dual-stack**

  VPC endpoints can be configured in dual-stack mode, supporting both IPv4 and IPv6 addresses simultaneously. This provides flexibility to access Amazon S3 over either IPv4 or IPv6 networks.

The IP address type you choose for your VPC endpoint will depend on the networking requirements of your applications and infrastructure. Considerations may include the IP addressing schemes used in your VPC, on-premises networks, and across the internet connectivity to Amazon S3. For more information, see IP address types for [interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html#aws-service-ip-address-type) and [gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html#gateway-endpoint-ip-address-type) in the *Amazon Virtual Private Cloud* guide.

## DNS record IP types for VPC endpoints
<a name="privatelink-dns-record-types"></a>

Depending on your IP address type, when you call a VPC endpoint, the AWS service can return `A` records, `AAAA` records, or both `A` and `AAAA` records. You can customize which record types your AWS service returns by modifying the DNS record IP type. The following table shows the supported DNS record IP types and the IP address types:


| Supported IP address types | DNS record IP types | 
| --- | --- | 
| IPv4 | IPv4 | 
| IPv6 | IPv6 | 
| Dualstack | Dualstack, IPv4, IPv6, Service-defined | 

### Configuring the service-defined DNS record IP type for Amazon S3
<a name="privatelink-dns-record-types-configure"></a>

If you create a gateway endpoint for Amazon S3 and configure the DNS record IP type as service-defined and use the regional service endpoint,(such as `s3.us-east-2.amazonaws.com`), Amazon S3 returns `A` records to your clients. In contrast, if you create a gateway endpoint and are using a dual-stack service endpoint, (such as `s3.dualstack.us-east-2.amazonaws.com`) and select the DNS record IP type as `service-defined`, Amazon S3 returns both `A` and `AAAA` records to your clients.

Similarly, if you create an interface endpoint with Private DNS enabled and choose service-defined as the DNS record type, for the regional service endpoint, (such as, `s3.us-east-2.amazonaws.com`), Amazon S3 returns `A` records to your client. Whereas, for a dualstack service endpoint, (such as, `s3.dualstack.us-east-2.amazonaws.com`), Amazon S3 returns both `A` and `AAAA` records. For more information, see DNS record IP type for [interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html#aws-services-dns-record-ip-type) and [gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html#gateway-endpoint-dns-record-ip-type) in the *VPC User Guide*.

The following table shows the supported DNS record IP types for gateway and interface endpoints:


| IP address type | Supported DNS record IP types for S3 Gateway endpoints | Supported DNS record IP types for S3 Interface endpoints  | 
| --- | --- | --- | 
| IPv4 | IPv4, service-defined\* | IPv4 | 
| IPv6 | IPv6, service-defined\* | IPv6 | 
| Dualstack | IPv4, IPv6, Dualstack, service-defined\* | Dualstack\*, IPv4, IPv6, service-defined | 

\* Represents the default DNS record IP type.

To enable IPv6 connectivity on an existing S3 gateway or interface endpoint, update the IP address type for the endpoint to **Dualstack**. When updated, Amazon S3 automatically updates the routing tables with IPv6 addresses for gateway endpoints. Then you can use the dualstack service endpoint, such as `s3.dualstack.us-east-2.amazonaws.com`, and Amazon S3 will return both `A` and `AAAA` records for dualstack S3 DNS queries. If you want to use IPV6 with the regional service endpoint, such as `s3.us-east-2.amazonaws.com`, modify the IP address type for the endpoint to **Dualstack**; and the DNS record IP type to **Dualstack**. Then Amazon S3 will return both `A` and `AAAA` records for the regional S3 DNS queries.

**Considerations**  
If your gateway endpoint has the default configuration of IP address type as `IPv4` and DNS record IP type as `service-defined`, then the dualstack service endpoint (such as `s3.dualstack.us-east-2.amazonaws.com`), traffic that uses `AAAA` records won't be routed through the gateway endpoint. Instead, this traffic will be dropped or routed over an IPv6-compatible path if one is present. For example, if your virtual private cloud (VPC) has an internet gateway, your IPv6 traffic will be routed over the internet gateway in your VPC in this scenario. If you want to ensure your traffic is always routed over a VPC endpoint, you can use an Amazon S3 bucket policy that restricts access to a specific bucket if a specified VPC endpoint is not used. For more information, see [Restricting access to a specific VPC endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.html#example-bucket-policies-restrict-accesss-vpc-endpoint).
If your interface endpoint has the default configuration of IP address type, which is IPv4, and DNS record IP type as IPv4, dualstack service endpoints, such as `ass3.dualstack.us-east-2.amazonaws.com`, are not supported. Traffic that uses the `A` or `AAAA` records of the dualstack service endpoints won't be routed through the interface endpoint. Instead, this traffic will be dropped or routed over another compatible path if one is present.
Creating or modifying a gateway endpoint with a DNS record IP type other than service-defined requires both the `enableDnsSupport` and `enableDnsHostnames` VPC attributes to be set to true.

## Private DNS
<a name="private-dns"></a>

Private DNS options for VPC interface endpoints simplify routing S3 traffic over VPC endpoints and help you take advantage of the lowest-cost network path available to your application. You can use private DNS options to route Regional S3 traffic without updating your S3 clients to use the endpoint-specific DNS names of your interface endpoints, or managing DNS infrastructure. With private DNS names enabled, Regional S3 DNS queries resolve to the private IP addresses of AWS PrivateLink for the following endpoints:
+ Regional bucket endpoints (for example, `s3.us-east-1.amazonaws.com`, or `s3-fips.us-east-1.amazonaws.com` for FIPS)
+ Control endpoints (for example, `s3-control.us-east-1.amazonaws.com`, or `s3-control-fips.us-east-1.amazonaws.com` for FIPS)
+ Access point endpoints (for example, `s3-accesspoint.us-east-1.amazonaws.com`, or `s3-accesspoint-fips.us-east-1.amazonaws.com` for FIPS)

If you configure the interface endpoint with the **Dualstack** IP address type, the FIPS dual-stack endpoints also resolve to the private IP addresses of AWS PrivateLink. For example, `s3-fips.dualstack.us-east-1.amazonaws.com` resolves to a private IP address.

If you have a gateway endpoint in your VPC, you can automatically route in-VPC requests over your existing S3 gateway endpoint and on-premises requests over your interface endpoint. This approach allows you to optimize your networking costs by using gateway endpoints, which are not billed, for your in-VPC traffic. Your on-premises applications can use AWS PrivateLink with the help of the inbound Resolver endpoint. Amazon provides a DNS server, called the Route 53 Resolver, for your VPC. An inbound Resolver endpoint forwards DNS queries from the on-premises network to Route 53 Resolver.

**Important**  
To take advantage of the lowest cost network path when using **Enable private DNS only for inbound endpoints**, a gateway endpoint must be present in your VPC. The presence of a gateway endpoint helps ensure that in-VPC traffic always routes over the AWS private network when the **Enable private DNS only for inbound endpoints** option is selected. You must maintain this gateway endpoint while you have the **Enable private DNS only for inbound endpoints** option selected. If you want to delete your gateway endpoint you must first clear **Enable private DNS only for inbound endpoints**.   
If you want to update an existing interface endpoint to **Enable private DNS only for inbound endpoints**, first confirm that your VPC has an S3 gateway endpoint. For more information about gateway endpoints and managing private DNS names, see [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway.html) and [Manage DNS names](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-dns-names.html) respectively in the *AWS PrivateLink Guide*.  
When enabling **Private DNS for inbound resolver only**, the `dnsRecordIpType` of the gateway endpoint must either match that of interface endpoint or be **service defined**.

The **Enable private DNS only for inbound endpoints** option is available only for services that support gateway endpoints.

For more information about creating a VPC endpoint that uses **Enable private DNS only for inbound endpoints**, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

**Using the VPC console**

In the console you have two options: **Enable DNS name** and **Enable private DNS only for inbound endpoints**. **Enable DNS name** is an option supported by AWS PrivateLink. By using the **Enable DNS name** option, you can use Amazon’s private connectivity to Amazon S3, while making requests to the default public endpoint DNS names. When this option is enabled, customers can take advantage of the lowest cost network path available to their application.

When you enable private DNS names on an existing or new VPC interface endpoint for Amazon S3, the **Enable private DNS only for inbound endpoints** option is selected by default. If this option is selected, your applications use only interface endpoints for your on-premises traffic. This in-VPC traffic automatically uses the lower-cost gateway endpoints. Alternatively, you can clear **Enable private DNS only for inbound endpoints** to route all S3 requests over your interface endpoint.

**Using the AWS CLI**

If you don't specify a value for `PrivateDnsOnlyForInboundResolverEndpoint`, it will default to `true`. However, before your VPC applies your settings, it performs a check to make sure that you have a gateway endpoint present in the VPC. If a gateway endpoint is present in the VPC, the call succeeds. If not, you will see the following error message: 

To set PrivateDnsOnlyForInboundResolverEndpoint to true, the VPC {{vpce\_id}} must have a gateway endpoint for the service.

**For a new VPC Interface endpoint**

Use the `private-dns-enabled` and `dns-options` attributes to enable private DNS through the command line. The `PrivateDnsOnlyForInboundResolverEndpoint` option in the `dns-options` attribute must be set to `true`. Replace the `{{user input placeholders}}` with your own information.

```
aws ec2 create-vpc-endpoint \
--region {{us-east-1}} \
--service-name {{s3-service-name}} \
--vpc-id {{client-vpc-id}} \
--subnet-ids {{client-subnet-id}} \ 
--vpc-endpoint-type Interface  \
--private-dns-enabled  \
--ip-address-type {{ip-address-type}} \ 
--dns-options PrivateDnsOnlyForInboundResolverEndpoint=true \
--security-group-ids {{client-sg-id}}
```

**For an existing VPC endpoint**

If you want to use private DNS for an existing VPC endpoint, use the following example command and replace the `{{user input placeholders}}` with your own information.

```
aws ec2 modify-vpc-endpoint \
--region {{us-east-1}} \
--vpc-endpoint-id {{client-vpc-id}} \
--private-dns-enabled \
--dns-options PrivateDnsOnlyForInboundResolverEndpoint=false
```

If you want to update an existing VPC endpoint to enable private DNS only for the Inbound Resolver, use the following example and replace the sample values with your own.

```
aws ec2 modify-vpc-endpoint \
--region {{us-east-1}} \
--vpc-endpoint-id {{client-vpc-id}} \
--private-dns-enabled \
--dns-options PrivateDnsOnlyForInboundResolverEndpoint=true
```

## Accessing buckets, access points, and Amazon S3 Control API operations from S3 interface endpoints
<a name="accessing-bucket-and-aps-from-interface-endpoints"></a>

You can use the AWS CLI or AWS SDKs to access buckets, S3 access points, and Amazon S3 Control API operations through S3 interface endpoints. 

The following image shows the VPC console **Details** tab, where you can find the DNS name of a VPC endpoint. In this example, the *VPC endpoint ID (vpce-id)* is `vpce-0e25b8cdd720f900e` and the *DNS name* is `*.vpce-0e25b8cdd720f900e-argc85vg.s3.us-east-1.vpce.amazonaws.com`. 







![The Details tab in the VPC console.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/vpc-console-details-tab.png)


When using the DNS name to access a resource, replace {{\*}} with the appropriate value. The appropriate values to use in place of `*` are as follows: 
+ `bucket`
+ `accesspoint`
+ `control`

For example, to access a bucket, use a *DNS name* like this:

 `bucket.vpce-0e25b8cdd720f900e-argc85vg.s3.us-east-1.vpce.amazonaws.com`

For examples of how to use DNS names to access buckets, access points, and Amazon S3 Control API operations, see the following sections of [AWS CLI examples](#privatelink-aws-cli-examples) and [AWS SDK examples](#privatelink-aws-sdk-examples).

For more information about how to view your endpoint-specific DNS names, see [Viewing endpoint service private DNS name configuration](https://docs.aws.amazon.com/vpc/latest/privatelink/view-vpc-endpoint-service-dns-name.html) in the *VPC User Guide*.

### AWS CLI examples
<a name="privatelink-aws-cli-examples"></a>

To access S3 buckets, S3 access points, or Amazon S3 Control API operations through S3 interface endpoints in AWS CLI commands, use the `--region` and `--endpoint-url` parameters. 

**Example: Use an endpoint URL to list objects in your bucket**  
In the following example, replace the bucket name `{{my-bucket}}`, Region `{{us-east-1}}`, and the DNS name of the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` with your own information.

```
aws s3 ls s3://{{my-bucket}}/ --region {{us-east-1}} --endpoint-url https://bucket.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}
```

**Example: Use an endpoint URL to list objects from an access point**
+ **Method 1** – Using the Amazon Resource Name (ARN) of the access point with the access point endpoint

  Replace the ARN `{{us-east-1:123456789012:accesspoint/accesspointexamplename}}`, the Region `{{us-east-1}}`, and the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` with your own information.

  ```
  aws s3api list-objects-v2 --bucket arn:aws:s3:{{us-east-1:123456789012:accesspoint/accesspointexamplename}} --region {{us-east-1}} --endpoint-url https://accesspoint.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}
  ```

  If you can't run the command successfully, update your AWS CLI to the latest version and try again. For more information on the update instructions, see [ Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) in the *AWS Command Line Interface User Guide*.
+ **Method 2** – Using the alias of the access point with the regional bucket endpoint

  In the following example, replace the access point alias `{{accesspointexamplename-8tyekmigicmhun8n9kwpfur39dnw4use1a-s3alias}}`, the Region `{{us-east-1}}`, and the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` with your own information.

  ```
  aws s3api list-objects-v2 --bucket {{accesspointexamplename-8tyekmigicmhun8n9kwpfur39dnw4use1a-s3alias}} --region {{us-east-1}} --endpoint-url https://bucket.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}
  ```
+ **Method 3** – Using the alias of the access point with the access point endpoint

  First, to construct an S3 endpoint with the bucket included as part of the hostname, set the addressing style to `virtual` for `aws s3api` to use. For more information about `AWS configure`, see [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) in the *AWS Command Line Interface User Guide*. 

  ```
  aws configure set default.s3.addressing_style virtual
  ```

  Then, in the following example, replace the access point alias `{{accesspointexamplename-8tyekmigicmhun8n9kwpfur39dnw4use1a-s3alias}}`, the Region `{{us-east-1}}`, and the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` with your own information. For more information about access point alias, see [Access point aliases](access-points-naming.md#access-points-alias).

  ```
  aws s3api list-objects-v2 --bucket {{accesspointexamplename-8tyekmigicmhun8n9kwpfur39dnw4use1a-s3alias}} --region {{us-east-1}} --endpoint-url https://accesspoint.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}
  ```

**Example: Use an endpoint URL to list jobs with an S3 control API operation**  
In the following example, replace the Region `{{us-east-1}}`, the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}`, and the account ID `{{12345678}}` with your own information.

```
aws s3control --region {{us-east-1}} --endpoint-url https://control.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}} list-jobs --account-id {{12345678}}
```

### AWS SDK examples
<a name="privatelink-aws-sdk-examples"></a>

To access S3 buckets, S3 access points, or Amazon S3 Control API operations through S3 interface endpoints when using the AWS SDKs, update your SDKs to the latest version. Then configure your clients to use an endpoint URL for accessing a bucket, access point, or Amazon S3 Control API operations through S3 interface endpoints. 

------
#### [ SDK for Python (Boto3) ]

**Example: Use an endpoint URL to access an S3 bucket**  
In the following example, replace the Region `{{us-east-1}}` and VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` with your own information. 

```
s3_client = session.client(
service_name='s3',
region_name='{{us-east-1}}',
endpoint_url='https://bucket.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}'
)
```

**Example: Use an endpoint URL to access an S3 access point**  
In the following example, replace the Region `{{us-east-1}}` and VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` with your own information. 

```
ap_client = session.client(
service_name='s3',
region_name='{{us-east-1}}',
endpoint_url='https://accesspoint.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}'
)
```

**Example: Use an endpoint URL to access the Amazon S3 Control API**  
In the following example, replace the Region `{{us-east-1}}` and VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` with your own information. 

```
control_client = session.client(
service_name='s3control',
region_name='{{us-east-1}}',
endpoint_url='https://control.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}'
)
```

------
#### [ SDK for Java 1.x ]

**Example: Use an endpoint URL to access an S3 bucket**  
In the following example, replace the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` with your own information. 

```
// bucket client
final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withEndpointConfiguration(
        new AwsClientBuilder.EndpointConfiguration(
                "https://bucket.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}",
                Regions.DEFAULT_REGION.getName()
        )
).build();
List<Bucket> buckets = s3.listBuckets();
```

**Example: Use an endpoint URL to access an S3 access point**  
In the following example, replace the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` and ARN `{{us-east-1:123456789012:accesspoint/prod}}` with your own information. 

```
// accesspoint client
final AmazonS3 s3accesspoint = AmazonS3ClientBuilder.standard().withEndpointConfiguration(
        new AwsClientBuilder.EndpointConfiguration(
                "https://accesspoint.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}",
                Regions.DEFAULT_REGION.getName()
        )
).build();
ObjectListing objects = s3accesspoint.listObjects("arn:aws:s3:{{us-east-1:123456789012:accesspoint/prod}}");
```

**Example: Use an endpoint URL to access an Amazon S3 Control API operation**  
In the following example, replace the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` with your own information. 

```
// control client
final AWSS3Control s3control = AWSS3ControlClient.builder().withEndpointConfiguration(
        new AwsClientBuilder.EndpointConfiguration(
                "https://control.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}",
                Regions.DEFAULT_REGION.getName()
        )
).build();
final ListJobsResult jobs = s3control.listJobs(new ListJobsRequest());
```

------
#### [ SDK for Java 2.x ]

**Example: Use an endpoint URL to access an S3 bucket**  
In the following example, replace the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` and the Region `{{Region.US_EAST_1}}` with your own information.

```
// bucket client
Region region = {{Region.US_EAST_1}};
s3Client = S3Client.builder().region(region)
                   .endpointOverride(URI.create("https://bucket.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}"))
                   .build()
```

**Example: Use an endpoint URL to access an S3 access point**  
In the following example, replace the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` and the Region `{{Region.US_EAST_1}}` with your own information.

```
// accesspoint client
Region region = {{Region.US_EAST_1}};
s3Client = S3Client.builder().region(region)
                   .endpointOverride(URI.create("https://accesspoint.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}"))
                   .build()
```

**Example: Use an endpoint URL to access the Amazon S3 Control API**  
In the following example, replace the VPC endpoint ID `{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}` and the Region `{{Region.US_EAST_1}}` with your own information.

```
// control client
Region region = {{Region.US_EAST_1}};
s3ControlClient = S3ControlClient.builder().region(region)
                                 .endpointOverride(URI.create("https://control.{{vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com}}"))
                                 .build()
```

------

## Updating an on-premises DNS configuration
<a name="updating-on-premises-dns-config"></a>

When using endpoint-specific DNS names to access the interface endpoints for Amazon S3, you don’t have to update your on-premises DNS resolver. You can resolve the endpoint-specific DNS name with the private IP address of the interface endpoint from the public Amazon S3 DNS domain. 

### Using interface endpoints to access Amazon S3 without a gateway endpoint or an internet gateway in the VPC
<a name="using-interface-endpoints"></a>

Interface endpoints in your VPC can route both in-VPC applications and on-premises applications to Amazon S3 over the Amazon network, as illustrated in the following diagram.

![Data-flow diagram showing access to Amazon S3 using an interface endpoint and AWS PrivateLink.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/interface-endpoints.png)


The diagram illustrates the following: 
+ Your on-premises network uses Direct Connect or Site-to-Site VPN to connect to VPC A.
+ Your applications on-premises and in VPC A use endpoint-specific DNS names to access Amazon S3 through the S3 interface endpoint.
+ On-premises applications send data to the interface endpoint in the VPC through Direct Connect (or Site-to-Site VPN). AWS PrivateLink moves the data from the interface endpoint to Amazon S3 over the AWS network.
+ In-VPC applications also send traffic to the interface endpoint. AWS PrivateLink moves the data from the interface endpoint to Amazon S3 over the AWS network.

### Using gateway endpoints and interface endpoints together in the same VPC to access Amazon S3
<a name="using-gateway-and-interface-endpoints"></a>

You can create interface endpoints and retain the existing gateway endpoint in the same VPC, as the following diagram shows. By taking this approach, you allow in-VPC applications to continue accessing Amazon S3 through the gateway endpoint, which is not billed. Then, only your on-premises applications would use interface endpoints to access Amazon S3. To access Amazon S3 this way, you must update your on-premises applications to use endpoint-specific DNS names for Amazon S3.

![Data-flow diagram showing access to Amazon S3 using gateway endpoints and interface endpoints.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/interface-and-gateway-endpoints.png)


The diagram illustrates the following: 
+ On-premises applications use endpoint-specific DNS names to send data to the interface endpoint within the VPC through Direct Connect (or Site-to-Site VPN). AWS PrivateLink moves the data from the interface endpoint to Amazon S3 over the AWS network.
+ Using default Regional Amazon S3 names, in-VPC applications send data to the gateway endpoint that connects to Amazon S3 over the AWS network.

For more information about gateway endpoints, see [Gateway VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway.html) in the *VPC User Guide*. 

## Creating a VPC endpoint policy for Amazon S3
<a name="creating-vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to Amazon S3. The policy specifies the following information: 
+ The AWS Identity and Access Management (IAM) principal that can perform actions 
+ The actions that can be performed 
+ The resources on which actions can be performed 

You can also use Amazon S3 bucket policies to restrict access to specific buckets from a specific VPC endpoint by using the `aws:sourceVpce` condition in your bucket policy. The following examples show policies that restrict access to a bucket or to an endpoint.

**Topics**
+ [Example: Restricting access to a specific bucket from a VPC endpoint](#privatelink-example-restrict-access-to-bucket)
+ [Example: Restricting access to buckets in a specific account from a VPC endpoint](#privatelink-example-access-bucket-in-specific-account-only)
+ [Example: Restricting access to a specific VPC endpoint in the S3 bucket policy](#privatelink-example-restrict-access-to-vpc-endpoint)

### Example: Restricting access to a specific bucket from a VPC endpoint
<a name="privatelink-example-restrict-access-to-bucket"></a>

You can create an endpoint policy that restricts access to only specific Amazon S3 buckets. This type of policy is useful if you have other AWS services in your VPC that use buckets. The following bucket policy restricts access to only the `{{{{amzn-s3-demo-bucket1}}}}`. To use this endpoint policy, replace `{{{{amzn-s3-demo-bucket1}}}}` with the name of your bucket.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Id": "Policy1415115909151",
  "Statement": [
    { "Sid": "Access-to-specific-bucket-only",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Effect": "Allow",
      "Resource": ["arn:aws:s3:::{{amzn-s3-demo-bucket1}}",
                   "arn:aws:s3:::{{amzn-s3-demo-bucket1}}/*"]
    }
  ]
}
```

------

### Example: Restricting access to buckets in a specific account from a VPC endpoint
<a name="privatelink-example-access-bucket-in-specific-account-only"></a>

You can create an endpoint policy that restricts access to only the S3 buckets in a specific AWS account. To prevent clients within your VPC from accessing buckets that you don't own, use the following statement in your endpoint policy. The following example statement creates a policy that restricts access to resources owned by a single AWS account ID, {{`111122223333`}}.

```
{
  "Statement": [
    {
      "Sid": "Access-to-bucket-in-specific-account-only",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Effect": "Deny",
      "Resource": "arn:aws:s3:::*",
      "Condition": {
        "StringNotEquals": {
          "aws:ResourceAccount": "{{111122223333}}"
        }
      }
    }
  ]
}
```

**Note**  
To specify the AWS account ID of the resource being accessed, you can use either the `aws:ResourceAccount` or the `s3:ResourceAccount` key in your IAM policy. However, be aware that some AWS services rely on access to AWS managed buckets. Therefore, using the `aws:ResourceAccount` or `s3:ResourceAccount` key in your IAM policy might also affect access to these resources.

### Example: Restricting access to a specific VPC endpoint in the S3 bucket policy
<a name="privatelink-example-restrict-access-to-vpc-endpoint"></a>

The following Amazon S3 bucket policy allows access to a specific bucket, `{{{{amzn-s3-demo-bucket2}}}}`, from only the VPC endpoint `{{vpce-1a2b3c4d}}`. The policy denies all access to the bucket if the specified endpoint is not being used. The `aws:sourceVpce` condition specifies the endpoint and doesn't require an Amazon Resource Name (ARN) for the VPC endpoint resource, only the endpoint ID. To use this bucket policy, replace `{{{{amzn-s3-demo-bucket2}}}}` and `{{vpce-1a2b3c4d}}` with your bucket name and endpoint. 

**Important**  
When applying the following Amazon S3 bucket policy to restrict access to only certain VPC endpoints, you might block your access to the bucket without intending to do so. Bucket policies that are intended to specifically limit bucket access to connections originating from your VPC endpoint can block all connections to the bucket. For information about how to fix this issue, see [My bucket policy has the wrong VPC or VPC endpoint ID. How can I fix the policy so that I can access the bucket?](https://aws.amazon.com/premiumsupport/knowledge-center/s3-regain-access/) in the *Support Knowledge Center*.
Before using the following example policy, replace the VPC endpoint ID with an appropriate value for your use case. Otherwise, you won't be able to access your bucket. 
This policy disables *console* access to the specified bucket, because console requests don't originate from the specified VPC endpoint. 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Id": "Policy1415115909152",
  "Statement": [
    { "Sid": "Access-to-specific-VPCE-only",
      "Principal": "*",
      "Action": "s3:*",
      "Effect": "Deny",
      "Resource": ["arn:aws:s3:::{{amzn-s3-demo-bucket2}}",
                   "arn:aws:s3:::{{amzn-s3-demo-bucket2/*}}"],
      "Condition": {"StringNotEquals": {"aws:sourceVpce": "{{vpce-1a2b3c4d}}"}}
    }
  ]
}
```

------

For more policy examples, see [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#vpc-endpoints-policies-s3) in the *VPC User Guide*.

For more information about VPC connectivity, see [Network-to-VPC connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) in the AWS whitepaper [Amazon Virtual Private Cloud Connectivity Options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/welcome.html).