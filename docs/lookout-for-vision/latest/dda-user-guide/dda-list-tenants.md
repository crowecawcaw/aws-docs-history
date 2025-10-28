Defect Detection App is in preview release and is subject to change.

# Listing your Defect Detection App tenants

You can use the `list-tenants` command to list the tenants that
you have created. The response is an array which incudes the tenant ID and status for each
tenant. To get information about a tenant, call the `get-tenant` operation
and pass the tenant ID. For more information, see [Getting Defect Detection App tenant information](dda-get-tenant.md "dda-get-tenant.md").

###### To list tenants

- At the command prompt enter the following command. Change the following values:
  - `--region` — The AWS Region for the Defect Detection App API.
    For beta, use `us-east-1`.
  - `--endpoint-url` — The endpoint for the Defect Detection App Tenant
    API. For beta, use `https://6do9jn9pi9.execute-api.us-east-1.amazonaws.com/live`.

```
aws dda list-tenants \
    --region `REGION` \
    --endpoint-url `TENANT_MANAGEMENT_ENDPOINT_URL`
```

The response from `list-tenants` is a list of tenants (`Tenants`) in your AWS account.
For each tenant you get an `TenantMetadata` object with the following fields:

- `TenantId` — The ID for the tenant.
- `Status` — The status for tenant. Possible values are:

      + `CREATING` — We are creating the tenant.
      + `CREATED` — The tenant is created and ready for use.
      + `DELETING` — We are deleting the tenant.

  The following is an example response from `list-tenants`.

```
{
    "Tenants": [
        {
            "TenantId": "1111111111",
            "Status": "CREATING"
        }
    ]
}
```
