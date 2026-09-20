

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# VPC endpoint policies for AWS Wickr
<a name="vpce-policy"></a>

A VPC endpoint policy is an IAM resource policy that you attach to a VPC endpoint to control which resources and actions are accessible through that endpoint. You can attach VPC endpoint policies to Wickr Messaging and Wickr Admin endpoints.

For Wickr Messaging endpoints, VPC endpoint policies enable you to enforce data perimeter controls. For example, you can restrict which Wickr networks are reachable through a VPC endpoint so that users can't connect to unauthorized networks. For Wickr Admin endpoints, VPC endpoint policies support the same network and condition controls as Messaging, and additionally allow you to control which specific administrative actions are permitted through the endpoint.

**Note**  
VPC endpoint policies are not supported for Wickr Calling endpoints. However, Wickr Calling depends on Wickr Messaging to exchange encryption keys and other call setup information. If your Wickr Messaging VPC endpoint policy blocks access to a network, you can't initiate or receive calls on that network through the messaging endpoint.

For more information about VPC endpoints, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

## Considerations
<a name="vpce-policy-considerations"></a>
+ VPC endpoint policies apply to all users and traffic passing through the endpoint. They don't replace other access controls such as Wickr network security settings or IAM policies.
+ If you attach a policy that denies all access, no users can access Wickr through that VPC endpoint.
+ Policy changes can take a few minutes to take effect. Avoid immediately re-testing after a change.
+ For Wickr Messaging, VPC endpoint policies are evaluated against data plane actions, which include messaging, file transfer, and call signaling. Pre-login requests such as user registration are evaluated without matching a specific network resource.
+ For Wickr Messaging, only the wildcard action (`wickr:*`) is supported. Individual messaging actions can't be specified.

**Topics**
+ [Considerations](#vpce-policy-considerations)
+ [VPC endpoint policies for Wickr Messaging](#vpce-policy-messaging)
+ [VPC endpoint policies for Wickr Admin](#vpce-policy-admin)
+ [Default VPC endpoint policy](#vpce-policy-default)
+ [Create a VPC endpoint policy for Wickr](#vpce-policy-attach)

## VPC endpoint policies for Wickr Messaging
<a name="vpce-policy-messaging"></a>

For Wickr Messaging endpoints, VPC endpoint policies enable you to enforce data perimeter controls. For example, you can attach a VPC endpoint policy that permits access only to your organization's Wickr networks.

### Policy elements for Wickr Messaging
<a name="vpce-policy-messaging-elements"></a>

The following elements are supported in VPC endpoint policies for Wickr Messaging:

Principal  
Use the wildcard principal (`"*"`). The policy applies to all traffic passing through the VPC endpoint, regardless of the caller's identity.

Action  
Use the wildcard action `wickr:*`. Individual messaging actions are not supported in VPC endpoint policies for Wickr Messaging. The wildcard action applies the policy to all Wickr Messaging data plane actions, including sending messages, transferring files, and initiating calls.

Resource  
Specify a Wickr network resource by using the following Amazon Resource Name (ARN) format:  

```
arn:aws:wickr:{{region}}:{{account-id}}:network/{{network-id}}
```
To find your network ID and account ID, navigate to the Wickr console and view your network details. You can also use a wildcard (`"*"`) to match all networks.

Effect  
Use `Allow` or `Deny` to permit or restrict access to the specified resources.

Condition  
The following condition keys are supported:  
+ `aws:SourceVpc` – Restricts access to requests originating from the specified VPC.
+ `aws:SourceVpce` – Restricts access to requests made through the specified VPC endpoint.
+ `aws:VpceAccount` – Restricts access to requests from VPC endpoints owned by the specified AWS account.

### Example VPC endpoint policies for Wickr Messaging
<a name="vpce-policy-messaging-examples"></a>

The following are example VPC endpoint policies for Wickr Messaging.

#### Restrict access to a specific Wickr network
<a name="vpce-policy-restrict-network"></a>

The following VPC endpoint policy allows access only to the Wickr network with the specified network ID. All traffic to other Wickr networks through this endpoint is denied.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": "wickr:*",
            "Resource": "arn:aws:wickr:{{us-east-1}}:{{123456789012}}:network/{{12345678}}"
        }
    ]
}
```

#### Restrict access to a specific VPC
<a name="vpce-policy-restrict-vpc"></a>

The following VPC endpoint policy allows access to a Wickr network only if the request originates from the specified VPC. This is useful when you have multiple VPC endpoints configured and you want to restrict which VPCs can reach your Wickr network.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": "wickr:*",
            "Resource": "arn:aws:wickr:{{us-east-1}}:{{123456789012}}:network/{{12345678}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceVpc": "{{vpc-1a2b3c4d}}"
                }
            }
        }
    ]
}
```

#### Restrict access to a specific VPC endpoint
<a name="vpce-policy-restrict-vpce"></a>

The following VPC endpoint policy allows access to a Wickr network only through the specified VPC endpoint. This is useful when you have multiple VPC endpoints and you want to limit which endpoint can be used to reach a specific Wickr network.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": "wickr:*",
            "Resource": "arn:aws:wickr:{{us-east-1}}:{{123456789012}}:network/{{12345678}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceVpce": "{{vpce-0abcdef1234567890}}"
                }
            }
        }
    ]
}
```

#### Deny access to all Wickr networks except a specific network
<a name="vpce-policy-deny-other-networks"></a>

The following VPC endpoint policy denies access to all Wickr networks except the specified network. This is useful when you want to ensure that only your organization's Wickr network is accessible through the VPC endpoint, and all other networks are blocked. Unlike the allow-only policy, this explicit deny can't be overridden by other policy statements.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Deny",
            "Action": "wickr:*",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:SourceVpce": "{{vpce-0abcdef1234567890}}"
                }
            }
        },
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": "wickr:*",
            "Resource": "arn:aws:wickr:{{us-east-1}}:{{123456789012}}:network/{{12345678}}"
        }
    ]
}
```

