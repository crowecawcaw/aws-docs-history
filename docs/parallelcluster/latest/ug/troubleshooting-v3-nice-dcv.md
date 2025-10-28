# Troubleshooting issues in Amazon DCV

###### Topics

- [Logs for Amazon DCV](#troubleshooting-v3-nice-dcv-logs "#troubleshooting-v3-nice-dcv-logs")
- [Ubuntu Amazon DCV issues](#troubleshooting-v3-nice-dcv-modules "#troubleshooting-v3-nice-dcv-modules")

## Logs for Amazon DCV

The logs for Amazon DCV are written to files in the `/var/log/dcv/` directory. Reviewing these logs can help to troubleshoot
issues.

The instance type should have at least 1.7 gibibytes (GiB) of RAM to run Amazon DCV. Nano and micro instance types don't have enough memory to run
Amazon DCV.

AWS ParallelCluster creates Amazon DCV log streams in log groups. You can view these logs in the CloudWatch console
**Custom Dashboards** or **Log groups**. For more information,
see [Integration with Amazon CloudWatch Logs](cloudwatch-logs-v3.md "cloudwatch-logs-v3.md") and [Amazon CloudWatch dashboard](cloudwatch-dashboard-v3.md "cloudwatch-dashboard-v3.md").

## Ubuntu Amazon DCV issues

When running Gnome Terminal over a Amazon DCV session on Ubuntu, you might not automatically have access to the user environment that
AWS ParallelCluster makes available through the login shell. The user environment provides environment modules such as openmpi or intelmpi, and
other user settings.

Gnome Terminal's default settings prevent the shell from starting as a login shell. This means that shell profiles aren't
automatically sourced and the AWS ParallelCluster user environment isn't loaded.

To properly source the shell profile and access the AWS ParallelCluster user environment, do one of the following:

- ###### Change the default terminal settings:
  1.  Choose the **Edit** menu in the Gnome terminal.
  2.  Select **Preferences**, then **Profiles**.
  3.  Choose **Command** and select **Run Command as login shell**.
  4.  Open a new terminal.

- Use the command line to source the available profiles:

```
`$` `source /etc/profile && source $HOME/.bashrc`
```
