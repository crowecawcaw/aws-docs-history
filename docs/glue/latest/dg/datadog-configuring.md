# Configuring Datadog

Before you can use AWS Glue to transfer from Datadog, you must meet the following
requirements:

## Minimum requirements

- You have a Datadog account with DD-API-KEY and DD-APPLICATION-KEY. For
  more information about creating an account, see [Creating a Datadog account](datadog-create-account.md "datadog-create-account.md").
- Your Datadog account has API access with valid license.

Datadog supports the following six URLs. All Datadog API clients are configured by default to consume Datadog US1 site APIs.
If you are on the Datadog EU site, you must select https://api.datadoghq.eu URL with the `DD-API-KEY` and `DD-APPLICATION-KEY` of the
Datadog EU site to access the APIs. Similarly, for other sites, you should select the respective
URLs with the `DD-API-KEY and DD-APPLICATION-KEY` of the respective site.

- US1 API URL — [https://api.datadoghq.com](https://api.datadoghq.com "https://api.datadoghq.com")https://api.datadoghq.com
- EU API URL — [https://api.datadoghq.eu](https://api.datadoghq.eu "https://api.datadoghq.eu")
- US3 API URL — [https://api.us3.datadoghq.com](https://api.us3.datadoghq.com "https://api.us3.datadoghq.com")
- US5 API URL — [https://api.us5.datadoghq.com](https://api.us5.datadoghq.com "https://api.us5.datadoghq.com")
- S1-FED API URL — [https://api.ddog-gov.com](https://api.ddog-gov.com "https://api.ddog-gov.com")
- Japan API URL — [https://api.ap1.datadoghq.com](https://api.ap1.datadoghq.com "https://api.ap1.datadoghq.com")

If you meet these requirements, you’re ready to connect AWS Glue to your Datadog
account.
