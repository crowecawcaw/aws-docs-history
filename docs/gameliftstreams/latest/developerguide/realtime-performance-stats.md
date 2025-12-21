# Real-time performance stats

Amazon GameLift Streams collects performance stats during active stream sessions, measuring resource utilization every second. Use these stats to monitor your application's performance, identify resource bottlenecks, and optimize your streaming experience.

Performance stats include both application-level stats (CPU and memory utilization for your specific application) and system-level stats (CPU, memory, GPU, and VRAM utilization for the shared compute infrastructure).

You can receive performance stats in two ways:

- **In real-time during the session:** Use the Amazon GameLift Streams Web SDK to receive stats as they're collected. This enables you to build performance overlays and monitor resource utilization as you interact with the application.
- **Post-session as a CSV file:** When you export session files, the stats are included as `stats/perf_stats_v1.csv`. This provides a complete record for post-session analysis and debugging.

## Receive performance stats

### Receive stats in real-time

To receive performance stats in your client application during an active session, set the `SharedWithClient` parameter to `true` when calling the `StartStreamSession` API. The Amazon GameLift Streams Web SDK provides a `performanceStats` callback that triggers whenever new stats arrive from the streaming session.

###### Warning

Do not enable `SharedWithClient` for production sessions with end users. Enable it only when the client is trusted, such as for internal debugging and testing.

When initializing the Amazon GameLift Streams Web SDK, set `clientConnection.performanceStats` to a callback function that will receive performance stats.

```
const gls = new gameliftstreams.GameLiftStreams({
    videoElement: document.getElementById('streamVideoElement'),
    audioElement: document.getElementById('streamAudioElement'),
    inputConfiguration: {
        ...
    },
    clientConnection: {
        ...
        performanceStats: (perfStats) => {
            // Your callback logic here
            console.log('CPU: ' + perfStats.application.cpuNormalized);
            console.log('Memory: ' + perfStats.application.memoryMB + ' MB');
            console.log('GPU: ' + perfStats.system.gpuPercent + '%');
        },
    }
});
```

The callback receives a `PerformanceStats` object containing both application-level and system-level stats. For details on the interface structure, see the Amazon GameLift Streams Web SDK documentation on the [Getting Started product page](https://aws.amazon.com/gamelift/streams/getting-started/ "https://aws.amazon.com/gamelift/streams/getting-started/").

The Amazon GameLift Streams console also includes a built-in performance overlay when using the test stream feature, allowing you to monitor stats in real-time without any implementation work.

You can combine performance stats with WebRTC stats provided by the `getVideoRTCStats()` and `getAudioRTCStats()` functions in the Amazon GameLift Streams Web SDK. This combination provides a complete picture of streaming performance, including network stats, client frame rate, and resource utilization.

### Receive stats post-session

Amazon GameLift Streams automatically collects performance stats during every stream session. When you export session files, the stats are included as `stats/perf_stats_v1.csv` in the exported ZIP file. This provides a complete record of all stats collected during the session for post-session analysis and debugging.

For more information about exporting session files, see [Export stream session files](stream-sessions-export-files.md "stream-sessions-export-files.md").

## Performance stats reference

The following table lists all performance stats collected by Amazon GameLift Streams. Application stats are specific to the current session, while shared system stats reflect the total utilization of the shared compute by sessions on multi-tenant stream classes.

###### Normalized stats on multi-tenant stream classes

Amazon GameLift Streams supports multi-tenant stream classes where multiple sessions may share the same compute instance. Normalized stats (application CPU and memory utilization) measure your application's resource usage relative to its allocated fair share. The fair share is calculated by dividing the total available CPU and memory on the compute instance evenly based on the stream class tenancy.

A value of 1.0 means your application is using exactly its fair share allocation. Values below 1.0 indicate you're using less than your allocation. Values exceeding 1.0 indicate overutilization, which may lead to performance degradation for your session. On multi-tenant stream classes (tenancy greater than 1), overutilization may also impact other sessions sharing the same compute instance.

The stat names listed in the following table are used as CSV column headers in the exported file. When receiving stats in real-time via the Amazon GameLift Streams Web SDK, these stats are available through the `PerformanceStats` interface with property names in camel case. For the exact interface structure and property names, see the Amazon GameLift Streams Web SDK API reference guide on the [Getting Started product page](https://aws.amazon.com/gamelift/streams/getting-started/ "https://aws.amazon.com/gamelift/streams/getting-started/").

| Stat name (CSV column) | Description                                                                                                                                                                                               | Scope         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `timestamp`            | Time when the measurement was taken, in ISO 8601 format.                                                                                                                                                  | All           |
| `app_cpu_normalized`   | Application's CPU usage normalized against the fair share allocation, where 1.0 represents the target fair share limit. Usage over 1.0 indicates overutilization, which may lead to performance issues    | Application   |
| `app_mem_mb`           | Total memory (RAM) used by the application (measured in MiB)                                                                                                                                              | Application   |
| `app_mem_normalized`   | Application's memory usage normalized against the fair share allocation, where 1.0 represents the target fair share limit. Usage over 1.0 indicates overutilization, which may lead to performance issues | Application   |
| `shared_sys_cpu_pct`   | Percentage of total CPU usage across the shared compute.                                                                                                                                                  | Shared System |
| `shared_sys_mem_mb`    | Total memory used on the instance (measured in MiB).                                                                                                                                                      | Shared System |
| `shared_sys_mem_pct`   | Percentage of total memory in use across the shared compute.                                                                                                                                              | Shared System |
| `shared_sys_gpu_pct`   | Percentage of total GPU utilization across the shared compute.                                                                                                                                            | Shared System |
| `shared_sys_vram_mb`   | Total VRAM (GPU memory) used on the shared compute (measured in MiB).                                                                                                                                     | Shared System |
| `shared_sys_vram_pct`  | Percentage of total VRAM (GPU memory) in use across the shared compute.                                                                                                                                   | Shared System |
