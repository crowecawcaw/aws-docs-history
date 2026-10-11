

# Issuing ACME certificates over AWS PrivateLink
<a name="acm-acme-privatelink"></a>

AWS Certificate Manager (ACM) supports issuing certificates through the Automated Certificate Management Environment (ACME) protocol over AWS PrivateLink, so that ACME clients in your VPC can issue certificates without routing traffic over the public internet. AWS PrivateLink connects your VPC directly to ACM through the Amazon network without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.

For more information about AWS PrivateLink and Amazon VPC endpoints, see [Interface Amazon VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon Virtual Private Cloud User Guide*.

ACM offers two Amazon VPC endpoint services for ACME, one for each side of the protocol:
+ `com.amazonaws.{{region}}.acm-acme` serves the ACME management operations that a PKI administrator uses to configure ACME, such as `CreateAcmeEndpoint`, `CreateAcmeDomainValidation`, and `CreateAcmeExternalAccountBinding`.
+ `com.amazonaws.{{region}}.acm-acme-enroll` serves the ACME protocol itself, which ACME clients use to issue and revoke certificates.

The two are independent: an endpoint for one does not provide access to the other, and each takes its own endpoint policy. The rest of this section describes the endpoint for certificate issuance.

## Considerations for ACME issuance VPC endpoints
<a name="acm-acme-privatelink-considerations"></a>

Before you set up interface Amazon VPC endpoints for ACME certificate issuance, be aware of the following considerations:
+ ACM might not support Amazon VPC endpoints for ACME in some Availability Zones. When you create an Amazon VPC endpoint, first check support in the management console. Unsupported Availability Zones are marked *Service not supported in this Availability Zone*.
+ Amazon VPC endpoints do not support cross-Region requests. Ensure that you create your endpoint in the same Region where your ACME endpoint is configured.
+ Amazon VPC endpoints only support Amazon provided DNS through Amazon Route 53. If you want to use your own DNS, you can use conditional DNS forwarding. For more information, see [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon Virtual Private Cloud User Guide*.
+ The security group attached to the Amazon VPC endpoint must allow incoming connections on port 443 from the private subnet of the VPC.

## Creating the Amazon VPC endpoint for ACME certificate issuance
<a name="acm-acme-privatelink-create"></a>

You can create an Amazon VPC endpoint for ACME certificate issuance using either the VPC console or the AWS Command Line Interface. For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/create-interface-endpoint.html) in the *Amazon Virtual Private Cloud User Guide*.

When creating the endpoint, specify `com.amazonaws.{{region}}.acm-acme-enroll` as the service name.

**Important**  
You must enable private DNS host names for the Amazon VPC endpoint. Without them, ACME clients cannot reach your ACME endpoint through the Amazon VPC endpoint.

## Creating an Amazon VPC endpoint policy for ACME certificate issuance
<a name="acm-acme-privatelink-policy"></a>

You can attach a policy to your Amazon VPC endpoint to control access to ACME operations. The policy specifies the principals that can perform actions, the actions they can perform, and the resources on which they can act. For more information, see [Control access to Amazon VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon Virtual Private Cloud User Guide*.

The ACME issuance flow (account registration, order placement, authorization, finalize, and download) spans several operations. Most of them are evaluated against the ACME endpoint resource and do not correspond to a named IAM action. The finalize and revocation steps are evaluated against the certificate resource, as `acm:RequestCertificate` and `acm:RevokeCertificate`. An Amazon VPC endpoint policy that restricts access to a specific ACME endpoint must therefore cover both resource types.

**Example Amazon VPC endpoint policy for ACME certificate issuance on a specific endpoint**  <a name="acm-acme-privatelink-policy-example"></a>
The following policy restricts all ACME operations to a single endpoint. The first statement covers account registration, order placement, authorization, and download. Because those operations have no named IAM action for a policy to match, `"Action": "*"` is required. The second statement covers finalize and revocation.  

```
{
   "Version": "2012-10-17",		 	 	 
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": "*",
         "Resource": "arn:aws:acm:{{region}}:{{account-id}}:acme-endpoint/{{endpoint-id}}"
      },
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "acm:RequestCertificate",
            "acm:RevokeCertificate"
         ],
         "Resource": "arn:aws:acm:{{region}}:{{account-id}}:certificate/*"
      }
   ]
}
```

A request that arrives through the Amazon VPC endpoint must be allowed by both the endpoint policy and the IAM policies on the IAM role associated with the EAB credentials. Because the endpoint policy cannot identify the calling principal, use the role's identity policies to control which principals can issue or revoke certificates. For more information, see [IAM for ACME certificate automation](security-iam-acme.md).