The first statement denies all Wickr actions when the request doesn't come from the specified VPC endpoint. The second statement allows access to the specified Wickr network. Together, these statements ensure that only the specified network is accessible, and only through the specified VPC endpoint.

#### Restrict access with multiple conditions
<a name="vpce-policy-multiple-conditions"></a>

The following VPC endpoint policy allows access to a Wickr network only when all specified conditions are met: the request must originate from a specific VPC, through a specific VPC endpoint, and from a VPC endpoint owned by a specific AWS account.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": "wickr:*",
            "Resource": "arn:aws:wickr:{{us-east-1}}:{{123456789012}}:network/{{12345678}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceVpc": "{{vpc-1a2b3c4d}}",
                    "aws:SourceVpce": "{{vpce-0abcdef1234567890}}",
                    "aws:VpceAccount": "{{123456789012}}"
                }
            }
        }
    ]
}
```

## VPC endpoint policies for Wickr Admin
<a name="vpce-policy-admin"></a>

For Wickr Admin endpoints, VPC endpoint policies support all the same policy elements as Wickr Messaging, including network resource restrictions and condition keys (`aws:SourceVpc`, `aws:SourceVpce`, `aws:VpceAccount`). In addition, Wickr Admin supports specific action-level controls. You can use the wildcard action `wickr:*` to allow or deny all actions, or specify individual Wickr Admin actions. For a complete list of Wickr actions, see [Actions defined by AWS Wickr](https://docs.aws.amazon.com/service-authorization/latest/reference/list_wickr.html#list_wickr-actions-as-permissions) in the *Service Authorization Reference*.

### Example VPC endpoint policies for Wickr Admin
<a name="vpce-policy-admin-examples"></a>

**Restrict access to a specific Wickr network**  
The following VPC endpoint policy allows all Wickr Admin actions, but only for the specified network resource.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": "wickr:*",
            "Resource": "arn:aws:wickr:{{us-east-1}}:{{123456789012}}:network/{{12345678}}"
        }
    ]
}
```

**Allow only read-only access to a specific Wickr network**  
The following VPC endpoint policy allows only read-only Wickr Admin actions on a specific network through the endpoint. Write operations such as creating or deleting networks are not permitted.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": [
                "wickr:ListNetworks",
                "wickr:GetNetwork",
                "wickr:GetNetworkSettings",
                "wickr:ListUsers",
                "wickr:GetUser",
                "wickr:GetUsersCount"
            ],
            "Resource": "arn:aws:wickr:{{us-east-1}}:{{123456789012}}:network/{{12345678}}"
        }
    ]
}
```

## Default VPC endpoint policy
<a name="vpce-policy-default"></a>

If you don't attach a custom policy to a VPC endpoint, the default endpoint policy is applied. The default policy allows full access to Wickr through the endpoint.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

To restrict access, attach a custom endpoint policy to the VPC endpoint.

## Create a VPC endpoint policy for Wickr
<a name="vpce-policy-attach"></a>

You can create and attach a VPC endpoint policy when you create a VPC endpoint, or you can attach a policy to an existing VPC endpoint.

**Attach a VPC endpoint policy using the AWS Management Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the left navigation pane, choose **Endpoints**.

1. Select the Wickr VPC endpoint (Wickr Messaging or Wickr Admin).

1. Choose the **Policy** tab, then choose **Edit policy**.

1. Choose **Custom**, and enter your endpoint policy.

1. Choose **Save**.

**Attach a VPC endpoint policy using the AWS CLI**

Use the `modify-vpc-endpoint` command to attach a policy to an existing VPC endpoint.

```
aws ec2 modify-vpc-endpoint \
    --vpc-endpoint-id {{vpce-0abcdef1234567890}} \
    --policy-document file://{{policy.json}}
```

Replace {{vpce-0abcdef1234567890}} with the ID of your Wickr VPC endpoint, and {{policy.json}} with the path to your endpoint policy JSON file.