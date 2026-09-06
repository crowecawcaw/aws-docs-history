

# Accessing the AWS Transform web application from a VPC
<a name="vpc-webapp-access"></a>

When you use AWS PrivateLink to access the AWS Transform API privately from your VPC, the web application requires additional network configuration. It serves static content (HTML, JavaScript, CSS) through CloudFront, which requires internet connectivity. API calls from the web application go through your VPC endpoint and remain fully private.

This guide shows you how to configure controlled internet egress from your VPC so the web application can load while keeping your VPC locked down to only the required domains.

## How it works
<a name="vpc-webapp-how-it-works"></a>

The AWS Transform web application uses two network paths:
+ **API calls** – When you interact with the web application (starting jobs, viewing workspaces, and so on), the browser sends API requests to `api.transform.{{region}}.on.aws`. With the `com.amazonaws.{{region}}.api.transform` VPC endpoint and private DNS enabled, these requests resolve to a private IP address in your VPC and never leave the AWS network.
+ **Static content** – The web application's HTML, JavaScript, and CSS files are served through CloudFront via `{{tenant-id}}.transform.{{region}}.on.aws`. Loading these files requires internet connectivity because CloudFront content delivery is only available over the public internet.
+ **Authentication** – AWS IAM Identity Center sign-in flows use `{{region}}.signin.aws`, which also requires internet connectivity.

To enable the web application while maintaining security, you create a controlled egress path using AWS Network Firewall with domain-based filtering. This allows your VPC to reach *only* the specific domains required by the web application while blocking all other internet traffic.

## Architecture
<a name="vpc-webapp-architecture"></a>

The following diagram shows the network path for web application traffic:

```
EC2 Instance / Workspace (Private Subnet)
    |
    | Route: 0.0.0.0/0 → Network Firewall Endpoint
    v
AWS Network Firewall (Firewall Subnet)
    | Allows: *.cloudfront.net, *.transform.<region>.on.aws,
    |         <region>.signin.aws, SSO domains, S3 presigned URLs
    | Blocks: everything else (TLS SNI inspection)
    |
    | Route: 0.0.0.0/0 → NAT Gateway
    v
NAT Gateway (Public Subnet)
    |
    | Route: 0.0.0.0/0 → Internet Gateway
    v
Internet Gateway → CloudFront Edge Locations
```

**Important**  
The Network Firewall must see both directions of traffic (symmetric routing) to perform TLS SNI inspection. You must configure a return route in the NAT Gateway subnet that sends traffic destined for the private subnet back through the firewall. Without this, domain-based filtering rules will not work.

## Prerequisites
<a name="vpc-webapp-prereqs"></a>

Before you begin, ensure you have:
+ An AWS account with permissions to create VPC resources, Network Firewall, and NAT Gateways.
+ A VPC with a private subnet where your instances or workloads run.
+ An internet gateway attached to the VPC (or permissions to create one).
+ A AWS Transform VPC endpoint for `com.amazonaws.{{region}}.api.transform` with private DNS enabled. This is the endpoint used by the web application browser client. For instructions on creating endpoints, see [AWS Transform and interface endpoints (AWS PrivateLink)](vpc-interface-endpoints.md).

## Configuring the VPC endpoint policy
<a name="vpc-webapp-endpoint-policy"></a>

If your `com.amazonaws.{{region}}.api.transform` VPC endpoint has a custom endpoint policy, you must add a statement that allows AWS Transform operations. Without this, the web application will be unable to make API calls through the endpoint.

Add the following statement to your VPC endpoint policy. Replace {{AWS\_TRANSFORM\_PROFILE\_ARN}} with your AWS Transform service profile ARN, which you can find in the AWS Transform console on the *Settings* page.

```
{
    "Statement": [
        {
            "Sid": "AllowAWSTransform",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalArn": [
                        "{{AWS_TRANSFORM_PROFILE_ARN}}"
                    ]
                }
            }
        }
    ]
}
```

**Note**  
If your VPC endpoint uses the default policy (full access), no changes are needed and you can skip this step.

## Setting up controlled internet egress
<a name="vpc-webapp-setup"></a>

Complete the following steps to configure Network Firewall with domain-based filtering for the AWS Transform web application.

### Step 1: Create the firewall subnet
<a name="vpc-webapp-step1"></a>

Create a small /28 subnet dedicated to the Network Firewall endpoint. This subnet must be in the same Availability Zone as your private subnet.

```
aws ec2 create-subnet \
  --vpc-id {{your-vpc-id}} \
  --cidr-block {{firewall-subnet-cidr}} \
  --availability-zone {{your-az}} \
  --region {{region}}
```

