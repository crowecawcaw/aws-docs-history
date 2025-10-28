# Troubleshooting Mountpoint

Mountpoint for Amazon S3 is backed by Support. If you need assistance, contact the
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

You can also review and submit Mountpoint [Issues](https://github.com/awslabs/mountpoint-s3/issues "https://github.com/awslabs/mountpoint-s3/issues") on
GitHub.

If you discover a potential security issue in this project, we ask that you notify AWS
Security through our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/ "http://aws.amazon.com/security/vulnerability-reporting/"). Do not create a public GitHub
issue.

If your application behaves unexpectedly with Mountpoint, you can inspect your log
information to diagnose the problem.

**Logging**

By default, Mountpoint emits high-severity log information to [syslog](https://datatracker.ietf.org/doc/html/rfc5424 "https://datatracker.ietf.org/doc/html/rfc5424").

To view logs on most modern Linux distributions, including Amazon Linux, run the
following `journald` command:

```
journalctl -e SYSLOG_IDENTIFIER=mount-s3
```

On other Linux systems, `syslog` entries are likely written to a
file such as `/var/log/syslog`.

You can use these logs to troubleshoot your application. For example, if your application
tries to overwrite an existing file, the operation fails, and you will see a line similar to
the following in the log:

```
[WARN] open{req=12 ino=2}: mountpoint_s3::fuse: open failed: inode error: inode 2 (full key "README.md") is not writable
```

For more information, see Mountpoint for Amazon S3 [Logging](https://github.com/awslabs/mountpoint-s3/blob/main/doc/LOGGING.md "https://github.com/awslabs/mountpoint-s3/blob/main/doc/LOGGING.md") on
GitHub.
