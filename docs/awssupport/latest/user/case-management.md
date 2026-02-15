# Case management

###### Note

You can revert to the legacy method of case management by choosing **Use the old experience** in the banner at the top of the Support Center console. For more information, see [Legacy experience: Creating support cases and case management](case-management-legacy.md "case-management-legacy.md").

In the AWS Management Console, you can create three types of customer cases in Support:

- **Account and billing** support cases are available to all AWS
  customers. You can get help with billing and account questions.
- **Service limit increase** requests are available to all AWS
  customers. For more information about the default service quotas, formerly referred
  to as limits, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in
  the _AWS General Reference_.
- **Technical** support cases connect you to technical support for
  help with service-related technical issues and, in some cases, third-party
  applications. If you have Basic Support, you can't create a technical support
  case.

###### Notes

    + To change your support plan, see [Change AWS Support Plans](changing-support-plans.md "changing-support-plans.md").
    + To close your account, see [Closing
     an Account](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md") in the
     *AWS Billing User Guide*.
    + To find common troubleshooting topics for AWS services, see [Troubleshooting resources](troubleshooting.md "troubleshooting.md").
    + If you're a customer of an AWS Partner that is part of the AWS Partner Network, and
     you use Resold Support, contact your AWS Partner directly for any billing
     related issues. AWS Support can't assist with non-technical issues for
     Resold Support, such as billing and account management. For more
     information, see the following topics:




    	- [How AWS Partners can determine AWS Support
    	 plans in an organization](https://aws.amazon.com/blogs/mt/aws-partners-determine-aws-support-plans-in-organization/ "https://aws.amazon.com/blogs/mt/aws-partners-determine-aws-support-plans-in-organization/")
    	- [AWS Partner-Led Support](https://aws.amazon.com/premiumsupport/partner-led-support/ "https://aws.amazon.com/premiumsupport/partner-led-support/")

## Describing your problem

Make your description as detailed as possible. Include relevant resource information,
along with anything else that might help us understand your issue. For example, to
troubleshoot performance, include timestamps and logs. For feature requests or general
guidance questions, include a description of your environment and purpose.

When you provide as much detail as possible, you increase the chances that your case
can be resolved quickly.

## Choosing an initial support case severity level

When creating a support case make sure that the right severity is defined and that you provide as much information as possible.

You might want to create a support case at the highest severity that
your support plan allows. However, it's a best practice to choose the highest severity
only for cases that can't be worked around or that directly affect production applications.
For information about building your services so that losing a single resource doesn't
affect your applications, see the [Building Fault-Tolerant Applications on AWS](http://media.amazonwebservices.com/AWS_Building_Fault_Tolerant_Applications.pdf "http://media.amazonwebservices.com/AWS_Building_Fault_Tolerant_Applications.pdf") technical paper.

The following table lists the severity levels, response times, and example problems.

###### Notes

- If you have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan, you can reassign your support case severity level to reflect changes to urgency and business impact. For example, you can change your support case from **System impaired** to **Production system impaired**. When you change the case severity, AWS Support receives notification and routes the case according to the new severity level. For more information, see [Changing the severity level of your support case](#change-severity-for-support-cases "#change-severity-for-support-cases").
- If you have a Basic Support plan, then you can't change the severity level for a support case after you create
  it. If your situation changes, work with the Support agent.
- For more information about the severity level, see the [AWS Support API Reference](../APIReference/API_SeverityLevel.md "../APIReference/API_SeverityLevel.md").

| Severity                          | Severity level code | First-response time                                                                                                                                                         | Description and support plan                                                                                                                                                                                 |
| --------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **General guidance**              | `low`               | 24 hours                                                                                                                                                                    | You have a general development question, or you want to request a<br>feature. (AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan)                                                |
| **System impaired**               | `normal`            | 12 hours                                                                                                                                                                    | Non-critical functions of your application are behaving<br>abnormally, or you have a time-sensitive development question.<br>(AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan) |
| **Production system impaired**    | `high`              | 4 hours                                                                                                                                                                     | Important functions of your application are impaired or degraded.<br>(AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan)                                                         |
| **Production system down**        | `urgent`            | 1 hour                                                                                                                                                                      | Your business is significantly impacted. Important functions of<br>your application aren't available. (AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan)                        |
| **Business-critical system down** | `critical`          | • AWS Business Support+: Less than 30 minutes<br>• AWS Enterprise Support: Less than 15 minutes<br>• AWS Unified Operations: 5 minutes from an Incident Management Engineer | Your business is at risk. Critical functions of your application aren't available.                                                                                                                           |

## Understanding AWS Support response times

AWS Support makes every reasonable effort to respond to your initial request within the
indicated timeframe. For information about the scope of support for each Support plan,
see [AWS Support features](https://aws.amazon.com/premiumsupport/features/ "https://aws.amazon.com/premiumsupport/features/").

If you have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan, you have round-the-clock access for technical support.

###### Note

If you choose Japanese as your preferred contact language for support cases, support
in Japanese may be available as follows:

- If you need customer service for non-technical support cases, support in Japanese is available during
  business hours in Japan defined as 09:00 AM to 06:00 PM Japan Standard Time (GMT+9), excluding
  holidays and weekends.
- If you have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan, technical support is available
  all day, every day in Japanese.
  If you choose Chinese as your preferred contact language for support cases, support in Chinese might be available
  as follows:

- If you need customer service for non-technical support cases, support in Chinese is available
  09:00 AM to 06:00 PM (GMT+8), excluding holidays and weekends.
- If you have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan, technical support is available all day, every day in Chinese.
  If you choose Korean as your preferred contact language for support cases, support in Korean may be
  available as follows:

- If you need customer service for non-technical support cases, support in Korean is available
  during business hours in Korea defined as 09:00 AM to 06:00 PM Korean Standard Time (GMT+9),
  excluding holidays and weekends.
- If you have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan, technical support is available all day, every day in Korean.

## Changing the severity level of your support case

If you have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan, you can reassign your support case severity level to reflect changes to urgency and business impact. For example, you can change your support case from **System impaired** to **Production system impaired**. When you change the case severity, AWS Support receives notification and attends to the case according to the new severity level.

###### Note

Japanese (JP) account or billing, Service Quota Increase Request (SQIR), and Turkish (TR) account or billing cases created in these languages have a default severity and can't be changed.

To change the severity of a support case, complete the following steps:

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").

###### Tip

In the AWS Management Console, you can also choose the question mark icon (
![Question mark icon representing help or information.](/images/awssupport/latest/user/images/questionmark.png)
) and then choose **Support Center**. 2. Select the case that you want to change the severity level for. 3. In **Case details**, choose the pencil icon next to the **Severity** field, as shown in the following example.

![The Case details section with the Severity field and pencil icon highlighted.](images/case-details-change-severity.png) 4. For **Severity**, choose the new severity level from the following options:

    * General guidance
    * System impaired
    * Production system impaired
    * Production system down
    * Business-critical system down

5. For **Reason for case severity change**, choose from the available options for why you're changing the case severity.
6. (Optional) For **Tell us more**, enter additional information about this change.
7. Do one of the following:
   - If you're lowering the support case severity, or if you're raising it
     from **General guidance** to **System
     impaired** or **Production system
     impaired**, choose **Update**.
   - If you're raising the severity to **Production system down** or **Business-critical system down**, use one of the options in the **Contact methods** section to engage with AWS Support, and then choose **Update**. The following example shows the options available in the **Contact methods** section.

   ![The Change case severity screen showing the Contact methods section with the following options: Web, Chat, and Phone.](images/change-case-severity-contact-methods.png)

###### Note

- If you upgrade your support case severity to **Production system
  down** or **Business-critical system down**,
  you must wait 60 minutes before you can change the severity again.
- If your support case is currently set to **Business-critical system down**, you're
  prompted to initiate live contact with AWS Support instead of assigning a
  higher severity.
- If you're raising your support case severity level after already raising
  it at least once, you might encounter a waiting period. For example, if you
  change the severity from **System impaired** to
  **Production system impaired** at 6:00 AM, then your
  support case falls under the 4-hour first-response time for the
  **Production system impaired** severity level. In this
  scenario, you can upgrade the severity level again at 10:00 AM, after the
  4-hour window. For a list of first-response times for each severity level,
  see the table in [Understanding AWS Support response times](#response-times-for-support-cases "#response-times-for-support-cases").
