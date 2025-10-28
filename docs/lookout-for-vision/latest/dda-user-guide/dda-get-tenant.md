Defect Detection App is in preview release and is subject to change.

# Getting Defect Detection App tenant information

To information about a tenant, call the `get-tenant` operation and pass the tenant ID.
You can get a list of tenants (and tenant IDs) by calling the [list-tenants](dda-list-tenants.md "dda-list-tenants.md") operation.

###### To get tenant information

- At the command prompt, enter the following command. Change the following values:
  - `--tenant-id` — The ID for the tenant that you want.
  - `--region` — The AWS Region for the Defect Detection App API.
    For beta, use `us-east-1`.
  - `--endpoint-url` — The endpoint for the Defect Detection App Tenant
    API. For beta, use `https://6do9jn9pi9.execute-api.us-east-1.amazonaws.com/live`.

```
aws dda get-tenant \
    --tenant-id `TENANT_ID \`
    --region `REGION` \
    --endpoint-url `TENANT_MANAGEMENT_ENDPOINT_URL`
```

If successful, the response code is `200`. If the tenant doesn't exist, the response code
is `404` (The resource could not be found).

The response from `get-tenant` is a `Tenant` object with the following fields:

- `RootUserEmail` — The root email address for the tenant.
- `Status` — The status for tenant. Possible values are:
  - `CREATING` — We are creating the tenant. Creating a
    tenant might take a while. To check if the tenant is ready, call get-tenant with the Tenant ID. The
    tenant is ready if the value of `Status` is
    `Ready`.
  - `CREATED` — The tenant is created and ready for use.
  - `DELETING` — We are deleting the tenant.

- `TenantId` — The ID for the tenant
  The following JSON is an example response from `get-tenant`.

```
{
    "Tenant": {
        "TenantId": "1111111111",
        "Status": "CREATED",
        "RootUserEmail": "user@anycompany.com"
    }
}
```
