

# Discovering support actions
<a name="support-authorization-actions"></a>

Support actions are service-specific operations that AWS Support can perform on your resources. Each action has a descriptive name and description that explains what the operation does. Actions use a namespaced format that identifies the AWS service and the specific operation. Use the `ListActions` API to view the actions available for a service before you create a scoped support permit.

## Listing actions for a service
<a name="support-authorization-actions-list"></a>

Use `ListActions` to view the actions available for a specific service. The `service` parameter is required.

```
aws supportauthz list-actions \
    --service "rds"
```

**Example output**

```
{
    "actionSummaries": [
        {
            "action": "rds:ReadClusterData",
            "service": "rds",
            "description": "Read diagnostic data from the database cluster."
        },
        {
            "action": "rds:ViewQueryLogsWithParameters",
            "service": "rds",
            "description": "View query logs including query parameters."
        }
    ]
}
```

The response includes up to 100 results per page. Use the `nextToken` value in subsequent requests to retrieve additional pages.

## Getting action details
<a name="support-authorization-actions-get"></a>

Use `GetAction` to retrieve details about a specific action.

```
aws supportauthz get-action \
    --action "rds:ReadClusterData"
```

**Example output**

```
{
    "action": "rds:ReadClusterData",
    "service": "rds",
    "description": "Read diagnostic data from the database cluster."
}
```

## Using actions in support permits
<a name="support-authorization-actions-in-permits"></a>

After you identify the available actions, use specific action names in your support permit to apply least-privilege scoping. Specify individual actions in the `actions` list rather than using `allActions` when you want to limit what AWS Support can do on your resources.

**Create a support permit with specific actions**

```
aws supportauthz create-support-permit \
    --name "ScopedPermit" \
    --signing-key-info '{"kmsKey": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}' \
    --permit '{
        "actions": {"actions": ["rds:ReadClusterData"]},
        "resources": {"resources": ["arn:aws:rds:us-east-1:111122223333:cluster:my-cluster"]},
        "conditions": [
            {"allowBefore": "2026-06-15T00:00:00Z"}
        ]
    }'
```