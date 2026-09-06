

# Keywords in AWS End User Messaging SMS
<a name="keywords"></a>

A *keyword* is a specific word or phrase that a customer can send to your phone number to elicit a response, such as an informational message, opting-in to receive more messages, a special offer and other promotional and transactional messages. When your number receives a message that begins with a keyword, AWS End User Messaging SMS responds with a customizable message.

For short codes, the console shows the keywords and responses that you initially define when you request a short code from Support. Support registers your keywords and responses with wireless carriers when it provisions your short code.

For long codes, the console shows the default keywords and responses.

**Important**  
Your keywords and response messages must comply with the guidelines that are set by wireless carriers and wireless industry groups. Otherwise, following an audit, such groups might take action against your short code or long code. This action can include deny listing your number and blocking your messages.

A keyword can be between 1 and 30 characters in length and can't start or end with a space. Keywords are case insensitive.

For AWS RCS Agents, keywords are configured on the AWS RCS Agent and apply to all associated RCS for Business IDs (testing agent and country launch agents). When an end user sends a message containing a keyword to your AWS RCS Agent, AWS End User Messaging SMS responds with the configured keyword response. For more information about receiving inbound RCS messages and keyword handling, see [Receiving inbound RCS messages](rcs-inbound.md).

Wireless carriers in the US require short codes to support the following keywords. In addition, AWS expects all long codes and short codes to support these keywords:

HELP  
Used to obtain customer support. The response message must include customer-support contact information, as in the following example:  
*"For assistance with your account, call (206) 555-0199."*

STOP  
Used to opt out of receiving messages from your number. In addition to *STOP*, your audience can use any supported opt-out keyword, such as *CANCEL* or *OPTOUT*. For a list of supported opt-out keywords, see [Required opt-out keywords](keywords-required.md). After your number receives an SMS message that contains an opt-out keyword, AWS End User Messaging SMS stops sending SMS messages from your account to the individual who opted out.   
The response message must confirm that messages will stop being sent to the individual who opted out, as in the following example:  
*"You are now opted out and will no longer receive messages."*

**Topics**
+ [Required opt-out keywords](keywords-required.md)
+ [Keyword actions](keywords-actions.md)
+ [Add a keyword to a phone number](keywords-manage-phone-number.md)
+ [View the keywords used by a phone number](keywords-phone-number-list.md)
+ [Edit a keyword used by a phone number](keywords-phone-number-edit.md)
+ [Delete a keyword from a phone number](keywords-phone-number-delete.md)
+ [Add a keyword to a phone pool](keywords-pool-add.md)
+ [View keywords used by a phone pool](keywords-pool-list.md)
+ [Edit a keyword in a phone pool](keywords-pool-edit.md)
+ [Delete a keyword from a phone pool](keywords-pool-delete.md)