# Maintaining Amazon DocumentDB elastic clusters

###### Topics

- [Viewing pending elastic cluster maintenance actions](#view-elastic-cluster-maintenance "#view-elastic-cluster-maintenance")
- [Elastic cluster engine updates](#elastic-cluster-engine-updates "#elastic-cluster-engine-updates")
- [Elastic cluster operating system updates](#elastic-cluster-os-updates "#elastic-cluster-os-updates")
  Periodically, Amazon DocumentDB performs maintenance on Amazon DocumentDB elastic cluster resources.
  Maintenance most often involves updates to the database engine (elastic cluster maintenance) or the elastic cluster's underlying operating system (OS updates).
  Database engine updates are required patches and include security fixes, bug fixes, and enhancements to the database engine.
  While most operating system patches are optional, if you don't apply them for a while, the patch may be required and auto applied to maintain your security posture.
  So, we recommend that you apply operating system updates to your Amazon DocumentDB elastic clusters as soon as they are available.

Database engine patches require that you take your Amazon DocumentDB elastic clusters offline for a short time.
Once available, these patches are automatically scheduled to apply during an upcoming scheduled maintenance window of your Amazon DocumentDB elastic cluster.

Elastic clusters have their own respective maintenance windows.
Elastic cluster modifications that you have chosen not to apply immediately, are applied during the maintenance window.
By default, when you create an elastic cluster, Amazon DocumentDB assigns a maintenance window for your elastic cluster.
You can choose the maintenance window when creating an elastic cluster.
You can also modify the maintenance windows at any time to fit your business schedules or practices.
It is generally advised to choose maintenance windows that minimize the impact of the maintenance on your application (for example, on evenings or weekends).

## Viewing pending elastic cluster maintenance actions

You can view whether a maintenance update is available for your elastic cluster by using the AWS CLI.

If an update is available, you can do one of the following:

- Defer a maintenance action that is currently scheduled for next maintenance window (for OS patches only).
- Apply the maintenance actions immediately.
- Schedule the maintenance actions to start during your next maintenance window.
- Schedule the maintenance actions to start during your selected apply-on window.

The maintenance window determines when pending operations start, but it does not limit the total execution time of these operations.

Use the following AWS CLI operation to determine what maintenance actions are pending.
List all pending maintenance actions:

```
aws docdb-elastic list-pending-maintenance-actions
```

Output from this operation looks something like the following (JSON format):

```
{
'ResourcePendingMaintenanceActions': [
    {
        'ResourceArn': 'string-arn',
        'PendingMaintenanceActionDetails': [
            {
                'Action': 'ENGINE_UPDATE',
                'AutoAppliedAfterDate': 'string',
                'ForcedApplyDate': 'string',
                'OptInStatus': 'string',
                'CurrentApplyDate': 'string',
                'Description': 'string'
            },
        ]
    },
],
'NextToken': 'string'
}
```

Get pending maintenance action (if any) on a given `resourceArn`:

```
aws docdb-elastic get-pending-maintenance-action --resource-arn `string-arn`
```

Output from this operation looks something like the following (JSON format).

```
{
    'ResourcePendingMaintenanceAction': {
        'ResourceArn': 'string-arn',
        'PendingMaintenanceActionDetails': [
            {
                'Action': 'ENGINE_UPDATE',
                'AutoAppliedAfterDate': 'string',
                'ForcedApplyDate': 'string',
                'OptInStatus': 'string',
                'CurrentApplyDate': 'string',
                'Description': 'string'
            }
        ]
    }
}
```

Parameters:

- `ResourceArn`—The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.
- `Action`—The pending maintenance action being applied to the resource.

Valid values:

    + `ENGINE_UPDATE`
    + `ENGINE_UPGRADE`
    + `SECURITY_UPDATE`
    + `OS_UPDATE`
    + `MASTER_USER_PASSWORD_UPDATE`

- `AutoAppliedAfterDate`—First maintenance window after this date. `NEXT_MAINTENANCE OPT_IN` is ignored in this case.
- `ForcedApplyDate`—Applied regardless of maintenance window. `IMMEDIATE OPT_IN` is ignored in this case.
- `OptInStatus`—A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type `IMMEDIATE` can't be undone.

Valid values:

    + `IMMEDIATE`—Apply the maintenance action immediately.
    + `NEXT_MAINTENANCE`—Apply the maintenance action during the next maintenance window for the resource.
    + `APPLY_ON`—Apply the maintenance action on specified apply date regardless of next maintenance window for the resource.
    + `UNDO_OPT_IN`—Cancel any existing `NEXT_MAINTENANCE` or `APPLY_ON` opt in requests.

- `CurrentApplyDate`—Displayed if opt-in-type is `APPLY_ON`.
- `Description`—An option description for the maintenance action.

## Elastic cluster engine updates

With Amazon DocumentDB, you can choose when to apply maintenance operations. You can decide when Amazon DocumentDB applies updates using the AWS CLI.

Apply pending maintenance actions:

```
aws docdb-elastic apply-pending-maintenance-action
--resource-arn `string-arn`
--apply-action `string-enum`
--opt-in-type `string-enum`
[--apply-on `string-date-range`]
```

Parameters:

- `--resource-arn`—The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.
- `--apply-action`—The pending maintenance action to apply to this resource.

Valid values:

    + `ENGINE_UPDATE`
    + `ENGINE_UPGRADE`
    + `SECURITY_UPDATE`
    + `OS_UPDATE`
    + `MASTER_USER_PASSWORD_UPDATE`

- `--opt-in-type`—A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type `IMMEDIATE` can't be undone.

Valid values:

    + `IMMEDIATE`—Apply the maintenance action immediately.
    + `NEXT_MAINTENANCE`—Apply the maintenance action during the next maintenance window for the resource.
    + `APPLY_ON`—Apply the maintenance action on specified apply date regardless of next maintenance window for the resource.
    + `UNDO_OPT_IN`—Cancel any existing `NEXT_MAINTENANCE` or `APPLY_ON` opt in requests.

- `[--apply-on]`—Required if opt-in-type is `APPLY_ON`. Format: `yyyy/MM/dd HH:mm-yyyy/MM/dd HH:mm`
  (This option uses UTC time. The start time can be any time in the future from a minimum of 30 minutes and a maximum of 14 days, or force/apply date on pending action, whichever is earlier.
  Start to end time window can be a minimum of 30 minutes to a maximum of 8 hours long.)

Output from this operation looks something like the following (JSON format):

```
{
 'ResourcePendingMaintenanceAction': {
        'ResourceArn': 'string-arn',
        'PendingMaintenanceActionDetails': [
            {
                'Action': 'SECURITY_UPDATE',
                'AutoAppliedAfterDate': 'string',
                'ForcedApplyDate': 'string',
                'OptInStatus': 'IMMEDIATE',
                'CurrentApplyDate': 'string',
                'Description': 'string'
            },
        ]
 }
}
```

Parameters:

- `ResourceArn`—The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.
- `Action`—The pending maintenance action being applied to the resource.

Valid values:

    + `ENGINE_UPDATE`
    + `ENGINE_UPGRADE`
    + `SECURITY_UPDATE`
    + `OS_UPDATE`
    + `MASTER_USER_PASSWORD_UPDATE`

- `AutoAppliedAfterDate`—First maintenance window after this date. `NEXT_MAINTENANCE OPT_IN` is ignored in this case.
- `ForcedApplyDate`—Applied regardless of maintenance window. `IMMEDIATE OPT_IN` is ignored in this case.
- `OptInStatus`—A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type `IMMEDIATE` can't be undone.

Valid values:

    + `IMMEDIATE`—Apply the maintenance action immediately.
    + `NEXT_MAINTENANCE`—Apply the maintenance action during the next maintenance window for the resource.
    + `APPLY_ON`—Apply the maintenance action on specified apply date regardless of next maintenance window for the resource.
    + `UNDO_OPT_IN`—Cancel any existing `NEXT_MAINTENANCE` or `APPLY_ON` opt in requests.

- `CurrentApplyDate`—Displayed if opt-in-type is `APPLY_ON`.
- `Description`—An option description for the maintenance action.

### Apply dates

Each maintenance action has a respective apply date that you can find when describing the pending maintenance actions.
When you read the output of pending maintenance actions from the AWS CLI, three dates are listed:

- `CurrentApplyDate`—The date the maintenance action will get applied either immediately or during the next maintenance window.
  If the maintenance is optional, this value can be null.
- `ForcedApplyDate`—The date when the maintenance will be automatically applied, independent of your maintenance window.
- `AutoAppliedAfterDate`—The date after which the maintenance will be applied during the cluster's maintenance window.

### User-created maintenance actions

As an Amazon DocumentDBelastic cluster user, you can initiate updates to your clusters configurations.

**Updating cluster primary password**

```
aws docdb-elastic update-cluster
--cluster-arn `string-arn`
[--admin-user-password `string`]
[--auth-type `string-enum`]
[--apply-method `string-enum`]
[--apply-on `string-date-range`]
#... other parameters of the API that follow here are not relevant for this configuration
```

Parameters:

- `--cluster-arn`—The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the maintenance action will be applied.
- `[--admin-user-password]`—The password associated with the admin user.
- `[--auth-type]`—The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are `PLAIN_TEXT` or `SECRET_ARN`.
- `[--apply-method]`—A value that specifies the type of method being applied. Allowed values are `IMMEDIATE` and `APPLY_ON`. Default is `IMMEDIATE`.
- `[--apply-on]`—Required if `apply-method` is `APPLY_ON`. Format: `yyyy/MM/dd HH:mm-yyyy/MM/dd HH:mm`
  (This option uses UTC time. The start time can be any time in the future from a minimum of 30 minutes and a maximum of 14 days.
  Start to end time window can be a minimum of 30 minutes to a maximum of 8 hours long.)

Output from this operation looks something like the following (JSON format):

```
{
 'ResourcePendingMaintenanceAction': {
        'ResourceArn': 'string-arn',
        'PendingMaintenanceActionDetails': [
            {
                'Action': 'MASTER_USER_PASSWORD_UPDATE',
                'OptInStatus': 'APPLY_ON',
                'CurrentApplyDate': 'string',
                'Description': 'string'
            },
        ]
 }
}
```

### Changing your Amazon DocumentDB maintenance windows

The maintenance window should fall at the time of lowest usage and thus might need changing from time to time.
Your elastic cluster is unavailable during this time only if system changes (such as a scale storage operation change) are being applied and require an outage.
It is unavailable only for the minimum amount of time required to make the necessary changes.

The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.

To change the maintenance window, see [Modifying elastic cluster configurations](elastic-managing.md#elastic-modify "elastic-managing.md#elastic-modify").

## Elastic cluster operating system updates

Amazon DocumentDB elastic clusters occasionally require operating system updates.
Amazon DocumentDB upgrades the operating system to a newer version to improve database performance and customers’ overall security posture.
Operating system updates don't change the cluster engine version of an Amazon DocumentDB elastic cluster.

Most operating system updates for Amazon DocumentDB elastic clusters are optional and don't have a set date to apply them.
However, if you don't apply these updates for a while, they may eventually become required and automatically applied during your clusters maintenance window.
This is to help maintain the security posture of your database.
To avoid any unexpected downtime, we recommend that you apply operating system updates to your Amazon DocumentDB elastic cluster as soon as they become available and set your cluster maintenance window at a time of your convenience as per your business needs.
