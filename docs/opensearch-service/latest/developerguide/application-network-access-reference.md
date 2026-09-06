

# Network access control configuration reference for OpenSearch UI applications
<a name="application-network-access-reference"></a>

The following sections provide policy examples for each network access control that OpenSearch UI supports. Each example includes the AWS Command Line Interface (AWS CLI) commands to apply it. For an explanation of how OpenSearch UI evaluates these policies, and for a step by step walkthrough of the most common task, see [Restricting network access to OpenSearch UI applications](application-network-access.md).

Choose an example based on the scope you want to protect and the network path your users connect through:


| Scope | Control | Blocks the login page | 
| --- | --- | --- | 
| A single principal | Identity-based policy | No | 
| A single VPC endpoint | VPC endpoint policy | No | 
| Every account in an organization | Resource control policy (RCP) | Yes | 

**Note**  
Only a resource control policy that denies `opensearch:ViewLoginPage` blocks off-network users before they authenticate. Identity-based and VPC endpoint policies apply after a user signs in.

**Topics**
+ [Restricting a principal to a VPC endpoint](#application-network-access-identity-vpce)
+ [Restricting a principal to an IP address range](#application-network-access-identity-ip)
+ [Restricting access with a VPC endpoint policy](#application-network-access-endpoint-policy)
+ [Enforcing VPC endpoint access across an organization](#application-network-access-rcp-vpce)
+ [Enforcing VPC access across an organization](#application-network-access-rcp-vpc)
+ [Enforcing IP address range access across an organization](#application-network-access-rcp-ip)

## Restricting a principal to a VPC endpoint
<a name="application-network-access-identity-vpce"></a>

The following identity-based policy denies a user or role access to OpenSearch UI applications unless the request arrives through the specified interface VPC endpoint. Attach it to the IAM principal that accesses the application. Replace the {{placeholder value}} with your own VPC endpoint ID.

**To restrict a principal to a VPC endpoint**

1. Save the following policy to a local file named `policy.json`.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "DenyOpenSearchUIAccessOutsideVpce",
               "Effect": "Deny",
               "Action": "opensearch:ApplicationAccessAll",
               "Resource": "arn:aws:opensearch:*:*:application/*",
               "Condition": {
                   "StringNotEqualsIfExists": {
                       "aws:SourceVpce": "{{vpc-endpoint-id}}"
                   }
               }
           }
       ]
   }
   ```

1. Create the IAM policy.

   ```
   aws iam create-policy \
     --policy-name {{DenyOpenSearchUIOutsideVpce}} \
     --description "{{Denies OpenSearch UI access outside the approved VPC endpoint}}" \
     --policy-document file://policy.json
   ```

   The response includes the policy ARN. Note this value for the next step.

1. Attach the policy to the IAM role or user that accesses the application.

   ```
   aws iam attach-role-policy \
     --role-name {{OpenSearchUIUserRole}} \
     --policy-arn {{arn:aws:iam::111122223333:policy/DenyOpenSearchUIOutsideVpce}}
   ```

After the policy takes effect, the principal receives a `403 forbidden` response when accessing the application from outside the approved VPC endpoint. Access through the endpoint works normally.

## Restricting a principal to an IP address range
<a name="application-network-access-identity-ip"></a>

The following identity-based policy denies access unless the request originates from an approved IP address range, for example your corporate network's public egress range. Replace the {{placeholder values}} with your own IP address ranges in CIDR notation.

**To restrict a principal to an IP address range**

1. Save the following policy to a local file named `policy.json`.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "DenyOpenSearchUIAccessOutsideCorpNetwork",
               "Effect": "Deny",
               "Action": "opensearch:ApplicationAccessAll",
               "Resource": "arn:aws:opensearch:*:*:application/*",
               "Condition": {
                   "NotIpAddress": {
                       "aws:SourceIp": [
                           "{{203.0.113.0/24}}",
                           "{{198.51.100.0/24}}"
                       ]
                   }
               }
           }
       ]
   }
   ```

1. Create the IAM policy.

   ```
   aws iam create-policy \
     --policy-name {{DenyOpenSearchUIExternalAccess}} \
     --description "{{Denies OpenSearch UI access from outside corporate IP ranges}}" \
     --policy-document file://policy.json
   ```

1. Attach the policy to the IAM role or user that accesses the application.

   ```
   aws iam attach-role-policy \
     --role-name {{OpenSearchUIUserRole}} \
     --policy-arn {{arn:aws:iam::111122223333:policy/DenyOpenSearchUIExternalAccess}}
   ```

**Note**  
When a request arrives through a VPC endpoint, `aws:SourceIp` is not present. If you use both private (VPC endpoint) and public (IP-restricted) access paths, account for both condition keys in your policy so that you don't unintentionally deny legitimate VPC endpoint traffic.

## Restricting access with a VPC endpoint policy
<a name="application-network-access-endpoint-policy"></a>

An identity-based policy governs a specific principal. To control which applications users can reach *through* a VPC endpoint, regardless of which principal connects, attach a policy to the interface VPC endpoint itself. The following endpoint policy allows access only to a specific application. Replace the {{placeholder values}} with your own AWS Region, account ID, and application ID.

**To restrict access with a VPC endpoint policy**

1. Save the following policy to a local file named `policy.json`.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "AllowOpenSearchUIApplication",
               "Effect": "Allow",
               "Principal": "*",
               "Action": "opensearch:ApplicationAccessAll",
               "Resource": "arn:aws:opensearch:{{region}}:{{account-id}}:application/{{application-id}}"
           }
       ]
   }
   ```

1. Apply the policy to the interface VPC endpoint.

   ```
   aws ec2 modify-vpc-endpoint \
     --vpc-endpoint-id {{vpce-1a2b3c4d5e6f7g8h9}} \
     --policy-document file://policy.json
   ```

For more information about VPC endpoint policies for OpenSearch UI, see [Managing access to the OpenSearch UI from a VPC endpoint](application-access-ui-from-vpc-endpoint.md).

## Enforcing VPC endpoint access across an organization
<a name="application-network-access-rcp-vpce"></a>

An identity-based policy restricts a specific principal, and a VPC endpoint policy restricts a specific endpoint. To enforce network access uniformly across every account in your organization, and to block off-network users *before* they authenticate, attach a resource control policy (RCP) to your AWS organization.

The following resource control policy denies all access to OpenSearch UI applications in the organization unless the request arrives through the specified VPC endpoint. It denies both the pre-authentication login page (`opensearch:ViewLoginPage`) and authenticated access (`opensearch:ApplicationAccessAll`). Users outside the approved network can neither load the sign-in page nor access the application. Replace the {{placeholder value}} with your own VPC endpoint ID.

**To enforce VPC endpoint access across an organization**

1. Save the following policy to a local file named `policy.json`.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "DenyOpenSearchUIAccessOutsideVpce",
               "Effect": "Deny",
               "Principal": "*",
               "Action": [
                   "opensearch:ViewLoginPage",
                   "opensearch:ApplicationAccessAll"
               ],
               "Resource": "arn:aws:opensearch:*:*:application/*",
               "Condition": {
                   "StringNotEqualsIfExists": {
                       "aws:SourceVpce": "{{vpc-endpoint-id}}"
                   }
               }
           }
       ]
   }
   ```

