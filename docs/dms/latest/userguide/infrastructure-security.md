# Infrastructure security in

AWS Database Migration Service

As a managed service, AWS Database Migration Service is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access AWS DMS through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  You can call these API operations from any network location. AWS DMS also supports
  resource-based access policies, which can specify restrictions on actions and resources, for
  example, based on the source IP address. In addition, you can use AWS DMS policies to
  control access from specific Amazon VPC endpoints or specific virtual private clouds (VPCs).
  Effectively, this isolates network access to a given AWS DMS resource from only the
  specific VPC within the AWS network. For more information about using resource-based access
  policies with AWS DMS, including examples, see [Fine-grained access control
  using resource names and tags](CHAP_Security.md "CHAP_Security.md").

To confine your communications with AWS DMS within a single VPC, you can create a
VPC interface endpoint that enables you to connect to AWS DMS through AWS PrivateLink.
AWS PrivateLink helps ensure that any call to AWS DMS and its associated results remain
confined to the specific VPC for which your interface endpoint is created. You can then
specify the URL for this interface endpoint as an option with every AWS DMS command
that you run using the AWS CLI or an SDK. Doing this helps ensure that your entire
communications with AWS DMS remain confined to the VPC and are otherwise invisible to
the public internet.

###### To create an interface endpoint to access DMS in a single VPC

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. From the navigation pane, choose **Endpoints**. This opens the
   **Create endpoints** page, where you can create the interface
   endpoint from a VPC to AWS DMS.
3. Choose **AWS services**, then search for and choose a value for
   **Service Name**, in this case AWS DMS in the following form.

```
com.amazonaws.`region`.dms
```

Here, `region` specifies the AWS Region where
AWS DMS runs, for example `com.amazonaws.us-west-2.dms`. 4. For **VPC**, choose the VPC to create the interface endpoint from,
for example `vpc-12abcd34`. 5. Choose a value for **Availability Zone** and for **Subnet
ID**. These values should indicate a location where your chosen
AWS DMS endpoint can run, for example `us-west-2a (usw2-az1)` and
`subnet-ab123cd4`. 6. Choose **Enable DNS name** to create the endpoint with a DNS name.
This DNS name consists of the endpoint ID (`vpce-12abcd34efg567hij`)
hyphenated with a random string (`ab12dc34`). These are separated from the
service name by a dot in reverse dot-separated order, with `vpce` added
(`dms.us-west-2.vpce.amazonaws.com`).

An example is
`vpce-12abcd34efg567hij-ab12dc34.dms.us-west-2.vpce.amazonaws.com`. 7. For **Security group**, choose a group to use for the
endpoint.

When you set up your security group, make sure to allow outbound HTTPS calls from
within it. For more information, see [Creating
security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md#CreatingSecurityGroups "../../../vpc/latest/userguide/VPC_SecurityGroups.md#CreatingSecurityGroups") in the _Amazon VPC User Guide_. 8. Choose either **Full Access** or a custom value for
**Policy**. For example, you might choose a custom policy similar to
the following that restricts your endpoint's access to certain actions and
resources.

```
{
  "Statement": [
    {
      "Action": "dms:*",
      "Effect": "Allow",
      "Resource": "*",
      "Principal": "*"
    },
    {
      "Action": [
        "dms:ModifyReplicationInstance",
        "dms:DeleteReplicationInstance"
      ],
      "Effect": "Deny",
      "Resource": "arn:aws:dms:us-west-2:<account-id>:rep:<replication-instance-id>",
      "Principal": "*"
    }
  ]
}
```

Here, the sample policy allows any AWS DMS API call, except for deleting or
modifying a specific replication instance.
You can now specify a URL formed using the DNS name created in step 6 as an option. You
specify this for every AWS DMS CLI command or API operation to access the service
instance using the created interface endpoint. For example, you might run the DMS CLI command
`DescribeEndpoints` in this VPC as shown following.

```
$ aws dms describe-endpoints --endpoint-url https://vpce-12abcd34efg567hij-ab12dc34.dms.us-west-2.vpce.amazonaws.com
```

If you enable the private DNS option, you don't have to specify the endpoint URL in the
request.

For more information on creating and using VPC interface endpoints (including enabling the
private DNS option), see [Interface VPC endpoints (AWS
PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.
