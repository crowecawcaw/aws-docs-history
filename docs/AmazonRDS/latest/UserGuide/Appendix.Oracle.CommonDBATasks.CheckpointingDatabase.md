

# Checkpointing a database

To checkpoint the database, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.checkpoint`. The `checkpoint` procedure has no parameters. 

The following example checkpoints the database.

```sql
EXEC rdsadmin.rdsadmin_util.checkpoint;
```