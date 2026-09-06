

# Singapore sender ID registration process
<a name="registrations-sg"></a>

AWS End User Messaging SMS customers are able to send SMS traffic in Singapore using a Sender ID that has been registered through the Singapore SMS Sender ID Registry (SSIR). SSIR was launched in March of 2022 through the Singapore Network Information Centre (SGNIC) which is owned by Info-communications Media Development Authority (IMDA) of Singapore, and enables organizations to register their Sender ID when sending SMS to mobile phones in Singapore. To use a registered Singapore Sender ID you must obtain a Unique Entity Number (UEN), then submit a request to AWS End User Messaging SMS to allow-list your account for usage of your Sender ID and finally complete the registration process through SSIR. 

If you do not register your sender ID any message sent using a sender ID will have its ID changed to **LIKELY-SCAM** per regulatory agency rules. Regulators will filter or block unregistered traffic at their discretion. 

**Important**  
Your Singapore registration must be completed in this order:  
[Registering for a Singapore Unique Entity Number (UEN)](registrations-sg-uen.md)
[Create a new registration using the AWS End User Messaging SMS console](registrations-create.md) with **Registration type** set to Singapore sender ID registration and complete the registration form.
[Registering a Sender ID with Singapore Network Information Centre (SGNIC)](registrations-sg-sgnic.md)

**Topics**
+ [Singapore Unique Entity Number (UEN)](registrations-sg-uen.md)
+ [Singapore sender ID registration form](registrations-sg-form.md)
+ [Register a Sender ID with Singapore Network Information Centre (SGNIC)](registrations-sg-sgnic.md)
+ [Singapore sender ID registration frequently asked questions](registrations-sg-faq.md)