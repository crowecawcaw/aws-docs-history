

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure private endpoint access for Argo CD
<a name="argocd-private-access"></a>

By default, you can access the Argo CD endpoint over the public internet. You can configure private endpoint access so that traffic between your VPC and the Argo CD endpoint stays within the AWS network, without going through the public internet.

When you enable private access, AWS updates the Domain Name System (DNS) so that the Argo CD endpoint hostname resolves to private IP addresses associated with your VPC endpoint. You must have network connectivity to these private IPs (through your VPC, a virtual private network (VPN) connection, or AWS Direct Connect) to access the Argo CD endpoint.

## How private access works
<a name="_how_private_access_works"></a>

When you configure private access for your Argo CD capability:

1. You create a VPC endpoint for the `com.amazonaws.region-code.eks-capabilities` service in your VPC.

1. You provide the VPC endpoint ID when creating or updating the Argo CD capability.

1.  AWS configures DNS records so that the Argo CD endpoint hostname resolves to private IP addresses associated with your VPC endpoint.

1. All traffic to the Argo CD endpoint flows privately through the VPC endpoint.

## Prerequisites
<a name="_prerequisites"></a>
+ An Amazon Elastic Kubernetes Service (Amazon EKS) cluster with an active Argo CD capability (see [Create an Argo CD capability](create-argocd-capability.md))
+ Familiarity with Amazon VPC concepts, including subnets, security groups, and interface VPC endpoints
+ A VPC with subnets in the Availability Zones where you want private access
+  AWS Command Line Interface (AWS CLI) version `2.12.3` or later

## Step 1: Create a VPC endpoint for eks-capabilities
<a name="_step_1_create_a_vpc_endpoint_for_eks_capabilities"></a>

Create an interface VPC endpoint for the `com.amazonaws.region-code.eks-capabilities` service.

------
#### [ Console ]

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).

1. In the left navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. For **Service category**, choose ** AWS services**.

1. In the search field, enter `eks-capabilities` and select `com.amazonaws.region-code.eks-capabilities`.

1. For **VPC**, select the VPC from which you want to access the Argo CD endpoint.

1. For **Subnets**, select a subnet in each Availability Zone where you want private access.

1. For **Security groups**, select a security group that allows HTTPS (port 443) inbound traffic from your client networks.

1. Choose **Create endpoint**.

1. Note the VPC endpoint ID (for example, `vpce-0123456789abcdef0`).

------
#### [ CLI ]

Replace {{region-code}} with your AWS Region, {{vpc-id}} with your VPC ID, {{subnet-id-1 subnet-id-2}} with subnet IDs in different Availability Zones, and {{sg-id}} with a security group that allows HTTPS inbound traffic.

```
aws ec2 create-vpc-endpoint \
  --region {{region-code}} \
  --vpc-endpoint-type Interface \
  --service-name com.amazonaws.{{region-code}}.eks-capabilities \
  --vpc-id {{vpc-id}} \
  --subnet-ids {{subnet-id-1 subnet-id-2}} \
  --security-group-ids {{sg-id}}
```

Note the `VpcEndpointId` in the response.

------

**Important**  
Make sure the security group attached to the VPC endpoint allows inbound HTTPS (port 443) traffic. The traffic source must include all networks where your users or applications access the Argo CD endpoint.

## Step 2: Configure private access on the Argo CD capability
<a name="_step_2_configure_private_access_on_the_argo_cd_capability"></a>

After the VPC endpoint is available, configure the Argo CD capability to use it. You can configure private access when creating a new capability or by updating an existing one.

### Create a new capability with private access
<a name="_create_a_new_capability_with_private_access"></a>

Include the `networkAccess` in the `create-capability` command. Replace {{region-code}}, {{my-cluster}}, and other placeholders with your values:

```
aws eks create-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name my-argocd \
  --type ARGOCD \
  --role-arn {{arn:aws:iam::111122223333:role/ArgoCDCapabilityRole}} \
  --configuration '{
    "argoCd": {
      "awsIdc": {
        "idcInstanceArn": "arn:aws:sso:::instance/ssoins-1234567890abcdef",
        "idcRegion": "idc-region-code"
      },
      "rbacRoleMappings": [{
        "role": "ADMIN",
        "identities": [{
          "id": "user-id",
          "type": "SSO_USER"
        }]
      }],
      "networkAccess": {
        "vpceIds": ["vpce-0123456789abcdef0"]
      }
    }
  }'
```

### Update an existing capability to enable private access
<a name="_update_an_existing_capability_to_enable_private_access"></a>

Replace {{region-code}}, {{my-cluster}}, {{my-argocd}}, and the VPC endpoint ID with your values:

```
aws eks update-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name {{my-argocd}} \
  --configuration '{
    "argoCd": {
      "networkAccess": {
        "vpceIds": ["vpce-0123456789abcdef0"]
      }
    }
  }'
```

Wait for the capability update to complete:

```
aws eks describe-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name {{my-argocd}} \
  --query 'capability.status' \
  --output text
```

The status returns to `ACTIVE` when the update is complete.

## Step 3: Verify DNS resolution and connectivity
<a name="_step_3_verify_dns_resolution_and_connectivity"></a>

After the capability becomes active with private access configured, verify that the Argo CD endpoint hostname resolves to private IP addresses.

Run the following `nslookup` command from any network:

```
nslookup {{your-argocd-endpoint.eks-capabilities.region-code.amazonaws.com}}
```

The response should show private IP addresses (for example, addresses in RFC 1918 ranges such as `10.x.x.x` or `172.16.x.x`).

If the endpoint does not resolve to private IPs, verify that:
+ The capability status is `ACTIVE` (AWS creates DNS records after the capability becomes active)
+ The VPC endpoint is in the `available` state
+ The VPC endpoint ID in the capability configuration matches the endpoint you created

**Note**  
After you configure private access, the Argo CD endpoint hostname resolves to private IP addresses. To connect, you must have network connectivity to those private IPs through your VPC, a VPN connection, or AWS Direct Connect.

## Disable private access
<a name="_disable_private_access"></a>

To disable private access and restore public endpoint access, update the capability to remove the VPC endpoint IDs:

```
aws eks update-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name {{my-argocd}} \
  --configuration '{
    "argoCd": {
      "networkAccess": {
        "vpceIds": []
      }
    }
  }'
```

## Considerations
<a name="_considerations"></a>
+ After you enable private access, the Argo CD endpoint is only reachable from within your VPC or networks connected to it (for example, through VPN or AWS Direct Connect).
+ The VPC endpoint must remain in the `available` state for private access to function. If you delete the VPC endpoint, you lose access to the Argo CD endpoint until you create a new endpoint and update the capability.
+  AWS doesn’t currently support VPC endpoint policies for the `eks-capabilities` service endpoint.