

# Troubleshoot AppClients in AppFabric for productivity
<a name="ahead-app-dev-errors"></a>


|  | 
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. | 

This section describes common errors and troubleshooting for AppFabric for productivity.

## Unverified application
<a name="unverified-application"></a>

App developers that use AppFabric for productivity to enrich their app experiences will go through a verification process prior to launching their features to end users. All applications start as unverified and change to verified only when the verification process is complete. This means that the `starterUserEmails` you used when creating an AppClient will see this message.

![Warning message for an unverified application in AWS AppFabric, requesting data access.](http://docs.aws.amazon.com/appfabric/latest/adminguide/images/fabric-24.png)


## `CreateAppClient` errors
<a name="dev-errors-CreateAppClient"></a>

### ServiceQuotaExceededException
<a name="service-quota-exceeded"></a>

If you receive the following exception when creating an AppClient, you've exceeded the number of AppClients that can be created per AWS account. The limit is 1. HTTP Status Code: 402

```
ServiceQuotaExceededException / SERVICE_QUOTA_EXCEEDED
You have exceeded the number of AppClients that can be created per AWS Account. The limit is 1.
HTTP Status Code: 402
```

## `GetAppClient` errors
<a name="dev-errors-GetAppClient"></a>

### ResourceNotFoundException
<a name="get-app-client-not-found"></a>

If you receive the following exception when getting details for an AppClient, ensure you’ve entered the correct AppClient identifier. This error signifies that the specified AppClient was not found.

```
ResourceNotFoundException / APP_CLIENT_NOT_FOUND
The specified AppClient is not found. Ensure you’ve entered the correct AppClient identifier.
HTTP Status Code: 404
```

## `DeleteAppClient` errors
<a name="dev-errors-DeleteAppClient"></a>

### ConflictException
<a name="another-delete-request"></a>

If you receive the following exception when deleting an AppClient, another delete request is in progress. Wait until it completes then try again. HTTP Status Code: 409

```
ConflictException
Another delete request is in progress. Wait until it completes then try again.
HTTP Status Code: 409
```

### ResourceNotFoundException
<a name="delete-app-client-not-found"></a>

If you receive the following exception when deleting an AppClient, ensure you’ve entered the correct AppClient identifier. This error signifies that the specified AppClient was not found.

```
ResourceNotFoundException / APP_CLIENT_NOT_FOUND
The specified AppClient is not found. Ensure you’ve entered the correct AppClient identifier.
HTTP Status Code: 404
```

## `UpdateAppClient` errors
<a name="dev-errors-UpdateAppClient"></a>

### ResourceNotFoundException
<a name="update-app-client-not-found"></a>

If you receive the following exception when updating an AppClient, ensure you’ve entered the correct AppClient identifier. This error signifies that the specified AppClient was not found.

```
ResourceNotFoundException / APP_CLIENT_NOT_FOUND
The specified AppClient is not found. Ensure you’ve entered the correct AppClient identifier.
HTTP Status Code: 404
```

## `Authorize` errors
<a name="dev-errors-Authorize"></a>

### ValidationException
<a name="authorize-validation-exception"></a>

You might receive the following exception if any of the API parameters don’t satisfy the constraints defined in the API specifications.

```
ValidationException
HTTP Status Code: 400
```

**Reason 1: When AppClient ID is not specified**

The `app_client_id` is missing in the request parameters. Create the AppClient if it hasn't yet been created or use your existing `app_client_id` and try again. To find the AppClient ID, use the [ListAppClient](manage-appclients.md#list_appclients) API operation.

**Reason 2: When AppFabric doesn’t have access to the customer managed key**

```
Message: AppFabric couldn't access the customer managed key configured for AppClient.
```

AppFabric is currently unable to access the customer managed keys, likely due to recent changes in its permissions. Verify the specified key exists and ensure AppFabric is granted the appropriate access permissions.

**Reason 3: The redirect URL specified is not valid**

```
Message: Redirect url invalid
```

Ensure the redirect URL in your request is correct. It must match one of the redirect URLs specified when you created or updated the AppClient. To view the list of allowed redirect URLs, use the [GetAppClient](manage-appclients.md#get_appclient_details) API operation.

## `Token` errors
<a name="dev-errors-Token"></a>

### TokenException
<a name="Token-token-exception"></a>

You might receive the following exception for a few reasons.

```
TokenException
HTTP Status Code: 400
```

**Reason 1: When an email that is not valid is specified**

```
Message: Invalid Email used
```

Ensure the email address you’re using matches the one listed for the `starterUserEmails` attribute when you created the AppClient. If the emails don’t match, change to the matching email address and try again. To view the email used, use the [GetAppClient](manage-appclients.md#get_appclient_details) API operation.

**Reason 2: For grant\_type as refresh\_token when the token is not specified.**

```
Message: refresh_token must be non-null for Refresh Token Grant-type
```

The refresh token specified in the request is null or empty. Specify an active `refresh_token` received in [Token](getting-started-appdeveloper-productivity.md#authorize_data_access) API call response.

### ThrottlingException
<a name="throttling-exception"></a>

You might receive the following exception if the API is being called at rate which is more than the allowed quota.

```
ThrottlingException
HTTP Status Code: 429
```

## `ListActionableInsights`, `ListMeetingInsights`, and `PutFeedback` errors
<a name="dev-errors-many-apis"></a>

### ValidationException
<a name="many-apis-validation-exception"></a>

You might receive the following exception if any of the API parameters don't satisfy the constraint defined on the API specifications.

```
ValidationException
HTTP Status Code: 400
```

### ThrottlingException
<a name="many-apis-throttling-exception"></a>

You might receive the following exception if the API is being called at rate which is more than the allowed quota.

```
ThrottlingException
HTTP Status Code: 429
```