

# Quick and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and Quick by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access the Quick website and APIs without leaving the Amazon network. Instances in your VPC don't need public IP addresses to communicate with Quick website and APIs, but still need access to certain domains other than Quick so that static assets, reports, and other files can be downloaded. For a list of domains that Quick needs to access, see [Domains accessed by Quick](#vpc-interface-endpoints-supported-domains).

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

## Considerations for Quick VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Quick, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

The following considerations apply to VPC endpoint restrictions in Quick:
+ Quick supports data sources from AWS services including Amazon S3, Amazon Redshift, and Athena. Quick needs access to the resources from your AWS accounts to retrieve this data. If you want traffic to other AWS services to be routed through the VPC endpoint, you need to create VPC endpoint connections for each service that your Quick account is configured to. For more information about connecting to a VPC connection with Quick, see [Connecting to a VPC with Quick](https://docs.aws.amazon.com/quicksight/latest/user/working-with-aws-vpc.html).
+ IP and VPC endpoint rules precede all other rules in Quick. If you have embedded dashboards or visuals that are visible to the public (anyone on the internet) and restrict traffic to the Quick website through a VPC endpoint, public dashboards can only be shared through the VPC endpoint. For more information on public embedding, see [Turning on public access to visuals and dashboards with a 1-click embed code](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-1-click-public.html).
+ Quick Website VPC endpoints are not available in China regions & Govcloud.

## Creating an interface VPC endpoint for Quick Website
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the Quick website using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create VPC endpoints for Quick using the following service names: 
+ `com.amazonaws.{{region}}.quicksight-website` - For Quick website access

The private DNS names for the Quick website are not same as the public URL for Quick. To reach Quick through the public URL, create an A record for the website in the format `<region>.quicksight.aws.amazon.com` and point it to the VPC endpoint. For more information about routing to a VPC endpoint, see [Routing traffic to an Amazon Virtual Private Cloud interface endpoint by using your domain name](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html).

The management of certain administrator features require that an administrator sign in to Quick as an IAM user. If you sign in through the VPC endpoint, you need to create the following VPC endpoints for the AWS Management Console.
+ `com.amazonaws.{{region}}.console`
+ `com.amazonaws.{{region}}.signin`

For more information about VPC endpoints for the AWS Management Console, see [Required VPC endpoints and DNS configuration](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/required-endpoints-dns-configuration.html).

## Creating a VPC endpoint policy for Quick Website
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint to restrict usage of the endpoint to specific Quick accounts or to accounts under specific AWS organizations. The AWS account IDs that are allow–listed or deny–listed are the AWS accounts in which the Quick account is created. In most cases, this is the same account ID in which the VPC endpoint is created. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for Quick Website actions**  
The following is an example of an endpoint policy for Quick. When attached to an endpoint, this policy grants access to all Quick actions for all principals on all resources.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalAccount": [
                        "012345678901"
                    ]
                }
            }
        }
    ]
}
```

------

Policies for the Quick website must have the values of the `Principal`, `Action`, and `Resource` fields set to `"*"`. A condition may be specified only against the `aws:PrincipalAccount` or the `aws:OrgId attributes`. These conditions are evaluated on all requests to the Quick website and API calls after the user signs in.

## Creating an interface VPC endpoint for Quick APIs
<a name="vpc-endpoint-create-apis"></a>

You can create a VPC endpoint for the Quick APIs using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create VPC endpoints for Quick using the following service names: 
+ `com.amazonaws.{{region}}.quicksight`
+ For Quick API access through FIPS endpoint- `com.amazonaws.{{region}}.quicksight-fips`

When you create a VPC endpoint for Quick APIs, the private DNS resolution automatically routes API calls to the VPC endpoint. No additional DNS configuration is required - your existing API calls to `quicksight.<region>.amazonaws.com` will automatically use the VPC endpoint when private DNS is enabled.

For more information about VPC endpoints for the AWS Management Console, see [Required VPC endpoints and DNS configuration](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/required-endpoints-dns-configuration.html).

**APIs listed in the [CLI reference](https://docs.aws.amazon.com/cli/latest/reference/quicksight/) are supported via interface VPC endpoint Quick APIs except the ones listed below:**  



| API Name | 
| --- | 
| CreateActionConnector | 
| DeleteActionConnector | 
| DescribeActionConnector | 
| DescribeActionConnectorPermissions | 
| ListActionConnectors | 
| SearchActionConnectors | 
| UpdateActionConnector | 
| UpdateActionConnectorPermissions | 
| GetFlowMetadata | 
| GetFlowPermissions | 
| ListFlows | 
| SearchFlows | 
| UpdateFlowPermissions | 

## Creating a VPC endpoint policy for Quick APIs
<a name="vpc-endpoint-policy-apis"></a>

You can attach an endpoint policy to your VPC endpoint to restrict usage of the endpoint to specific Quick accounts or to accounts under specific AWS organizations. The AWS account IDs that are allow–listed or deny–listed are the AWS accounts in which the Quick account is created. In most cases, this is the same account ID in which the VPC endpoint is created. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for Quick API actions**  
The following is an example of an endpoint policy for Quick APIs. When attached to an endpoint, this policy grants access to all Quick actions for specific Quick actions and conditions.

```
{  
    "Version":"2012-10-17",		 	 	   
    "Statement": [  
        {  
            "Effect": "Allow",  
            "Principal": "*",  
            "Action": [  
                "quicksight:DescribeUser",  
                "quicksight:ListUsers"
            ],  
            "Resource": "*",  
            "Condition": {  
                "StringEquals": {  
                    "aws:PrincipalAccount": [  
                        "012345678901"  
                    ]  
                }  
            }  
        }  
    ]  
}
```

## Restricting access to the Quick website
<a name="vpc-interface-endpoints-restrict"></a>

You can choose to restrict access to your Quick account to only allow traffic from an approved VPC endpoint. This prevents general internet users from accessing your Quick account. Before you can make this change, make sure that you're an IAM user with the `UpdateIpRestriction` permission. For more information on the permissions that are required to restrict access with a VPC endpoint, see [Turning on IP and VPC endpoint restrictions in Quick](https://docs.aws.amazon.com/quicksight/latest/user/enabling-ip-restrictions.html).

Use the following procedure to restrict access with a VPC endpoint in Quick.

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Choose **Manage Quick**, and then choose **Security & permissions**.

1. On the **Security & permissions** page that opens, navigate to **IP and VPC endpoint restrictions** and choose **Manage**.

1. Turn on the **Enforce restrictions** switch to turn on your VPC endpoint restrictions.

You can also perform this action with the Quick APIs. The following example turns on the enforcement of a VPC endpoint restriction.

```
aws quicksight update-ip-restriction \
--aws-account-id {{AWSACCOUNTID}} \
--region {{REGION}} \
--enabled \
--vpc-endpoint-id-restriction-rule-map {{vpce-001122def=MyVpcEndpointAllowed}}
```

## Domains accessed by Quick
<a name="vpc-interface-endpoints-supported-domains"></a>

The table below lists all URLs that are accessed by Quick from your browser. Make sure that you have established connectivity for all of domains listed in the table.


| URL | Reason | Has VPC endpoint support? | 
| --- | --- | --- | 
| region.quicksight.aws.amazon.com | The bulk of traffic to Quick flows through this domain. | Yes | 
| quicksight.region.amazonaws.com | Quick public API calls. | Yes | 
| signin.aws.amazon.com | To sign in to the AWS console if the account uses IAM identities. | Yes | 
| region.signin.aws | To sign in to the AWS console if the account uses or Quick native users for identity management. | No | 
| \*.cloudfront.net | To download static assets, for example CSS or JS. | No | 
| \*.s3.region.amazonaws.com | To download reports and thumbnails. | Yes | 
| \*.execute-api.region.amazonaws.com | To access client-side metrics. | No | 
| https://\*.kinesisvideo.amazonaws.com | To allow live streaming of automation workflows | No | 
| https://apis.google.com/js/api.js | To allow google drive file picker | NA | 
| https://\*.officeapps.live.com | To allow Quick side panel extenstion | NA | 
| https://outlook.cloud.microsoft | To allow Quick side panel extenstion | NA | 
| https://\*.sharepoint.com | To allow Quick side panel extenstion | NA | 
| https://\*.office.com | To allow Quick side panel extenstion | NA | 
| https://\*.office365.com | To allow Quick side panel extenstion | NA | 