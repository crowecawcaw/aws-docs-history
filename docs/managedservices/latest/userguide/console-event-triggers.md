# Email notifications

You can add email addresses to receive RFC state changes to an RFC that you create in the AMS console,
or by using the AMS API/CLI.

In the AMS console, use the **Email notifications** option, on the second page of the
Create RFC wizard:

![Email notification options are under general configurations.](images/emailNoticeOption2.png)
In the AMS API/CLI, add a line like this to the RFC parameters section of your RFC (do not add the line
to the run parameters section):

```
--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"
```

The behavior of the notifications varies depending the RFC scheduling type:

- Scheduled RFCs receive email notifications on : Submitted, Scheduled, InProgress, Completed,
  Rejected, Canceled, Auto-Rejected, or Auto-Canceled.
- ASAP RFCs receive email notification on: Submitted, InProgress, Completed, Rejected, Canceled,
  AutoRejected, or Auto-Canceled.

###### Note

- Email notifications are sent from this address:
  `no-reply@managedservices.amazonaws.com`.
- Special characters and URLs in your RFC title are redacted in the emails we send. This is a
  security measure.
