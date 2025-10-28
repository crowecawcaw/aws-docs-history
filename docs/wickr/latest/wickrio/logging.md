This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Wickr IO clients logging

The Wickr IO bots generate log and output files that can be used to determine possible
issues. These files can be accessed on your host where the Wickr IO docker container is running.

In case of any issues, these files should be sent to Wickr Support to allow them to
diagnose any issues that cannot be easily fixed.

###### Note

Output and log files have a maximum file size. When this size is exceeded, a new file is
created. The system keeps up to 5 output and log files on disk.

Logs are generated from three primary components: client provisioning logs, client logs, and
integration logs.

###### Topics

- [Wickr IO client provisioning logs](#provisioning-logs "#provisioning-logs")
- [Wickr IO client logs](#client-logs "#client-logs")
- [Wickr IO integration logs](#integration-logs "#integration-logs")

## Wickr IO client provisioning logs

Provisioning logs are generated when a new or existing bot client is added to the running
Docker container using the docker CLI. To set up a bot client, see[Quick Start section].

Depending on how you setup the shared files, the provisioning log and output files are
located in the following location:

`/opt/WickrIO/logs`

Below is an example of a different shared host volume while starting the docker
container.

```
docker run -v /opt/WickrIOOnHost:/opt/WickrIO -ti public.ecr.aws/x3s2s6k3/wickrio/bot-cloud:latest
```

In the example above, the host directory shared with the Docker container is
`/opt/WickrIOOnHost`. As a result,the logs will be located at:
`/opt/WickrIOOnHost/logs`.

This directory contains several files:

- `WickrIOProvisionLog.output` - Contains detailed information useful for
  diagnosing issues during Wickr IO client provisioning.
- `WickrIOSvr.output` - Helps identify problems that may occur when starting a
  Wickr IO client.

## Wickr IO client logs

Once the Wickr IO Client bot is successfully provisioned, the bot client and the
background services initiate logging for all interactions with Wickr backend, along with
internal system-level processes.

Depending on how you setup the shared files, the provisioning log and output files are
located in the following location:

`/opt/WickrIO/clients/(client name)/logs`

Below is an example of a different shared host volume while starting the docker
container.

```
docker run -v /opt/WickrIOOnHost:/opt/WickrIO -ti public.ecr.aws/x3s2s6k3/wickrio/bot-cloud:latest
```

In the above example, the host directory path shared with the docker container is
`/opt/WickrIOOnHost`, then the logs path will be
`/opt/WickrIOOnHost/clients/(client name)/logs`.

There are several files found in that directory. The file with the “.output” extension
contains the most information and is useful in diagnosing issues with the Wickr IO
client.

To view logs in real time, run the following command from the
`/opt/WickrIO/clients/(client name)/logs` directory:

`tail -f (OutputFileName)`.

## Wickr IO integration logs

Wickr IO integrations also generate log data, which can be helpful for diagnosing issues
specific to the integration type used by the Wickr IO client.

Integration logs are located in the integration-specific directory associated with the
Wickr IO client. For example, a broadcast bot named "test_bot" is running, its integration logs
can be found at:

`/opt/WickrIO/clients/test_bot/integration/wickrio-broadcast-bot/logs`

Typical Wickr IO integrations will write output to a file named "log.output" and error
output will be written to a file named "err.output". Output in the "err.output" is an indication
the integration has crashed.
