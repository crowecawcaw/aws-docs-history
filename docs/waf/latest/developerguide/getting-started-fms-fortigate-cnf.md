**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up AWS Firewall Manager​ Fortigate CNF policies

Fortigate Cloud Native Firewall (CNF) as a Service is a third-party firewall service that you can use for your AWS Firewall Manager policies.
With Fortigate CNF for Firewall Manager, you can create and centrally deploy Fortigate CNF resources and policy sets
across all of your AWS accounts. To use AWS Firewall Manager to enable Fortigate CNF policies, perform the
following steps in sequence. For more information about Fortigate CNF
policies, see [Using Fortigate Cloud Native Firewall (CNF) as a Service policies for Firewall Manager](fortigate-cnf-policies.md "fortigate-cnf-policies.md").

###### Topics

- [Step 1: Completing the general
  prerequisites](#complete-fms-prereq-fortigate-cnf "#complete-fms-prereq-fortigate-cnf")
- [Step 2: Completing the Fortigate CNF policy prerequisites](#complete-prereq-fortigate-cnf "#complete-prereq-fortigate-cnf")
- [Step 3: Creating and applying a Fortigate CNF policy](#get-started-fms-fortigate-cnf-create-policy "#get-started-fms-fortigate-cnf-create-policy")

## Step 1: Completing the general

prerequisites

There are several mandatory steps to prepare your account for AWS Firewall Manager. Those steps are
described in [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). Complete all the
prerequisites before proceeding to the next step.

## Step 2: Completing the Fortigate CNF policy prerequisites

There are additional mandatory steps that you must complete in order to use Fortigate CNF policies. Those steps are
described in [Fortigate Cloud Native Firewall (CNF) as a Service policy prerequisites](fms-third-party-prerequisites.md#fms-fortigate-cnf-prerequisites "fms-third-party-prerequisites.md#fms-fortigate-cnf-prerequisites"). Complete all the
prerequisites before proceeding to the next step.

## Step 3: Creating and applying a Fortigate CNF policy

After completing the prerequisites, you create an AWS Firewall Manager Fortigate CNF policy.

For more information about Firewall Manager policies for Fortigate CNF, see [Using Fortigate Cloud Native Firewall (CNF) as a Service policies for Firewall Manager](fortigate-cnf-policies.md "fortigate-cnf-policies.md").

###### To create a Firewall Manager policy for Fortigate CNF (console)

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. In the navigation pane, choose **Security
policies**. 3. Choose **Create policy**. 4. For **Policy type**, choose Fortigate CNF. If you haven't
already subscribed to the Fortigate CNF service in the AWS Marketplace, you'll
need to do that first. To subscribe in the AWS Marketplace, choose
**View AWS Marketplace details**. 5. For **Deployment model**, choose either the **Distributed model** or **Centralized model**. The deployment model determines how Firewall Manager manages endpoints for the policy. With the distributed model, Firewall Manager maintains firewall endpoints in each VPC that's within policy scope. With the centralized model, Firewall Manager maintains a single endpoint in an inspection VPC. 6. For **Region**, choose an AWS Region. To protect
resources in multiple Regions, you must create separate policies for each
Region. 7. Choose **Next**. 8. 9. In the policy configuration, choose the Fortigate CNF firewall policy to associate with this
policy. The list of Fortigate CNF firewall policies contains all of the Fortigate CNF
firewall policies that are associated with your Fortigate CNF tenant. For information
about creating and managing Fortigate CNF firewall policies, see the [Fortigate CNF documentation](https://docs.fortinet.com/product/fortigate-cnf "https://docs.fortinet.com/product/fortigate-cnf"). 10. Choose **Next**. 11. Under **Configure third-party firewall endpoint** do one of the following, depending on whether you're using the distributed or centralized
deployment model to create your firewall endpoints:

    * If you're using the distributed deployment model for this policy, under **Availability Zones**,
     select which Availability Zones to create firewall
     endpoints in. You can select Availability Zones by
     **Availability Zone name** or by
     **Availability Zone ID**.
    * If you're using the centralized deployment model for this policy, in
     **AWS Firewall Manager endpoint configuration** under
     **Inspection VPC configuration**, enter the
     AWS account ID of the owner of the inspection VPC, and the VPC ID
     of the inspection VPC.




    	+ Under **Availability Zones**,
    	 select which Availability Zones to create firewall
    	 endpoints in. You can select Availability Zones by
    	 **Availability Zone name** or by
    	 **Availability Zone ID**.

12. Choose **Next**.
13. For **Policy scope**, under **AWS accounts this policy applies to**, choose the
    option as follows:

        * If you want to apply the policy to all accounts in your
         organization, leave the default selection, **Include all
         accounts under my AWS organization**.
        * If you want to apply the policy only to specific accounts or
         accounts that are in specific AWS Organizations organizational units
         (OUs), choose **Include only the specified accounts and
         organizational units**, and then add the accounts and
         OUs that you want to include. Specifying an OU is the equivalent of
         specifying all accounts in the OU and in any of its child OUs,
         including any child OUs and accounts that are added at a later time.
        * If you want to apply the policy to all but a specific set of
         accounts or AWS Organizations organizational units (OUs), choose
         **Exclude the specified accounts and organizational
         units, and include all others**, and then add the
         accounts and OUs that you want to exclude. Specifying an OU is the
         equivalent of specifying all accounts in the OU and in any of its
         child OUs, including any child OUs and accounts that are added at a
         later time.

    You can only choose one of the options.

After you apply the policy, Firewall Manager automatically evaluates any new accounts
against your settings. For example, if you include only specific accounts,
Firewall Manager doesn't apply the policy to any new accounts. As another example, if
you include an OU, when you add an account to the OU or to any of its child
OUs, Firewall Manager automatically applies the policy to the new account.

The **Resource type** for Fortigate CNF policies is
**VPC**. 14. For **Resources**, you can narrow the scope of the policy
using tagging, by either including or excluding resources with the tags that you specify.
You can use inclusion or exclusion, and not both. For
more information about tags to define policy scope, see [Using the AWS Firewall Manager policy scope](policy-scope.md "policy-scope.md").

Resource tags can only have non-null values. If you omit the value for a tag,
Firewall Manager saves the tag with an empty string value: "". Resource tags only match with tags that have the same key
and the same value. 15. For **Grant cross-account access**, choose **Download CloudFormation
template**. This downloads an CloudFormation template that you can use to
create an CloudFormation stack. This stack creates an AWS Identity and Access Management role that grants Firewall Manager cross-account permissions to manage Fortigate CNF resources. For information about stacks, see [Working with stacks](../../../AWSCloudFormation/latest/gsg/stacks.md "../../../AWSCloudFormation/latest/gsg/stacks.md") in the _CloudFormation User
Guide_. To create a stack, you'll need the account ID from the Fortigate CNF portal. 16. Choose **Next**. 17. For **Policy tags**, add any identifying tags that you want
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
of the accounts and resources. For information, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md")

For more information about Firewall Manager Fortigate CNF policies, see [Using Fortigate Cloud Native Firewall (CNF) as a Service policies for Firewall Manager](fortigate-cnf-policies.md "fortigate-cnf-policies.md").
