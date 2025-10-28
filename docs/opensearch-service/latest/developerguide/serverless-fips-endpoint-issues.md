# Resolve FIPS endpoint connectivity issues

in private hosted zones

FIPS endpoints work with Amazon OpenSearch Serverless collections that have public access. For newly created
VPC collections that use newly created VPC endpoints, FIPS endpoints function as expected.
For other VPC collections, you might need to perform manual setup to ensure FIPS endpoints
operate correctly.

###### To configure FIPS private hosted zones in Amazon Route 53

1. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. Review your hosted zones:
   1. Locate the hosted zones for the AWS Regions your collections are
      in.
   2. Verify the hosted zone naming patterns:
      - Non-FIPS format:
        ``region`.aoss.amazonaws.com`.
      - FIPS format:
        ``region`.aoss-fips.amazonaws.com`.

   3. Confirm the **Type** for all of your hosted zones is set
      to **Private hosted zone**.

3. If the FIPS private hosted zone is missing:
   1. Select the corresponding non-FIPS private hosted zone.
   2. Copy the **Associated VPCs** information. For example:
      `vpc-1234567890abcdef0 | us-east-2`.
   3. Find the wildcard domain record. For example:
      `*.us-east-2.aoss.amazonaws.com`.
   4. Copy the **Value/Route traffic to** information. For
      example:`uoc1c1qsw7poexampleewjeno1pte3rw.3ym756xh7yj.aoss.searchservices.aws`.

4. Create the FIPS private hosted zone:
   1. Create a new private hosted zone with the FIPS format. For example:
      `us-east-2.aoss-fips.amazonaws.com`.
   2. For **Associated VPCs**, enter the VPC information you
      copied from the non-FIPS private hosted zone.

5. Add a new record with the following settings:
   1. Record name: \*
   2. Record type: CNAME
   3. Value: Enter the **Value/Route traffic to** information
      you copied earlier.

## Common Issues

If you experience connectivity issues with your FIPS-compliant VPC endpoints, use the
following information to help resolve the problem.

- DNS resolution failures - You cannot resolve the FIPS endpoint domain name
  within your VPC
- Connection timeouts - Your requests to the FIPS endpoint time out
- Access denied errors - Authentication or authorization fails when using FIPS
  endpoints
- Missing private hosted zone records for VPC-only collections

###### To troubleshoot FIPS endpoint connectivity

1. Verify your Private Hosted Zone configuration:
   1. Confirm that a Private Hosted Zone exists for the FIPS endpoint domain
      (`*.region.aoss-fips.amazonaws.com`.
   2. Verify that the private hosted zone is associated with the correct
      VPC.

   For more information, see [Private hosted zones](../../../Route53/latest/DeveloperGuide/hosted- zones-private.md "../../../Route53/latest/DeveloperGuide/hosted- zones-private.md") in the
   _Amazon Route 53 Developer Guide_, and [Manage DNS
   names](../../../vpc/latest/privatelink/manage-dns-names.md "../../../vpc/latest/privatelink/manage-dns-names.md") in the
   _AWS PrivateLink Guide_.

2. Test DNS resolution:
   1. Connect to an EC2 instance in your VPC.
   2. Run the following command:

   ```
   nslookup collection-id.region.aoss-fips.amazonaws.com
   ```

   3. Confirm that the response includes the private IP address of your VPC
      endpoint.

   For more information, see [Endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints- access.md#endpoint-dns-verification "../../../vpc/latest/privatelink/vpc-endpoints- access.md#endpoint-dns-verification"), and
   [DNS attributes](../../../vpc/latest/userguide/vpc-dns.md#vpc- dns-troubleshooting "../../../vpc/latest/userguide/vpc-dns.md#vpc- dns-troubleshooting") in the
   _Amazon VPC User Guide_.

3. Check your security group settings:
   1. Verify that the security group attached to the VPC endpoint permits HTTPS
      traffic (port 443) from your resources.
   2. Confirm that security groups for your resources permit outbound traffic to
      the VPC endpoint.For more information, see [Endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-security-groups "../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-security-groups") in the _AWS PrivateLink Guide_,
      and [Security
      groups](../../../vpc/latest/userguide/vpc-security-groups.md#SecurityGroupRules "../../../vpc/latest/userguide/vpc-security-groups.md#SecurityGroupRules") in the _Amazon VPC User Guide_ .

4. Review your network ACL configuration:
   1. Verify that network ACLs permit traffic between your resources and the VPC
      endpoint.

   For more information, see [Network ACLs](../../../vpc/latest/userguide/vpc-network- acls.md#nacl-troubleshooting "../../../vpc/latest/userguide/vpc-network- acls.md#nacl-troubleshooting") in the
   _Amazon VPC User Guide_.

5. Review your endpoint policy:
   1. Check that the VPC endpoint policy permits the required actions on your
      OpenSearch Serverless resources.

   For more information, see [VPC
   endpoint permissions required](serverless-vpc.md#serverless-vpc-permissions "serverless-vpc.md#serverless-vpc-permissions"), and [Endpoints policies](../../../vpc/latest/privatelink/vpc-endpoints- access.md#vpc-endpoint-policies "../../../vpc/latest/privatelink/vpc-endpoints- access.md#vpc-endpoint-policies") in the
   _AWS PrivateLink Guide_.

###### Tip

If you use custom DNS resolvers in your VPC, configure them to forward requests for
`*.amazonaws.com` domains to the AWS servers.