1. Create the resource control policy. Run this command from your organization's management account or from a delegated administrator account.

   ```
   aws organizations create-policy \
     --name {{DenyOpenSearchUIOutsideVpce}} \
     --description "{{Denies OpenSearch UI access outside the approved VPC endpoint}}" \
     --type RESOURCE_CONTROL_POLICY \
     --content file://policy.json
   ```

1. Attach the policy to the organization root, an organizational unit, or an account, depending on the scope you want to protect.

   ```
   aws organizations attach-policy \
     --policy-id {{p-example12345}} \
     --target-id {{111122223333}}
   ```

   For more information, see [Attaching and detaching resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_attach.html) in the *AWS Organizations User Guide*.

After the policy takes effect, a user outside the approved VPC endpoint cannot access the application. Depending on the application's authentication type and the URL requested, the user either receives a `403 forbidden` response instead of the login page, or is redirected to sign in and is then denied access to the application. If you connect through the VPC endpoint, you reach the login page and sign in normally.

**Note**  
Changes to a resource control policy can take up to a minute to take effect. If you test immediately after you create, update, or attach a policy, you might still observe the previous behavior.

## Enforcing VPC access across an organization
<a name="application-network-access-rcp-vpc"></a>

To approve every interface VPC endpoint in a VPC instead of naming one endpoint, use `aws:SourceVpc`. The following resource control policy denies access across the organization unless the request arrives through the specified VPC. Replace the {{placeholder value}} with your own VPC ID.

**To enforce VPC access across an organization**

1. Save the following policy to a local file named `policy.json`.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "DenyOpenSearchUIAccessOutsideVpc",
               "Effect": "Deny",
               "Principal": "*",
               "Action": [
                   "opensearch:ViewLoginPage",
                   "opensearch:ApplicationAccessAll"
               ],
               "Resource": "arn:aws:opensearch:*:*:application/*",
               "Condition": {
                   "StringNotEqualsIfExists": {
                       "aws:SourceVpc": "{{vpc-id}}"
                   }
               }
           }
       ]
   }
   ```

1. Create and attach the resource control policy.

   ```
   aws organizations create-policy \
     --name {{DenyOpenSearchUIOutsideVpc}} \
     --description "{{Denies OpenSearch UI access outside the approved VPC}}" \
     --type RESOURCE_CONTROL_POLICY \
     --content file://policy.json
   
   aws organizations attach-policy \
     --policy-id {{p-example12345}} \
     --target-id {{111122223333}}
   ```

## Enforcing IP address range access across an organization
<a name="application-network-access-rcp-ip"></a>

The following resource control policy denies access across the organization unless the request originates from an approved IP address range, for example your corporate network's public egress range. Replace the {{placeholder values}} with your own IP address ranges in CIDR notation.

**To enforce IP address range access across an organization**

1. Save the following policy to a local file named `policy.json`.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "DenyOpenSearchUIAccessOutsideCorpNetwork",
               "Effect": "Deny",
               "Principal": "*",
               "Action": [
                   "opensearch:ViewLoginPage",
                   "opensearch:ApplicationAccessAll"
               ],
               "Resource": "arn:aws:opensearch:*:*:application/*",
               "Condition": {
                   "NotIpAddress": {
                       "aws:SourceIp": [
                           "{{203.0.113.0/24}}",
                           "{{198.51.100.0/24}}"
                       ]
                   }
               }
           }
       ]
   }
   ```

1. Create and attach the resource control policy.

   ```
   aws organizations create-policy \
     --name {{DenyOpenSearchUIExternalAccess}} \
     --description "{{Denies OpenSearch UI access from outside corporate IP ranges}}" \
     --type RESOURCE_CONTROL_POLICY \
     --content file://policy.json
   
   aws organizations attach-policy \
     --policy-id {{p-example12345}} \
     --target-id {{111122223333}}
   ```

**Note**  
As with the identity-based IP example, `aws:SourceIp` is not present on requests that arrive through a VPC endpoint. If you use both private and public access paths, account for both condition keys so that you don't unintentionally deny legitimate VPC endpoint traffic.