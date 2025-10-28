# Integrate Verified Access with AWS WAF

In addition to the authentication and authorization rules enforced by Verified Access, you might also
want to apply perimeter protection. This can help you protect your applications from additional
threats. You can accomplish this by integrating AWS WAF into your Verified Access deployment. AWS WAF
is a web application firewall that lets you monitor the HTTP requests that are forwarded to
your protected web application resources. For more information, see the [AWS WAF Developer Guide](../../../waf/latest/developerguide.md "../../../waf/latest/developerguide.md").

You can integrate AWS WAF with Verified Access by associating an AWS WAF web access control list (ACL)
with a Verified Access instance. A web ACL is a AWS WAF resource that gives you fine-grained control over all
of the HTTP web requests that your protected resource responds to. While the AWS WAF association
or disassociation request is being processed, the status of any Verified Access endpoints attached to the
instance are shown as `updating`. After the request is complete, the status returns to
`active`. You can view the status in the AWS Management Console or by describing the endpoint with
the AWS CLI.

The user-identity trust provider determines when AWS WAF inspects the traffic. If you use IAM Identity Center,
AWS WAF inspects the traffic before user authentication. If you use OpenID Connect (OIDC), AWS WAF
inspects the traffic after user authentication.

###### Contents

- [Required IAM permissions](#waf-permissions "#waf-permissions")
- [Associate an AWS WAF web ACL](#associate-web-acl "#associate-web-acl")
- [Check the status of the association](#waf-integration-status "#waf-integration-status")
- [Disassociate an AWS WAF web ACL](#disassociate-web-acl "#disassociate-web-acl")

## Required IAM permissions

Integrating AWS WAF with Verified Access includes permission-only actions that don't directly
correspond to an API operation. These actions are indicated in the AWS Identity and Access Management
_Service Authorization Reference_ with `[permission only]`. See [Actions,
resources, and condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md") in the
_Service Authorization Reference_.

To work with a web ACL, your AWS Identity and Access Management principal must have the following permissions.

- `ec2:AssociateVerifiedAccessInstanceWebAcl`
- `ec2:DisassociateVerifiedAccessInstanceWebAcl`
- `ec2:DescribeVerifiedAccessInstanceWebAclAssociations`
- `ec2:GetVerifiedAccessInstanceWebAcl`

## Associate an AWS WAF web ACL

The following steps demonstrate how to associate an AWS WAF web access control list (ACL)
with a Verified Access instance using the Verified Access console.

###### Prerequisite

Before you begin, create a AWS WAF web ACL. For more information, see
[Create a web ACL](../../../waf/latest/developerguide/web-acl-creating.md "../../../waf/latest/developerguide/web-acl-creating.md")
in the _AWS WAF Developer Guide_.

###### To associate an AWS WAF web ACL to a Verified Access instance

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access instances**.
3. Select the Verified Access instance.
4. Select the **Integrations** tab.
5. Choose **Actions**, then **Associate Web ACL**.
6. For **Web ACL**, choose an existing web ACL, then choose
   **Associate Web ACL**.

Alternatively, you can use the AWS WAF console. If you use the AWS WAF console or API, you need the
Amazon Resource Name (ARN) of your Verified Access instance. An AVA ARN has the following format:
`arn:${Partition}:ec2:${Region}:${Account}:verified-access-instance/${VerifiedAccessInstanceId}`.
For more information, see [Associate a web ACL with an AWS resource](../../../waf/latest/developerguide/web-acl-associating.md "../../../waf/latest/developerguide/web-acl-associating.md")
in the _AWS WAF Developer Guide_.

## Check the status of the association

You can verify whether an AWS WAF web access control list (ACL) is associated with a
Verified Access instance or not by using the Verified Access console.

###### To view the status of AWS WAF integration with a Verified Access instance

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access instances**.
3. Select the Verified Access instance.
4. Select the **Integrations** tab.
5. Check the details listed under **WAF integration status**. The status
   will be shown as **Associated** or **Not associated**, along
   with the web ACL identifier, if in the **Associated** state.

## Disassociate an AWS WAF web ACL

The following steps demonstrate how to disassociate an AWS WAF web access control list
(ACL) from a Verified Access instance using the Verified Access console.

###### To disassociate an AWS WAF web ACL from a Verified Access instance

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access instances**.
3. Select the Verified Access instance.
4. Select the **Integrations** tab.
5. Choose **Actions**, then **Disassociate Web ACL**.
6. Confirm by choosing **Disassociate Web ACL**.

Alternatively, you can use the AWS WAF console. For more information, see [Disassociate a web ACL from an AWS resource](../../../waf/latest/developerguide/web-acl-dissociating-aws-resource.md "../../../waf/latest/developerguide/web-acl-dissociating-aws-resource.md")
in the _AWS WAF Developer Guide_.
