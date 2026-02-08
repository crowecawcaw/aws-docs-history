# Other parameters

that affect autovacuum

The following query shows the values of some of the parameters that directly affect
autovacuum and its behavior. The [autovacuum parameters](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html "https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html") are described fully in the PostgreSQL documentation.

```
SELECT name, setting, unit, short_desc
FROM pg_settings
WHERE name IN (
'autovacuum_max_workers',
'autovacuum_analyze_scale_factor',
'autovacuum_naptime',
'autovacuum_analyze_threshold',
'autovacuum_analyze_scale_factor',
'autovacuum_vacuum_threshold',
'autovacuum_vacuum_scale_factor',
'autovacuum_vacuum_threshold',
'autovacuum_vacuum_cost_delay',
'autovacuum_vacuum_cost_limit',
'vacuum_cost_limit',
'autovacuum_freeze_max_age',
'maintenance_work_mem',
'vacuum_freeze_min_age');
```

While these all affect autovacuum, some of the most important ones are:

- [maintenance_work_mem](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE_WORK_MEM "https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE_WORK_MEM")
- [autovacuum_freeze_max_age](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-FREEZE-MAX-AGE "https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-FREEZE-MAX-AGE")
- [autovacuum_max_workers](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-MAX-WORKERS "https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-MAX-WORKERS")
- [autovacuum_vacuum_cost_delay](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-DELAY "https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-DELAY")
- [autovacuum_vacuum_cost_limit](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-LIMIT "https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-LIMIT")
