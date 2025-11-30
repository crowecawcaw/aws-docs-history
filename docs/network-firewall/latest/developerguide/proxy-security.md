# Security in your use of the AWS Network Firewall service

## Considerations on creating Proxy endpoints in a VPC with Block Public Access (BPA) enabled

###### Note

Network Firewall Proxy is in public preview release and is subject to change.

If you host applications in a separate VPC with BPA enabled and create a Proxy VPC endpoint in that VPC, such applications will now potentially have access to public internet through Proxy's VPC, assuming that the Proxy configuration allows such traffic. Therefore, it's important to ensure the Proxy is appropriately configured before creating the VPC endpoints in isolated VPCs to avoid unintended outbound (to IGW) access.

## Ensuring clients do not bypass Proxy

When you create a new Proxy, a VPC endpoint is automatically created in the same subnet as your NATGW. Application resources need to be guarded with Security group rules to prevent direct routing of traffic via the NAT GW instead of being evaluated via Proxy first.

If a potential Proxy client is part of a security group that allows outbound to anywhere and belongs to a subnet with a route to IGW via the NAT GW, then they can bypass proxy.

## Reachability of resources co-located with the NATGW - Same VPC

Any traffic processed by the Proxy attached to your NATGW respects your VPC route tables. Any clients using the Proxy to send traffic to destinations that resolve to local IPv4 addresses within the VPC will be able to do so.

Additionally, if you create Proxy VPC Endpoints in other VPCs, clients in those VPCs may now be able to access resources in the NATGW VPC depending on how the security groups or NACLs are configured in the NATGW VPC.

To avoid unintended access by resources in either of the VPCs, ensure that the security groups are configured to allow only relevant clients to use the Proxy VPC endpoint, as well as ensuring that the NATGW subnet is sufficiently isolated using route tables or NACLs.

## Securely configuring your PCA resource for use with AWS Network Firewall Proxy

AWS requires that any PCA resource used with Network Firewall Proxy allows the service principal `proxy.network-firewall.amazonaws.com` to perform `acm-pca` actions listed in this policy: `arn:aws:ram::aws:permission/AWSRAMSubordinateCACertificatePathLen0IssuanceCertificateAuthority`

In order to ensure your PCA resource is used only in the context of your Network Firewall Proxy resource, we recommend attaching a resource policy that is appropriately scoped to your PCA resource, using the `aws:SourceArn` or `aws:SourceAccount` global condition keys. An example policy:

```
{
  "Version": "2012-10-17"
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "preprod.proxy.network-firewall.amazonaws.com"
      },
      "Resource": "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/CA_ID",
      "Action": [
        "acm-pca:GetCertificate",
        "acm-pca:DescribeCertificateAuthority",
        "acm-pca:GetCertificateAuthorityCertificate",
        "acm-pca:ListTags",
        "acm-pca:ListPermissions"
      ],
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:network-firewall:us-east-1:123456789012:proxy/PROXY_NAME"
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "preprod.proxy.network-firewall.amazonaws.com"
      },
      "Action": [
        "acm-pca:IssueCertificate"
      ],
      "Resource": "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/CA_ID",
      "Condition": {
        "StringEquals": {
          "acm-pca:TemplateArn": "arn:aws:acm-pca:::template/SubordinateCACertificate_PathLen0/V1"
        },
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:network-firewall:us-east-1:123456789012:proxy/PROXY_NAME"
        }
      }
    }
  ]
}
```
