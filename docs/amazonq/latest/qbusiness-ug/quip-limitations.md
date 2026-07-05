Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Known limitations for the Amazon Q Business Quip connector

The Quip connector has the following known limitations:

- Only **Full sync** is supported by default. For
  **New, modified, or deleted content sync**, Admin API
  access is required and Admin API has to be enabled on the Quip
  website .
- Only data in shared folders will be crawled by the Amazon Q
  Quip connector. Private folders, other than the private folders
  belonging to the Private Access Token user, will not be crawled.
- Quip doesn't store file types and file paths. Amazon Q Quip connector can't support inclusion and exclusion filters on
  these.
