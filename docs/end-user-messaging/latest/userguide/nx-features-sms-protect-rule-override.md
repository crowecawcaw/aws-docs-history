

# Phone number override rules in AWS End User Messaging
<a name="nx-features-sms-protect-rule-override"></a>

You can use a phone number override rule to override the country mode and ensure important phone numbers are always allowed or blocked. For example if you have an application that you only want to be able to send messages to your employees, you could block sending to every country and add phone number override rules for each employee phone number.

Additionally, you can integrate with your customer data platforms (CDPs), contact centers, or other internal tools to dynamically apply overrides based on customer value or support requests. For example, high-value customers identified in a CDP could receive SMS message allowlists, or a customer support agent could initiate an override for a customer complaining about not receiving SMS messages. Phone number overrides can be set as permanent or with an expiration date.

**Topics**
+ [How phone number override rules are processed](nx-features-sms-protect-rule-override-processing.md)
+ [Create a phone number override rule](nx-features-sms-protect-rule-override-create.md)
+ [Query phone number override rule](nx-features-sms-protect-rule-override-querying.md)
+ [Edit a phone number override rule](nx-features-sms-protect-rule-override-update.md)
+ [Delete a phone number override rule](nx-features-sms-protect-rule-override-delete.md)