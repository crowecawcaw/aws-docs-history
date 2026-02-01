Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Troubleshooting Identity Center authentication

Use the following sections to help troubleshoot problems that you have with Identity Center authentication.

###### Topics

- [API errors](#api-errors "#api-errors")
- [Connection errors](#connection-errors "#connection-errors")

## API errors

The `GetIdentityCenterAuthToken` API can return the following errors:

- **UnsupportedOperationFault** – The request was made without identity-enhanced credentials or Identity Center identity propagation is not supported in the current configuration.
- **ClusterNotFoundFault (redshift:GetIdentityCenterAuthToken)** – One or more of the specified cluster identifiers do not exist or you do not have permission to access them.
- **WorkgroupNotFoundFault (redshift-serverless:GetIdentityCenterAuthToken)** – One or more of the specified workgroup names do not exist or you do not have permission to access them.
- **InvalidParameterValueException** – The request parameters are invalid, such as an empty list of clusters or workgroups, or more than 20 items in the list.

## Connection errors

When connecting to Amazon Redshift using Identity Center tokens, you may encounter the following errors:

- **Token credentials expired or invalid** – Generate a new token using the `GetIdentityCenterAuthToken` API and update your connection configuration.
- **invalid token** – Verify the token format and ensure it was generated for the correct cluster or workgroup.
- **TYPE_INVALID_TOKEN** – Ensure you're using `token_type = SUBJECT_TOKEN` in your connection parameters.
- **identity provider type "awsidc" is not supported** – Verify your Amazon Redshift cluster or workgroup supports Identity Center authentication and update to a compatible version.
- **AWS IdC identity provider does not exist** – Configure Identity Center integration for your Amazon Redshift resource through the AWS console.
- **Invalid scope. User's credentials are not authorized to connect to Amazon Redshift** – Verify the user has appropriate permissions in Identity Center and the token was generated for the correct resources.
