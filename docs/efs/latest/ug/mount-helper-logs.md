# Getting support logs

The EFS mount helper has built-in logging for your EFS file system. You can
share these logs with AWS Support for troubleshooting purposes. You can find the logs
stored in `/var/log/amazon/efs` on clients using the EFS mount
helper. These logs are for the EFS mount helper, the stunnel process (disabled by
default), and for the `amazon-efs-mount-watchdog` process that monitors the
stunnel process.

###### Note

The `amazon-efs-mount-watchdog` process ensures that each mount's stunnel
process is running, and stops the stunnel process when the EFS file system is
unmounted. If for some reason a stunnel process is terminated unexpectedly, the watchdog
process will restart it.

You can change the log configuration in
`/etc/amazon/efs/efs-utils.conf`. In order for any log changes to take
effect, you need to unmount and remount the file system using the EFS mount
helper. Log capacity for the mount helper and watchdog logs is limited to 20 MiB. Logs for
the stunnel process are disabled by default.

###### Important

You can enable logging for the stunnel process logs. However, enabling the stunnel logs
can use up a nontrivial amount of space on your file system.
