Defect Detection App is in preview release and is subject to change.

# Creating a Defect Detection App tenant

You create a tenant for each of your customers. For beta, we support a single user per tenant
through the Defect Detection App API;. If you want to add additional users to a tenant, contact AWS.

When a tenant is created, an email with login instructions to the Defect Detection App web app is sent to the tenant email address (`root-user-email`).

###### To create a tenant

- At the command prompt, the enter the following command to create a tenant. Change
  the following values:
  - `--root-user-email` — The email address for the
    tenant.
  - (Optional) `--description` — A description for the tenant. For billing purposes,
    This field is useful for identifying tenants.
  - `--region` — The AWS Region for the Defect Detection App API.
    For beta, use `us-east-1`.
  - `--endpoint-url` — The endpoint for the Defect Detection App Tenant
    API. For beta, use `https://6do9jn9pi9.execute-api.us-east-1.amazonaws.com/live`.

```
aws dda create-tenant \
    --root-user-email `VALID_EMAIL_ADDRESS` \
    --description '`TENANT_DESCRIPTION`' \
    --region `REGION` \
    --endpoint-url `TENANT_MANAGEMENT_ENDPOINT_URL`

```

If successful, the response code is `200`.

The response from `create-tenant` is a `TenantDescription` object with the following fields:

- `RootUserEmail` — The root email address for the tenant.
- `Status` — The status for tenant. Possible values are:
  - `CREATING` — We are creating the tenant. Creating a
    tenant might take a while. To check if the tenant is ready, call [get-tenant](dda-get-tenant.md "dda-get-tenant.md") with the Tenant ID. The
    tenant is ready if the value of `Status` is
    `Ready`.
  - `CREATED` — The tenant is created and ready for use.
  - `DELETING` — We are deleting the tenant.

- `TenantId` — The ID for the tenant
  the following JSON is an example response.

```
{
    "Tenant": {
        "TenantId": "1111111111",
        "Status": "CREATING",
        "RootUserEmail": "user@anycompany.com"
    }
}
```
