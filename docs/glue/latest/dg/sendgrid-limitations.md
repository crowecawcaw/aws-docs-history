# SendGrid limitations

The following are limitations or notes for SendGrid:

- Incremental pull is only supported by the Stats entity on the `start_date` field and by the Contact entity on the `event_timestamp` field.
- Pagination is only supported by the Marketing Campaign Stats (Automations), Marketing Campaign Stats (Single Sends), Single Sends, and Lists entities.
- For the Stats entity, `start_date` is a mandatory filter parameter.
- An API key with Restricted Access can’t support read access for the Email API and Stats entities. Use an API key with Full Access. For more information, see [API Overview](https://www.twilio.com/docs/sendgrid/api-reference/api-keys/create-api-keys#api-overview "https://www.twilio.com/docs/sendgrid/api-reference/api-keys/create-api-keys#api-overview").
