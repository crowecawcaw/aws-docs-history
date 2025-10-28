**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Security best practices for Amazon Pinpoint

The following best practices are general guidelines and don't represent a complete
security solution. Because these best practices might not be appropriate or sufficient for
your environment, treat them as helpful considerations rather than prescriptions.

AWS Identity and Access Management (IAM) is a service that you can use to control AWS services, including
Amazon Pinpoint. Consider the following best practices as you build your Amazon Pinpoint architecture:

- Use IAM accounts to control access to Amazon Pinpoint API operations, especially
  operations that create, modify, or delete Amazon Pinpoint resources. For the Amazon Pinpoint API, these
  resources include projects, campaigns, and journeys. For the Amazon Pinpoint SMS and Voice API, these
  resources include phone numbers, pools, and configuration sets.
- Create an individual IAM user for each person who manages Amazon Pinpoint resources,
  including yourself. Don't use AWS account root users to manage Amazon Pinpoint
  resources.
- Grant users the minimum set of permissions required to perform his or her
  duties.
- Use IAM groups to effectively manage permissions for multiple users.
- Rotate your IAM credentials regularly.
  For more information about Amazon Pinpoint security, see [Security in Amazon Pinpoint](../../../awssupport/latest/user/trusted-advisor.md "../../../awssupport/latest/user/trusted-advisor.md"). For more information about IAM, see [AWS Identity and Access Management](../../../IAM/latest/UserGuide/getting-set-up.md "../../../IAM/latest/UserGuide/getting-set-up.md").
  For information on IAM best practices, see [Security best practices in
  IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").
