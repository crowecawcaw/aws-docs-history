# Associating an AWS WAF web ACL with your service

AWS WAF is a web application firewall that you can use to secure your App Runner service. With AWS WAF web access control lists (web ACLs), you can guard your
App Runner service endpoints against common web exploits and unwanted bots.

A web ACL provides you with fine-grained control over all incoming web requests to your App Runner service. You can define rules in a web ACL to allow, block,
or monitor web traffic, to ensure that only authorized and legitimate requests reach your web applications and APIs. You can customize the web ACL rules
based on your specific business and security needs. To learn more about infrastructure security and best practices for applying network ACLs, see [Control network traffic](../../../vpc/latest/userguide/infrastructure-security.md#control-network-traffic "../../../vpc/latest/userguide/infrastructure-security.md#control-network-traffic") in the
_Amazon VPC User Guide_.

###### Important

Source IP rules for App Runner private services that are associated with WAF web ACLs _do not adhere to IP based rules_. This is
because we currently don't support forwarding request source IP data to App Runner private services associated with WAF. If your App Runner application requires source
IP/CIDR incoming traffic control rules, you must use [security group rules for private endpoints](network-pl-manage.md "network-pl-manage.md") instead of WAF web
ACLs.

## Incoming web request flow

When an AWS WAF web ACL is associated with an App Runner service, incoming web requests go through the following process:

1. App Runner forwards the contents of the origin request to AWS WAF.
2. AWS WAF inspects the request and compares its contents to the rules that you specified in your web ACL.
3. Based on its inspection, AWS WAF returns an `allow` or `block` response to App Runner.
   - If an `allow` response is returned, App Runner forwards the request to your application.
   - If a `block` response is returned, App Runner blocks the request from reaching your web application. It forwards the `block`
     response from AWS WAF to your application.

   ###### Note

   By default App Runner blocks the request if no response is returned from AWS WAF.

For more information about AWS WAF web ACLs, see [Web access control lists (web ACLs)](../../../waf/latest/developerguide/web-acl.md "../../../waf/latest/developerguide/web-acl.md") in the
_AWS WAF Developer Guide_.

###### Note

You pay standard AWS WAF pricing. You don't incur any additional costs for using AWS WAF web ACLs for your App Runner services.
For more information about
pricing, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing "https://aws.amazon.com/waf/pricing").

## Associating WAF web ACLs to your App Runner service

The following is the high-level process to associate an AWS WAF web ACL with your App Runner service:

1. Create a web ACL in the AWS WAF console. For more information, see [Creating a web ACL](../../../waf/latest/developerguide/web-acl-creating.md "../../../waf/latest/developerguide/web-acl-creating.md") in the
   _AWS WAF Developer Guide_.
2. Update your AWS Identity and Access Management (IAM) permissions for AWS WAF. For more information, see [Permissions](#waf.permissions "#waf.permissions").
3. Associate the web ACL with the App Runner service using one of the following methods:
   - **App Runner console**: Associate an existing web ACL using App Runner console when you [create](manage-create.md "manage-create.md") or
     [update](manage-configure.md "manage-configure.md") an App Runner service. For instructions, see [Managing AWS WAF web ACLs](waf-manage.md "waf-manage.md").
   - **AWS WAF console**: Associate the web ACL using the AWS WAF console for an existing App Runner service. For more information, see
     [Associating or disassociating a web ACL with an AWS resource](../../../waf/latest/developerguide/web-acl-associating-aws-resource.md "../../../waf/latest/developerguide/web-acl-associating-aws-resource.md") in the
     _AWS WAF Developer Guide_.
   - **AWS CLI**: Associate the web ACL using the AWS WAF public APIs. For more information about AWS WAF public APIs, see [AssociateWebACL](../../../waf/latest/APIReference/API_AssociateWebACL.md "../../../waf/latest/APIReference/API_AssociateWebACL.md") in the _AWS WAF API Reference Guide_.

## Considerations

- Source IP rules for App Runner private services that are associated with WAF web ACLs _do not adhere to IP based rules_. This is
  because we currently don't support forwarding request source IP data to App Runner private services associated with WAF. If your App Runner application requires source
  IP/CIDR incoming traffic control rules, you must use [security group rules for private endpoints](network-pl-manage.md "network-pl-manage.md") instead of WAF web
  ACLs.
- An App Runner service can be associated with only one web ACL. However, you can associate one web ACL with multiple App Runner services and with multiple
  AWS resources. Examples include Amazon Cognito user pools and Application Load Balancer resources.
- When you create a web ACL, a small amount of time passes before the web ACL fully propagates and is available to App Runner.
  The propagation time can be from a few seconds to a number of minutes.
  AWS WAF returns a `WAFUnavailableEntityException` when you try to associate a web ACL before it has fully propagated.

If you refresh the browser or navigate away from the App Runner console before the web ACL is fully propagated, the association fails to occur. However, you
can navigate within the App Runner console.

- AWS WAF returns a `WAFNonexistentItemException` error when you call one of the following AWS WAF APIs for an App Runner service which is in an
  invalid state:

      + `AssociateWebACL`
      + `DisassociateWebACL`
      + `GetWebACLForResource`

  The invalid states for your App Runner service include:

      + `CREATE_FAILED`
      + `DELETE_FAILED`
      + `DELETED`
      + `OPERATION_IN_PROGRESS`



      ###### Note

      `OPERATION_IN_PROGRESS` state is invalid only if your App Runner service is being deleted.

- Your request might result in a payload that is larger than the limits of what AWS WAF can inspect. For more information about how AWS WAF handles
  oversize requests from App Runner, see [Oversize request component handling](../../../waf/latest/developerguide/waf-rule-statement-oversize-handling.md "../../../waf/latest/developerguide/waf-rule-statement-oversize-handling.md") in
  the _AWS WAF Developer Guide_ to learn how AWS WAF handles oversize requests from App Runner.
- If you don’t set appropriate rules or your traffic patterns change, a web ACL might not be as effective at securing your application.

## Permissions

To work with a web ACL in AWS App Runner, add the following IAM permissions for AWS WAF:

- `apprunner:ListAssociatedServicesForWebAcl`
- `apprunner:DescribeWebAclForService`
- `apprunner:AssociateWebAcl`
- `apprunner:DisassociateWebAcl`

For more information about IAM permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
_IAM User Guide_.

The following is an example of the updated IAM policy for AWS WAF. This IAM policy includes the necessary permissions to work with an App Runner
service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "wafv2:ListResourcesForWebACL",
 "wafv2:GetWebACLForResource",
 "wafv2:AssociateWebACL",
 "wafv2:DisassociateWebACL",
 "apprunner:ListAssociatedServicesForWebAcl",
 "apprunner:DescribeWebAclForService",
 "apprunner:AssociateWebAcl",
 "apprunner:DisassociateWebAcl"
 ],
 "Resource":"*"
 }
 ]
}`

```

###### Note

Though you must grant IAM permissions, the listed actions are permission-only and don't correspond to an API operation.
