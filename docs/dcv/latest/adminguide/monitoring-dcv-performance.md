# Monitoring Amazon DCV Performance and Statistics

Starting with Amazon DCV 2023.1 server, you can use Windows Performance Counters to monitor various aspects of the protocol performance and
collect the statistics about the Amazon DCV sessions and connections.

Tools to Collect Performance Counters:

- [Performance Monitor (PerfMon):](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/perfmon "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/perfmon")
  A Windows-native tool that lets you visualize performance data in real-time or from log files.
- [LogMan:](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/logman "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/logman")
  A command-line tool that can start and stop logging based on specified criteria.
- [TypePerf:](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/typeperf "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/typeperf")
  A command-line tool that writes performance data to the command window or to a log file.
- [PowerShell:](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-counter "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-counter")
  Windows scripting language, which can be used to gather and manipulate performance data.
- Third-party tools: There are several third-party monitoring solutions available that can gather these counters and provide in-depth insights.

## Amazon DCV Performance counter sets

Performance counters are metrics that provide insight into the behavior and utilization of Amazon DCV. By gathering and analyzing performance
counter data over time, you can identify performance bottlenecks, optimize resource usage, debug issues, and gain a deeper understanding of
how Amazon DCV works for you.

DCV Performance counters are grouped in six counter sets:

- [Amazon DCV server](dcv-server.md "dcv-server.md")
- [Amazon DCV server processes](dcv-server-processes.md "dcv-server-processes.md")
- [Amazon DCV server sessions](dcv-server-sessions.md "dcv-server-sessions.md")
- [Amazon DCV server connections](dcv-server-connections.md "dcv-server-connections.md")
- [Amazon DCV server channels](dcv-server-channels.md "dcv-server-channels.md")
- [Amazon DCV server imaging](dcv-server-imaging.md "dcv-server-imaging.md")
