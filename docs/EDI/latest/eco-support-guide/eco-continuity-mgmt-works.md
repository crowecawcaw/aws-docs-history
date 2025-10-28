# How continuity management works

AMS backup plans for EDI deﬁne how frequently AWS Backup backs up your data and the retention policy for your backups. ECO backup vaults keep your backup data organized.
After you associate a compatible resource with a backup plan, AWS Backup automatically backs up the resource. The ﬁrst backup is a full copy, and subsequent backups
capture incremental changes.

The ECO team applies the default backup plan for your EDI environment that provides a reasonable restoration and retention period. However,
there are other enhanced and data sensitive backup plans. To determine the most effective backup plan for your environment, work with your E-SDM when you're onboarding.

The following table lists the backup plan restoration and retention periods.

| Default backup plan | Start time                       | Retention |
| ------------------- | -------------------------------- | --------- |
| hourly backup       | N/A                              | N/A       |
| daily backup        | daily 4:00 UTC                   | 7 days    |
| weekly backup       | Saturday, 2:00 UTC               | 4 weeks   |
| monthly backup      | First day of the month, 2:00 UTC | 26 weeks  |
| yearly backup       | Jan 1, 2:00 UTC                  | 2 years   |
