

# Manage Multi-Session Fleet Instances
<a name="manage-multi-session-instances"></a>

When running multi-session fleets on Amazon WorkSpaces Applications, multiple user sessions share a fleet instance. Unlike single-session fleets — where each instance serves one user and is automatically recycled after the session is terminated — multi-session instances can remain active for extended periods as long as users continue to occupy sessions on them.

This creates an important operational consideration: a multi-session instance cannot be terminated while active user sessions are running. If an instance is never fully vacated, it may never be reclaimed or rebooted, which means:
+ **Image updates may not propagate** — new image versions containing patches, software updates, or security fixes will not reach an instance until all sessions on it have ended and the instance is recycled.
+ **Fleet hygiene is harder to maintain** — without a mechanism to gracefully cycle instances, administrators must manually restart fleets or terminate all active sessions to apply updates, which can be disruptive to end users.
+ **Long-running instances may experience performance degradation** — instances that remain active for extended periods without a restart can accumulate resource contention, memory pressure, and other system-level issues over time, leading to a degraded experience for end users sharing that instance.

To address this, WorkSpaces Applications provides a method to manage the lifecycle of individual fleet instances through a process called draining (also referred to as Drain Mode).

Putting an instance in Drain Mode impacts the capacity of the fleet. The fleet capacity metrics are available at [Viewing Fleet Usage Using the Console](monitoring-console.md).