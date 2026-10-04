

# Long code registration
<a name="nx-reg-type-long"></a>

The following countries and regions require registering a long code or other dedicated number before you can send messages to recipients there. Select a country or region to review its requirements and the step-by-step registration process.

## United States 10DLC registration
<a name="nx-dednum-us-10dlc"></a>

**Important**  
The following table has the expected times for each 10DLC registration step based on if your business is located in the United States or internationally.  



| 10DLC registration step | US based companies | International based companies | 
| --- | --- | --- | 
| Register your brand/company | 1-2 business days | Up to 3 weeks | 
| Apply for vetting | 1-2 business days | Up to 3 weeks | 
| Register your campaign | Up to 4 weeks | Up to 4 weeks | 
| Request your 10DLC number | Up to 10 days | Up to 10 days | 

If you use AWS End User Messaging to send messages to recipients in the United States or the US territories of Puerto Rico, US Virgin Islands, Guam and American Samoa, you can use 10DLC phone numbers to deliver those messages. The abbreviation *10DLC* stands for "10-digit long code." A 10DLC phone number is registered for use by a single sender and for a single use case. This registration process gives the mobile carriers insight into the approved use cases for each phone number that is used to send messages. As a result, 10DLC phone numbers can offer high throughput and deliverability rates.

A message that you send from a 10DLC phone number appears on the devices of your recipients as a 10-digit phone number. You can use 10DLC phone numbers to send both transactional and promotional messages. If you already use short codes or toll-free numbers to send your messages, then you don't need to set up 10DLC.

To set up 10DLC, you first register your company or brand. You should then externally vet your 10DLC company to ensure you get the highest eligible throughput. Next, you create a *10DLC campaign*, which is a description of your use case. This information is then shared with the Campaign Registry, an industry organization that collects 10DLC registration information.

