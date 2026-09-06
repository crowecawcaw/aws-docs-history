

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Configure RFC email notifications (console)
<a name="ex-rfc-email-notices"></a>

The AMS console **Requests for Change** create page provides you with an option to add email addresses to receive notifications of RFC state changes:

![Add email addresses to receive notifications of RFC state changes.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/emailNoticeOption2.png)


Additionally, you can add email addresses for notifications to any change type, for example:

```
aws amscm create-rfc --change-type-id <Change type ID>
                    --change-type-version 1.0 --title "TITLE"
                    --notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"
```

Add a similar line (`--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"`) to any change type inline or template request in the RFC parameters part of the request, not the parameters part.