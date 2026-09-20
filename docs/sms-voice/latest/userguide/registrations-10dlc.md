

# United States 10DLC registration
<a name="registrations-10dlc"></a>

**Important**  
The following table has the expected times for each 10DLC registration step based on if your business is located in the United States or internationally.  



| 10DLC registration step | US based companies | International based companies | 
| --- | --- | --- | 
| Register your brand/company | 1-2 business days | Up to 3 weeks | 
| Apply for vetting | 1-2 business days | Up to 3 weeks | 
| Register your campaign | Up to 4 weeks | Up to 4 weeks | 
| Request your 10DLC number | Up to 10 days | Up to 10 days | 

If you use AWS End User Messaging SMS to send messages to recipients in the United States or the US territories of Puerto Rico, US Virgin Islands, Guam and American Samoa, you can use 10DLC phone numbers to deliver those messages. The abbreviation *10DLC* stands for "10-digit long code." A 10DLC phone number is registered for use by a single sender and for a single use case. This registration process gives the mobile carriers insight into the approved use cases for each phone number that is used to send messages. As a result, 10DLC phone numbers can offer high throughput and deliverability rates.

A message that you send from a 10DLC phone number appears on the devices of your recipients as a 10-digit phone number. You can use 10DLC phone numbers to send both transactional and promotional messages. If you already use short codes or toll-free numbers to send your messages, then you don't need to set up 10DLC.

To set up 10DLC, you first register your company or brand. You should then externally vet your 10DLC company to ensure you get the highest eligible throughput. Next, you create a *10DLC campaign*, which is a description of your use case. This information is then shared with the Campaign Registry, an industry organization that collects 10DLC registration information.

**Note**  
For more information about how the Campaign Registry uses your information, see the FAQ on the [Campaign Registry website](https://www.campaignregistry.com/resources/).

After your company and 10DLC campaign are approved, you can purchase a phone number and associate it with your 10DLC campaign. Associating a phone number with a 10DLC campaign can take approximately 14 days to complete. Although you can associate multiple phone numbers with a single campaign, you can't use the same phone number across multiple 10DLC campaigns. For each 10DLC campaign that you create, you must have at least one unique phone number. Throughput for 10DLC phone numbers is based on the company and campaign registration information that you provide. Each 10DLC number associated to a campaign supports 1 message part per second (MPS). To get the eligible throughput from your campaign applied to the associated 10DLC numbers, you need to submit a request to increase SMS sending rates.

If you have an existing unregistered long code in your AWS End User Messaging SMS account, you can request that it be converted to a 10DLC number. To convert an existing long code, complete the registration process, and then create a case in the AWS Support Center. In some situations, it isn't possible to convert an unregistered long code to a 10DLC phone number. In this case, you must request a new number through the AWS End User Messaging SMS console and associate it with your 10DLC campaign. For more information about using 10DLC with existing long codes, see [Associating a long code with a 10DLC campaign](registrations-10dlc-associate.md).

**Topics**
+ [10DLC capabilities](#registrations-10dlc-capabilities)
+ [10DLC registration process](registrations-10dlc-setup.md)
+ [10DLC brand registration form](registrations-10dlc-company.md)
+ [Resend a 10DLC brand email authentication](registrations-10dlc-auth.md)
+ [10DLC brand vetting form](registrations-10dlc-vetting.md)
+ [10DLC campaign registration form](registrations-10dlc-register-campaign.md)
+ [Associating a long code with a 10DLC campaign](registrations-10dlc-associate.md)
+ [10DLC registration and monthly fees](#registrations-10dlc-fees)
+ [10DLC cross-account access](registrations-10dlc-configure-cross-account-access.md)

## 10DLC capabilities
<a name="registrations-10dlc-capabilities"></a>

**Note**  
When your 10DLC campaign is approved, AWS End User Messaging SMS automatically applies the message throughput that the campaign qualifies for to the phone numbers associated with that campaign. You do not need to submit a separate request to increase the message parts per second (MPS) for those numbers.

The capabilities of 10DLC phone numbers depend on which mobile carriers your recipients use. AT&T provides a per-second send rate for each campaign. T-Mobile provides a daily limit on the number of messages that can be sent, with no separate per-second send rate. Verizon has not published throughput limits, but uses a filtering system for 10DLC that is designed to remove spam, unsolicited messages, and abusive content, with less emphasis on the actual message throughput.

Throughput is applied at the *campaign* level. All phone numbers associated with the same campaign share a single send rate limit, rather than each number having its own. Each associated phone number shows the campaign's send rate as its limit. Because the limit is shared, messages sent from multiple numbers on the same campaign count toward the same limit. For example, if a campaign has a send rate limit of 8 message parts per second (MPS), you can send up to 8 MPS from a single number on that campaign. You can also split that throughput across multiple numbers, such as 4 MPS from each of two numbers. In both cases, the combined rate across the campaign cannot exceed 8 MPS before messages are throttled.

The T-Mobile daily message cap is advisory and is applied per campaign for T-Mobile recipients. After a campaign reaches its daily message cap, additional messages to T-Mobile recipients fail until the cap resets. For instructions on viewing the current send rate limits and daily message caps for a phone number, see [View your current messaging limits](sms-limitations-mps-view.md).

To increase the throughput that a campaign qualifies for, you can request that your company registration be vetted. When you vet your company registration, a third-party verification provider analyzes your company details and provides a vetting score. A higher score can raise the throughput tier that your campaigns qualify for. Vetting scores are not applied retroactively: if you vet your company registration after you have already created a campaign, the new score is not applied to that existing campaign. For this reason, vet your company or brand *before* you create your 10DLC campaigns. There is a one-time charge for the vetting service. For more information, see [10DLC brand vetting form](registrations-10dlc-vetting.md).

Throughput rates for 10DLC are determined by the US mobile carriers in cooperation with the Campaign Registry. Neither AWS End User Messaging SMS nor any other SMS sending service can increase 10DLC throughput beyond these rates. If you need high throughput rates and high deliverability rates across all US carriers, we recommend that you use a short code. 

## 10DLC registration and monthly fees
<a name="registrations-10dlc-fees"></a>

There are registration and monthly fees associated with using 10DLC, such as registering your company and 10DLC campaign. These are separate from any other monthly or AWS fees. For more information about 10DLC fees, see the [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/) page.