### Step 2: Create a public subnet for the NAT Gateway
<a name="vpc-webapp-step2"></a>

```
aws ec2 create-subnet \
  --vpc-id {{your-vpc-id}} \
  --cidr-block {{public-subnet-cidr}} \
  --availability-zone {{your-az}} \
  --region {{region}}
```

### Step 3: Configure the public subnet route table
<a name="vpc-webapp-step3"></a>

Create a route table for the public subnet that routes internet traffic to the internet gateway.

```
# Create route table
PUB_RTB=$(aws ec2 create-route-table \
  --vpc-id {{your-vpc-id}} \
  --region {{region}} \
  --query 'RouteTable.RouteTableId' --output text)

# Add default route to internet gateway
aws ec2 create-route \
  --route-table-id $PUB_RTB \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id {{your-igw-id}} \
  --region {{region}}

# Associate with public subnet
aws ec2 associate-route-table \
  --route-table-id $PUB_RTB \
  --subnet-id {{public-subnet-id}} \
  --region {{region}}
```

### Step 4: Create the NAT Gateway
<a name="vpc-webapp-step4"></a>

```
# Allocate an Elastic IP
EIP=$(aws ec2 allocate-address --domain vpc \
  --region {{region}} --query 'AllocationId' --output text)

# Create NAT Gateway in the public subnet
NAT_ID=$(aws ec2 create-nat-gateway \
  --subnet-id {{public-subnet-id}} \
  --allocation-id $EIP \
  --region {{region}} \
  --query 'NatGateway.NatGatewayId' --output text)

# Wait for NAT Gateway to become available (~2 minutes)
aws ec2 wait nat-gateway-available \
  --nat-gateway-ids $NAT_ID --region {{region}}
```

### Step 5: Create the Network Firewall rule group
<a name="vpc-webapp-step5"></a>

Create a stateful rule group that allows traffic only to the domains required by the AWS Transform web application.

```
aws network-firewall create-rule-group \
  --rule-group-name transform-webapp-domains \
  --type STATEFUL \
  --capacity 100 \
  --rule-group '{
    "StatefulRuleOptions": {
      "RuleOrder": "STRICT_ORDER"
    },
    "RulesSource": {
      "RulesSourceList": {
        "Targets": [
          ".cloudfront.net",
          ".transform.{{region}}.on.aws",
          "{{region}}.signin.aws",
          ".s3.{{region}}.amazonaws.com",
          "oidc.{{region}}.amazonaws.com",
          "portal.sso.{{region}}.amazonaws.com",
          "assets.sso-portal.{{region}}.amazonaws.com",
          "{{directory-id}}.awsapps.com"
        ],
        "TargetTypes": ["TLS_SNI", "HTTP_HOST"],
        "GeneratedRulesType": "ALLOWLIST"
      }
    }
  }' \
  --region {{region}}
```

Replace {{region}} with the AWS Region where your AWS Transform profile is installed (for example, `us-east-1`). Replace {{directory-id}} with your IAM Identity Center directory ID (for example, `d-1234567890`). You can find your directory ID in the IAM Identity Center console.

The following table explains the allowed domains.


| Domain | Purpose | 
| --- | --- | 
| .cloudfront.net | CloudFront CDN – serves web application static assets (JavaScript, CSS, images) | 
| .transform.{{region}}.on.aws | Web application tenant URL – the browser loads the initial page from this domain via CloudFront | 
| {{region}}.signin.aws | SSO sign-in redirect page | 
| .s3.{{region}}.amazonaws.com | S3 presigned URLs – artifact uploads and downloads | 
| oidc.{{region}}.amazonaws.com | OIDC token exchange for SSO authentication | 
| portal.sso.{{region}}.amazonaws.com | SSO portal login page | 
| assets.sso-portal.{{region}}.amazonaws.com | SSO portal static assets (CSS, JavaScript) | 
| {{directory-id}}.awsapps.com | IAM Identity Center portal for your organization | 

**Note**  
The `.cloudfront.net` wildcard allows traffic to any CloudFront distribution, not only the AWS Transform web application's. A narrower domain filter is not possible because CloudFront edge IPs are shared across distributions and TLS SNI inspection cannot distinguish individual distributions behind the same domain.

**Note**  
API calls to `api.transform.{{region}}.on.aws` go through AWS PrivateLink and do not require internet egress. They are not affected by the firewall.

### Step 6: Create the firewall policy
<a name="vpc-webapp-step6"></a>

The policy must use `STRICT_ORDER` rule evaluation with `drop_established` as the default action. This ensures that any traffic not matching the allowlist is dropped.

