

# SMS message handling
<a name="nx-security-sms-message-handling"></a>

AWS End User Messaging processes and stores SMS messages within the AWS Region selected by the customer. However, the final stages of SMS message delivery operate on international mobile networks beyond AWS control. As is typical in SMS message delivery, the SMS service providers that AWS uses may themselves use downstream service providers to route the SMS messages globally. These downstream service providers may route the SMS messages through endpoints or networks in different Regions from the AWS Region selected by the customer, even if the end user recipient of an SMS message is in the same Region.