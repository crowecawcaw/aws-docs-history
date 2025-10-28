Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_IDENTITY_PROVIDERS

The SVV_IDENTITY_PROVIDERS view returns the name and additional properties for
identity providers. For more information about how to create an identity provider, see
[CREATE IDENTITY PROVIDER](r_CREATE_IDENTITY_PROVIDER.md "r_CREATE_IDENTITY_PROVIDER.md").

SVV_IDENTITY_PROVIDERS is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name | Data type | Description                                                   |
| ----------- | --------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ---------- | ------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------------------------------ | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| uid         | integer   | The unique ID of the registered identity provider.            |
| name        | text      | The identity provider name.                                   |
| type        | text      | The identity provider type.                                   |
| instanceid  | text      | The unique differentiator between instances of the same type. |
| namespc     | text      | The namespace prefix of the identity provider.                |
| params      | text      | The JSON object with parameters for the identity provider.    |
| enabled     | bool      | Indicates if the identity provider is enabled.                | ### Sample queries To view identity provider properties, run a query like the following after creating identity providers. `SELECT name, type, instanceid, namespc, params, enabled FROM svv_identity_providers ORDER BY 1;` The sample output includes param descriptions. ``` name | type | instanceid | namespc | params | enabled ------------------+-------+--------------------------------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------- rs5517_azure_idp | azure | e40d4bb2-7670-44ae-bfb8-5db013221d73 | abc | {"issuer":"https://login.microsoftonline.com/e40d4bb2-7670-44ae-bfb8-5db013221d73/v2.0", "client_id":"871c010f-5e61-4fb1-83ac-98610a7e9110", "client_secret":, "audience":["https://analysis.windows.net/powerbi/connector/AmazonRedshift", "https://analysis.windows.net/powerbi/connector/AWSRDS"]} | t (1 row) ``` |
