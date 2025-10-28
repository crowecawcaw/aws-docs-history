# Exporting and

importing managed plans for Aurora PostgreSQL

You can export your managed plans and import them into another DB instance.

###### To export managed plans

An authorized user can copy any subset of the `apg_plan_mgmt.plans`
table to another table, and then save it using the `pg_dump` command. The
following is an example.

```
CREATE TABLE plans_copy AS SELECT *
FROM apg_plan_mgmt.plans [ WHERE predicates ] ;
```

```
`%` pg_dump --table apg_plan_mgmt.plans_copy -Ft mysourcedatabase > plans_copy.tar
```

```
DROP TABLE apg_plan_mgmt.plans_copy;
```

###### To import managed plans

1. Copy the .tar file of the exported managed plans to the system where the plans
   are to be restored.
2. Use the `pg_restore` command to copy the tar file into a new table.

```
`%` pg_restore --dbname mytargetdatabase -Ft plans_copy.tar
```

3. Merge the `plans_copy` table with the
   `apg_plan_mgmt.plans` table, as shown in the following
   example.

###### Note

In some cases, you might dump from one version of the
`apg_plan_mgmt` extension and restore into a different
version. In these cases, the columns in the plans table might be different.
If so, name the columns explicitly instead of using SELECT \*.

```
`INSERT INTO apg_plan_mgmt.plans SELECT * FROM plans_copy
 ON CONFLICT ON CONSTRAINT plans_pkey
 DO UPDATE SET
 status = EXCLUDED.status,
 enabled = EXCLUDED.enabled,`
 `-- Save the most recent last_used date
 --`
 `last_used = CASE WHEN EXCLUDED.last_used > plans.last_used
 THEN EXCLUDED.last_used ELSE plans.last_used END,`
 `-- Save statistics gathered by evolve_plan_baselines, if it ran:
 --`
 `estimated_startup_cost = EXCLUDED.estimated_startup_cost,
 estimated_total_cost = EXCLUDED.estimated_total_cost,
 planning_time_ms = EXCLUDED.planning_time_ms,
 execution_time_ms = EXCLUDED.execution_time_ms,
 total_time_benefit_ms = EXCLUDED.total_time_benefit_ms,
 execution_time_benefit_ms = EXCLUDED.execution_time_benefit_ms;`
```

4. Reload the managed plans into shared memory and remove the temporary plans
   table.

```
`SELECT apg_plan_mgmt.reload();` `-- refresh shared memory`
`DROP TABLE plans_copy;`
```
