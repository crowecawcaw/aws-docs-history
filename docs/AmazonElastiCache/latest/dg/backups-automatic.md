# Scheduling automatic backups

You can enable automatic backups for any Valkey or Redis OSS serverless cache or node-based cluster.
When automatic backups are
enabled, ElastiCache creates a backup of the cache on a daily basis. There is no impact
on the cache and the change is immediate. Automatic backups can
help guard against data loss. In the event of a failure, you can create a new cache,
restoring your data from the most recent backup. The result is a warm-started cache,
preloaded with your data and ready for use. For more information, see [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").

You can enable automatic backups for any Memcached Serverless cache. When automatic backups are
enabled, ElastiCache creates a backup of the cache on a daily basis. There is no impact
on the cache and the change is immediate. Automatic backups can
help guard against data loss. In the event of a failure, you can create a new cache,
restoring your data from the most recent backup. The result is a warm-started cache,
preloaded with your data and ready for use. For more information, see [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").

When you schedule automatic backups, you should plan the following settings:

- Backup start time – A time of day
  when ElastiCache begins creating a backup.
  You can set the backup window for any time when it's most convenient.
  If you don't specify a backup window, ElastiCache assigns one automatically.
- Backup retention limit – The number of
  days the backup is retained in Amazon S3. For example, if you set the retention limit
  to 5, then a backup taken today is retained for 5 days. When the retention limit
  expires, the backup is automatically deleted.

The maximum backup retention limit is 35 days. If the backup retention limit
is set to 0, automatic backups are disabled for the cache.
When you schedule automatic backups, ElastiCache will begin creating the backup.
You can set the backup window for any time when it's most convenient.
If you don't specify a backup window, ElastiCache assigns one automatically.

You can enable or disable automatic backups when either creating a new cache or updating an existing cache,
by using the ElastiCache console, the AWS CLI, or the ElastiCache API. For Valkey and Redis OSS, this is done by checking the
**Enable Automatic Backups** box in the **Advanced Valkey Settings** or **Advanced Redis OSS Settings** section. For Memcached, this is done by checking the
**Enable Automatic Backups** box in the **Advanced Memcached
Settings** section.
