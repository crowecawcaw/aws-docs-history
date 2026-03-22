# Function reference for Aurora PostgreSQL query plan management

The `apg_plan_mgmt` extension provides the following functions.

###### Functions

- [apg_plan_mgmt.copy_outline](#AuroraPostgreSQL.Optimize.Functions.copy_outline "#AuroraPostgreSQL.Optimize.Functions.copy_outline")
- [apg_plan_mgmt.delete_plan](#AuroraPostgreSQL.Optimize.Functions.delete_plan "#AuroraPostgreSQL.Optimize.Functions.delete_plan")
- [apg_plan_mgmt.evolve_plan_baselines](#AuroraPostgreSQL.Optimize.Functions.evolve_plan_baselines "#AuroraPostgreSQL.Optimize.Functions.evolve_plan_baselines")
- [apg_plan_mgmt.get_explain_plan](#AuroraPostgreSQL.Optimize.Functions.get_explain_plan "#AuroraPostgreSQL.Optimize.Functions.get_explain_plan")
- [apg_plan_mgmt.plan_last_used](#AuroraPostgreSQL.Optimize.Functions.plan_last_used "#AuroraPostgreSQL.Optimize.Functions.plan_last_used")
- [apg_plan_mgmt.reload](#AuroraPostgreSQL.Optimize.Functions.reload "#AuroraPostgreSQL.Optimize.Functions.reload")
- [apg_plan_mgmt.set_plan_enabled](#AuroraPostgreSQL.Optimize.Functions.set_plan_enabled "#AuroraPostgreSQL.Optimize.Functions.set_plan_enabled")
- [apg_plan_mgmt.set_plan_status](#AuroraPostgreSQL.Optimize.Functions.set_plan_status "#AuroraPostgreSQL.Optimize.Functions.set_plan_status")
- [apg_plan_mgmt.update_plans_last_used](#AuroraPostgreSQL.Optimize.Functions.update_plans_last_used "#AuroraPostgreSQL.Optimize.Functions.update_plans_last_used")
- [apg_plan_mgmt.validate_plans](#AuroraPostgreSQL.Optimize.Functions.validate_plans "#AuroraPostgreSQL.Optimize.Functions.validate_plans")

## apg_plan_mgmt.copy_outline

Copy a given SQL plan hash and plan outline to a target SQL plan hash and outline,
thereby overwriting the target's plan hash and outline. This function is
available in `apg_plan_mgmt` 2.3 and higher releases.

**Syntax**

```
apg_plan_mgmt.copy_outline(
    source_sql_hash,
    source_plan_hash,
    target_sql_hash,
    target_plan_hash,
    force_update_target_plan_hash
)
```

###### Return value

Returns 0 when the copy is successful. Raises exceptions for invalid
inputs.

**Parameters**

| Parameter                       | Description                                                                                                                                                                                                                                                             |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source_sql_hash`               | The `sql_hash` ID associated with the<br>`plan_hash` to copy to the target query.                                                                                                                                                                                       |
| `source_plan_hash`              | The `plan_hash` ID to copy to the target<br>query.                                                                                                                                                                                                                      |
| `target_sql_hash`               | The `sql_hash` ID of the query to update with the<br>source plan hash and outline.                                                                                                                                                                                      |
| `target_plan_hash`              | The `plan_hash` ID of the query to update with the<br>source plan hash and outline.                                                                                                                                                                                     |
| `force_update_target_plan_hash` | (Optional) The `target_plan_hash` ID of the query is<br>updated even if the source plan isn't reproducible for the<br>`target_sql_hash`. When set to true, the function can<br>be used to copy plans across schemas where relation names and<br>columns are consistent. |

**Usage notes**

This function allows you to copy a plan hash and plan outline that uses hints to
other, similar statements, and thus saves you from needing to use in-line hint
statements at every occurrence in the target statements. If the updated target query
results in an invalid plan, this function raises an error and rolls back the
attempted update.

## apg_plan_mgmt.delete_plan

Delete a managed plan.

**Syntax**

```
apg_plan_mgmt.delete_plan(
    sql_hash,
    plan_hash
)
```

###### Return value

Returns 0 if the delete was successful or -1 if the delete failed.

**Parameters**

| Parameter   | Description                                               |
| ----------- | --------------------------------------------------------- |
| `sql_hash`  | The `sql_hash` ID of the plan's managed SQL<br>statement. |
| `plan_hash` | The managed plan's `plan_hash` ID.                        |

## apg_plan_mgmt.evolve_plan_baselines

Verifies whether an already approved plan is faster or whether a plan identified
by the query optimizer as a minimum cost plan is faster.

**Syntax**

```
apg_plan_mgmt.evolve_plan_baselines(
    sql_hash,
    plan_hash,
    min_speedup_factor,
    action
)
```

**Return value**

The number of plans that were not faster than the best approved plan.

**Parameters**

| Parameter            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sql_hash`           | The `sql_hash` ID of the plan's managed SQL<br>statement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `plan_hash`          | The managed plan's `plan_hash` ID. Use NULL to<br>mean all plans that have the same `sql_hash` ID<br>value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `min_speedup_factor` | The _minimum speedup factor_<br>can be the number of times faster that a plan must be than the<br>best of the already approved plans to approve it. Alternatively,<br>this factor can be the number of times slower that a plan must<br>be to reject or disable it.<br>This is a positive float value.                                                                                                                                                                                                                                                                                                                |
| `action`             | The action the function is to perform. Valid values include<br>the following. Case does not matter.<br>• `'disable'` – Disable each matching<br>plan that does not meet the minimum speedup<br>factor.<br>• `'approve'` – Enable each matching<br>plan that meets the minimum speedup factor and set its<br>status to `approved`.<br>• `'reject'` – For each matching plan<br>that does not meet the minimum speedup factor, set its<br>status to `rejected`.<br>• NULL – The function simply returns the number<br>of plans that have no performance benefit because they<br>do not meet the minimum speedup factor. |

**Usage notes**

Set specified plans to approved, rejected, or disabled based on whether the
planning plus execution time is faster than the best approved plan by a factor that
you can set. The action parameter might be set to `'approve'` or
`'reject'` to automatically approve or reject a plan that meets the
performance criteria. Alternatively, it might be set to '' (empty string) to do the
performance experiment and produce a report, but take no action.

You can avoid pointlessly rerunning of the
`apg_plan_mgmt.evolve_plan_baselines` function for a plan on which it
was recently run. To do so, restrict the plans to just the recently created
unapproved plans. Alternatively, you can avoid running the
`apg_plan_mgmt.evolve_plan_baselines` function on any approved plan
that has a recent `last_verified` timestamp.

Conduct a performance experiment to compare the planning plus execution time of
each plan relative to the other plans in the baseline. In some cases, there is only
one plan for a statement and the plan is approved. In such a case, compare the
planning plus execution time of the plan to the planning plus execution time of
using no plan.

The incremental benefit (or disadvantage) of each plan is recorded in the
`apg_plan_mgmt.dba_plans` view in the
`total_time_benefit_ms` column. When this value is positive, there is
a measurable performance advantage to including this plan in the baseline.

In addition to collecting the planning and execution time of each candidate plan,
the `last_verified` column of the `apg_plan_mgmt.dba_plans`
view is updated with the `current_timestamp`. The
`last_verified` timestamp might be used to avoid running this
function again on a plan that recently had its performance verified.

## apg_plan_mgmt.get_explain_plan

Generates the text of an `EXPLAIN` statement for the specified SQL
statement.

**Syntax**

```
apg_plan_mgmt.get_explain_plan(
    sql_hash,
    plan_hash,
    [explainOptionList]
)
```

###### Return value

Returns runtime statistics for the specified SQL statements. Use without
`explainOptionList` to return a simple `EXPLAIN`
plan.

**Parameters**

| Parameter           | Description                                                                                                                                                                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sql_hash`          | The `sql_hash` ID of the plan's managed SQL<br>statement.                                                                                                                                                                                                                                     |
| `plan_hash`         | The managed plan's `plan_hash` ID.                                                                                                                                                                                                                                                            |
| `explainOptionList` | A comma-separated list of explain options. Valid values<br>include `'analyze'`, `'verbose'`,<br>`'buffers'`, `'hashes'`, and<br>`'format json'`. If the<br>`explainOptionList` is NULL or an empty string<br>(''), this function generates an `EXPLAIN` statement,<br>without any statistics. |

**Usage notes**

For the `explainOptionList`, you can use any of the same options that
you would use with an `EXPLAIN` statement. The Aurora PostgreSQL optimizer
concatenates the list of options that you provide to the `EXPLAIN`
statement.

## apg_plan_mgmt.plan_last_used

Returns the `last_used` date of the specified plan from shared memory.

###### Note

The value in shared memory is always current on the primary DB instance in the
DB cluster. The value is only periodically flushed to the `last_used`
column of the `apg_plan_mgmt.dba_plans` view.

**Syntax**

```
apg_plan_mgmt.plan_last_used(
    sql_hash,
    plan_hash
)
```

###### Return value

Returns the `last_used` date.

**Parameters**

| Parameter   | Description                                               |
| ----------- | --------------------------------------------------------- |
| `sql_hash`  | The `sql_hash` ID of the plan's managed SQL<br>statement. |
| `plan_hash` | The managed plan's `plan_hash` ID.                        |

## apg_plan_mgmt.reload

Reload plans into shared memory from the `apg_plan_mgmt.dba_plans`
view.

**Syntax**

```
apg_plan_mgmt.reload()
```

**Return value**

None.

**Parameters**

None.

**Usage notes**

Call `reload` for the following situations:

- Use it to refresh the shared memory of a read-only replica immediately,
  rather than wait for new plans to propagate to the replica.
- Use it after importing managed plans.

## apg_plan_mgmt.set_plan_enabled

Enable or disable a managed plan.

**Syntax**

```
apg_plan_mgmt.set_plan_enabled(
    sql_hash,
    plan_hash,
    [true | false]
)
```

**Return value**

Returns 0 if the setting was successful or -1 if the setting failed.

**Parameters**

| Parameter   | Description                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| `sql_hash`  | The `sql_hash` ID of the plan's managed SQL<br>statement.                                                              |
| `plan_hash` | The managed plan's `plan_hash` ID.                                                                                     |
| `enabled`   | Boolean value of true or false:<br>• A value of `true` enables the plan.<br>• A value of `false` disables the<br>plan. |

## apg_plan_mgmt.set_plan_status

Set a managed plan's status to `Approved`,
`Unapproved`, `Rejected`, or `Preferred`.

**Syntax**

```
apg_plan_mgmt.set_plan_status(
    sql_hash,
    plan_hash,
    status
)
```

**Return value**

Returns 0 if the setting was successful or -1 if the setting failed.

**Parameters**

| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sql_hash`  | The `sql_hash` ID of the plan's managed SQL<br>statement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `plan_hash` | The managed plan's `plan_hash` ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `status`    | A string with one of the following values:<br>• `'Approved'`<br>• `'Unapproved'`<br>• `'Rejected'`<br>• `'Preferred'`<br>The case you use does not matter, however the status value is<br>set to initial uppercase in the<br>`apg_plan_mgmt.dba_plans` view. For more<br>information about these values, see `status` in [Reference for the apg_plan_mgmt.dba_plans view for Aurora PostgreSQL-Compatible Edition](AuroraPostgreSQL.Optimize.dba_plans_view_Reference.md "AuroraPostgreSQL.Optimize.dba_plans_view_Reference.md"). |

## apg_plan_mgmt.update_plans_last_used

Immediately updates the plans table with the `last_used` date stored in
shared memory.

**Syntax**

```
apg_plan_mgmt.update_plans_last_used()
```

**Return value**

None.

**Parameters**

None.

**Usage notes**

Call `update_plans_last_used` to make sure queries against the
`dba_plans.last_used` column use the most current information. If the
`last_used` date isn't updated immediately, a background process
updates the plans table with the `last_used` date once every hour (by
default).

For example, if a statement with a certain `sql_hash` begins to run
slowly, you can determine which plans for that statement were executed since the
performance regression began. To do that, first flush the data in shared memory to
disk so that the `last_used` dates are current, and then query for all
plans of the `sql_hash` of the statement with the performance regression.
In the query, make sure the `last_used` date is greater than or equal to
the date on which the performance regression began. The query identifies the plan or
set of plans that might be responsible for the performance regression. You can use
`apg_plan_mgmt.get_explain_plan` with `explainOptionList`
set to `verbose, hashes`. You can also use
`apg_plan_mgmt.evolve_plan_baselines` to analyze the plan and any
alternative plans that might perform better.

The `update_plans_last_used` function has an effect only on the primary
DB instance of the DB cluster.

## apg_plan_mgmt.validate_plans

Validate that the optimizer can still recreate plans. The optimizer validates
`Approved`, `Unapproved`, and `Preferred`
plans, whether the plan is enabled or disabled. `Rejected` plans are not
validated. Optionally, you can use the `apg_plan_mgmt.validate_plans`
function to delete or disable invalid plans.

**Syntax**

```
apg_plan_mgmt.validate_plans(
    sql_hash,
    plan_hash,
    action)

apg_plan_mgmt.validate_plans(
    action)
```

**Return value**

The number of invalid plans.

**Parameters**

| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sql_hash`  | The `sql_hash` ID of the plan's managed SQL<br>statement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `plan_hash` | The managed plan's `plan_hash` ID. Use NULL to<br>mean all plans for the same `sql_hash` ID value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `action`    | The action the function is to perform for invalid plans. Valid<br>string values include the following. Case does not<br>matter.<br>• `'disable'` – Each invalid plan is<br>disabled.<br>• `'delete'` – Each invalid plan is<br>deleted.<br>• `'update_plan_hash'` – Updates the<br>`plan_hash` ID for plans that can't<br>be reproduced exactly. It also allows you to fix a plan<br>by rewriting the SQL. You can then register the good<br>plan as an `Approved` plan for the original<br>SQL.<br>• NULL – The function simply returns the number<br>of invalid plans. No other action is performed.<br>• '' – An empty string produces a message<br>indicating the number of both valid and invalid<br>plans.<br>Any other value is treated like the empty string. |

**Usage notes**

Use the form `validate_plans(action)` to validate all the managed plans
for all the managed statements in the entire `apg_plan_mgmt.dba_plans`
view.

Use the form `validate_plans(sql_hash, plan_hash, action)` to validate
a managed plan specified with `plan_hash`, for a managed statement
specified with `sql_hash`.

Use the form `validate_plans(sql_hash, NULL, action)` to validate all
the managed plans for the managed statement specified with
`sql_hash`.
