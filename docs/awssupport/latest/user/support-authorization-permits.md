

# Managing support permits
<a name="support-authorization-permits"></a>

Support permits define the scope and conditions under which AWS Support can access information about your services. This topic describes how to create, view, list, and delete support permits.

## Creating a support permit
<a name="support-authorization-permits-create"></a>

Create a support permit to define the scope and conditions under which AWS Support can access information about your services.

------
#### [ Console ]

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. In the navigation pane, choose **Support authorization**.

1. In the **Granted access** section, choose **Preconfigure access**.

1. For **Access type**, choose one of the following:
   + **All supported resources in this Region** – Applies broad access to your entire account in the selected Region.
   + **Choose resource ARN** – Limits access to a specific resource that you identify by ARN.

1. (Optional) For **Details**, enter a **Name** and **Description** for the support permit.

1. For **Access duration**, choose one of the following:
   + **No expiration** – Access remains active until you revoke it.
   + **Custom duration** – Set a specific time window during which the support permit is valid.

1. For **Actions**, choose the actions that AWS Support is permitted to perform:
   + Select the **All actions** check box to permit all available actions on the covered resources. This removes the 10-action limit.
   + To choose specific actions, clear the **All actions** check box. Select a service from the **Services** list, and then select up to 10 individual actions from the actions table.

1. For **Signing key**, choose an AWS KMS key from the dropdown list. To create a new key, choose **Create KMS signing key**.

1. Choose **Submit**.

------
#### [ AWS CLI ]

Use `CreateSupportPermit` to create a new support permit. The following parameters are available:

**Required parameters**: `name`, a unique name for the support permit (1–256 alphanumeric characters).

**Optional parameters**: `description`, a human-readable description (maximum 1,024 characters).

**Create a support permit with specific actions and resources**

```
aws supportauthz create-support-permit \
    --name "AuroraDBPermit" \
    --description "Access to Aurora cluster diagnostic data" \
    --signing-key-info '{"kmsKey": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}' \
    --support-case-display-id "case-12345678" \
    --permit '{
        "actions": {"actions": ["rds:ReadClusterData", "rds:ViewQueryLogsWithParameters"]},
        "resources": {"resources": ["arn:aws:rds:us-east-1:111122223333:cluster:my-cluster"]},
        "conditions": [
            {"allowAfter": "2026-06-01T00:00:00Z"},
            {"allowBefore": "2026-06-15T00:00:00Z"}
        ]
    }'
```

------

## Scoping a support permit
<a name="support-authorization-permits-scope"></a>

You control the scope of a support permit by specifying actions, resources, and conditions.

### Actions
<a name="support-authorization-permits-scope-actions"></a>

You can permit actions in two ways:
+ `allActions`: Permits all support actions for the specified resources.
+ `actions`: A list of up to 10 specific action names. Use `ListActions` to view available actions.

### Resources
<a name="support-authorization-permits-scope-resources"></a>

You can specify resources in two ways:
+ `allResourcesInRegion`: Permits access to service information for all resources in the Region.
+ `resources`: A list of up to 10 specific resource ARNs for which AWS Support can access service information.

### Conditions
<a name="support-authorization-permits-scope-conditions"></a>

You can define up to 2 time-based conditions:
+ `allowAfter`: The support permit is not valid before this time (ISO 8601 format).
+ `allowBefore`: The support permit is not valid after this time (ISO 8601 format).

Use both conditions together to create a time window during which the support permit is valid.

## Viewing a support permit
<a name="support-authorization-permits-view"></a>

Retrieve the configuration and status of a support permit.

------
#### [ Console ]

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. In the navigation pane, choose **Support authorization**.

1. In the **Granted access** section, locate the support permit. The table displays the support case, service, Support Permit ARN, name, status, creation date, and duration for each support permit.

------
#### [ AWS CLI ]

Use `GetSupportPermit` to retrieve the configuration and status of a support permit. You can identify the support permit by name or ARN.

```
aws supportauthz get-support-permit \
    --support-permit-identifier "AuroraDBPermit"
```

------

## Listing support permits
<a name="support-authorization-permits-list"></a>

View all support permits in your account and Region.

------
#### [ Console ]

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. In the navigation pane, choose **Support authorization**.

1. In the **Granted access** section, view the list of support permits. Use the **Status** and **Service** dropdown filters to narrow the results, or search by resource in the search field.

------
#### [ AWS CLI ]

Use `ListSupportPermits` to list support permits in your account and Region. You can filter results by status.

```
aws supportauthz list-support-permits \
    --support-permit-statuses '["ACTIVE"]'
```

The response includes up to 100 results per page. Use the `nextToken` value in subsequent requests to retrieve additional pages.

------

## Revoking a support permit
<a name="support-authorization-permits-delete"></a>

Revoke a support permit to terminate active access for the selected resources. This action can't be undone. New authorizations stop being issued for the revoked support permit.

------
#### [ Console ]

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. In the navigation pane, choose **Support authorization**.

1. In the **Granted access** section, select the support permit that you want to revoke.

1. Choose **Revoke access**.

**Important**  
Revoking access terminates active access for the selected resources. This action can't be undone.

------
#### [ AWS CLI ]

Use `DeleteSupportPermit` to delete a support permit.

```
aws supportauthz delete-support-permit \
    --arn "arn:aws:supportauthz:us-east-1:111122223333:supportpermit/AuroraDBPermit"
```

------

To prevent new signing operations, you can revoke the grant on the associated AWS KMS key. For more information, see [Revoking AWS Support authorization access](support-authorization-kms.md#support-authorization-kms-revoke). Alternatively, you can disable or schedule deletion of the key, but both AWS KMS and AWS Support authorization are eventually consistent. After you disable a key, it can take up to several minutes for the change to take effect. During this period, signed authorizations might continue to be issued by using the key.

## Best practices
<a name="support-authorization-permits-best-practices"></a>

Follow these recommendations when you create support permits:
+ **Use time-based conditions**: Set `allowAfter` and `allowBefore` conditions to limit support permit validity to specific time windows.
+ **Apply least-privilege scoping**: Specify only the actions and resources that AWS Support needs for the investigation. Avoid using `allActions` and `allResourcesInRegion` together unless necessary.
+ **Link support permits to support cases**: Use the `supportCaseDisplayId` parameter to automatically deactivate the support permit when the support case closes.
+ **Audit regularly**: Use `ListSupportPermits` to review active support permits and delete support permits that are no longer needed.