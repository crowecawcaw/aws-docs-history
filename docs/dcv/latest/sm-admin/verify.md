# Step 5: Verify the installations

After you have set up the agent, set up the broker, and configured both on the Amazon DCV server,
you need to verify that the installations are functioning properly.

###### Topics

- [Verify the agent](#verify-broker-agent "#verify-broker-agent")
- [Verify the broker](#verify-client-broker "#verify-client-broker")

## Verify the agent

After you have installed the broker and the agent, make sure that the agent is running and
that it's able to connect to the broker.

###### Linux agent host

The command to run depends on the version.

- Since version 2022.0

From the agent host, run the following command:

```
`$` grep 'sessionsUpdateResponse' /var/log/dcv-session-manager-agent/agent.log | tail -1 | grep -o success
```

- Versions prior to 2022.0

From the agent host, run the following command, and specify the current year, month, and
day.

```
`$` grep 'sessionsUpdateResponse' /var/log/dcv-session-manager-agent/agent.log.`yyyy`-`mm`-`dd` | tail -1 | grep -o success
```

For example

```
`$` grep 'sessionsUpdateResponse' /var/log/dcv-session-manager-agent/agent.log.2020-11-19 | tail -1 | grep -o success
```

If the agent is running and it's able to connect to the broker, the command should return
`success`.

If the command returns different output, inspect the agent log file for more information.
The log files are located here: `/var/log/dcv-session-manager-agent/`.

###### Windows agent host

Open the agent log file, which is located in `C:\ProgramData\NICE\DCVSessionManagerAgent\log`.

If the log file includes a line similar to the one below, the agent is running and it's
able to connect to the broker.

```
2020-11-02 12:38:03,996919  INFO ThreadId(05) dcvsessionmanageragent::agent:Processing broker message "{\n  \"sessionsUpdateResponse\" : {\n    \"requestId\" : \"69c24a3f5f6d4f6f83ffbb9f7dc6a3f4\",\n    \"result\" : {\n      \"success\" : true\n    }\n  }\n}"
```

If your log file doesn’t have a similar line, inspect the log file for errors.

## Verify the broker

After you have installed the broker and agent, make sure that your broker is running and
that it's reachable from your users and front-end applications.

From a computer that should be able to reach the broker, run the following command:

```
`$` curl -X GET https://`broker_host_ip`:`port`/sessionConnectionData/aSession/aOwner --insecure
```

If the verification is successful, the broker returns the following:

```
{
    "error": "No authorization header"
}
```
