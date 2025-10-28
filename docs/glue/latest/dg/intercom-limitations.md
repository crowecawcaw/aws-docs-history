# Limitations

The following are limitations for the Intercom connector:

- When using the Company entity, there is a limit of 10,000 Companies that can be returned.
  For more information, see
  [List all companies API](https://developers.intercom.com/docs/references/2.5/rest-api/companies/list-companies "https://developers.intercom.com/docs/references/2.5/rest-api/companies/list-companies").
- While applying order by, filter is mandatory for both **Contact** and
  **Conversation** entities.
- MCA is supported by the SaaS provider. However, based on the API rate limits mentioned in the documentation,
  we will not host MCA on AWS Glue as it may impact other workloads and potentially cause performance issues due to
  resource contention.
