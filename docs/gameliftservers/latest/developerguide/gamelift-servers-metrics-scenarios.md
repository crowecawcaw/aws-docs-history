# Common monitoring scenarios

## Dive deep performance investigation

**Scenario:** A host/instance is having degraded performance due to specific processes or game sessions

**Investigation steps:**

- Access the Instance Performance dashboard.
- Review "Top N Memory Consuming Game Sessions" table to identify which processes contribute the most to instance memory consumption.
- Review "Top N CPU Consuming Game Sessions" table to identify which processes contribute the most to instance CPU utilization.
- Click on Game Session links to enable deeper investigation of detailed metrics.
- Analyze server timings (Server Delta Time, Server Tick Rate, Server Tick Time, Server World Tick Time) to identify performance bottlenecks.

## Game server crash investigation

**Scenario:** A game session has crashed and you need to determine the root cause

**Investigation steps:**

- Access the Server Performance dashboard for the crashed game session.
- Check Memory Usage (Units) and Physical Memory Usage (%) to determine if the crash was due to out of memory.
- Review CPU Usage (%) to identify if CPU overload caused the crash.
- Analyze Network I/O (Bytes) and Network I/O (Packets) to determine if network bandwidth problems contributed to the crash.
- Examine Packet Loss percentage to identify network-related issues.

## Investigate player reported issues

**Scenario:** Players report lag or interruption during gameplay

**Investigation steps:**

- Access the Server Performance dashboard for the affected game session.
- Review Server Tick Time and Server World Tick Time to identify delays in game updates.
- Check Server Tick Rate to ensure consistent server update frequency.
- Analyze CPU Usage (%) to identify processing bottlenecks.
- Review Memory Usage metrics to identify memory-related performance issues.
- Check Network I/O metrics and Packet Loss to identify network bottlenecks.

## Identify performance changes in different game server builds

**Scenario:** You want to measure how game performance changes across different server builds

**Investigation steps:**

- Compare Server Tick Time metrics between different builds to measure processing efficiency changes.
- Analyze Server Tick Rate consistency across builds to identify performance regressions.
- Review Server World Tick Time to measure game world update performance changes.
- Compare Memory Usage patterns between builds to identify memory optimization improvements or regressions.
- Monitor CPU Usage trends to assess computational efficiency changes.

## Detect delays and slowness in gameplay

**Scenario:** You need to monitor server responsiveness and game update speed

**Investigation steps:**

- Monitor Server Tick Time to measure how fast the server processes each update cycle.
- Track Server Tick Rate to ensure consistent game state updates per second.
- Analyze Server World Tick Time to measure game world update speed, which directly impacts customer experience.
- Set up alerts for Server Delta Time variations to detect inconsistent server performance.

## Benchmarking different game scenarios

**Scenario:** You want to identify how different game scenarios affect server performance

**Investigation steps:**

- Compare server performance metrics across different player counts to understand scaling impact.
- Analyze performance differences between game modes using Server Tick Time and CPU Usage metrics.
- Monitor Memory Usage patterns across different game scenarios to identify resource-intensive features.
- Track Network I/O metrics to understand bandwidth requirements for different gameplay scenarios.
- Use the Instance Performance dashboard to identify which game scenarios produce the highest resource-consuming game sessions.

## High resource utilization response

**Scenario:** Unusual resource spikes (CPU >85%, Memory >90%)

**Investigation steps:**

### Identify affected resources

- Use DescribeGameSessionDetails API.
- Filter by Status if needed.
- Document affected instances.

### Analyze resource usage

- Review Instance Overview dashboard.
- Compare utilization across fleet.
- Check historical patterns.

### Monitor game server impact

- Check Server Performance metrics.
- Review tick times and packet loss.
- Monitor memory leaks.

### Resolution steps

- Download session logs.
- Address build issues.
- Monitor improvements.

## Game server crash analysis

**Scenario:** Multiple error-status game sessions across fleet

**Investigation steps:**

### Initial assessment

- Access Fleet Overview dashboard.
- Review crashed session table.
- Note patterns in timing/location.

### Performance analysis

- Check server timing metrics.
- Review resource utilization.
- Monitor network performance.

### Infrastructure review

- Verify fleet capacity.
- Check instance health.
- Review scaling policies.

### Resolution path

- Analyze server logs.
- Review code optimization.
- Implement fixes.

## Fleet capacity optimization

**Scenario:** Game launch or benchmark study

**Analysis steps:**

### Resource utilization

- Filter by location.
- Review P50/P95/P99 metrics.
- Analyze usage patterns.

### Instance type analysis

- Compare performance by type.
- Identify scaling candidates.
- Document utilization patterns.

### Optimization actions

- Adjust scaling policies.
- Modify instance types.
- Update fleet configuration.
