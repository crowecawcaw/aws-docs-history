

# Agent logs and diagnostics
<a name="agent-diagnostics"></a>

When troubleshooting Elastic Disaster Recovery agent issues, start by checking the service status and reviewing recent log entries. This page provides commands for checking agent health and gathering diagnostic information for support cases.

**Topics**
+ [Check agent status and logs](#agent-log-locations)
+ [Common log patterns](#agent-log-patterns)
+ [Gather diagnostic information for support](#agent-diagnostic-tools)

## Check agent status and logs
<a name="agent-log-locations"></a>

Use the following commands to verify that the replication agent is running and to review recent log output.

------
#### [ Linux ]

Check the agent service status:

```
systemctl status aws-replication-agent
```

View the most recent log entries:

```
tail -100 /var/lib/aws-replication-agent/agent.log.0
```

Search for errors in the log file:

```
grep -i "ERROR\|FATAL" /var/lib/aws-replication-agent/agent.log.0
```

**Note**  
The agent log file is located at `/var/lib/aws-replication-agent/agent.log.0`. The service name is `aws-replication-agent`.

------
#### [ Windows ]

Check the agent service status:

```
Get-Service AwsReplicationService
```

View the most recent log entries:

```
Get-Content "C:\Program Files (x86)\AWS Replication Agent\agent.log.0" -Tail 100
```

Search for errors in the log file:

```
Select-String -Pattern "ERROR|FATAL" -Path "C:\Program Files (x86)\AWS Replication Agent\agent.log.0"
```

**Note**  
The agent log file is located at `C:\Program Files (x86)\AWS Replication Agent\agent.log.0`. The service name is `AwsReplicationService`.

------

## Common log patterns
<a name="agent-log-patterns"></a>

Look for the following patterns in agent logs to identify the root cause of issues.
+ **FATAL or ERROR entries** — Indicate agent failures that require immediate attention.
+ **Connection refused** — Indicates a network connectivity issue. Verify that the source server can reach the AWS replication endpoints.
+ **Certificate errors** — Indicates TLS or certificate trust issues. Verify that the source server trusts the AWS root certificates.
+ **Timeout** — Indicates a firewall blocking traffic or an unreachable endpoint. Check security group rules and network ACLs.

## Gather diagnostic information for support
<a name="agent-diagnostic-tools"></a>

Use the following tools to collect system details before opening a support case.

------
#### [ Linux ]

Run the AWS Linux system details tool:

[https://github.com/awslabs/mgn-drs-linux-system-details-tool](https://github.com/awslabs/mgn-drs-linux-system-details-tool)

Check the agent version:

```
cat /var/lib/aws-replication-agent/agent.version
```

------
#### [ Windows ]

Run the AWS Windows support tool:

[https://github.com/awslabs/aws-support-tools/tree/master/MGN/Windows](https://github.com/awslabs/aws-support-tools/tree/master/MGN/Windows)

------

Include the following information in your support case:
+ Agent log files (`agent.log.0`)
+ Diagnostic tool output
+ Operating system version
+ Agent version