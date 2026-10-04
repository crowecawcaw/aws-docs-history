

# Best practices
<a name="nx-voice-scale-best-practices"></a>

For the best results when creating and sending voice messages, we recommend that you follow the best practices in this topic. Following these practices can help with the satisfaction of your recipients, protect your sender reputation, and protect you from unexpected charges. Sending unsolicited content is a violation of the [acceptable use policy](https://aws.amazon.com/aup/#No_E-Mail_or_Other_Message_Abuse), and the AWS End User Messaging team routinely audits voice messages.

**Important**  
This topic describes several best practices that might help you improve your customer engagement and avoid costly penalties. However, this topic doesn't contain legal advice. Always consult an attorney to obtain legal advice.

**Topics**
+ [Comply with laws, regulations, and carrier requirements](#nx-voice-scale-best-practices-laws)
+ [Obtain permission](#nx-voice-scale-best-practices-permission)
+ [Manage your customer lists](#nx-voice-scale-best-practices-lists)
+ [Respond appropriately](#nx-voice-scale-best-practices-respond)
+ [Adjust your sending based on engagement](#nx-voice-scale-best-practices-engagement)
+ [Send at appropriate times](#nx-voice-scale-best-practices-times)
+ [Protect against unexpected charges](#nx-voice-scale-best-practices-voice)

## Comply with laws, regulations, and carrier requirements
<a name="nx-voice-scale-best-practices-laws"></a>

You can face significant fines and penalties if you violate the laws and regulations of the places where your customers reside. For this reason, it's vital to understand the laws related to voice messaging in each country or region where you do business.

**Important**  
In many countries, the local carriers ultimately have the authority to determine what kind of traffic flows over their networks. This means that the carriers might impose restrictions on voice content that exceed the minimum requirements of local laws.

Key laws that apply to voice communications in some major markets include the Telephone Consumer Protection Act (TCPA) in the United States. As a sender, these laws can apply to you even if your company isn't based in one of these countries. Consult an attorney in each country or region where your customers are located to obtain legal advice.

## Obtain permission
<a name="nx-voice-scale-best-practices-permission"></a>

Never send voice messages to recipients who haven't explicitly asked to receive the specific types of messages that you plan to send. Don't share opt-in lists, even among organizations within the same company. When you receive an opt-in request, confirm that the recipient wants to receive voice messages from you before you place any additional calls.

Maintain records that include the date, time, and source of each opt-in request and confirmation. This might be useful if a carrier or regulatory agency requests it.

### Opt-in workflow
<a name="nx-voice-scale-best-practices-permission-optin"></a>

Provide a clear opt-in workflow that your recipients complete before you send them voice messages. The opt-in should include a description of the voice messaging use case that you will send through your program, an indication of how often recipients will get messages from you, and publicly accessible links to your Terms and Conditions and Privacy Policy documents. In the opt-in flow, the customer must take distinct, intentional actions to provide their consent to receive voice messages.

## Manage your customer lists
<a name="nx-voice-scale-best-practices-lists"></a>

People change phone numbers often, so don't use an old list of phone numbers for a new voice messaging program. If you send recurring voice messages, audit your customer lists on a regular basis so that the only customers who receive your messages are those who are interested in receiving them. Keep records that show when each customer requested to receive messages from you, and which messages you sent to each customer. Occasionally, a carrier or regulatory agency asks us to provide proof that a customer opted to receive messages from you; if you can't provide the necessary information, we might pause your ability to send additional voice messages.

## Respond appropriately
<a name="nx-voice-scale-best-practices-respond"></a>

Give recipients a clear and easy way to opt out of future voice messages, and honor opt-out requests promptly. When a recipient asks to stop receiving messages, let them know that they won't receive any further calls.

## Adjust your sending based on engagement
<a name="nx-voice-scale-best-practices-engagement"></a>

Your customers' priorities can change over time. For customers who rarely engage with your messages, adjust the frequency of your messages, and remove customers who are completely unengaged from your customer lists. This prevents customers from becoming frustrated, saves you money, and helps protect your reputation as a sender.

## Send at appropriate times
<a name="nx-voice-scale-best-practices-times"></a>

Send voice messages during normal daytime business hours in each recipient's time zone. If you place calls at dinner time or in the middle of the night, there's a good chance that your customers will opt out of your program.

## Protect against unexpected charges
<a name="nx-voice-scale-best-practices-voice"></a>

Because voice calls can be expensive, it's important to secure your AWS account against unauthorized access and to monitor the destinations of the messages that you send. Carefully manage IAM roles, policies, and users so that they grant least privilege, and rotate credentials regularly. Know which country you're sending to, because the per-minute price depends on the recipient's country and the country code isn't always a reliable indicator. Limit your sending to specific countries, and limit the number of messages that you send to a single number.