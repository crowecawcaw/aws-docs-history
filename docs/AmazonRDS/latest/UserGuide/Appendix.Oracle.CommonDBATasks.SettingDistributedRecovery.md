

# Setting distributed recovery

To set distributed recovery, use the Amazon RDS procedures `rdsadmin.rdsadmin_util.enable_distr_recovery` and `disable_distr_recovery`. The procedures have no parameters. 

The following example enables distributed recovery.

```sql
EXEC rdsadmin.rdsadmin_util.enable_distr_recovery;
```

The following example disables distributed recovery.

```sql
EXEC rdsadmin.rdsadmin_util.disable_distr_recovery;
```