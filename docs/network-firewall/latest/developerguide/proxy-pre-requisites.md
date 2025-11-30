# Pre-requisites

## Related services and prerequisites

###### Note

Network Firewall Proxy is in public preview release and is subject to change.

NFW proxy operates as an explicit proxy. No routing rules are required, but workloads need to be configured to route traffic through the proxy. Before implementing Proxy, ensure you have the following prerequisites in place

### NAT Gateway

You must have an existing NAT gateway configured in your VPC. The proxy attaches to NAT gateways to inspect egress traffic. For information about creating a NAT Gateway, see [Creating a NAT Gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating").

In addition, make sure that these are configured in the VPC that you are setting up the NAT Gateway. In addition to creating the NAT Gateway, customers need to ensure that their VPC has these fields enabled, if not proxy creation will fail asynchrously today.VPC attributes: enableDnsSupport and enableDnsHostnames.

Otherwise, the proxy setup will fail. . Error message/failure seen when proxy provisioning fails today on describes: VPC attributes enableDnsSupport and enableDnsHostnames should be set to true to allow proxy on NAT Gateway

### IAM permissions

You need appropriate IAM permissions to create and manage proxy configurations, attach them to NAT gateways, and view logs and metrics. See [Proxy Permissions](#proxy-permissions "#proxy-permissions") for detailed permission requirements.

### Proxy endpoints

When a proxy is created and attached to a NAT Gateway, a Private Link endpoint is automatically created in the same subnet as the associated NAT Gateway.

1. For applications hosted in the same VPC as the Proxy, there is no need to create a Private Link endpoint.
2. For applications hosted in a different VPC than the Proxy, a Private Link endpoint needs to be created in each VPC that needs outbound traffic filtering through the Proxy. This is only needed when the other VPC can't route traffic to the proxy endpoint

###### Create a VPC endpoint to access Proxy

Use the following procedure to create a VPC endpoint that connects to Proxy.

###### Prerequisite

Create a security group for the VPC endpoint that allows traffic to and from the Proxy to the VPC. Add a rule that allows HTTPS traffic, TCP traffic and the required port range from the VPC CIDR block. For more information on setting up policies in security groups, [visit here](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md").

###### To create a VPC endpoint for Proxy:

1. In the AWS NFW proxy console, after you create the proxy, click on the proxy to view details. You will be able to see the VPC service endpoint service name here. Note the VPC service endpoint service name and that it will come in handy.
2. Open the Amazon VPC console.
3. Now, In the navigation pane, choose **Endpoints**.
4. Choose **Create endpoint**.
5. For **Name tag**, enter a name for the endpoint.
6. For **Service category**, choose **AWS services**.
7. Under Endpoint settings -> **Service type**, select the **Endpoint services that use NLB and GWLB**
8. Under **Service settings,** put in the name that the Proxy provides them. You can obtain this name by looking at the VPC endpoint service name under the Proxy details page that you took from step 1.
9. Under **additional settings**, enable **Private DNS name.**
10. For **VPC**, select your VPC.
11. For **Subnets**, select the Availability Zone and then select the private subnet.
12. For **Security group**, select the security group for the VPC endpoint.
13. For **Policy**, select **Full access** to allow all operations by all principals on all resources over the VPC endpoint.
14. (Optional) To add a tag, choose **Add new tag** and enter the tag key and the tag value.
15. Choose **Create endpoint**. The initial status is **Pending**. Before you go to the next step, wait until the status is **Available**. This can take a few minutes.

### Setup Trust between your applications and the Proxy

If you plan to do TLS interception and filter on header attributes using the Proxy, you will need to setup trust between your applications and the Proxy. NFW Proxy supports Private Certificate Authority as a mechanism for you to provide a CA certificate. You can either create a Private CA using AWS Private Certificate Authority (PCA) or bring your own external enterprise CA and use it to sign a subordinate CA on AWS PCA. In either case, please ensure to include the root certificate to the trust store of your applications. The proxy presents PCA-signed certificates which applications trust through the same root, establishing a secure and consistent trust model for encrypted communication.

For more information on how to manage certificates using PCA, check here - https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html

###### First give Proxy access to PCA through these steps:

1. Go to AWS console → cert authority → the PCA console.
2. Go to managed resource shares.
3. Create new resource share.
4. Add a name.
5. Select the resource type as Private CA.
6. Select the resource from the drop down menu Under managed permissions, select AWSRAMSubordinateCACertificatePathLen0IssuanceCertificateAuthority.
7. Click Next.
8. Grant access to service principle.
9. Enter the service principal name. It should be proxy.network-firewall.amazonaws.com.

###### Important

Do not skip the below step. Skipping this step may expose your system to confused
deputy attacks.

To restrict this permission to a specific proxy ARN, use the PCA put-policy API to
create a policy with the service principal.

In order to ensure your PCA resource is used only in the context of your Network Firewall Proxy
resource, we recommend attaching a resource policy that is appropriately scoped to your PCA
resource, using the `aws:SourceArn` or `aws:SourceAccount` global
condition keys. See below:

```
aws acm-pca put-policy \
--resource-arn arn:aws:acm-pca:us-east-2:<account_id>:certificate-authority/<certificate_authority_id> \
--policy file:///path/to/policy.json \
--region us-east-2

```

See below for an example policy:

```
{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "proxy.network-firewall.amazonaws.com"
 },
 "Resource": "arn:aws:acm-pca:us-east-2:<account_id>:certificate-authority/<certificate_authority_id>",
 "Action": [
 "acm-pca:GetCertificate",
 "acm-pca:DescribeCertificateAuthority",
 "acm-pca:GetCertificateAuthorityCertificate",
 "acm-pca:ListTags",
 "acm-pca:ListPermissions"
 ],
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:network-firewall:us-east-2:<account_id>:proxy/<proxy_name>"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "proxy.network-firewall.amazonaws.com"
 },
 "Action": [
 "acm-pca:IssueCertificate"
 ],
 "Resource": "arn:aws:acm-pca:us-east-2:<account_id>:certificate-authority/<certificate_authority_id>",
 "Condition": {
 "StringEquals": {
 "acm-pca:TemplateArn": "arn:aws:acm-pca:::template/SubordinateCACertificate_PathLen0/V1"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:network-firewall:us-east-2:<account_id>:proxy/<proxy_name>"
 }
 }
 }
 ]
}

```

For more details, see [Securely configuring your PCA resource for use with AWS Network Firewall Proxy](proxy-security.md#proxy-pca-configuration "proxy-security.md#proxy-pca-configuration"). 10. Click next. 11. Review the details and click on create.

Then, during the Proxy creation or modification, you need to select the checkbox for TLS intercept and enter the ARN of the PCA.

Also, make sure you have setup your application to trust the PCA.

Note: Console based permission setup should only be used using test PCA resources.

### Proxy variables

You must set up the proxy variables on your applications to route HTTP and HTTPS traffic through the proxy for inspection. Make sure to setup the proxy endpoints first. To set up proxy variables, you can use the fully qualified domain name of the proxy. You can find the domain name in the console under details of the proxy. This domain name resolves to the IP address of the proxy endpoint in your VPC and allows your traffic to be routed via the proxy.

For instructions on how to setup variables on workloads, you can refer this. https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-proxy.html

The most common way to route traffic to an explicit proxy is by using proxy environment variables. You can use http_proxy, and https_proxy variables to route http and https traffic to the proxy. You can combine it with no_proxy variable to exclude private and other trusted destinations that can bypass the proxy. As an example:

```
HTTP_PROXY=http://proxy-server-hostname:port HTTPS_PROXY=https://proxy-server-hostname:port NO_PROXY='amazonaws.com,127.0.0.1,localhost'
```

## Setting up

This tutorial is covered in the Network Firewall firewall documentation under Setting up and covers topics such as signing up for an AWS account, creating a user with administrative access and setting up tool access. For more details, please refer [here](setting-up.md "setting-up.md").

## Proxy Permissions

To work with Proxy, you need specific IAM permissions for creating configurations, managing rules, and attaching proxies to NAT gateways.

For details on how to add IAM permissions, please check IAM documentation [here](../../../IAM/latest/UserGuide/intro-managing-iam.md "../../../IAM/latest/UserGuide/intro-managing-iam.md").

### Proxy management permissions

The following permissions are required for creating and managing proxy configurations:

###### Important

For production deployments, follow the principle of least privilege and restrict permissions to specific resources using resource ARNs instead of wildcards.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "network-firewall:CreateProxyConfiguration",
        "network-firewall:UpdateProxyConfiguration",
        "network-firewall:DeleteProxyConfiguration",
        "network-firewall:DescribeProxyConfiguration",
        "network-firewall:ListProxyConfigurations"
      ],
      "Resource": "*"
    }
  ]
}
```

### Rule management permissions

The following permissions are required for creating and managing proxy filtering rules:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "network-firewall:CreateProxyRulegroups",
        "network-firewall:ModifyProxyRulegroups",
        "network-firewall:DeleteProxyRulegroups",
        "network-firewall:DescribeProxyRulegroups",
        "network-firewall:ListProxyRulegroups"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "network-firewall:CreateProxyRules",
        "network-firewall:ModifyProxyRules",
        "network-firewall:DeleteProxyRules",
        "network-firewall:DescribeProxyRule"
      ],
      "Resource": "*"
    }
  ]
}
```

### NAT Gateway attachment permissions

The following permissions are required for attaching proxy configurations to NAT gateways:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "network-firewall:CreateProxy",
        "network-firewall:DeleteProxy",
        "network-firewall:DescribeProxy",
        "network-firewall:ListProxies",
        "ec2:DescribeNatGateways",
        "ec2:AttachApplianceOnNatGateway",
        "ec2:DetachApplianceFromNatGateway"
      ],
      "Resource": "*"
    }
  ]
}
```

### Monitoring and logging permissions

The following permissions are recommended for monitoring proxy activity and viewing logs:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams",
        "cloudwatch:PutMetricData",
        "cloudwatch:GetMetricStatistics",
        "cloudwatch:ListMetrics"
      ],
      "Resource": "*"
    }
  ]
}
```

### VPC Endpoint permissions

Create/delete and describe permissions on VPC Endpoints.

Note: Proxy creation will fail if these permissions for VPC endpoints are not provided.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateVpcEndpoint",
        "ec2:DeleteVpcEndpoint",
        "ec2:DescribeVpcEndpoints"
      ],
      "Resource": "*"
    }
  ]
}
```
