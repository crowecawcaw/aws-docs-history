# Limitations and notes for Salesforce Marketing Cloud connector

The following are limitations or notes for the Salesforce Marketing Cloud connector:

- When using filter on DateTime datatype field, you need to pass the value in the format "yyyy-mm-ddThh:MM:ssZ".
- In Data Preview, the Boolean Datatype value comes as a Blank.
- For SOAP entities, you can define a maximum of two filters, and for REST entities, you can define only one filter, which restricts testing partitioning with filters.
- Several unexpected behaviors have been observed from the SaaS side: the `Link.Alias` field in the `linksend` entity does not support the CONTAINS operator (for example, `Link.Alias CONTAINS "ViewPrivacyPolicy"`), and filter operators for Data Extension entities (such as EQUALS and GREATER THAN) do not return the expected results.
- The SFMC ClickEvent SOAP API has a delay in reflecting newly created records so, the records created recently may not be immediately available in the API response.

Example: If you create 5 new ClickEvent records at **2025-01-10T14:30:00** and immediately fetch them using the SOAP API, the response might not include all 5 records. It may take up to 5 minutes for the newly created records to appear in the API response. This delay can affect both data retrieval and scheduled runs as well.

- Two different DateTime formats: **2025-03-11T04:46:00** (without milliseconds) and **2025-03-11T04:46:00.000Z** are supported when performing write operations in AWS Glue (with milliseconds).
- For the Event Notification Subscription entity, a subscription can only be created for a verified callback URL, and you can have up to 200 subscriptions per callback.
- For the Event Notification Callback entity, a maximum of 50 records can be created per account.
