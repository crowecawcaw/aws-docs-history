

# Configuring Workday Live Data Query

Before you can use AWS Glue to query data from Workday Live Data Query, you must meet these requirements.

## Minimum requirements
<a name="workday-ldq-configuring-min-requirements"></a>

The following are minimum requirements:
+ You have a Workday tenant with Workday Data Cloud, and Live Data Query is available for your tenant. Depending on your subscription, you might need extra steps to enable it.
+ You have an Integration System User (ISU) in your Workday tenant. The ISU belongs to an unconstrained integration system security group that has View Only permission on the domains that secure the tables and fields you want to read. Those domain permissions determine which tables and columns AWS Glue can read through the connection.
+ You have registered an API client in your Workday tenant for the ISU, with the JWT Bearer Grant client grant type and an x509 public certificate, and with Include Workday Owned Scope selected.
+ You have the RSA private key, in PEM format, that matches the x509 public certificate registered for the API client.

For more information, see the following topics in the Workday documentation:
+ [Get Started with Workday Live Data Query](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/workday-live-data-query.html)
+ [Set Up Live Data Query ISU Authentication in Workday](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/set-up-live-data-query-isu-authentication.html?toc=2.1.1)
+ [Generate Public and Private Keys for Workday Live Data Query](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/generate-public-and-private-keys-for-workday-live-.html?toc=2.1.7)
+ [Data Cloud Catalog](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/data-cloud-catalog.html?toc=2.0)

If you meet these requirements, you're ready to connect AWS Glue to your Workday tenant. For typical connections, you don't need to do anything else in Workday.

## Information to collect from your Workday administrator
<a name="workday-ldq-configuring-info-to-collect"></a>

Collect the following values from your Workday administrator. Workday displays the token endpoint, Integration System User, and client ID after you complete the Register API Client task.


**Information to collect from your Workday administrator**  

| Value | Description | Example | 
| --- | --- | --- | 
| Workday Data Service host | The host name of the Workday service that runs Live Data Query queries. | The {HOST1} value from the Token Endpoint on the API Client you created in the ISU setup. | 
| Token endpoint | The Workday OAuth 2.0 URL that issues access tokens for your tenant. | https://{{host}}/ccx/oauth2/{{tenant}}/token | 
| Client ID | The client ID of the API client registered for the ISU. | MThmMWI3YWEtZDZjMS00MzRmLTliZWBeMzg4ZjI2NmI1MjFl4 | 
| Integration System User | The user name of the ISU. AWS Glue uses it as the subject of the JWT. | demo-isu | 
| Private key | The PEM-formatted RSA private key that AWS Glue uses to sign the JWT. | -----BEGIN PRIVATE KEY----- … -----END PRIVATE KEY----- | 