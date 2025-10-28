# System bandwidth

System bandwidth is the rate at which network and data traffic moves
between process on each core, and between those cores and memory.

## Impact of system

bandwidth issues

Typically, system bandwidth rates don't create performance problems on
Elemental Live appliances.

One of the ways that you know there are memory bandwidth problems on
the appliance is through error messages in the logs. For more information,
see [Assessing performance with logging messages](performance-via-logs.md "performance-via-logs.md").

If you suspect that system bandwidth is causing these problems, reduce
density on the appliance.

## Measuring system

bandwidth

The `amd_bandwidth` utility is included in Elemental Live
versions 2.18.6 and later.

It shows the outbound bandwidth for each socket on the appliance. For
example:

```
$ sudo amd_bandwidth
Collecting bandwidth data for 10 seconds...
Socket0 bandwidth: 7.43645 GB/s
Socket1 bandwidth: 19.0827 GB/s
```

## Expected rates

The following guidelines apply for system bandwidth:

- Single-socket L8xx appliances have a maximum bandwidth of 90
  GBps
- Dual-socket L8xx appliances have a maximum bandwidth of 140
  GBps
