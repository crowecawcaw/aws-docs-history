# GAMEPERF04-BP01 Monitor game server processes to detect

issues

You might run multiple game server processes per instance to
efficiently utilize the resources on your game server instances.
If so, design your architecture so that an individual game server
process hosting a game session cannot cause adverse impact to
other game sessions hosted on the same instance. Use metrics to
understand how game placement and game mode type can impact the
performance of game server instances. Incorporate a mix of low
load (lobby, shop, or single player tutorial) and high load
(ranked, multi-player, or high skill gameplay) processes to avoid
hot spotting the game server instance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Monitor the player experience through client side and server-side
metrics by collecting telemetry for ping time and jitter, frame
drops, API response time, errors and successful game loop
completion. Correlate time stamps for these events with player
support issues and server logs to identify performance
bottlenecks. Tools like
[Dtrace](https://en.wikipedia.org/wiki/DTrace "https://en.wikipedia.org/wiki/DTrace"),
[ftrace](https://en.wikipedia.org/wiki/Ftrace "https://en.wikipedia.org/wiki/Ftrace"),
[uperf](https://uperf.org "https://uperf.org"), and
[eBPF](https://www.brendangregg.com/ebpf.html "https://www.brendangregg.com/ebpf.html")
can be used for deep investigation and analysis of system
performance.

Implement monitoring of the limited resources available to your
game server instances so that you can generate alerts when
individual game server processes are breaching pre-determined
resource budget thresholds. When thresholds are breached, you may
want to configure your game server software to dump relevant
system and game server logs out to durable storage, such as a
central logging solution, so that your game server engineers can
investigate this behavior. Additionally, your game server instance
should be configured to report metrics from each of the game
server processes running on the instance so that you can monitor
these individual game server processes in addition to the overall
metrics for the game server instance.

For example, GameLift provides metrics for
[monitoring
game sessions](../../../gamelift/latest/developerguide/monitoring-cloudwatch.md "../../../gamelift/latest/developerguide/monitoring-cloudwatch.md"), which can be augmented with custom
game-specific metrics and logs collected using the
[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")
[Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")
which you can configure on your game server instance. Your metrics
can be viewed in CloudWatch or exported to other tools such as
[Amazon Managed Grafana](https://aws.amazon.com/grafana/ "https://aws.amazon.com/grafana/") which is integrated with Single Sign-On to make it
straightforward to access metrics by users who may not have access
to the Management Console. Refer to the following best practices
for
[managing
logs and metrics using Amazon GameLift](../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_metrics.md "../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_metrics.md"), which also provides
support for viewing individual
[game
session logs](../../../gamelift/latest/apireference/API_GetGameSessionLogUrl.md "../../../gamelift/latest/apireference/API_GetGameSessionLogUrl.md").

### Implementation steps

- Run multiple game server processes per instance and mix low
  and high-load game modes to avoid hot spotting and verify
  balanced resource utilization.
- Monitor client-side and server-side metrics like ping,
  jitter, frame drops, and API response times, and correlate
  these with server logs and issues reported by players to
  identify bottlenecks.
- Configure resource monitoring for each game server process,
  generate alerts for threshold breaches, and store logs in
  durable storage for analysis using tools like CloudWatch and
  Amazon Managed Grafana.