**Note**  
For more information about how the Campaign Registry uses your information, see the FAQ on the [Campaign Registry website](https://www.campaignregistry.com/resources/).

After your company and 10DLC campaign are approved, you can purchase a phone number and associate it with your 10DLC campaign. Associating a phone number with a 10DLC campaign can take approximately 14 days to complete. Although you can associate multiple phone numbers with a single campaign, you can't use the same phone number across multiple 10DLC campaigns. For each 10DLC campaign that you create, you must have at least one unique phone number. Throughput for 10DLC phone numbers is based on the company and campaign registration information that you provide. Each 10DLC number associated to a campaign supports 1 message part per second (MPS). To get the eligible throughput from your campaign applied to the associated 10DLC numbers, you need to submit a request to increase SMS sending rates.

If you have an existing unregistered long code in your AWS End User Messaging account, you can request that it be converted to a 10DLC number. To convert an existing long code, complete the registration process, and then create a case in the AWS Support Center. In some situations, it isn't possible to convert an unregistered long code to a 10DLC phone number. In this case, you must request a new number through the AWS End User Messaging console and associate it with your 10DLC campaign. For more information about using 10DLC with existing long codes, see [Associating a long code with a 10DLC campaign](#registrations-10dlc-associate).

**Topics**
+ [10DLC capabilities](#registrations-10dlc-capabilities)
+ [10DLC registration process](#registrations-10dlc-setup)
+ [Associating a long code with a 10DLC campaign](#registrations-10dlc-associate)
+ [10DLC registration and monthly fees](#registrations-10dlc-fees)
+ [10DLC cross-account access](#registrations-10dlc-configure-cross-account-access)
+ [10DLC brand registration form](nx-dednum-us-10dlc-company.md)
+ [Resend a 10DLC brand email authentication](nx-dednum-us-10dlc-auth.md)
+ [10DLC brand vetting form](nx-dednum-us-10dlc-vetting.md)
+ [10DLC campaign registration form](nx-dednum-us-10dlc-register-campaign.md)

### 10DLC capabilities
<a name="registrations-10dlc-capabilities"></a>

**Note**  
When your 10DLC campaign is approved, AWS End User Messaging automatically applies the message throughput that the campaign qualifies for to the phone numbers associated with that campaign. You do not need to submit a separate request to increase the message parts per second (MPS) for those numbers.

The capabilities of 10DLC phone numbers depend on which mobile carriers your recipients use. AT&T provides a per-second send rate for each campaign. T-Mobile provides a daily limit on the number of messages that can be sent, with no separate per-second send rate. Verizon has not published throughput limits, but uses a filtering system for 10DLC that is designed to remove spam, unsolicited messages, and abusive content, with less emphasis on the actual message throughput.

Throughput is applied at the *campaign* level. All phone numbers associated with the same campaign share a single send rate limit, rather than each number having its own. Each associated phone number shows the campaign's send rate as its limit. Because the limit is shared, messages sent from multiple numbers on the same campaign count toward the same limit. For example, if a campaign has a send rate limit of 8 message parts per second (MPS), you can send up to 8 MPS from a single number on that campaign. You can also split that throughput across multiple numbers, such as 4 MPS from each of two numbers. In both cases, the combined rate across the campaign cannot exceed 8 MPS before messages are throttled.

The T-Mobile daily message cap is advisory and is applied per campaign for T-Mobile recipients. After a campaign reaches its daily message cap, additional messages to T-Mobile recipients fail until the cap resets. For instructions on viewing the current send rate limits and daily message caps for a phone number, see the SMS message-per-second limits.

To increase the throughput that a campaign qualifies for, you can request that your company registration be vetted. When you vet your company registration, a third-party verification provider analyzes your company details and provides a vetting score. A higher score can raise the throughput tier that your campaigns qualify for. Vetting scores are not applied retroactively: if you vet your company registration after you have already created a campaign, the new score is not applied to that existing campaign. For this reason, vet your company or brand *before* you create your 10DLC campaigns. There is a one-time charge for the vetting service. For more information, see [the 10DLC vetting process](nx-dednum-us-10dlc-vetting.md).

Throughput rates for 10DLC are determined by the US mobile carriers in cooperation with the Campaign Registry. Neither AWS End User Messaging nor any other SMS sending service can increase 10DLC throughput beyond these rates. If you need high throughput rates and high deliverability rates across all US carriers, we recommend that you use a short code. 

### 10DLC registration process
<a name="registrations-10dlc-setup"></a>

You can set up 10DLC directly in the AWS End User Messaging console. To set up 10DLC, you must complete all of the following steps.

1. **Register your brand/company**

   The first step in setting up 10DLC is to register your company or brand. For information about company registration, see [the 10DLC company registration](nx-dednum-us-10dlc-company.md). There is a one-time registration fee to register your company. This fee is shown on the registration page.

1. **(Optional) Apply for vetting**

   We recommend completing this step if your use case requires higher throughput. If your company registration is successful, you can begin creating low-volume, mixed-use 10DLC campaigns. To increase the throughput that your campaigns qualify for, you can apply for vetting of your company registration. A higher vetting score can raise the throughput tier that your campaigns qualify for, but vetting is not guaranteed to increase your throughput. Because vetting scores are not applied retroactively to campaigns that you have already created, vet your company or brand *before* you create your 10DLC campaigns. For more information about vetting, see [the 10DLC vetting process](nx-dednum-us-10dlc-vetting.md). For more information about how throughput is applied, see [10DLC capabilities](#registrations-10dlc-capabilities).

1. **Register your campaign**

   If the Campaign Registry is able to verify the company information that you provided, you can create a 10DLC campaign. A 10DLC campaign contains information about your use case. Each 10DLC campaign can be associated with one company. AWS End User Messaging sends this campaign information to the Campaign Registry for approval. In most cases, 10DLC campaign approval is instantaneous. In some cases, the Campaign Registry can require additional information. It can take up to 4 weeks to receive a response on if your 10DLC campaign was approved or needs to be revised. 

   You're charged a recurring monthly fee for each 10DLC campaign that you register. The monthly fee varies depending on your use case. The recurring fee for your campaign is shown on the registration page.

1. **Request your 10DLC number**

   After your 10DLC campaign is approved, you can request a phone number and associate it with the approved campaign. When you request a number through the **Request originator** flow, you choose the registered brand and campaign to associate the number with as part of the request. You can also search for and choose a specific number by area code or pattern instead of receiving a random assignment. Each phone number can only be associated with a single 10DLC campaign, and a campaign can have more than one number associated with it. For more information, see the phone number request process, selecting a 10DLC number, and [Associating a long code with a 10DLC campaign](#registrations-10dlc-associate). There is a monthly recurring fee for leasing the phone number. This fee is shown on the purchase page.
**Note**  
You are charged the monthly 10DLC number lease price regardless of status. For example, 10DLC numbers in a **Pending** state still generate a month fee. For more information about pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

### Associating a long code with a 10DLC campaign
<a name="registrations-10dlc-associate"></a>

You can associate a phone number with an approved 10DLC campaign when you request the number through the **Request originator** flow. If you provisioned a new long code without associating it, or you have an existing long code, you can associate it with the approved campaign by using the following procedure. The long code that you associate with the 10DLC campaign can only be used with that campaign, and you cannot use it for any other 10DLC campaign.

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose the 10DLC campaign(US\_TEN\_DLC\_CAMPAIGN\_REGISTRATION) to associate the long code with.

1. Choose the **Associated resourced** tab and **Add resource**.

1. For **Supported association**, choose **TEN\_DLC** from the dropdown list. 

1. For **Available resources**, choose the 10DLC phone number to add.

1. Choose **Associate resource**.

You can associate more than one long code with the 10DLC campaign.

### 10DLC registration and monthly fees
<a name="registrations-10dlc-fees"></a>

There are registration and monthly fees associated with using 10DLC, such as registering your company and 10DLC campaign. These are separate from any other monthly or AWS fees. For more information about 10DLC fees, see the [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/) page.

### 10DLC cross-account access
<a name="registrations-10dlc-configure-cross-account-access"></a>

Each 10DLC phone number is associated with a single account in a single AWS Region. If you want to use the same 10DLC phone number to send messages in more than one account or Region, you have two options:

1. You can register the same company and campaign in each of your AWS accounts. These registrations are managed and charged separately. If you register the same company in multiple AWS accounts, the number of messages that you can send to T-Mobile customers per day is shared across each of those accounts.

1. You can complete the 10DLC registration process in one AWS account, and use AWS Identity and Access Management (IAM) to grant other accounts permission to send through your 10DLC number.
**Note**  
This option allows for true cross-account access to your 10DLC phone numbers. However, note that messages sent from your secondary accounts are treated as if they were sent from your primary account. Quotas and billing are counted against the primary account and not against any secondary accounts.

#### Setting up cross-account access using IAM policies
<a name="registrations-10dlc-configure-cross-account-access-iam"></a>

You can use IAM roles to associate other accounts with your main account. Then, you can delegate access permissions from your primary account to your secondary accounts by granting them access to the 10DLC numbers in the primary account.

**To grant access to a 10DLC number in your primary account**

1. If you haven't already done so, complete the 10DLC registration process in the primary account. This process involves three steps:
   + Register your company. For more information, see [the 10DLC company registration](nx-dednum-us-10dlc-company.md).
   + Register your 10DLC campaign (use case). For more information, see the 10DLC campaign registration.
   + Associate a phone number with your 10DLC campaign. For more information, see [Associating a long code with a 10DLC campaign](#registrations-10dlc-associate).

1. Create an IAM role in your primary account that allows another account to call the `SendTextMessage` API operation for your 10DLC phone number. For more information on creating roles, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*. 

1. Delegate and test access permission from your primary account using IAM roles with any of your other accounts that need to use your 10DLC numbers. For example, you might delegate access permission from your Production account to your Development account. For more information about delegating and testing permissions, see [Delegate access across AWS account using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) in the *IAM User Guide*.

1. Using the new role, send a message using a 10DLC number from a secondary account. For more information about using a role, see [Using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html) in the *IAM User Guide*.