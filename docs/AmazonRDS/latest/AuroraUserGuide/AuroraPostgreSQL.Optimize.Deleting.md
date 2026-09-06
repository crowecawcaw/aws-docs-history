

# Deleting Aurora PostgreSQL query plans
<a name="AuroraPostgreSQL.Optimize.Deleting"></a>

Delete execution plans that you aren't using or plans that aren't valid. For more information about deleting plans, see the following sections.

**Topics**
+ [Deleting plans](#AuroraPostgreSQL.Optimize.Maintenance.DeletingPlans)
+ [Validating plans](#AuroraPostgreSQL.Optimize.Maintenance.ValidatingPlans)

## Deleting plans
<a name="AuroraPostgreSQL.Optimize.Maintenance.DeletingPlans"></a>

Plans are automatically deleted if they haven't been used in over a month, specifically, 32 days. That's the default setting for the `apg_plan_mgmt.plan_retention_period` parameter. You can change the plan retention period to a longer period of time, or to a shorter period of time starting from the value of 1. Determining the number of days since a plan was last used is calculated by subtracting the `last_used` date from the current date. The `last_used` date is the most recent date that the optimizer chose the plan as the minimum cost plan or that the plan was run. The date is stored for the plan in the `apg_plan_mgmt.dba_plans` view. 

We recommend that you delete plans that haven't been used for a long time or that aren't useful. Every plan has a `last_used` date that the optimizer updates each time it executes a plan or chooses the plan as the minimum-cost plan for a statement. Check the last `last_used` dates to identify the plans that you can safely delete.

The following query returns a three column table with the count on the total number of plans, plans failed to delete, and the plans successfully deleted. It has a nested query that is an example of how to use the `apg_plan_mgmt.delete_plan` function to delete all plans that haven't been chosen as the minimum-cost plan in the last 31 days and its status is not `Rejected`.

```
SELECT (SELECT COUNT(*) from apg_plan_mgmt.dba_plans) total_plans,
       COUNT(*) FILTER (WHERE result = -1) failed_to_delete,
       COUNT(*) FILTER (WHERE result = 0) successfully_deleted
       FROM (
            SELECT apg_plan_mgmt.delete_plan(sql_hash, plan_hash) as result
            FROM apg_plan_mgmt.dba_plans
            WHERE last_used < (current_date - interval '31 days')
            AND status <> 'Rejected'
            ) as dba_plans ;
```

```
 total_plans | failed_to_delete | successfully_deleted
-------------+------------------+----------------------
           3 |                0 |                    2
```

For more information, see [apg\_plan\_mgmt.delete\_plan](AuroraPostgreSQL.Optimize.Functions.md#AuroraPostgreSQL.Optimize.Functions.delete_plan).

To delete plans that aren't valid and that you expect to remain invalid, use the `apg_plan_mgmt.validate_plans` function. This function lets you delete or disable invalid plans. For more information, see [Validating plans](#AuroraPostgreSQL.Optimize.Maintenance.ValidatingPlans). 

**Important**  
If you don't delete extraneous plans, you might eventually run out of shared memory that's set aside for query plan management. To control how much memory is available for managed plans, use the `apg_plan_mgmt.max_plans` parameter. Set this parameter in your custom DB parameter group and reboot your DB instance for changes to take effect. For more information, see the [apg\_plan\_mgmt.max\_plans](AuroraPostgreSQL.Optimize.Parameters.md#AuroraPostgreSQL.Optimize.Parameters.max_plans) parameter. 

## Validating plans
<a name="AuroraPostgreSQL.Optimize.Maintenance.ValidatingPlans"></a>

Use the `apg_plan_mgmt.validate_plans` function to delete or disable plans that are invalid.

Plans can become invalid or stale when objects that they depend on are removed, such as an index or a table. However, a plan might be invalid only temporarily if the removed object gets recreated. If an invalid plan can become valid later, you might prefer to disable an invalid plan or do nothing rather than delete it. 

To find and delete all plans that are invalid and haven't been used in the past week, use the `apg_plan_mgmt.validate_plans `function as follows.

```
SELECT apg_plan_mgmt.validate_plans(sql_hash, plan_hash, 'delete') 
FROM apg_plan_mgmt.dba_plans
WHERE last_used < (current_date - interval '7 days');
```

To enable or disabled a plan directly, use the `apg_plan_mgmt.set_plan_enabled` function.