

# Best practices
<a name="nx-sms-scale-best-practices"></a>

For the best results when creating and sending messages, we recommend that you follow the best practices in this topic. Mobile phone carriers continuously audit bulk SMS and MMS senders and throttle or block messages from originators that they determine to be sending unsolicited messages. Sending unsolicited content is also a violation of the [acceptable use policy](https://aws.amazon.com/aup/#No_E-Mail_or_Other_Message_Abuse), and the AWS End User Messaging team routinely audits SMS and MMS messages.

**Important**  
This topic describes several best practices that might help you improve your customer engagement and avoid costly penalties. However, this topic doesn't contain legal advice. Always consult an attorney to obtain legal advice.

**Topics**
+ [Comply with laws, regulations, and carrier requirements](#nx-sms-best-practices-laws)
+ [Prohibited message content](#nx-sms-best-practices-content)
+ [Obtain permission](#nx-sms-best-practices-permission)
+ [Manage your customer lists](#nx-sms-best-practices-lists)
+ [Make your messages clear, honest, and concise](#nx-sms-best-practices-clear)
+ [Respond appropriately](#nx-sms-best-practices-respond)
+ [Adjust your sending based on engagement](#nx-sms-best-practices-engagement)
+ [Send at appropriate times](#nx-sms-best-practices-times)
+ [Use dedicated short codes](#nx-sms-best-practices-short-codes)
+ [Verify your destination phone numbers](#nx-sms-best-practices-verify)
+ [Voice best practices](#nx-sms-best-practices-voice)

## Comply with laws, regulations, and carrier requirements
<a name="nx-sms-best-practices-laws"></a>

You can face significant fines and penalties if you violate the laws and regulations of the places where your customers reside. For this reason, it's vital to understand the laws related to SMS and MMS messaging in each country or region where you do business.

**Important**  
In many countries, the local carriers ultimately have the authority to determine what kind of traffic flows over their networks. This means that the carriers might impose restrictions on SMS and MMS content that exceed the minimum requirements of local laws.

Key laws that apply to SMS and MMS communications in some major markets include the Telephone Consumer Protection Act (TCPA) in the United States, the Privacy and Electronic Communications Regulations (PECR) in the United Kingdom, the ePrivacy Directive in the European Union, Canada's Anti-Spam Law (CASL), and the Act on Regulation of Transmission of Specific Electronic Mail in Japan. As a sender, these laws can apply to you even if your company isn't based in one of these countries. Consult an attorney in each country or region where your customers are located to obtain legal advice.

## Prohibited message content
<a name="nx-sms-best-practices-content"></a>

Some countries or mobile carriers require that you register your number or sender ID before live messaging is enabled. When using or registering a number as an originator, follow these guidelines: provide a valid opt-in workflow to register the number; don't use shortened URLs created from third-party URL shorteners, as these messages are more likely to be filtered as spam; and don't send the same or similar message content using multiple numbers, which is considered snowshoe spamming.

Messages related to certain industries can be considered restricted, and are subject to heavy filtering or being blocked outright. This can include one-time passwords and multi-factor authentication for services related to restricted categories. The following table describes the types of restricted content.


| Category | Examples | 
| --- | --- | 
| Gambling | Casinos, sweepstakes, apps or websites that offer gambling, 50/50 raffles, betting or sports picks | 
| High-risk financial services | Payday loans, short-term high-interest loans, auto loans, mortgage loans, student loans, debt collection, stock alerts, cryptocurrency | 
| Debt forgiveness | Debt consolidation, debt reduction, credit repair programs, debt relief, third-party debt collection | 
| Get-rich-quick schemes | Work-from-home programs, risk-investment opportunities, pyramid or multi-level marketing schemes, mystery shopping | 
| Illegal substances | Cannabis or CBD, kratom, paraphernalia products, fireworks, vape or e-cig | 
| Prescription drugs | Drugs that require a prescription | 
| Phishing or smishing | Attempts to get users to reveal personal or login information, including security awareness training that simulates phishing or smishing attacks | 
| S.H.A.F.T. | Sex, hate, alcohol, firearms, tobacco or vape | 
| Third-party lead generation | Companies that buy, sell, or share consumer information, affiliate lending, affiliate marketing, deceptive marketing | 

## Obtain permission
<a name="nx-sms-best-practices-permission"></a>

Never send messages to recipients who haven't explicitly asked to receive the specific types of messages that you plan to send. Don't share opt-in lists, even among organizations within the same company. When you receive an SMS or MMS opt-in request, send the recipient a message that asks them to confirm that they want to receive messages from you, and don't send any additional messages until they confirm. A subscription confirmation message might resemble the following example:

`Text YES to join ExampleCorp alerts. 2 msgs/month. Msg & data rates may apply. Reply HELP for help, STOP to cancel.`

Maintain records that include the date, time, and source of each opt-in request and confirmation. This might be useful if a carrier or regulatory agency requests it.

### Opt-in workflow
<a name="nx-sms-best-practices-permission-optin"></a>

In some cases, such as US toll-free or short code registration, mobile carriers require you to provide mockups or screenshots of your entire opt-in workflow. The mockups or screenshots must closely resemble the opt-in workflow that your recipients will complete, and should include all of the following required disclosures:

**Required disclosures for your opt-in**
+ A description of the messaging use case that you will send through your program.
+ The phrase "Message and data rates may apply."
+ An indication of how often recipients will get messages from you.
+ Publicly accessible links to your Terms and Conditions and Privacy Policy documents.

The following example complies with the mobile carriers' requirements for a multi-factor authentication use case.

![Showing the workflow for multi-factor authentication.](https://docs.aws.amazon.com/end-user-messaging/latest/userguide/images/best-practices-usecase.png)


It contains finalized text and images, and shows the entire opt-in flow, complete with annotations. In the opt-in flow, the customer must take distinct, intentional actions to provide their consent to receive text messages, and it contains all of the required disclosures.

### SMS and MMS specific Terms and Conditions
<a name="nx-sms-best-practices-permission-terms"></a>

Mobile carriers also require that you make a specific set of SMS and MMS Terms and Conditions available to your customers. These terms describe what you send when a customer opts in, how to cancel by texting STOP, how to get help by texting HELP, the carriers you can deliver to, that message and data rates may apply, and a link to your privacy policy. If you don't provide your customers with a copy of these terms, the carriers won't approve your short code application.

## Manage your customer lists
<a name="nx-sms-best-practices-lists"></a>

People change phone numbers often, so don't use an old list of phone numbers for a new messaging program. If you send recurring SMS or MMS messages, audit your customer lists on a regular basis so that the only customers who receive your messages are those who are interested in receiving them. Keep records that show when each customer requested to receive messages from you, and which messages you sent to each customer. Occasionally, a carrier or regulatory agency asks us to provide proof that a customer opted to receive messages from you; if you can't provide the necessary information, we might pause your ability to send additional SMS and MMS messages.

## Make your messages clear, honest, and concise
<a name="nx-sms-best-practices-clear"></a>

SMS is a unique medium. The 160-character-per-message limit means that your messages must be concise, and techniques that you might use in other channels might seem dishonest or deceptive when used with SMS. The following practices help you create an effective message body:
+ Identify yourself as the sender by including an identifying program name at the beginning of each message.
+ Don't try to make your message look like a person-to-person message, because this technique might make your message seem like a phishing attempt.
+ Be careful when talking about money, and don't use currency symbols or offers that seem too good to be true.
+ Use only the necessary characters. Characters outside the GSM 03.38 alphabet, such as trademark symbols, cause your message to be sent using a different encoding that supports only 70 characters per message part, which can split your message into more parts and cost more.
+ Use valid, safe links, and avoid free link-shortening services because carriers tend to filter messages that include links on those domains.
+ Limit the number of abbreviations that you use, because the overuse of abbreviations can seem unprofessional and could cause some users to report your message as spam.

## Respond appropriately
<a name="nx-sms-best-practices-respond"></a>

When a recipient replies to your messages, respond with useful information. For example, when a customer responds with the keyword HELP, send them information about the program that they're subscribed to, the number of messages you send each month, and how to contact you. When a customer replies with the keyword STOP, let them know that they won't receive any further messages.

## Adjust your sending based on engagement
<a name="nx-sms-best-practices-engagement"></a>

Your customers' priorities can change over time. For customers who rarely engage with your messages, adjust the frequency of your messages, and remove customers who are completely unengaged from your customer lists. This prevents customers from becoming frustrated, saves you money, and helps protect your reputation as a sender.

## Send at appropriate times
<a name="nx-sms-best-practices-times"></a>

Send messages during normal daytime business hours. If you send messages at dinner time or in the middle of the night, there's a good chance that your customers will unsubscribe from your lists. If you send to very large audiences, double-check the throughput rates for your originator phone numbers and divide the number of recipients by your throughput rate to determine how long it will take to reach all of your recipients.

## Use dedicated short codes
<a name="nx-sms-best-practices-short-codes"></a>

If you use short codes, maintain a separate short code for each brand and each type of message. For example, if you send both transactional and promotional messages, use a separate short code for each type, or register the short code once for transactional and create another registration for promotional. For more information about requesting short codes, see [Phone numbers](nx-features-phone-numbers.md).

## Verify your destination phone numbers
<a name="nx-sms-best-practices-verify"></a>

When AWS End User Messaging accepts a request to send an SMS or MMS message, you're charged for sending that message, even if the intended recipient doesn't actually receive it. For this reason, you should validate that the phone numbers that you send messages to are valid mobile numbers. For more information about SMS and MMS pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

## Voice best practices
<a name="nx-sms-best-practices-voice"></a>

This section contains several best practices related to sending voice messages using AWS End User Messaging. These practices can help with the satisfaction of your recipients, and can protect you from unexpected charges. Comply with the laws and regulations of the places where your customers reside, send messages only during normal daytime business hours in each recipient's time zone, and avoid sending the same message across multiple channels at the same time.

Because voice calls can be expensive, it's important to secure your AWS account against unauthorized access and to monitor the destinations of the messages that you send. Carefully manage IAM roles, policies, and users so that they grant least privilege, and rotate credentials regularly. Know which country you're sending to, because the per-minute price depends on the recipient's country and the country code isn't always a reliable indicator. Limit your sending to specific countries, and limit the number of messages that you send to a single number.