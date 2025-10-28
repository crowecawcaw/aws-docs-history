# Prepare to take a DigIF contact

1. Review CPU Core Planning for desired dataflows, and provide a list of cores the agent can use. See [CPU core planning](agent-instance-selection.md#cpu-core-planning "agent-instance-selection.md#cpu-core-planning").
2. Review the AWS Ground Station Agent configuration file. See [AWS Ground Station Agent configuration](managing-agent.md#gs-agent-configuration "managing-agent.md#gs-agent-configuration").
3. Confirm that the necessary performance tuning is applied. See [Tune your EC2 instance for performance](ec2-instance-performance-tuning.md "ec2-instance-performance-tuning.md").
4. Confirm you are following all the called out best practices. See [Best practices](best-practices.md "best-practices.md").
5. Confirm that the AWS Ground Station Agent is started prior to the scheduled contact start time via:

```

systemctl status aws-groundstation-agent

```

6. Confirm that the AWS Ground Station Agent is healthy prior to the scheduled contact start time via:

```

aws groundstation get-dataflow-endpoint-group --dataflow-endpoint-group-id ${DATAFLOW-ENDPOINT-GROUP-ID} --region ${REGION}

```

Verify that the `agentStatus` of your `awsGroundStationAgentEndpoint` is ACTIVE and the `auditResults` is HEALTHY.
