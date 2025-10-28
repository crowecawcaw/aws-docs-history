Defect Detection App is in preview release and is subject to change.

# Deleting a Defect Detection App tenant

To delete a tenant, use the `delete-tenant` command. When you delete a tenant,
the status for the tenant is immediatly set to `DELETING` and billing for the tenant stops.

To get the status call the [delete-tenant](dda-get-tenant.md "dda-get-tenant.md")
operation and check the `Status` field. The tenant is deleted if you get a
`404` (The resource could not be found) error code.

For beta, resource clean up might take a few days. During that time the status for the
tenant remains as `DELETING`. We don't recommend checking deletion status by
continually polling the `get-tenant` operation.

###### To delete a tenant

- At the command prompt, enter the following command. Change the following values:
  - `--tenant-id` — The ID for the tenant that you want to delete.
  - `--region` — The AWS Region for the Defect Detection App API.
    For beta, use `us-east-1`.
  - `--endpoint-url` — The endpoint for the Defect Detection App Tenant
    API. For beta, use `https://6do9jn9pi9.execute-api.us-east-1.amazonaws.com/live`.

```
aws dda delete-tenant \
    --tenant-id `TENANT_ID`
    --region `REGION` \
    --endpoint-url `TENANT_MANAGEMENT_ENDPOINT_URL`
```

If successful, the response code is `200`. The tenant is then in the
`DELETING` state. If the tenant doesn't exist, the response code is
`404` (The resource could not be found).
