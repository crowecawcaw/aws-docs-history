Defect Detection App is in preview release and is subject to change.

# Updating a Defect Detection App tenant

You can update the description for a tenant.

To update a tenant, you call the `update-tenant` operation.

###### To update a tenant

- At the command prompt, the enter the following command to update a tenant. Change
  the following values:
  - `--tenant-id` — The ID for the tenant that you want to update.
  - `--description` — The updated description for the tenant.
  - `--region` — The AWS Region for the Defect Detection App API.
    For beta, use `us-east-1`.
  - `--endpoint-url` — The endpoint for the Defect Detection App Tenant
    API. For beta, use `https://6do9jn9pi9.execute-api.us-east-1.amazonaws.com/live`.

```
aws dda update-tenant \
    --tenant-id  `TENANT_ID` \
    --description '`Updated description`' \
    --region `REGION` \
    --endpoint-url `TENANT_MANAGEMENT_ENDPOINT_URL`

```

If successful, the response code is `200`.

The response from `update-tenant` is a `TenantDescription` object with the following fields:

- `Description` — The description for the tenant.
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
