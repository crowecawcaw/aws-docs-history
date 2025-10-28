**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Setting up AWS Firewall Manager​ Amazon VPC network ACL policies

To use AWS Firewall Manager to enable network ACLs across your organization, perform the steps in this section in sequence.

For information about network ACLs, see
[Control traffic to subnets using network ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md")
in the _Amazon VPC User Guide_.

###### Topics

- [Step 1: Completing the prerequisites](#complete-prereq-network-acl "#complete-prereq-network-acl")
- [Step 2: Creating a network ACL policy](#get-started-fms-nacl-create-security-policy "#get-started-fms-nacl-create-security-policy")

## Step 1: Completing the prerequisites

There are several mandatory steps to prepare your account for AWS Firewall Manager. Those steps are
described in [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). Complete all the
prerequisites before proceeding to [Step 2: Creating a network ACL policy](#get-started-fms-nacl-create-security-policy "#get-started-fms-nacl-create-security-policy").

## Step 2: Creating a network ACL policy

After completing the prerequisites, you create a Firewall Manager network ACL policy. A network ACL policy
provides a centrally controlled network ACL definition for your entire AWS organization. It
also defines the AWS accounts and subnets that the network ACL applies to.

For information about Firewall Manager network ACL policies, see [Network ACL policies](network-acl-policies.md "network-acl-policies.md").

For general information about Firewall Manager network ACL policies, see
[Network ACL policies](network-acl-policies.md "network-acl-policies.md").

###### Note

For this tutorial, you won't apply your network ACL policy to the subnets in your
organization. You'll just create the policy and see what would happen if you applied
the policy's network ACL to your subnets. You do this by disabling automatic
remediation on the policy.

###### To create a Firewall Manager network ACL policy (console)

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. In the navigation pane, choose **Security policies**. 3. If you have not met the prerequisites, the console displays instructions about how to fix
any issues. Follow the instructions, and then return to this step, to create a
network ACL policy. 4. Choose **Create policy**. 5. For **Region**, choose an AWS Region. 6. For **Policy type**, choose **Network ACL**. 7. Choose **Next**. 8. For **Policy name**, enter a descriptive name. 9. For **Network ACL policy rules**, define the first and last rules for both inbound
and outbound traffic.

You define network ACL rules in Firewall Manager similar to how you define them through Amazon VPC. The only difference is that,
instead of assigning rule numbers yourself, you assign the order to run each set of rules, and then Firewall Manager assigns
the numbers for you when you save the policy.
You can define up to 5 inbound rules, divided in any way between first and last, and
you can define up to 5 outbound rules.

For guidance specifying network ACL rules, see
[Add and delete network ACL rules](../../../vpc/latest/userguide/vpc-network-acls.md#Rules "../../../vpc/latest/userguide/vpc-network-acls.md#Rules")
in the _Amazon VPC User Guide_.

The rules that you define in the Firewall Manager policy specify the minimum rule configuration that a network ACL must have to be compliant with
the network ACL policy. For example, a network ACL's inbound rules cannot be compliant with the policy unless they start
with as the policy's inbound first rules, in the same order as they're specified in the policy. For more information,
see [Network ACL policies](network-acl-policies.md "network-acl-policies.md"). 10. For **Policy action**, choose **Identify resources
that don’t comply with the policy rules, but don’t auto
remediate.** 11. Choose **Next**. 12. **AWS accounts affected by this policy** allows you to narrow
the scope of your policy by specifying accounts to include or exclude. For this
tutorial, choose **Include all accounts under my
organization.**

The **Resource type** for a network ACL policy is always subnet. 13. For **Resources**, you can narrow the scope of the policy
using tagging, by either including or excluding resources with the tags that you specify.
You can use inclusion or exclusion, and not both. For
more information about tags to define policy scope, see [Using the AWS Firewall Manager policy scope](policy-scope.md "policy-scope.md").

Resource tags can only have non-null values. If you omit the value for a tag,
Firewall Manager saves the tag with an empty string value: "". Resource tags only match with tags that have the same key
and the same value. 14. Choose **Next**. 15. For **Policy tags**, add any identifying tags that you want
to add to the Firewall Manager policy resource. For more information about tags, see [Working with Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md"). 16. Choose **Next**. 17. Review the new policy settings and return to any pages where you need to any adjustments.

Check to be sure that **Policy actions** is
set to **Identify resources that don’t comply with the policy rules, but
don’t auto remediate.** This allows you to review the changes that
your policy would make before you enable them. 18. When you are satisfied with the policy, choose **Create policy**.

In the **AWS Firewall Manager policies** pane, your policy should be
listed. It will probably indicate **Pending** under the
accounts headings and it will indicate the status of the **Automatic
remediation** setting. The creation of a policy can take
several minutes. After the **Pending** status is replaced with
account counts, you can choose the policy name to explore the compliance status
of the accounts and resources. For information, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md") 19. When you are finished exploring, if you don't want to keep the policy that you created for this
tutorial, choose the policy name, choose **Delete**, choose
**Clean up resources created by this policy.**, and finally
choose **Delete**.

For more information about Firewall Manager network ACL policies, see [Network ACL policies](network-acl-policies.md "network-acl-policies.md").
