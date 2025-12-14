**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up AWS Firewall Manager​ DNS Firewall policies

To use AWS Firewall Manager to enable Amazon Route 53 Resolver DNS Firewall across your organization,
perform the following steps in sequence. For information about Firewall Manager DNS Firewall
policies, see [Using Amazon Route 53 Resolver DNS Firewall policies in Firewall Manager](dns-firewall-policies.md "dns-firewall-policies.md").

###### Topics

- [Step 1: Completing the
  prerequisites](#complete-prereq-dns-firewall "#complete-prereq-dns-firewall")
- [Step 2: Creating your DNS Firewall rule groups to use in your policy](#get-started-fms-create-dns-firewall-association "#get-started-fms-create-dns-firewall-association")
- [Step 3: Creating and applying a DNS Firewall policy](#get-started-fms-dns-firewall-create-policy "#get-started-fms-dns-firewall-create-policy")

## Step 1: Completing the

prerequisites

There are several mandatory steps to prepare your account for AWS Firewall Manager. Those steps are
described in [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). Complete all the
prerequisites before proceeding to the next step.

## Step 2: Creating your DNS Firewall rule groups to use in your policy

To follow this tutorial, you should be familiar with Amazon Route 53 Resolver DNS Firewall and know how to
configure its rule groups.

You must have least one rule group in DNS Firewall that will be used in your AWS Firewall Manager
policy. If you haven't already created a rule group in DNS Firewall, do so now.
For information about using DNS Firewall, see [Amazon Route 53 Resolver DNS Firewall](../../../Route53/latest/DeveloperGuide/resolver-dns-firewall.md "../../../Route53/latest/DeveloperGuide/resolver-dns-firewall.md") in the [Amazon Route 53 Developer Guide](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md").

## Step 3: Creating and applying a DNS Firewall policy

After
completing the prerequisites, you create an AWS Firewall Manager DNS Firewall policy.
A DNS Firewall policy provides a set of centrally controlled
DNS Firewall rule group associations for your entire AWS organization. It also defines the
AWS accounts and resources that the firewall applies to.

For more information about how Firewall Manager manages your DNS Firewall rule group associations, see
[Using Amazon Route 53 Resolver DNS Firewall policies in Firewall Manager](dns-firewall-policies.md "dns-firewall-policies.md").

###### To create a Firewall Manager DNS Firewall policy (console)

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").
2. In the navigation pane, choose **Security policies**.
3. If you haven't met the prerequisites, the console displays instructions about how to fix
   any issues. Follow the instructions, and then return to this step, to create a
   DNS Firewall policy.
4. Choose **Create security policy**.
5. For **Policy type**, choose **Amazon Route 53 Resolver DNS Firewall**.
6. For **Region**, choose an AWS Region.
7. Choose **Next**.
8. For **Policy name**, enter a descriptive name.
9. The policy configuration allows you to define the DNS Firewall rule group associations that you want to manage from Firewall Manager. You add the
   rule groups that you want to use in your policy. You can define an association to evaluate first for your VPCs and one to evaluate last. For this tutorial, add one or two rule
   group associations, depending on your needs.
10. Choose **Next**.
11. **AWS accounts affected by this policy** allows you to narrow the scope
    of your policy by specifying accounts to include or exclude. For this tutorial,
    choose **Include all accounts under my organization**.

The **Resource type** for a DNS Firewall policy is always
**VPC**. 12. For **Resources**, you can narrow the scope of the policy
using tagging, by either including or excluding resources with the tags that you specify.
You can use inclusion or exclusion, and not both. For
more information about tags to define policy scope, see [Using the AWS Firewall Manager policy scope](policy-scope.md "policy-scope.md").

Resource tags can only have non-null values. If you omit the value for a tag,
Firewall Manager saves the tag with an empty string value: "". Resource tags only match with tags that have the same key
and the same value. 13. Choose **Next**. 14. For **Policy tags**, add any identifying tags that you want
to add to the Firewall Manager policy resource. For more information about tags, see [Working with Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md"). 15. Choose **Next**. 16. Review the new policy settings and return to any pages where you need to any adjustments.

Check to be sure that **Policy actions** is
set to **Identify resources that don’t comply with the policy rules, but
don’t auto remediate.** This allows you to review the changes that
your policy would make before you enable them. 17. When you are satisfied with the policy, choose **Create policy**.

In the **AWS Firewall Manager policies** pane, your policy should be
listed. It will probably indicate **Pending** under the
accounts headings and it will indicate the status of the **Automatic
remediation** setting. The creation of a policy can take
several minutes. After the **Pending** status is replaced with
account counts, you can choose the policy name to explore the compliance status
of the accounts and resources. For information, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md") 18. When you are finished exploring, if you don't want to keep the policy that you created for
this tutorial, choose the policy name, choose **Delete**,
choose **Clean up resources created by this policy.**, and
finally choose **Delete**.

For more information about Firewall Manager DNS Firewall policies, see [Using Amazon Route 53 Resolver DNS Firewall policies in Firewall Manager](dns-firewall-policies.md "dns-firewall-policies.md").
