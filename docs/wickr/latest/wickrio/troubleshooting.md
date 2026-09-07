

This guide provides documentation for Wickr IO Integrations. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Wickr IO clients troubleshooting
<a name="troubleshooting"></a>

**Topics**
+ [Bot runtime architecture](#bot-architecture)
+ [Setting up Wickr IO Docker container](#troubleshooting-docker-container)
+ [Provisioning Wickr IO client](#troubleshooting-provisioning)
+ [Start bot client failures](#troubleshooting-failures)
+ [Wickr IO command line interface](#troubleshooting-command-line-interface)
+ [Client and Integration compatibility issues](#troubleshooting-compatibility-issues)
+ [Deploying custom Integrations](#troubleshooting-deploying-integrations)
+ [Monitor bot health with Amazon CloudWatch](#bot-monitoring)
+ [Collect bot logs](#bot-logging)
+ [Common issues](#troubleshooting-common-issues)
+ [Upgrading bots](#upgrading-bots)
+ [Improve bot resilience](#bot-resilience)

These are troubleshooting suggestions associated with running the Wickr IO gateway, clients, and integrations. You may also run into some issues when developing your own custom Wickr IO integrations.

This section will describe some possible issues you may run into while using the Wickr IO client and the associated services

**Note**  
AWS Support can help with AWS Wickr service configuration, network settings, and the Wickr bot SDK APIs. For issues with custom bot logic, container infrastructure, or host environment, contact your internal development or operations team.

## Bot runtime architecture
<a name="bot-architecture"></a>

Each Wickr IO bot has three layers, which AWS recommends independent monitoring for:

1. **Host** – The Amazon EC2 instance or on-premises server running Docker.

1. **Container** – The Wickr IO Docker container (`wickrio/bot-cloud` or `wickrio/bot-cloud-govcloud`).

1. **Bot process** – Your Node.js integration running inside the container.

The container can report as running while the bot process inside it has crashed or lost its connection to the Wickr network. Effective monitoring covers all three layers.

## Setting up Wickr IO Docker container
<a name="troubleshooting-docker-container"></a>

**Cannot load Docker image**

If you receive the following error then you may have to make sure you have permissions to access the unix socket to communicate with the Docker engine:

 `docker: Got permission denied while trying to connect to the Docker daemon socket at unix:...` 

**Solution**:

For help setting the appropriate permissions for you Docker account, see [Linux post-installation steps for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/)

**Wickr IO Fails startup due to directory permissions**

When running the Docker container on a Mac system, you may encounter a failure when starting the Wickr IO Docker container if you have not changed the write permissions for the `/opt` directory. This issue typically arises after the `./start.sh` command. You will see the following errors:

```
  "QIODevice::write (QFile, "/opt/WickrIO/logs/WickrIOSvr.output"): device not open
terminate called after throwing an instance of 'zmq::error_t'
what(): No such file or directory
./start.sh: line 3: 7 Aborted WickrIOSvr"
```

 This issue has only been seen on Mac systems. It occurs when a user creates the `/opt` directory as the root, and then runs the container as a user.

**Solution**:

This is caused by a permission issue in the `/opt` directory. To resolve the issue, change the permissions of the `/opt/WickrIO` directory (or the name of the directory you created for your installation) to make it writeable. The following command will fix this problem:

```
chmod 777 /opt/WickrIO
```

**Host system running out of disk space**

Your system is low on storage, preventing you from downloading and running a new Docker container. This issue may arise if you have not removed old Docker containers from your system.

**Solution**:
+ Run `docker ps` to see all running containers.
+ Run `docker kill container_id` on a container you would like to stop using.
+ Run `docker rm container_id` to remove it from your system completely.
**Note**  
Your integrations will not be affected and will stay on your system in your `/opt/WickrIO` directory for future use.

**Docker Mounts denied Error**

You're getting the following error: `docker: Error response from daemon: Mounts denied: The path /opt/WickrIO is not shared from OS X and is not known to Docker.`

**Solution**:

Restart Docker.

**Wickr IO Not working on Mac M1 hosts**

The Wickr IO Docker images are not built to run on the Mac M1 hosts. During our testing of the Mac M1 hardware, we discovered an issue related to the interaction exec() commands, which led to failures when trying to start a bot from the command line interface (CLI).

**Solution**:

If you want to run the Wickr IO Docker images on Mac M1 hardware, follow these steps:
+ Make sure you have a version of Docker that supports the Linux/amd64 platform. The version we recommend for Mac is 20.10.14.
+ When using the docker run command, make sure to include the —platform=linux/amd64 option

## Provisioning Wickr IO client
<a name="troubleshooting-provisioning"></a>

**Bot client provisioning failures**

When adding a bot client to a Docker image, you may encounter issues during the provisioning step. This can occur for both new and existing clients. Below are some common problems you might face:

***Username does not exist:***

![The username is does not exist.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickr-username.png)


**Solution**

Make sure the bot username is correct and exists in the Wickr Admin Console.

***Incorrect password:***

![The password is incorrect.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickr-incorrect-password.png)


**Solution**

Make sure the password entered is correct. It should match the one used when creating the bot user in the Wickr Admin Console.

**Note**  
If your issue is different from the scenarios defined above, you can also identify the issue by looking at the provisioning logs found in the following file: `/opt/WickrIO/WickrIOProvisionLog.output`  
For further assistance, [Wickr support ](https://mailto:wickr-support@amazon.com) is always available to assist you with any issues that are not addressed here.

## Start bot client failures
<a name="troubleshooting-failures"></a>

***Incorrect password***

When trying to start a bot client, if you enter an incorrect password, you will get a “Bus Error” and see the Docker container has exited.

![The password is incorrect.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickr-wrong-password.png)


**Solution**
+ Remove the stopped container using ` docker rm -f (container-name).`
+ Set up the docker container again by sharing a different host volume.

***Wickr IO client does not start***

If your Wickr IO client isn't starting and the previous solutions haven't resolved the issue, try the following steps. First, check if the client is running by using the `ps` command. Enter the following command in the terminal:

`ps -aef | grep wickrio_bot`

This command should return an entry for each Wickr IO client that is currently running. Additionally, the command line interface of the Wickr IO Docker container includes various commands that can help you diagnose any client issues.
+ Enter the ` list` command to see the list of Wickr IO clients.
+ If the client state is `Paused` then use the `start` command to start the client.
+ If the client state is `Running` and there are still no associated process running, then check the `WickrIOSvr.output` file for the background services to see if there is any issue starting the client. For more information on logging details, see [ Wickr IO clients logging](https://docs.aws.amazon.com/wickr/latest/wickrio/logging.html).

## Wickr IO command line interface
<a name="troubleshooting-command-line-interface"></a>

***Wickr IO client is not running.***

Once the client has started, it should remain in the `Running` state unless it is manually paused or deleted. If, at any point, your client enters a `Down` or `Not Running` state unexpectedly, follow the solution below.

**Solution:**

Try restarting the Wickr IO client using the `restart` command. If the issue continues, check the provisioning and client logs for more information, and then contact Wickr Support.

***Turn on debugging in Wickr IO CLI***

If you are facing issues with performing any operation using the Wickr IO command line interface like adding or deploying a custom bot , this procedure will help you view more detailed debugging information on the command line interface.

**Solution**

To enable debugging, enter `debug` in the CLI.

**Note**  
This action will output a lot of debug information with this option enabled.

![Turn debug on.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickr-debug.png)


## Client and Integration compatibility issues
<a name="troubleshooting-compatibility-issues"></a>

With the release of new Wickr IO Docker images containing changes to the Wickr IO Add-on APIs, when you upgrade your container to use the new version, it is possible there will be compatibility issues that will cause Integrations to not work. 

**Solution**

If you are running an officially Wickr supported integration, you will see the **Needs Upgrade** text on your Wickr IO client.

To upgrade your integration to avoid any compatibility issues, complete the following steps.

1. Pause the running client using `pause (index)` command.

1. Upgrade the client using `upgrade (index)` command.

1. Start the client again.

If you are using a custom integration, make sure to update your integration to ensure compatibility with the updated Wickr IO container. 

If you need to contact Wickr support it's helpful to have the version number of the Docker container ready. You can find the version number by using the `version` command in the Wickr IO command line interface. Additionally, new versions of the Wickr IO Docker image will display the version numbers of the integrations when you run the `list` command. When addressing integration issues, having the version numbers for the integrations will also be beneficial.

## Deploying custom Integrations
<a name="troubleshooting-deploying-integrations"></a>

***Cannot import a custom integration***

If the necessary files are missing from the software.tar.gz imported into the Docker container, you will receive an "install shell file does not exist" error when starting a Wickr IO client using your custom integration.

![The custom integration command.](http://docs.aws.amazon.com/wickr/latest/wickrio/images/wickr-custom-integration.png)


**Solution**

Make sure all the required files are present in the zipped integration software imported in the docker container. You can use any sample integrations as reference.

## Monitor bot health with Amazon CloudWatch
<a name="bot-monitoring"></a>

The following table summarizes the monitoring approaches for each layer, from simplest to most comprehensive.


| Layer | What it catches | Effort | Reliability | 
| --- | --- | --- | --- | 
| Amazon EC2 status check | Host failure, hardware issues | None (built-in) | High | 
| Container metric | Docker crash, OOM kill, restart loop | Low | Medium | 
| Log-based metric filter | Container crash, restart loop (container output only) | Low | Low | 
| Heartbeat metric | All of the above, plus silent disconnects and event loop blocks | Medium | High | 

For production bots, we recommend implementing all four approaches. They are not redundant – each catches different failure modes.

### Monitor the host instance
<a name="monitor-host"></a>

Use the built-in Amazon EC2 `StatusCheckFailed` metric to detect host-level failures. On supported instance types, Amazon EC2 simplified automatic recovery is enabled by default and automatically migrates the instance to healthy hardware when a status check fails. The alarm below is informational – it notifies you that a recovery occurred, but no manual action is required. For more information, see [Recover your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) in the *Amazon EC2 User Guide*.

```
HostDownAlarm:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmName: !Sub "${BotName}-HostDown"
    Namespace: AWS/EC2
    MetricName: StatusCheckFailed
    Dimensions:
      - Name: InstanceId
        Value: !Ref BotInstance
    Statistic: Maximum
    Period: 60
    EvaluationPeriods: 2
    Threshold: 1
    ComparisonOperator: GreaterThanOrEqualToThreshold
    AlarmActions:
      - !Ref AlertTopic
```

### Monitor the Docker container
<a name="monitor-container"></a>

Create a script on the host that publishes a custom CloudWatch metric based on container status. Run it every minute using `cron`. For example:

```
#!/bin/bash
# /opt/wickr-bot/monitor.sh
CONTAINER_NAME="${1:-wickr-bot}"
NAMESPACE="WickrIO/Bots"

STATUS=$(docker inspect --format='{{.State.Running}}' "$CONTAINER_NAME" 2>/dev/null)

aws cloudwatch put-metric-data \
  --namespace "$NAMESPACE" \
  --metric-name ContainerRunning \
  --dimensions BotName="$CONTAINER_NAME" \
  --value "$([ "$STATUS" = "true" ] && echo 1 || echo 0)" \
  --unit Count
```

Add a cron entry to run the script:

```
* * * * * /opt/wickr-bot/monitor.sh {{container-name}}
```

Create an alarm that fires when the value drops to 0.

### Monitor with log-based metric filters
<a name="monitor-logs"></a>

If you forward container logs to Amazon CloudWatch Logs using the `awslogs` driver, you can create a metric filter that counts log events. When the container stops producing output, the alarm fires.

1. Open the Amazon CloudWatch console and navigate to **Log groups**.

1. Select your bot's log group (`/wickr/bots/{{bot-name}}`).

1. Choose **Metric filters**, then **Create metric filter**.

1. For **Filter pattern**, enter a single space (`" "`) to match any log line.

1. Set the metric namespace to `WickrIO/Bots` and the metric name to `BotLogEvents`.

1. Create an alarm on this metric: `Sum < 1` over a 5-minute period.

### Add a heartbeat metric (recommended)
<a name="monitor-heartbeat"></a>

A heartbeat metric is the most reliable approach because it proves the Node.js process is alive and the event loop is not blocked. Add the following to your bot's entry point, after the bot starts successfully. For example:

```
const { CloudWatchClient, PutMetricDataCommand } = require('@aws-sdk/client-cloudwatch')
const cw = new CloudWatchClient()
const BOT_NAME = process.env.BOT_NAME || 'wickr-bot'

setInterval(async () => {
  try {
    await cw.send(new PutMetricDataCommand({
      Namespace: 'WickrIO/Bots',
      MetricData: [{
        MetricName: 'Heartbeat',
        Dimensions: [{ Name: 'BotName', Value: BOT_NAME }],
        Value: 1,
        Unit: 'Count'
      }]
    }))
  } catch (e) { console.error('Heartbeat publish failed:', e.message) }
}, 60000)
```

Add the `@aws-sdk/client-cloudwatch` dependency to your bot's `package.json`.

Create an alarm on the heartbeat metric. For example:

```
BotProcessAlarm:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmName: !Sub "${BotName}-ProcessDown"
    Namespace: WickrIO/Bots
    MetricName: Heartbeat
    Dimensions:
      - Name: BotName
        Value: !Ref BotName
    Statistic: Sum
    Period: 300
    EvaluationPeriods: 2
    Threshold: 1
    ComparisonOperator: LessThanThreshold
    TreatMissingData: breaching
    AlarmActions:
      - !Ref AlertTopic
```

Set `TreatMissingData` to `breaching` so the alarm fires when the metric stops arriving entirely, rather than entering `INSUFFICIENT_DATA`.

### Monitor memory usage
<a name="monitor-memory"></a>

Node.js bots that maintain session state, cache data, or process file attachments can develop memory leaks over time. If the bot's memory usage exceeds the Docker container's memory limit, Docker terminates the container with an out-of-memory (OOM) kill. The container restarts automatically if you configured the `--restart` policy, but active user sessions and in-flight messages are lost.

To detect memory growth before it causes an OOM kill, publish the Node.js heap usage alongside your heartbeat metric. For example:

```
setInterval(async () => {
  const mem = process.memoryUsage()
  try {
    await cw.send(new PutMetricDataCommand({
      Namespace: 'WickrIO/Bots',
      MetricData: [
        {
          MetricName: 'Heartbeat',
          Dimensions: [{ Name: 'BotName', Value: BOT_NAME }],
          Value: 1, Unit: 'Count'
        },
        {
          MetricName: 'HeapUsedMB',
          Dimensions: [{ Name: 'BotName', Value: BOT_NAME }],
          Value: Math.round(mem.heapUsed / 1048576),
          Unit: 'Megabytes'
        }
      ]
    }))
  } catch (e) { console.error('Metric publish failed:', e.message) }
}, 60000)
```

Create a CloudWatch alarm that fires when heap usage exceeds 80% of the container's memory limit. For example, if the container has a 512 MB memory limit (`--memory=512m`), set the threshold to 410 MB. Adjust the threshold to 80% of your configured limit.

```
MemoryAlarm:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmName: !Sub "${BotName}-HighMemory"
    Namespace: WickrIO/Bots
    MetricName: HeapUsedMB
    Dimensions:
      - Name: BotName
        Value: !Ref BotName
    Statistic: Maximum
    Period: 300
    EvaluationPeriods: 3
    Threshold: 410
    ComparisonOperator: GreaterThanThreshold
    AlarmActions:
      - !Ref AlertTopic
```

**Remediation**
+ **Immediate:** Restart the container with `docker restart {{container-name}}`. This clears the Node.js heap without losing the WickrIO registration database.
+ **Preventive:** Set a Docker memory limit with `--memory=512m` when starting the container to prevent a leaking bot from consuming all host memory.
+ **Automated:** Schedule a weekly container restart using `cron` during a low-traffic maintenance window.
+ **Root cause:** If heap usage grows steadily, the bot code likely has a memory leak. Common causes include unbounded session caches, event listeners that are never removed, and large message payloads stored in memory. Use the Node.js `--inspect` flag and Chrome DevTools to take heap snapshots and identify the leak.

### Required IAM permissions
<a name="bot-iam-permissions"></a>

The Amazon EC2 instance profile for the bot host requires the following permissions for Amazon CloudWatch monitoring:

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cloudwatch:PutMetricData",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:*:*:log-group:/wickr/bots/*",
                "arn:aws:logs:*:*:log-group:/wickr/bots/*:*"
            ]
        }
    ]
}
```

## Collect bot logs
<a name="bot-logging"></a>

A Wickr IO bot produces logs at multiple levels. Understanding where each log is stored helps you collect the right information when troubleshooting.


| Log | Path inside container | Contents | 
| --- | --- | --- | 
| Docker container log | Access with docker logs | WickrIO console output and container startup messages. Bot integrations do not write to standard output, so docker logs does not contain application-level bot logs. | 
| WickrIO server log | /opt/WickrIO/logs/WickrIOSvr.log | Server process events, client registration, and connection status. Check this log when the container is running but the bot is not connecting. | 
| Integration log (WickrLogger) | /opt/WickrIO/clients/{{bot-name}}/integration/{{bot-name}}/logs/log.output | Application-level logs from your bot code, written by the WickrLogger library. This is the most useful log for debugging bot logic issues. | 

To view the integration log from outside the container:

```
sudo docker exec {{container-name}} \
  cat /opt/WickrIO/clients/{{bot-name}}/integration/{{bot-name}}/logs/log.output
```

To view the WickrIO server log:

```
sudo docker exec {{container-name}} cat /opt/WickrIO/logs/WickrIOSvr.log
```

**View Docker container logs**

```
# View recent logs
sudo docker logs --tail 100 {{container-name}}

# Follow logs in real time
sudo docker logs -f {{container-name}}
```

**Configure integration log settings**

The WickrLogger library reads log settings from the `processes.json` file in your bot's integration directory. Add a `log_tokens` section to configure the log level, maximum file size, and maximum number of rotated log files:

```
{
  "apps": [{
    "name": "{{bot-name}}",
    "script": "src/index.js",
    "env": {
      "tokens": { },
      "log_tokens": {
        "LOG_LEVEL": "debug",
        "LOG_FILE_SIZE": "10m",
        "LOG_MAX_FILES": "5"
      }
    }
  }]
}
```

The defaults are `info` level, 10 MB maximum file size, and 5 rotated files. Set `LOG_LEVEL` to `debug` temporarily when troubleshooting, then revert to `info` for normal operation. For more information, see [Logging API](https://docs.aws.amazon.com/wickr/latest/botguide/logging-api.html) in the *Wickr IO Bot Guide*.

**Note**  
Always revert `LOG_LEVEL` to `info` after troubleshooting. Running at `debug` level in production generates excessive log volume and, on older bot versions, may log sensitive values such as authentication challenge tokens.

**Note**  
When investigating bot crashes, check both the integration log and the Docker container log (`docker logs {{container-name}}`). Crash traces from unhandled exceptions and segmentation faults are written to the container log.

**Configure Docker log rotation**

**Important**  
The default Docker log driver (`json-file`) does not rotate logs. The log file grows without limit until it fills the host's disk, which can cause the bot and other processes on the host to fail. Always configure log rotation for production bots.

Set the `max-size` and `max-file` options when you start the container. For example:

```
sudo docker run -it \
  --restart unless-stopped \
  --log-opt max-size=50m \
  --log-opt max-file=5 \
  {{other-options}} \
  {{image-name}}
```

This configuration keeps up to 5 log files of 50 MB each (250 MB total). To set this as the default for all containers on the host, add the following to `/etc/docker/daemon.json` and restart Docker:

```
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "50m",
    "max-file": "5"
  }
}
```

**Forward logs to Amazon CloudWatch Logs**

For production bots, you can forward container-level logs to Amazon CloudWatch Logs using the Docker `awslogs` log driver. This captures WickrIO server output and container startup messages, which is useful for detecting container crashes and restart loops. To forward bot application logs to Amazon CloudWatch Logs, use the CloudWatch agent on the host to tail the volume-mounted integration log file, or publish metrics directly from your bot code using the heartbeat approach described in [Add a heartbeat metric (recommended)](#monitor-heartbeat).

```
sudo docker run -it \
  --restart unless-stopped \
  --log-driver=awslogs \
  --log-opt awslogs-region={{us-east-1}} \
  --log-opt awslogs-group=/wickr/bots/{{bot-name}} \
  --log-opt awslogs-create-group=true \
  {{other-options}} \
  {{image-name}}
```

The Amazon EC2 instance profile must include the `logs:CreateLogGroup`, `logs:CreateLogStream`, and `logs:PutLogEvents` permissions.

**Note**  
Complete the initial bot setup (the `add` and `start` commands in the WickrIO console) using the default `json-file` driver first. After the bot is running, recreate the container with the `awslogs` driver. Use `docker restart` for subsequent restarts to preserve the registration database.

**Archive logs to Amazon S3**

For compliance or long-term retention, export Amazon CloudWatch Logs data to Amazon S3. You can configure automatic export using a Amazon CloudWatch Logs subscription filter with Amazon Data Firehose, or perform one-time exports from the Amazon CloudWatch console. For more information, see [Export log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html) in the *Amazon CloudWatch Logs User Guide*.

Set a retention policy on the Amazon CloudWatch Logs log group to control costs. For most bot deployments, 30 to 90 days of log retention in Amazon CloudWatch Logs is sufficient for troubleshooting, with older logs archived to Amazon S3.

## Common issues
<a name="troubleshooting-common-issues"></a>

***Exited Docker container ***

Once the Wickr IO container is set up, it is designed to run indefinitely unless stopped manually. However, unexpected events may occur that could cause your running Docker container to exit.

**Solution**
+ Run docker restart (container-name) to get your container back up.
+ Look at Wickr IO client logs to identify the reason for crash. For more information, see [ Wickr IO clients logging](https://docs.aws.amazon.com/wickr/latest/wickrio/logging.html).
+ Check your host’s disk space usage to ensure your host machine has enough disk space to support the clients running within the Wickr IO Docker container.

***Exited Docker container ***

Once you have a running bot client, you should be able to interact(depends on the integration type) with it on Wickr client application. If the bot is not responding as expected see the solution below to debug the issue.

**Solution**
+ Ensure the Wickr IO client is in `Running` state on the Wickr IO docker CLI. You can list all clients and their state using the `list` command.
+ If the client is running, then see the integration logs for any errors. For more information, see [ Wickr IO clients logging](https://docs.aws.amazon.com/wickr/latest/wickrio/logging.html).

***Too many bot devices ***

Bot clients do not automatically remove old devices upon start-up. If you frequently move a bot between different machines, you may reach the limit of 50 devices. Each time you move the bot to a new device or recreate it, a new device entry is created. Once you reach this limit of 50 devices, the bot may stop functioning properly.

**Solution**

Starting from version 5.81, there are multiple ways to clear out old bot devices. To do this, you need to modify the bot's `.ini` file. This is a one-time setting that the bot client will use to eliminate old devices. The setting will specify the number of seconds a bot device has remained logged in. If a device's last login exceeds this specified duration, it will be suspended. For example:

```
[oneshot]
suspenddeviceafterseconds=120
```

In the example, you can set the value to 120 seconds (or two minutes). This setting will NOT affect the current device but will suspend all devices that have not logged in within the specified time frame. The `.ini` file can be found in the client directory associated with the bot client. For example:

`/opt/WickrIO/clients/[botname]/WickrIO[botname].ini`

Restart the bot after you have added this to the `.ini` file.

***Wickr files are not received or transmitted***

If the Wickr IO integration you are using requires sending or receiving files but you're experiencing issues with either, it may be due to an inaccurate date and/or time setting on your system. Wickr's system relies on the host date and time to transfer encrypted files successfully. If these setting are incorrect, file transfers will fail.

**Solution**

For accuracy, it's recommended to install and run an NTP (Network Time Protocol) service on your host system.

***Network timeouts ***

If your bot is failing to interact with the backend servers and the logs indicate time errors, there is a way to increase the timeout for network requests. While this may not resolve the underlying problem, it can help rule out timeout as a cause of connection issues.

**Solution**

To adjust the network timeouts, you'll need to modify the `.ini` file for the bot client. The `/opt/WickrIO/clients/WickrIO.ini` is the appropriate file.

Add the following below to the `.ini` file:

```
[networksetup]
requesttimeout=[some value in seconds]
userrequesttimeout=[some value in seconds]
```

The `.ini` file is located in the client directory associated with the bot client, for example:

`/opt/WickrIO/clients/[botname]/WickrIO[botname].ini`

Restart the bot after you have added this to the `.ini` file.

**Bot doesn't respond to messages**

Possible causes:
+ The bot process has crashed inside the container.
+ The bot lost its connection to the Wickr network.
+ The container is running but the integration was not started.

**Resolution**

1. Check container status: `sudo docker ps -a --filter name={{container-name}}`

1. Check bot logs: `sudo docker logs --tail 50 {{container-name}}`

1. Verify the bot shows as online in the Wickr Admin Console under **Bots**.

1. Restart the container: `sudo docker restart {{container-name}}`

**Failed to create connection to host**

The bot container logs show `Failed to create connection to host` when attempting to reach the Wickr messaging gateway on port 443. The bot cannot connect to the Wickr service and will not come online.

Possible causes:
+ A firewall, security group, or network ACL is blocking outbound TCP port 443 from the bot host.
+ A proxy or web filter is intercepting TLS connections to Wickr domains.
+ DNS resolution is failing for the Wickr messaging gateway domain.
+ The bot is using the wrong Docker image for its deployment type (for example, the commercial image in GovCloud or vice versa).

**Resolution**

1. Verify that the host can resolve and reach the Wickr messaging gateway. Run the following commands from the bot host (not from inside the container):

   ```
   # For commercial deployments:
   nslookup gw-pro-prod.wickr.com
   curl -v https://gw-pro-prod.wickr.com
   
   # For GovCloud deployments:
   nslookup api.messaging.wickr.us-gov-west-1.amazonaws.com
   curl -v https://api.messaging.wickr.us-gov-west-1.amazonaws.com
   ```

   If `nslookup` fails, the host has a DNS resolution issue. If `curl` fails with a connection timeout or reset, a firewall or security group is blocking the traffic.

1. Verify that the Amazon EC2 security group allows outbound TCP port 443. In the Amazon EC2 console, select the instance, choose the **Security** tab, and review the outbound rules for the attached security group.

1. Allowlist the required Wickr domains for your AWS Region. The bot host must be able to reach the messaging gateway domain on TCP port 443. For the full list of domains and IP addresses by Region, see [Ports and domains to allow list for your Wickr network](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html).

1. If the host is behind a corporate proxy or web filter, verify that the proxy is not performing TLS inspection on Wickr traffic. The Wickr IO container requires a direct TLS connection to the messaging gateway. Configure a proxy bypass for the Wickr domains listed in the allowlist.

1. Verify you are using the correct Docker image for your deployment type. Commercial deployments must use `wickrio/bot-cloud:latest`. GovCloud deployments must use `wickrio/bot-cloud-govcloud:latest`. Using the wrong image causes the container to connect to the wrong messaging gateway, which results in a connection failure.

**Container starts but bot process fails**

Possible causes:
+ Missing Node.js dependencies.
+ Incorrect bot credentials.
+ The bot user was removed from the Wickr network.

**Resolution**

1. Check the container logs for error messages.

1. Verify the bot user exists in the Wickr Admin Console.

1. Re-run `npm install` inside the container to restore dependencies.

**Bot was working but stopped after container recreation**

If you removed and recreated the container (using `docker rm` followed by `docker run`) instead of restarting it (using `docker restart`), the WickrIO server's registration database was lost. The container starts, but the WickrIO server does not recognize any registered bot clients.

Symptoms:
+ The WickrIO server log shows `WickrIO Client Server configured` but no connection attempts.
+ The bot process starts but hangs at `Checking for client connection` indefinitely.
+ In interactive mode, the console shows `There are no clients currently configured!`
+ In detached mode (`-d`), the WickrIO server may crash with a segmentation fault (`Segmentation fault (core dumped)` in `docker logs`) and the container enters a restart loop. This occurs because the server attempts to auto-start registered clients in `-notty` mode, but the registration database is empty.

**Resolution**

1. Attach to the container: `sudo docker attach {{container-name}}`

1. Re-register the bot using the `add` command. If auto-login was previously configured and the client data volume is intact, the bot uses the existing auto-login keys.

1. Start the bot with `start 0`.

1. Detach from the container with `Ctrl+P`, `Ctrl+Q`.

To prevent this issue, use `docker restart` instead of `docker rm` and `docker run`. If you must recreate the container (for example, to change the log driver), plan for the re-registration step.

**Important**  
If the container is running in detached mode (`-d`) with `--restart` enabled and the registration database is lost, the WickrIO server repeatedly attempts to re-register on each restart. This can exhaust the Wickr service's registration rate limit, which locks the bot username for 24 hours. Stop the container immediately with `docker stop {{container-name}}` if you see `Segmentation fault` or `Begin register existing user context` repeating in `docker logs`.

**Bot is online but CloudWatch alarms are not working**

Possible causes:
+ The Amazon EC2 instance profile is missing `cloudwatch:PutMetricData` permission.
+ The bot is publishing to a different AWS Region than the alarm.

**Resolution**

1. Verify the instance profile includes `cloudwatch:PutMetricData`.

1. Confirm the `AWS_REGION` environment variable matches the Region where your alarms are configured.

1. Check the CloudWatch console under **Custom namespaces** for the `WickrIO/Bots` namespace to verify metrics are arriving.

**Bot integration does not start after container restart**

The container is running and the WickrIO server shows the bot as `Running`, but the bot does not respond to messages and no integration log is produced.

**Cause:** When the container restarts in detached mode, the WickrIO server starts the Wickr client process but does not automatically launch the Node.js integration. The integration must be started separately.

**Resolution**

1. Start the integration manually inside the container:

   ```
   sudo docker exec -d {{container-name}} bash -c \
     'source /usr/local/nvm/nvm.sh && nvm use 20 >/dev/null && \
      cd /opt/WickrIO/clients/{{bot-name}}/integration/{{bot-name}} && \
      node src/index.js > /tmp/bot.log 2>&1'
   ```

1. Verify the integration is running by checking for the Node.js process and the integration log:

   ```
   sudo docker exec {{container-name}} pgrep -a node
   sudo docker exec {{container-name}} tail /tmp/bot.log
   ```

**Note**  
The `name` field in your bot's `package.json` must match the registered bot username. The WickrIO SDK uses this value to determine the IPC socket path for communicating with the Wickr client process. If the names do not match, the integration starts but cannot connect to the client.

**Integration import fails with "install shell file does not exist"**

When importing a custom integration during the `add` command, the WickrIO console reports `install shell file does not exist for this software!` and the import fails.

**Cause:** The `software.tar.gz` file does not contain an `install.sh` script. The WickrIO import process requires this script to install the integration dependencies.

**Resolution:** Add an `install.sh` script to the root of your `software.tar.gz` archive:

```
#!/bin/bash
cd "$(dirname "$0")"
npm install --production
```

Rebuild the archive with the script included:

```
tar czf software.tar.gz src/ package.json install.sh
```

## Upgrading bots
<a name="upgrading-bots"></a>

The WickrIO bots do not automatically upgrade, like a Wickr client does. You will need to periodically and manually upgrade the bots to make sure you have the latest software.

**Solution**

The following are the steps you will perform to upgrade a WickrIO docker image and the associated bots:

1. Pause the bots that are running on the WickrIO docker container. This is a safety precaution to make sure there are no database corruption problems when you upgrade the container. You will log into the WickrIO CLI and perform the 'pause' command for each bot you have running. After pausing the bots, exit out of the WickrIO CLI (using the <ctrl>p <ctrl>q keyboard sequence).

1. Next, you will kill the current docker container. The following commands will kill the running container and remove it. Notice we named our bot 'MyBotName', you may have named it differently. If you ran the docker container with the appropriate "-v" option your bot data will be safe. The following is an example command:

   ```
   docker kill MyBotName
   docker rm -f MyBotName
   ```

1. Next, you will start the docker container with the new version and use the same options you used to start the old version. The following is an example command:

   ```
   docker run -v /opt/MyBotName:/opt/WickrIO -p 4001:4001 -d --restart=always --name="MyBotName" -ti wickr/bot-cloud:latest
   ```

1. Next, you will upgrade the bots running on this container. You will need to do that for each of the bots on this container. Log onto the WickrIO CLI, and perform the 'list' command, which will show you the list of bots and identify which ones need to be upgraded. Depending on how old your version is, it is likely all of your bots will require upgrading.

1. Next, for each bot perform the "upgrade" command. It is possible that the configuration tokens associated with the bot integration has changed, if so you will be prompted for the new values.

1. After ensuring all the bots have been upgraded, start each bot. When done starting you can perform the "list" command to verify each bot is running. Once verified, you can exit out of the WickrIO CLI.

The following is sample output from upgrading an old WickrIO bot running version v4.64.9.3, with a wickrio\_web\_interface bot. The version being upgraded to is the 5.116.18.01 version/tag.

```
Enter command:list
Current list of clients:
 client[0] old-test-bot, State=Running, Integration=wickrio_web_interface
Enter command:version
version: v4.64.9.3
Enter command:pause 0
Do you really want to pause the client with the name old-test-bot (default: yes):yes
Enter command:list
Current list of clients:
 client[0] old-test-bot, State=Paused, Integration=wickrio_web_interface
Enter command:read escape sequence
ubuntu@mybothost:~$ 
docker kill VeryOldBot
ubuntu@mybothost:~$ 
docker rm -f VeryOldBot
ubuntu@mybothost:~$ 
docker run -v /opt/VeryOldBot/WickrIO:/opt/WickrIO -p 4444:4444 -d --restart=always --name="VeryOldBot" -ti wickr/bot-cloud:latest
Unable to find image 'wickr/bot-cloud:latest' locally
5.116.18.01: Pulling from wickr/bot-cloud
4bbfd2c87b75: Already exists 
d2e110be24e1: Already exists 
889a7173dcfe: Already exists 
20ca454721b1: Already exists 
02c4b05cb492: Already exists 
1c731f8c023d: Already exists 
fcd34fc70cfe: Already exists 
b1fceb668295: Already exists 
68307b81514b: Pull complete 
b9f674e60307: Pull complete 
e4fd99322c5a: Pull complete 
3fdf8c473cd1: Pull complete 
9dd71d5d554c: Pull complete 
225a5f4a7590: Pull complete 
Digest: sha256:05f7d0df8a488f7e325845423d13ebda95b1967b7b00203fe2425ae35e43480f
Status: Downloaded newer image for wickr/bot-cloud:latest
71bb0c85bc4c4c92db604136ad9f64e62d9769debcfccb656794037b4dc06d44
ubuntu@mybothost:~$ docker attach VeryOldBot 

Updating integration software version numbers
Updating integration software version numbers
Searching NPM registry
Searching NPM registry

Welcome to the WickrIO Console program (v5.116.18.01)

Current list of clients:
#  Name          Status  Integration            Version  Events  Misc
======================================================================
0  old-test-bot  Paused  wickrio_web_interface  1.1.2    2       Needs Upgrade!
Enter command:
Enter command:upgrade 0
Upgrading from version 1.1.2 to version 5.82.2
Okay to proceed? (default: yes):yes
Copying wickrio_web_interface software

Upgrading wickrio_web_interface software
Installing wickrio_web_interface software
Installing
Installing
Begin configuration of wickrio_web_interface software for old-test-bot
Now using node v12.20.2 (npm v6.14.11)
adminsOptional=false
adminsOptional=false
Finished Configuring package!
Finished Configuring forever!
Finished Configuring!
Enter command:list
Current list of clients:
#  Name          Status  Integration            Version  Events  Misc
======================================================================
0  old-test-bot  Paused  wickrio_web_interface  5.82.2   2       
Enter command:start 0
Preparing to start the client with the name old-test-bot
Do you really want to start the client with the name old-test-bot:yes
Enter command:list
Current list of clients:
#  Name          Status   Integration            Version  Events  Misc
=======================================================================
0  old-test-bot  Running  wickrio_web_interface  5.82.2   3       
Enter command:
```

## Improve bot resilience
<a name="bot-resilience"></a>

A Wickr IO bot running on a single Amazon EC2 instance is a single point of failure. If the instance fails, the bot is offline until you manually intervene. The following practices improve bot availability for production deployments.

**Persist container state across restarts**

The Wickr IO container stores critical state in two locations that you must mount as Docker volumes to persist across container restarts:
+ **Client data** (`/opt/WickrIO/clients/{{bot-name}}/client/`) – Contains the bot's encryption keys, auto-login credentials, and message database.
+ **Integration code** (`/opt/WickrIO/clients/{{bot-name}}/integration/`) – Contains your bot's source code, `package.json`, and configuration files.

**Important**  
The WickrIO server process maintains a registration database (`wickrbot.database.sqlite`) inside the container at `/opt/WickrIO/`. This database records which bot clients are registered. If you recreate the container (by running `docker rm` followed by `docker run`), this database is lost and the bot must be re-registered through the interactive console using the `add` command. To avoid this, use `docker restart` instead of removing and recreating the container.

The following example shows the recommended volume mounts:

```
sudo docker run -it \
  --name {{bot-name}} \
  --restart unless-stopped \
  -e PRODUCT_TYPE={{govcloud}} \
  -v /opt/wickr-bot:/opt/WickrIO/clients/{{bot-name}}/integration \
  -v /opt/wickr-bot-client:/opt/WickrIO/clients/{{bot-name}}/client \
  {{image-name}}
```

**Enable automatic instance recovery**

Amazon EC2 simplified automatic recovery is enabled by default on supported instance types. If the underlying hardware fails, AWS automatically migrates the instance to healthy hardware. The instance retains its ID, IP addresses, and attached EBS volumes. For more information, see [Automatic instance recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) in the *Amazon EC2 User Guide*.

**Automate bot recovery with health checks**

The Docker `--restart unless-stopped` policy restarts the container when it exits, but it does not detect cases where the container is running while the bot process inside it has stopped responding. To detect and recover from these silent failures, add a Docker health check.

Create a health check script in your bot's integration directory that verifies the bot process is running and producing logs. For example:

```
#!/bin/bash
# healthcheck.sh — exit 0 = healthy, exit 1 = unhealthy

# Check that the Node.js bot process is running
pgrep -f "node {{entry-point}}" > /dev/null || exit 1

# Check that the bot has produced a log entry in the last 5 minutes
LOG="/opt/WickrIO/clients/{{bot-name}}/integration/{{bot-name}}/logs/log.output"
if [ -f "$LOG" ]; then
  LAST_MOD=$(stat -c %Y "$LOG" 2>/dev/null || stat -f %m "$LOG" 2>/dev/null)
  NOW=$(date +%s)
  DIFF=$(( NOW - LAST_MOD ))
  [ "$DIFF" -gt 300 ] && exit 1
fi

exit 0
```

Start the container with the health check configured. For example:

```
sudo docker run -it \
  --restart unless-stopped \
  --health-cmd="/opt/WickrIO/clients/{{bot-name}}/integration/healthcheck.sh" \
  --health-interval=60s \
  --health-retries=3 \
  --health-start-period=120s \
  {{other-options}} \
  {{image-name}}
```

The `--health-start-period` gives the bot time to authenticate with the Wickr network before health checks begin. After the start period, Docker runs the health check every 60 seconds. If 3 consecutive checks fail, Docker marks the container as `unhealthy`.

**Note**  
The Docker `--restart` policy does not automatically restart unhealthy containers. Add a watchdog script on the host to trigger a restart:

```
#!/bin/bash
# /opt/wickr-bot/watchdog.sh — run via cron every 2 minutes
CONTAINER="{{container-name}}"
HEALTH=$(docker inspect --format='{{.State.Health.Status}}' "$CONTAINER" 2>/dev/null)

if [ "$HEALTH" = "unhealthy" ]; then
  logger "Wickr bot $CONTAINER is unhealthy — restarting"
  docker restart "$CONTAINER"
fi
```

```
*/2 * * * * /opt/wickr-bot/watchdog.sh
```

Using `docker restart` preserves the WickrIO registration database and container logs.

**Use an Auto Scaling group**

An Auto Scaling group with a minimum, maximum, and desired capacity of 1 automatically replaces the instance if it fails a health check. Store your bot's client data and integration code on a separate Amazon EBS volume or Amazon EFS file system so the replacement instance can mount the same data and resume without re-registering the bot. For more information, see the [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/).

**Use a container orchestrator**

If your organization already uses a container orchestrator such as Amazon ECS, Amazon EKS, or a lightweight Kubernetes distribution, you can run the Wickr IO container as a managed task or pod with built-in health checks, automatic restarts, and log collection. This approach is recommended only if you already have orchestration infrastructure in place.