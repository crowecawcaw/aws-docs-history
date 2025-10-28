# Logging Session Script Output

When this option is enabled in the configuration file, AppStream 2.0 automatically
captures the output from the session script that is written to the standard out.
This output is uploaded to an Amazon S3 bucket in your account. You can review the log
files for troubleshooting or debugging purposes.

###### Note

The log files are uploaded when the session script returns a value, or the
value set in `WaitingTime` has elapsed, whichever comes
first.
