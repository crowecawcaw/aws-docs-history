# Post-failure analysis and reset

A review must be conducted after each failure to understand the source of failure as well the reaction of the cluster. In most scenarios, the cluster prevents an application outage. However, a manual action is often required to reset the cluster to a protective state for any subsequent failures.

###### Topics

- [Checking the Logs](#_checking_the_logs "#_checking_the_logs")
- [Cleanup pcs status](#_cleanup_pcs_status "#_cleanup_pcs_status")
- [Restart failed nodes or pacemaker](#_restart_failed_nodes_or_pacemaker "#_restart_failed_nodes_or_pacemaker")
- [Further Analysis](#_further_analysis "#_further_analysis")

## Checking the Logs

- For troubleshooting cluster issues, use journalctl to examine both pacemaker and corosync logs:

```
 # journalctl -u pacemaker -u corosync --since "1 hour ago"
```

    + Use `--since` to specify time periods (e.g., "2 hours ago", "today")
    + Add `-f` to follow logs in real-time
    + Combine with grep for specific searches

- System messages and resource agent activity can be found in `/var/log/messages`.
- For HANA-specific issues, check the HANA trace directory. This can be reached using 'cdtrace' when logged in as <sid>adm. Also consult the DB\_<tenantdb> directory within the HANA trace directory.

## Cleanup pcs status

If failed actions are reported using the `pcs status` command, and if they have already been investigated, then you can clear the reports with the following command.

```
 # pcs resource cleanup <resource> <hostname>
```

## Restart failed nodes or pacemaker

It is recommended that failed (or fenced) nodes are not automatically restarted. It gives operators a chance to investigate the failure, and ensure that the cluster doesn’t make assumptions about the state of resources.

You need to restart the instance or the pacemaker service based on your approach.

## Further Analysis

For cluster-specific issues, use `pcs cluster report` to generate a targeted analysis of cluster components across all nodes:

```
 # pcs cluster report --from="YYYY-MM-DD HH:MM:SS" --to="YYYY-MM-DD HH:MM:SS" /tmp/cluster-report
```

###### Using pcs cluster report

- Specify a time range that encompasses the incident
- The report includes logs and configuration from all nodes
- Review the generated tarball for cluster events, resource operations, and configuration changes
