# Move an Amazon Connect phone number

across instances

You can move a phone number from one Amazon Connect instance or traffic distribution group
to another Amazon Connect instance or traffic distribution group in the same AWS account
and Region, different AWS accounts, or different Regions.

Amazon Connect supports the following scenarios for migrating phone numbers:

- Both Amazon Connect instances are in the same AWS Region and AWS account. In
  this scenario, you can move the numbers yourself.
- The old and new Amazon Connect instances are in different Regions, but same
  account. AWS Support must migrate the numbers for you.
- The old and new Amazon Connect instances are in same AWS Regions but different
  AWS accounts. AWS Support must migrate the numbers for you.

###### Contents

- [Important things to know](#move-number-important "#move-number-important")
- [Self-move: same Region and
  AWS account](#move-number-same-region-account "#move-number-same-region-account")
- [Different Regions and/or
  AWS account](#move-number-different-region-account "#move-number-different-region-account")

## Important things to know

The following information applies to phone number migrations that are
performed by AWS Support.

- If your new instance ARN belongs to traffic distribution group, you
  need to provide AWS Support with the instance and traffic distribution
  group ARNs. To obtain the traffic distribution group ARN, run a [list-traffic-distribution-groups](../../../cli/latest/reference/connect/list-traffic-distribution-groups.md "../../../cli/latest/reference/connect/list-traffic-distribution-groups.md") CLI command.
- AWS Support can schedule migrations anytime between Monday and Friday.
  Exceptions to this are local National Holidays when no phone number
  migrations can be scheduled.
- When the migration date and time arrives, you must make sure the phone
  number is no longer configured as the outbound callback number on any of
  your queues. Otherwise, this will prevent AWS Support from migrating the
  number and it may delay the process.
- The migration of each phone number takes between 20-30 minutes. During
  a phone number migration, **calls may be blocked and
  may fail for the number being migrated**.
- To eliminate additional downtime, if you're associating a flow to a
  migrated phone number in the new Amazon Connect instance, make sure the flow
  exists and is published in the new Amazon Connect instance. Provide AWS Support
  with the flow ARN so they can associate it with the phone number when
  they do the migration.
- Depending on the phone number, migration might not be possible. You'll
  be contacted through your AWS Support case if this applies to your
  request. Refer to the [Amazon Connect Telecoms Country Coverage Guide](https://d1v2gagwb6hfe1.cloudfront.net/Amazon_Connect_Telecoms_Coverage.pdf "https://d1v2gagwb6hfe1.cloudfront.net/Amazon_Connect_Telecoms_Coverage.pdf") for regional
  availability of phone numbers in certain countries.
- After your phone number is migrated, you must set the outbound number
  on your queues. This cannot be done by AWS Support.

AWS Support will request that you acknowledge and understand the above
information before they schedule your phone number migration.

## Self-move: same Region and

AWS account

When both Amazon Connect instances are in the same Region and AWS account, you can
move the phone number yourself by using the [ListPhoneNumbersV2](../APIReference/API_ListPhoneNumbersV2.md "../APIReference/API_ListPhoneNumbersV2.md") and [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") APIs.

###### Note

If you receive errors when running AWS CLI commands, make sure that
you're using the [most recent
AWS CLI version](../../../cli/latest/userguide/cli-chap-troubleshooting.md "../../../cli/latest/userguide/cli-chap-troubleshooting.md").

For instructions and sample CLI commands, see [How
do I migrate phone numbers from one Amazon Connect instance to another?](https://repost.aws/knowledge-center/connect-migrate-phone-number "https://repost.aws/knowledge-center/connect-migrate-phone-number")

## Different Regions and/or

AWS account

When the old and new Amazon Connect instances are located in different Regions, but the
same AWS account, complete the following steps to create a single AWS Support
case.

When the old and new Amazon Connect instances belong to different AWS accounts,
create two AWS Support cases, one from each account, following the same steps.

1. Sign in to your AWS account and then click [here](https://console.aws.amazon.com/support/home#/case/create?issueType=customer-service&serviceCode=service-connect-number-management "https://console.aws.amazon.com/support/home#/case/create?issueType=customer-service&serviceCode=service-connect-number-management") to access a pre-populated form in the AWS Support
   console.
2. In the form, for **Service**, select
   **Connect (Number Management)**.
3. For **Category**, select **Phone Number
   Migration**.
4. Choose the appropriate severity.
5. Choose **Next step: Additional information**.
6. On the **Additional information** page:
   1. Enter the subject.
   2. Under **Description**, include as much
      information as possible about your request, including the phone
      numbers (in E164 format) and a flow, if you want Support to assign
      your numbers after the migration completes.

7. Under **Help us resolve your case faster**, provide
   all of the required information such as the source and destination
   instance ARNs and your desired migration date and time, including
   timezone.
8. Choose **Next step: Solve now or contact us**.
9. On the **Solve now or contact us** page:
   1. Choose the **Contact us** tab and select your
      **Preferred contact language** and your
      preferred contact method.

10. Choose **Submit**.
11. The Amazon Connect team will review your ticket and get back to you.
