

# Replication bandwidth requirements
<a name="comm-bandwidth-planning"></a>

AWS Elastic Disaster Recovery replicates data changes from your source servers to AWS over TCP port 1500. The required network bandwidth must exceed the combined write throughput of all source servers that replicate through the same network path. If your available bandwidth is lower than the total write rate, replication can't keep up and data won't converge.

**Topics**
+ [Calculating required bandwidth](#Calculating-Bandwidth)
+ [Measuring source server write speed](#comm-bandwidth-measure)
+ [Testing available bandwidth](#comm-bandwidth-test)

## Calculating required bandwidth
<a name="Calculating-Bandwidth"></a>

Use the following formula to determine the minimum bandwidth you need:

```
Minimum bandwidth >= sum of average write speed of all source servers
```

For example, if you replicate two source servers through the same network path and their average write speeds are 5 MBps and 7 MBps, you need at least 12 MBps of available bandwidth.

**Note**  
We recommend adding at least 20% headroom to account for burst writes. If available bandwidth is insufficient, replication lag increases and convergence might fail.

## Measuring source server write speed
<a name="comm-bandwidth-measure"></a>

To determine the write speed of each source server, use the following operating system-specific tools. We recommend collecting data for at least 24 hours to capture both peak and average write patterns.

------
#### [ Linux ]

Use `iostat` from the `sysstat` package to measure disk write speed.

Install `sysstat`:

```
$ sudo yum install sysstat
```

On Debian or Ubuntu, run the following command instead:

```
$ sudo apt-get install sysstat
```

Run `iostat` with extended statistics, reporting every 3 seconds:

```
$ iostat -x 3
```

In the output, look at the `wkB/s` column (write kilobytes per second) for each disk. The following example shows sample output:

```
Device         rrqm/s wrqm/s   r/s    w/s   rkB/s    wkB/s  %util
sda              0.00   5.00  1.00  15.00   4.00   5120.00  12.50
sdb              0.00   2.00  0.00  10.00   0.00   3072.00   8.00
```

In this example, `sda` writes at 5,120 KB/s (5 MBps) and `sdb` writes at 3,072 KB/s (3 MBps).

------
#### [ Windows ]

Use Performance Monitor (`perfmon`) to measure disk write speed.

**To measure write speed with Performance Monitor**

1. Open Performance Monitor.

1. Add the counter **PhysicalDisk** > **Disk Write Bytes/sec** for all disk instances.

1. Monitor for at least 24 hours to identify peak write patterns.

Alternatively, use the following PowerShell command to collect write speed samples:

```
Get-Counter '\PhysicalDisk(*)\Disk Write Bytes/sec' -SampleInterval 3 -MaxSamples 10
```

------

## Testing available bandwidth
<a name="comm-bandwidth-test"></a>

If replication is not converging, verify that your actual network throughput matches or exceeds the calculated requirement. For instructions on running a bandwidth test between your source network and AWS, see the [network bandwidth test](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test).