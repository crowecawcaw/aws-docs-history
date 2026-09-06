

# Collect EFA metrics
<a name="CloudWatch-Agent-EFA"></a>

 You can use the CloudWatch agent to collect Elastic Fabric Adapter (EFA) metrics from Linux servers that have EFA devices attached. To set this up, add an `efa` section inside the `metrics_collected` section of the CloudWatch agent configuration file. For more information, see [Linux section](CloudWatch-Agent-Configuration-File-Details.md#CloudWatch-Agent-Linux-section). 

**Note**  
All EFA metrics are reported as delta values. The agent automatically applies cumulative-to-delta conversion.

The following metrics can be collected.


| Metric | Description | 
| --- | --- | 
| `efa_tx_bytes` | Bytes transmitted on the EFA device. | 
| `efa_rx_bytes` | Bytes received on the EFA device. | 
| `efa_tx_pkts` | Packets transmitted on the EFA device. | 
| `efa_rx_pkts` | Packets received on the EFA device. | 
| `efa_rx_dropped` | Received packets dropped on the EFA device. | 
| `efa_send_bytes` | Bytes sent through EFA send operations. | 
| `efa_send_wrs` | Send work requests completed. | 
| `efa_recv_bytes` | Bytes received through EFA receive operations. | 
| `efa_recv_wrs` | Receive work requests completed. | 
| `efa_rdma_read_bytes` | Bytes transferred through RDMA read operations. | 
| `efa_rdma_read_resp_bytes` | Bytes received in RDMA read responses. | 
| `efa_rdma_read_wrs` | RDMA read work requests completed. | 
| `efa_rdma_read_wr_err` | RDMA read work request errors. | 
| `efa_rdma_write_bytes` | Bytes transferred through RDMA write operations. | 
| `efa_rdma_write_recv_bytes` | Bytes received through RDMA write operations. | 
| `efa_rdma_write_wrs` | RDMA write work requests completed. | 
| `efa_rdma_write_wr_err` | RDMA write work request errors. | 
| `efa_retrans_bytes` | Bytes retransmitted. | 
| `efa_retrans_pkts` | Packets retransmitted. | 
| `efa_retrans_timeout_events` | Retransmission timeout events. | 
| `efa_impaired_remote_conn_events` | Impaired remote connection events. | 
| `efa_unresponsive_remote_events` | Unresponsive remote endpoint events. | 

## Dimensions
<a name="CloudWatch-Agent-EFA-dimensions"></a>

Each EFA metric is emitted with the following dimensions by default:
+ `device` – The EFA device name.
+ `port` – The EFA port number.
+ `eniId` – The ENI ID of the EFA NIC.

To append additional dimensions such as `InstanceId`, use the `append_dimensions` field in the `metrics` section of the agent configuration file.

## Example configuration
<a name="CloudWatch-Agent-EFA-example"></a>

The following example configuration collects a subset of EFA metrics every 60 seconds and appends the `InstanceId` dimension to each metric.

```
{
  "metrics": {
    "append_dimensions": {
      "InstanceId": "${aws:InstanceId}"
    },
    "metrics_collected": {
      "efa": {
        "measurement": [
          "efa_tx_bytes",
          "efa_rx_bytes",
          "efa_tx_pkts",
          "efa_rx_pkts",
          "efa_rx_dropped",
          "efa_rdma_read_bytes",
          "efa_rdma_write_bytes"
        ],
        "metrics_collection_interval": 60
      }
    }
  }
}
```