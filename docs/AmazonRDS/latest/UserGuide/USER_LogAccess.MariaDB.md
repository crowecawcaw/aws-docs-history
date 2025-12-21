# Log rotation and retention for MariaDB

When logging is enabled, Amazon RDS rotates table logs or deletes log files at regular intervals. This measure is a precaution to reduce the possibility of a
large log file either blocking database use or affecting performance.

The MariaDB slow query log, error log, and the general log file sizes are constrained to
no more than 2 percent of the allocated storage space for a DB instance. To maintain
this threshold, logs are automatically rotated every hour and log files older than
24 hours are removed. If the combined log file size exceeds the threshold after
removing old log files, then the largest log files are deleted until the log file
size no longer exceeds the threshold.

Amazon RDS rotates IAM database authentication error log files larger than 10 MB.
Amazon RDS removes IAM database authentication error log files that are older than five days or larger than 100 MB.
