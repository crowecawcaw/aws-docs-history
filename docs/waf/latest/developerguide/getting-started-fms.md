**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up AWS Firewall Manager​ AWS WAF policies

To use AWS Firewall Manager to enable AWS WAF rules across your organization, perform the following steps
in sequence.

###### Topics

- [Step 1: Completing the prerequisites](#complete-prereq "#complete-prereq")
- [Step 2: Creating and applying an AWS WAF policy](#get-started-fms-create-security-policy "#get-started-fms-create-security-policy")
- [Step 3: Cleaning Up](#clean-up "#clean-up")

## Step 1: Completing the prerequisites

There are several mandatory steps to prepare your account for AWS Firewall Manager. Those steps are
described in [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). Complete all of
the prerequisites before proceeding to [Step 2: Creating and applying an AWS WAF policy](#get-started-fms-create-security-policy "#get-started-fms-create-security-policy").

## Step 2: Creating and applying an AWS WAF policy

A Firewall Manager AWS WAF policy contains the rule groups that you want to apply to your resources.
Firewall Manager creates a Firewall Manager web ACL in each account where you apply the policy. The individual
account managers can add rules and rule groups to the resulting web ACL, in addition to
the rule groups that you define here. For information about Firewall Manager AWS WAF policies, see
[Using AWS WAF policies with Firewall Manager](waf-policies.md "waf-policies.md").

###### To create a Firewall Manager AWS WAF policy (console)

Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

1. In the navigation pane, choose **Security policies**.
2. Choose **Create policy**.
3. For **Policy type**, choose **AWS WAF**.
4. For **Region**, choose an AWS Region. To protect Amazon CloudFront
   distributions, choose **Global**.

To protect resources in multiple Regions (other than CloudFront distributions), you
must create separate Firewall Manager policies for each Region. 5. Choose **Next**. 6. For **Policy name**, enter a descriptive name. Firewall Manager includes
the policy name in the names of the web ACLs that it manages. The web ACL names
have `FMManagedWebACLV2-` followed by the policy name that you enter
here, `-`, and the web ACL creation timestamp, in UTC milliseconds.
For example,
`FMManagedWebACLV2-MyWAFPolicyName-1621880374078`.

###### Important

Web ACL names can't change after creation. If you update your policy's name, Firewall Manager won't update the associated web ACL name. To have Firewall Manager create a web ACL with a different name, you must create a new policy. 7. Under
**Policy rules**, for **First rule
groups**, choose **Add rule groups**. Expand the
**AWS managed rule groups**. For **Core rule
set**, toggle **Add to web ACL**. For
**AWS known bad inputs**, toggle **Add to web
ACL**. Choose **Add rules**.

For **Last rule groups**, choose **Add rule
groups**. Expand the **AWS managed rule groups**
and for the **Amazon IP reputation list**, toggle **Add
to web ACL**. Choose **Add
rules**.

Under **First rule groups**, select **Core rule
set** and choose **Move down**. AWS WAF evaluates
web requests against the **AWS known bad inputs** rule group
before it evaluates against the **Core rule set**.

You can also create your own AWS WAF rule groups if you want, using the
AWS WAF console. Any rule groups that you create show up under **Your
rule groups** in the **Describe policy : Add rule
groups page**.

The first and last AWS WAF rule groups that you manage through Firewall Manager have
names that begin with `PREFMManaged-` or `POSTFMManaged-`,
respectively, followed by the Firewall Manager policy name, and the rule group creation
timestamp, in UTC milliseconds. For example,
`PREFMManaged-MyWAFPolicyName-1621880555123`. 8. Leave the default action for the web ACL at **Allow**. 9. Leave the **Policy action** at the default, to not
automatically remediate noncompliant resources. You can change the option later. 10. Choose **Next**. 11. For **Policy scope**, you provide the settings for the
accounts, resource types, and tagging that identify the resources you want to
apply the policy to. For this tutorial, leave the
**AWS accounts** and **Resources**
settings, and choose one or more resource types. 12. For **Resources**, you can narrow the scope of the policy
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
of the accounts and resources. For information, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md")

## Step 3: Cleaning Up

To avoid extraneous charges, delete any unnecessary policies and resources.

###### To delete a policy (console)

1. On the **AWS Firewall Manager policies** page, choose the radio button next to the policy name, and
   then choose **Delete**.
2. In the **Delete** confirmation box, select **Delete all policy resources**, and then choose **Delete** again.

AWS WAF removes the policy and any associated resources, like web ACLs, that it
created in your account. The changes might take a few minutes to propagate to
all accounts.
