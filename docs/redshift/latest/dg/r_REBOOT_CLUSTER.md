Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# REBOOT\_CLUSTER

Reboot the Amazon Redshift cluster without closing the connections to the cluster. You must be a
database superuser to run this command.

After this soft reboot has completed, the Amazon Redshift cluster returns an error to the user application and requires the user application to resubmit any transactions or queries interrupted by the soft reboot.

## Syntax

```
SELECT REBOOT_CLUSTER();
```
