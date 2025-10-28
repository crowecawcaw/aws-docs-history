NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Installing the MGN connector on a secured network

The MGN connector and the AWS Replication Agents that the MGN connector installs, require network access to various AWS endpoints.
If your on-premises network is not open to AWS endpoints, then you can install the MGN connector and the AWS Replication Agents
with the aid of PrivateLink.

You can connect your on-premises network to your VPCs using AWS VPN or DirectConnect.

## Global view

If you are using the
[Global view](global-view.md "global-view.md")
feature, which provides cross-account view and operations, you will have at least one staging VPC per member account.

You will also need to designate a VPC in the management account in order to allow the MGN connector to communicate
with AWS services via PrivateLink. If you are migrating some of your source servers into the management account,
you can use the same VPC as a staging VPC.

**The following sections apply to the MGN connector VPC as well as to each staging VPC.**

## Create VPC endpoints

To allow the MGN connector and AWS Replication Agents to communicate with AWS services, create the VPC endpoints listed below.
For each endpoint:

1. Select your staging area VPC or MGN connector VPC (see
   [Global view](#mgn-connector-global-view "#mgn-connector-global-view")
   above).
2. **Enable private DNS names.**
3. Choose a subnet, and ensure that a route exists from the MGN connector or AWS Replication Agent to the selected subnet.
4. Ensure that the security groups associated with the endpoint allow inbound traffic from the MGN connector and source servers.

Create the following interface endpoints:

1. **`com.amazonaws.`region`.ssm`**
   – The endpoint for the Systems Manager service.
   This endpoint is required by the SSM Agent, which is installed by the MGN connector installer.
2. **`com.amazonaws.`region`.ec2messages`**
   – Systems Manager uses this endpoint to make calls from the SSM Agent to the Systems Manager service.
3. **`com.amazonaws.`region`.ssmmessages`**
   – This endpoint is required only if you wish to connect to the MGN connector using Session Manager.
4. **`com.amazonaws.`region`.kms`**
   – This endpoint is required only if you wish to connect to the MGN connector using Session Manager
   and using AWS KMS encryption to add an additional layer of encryption to the session.
   For more information, see
   [Turn on KMS key encryption of session data](../../../systems-manager/latest/userguide/session-preferences-enable-encryption.md "../../../systems-manager/latest/userguide/session-preferences-enable-encryption.md")
   in the _Amazon Systems Manager User Guide_.
5. **`com.amazonaws.`region`.s3`**
   – Systems Manager uses this endpoint to update the SSM Agent and to perform patching operations.
   The MGN connector installer and the AWS Replication Agent installer download installation assets from this endpoint.
   1. Note that private DNS names are disabled by default for the S3 endpoint.
   2. If you wish to also **Enable private DNS only for inbound endpoint**,
      you must first create an S3 gateway VPC endpoint. For more information, see
      [S3 Private DNS](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md#private-dns "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md#private-dns")
      in the _Amazon Simple Storage Service User Guide_.

6. **`com.amazonaws.`region`.secretsmanager`**
   – The MGN connector calls this endpoint to retrieve source server credentials.
7. **`com.amazonaws.`region`.sts`**
   – The MGN connector calls this endpoint to retrieve credentials of the AWS Replication Agent installer role.
8. **`com.amazonaws.`region`.mgn`**
   – The endpoint for MGN. This endpoint is required by the MGN connector, the AWS Replication Agent,
   and their respective installers.
   If a VPCE Policy is used (to scope down access), add the following statement to your policy:

```
{
    "Effect": "Allow",
    "Principal": "*",
    "Action": "execute-api:Invoke",
    "Resource": "arn:aws:execute-api:<region>:*:*/POST/CreateSessionForMgn"
}
```

For more information, see
[Creating an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html")
in the _Amazon VPC User Guide_.

## Create a Route 53 inbound endpoint

To route your traffic to the VPC endpoints created above, create a Route 53 inbound endpoint in your staging area VPC
or the MGN connector VPC (see
[Global view](#mgn-connector-global-view "#mgn-connector-global-view")
above).

Ensure that the security group associated with the inbound endpoint allows traffic from your on-premises DNS resolvers.

Configure DNS resolvers on your on-premises network to forward DNS queries for the endpoints of the above AWS services,
to the IP addresses of your Route 53 inbound endpoint.
To find the regional endpoints of these services, see
[Service endpoints](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md")
in the _AWS General Reference Guide_.
For example, the endpoint of the MGN service in the US East (Ohio) Region (us-east-2) is
**`mgn.us-east-2.amazonaws.com`**

For more information, see
[Forwarding inbound DNS queries to your VPCs](../../../Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.md "../../../Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.md")
in the _Amazon Route 53 User Guide_.

## Modify replication settings

In order to allow the AWS Replication Agent to communicate with the replication server without using the public internet,
you must use Private IP for data replication. The replication server requires access to the EC2 service. Therefore:

- If your staging area VPC has a VPC endpoint for
  **`com.amazonaws.`region`.ec2`**
  with private DNS names enabled, or if your staging area subnet has a route to the public internet via a NAT gateway,
  then the replication server can communicate with EC2 over its private IP. Choose the option:

**Use private IP for data replication**

- Otherwise, if your staging area subnet has a route to the public internet via an internet gateway,
  a public IP is required for the replication server to reach EC2. Choose the option:

**Create public IP, and use Private IP for data replication**

Ensure that the security groups associated with the MGN VPC endpoint allow inbound traffic from the replication server.

## Verify VPC endpoints are being used

Use CloudTrail to verify that calls to AWS services from the MGN connector and its associated source servers,
are made via the **vpcEndpointId**s of the VPC endpoints you have created.
