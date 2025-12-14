**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up AWS Firewall Manager​ Amazon VPC security

group policies

To use AWS Firewall Manager to enable Amazon VPC security groups across your organization, perform the following steps
in sequence.

###### Topics

- [Step 1: Completing the prerequisites](#complete-prereq-security-group "#complete-prereq-security-group")
- [Step 2: Creating a security group to use
  in your policy](#get-started-fms-create-security-groups "#get-started-fms-create-security-groups")
- [Step 3: Creating and applying a common security group policy](#get-started-fms-sg-create-security-policy "#get-started-fms-sg-create-security-policy")

## Step 1: Completing the prerequisites

There are several mandatory steps to prepare your account for AWS Firewall Manager. Those steps are
described in [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). Complete all the
prerequisites before proceeding to [Step 2: Creating a security group to use
in your policy](#get-started-fms-create-security-groups "#get-started-fms-create-security-groups").

## Step 2: Creating a security group to use

in your policy

In this step, you create a security group that you could apply across your organization
using Firewall Manager.

###### Note

For this tutorial, you won't apply your security group policy to the resources in your
organization. You'll just create the policy and see what would happen if you applied
the policy's security group to your resources. You do this by disabling automatic
remediation on the policy.

If you already have a general security group defined, skip this step and go to [Step 3: Creating and applying a common security group policy](#get-started-fms-sg-create-security-policy "#get-started-fms-sg-create-security-policy").

###### To create a security group to use in a Firewall Manager common

security group policy

- Create a security group that you could apply to all accounts and resources in your
  organization, following the guidance under [Security Groups for Your
  VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

For information on the security group rules options, see
[Security Group Rules Reference](../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md "../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md").

You are now ready to go to [Step 3: Creating and applying a common security group policy](#get-started-fms-sg-create-security-policy "#get-started-fms-sg-create-security-policy").

## Step 3: Creating and applying a common security group policy

After completing the prerequisites, you create an AWS Firewall Manager common security group policy. A
common security group policy provides a centrally controlled security group for your
entire AWS organization. It also defines the AWS accounts and resources that the
security group applies to. In addition to common security group policies, Firewall Manager supports
content audit security group policies, to manage the security group rules in use in your
organization, and usage audit security group policies, to manage unused and redundant
security groups. For more information, see [Using security group policies in Firewall Manager to manage Amazon VPC security groups](security-group-policies.md "security-group-policies.md").

For this tutorial, you create a common security group policy and set its action to not automatically
remediate. This allows you to see what effect the policy would have without making
changes to your AWS organization.

###### To create a Firewall Manager common

security group policy (console)

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. In the navigation pane, choose **Security policies**. 3. If you have not met the prerequisites, the console displays instructions about how to fix
any issues. Follow the instructions, and then return to this step, to create a
common security group policy. 4. Choose **Create policy**. 5. For **Policy type**, choose **Security
group**. 6. For **Security group policy type**, choose **Common
security groups**. 7. For **Region**, choose an AWS Region. 8. Choose **Next**. 9. For **Policy name**, enter a descriptive name. 10. **Policy rules** allow you to choose how the security groups
in this policy are applied and maintained. For this tutorial,
leave the options unchecked. 11. Choose **Add primary security group**, select the security
group that you created for this tutorial, and choose **Add security
group**. 12. For **Policy action**, choose **Identify resources
that don’t comply with the policy rules, but don’t auto
remediate.** 13. Choose **Next**. 14. **AWS accounts affected by this policy** allows you to narrow
the scope of your policy by specifying accounts to include or exclude. For this
tutorial, choose **Include all accounts under my
organization.** 15. For **Resource type**, choose one or more types, according to the
resources you have defined for your AWS organization. 16. For **Resources**, you can narrow the scope of the policy
using tagging, by either including or excluding resources with the tags that you specify.
You can use inclusion or exclusion, and not both. For
more information about tags to define policy scope, see [Using the AWS Firewall Manager policy scope](policy-scope.md "policy-scope.md").

Resource tags can only have non-null values. If you omit the value for a tag,
Firewall Manager saves the tag with an empty string value: "". Resource tags only match with tags that have the same key
and the same value. 17. Choose **Next**. 18. For **Policy tags**, add any identifying tags that you want
to add to the Firewall Manager policy resource. For more information about tags, see [Working with Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md"). 19. Choose **Next**. 20. Review the new policy settings and return to any pages where you need to any adjustments.

Check to be sure that **Policy actions** is
set to **Identify resources that don’t comply with the policy rules, but
don’t auto remediate.** This allows you to review the changes that
your policy would make before you enable them. 21. When you are satisfied with the policy, choose **Create policy**.

In the **AWS Firewall Manager policies** pane, your policy should be
listed. It will probably indicate **Pending** under the
accounts headings and it will indicate the status of the **Automatic
remediation** setting. The creation of a policy can take
several minutes. After the **Pending** status is replaced with
account counts, you can choose the policy name to explore the compliance status
of the accounts and resources. For information, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md") 22. When you are finished exploring, if you don't want to keep the policy you created for this
tutorial, choose the policy name, choose **Delete**, choose
**Clean up resources created by this policy.**, and finally
choose **Delete**.

For more information about Firewall Manager security group policies, see [Using security group policies in Firewall Manager to manage Amazon VPC security groups](security-group-policies.md "security-group-policies.md").
