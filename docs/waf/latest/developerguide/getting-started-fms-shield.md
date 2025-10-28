**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Setting up AWS Firewall Manager​ AWS Shield Advanced policies

You can use AWS Firewall Manager to enable AWS Shield Advanced protections across your organization.

###### Important

Firewall Manager doesn't support Amazon Route 53 or AWS Global Accelerator. If you need to protect these
resources with Shield Advanced, you can't use a Firewall Manager policy. Instead, follow the instructions
in [Adding AWS Shield Advanced protection to AWS resources](configure-new-protection.md "configure-new-protection.md").

To use Firewall Manager to enable Shield Advanced protection, perform the following steps in sequence.

###### Topics

- [Step 1: Completing the prerequisites](#complete-prereq-fms-shield "#complete-prereq-fms-shield")
- [Step 2: Creating and applying a Shield Advanced policy](#get-started-fms-shield-create-security-policy "#get-started-fms-shield-create-security-policy")
- [Step 3: (Optional) Authorizing the Shield Response Team (SRT)](#get-started-fms-shield-authorize-srt "#get-started-fms-shield-authorize-srt")
- [Step 4: Configuring Amazon SNS notifications and Amazon CloudWatch alarms](#get-started-fms-shield-cloudwatch "#get-started-fms-shield-cloudwatch")

## Step 1: Completing the prerequisites

There are several mandatory steps to prepare your account for AWS Firewall Manager. Those steps are
described in [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). Complete all the
prerequisites before proceeding to [Step 2: Creating and applying a Shield Advanced policy](#get-started-fms-shield-create-security-policy "#get-started-fms-shield-create-security-policy").

## Step 2: Creating and applying a Shield Advanced policy

After completing the prerequisites, you create an AWS Firewall Manager Shield Advanced policy. A Firewall Manager
Shield Advanced policy contains the accounts and resources that you want to protect with
Shield Advanced.

###### Important

Firewall Manager does not support Amazon Route 53 or AWS Global Accelerator. If you need to protect these resources with
Shield Advanced, you can't use a Firewall Manager policy. Instead, follow the instructions in [Adding AWS Shield Advanced protection to AWS resources](configure-new-protection.md "configure-new-protection.md").

###### To create a Firewall Manager Shield Advanced policy

(console)

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. In the navigation pane, choose **Security policies**. 3. Choose **Create policy**. 4. For **Policy type**, choose **Shield Advanced**.

To create a Shield Advanced policy, your Firewall Manager administrator account must be subscribed to
Shield Advanced. If you are not subscribed, you are prompted to do so. For information
about the cost for subscribing, see
[AWS Shield Advanced Pricing](https://aws.amazon.com/shield/pricing/ "https://aws.amazon.com/shield/pricing/").

###### Note

You don't need to manually subscribe each member account to Shield Advanced. Firewall Manager does this for you
when it creates the policy. Each account must remain subscribed for Firewall Manager and Shield Advanced to continue to protect resources in the account. 5. For **Region**, choose an AWS Region. To protect Amazon CloudFront resources,
choose **Global**.

To protect resources in multiple Regions (other than CloudFront resources), you must create
separate Firewall Manager policies for each Region. 6. Choose **Next**. 7. For **Name**, enter a descriptive name. 8. (Global Region only) For **Global** Region policies, you can
choose whether you want to manage Shield Advanced automatic application layer DDoS mitigation. For
this tutorial, leave this choice at the default setting of
**Ignore**. 9. For **Policy action**, choose the option that doesn't
automatically remediate. 10. Choose **Next**. 11. **AWS accounts this policy applies to** allows you to narrow the scope
of your policy by specifying accounts to include or exclude. For this tutorial,
choose **Include all accounts under my organization.** 12. Choose the types of resources that you want to protect.

Firewall Manager doesn't support Amazon Route 53 or AWS Global Accelerator. If you need to
protect these resources with Shield Advanced, you can't use a Firewall Manager policy. Instead,
follow the Shield Advanced guidance at [Adding AWS Shield Advanced protection to AWS resources](configure-new-protection.md "configure-new-protection.md"). 13. For **Resources**, you can narrow the scope of the policy
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
of the accounts and resources. For information, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md")

Continue to [Step 3: (Optional) Authorizing the Shield Response Team (SRT)](#get-started-fms-shield-authorize-srt "#get-started-fms-shield-authorize-srt").

## Step 3: (Optional) Authorizing the Shield Response Team (SRT)

One of the benefits of AWS Shield Advanced is support from the Shield Response Team (SRT). When you experience
a potential DDoS attack, you can contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). If necessary,
the Support Center escalates your issue to the SRT. The SRT helps you analyze the
suspicious activity and assists you in mitigating the issue. This mitigation often
involves creating or updating AWS WAF rules and web ACLs in your account. The SRT
can inspect your AWS WAF configuration and create or update AWS WAF rules and web
ACLs for you, but the team needs your authorization to do so. We recommend that as part
of setting up AWS Shield Advanced, you proactively provide the SRT with the needed
authorization. Providing authorization ahead of time helps prevent mitigation delays in
the event of an actual attack.

You authorize and contact the SRT at the account level. That is, the account owner, not the
Firewall Manager administrator, must perform the following steps to authorize the SRT to mitigate
potential attacks. The Firewall Manager administrator can authorize the SRT only for accounts that
they own. Likewise, only the account owner can contact the SRT for support.

###### Note

To use the services of the SRT, you must be subscribed to the [Business Support
plan](https://aws.amazon.com/premiumsupport/business-support/ "https://aws.amazon.com/premiumsupport/business-support/") or the [Enterprise
Support plan](https://aws.amazon.com/premiumsupport/enterprise-support/ "https://aws.amazon.com/premiumsupport/enterprise-support/").

To authorize the SRT to mitigate potential
attacks on your behalf, follow the instructions in [Managed DDoS event response with Shield Response Team (SRT) support](ddos-srt-support.md "ddos-srt-support.md"). You can change SRT access and permissions at any time by using the same steps.

Continue to [Step 4: Configuring Amazon SNS notifications and Amazon CloudWatch alarms](#get-started-fms-shield-cloudwatch "#get-started-fms-shield-cloudwatch").

## Step 4: Configuring Amazon SNS notifications and Amazon CloudWatch alarms

You can continue from this step without configuring Amazon SNS notifications or CloudWatch alarms. However, configuring these alarms and notifications
significantly increases your visibility into possible DDoS events.

You can monitor your protected resources for potential DDoS activity using Amazon SNS. To receive
notification of possible attacks, create an Amazon SNS topic for each Region.

###### Important

Amazon SNS notifications of potential DDoS activity are not sent in real time and can be
delayed. Additionally, if you exceed the Shield Advanced quota of 1,000 protected resources
for each resource type for each account, Firewall Manager performance constraints might prevent
the successful delivery of DDoS attack notifications entirely. For more information,
see [AWS Shield Advanced quotas](shield-limits.md "shield-limits.md").

To enable real-time notifications of potential DDoS activity, you can use a
CloudWatch alarm. Your alarm must be based on the `DDoSDetected` metric
from the account in which the protected resource exists.

###### To create an Amazon SNS topic in Firewall Manager

(console)

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. In the navigation pane, under **AWS FMS**, choose
**Settings**. 3. Choose **Create new topic**. 4. Enter a topic name. 5. Enter an email address that the Amazon SNS messages will be sent to, and then choose **Add
email address**. 6. Choose **Update SNS configuration**.

### Configuring Amazon CloudWatch alarms

Shield Advanced records detection, mitigation, and top contributor metrics
in CloudWatch that you can monitor. For more information, see [AWS Shield Advanced metrics](shield-metrics.md "shield-metrics.md"). CloudWatch incurs
additional costs. For CloudWatch pricing, see
[Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

To create a CloudWatch alarm, follow the instructions in [Using Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md"). By default, Shield Advanced configures CloudWatch to alert
you after just one indicator of a potential DDoS event. If needed, you can use the
CloudWatch console to change this setting to alert you only after multiple indicators are
detected.

###### Note

In addition to the alarms, you can also use a CloudWatch dashboard to monitor
potential DDoS activity. The dashboard collects and processes raw data from Shield Advanced
into readable, near real-time metrics. You can use statistics in Amazon CloudWatch to gain a perspective on how your web
application or service is performing. For more
information, see [What is CloudWatch](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md")
in the _Amazon CloudWatch User Guide_.

For instructions about creating a CloudWatch dashboard, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"). For
information about specific Shield Advanced metrics that you can add to your dashboard,
see [AWS Shield Advanced metrics](shield-metrics.md "shield-metrics.md").

When you've completed your Shield Advanced configuration, familiarize yourself with your options for
viewing events at [Visibility into DDoS events with Shield Advanced](ddos-viewing-events.md "ddos-viewing-events.md").
