**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up AWS Firewall Manager​ AWS Network Firewall policies

To use AWS Firewall Manager to enable an AWS Network Firewall firewall across your organization,
perform the following steps in sequence. For information about Firewall Manager Network Firewall
policies, see [Using AWS Network Firewall policies in Firewall Manager](network-firewall-policies.md "network-firewall-policies.md").

###### Topics

- [Step 1: Completing the
  prerequisites](#complete-prereq-network-firewall "#complete-prereq-network-firewall")
- [Step 2: Creating a Network Firewall
  rule group to use in your policy](#get-started-fms-create-network-firewall-rule-group "#get-started-fms-create-network-firewall-rule-group")
- [Step 3: Creating and applying a Network Firewall policy](#get-started-fms-network-firewall-create-policy "#get-started-fms-network-firewall-create-policy")

## Step 1: Completing the

prerequisites

There are several mandatory steps to prepare your account for AWS Firewall Manager. Those steps are
described in [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). Complete all the
prerequisites before proceeding to the next step.

## Step 2: Creating a Network Firewall

rule group to use in your policy

To follow this tutorial, you should be familiar with AWS Network Firewall and know how to
configure its rule groups and firewall policies.

You must have at least one rule group in Network Firewall that will be used in your
AWS Firewall Manager policy. If you haven't already created a rule group in Network Firewall, do
so now. For information about using Network Firewall, see the [AWS Network Firewall Developer Guide](../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md "../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md").

## Step 3: Creating and applying a Network Firewall policy

After completing the prerequisites, you create an AWS Firewall Manager
Network Firewall policy. A Network Firewall policy provides a
centrally controlled AWS Network Firewall firewall for your entire AWS
organization. It also defines the AWS accounts and resources that the firewall applies
to.

For more information about how Firewall Manager manages your Network Firewall policies, see
[Using AWS Network Firewall policies in Firewall Manager](network-firewall-policies.md "network-firewall-policies.md").

###### To create a Firewall Manager Network Firewall policy (console)

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. In the navigation pane, choose **Security policies**. 3. If you haven't met the prerequisites, the console displays instructions about how to fix
any issues. Follow the instructions, and then return to this step, to create a
Network Firewall policy. 4. Choose **Create security policy**. 5. For **Policy type**, choose **AWS Network Firewall**. 6. For **Region**, choose an AWS Region. 7. Choose **Next**. 8. For **Policy name**, enter a descriptive name. 9. The policy configuration allows you to define the firewall policy. This is the same
process as the one you use in the AWS Network Firewall console. You add the
rule groups that you want to use in your policy and provide the default
stateless actions. For this tutorial, configure this policy as you would a
firewall policy in Network Firewall.

###### Note

Auto remediation happens automatically for AWS Firewall Manager Network Firewall policies, so you won't see an option to choose not to auto remediate here. 10. Choose **Next**. 11. For **Firewall endpoints**, choose **Multiple firewall
endpoints**. This option provides high availability for your
firewall. When you create the policy, Firewall Manager creates a firewall subnet in each
Availability Zone where you have public subnets to protect. 12. For **AWS Network Firewall route configuration**, choose **Monitor**
to have Firewall Manager monitor your
VPCs for route configuration violations and alert you with remediation suggestions to help you to
bring the routes into compliance. Optionally, if you don't want to have your route configurations monitored by Firewall Manager and
receive these alerts, choose **Off**.

###### Note

Monitoring provides you with details about non-compliant resources due to faulty route
configuration, and suggests remediation actions from the Firewall Manager `GetViolationDetails`
API. For example, Network Firewall alerts you if traffic is not routed through the firewall
endpoints that are created by your policy.

###### Warning

If you choose **Monitor**, you can't change it to **Off** in
the future for the same policy. You must create a new policy. 13. For **Traffic type**, select **Add to firewall policy** to route traffic through the internet gateway. 14. **AWS accounts affected by this policy** allows you to narrow the scope
of your policy by specifying accounts to include or exclude. For this tutorial,
choose **Include all accounts under my organization**.

The **Resource type** for a Network Firewall policy is always
**VPC**. 15. For **Resources**, you can narrow the scope of the policy
using tagging, by either including or excluding resources with the tags that you specify.
You can use inclusion or exclusion, and not both. For
more information about tags to define policy scope, see [Using the AWS Firewall Manager policy scope](policy-scope.md "policy-scope.md").

Resource tags can only have non-null values. If you omit the value for a tag,
Firewall Manager saves the tag with an empty string value: "". Resource tags only match with tags that have the same key
and the same value. 16. Choose **Next**. 17. For **Policy tags**, add any identifying tags that you want
to add to the Firewall Manager policy resource. For more information about tags, see [Working with Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md"). 18. Choose **Next**. 19. Review the new policy settings and return to any pages where you need to any adjustments.

Check to be sure that **Policy actions** is
set to **Identify resources that don’t comply with the policy rules, but
don’t auto remediate.** This allows you to review the changes that
your policy would make before you enable them. 20. When you are satisfied with the policy, choose **Create policy**.

In the **AWS Firewall Manager policies** pane, your policy should be
listed. It will probably indicate **Pending** under the
accounts headings and it will indicate the status of the **Automatic
remediation** setting. The creation of a policy can take
several minutes. After the **Pending** status is replaced with
account counts, you can choose the policy name to explore the compliance status
of the accounts and resources. For information, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md") 21. When you are finished exploring, if you don't want to keep the policy that you created for
this tutorial, choose the policy name, choose **Delete**,
choose **Clean up resources created by this policy.**, and
finally choose **Delete**.

For more information about Firewall Manager Network Firewall policies, see [Using AWS Network Firewall policies in Firewall Manager](network-firewall-policies.md "network-firewall-policies.md").
