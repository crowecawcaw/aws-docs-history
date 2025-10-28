# Detect Lightsail instance

bursting for optimal performance

Amazon Lightsail instances provide a baseline amount of CPU performance, but also have the
ability to temporarily provide additional CPU performance above the baseline as needed. This is
referred to as bursting. The baseline performance and ability to burst are governed by the
following instance metrics:

- **CPU utilization** – The percentage of allocated compute
  units that are in use on your instance. This metric identifies the processing power used to
  run applications on your instance.
- **CPU burst capacity percentage** – The percentage of CPU
  performance available to your instance.
- **CPU burst capacity minutes** – The amount of time
  available for your instance to burst at 100% CPU utilization.
  With the following topics, you will learn how to monitor these metrics to maximize the
  availability of your instance.

###### Topics

- [CPU performance](baseline-cpu-performance.md "baseline-cpu-performance.md")
- [Burst capacity accrual](cpu-burst-capacity-accrual.md "cpu-burst-capacity-accrual.md")
- [Identify instance bursts](identifying-instance-burst.md "identifying-instance-burst.md")
- [Monitor burst capacity](monitoring-cpu-burst-capacity.md "monitoring-cpu-burst-capacity.md")
- [View burst capacity](viewing-instance-burst-capacity.md "viewing-instance-burst-capacity.md")
- [Troubleshoot high CPU](troubleshooting-high-cpu-utilization.md "troubleshooting-high-cpu-utilization.md")
