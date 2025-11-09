# Quick Suite and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and Quick Suite by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access the Quick Suite website and APIs without leaving the Amazon network. Instances in your VPC don't need public IP addresses to communicate with Quick Suite website and APIs, but still need access to certain domains other than Quick Suite so that static assets, reports, and other files can be downloaded. For a list of domains that Quick Suite needs to access, see [Domains accessed by Quick Suite](#vpc-interface-endpoints-supported-domains "#vpc-interface-endpoints-supported-domains").

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for Quick Suite VPC

endpoints

Before you set up an interface VPC endpoint for Quick Suite, ensure that you review [Interface endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

The following considerations apply to VPC endpoint restrictions in Quick Suite:

- Quick Suite supports data sources from AWS services including Amazon S3, Amazon Redshift, and Athena. Quick Suite needs access to the resources from your AWS accounts to retrieve this data. If you want traffic to other AWS services to be routed through the VPC endpoint, you need to create VPC endpoint connections for each service that your Quick Suite account is configured to. For more information about connecting to a VPC connection with Quick Suite, see [Connecting to a VPC with Quick Suite](../user/working-with-aws-vpc.md "../user/working-with-aws-vpc.md").
- IP and VPC endpoint rules precede all other rules in Quick Suite. If you have embedded dashboards or visuals that are visible to the public (anyone on the internet) and restrict
  traffic to the Quick Suite website through a VPC endpoint, public dashboards can
  only be shared through the VPC endpoint. For more information on public
  embedding, see [Turning
  on public access to visuals and dashboards with a 1-click embed
  code](../user/embedded-analytics-1-click-public.md "../user/embedded-analytics-1-click-public.md").
- Quick Suite Website VPC endpoints are not available in China regions & Govcloud.

## Creating an interface VPC endpoint for

Quick Suite Website

You can create a VPC endpoint for the Quick Suite website using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create VPC endpoints for Quick Suite using the following service names:

- `com.amazonaws.`region`.quicksight-website` - For Quick Suite website access

The private DNS names for the Quick Suite website are not same as the public URL for Quick Suite. To reach Quick Suite through the public URL, create an A record for the website in the format `<region>.quicksight.aws.amazon.com` and point it to the VPC endpoint. For more information about routing to a VPC endpoint, see [Routing traffic to an Amazon Virtual Private Cloud interface endpoint by using your domain name](../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md "../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md").

The management of certain administrator features require that an administrator
sign in to Quick Suite as an IAM user.
If you sign in through the VPC endpoint, you need to create the following VPC endpoints
for the AWS Management Console.

- `com.amazonaws.`region`.console`
- `com.amazonaws.`region`.signin`

For more information about VPC endpoints for the AWS Management Console,
see [Required VPC endpoints and DNS configuration](../../../awsconsolehelpdocs/latest/gsg/required-endpoints-dns-configuration.md "../../../awsconsolehelpdocs/latest/gsg/required-endpoints-dns-configuration.md").

## Creating a VPC endpoint policy for

Quick Suite Website

You can attach an endpoint policy to your VPC endpoint to restrict usage of the endpoint to specific Quick Suite accounts or to accounts under specific AWS organizations. The AWS account IDs that are allow–listed or deny–listed are the AWS accounts in which the Quick Suite account is created. In most cases, this is the same account ID in which the VPC endpoint is created. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Quick Suite Website actions

The following is an example of an endpoint policy for Quick Suite. When attached
to an endpoint, this policy grants access to all Quick Suite actions for
all principals on all resources.

JSON

```
`{
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
}`

```

Policies for the Quick Suite website must have the values of the `Principal`,
`Action`, and `Resource` fields set to
`"*"`.
A condition may be specified only against the `aws:PrincipalAccount` or the
`aws:OrgId attributes`. These conditions are evaluated on all requests to
the Quick Suite website and API calls after the user signs in.

## Creating an interface VPC endpoint for Quick Suite APIs

You can create a VPC endpoint for the Quick Suite APIs using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create VPC endpoints for Quick Suite using the following service names:

- `com.amazonaws.`region`.quicksight`
- For Quick Suite API access through FIPS endpoint- `com.amazonaws.`region`.quicksight-fips`

When you create a VPC endpoint for Quick Suite APIs, the private DNS resolution automatically routes API calls to the VPC endpoint. No additional DNS configuration is required - your existing API calls to `quicksight.<region>.amazonaws.com` will automatically use the VPC endpoint when private DNS is enabled.

For more information about VPC endpoints for the AWS Management Console,
see [Required VPC endpoints and DNS configuration](../../../awsconsolehelpdocs/latest/gsg/required-endpoints-dns-configuration.md "../../../awsconsolehelpdocs/latest/gsg/required-endpoints-dns-configuration.md").

###### Following APIs are not supported via interface VPC endpoint Quick Suite API:

| API Name                           |
| ---------------------------------- |
| CreateActionConnector              |
| DeleteActionConnector              |
| DescribeActionConnector            |
| DescribeActionConnectorPermissions |
| ListActionConnectors               |
| SearchActionConnectors             |
| UpdateActionConnector              |
| UpdateActionConnectorPermissions   |
| GetFlowMetadata                    |
| GetFlowPermissions                 |
| ListFlows                          |
| SearchFlows                        |
| UpdateFlowPermissions              |

## Creating a VPC endpoint policy for Quick Suite APIs

You can attach an endpoint policy to your VPC endpoint to restrict usage of the endpoint to specific Quick Suite accounts or to accounts under specific AWS organizations. The AWS account IDs that are allow–listed or deny–listed are the AWS accounts in which the Quick Suite account is created. In most cases, this is the same account ID in which the VPC endpoint is created. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Quick Suite API actions

The following is an example of an endpoint policy for Quick Suite APIs. When attached
to an endpoint, this policy grants access to all Quick Suite actions for specific Quick Suite actions and conditions.

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

## Restricting access to the Quick Suite website

You can choose to restrict access to your Quick Suite account to only allow traffic from
an approved VPC endpoint.
This prevents general internet users from accessing your Quick Suite account. Before you
can make this change, make sure that you're an IAM user with the `UpdateIpRestriction` permission. For more information on the
permissions that are required to restrict access with a VPC endpoint, see [Turning on IP and VPC endpoint restrictions in Quick Suite](../user/enabling-ip-restrictions.md "../user/enabling-ip-restrictions.md").

Use the following procedure to restrict access with a VPC endpoint in Quick Suite.

1. Open the [Quick Suite console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. Choose **Manage Quick Suite**, and then choose **Security & permissions**.
3. On the **Security & permissions** page that opens, navigate to **IP and VPC endpoint restrictions** and choose **Manage**.
4. Turn on the **Enforce restrictions** switch to turn on your VPC endpoint restrictions.

You can also perform this action with the Quick Suite APIs. The following example turns on the enforcement of a VPC endpoint restriction.

```
aws quicksight update-ip-restriction \
--aws-account-id `AWSACCOUNTID` \
--region `REGION` \
--enabled \
--vpc-endpoint-id-restriction-rule-map `vpce-001122def=MyVpcEndpointAllowed`
```

## Domains accessed by Quick Suite

The table below lists all URLs that are accessed by Quick Suite from your browser. Make sure that you have established connectivity for all of domains listed in the table.

| URL                                   | Reason                                                                                                 | Has VPC endpoint support? |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------- |
| region.quicksight.aws.amazon.com      | The bulk of traffic to Quick Suite flows through this domain.                                          | Yes                       |
| quicksight.region.amazonaws.com       | Quick Suite public API calls.                                                                          | Yes                       |
| signin.aws.amazon.com                 | To sign in to the AWS console if the account uses IAM identities.                                      | Yes                       |
| region.signin.aws                     | To sign in to the AWS console if the account uses or Quick Suite native users for identity management. | No                        |
| \*.cloudfront.net                     | To download static assets, for example CSS or JS.                                                      | No                        |
| \*.s3.region.amazonaws.com            | To download reports and thumbnails.                                                                    | Yes                       |
| \*.execute-api.region.amazonaws.com   | To access client-side metrics.                                                                         | No                        |
| https://\*.kinesisvideo.amazonaws.com | To allow live streaming of automation workflows                                                        | No                        |
| https://apis.google.com/js/api.js     | To allow google drive file picker                                                                      | NA                        |
| https://\*.officeapps.live.com        | To allow Quick Suite side panel extenstion                                                             | NA                        |
| https://outlook.cloud.microsoft       | To allow Quick Suite side panel extenstion                                                             | NA                        |
| https://\*.sharepoint.com             | To allow Quick Suite side panel extenstion                                                             | NA                        |
| https://\*.office.com                 | To allow Quick Suite side panel extenstion                                                             | NA                        |
| https://\*.office365.com              | To allow Quick Suite side panel extenstion                                                             | NA                        |
