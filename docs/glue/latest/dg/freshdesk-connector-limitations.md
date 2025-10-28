# Limitations and notes for Freshdesk connector

The following are limitations or notes for the Freshdesk connector:

- The `Company`, `Contacts`, and `Tickets` entities with filtration have pagination limitations. They return only 30 records per page and the page value can be set up to a maximum of 10 (fetching a maximum of 300 records).
- The `Tickets` entity does not fetch records older than 30 days.
- The `Company`, `Contacts`, and `Tickets` entities support the 'Date' datatype in filtration. You should select the 'Daily' onward trigger frequencies for these three entities. Selecting 'Minutes' or 'Hourly' can lead to duplicate data. Also, while selecting these fields for filtration, only the date value should be selected, since it will only consider the date portion of the selected timestamp.
- The number of API calls per minute is based on your plan. This limit is applied on an account wide basis irrespective of factors such as the number of agents or IP addresses used to make the calls. For all trial users, there is a default API limit of 50 calls/minute. For more details, refer to [Freshdesk](https://developer.freshdesk.com/api/#ratelimit "https://developer.freshdesk.com/api/#ratelimit")
- For any entity, only one Export/Async Job is processed at a time. A new job will only be processed once the existing job has completed successfully or failed. For more details, refer to [Freshdesk](https://developers.freshdesk.com/api/#export_contact "https://developers.freshdesk.com/api/#export_contact")
- The following fields are supported for Sync API calls, but are not supported/allowed to be passed in Async API request body.
  - id
  - created_at
  - updated_at
  - updated_since
  - active
  - company_id
  - other_companies
  - avatar
  - view_all_tickets
  - deleted
  - other_emails
  - state
  - tag
  - tags
