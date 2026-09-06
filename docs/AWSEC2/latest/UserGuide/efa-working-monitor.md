

# Monitor an Elastic Fabric Adapter on Amazon EC2
<a name="efa-working-monitor"></a>

You can use the following features to monitor the performance of your Elastic Fabric Adapters.

**Topics**
+ [EFA driver metrics for an Amazon EC2 instance](#efa-driver-metrics)
+ [Amazon VPC flow logs](#efa-flowlog)
+ [Amazon CloudWatch](#efa-cloudwatch)

## EFA driver metrics for an Amazon EC2 instance
<a name="efa-driver-metrics"></a>

The Elastic Fabric Adapter (EFA) driver publishes multiple metrics from the instances that have EFA interfaces attached, in real time. You can use these metrics to troubleshoot application performance and networking issues, choose the right cluster size for a workload, plan scaling activities proactively, and benchmark applications to determine whether they maximize the EFA performance available on an instance.

**Topics**
+ [Available EFA driver metrics](#available-efa-metrics)
+ [Retrieve EFA driver metrics for your instance](#view-efa-driver-metrics)

### Available EFA driver metrics
<a name="available-efa-metrics"></a>

The EFA driver publishes the following metrics to the instance in real time. They provide the cumulative number of errors, connection events, and packets or bytes sent, received, retransmitted, or dropped by the attached EFA devices since instance launch or the last driver reset.


| Metric | Description | Supported instance types | 
| --- | --- | --- | 
| tx\_bytes | The number of bytes transmitted.<br />Unit: bytes | All instance types that support EFA | 
| rx\_bytes | The number of bytes received.<br />Unit: bytes | All instance types that support EFA | 
| tx\_pkts | The number of packets transmitted.<br />Unit: count | All instance types that support EFA | 
| rx\_pkts | The number of packets received.<br />Unit: count | All instance types that support EFA | 
| rx\_drops | The number of packets that were received and then dropped.<br />Unit: count | All instance types that support EFA | 
| send\_bytes | The number of bytes sent using send operations.<br />Unit: bytes | All instance types that support EFA | 
| recv\_bytes | The number of bytes received by send operations.<br />Unit: bytes | All instance types that support EFA | 
| send\_wrs | The number of packets sent using send operations.<br />Unit: count | All instance types that support EFA | 
| recv\_wrs | The number of packets received by send operations.<br />Unit: count | All instance types that support EFA | 
| rdma\_write\_wrs | The number of completed rdma write operations.<br />Unit: count | All instance types that support EFA | 
| rdma\_read\_wrs | The number of completed rdma read operations.<br />Unit: count | All instance types that support EFA | 
| rdma\_write\_bytes | The number of bytes written to it by other instances using rdma write operations.<br />Unit: bytes | All instance types that support EFA | 
| rdma\_read\_bytes | The number of bytes received using rdma read operations.<br />Unit: bytes | All instance types that support EFA | 
| rdma\_write\_wr\_err | The number of rdma write operations that had local or remote errors.<br />Unit: count | All instance types that support EFA | 
| rdma\_read\_wr\_err | The number of rdma read operations that had local or remote errors.<br />Unit: count | All instance types that support EFA | 
| rdma\_read\_resp\_bytes | The number of bytes sent in response to rdma read operations.<br />Unit: bytes | All instance types that support EFA | 
| rdma\_write\_recv\_bytes | The number of bytes received by rdma write operations.<br />Unit: bytes | All instance types that support EFA | 
| retrans\_bytes | The number of EFA SRD bytes retransmitted.<br />Unit: count | Nitro v4 and later instance types that support EFA | 
| retrans\_pkts | The number of EFA SRD packets retransmitted.<br />Unit: bytes | Nitro v4 and later instance types that support EFA | 
| retrans\_timeout\_events | The number of times EFA SRD traffic timed out and resulted in a network path change.<br />Unit: count | Nitro v4 and later instance types that support EFA | 
| impaired\_remote\_conn\_events | The number of times EFA SRD connections entered an impaired state, resulting in a reduced throughput rate limit.<br />Unit: count | Nitro v4 and later instance types that support EFA | 
| unresponsive\_remote\_events | The number of times an EFA SRD remote connection was unresponsive.<br />Unit: count | Nitro v4 and later instance types that support EFA | 

For more information about the instance types that support EFA, see [Supported instance types](efa.md#efa-instance-types).

### Retrieve EFA driver metrics for your instance
<a name="view-efa-driver-metrics"></a>

You can use the [rdma-tool](https://man7.org/linux/man-pages/man8/rdma.8.html) command line tool to retrieve the metrics for all EFA interfaces attached to an instance as follows:

```
$ rdma -p statistic show
link rdmap0s31/1 
    tx_bytes 0 
    tx_pkts 0 
    rx_bytes 0 
    rx_pkts 0 
    rx_drops 0 
    send_bytes 0 
    send_wrs 0 
    recv_bytes 0 
    recv_wrs 0 
    rdma_read_wrs 0 
    rdma_read_bytes 0 
    rdma_read_wr_err 0 
    rdma_read_resp_bytes 0 
    rdma_write_wrs 0 
    rdma_write_bytes 0 
    rdma_write_wr_err 0
    retrans_bytes 0
    retrans_pkts 0
    retrans_timeout_events 0
    unresponsive_remote_events 0
    impaired_remote_conn_events 0
```

Alternatively, you can retrieve the metrics for each EFA interface attached to an instance from the sys files using the following command.

```
$ more /sys/class/infiniband/{{device_number}}/ports/{{port_number}}/hw_counters/* | cat
```

For example

```
$ more /sys/class/infiniband/rdmap0s31/ports/1/hw_counters/* | cat
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/lifespan
::::::::::::::
12
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_read_bytes
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_read_resp_bytes
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_read_wr_err
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_read_wrs
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_write_bytes
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_write_recv_bytes
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_write_wr_err
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_write_wrs
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/recv_bytes
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/recv_wrs
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rx_bytes
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rx_drops
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rx_pkts
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/send_bytes
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/send_wrs
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/tx_bytes
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/tx_pkts
::::::::::::::
0
::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/retrans_bytes
::::::::::::::
0
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/retrans_pkts
::::::::::::::
0
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/retrans_timeout_events
::::::::::::::
0
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/unresponsive_remote_events
::::::::::::::
0
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/impaired_remote_conn_events
::::::::::::::
0
```

## Amazon VPC flow logs
<a name="efa-flowlog"></a>

You can create an Amazon VPC Flow Log to capture information about the traffic going to and from an EFA. Flow log data can be published to Amazon CloudWatch Logs and Amazon S3. After you create a flow log, you can retrieve and view its data in the chosen destination. For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide*.

You create a flow log for an EFA in the same way that you create a flow log for an elastic network interface. For more information, see [Create a flow log](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-flow-logs.html#create-flow-log) in the *Amazon VPC User Guide*.

In the flow log entries, EFA traffic is identified by the `srcAddress` and `destAddress`, which are both formatted as MAC addresses, as shown in the following example.

```
version accountId  eniId        srcAddress        destAddress       sourcePort destPort protocol packets bytes start      end        action log-status
2       3794735123 eni-10000001 01:23:45:67:89:ab 05:23:45:67:89:ab -          -        -        9       5689  1521232534 1524512343 ACCEPT OK
```

## Amazon CloudWatch
<a name="efa-cloudwatch"></a>

If you are using EFA in an Amazon EKS cluster, you can monitor your EFAs using CloudWatch Container Insights. Amazon CloudWatch Container Insights supports all of the [EFA driver metrics](#efa-driver-metrics), except: `retrans_bytes`, `retrans_pkts`, `retrans_timeout_events`, `unresponsive_remote_events`, and `impaired_remote_conn_events`.

For more information, see [ Amazon EKS and Kubernetes Container Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-enhanced-EKS.html#Container-Insights-metrics-EFA) in the *Amazon CloudWatch User Guide*.