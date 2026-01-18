# Post-failure analysis and reset

A review must be conducted after each failure to understand the source of failure as well the reaction of the cluster. In most scenarios, the cluster prevents an application outage. However, a manual action is often required to reset the cluster to a protective state for any subsequent failures.

###### Topics

- [Checking the logs](#checking-logs-nw-rhel "#checking-logs-nw-rhel")
- [Cleanup pcs status](#cleanup-crm-nw-rhel "#cleanup-crm-nw-rhel")
- [Restart failed nodes or pacemaker](#restart-nodes-nw-rhel "#restart-nodes-nw-rhel")
- [Further Analysis](#_further_analysis "#_further_analysis")

## Checking the logs

- For troubleshooting cluster issues, use journalctl to examine both pacemaker and corosync logs:

```
 # journalctl -u pacemaker -u corosync --since "1 hour ago"
```

    + Use `--since` to specify time periods (e.g., "2 hours ago", "today")
    + Add `-f` to follow logs in real-time
    + Combine with grep for specific searches

- System messages and resource agent activity can be found in `/var/log/messages`.

Application based failures can be investigated in the SAP work directory.

## Cleanup pcs status

If failed actions are reported using the `pcs status` command, and if they have already been investigated, then you can clear the reports with the following command.

```
 # pcs resource cleanup <resource> <hostname>
```

## Restart failed nodes or pacemaker

It is recommended that failed (or fenced) nodes are not automatically restarted. It gives operators a chance to investigate the failure, and ensure that the cluster doesn’t make assumptions about the state of resources.

You need to restart the instance or the pacemaker service based on your approach.

## Further Analysis

For cluster-specific issues, use `sosreport` to generate a targeted analysis of cluster components:

```
 # sosreport --batch --tmp-dir /tmp
```

For quick analysis of recent events, you can use:

```
 # pcs status --full
# journalctl -u pacemaker --since "1 hour ago"
```

- `sosreport` collects system configuration and diagnostic information
- For more information, see Red Hat Documentation - [What is sosreport and how to create and retrieve one](https://access.redhat.com/solutions/3592 "https://access.redhat.com/solutions/3592")
