

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Gmail connector overview
<a name="gmail-overview"></a>

The following table gives an overview of the Gmail connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Latest Connector:** Google Service Account / **Legacy Connector:** Google Service Account
  - **Feature:** Authentication credentials / **Latest Connector:**  +  Google service account <br />+  Admin account email <br />+  Client email <br />+  Private key   / **Legacy Connector:**  +  Google service account <br />+  Admin account email <br />+  Client email <br />+  Private key  
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Latest Connector:** Yes (Automatic) / **Legacy Connector:** Yes (Manual configuration)
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Latest Connector:** Yes (Automatic) / **Legacy Connector:** Yes (Manual configuration)
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Latest Connector:** No / **Legacy Connector:** Yes

- ****
  - **Feature:** Customer Managed Key (CMK) support
  - **Latest Connector:** No
  - **Legacy Connector:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Latest Connector:** No / **Legacy Connector:** No
  - **Feature:** Entities / **Latest Connector:** Messages (automatic), Draft emails (configurable) / **Legacy Connector:** Messages, Attachments (configurable)
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Latest Connector:** No (Uses optimized defaults) / **Legacy Connector:** Yes (Configurable)
  - **Feature:** Filters / **Latest Connector:** No / **Legacy Connector:** Date range, Attachments (regex), Domains, Keywords, Labels

- ****[Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode)****
  - **Feature:** Sync mode
  - **Latest Connector:** No (Optimized automatic sync)
  - **Legacy Connector:** Yes (Full and incremental sync)

