# Removing the only continuous backup rule from a backup plan

When you create a backup plan with a continuous backup rule and then you remove that
rule, AWS Backup remembers the retention period from your now-deleted rule. It will delete the
continuous backup from your backup vault when the retention period elapses.