```
# Get the rule group ARN
RG_ARN=$(aws network-firewall describe-rule-group \
  --rule-group-name transform-webapp-domains \
  --type STATEFUL --region {{region}} \
  --query 'RuleGroupResponse.RuleGroupArn' --output text)

# Create the firewall policy
aws network-firewall create-firewall-policy \
  --firewall-policy-name transform-webapp-policy \
  --firewall-policy "{
    \"StatelessDefaultActions\": [\"aws:forward_to_sfe\"],
    \"StatelessFragmentDefaultActions\": [\"aws:forward_to_sfe\"],
    \"StatefulRuleGroupReferences\": [
      {
        \"ResourceArn\": \"$RG_ARN\",
        \"Priority\": 1
      }
    ],
    \"StatefulEngineOptions\": {
      \"RuleOrder\": \"STRICT_ORDER\"
    },
    \"StatefulDefaultActions\": [\"aws:drop_established\", \"aws:alert_established\"]
  }" \
  --region {{region}}
```

### Step 7: Create the Network Firewall
<a name="vpc-webapp-step7"></a>

```
# Get the policy ARN
FW_POLICY_ARN=$(aws network-firewall describe-firewall-policy \
  --firewall-policy-name transform-webapp-policy \
  --region {{region}} \
  --query 'FirewallPolicyResponse.FirewallPolicyArn' --output text)

# Create the firewall
aws network-firewall create-firewall \
  --firewall-name transform-webapp-firewall \
  --firewall-policy-arn $FW_POLICY_ARN \
  --vpc-id {{your-vpc-id}} \
  --subnet-mappings SubnetId={{firewall-subnet-id}} \
  --region {{region}}

# Wait for the firewall to become READY (3-5 minutes)
while true; do
  STATUS=$(aws network-firewall describe-firewall \
    --firewall-name transform-webapp-firewall \
    --region {{region}} \
    --query 'FirewallStatus.Status' --output text)
  echo "Status: $STATUS"
  if [ "$STATUS" = "READY" ]; then break; fi
  sleep 15
done
```

### Step 8: Get the firewall endpoint ID
<a name="vpc-webapp-step8"></a>

```
FW_ENDPOINT=$(aws network-firewall describe-firewall \
  --firewall-name transform-webapp-firewall \
  --region {{region}} \
  --query "FirewallStatus.SyncStates.\"{{your-az}}\".Attachment.EndpointId" \
  --output text)
echo "Firewall endpoint: $FW_ENDPOINT"
```

### Step 9: Configure the firewall subnet route table
<a name="vpc-webapp-step9"></a>

Route internet-bound traffic from the firewall subnet to the NAT Gateway.

```
FW_RTB=$(aws ec2 create-route-table \
  --vpc-id {{your-vpc-id}} \
  --region {{region}} \
  --query 'RouteTable.RouteTableId' --output text)

aws ec2 create-route \
  --route-table-id $FW_RTB \
  --destination-cidr-block 0.0.0.0/0 \
  --nat-gateway-id $NAT_ID \
  --region {{region}}

aws ec2 associate-route-table \
  --route-table-id $FW_RTB \
  --subnet-id {{firewall-subnet-id}} \
  --region {{region}}
```

### Step 10: Update the private subnet route table
<a name="vpc-webapp-step10"></a>

Route all internet-bound traffic from the private subnet through the firewall.

```
aws ec2 create-route \
  --route-table-id {{private-subnet-route-table-id}} \
  --destination-cidr-block 0.0.0.0/0 \
  --vpc-endpoint-id $FW_ENDPOINT \
  --region {{region}}
```

If a default route already exists, use `replace-route` instead of `create-route`.

### Step 11: Add the symmetric return route (required)
<a name="vpc-webapp-step11"></a>

**Important**  
This step is critical. Network Firewall uses TLS SNI inspection and must see both directions of a TCP connection. Add a route in the NAT Gateway subnet's route table that sends return traffic destined for the private subnet back through the firewall.

```
aws ec2 create-route \
  --route-table-id $PUB_RTB \
  --destination-cidr-block {{private-subnet-cidr}} \
  --vpc-endpoint-id $FW_ENDPOINT \
  --region {{region}}
```

Replace {{private-subnet-cidr}} with the CIDR block of your private subnet (for example, `10.0.144.0/20`).

Without symmetric routing, the firewall only sees one direction of traffic. The TLS inspection engine cannot extract the Server Name Indication (SNI) from the TLS handshake, and all domain-based rules will fail silently.

### Step 12: Remove the IPv6 default route (if present)
<a name="vpc-webapp-step12"></a>

If the private subnet route table has an IPv6 default route (`::/0`) pointing directly to an internet gateway, it will bypass the firewall for IPv6-capable destinations. Remove it:

