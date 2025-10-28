# Troubleshooting

## Agent fails to start

The AWS Ground Station Agent may fail to start due to several reasons, but the most common scenario might be a misconfigured agent configuration file.
After starting the agent (see [AWS Ground Station Agent start](managing-agent.md#gs-agent-start "managing-agent.md#gs-agent-start")) you might get a status such as:

```

#agent is automatically retrying a restart
aws-groundstation-agent.service - aws-groundstation-agent
Loaded: loaded (/usr/lib/systemd/system/aws-groundstation-agent.service; enabled; vendor preset: disabled)
Active: activating (auto-restart) (Result: exit-code) since Fri 2023-03-10 01:48:14 UTC; 23s ago
Docs: https://aws.amazon.com/ground-station/
Process: 43038 ExecStart=/opt/aws/groundstation/bin/launch-aws-gs-agent (code=exited, status=101)
Main PID: 43038 (code=exited, status=101)

#agent has failed to start
aws-groundstation-agent.service - aws-groundstation-agent
Loaded: loaded (/usr/lib/systemd/system/aws-groundstation-agent.service; enabled; vendor preset: disabled)
Active: failed (Result: start-limit) since Fri 2023-03-10 01:50:15 UTC; 13s ago
Docs: https://aws.amazon.com/ground-station/
Process: 43095 ExecStart=/opt/aws/groundstation/bin/launch-aws-gs-agent (code=exited, status=101)
Main PID: 43095 (code=exited, status=101)

```

### Troubleshooting

```

sudo journalctl -u aws-groundstation-agent | grep -i -B 3 -A 3 'Loading Config' | tail -6

```

might result in an output of:

```

launch-aws-gs-agent[43095]: Running with options Production(ProductionOptions { endpoint: None, region: None })
launch-aws-gs-agent[43095]: Loading Config
launch-aws-gs-agent[43095]: System has 96 logical cores
systemd[1]: aws-groundstation-agent.service: main process exited, code=exited, status=101/n/a
systemd[1]: Unit aws-groundstation-agent.service entered failed state.

```

Failure to start the agent after “Loading Config” indicates an issue with the agent configuration.
See [Agent config file](configuring-agent.md#agent-config-file "configuring-agent.md#agent-config-file") to verify your agent configuration.

## AWS Ground Station Agent logs

AWS Ground Station Agent writes information about contact executions, errors, and health status to log files on the instance running the agent.
You can view the log files by manually connecting to an instance.

You can view agent logs in the following location.

```

/var/log/aws/groundstation

```

## No contacts available

Scheduling contacts requires a healthy AWS Ground Station Agent. Please confirm that your AWS Ground Station Agent has started and that it is healthy by querying the AWS Ground Station API via get-dataflow-endpoint-group:

```

aws groundstation get-dataflow-endpoint-group --dataflow-endpoint-group-id ${DATAFLOW-ENDPOINT-GROUP-ID} --region ${REGION}

```

Verify that the `agentStatus` of your `awsGroundStationAgentEndpoint` is ACTIVE and the `auditResults` is HEALTHY.
