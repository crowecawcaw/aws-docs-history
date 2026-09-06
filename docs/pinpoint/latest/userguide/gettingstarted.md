

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Getting started with Amazon Pinpoint
<a name="gettingstarted"></a>

**Important**  
Amazon Pinpoint is no longer accepting new customers as of May 20, 2025. Existing customers can continue using Amazon Pinpoint until end of support on October 30, 2026. For migration guidance, see [Amazon Pinpoint end of support](migrate.md).

The following tutorial content is preserved for existing customers who need to reference the original onboarding steps. New implementations should use [Amazon Connect Customer outbound campaigns](https://aws.amazon.com/connect/outbound/) or [AWS End User Messaging](https://aws.amazon.com/end-user-messaging/) instead.

## About this tutorial
<a name="gettingstarted-about-this-tutorial"></a>

This section contains an overview of this tutorial.

**Intended Audience**  
This tutorial is designed for marketing and business users.

If you're a software developer or system administrator, you might also find the [tutorials](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tutorials.html) in the *Amazon Pinpoint Developer Guide* to be useful.

**Features Used**  
This tutorial shows you how to complete all of the following steps by using the Amazon Pinpoint console:
+ Importing customer data from a file.
+ Creating a segment that targets specific users based on their attributes.
+ Creating an email campaign and scheduling it to be sent at a specific time.
+ Viewing email delivery and response data by using the analytics dashboards that are built into Amazon Pinpoint.

**Time Required**  
It should take about 30–45 minutes to complete this tutorial.

**Regional Restrictions**  
There are no regional restrictions associated with using this solution.

**Resource Usage Costs**  
There's no charge for creating an AWS account. However, by implementing this solution, you might incur some or all of the costs that are listed in the following table.


| Description | Cost (US dollars) | 
| --- | --- | 
| Message sending costs | You pay $0.0001 for each email that you send through Amazon Pinpoint. | 
| Monthly targeted audience costs | You pay $0 for the first 5,000 endpoints that you target in Amazon Pinpoint each month. (An endpoint is a destination that you can send messages to, such as a user's email address or mobile phone number.) After that, you pay $0.0012 per endpoint that you target. | 

If you use this tutorial to send 5 messages to 5 separate endpoints in one month, you incur charges of $0.0005.

For detailed information about the costs that you might incur using Amazon Pinpoint, see [Amazon Pinpoint pricing](https://aws.amazon.com/pinpoint/pricing/).

**Next:** [Create and Configure a Project](gettingstarted-create-project.md)