```
aws ec2 delete-route \
  --route-table-id {{private-subnet-route-table-id}} \
  --destination-ipv6-cidr-block ::/0 \
  --region {{region}}
```

## Verification
<a name="vpc-webapp-verification"></a>

From an instance in the private subnet, verify the configuration:

```
# Should SUCCEED - web application content via CloudFront (allowed)
curl -vL --connect-timeout 15 \
  'https://{{tenant-id}}.transform.{{region}}.on.aws'

# Should SUCCEED - API via PrivateLink (does not use firewall)
curl -v --connect-timeout 15 \
  'https://api.transform.{{region}}.on.aws/'

# Should FAIL - non-allowlisted domain (blocked by firewall)
curl -v --connect-timeout 15 'https://www.example.com'
# Expected: TLS connection error (firewall drops after SNI inspection)
```

## Troubleshooting
<a name="vpc-webapp-troubleshooting"></a>

API calls to api.transform are blocked by your firewall  
The domain `api.transform.{{region}}.on.aws` should resolve to a private IP address via the VPC endpoint and should not reach your internet firewall.  
+ Verify you have created the `com.amazonaws.{{region}}.api.transform` endpoint.
+ Verify private DNS is enabled on the endpoint:

  ```
  aws ec2 describe-vpc-endpoints \
    --filters "Name=service-name,Values=com.amazonaws.{{region}}.api.transform" \
    --query 'VpcEndpoints[*].[State,PrivateDnsEnabled]' \
    --output table
  ```

  Expected output: `available | True`

The web application does not load (connection timeout)  
+ Verify the private subnet route table has a `0.0.0.0/0` route pointing to the firewall endpoint.
+ Verify the firewall subnet route table has a `0.0.0.0/0` route pointing to the NAT Gateway.
+ Verify the NAT Gateway is in an `available` state.

Non-allowlisted domains are not blocked  
+ Check for an IPv6 `::/0` route pointing to the internet gateway. This bypasses the firewall. Remove it (Step 12).
+ Verify symmetric routing is configured. The NAT Gateway subnet route table must have a return route through the firewall for the private subnet CIDR (Step 11).
+ Verify the firewall policy uses `STRICT_ORDER` with `drop_established` and `alert_established` as default actions.

## Cost considerations
<a name="vpc-webapp-costs"></a>


| Resource | Approximate cost | 
| --- | --- | 
| Network Firewall | \~$0.395/hr (\~$288/month) per Availability Zone | 
| NAT Gateway | \~$0.045/hr (\~$33/month) \+ data processing fees | 
| Elastic IP (public IPv4) | \~$0.005/hr (\~$3.60/month) | 
| Network Firewall data processing | $0.065/GB | 
| NAT Gateway data processing | $0.045/GB | 

Estimated base cost is approximately $325/month for a single Availability Zone deployment. For production deployments, deploy the firewall, NAT Gateway, and associated subnets in each Availability Zone where private subnets exist.

## Cleanup
<a name="vpc-webapp-cleanup"></a>

To remove all resources created by this guide, run the following commands in reverse order. Replace the placeholders with the resource IDs from your deployment. You can find these values in the AWS Management Console or by using the `describe` commands from the setup steps.

```
# Remove return route from NAT Gateway subnet
aws ec2 delete-route --route-table-id {{pub-rtb-id}} \
  --destination-cidr-block {{private-subnet-cidr}} \
  --region {{region}}

# Remove route from private subnet
aws ec2 delete-route \
  --route-table-id {{private-subnet-route-table-id}} \
  --destination-cidr-block 0.0.0.0/0 --region {{region}}

# Delete Network Firewall (takes ~5 minutes)
aws network-firewall delete-firewall \
  --firewall-name transform-webapp-firewall \
  --region {{region}}

# Delete firewall policy and rule group
aws network-firewall delete-firewall-policy \
  --firewall-policy-name transform-webapp-policy \
  --region {{region}}
aws network-firewall delete-rule-group \
  --rule-group-name transform-webapp-domains \
  --type STATEFUL --region {{region}}

# Delete NAT Gateway (wait ~5 minutes for full deletion)
aws ec2 delete-nat-gateway --nat-gateway-id {{nat-gateway-id}} \
  --region {{region}}

# Release Elastic IP
aws ec2 release-address --allocation-id {{eip-allocation-id}} \
  --region {{region}}

# Delete subnets
aws ec2 delete-subnet --subnet-id {{firewall-subnet-id}} \
  --region {{region}}
aws ec2 delete-subnet --subnet-id {{public-subnet-id}} \
  --region {{region}}
```