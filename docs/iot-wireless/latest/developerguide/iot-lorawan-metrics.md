# Use AWS IoT Core for LoRaWAN metrics

Use AWS IoT Core for LoRaWAN metrics to monitor the health of your LoRaWAN resources in a dashboard
view. It provides information about the connectivity of your devices with the cloud, how
they are functioning, and whether they are operating within specifications. These metrics
can be aggregated to provide historical and up-to-the-minute view of data and trends for
your resources.

## What metrics can I view?

When you activate summary metrics, you can view the following information for all
resources, or for your individual devices and gateways.

If you see that no data is available for one or more widgets, check whether you have
completed the activation steps for viewing summary metrics. You can use the
**Activation steps** widget in the dashboard to check whether you
have correctly configured your LoRaWAN devices, gateways, and destinations, and
activated summary metrics. For information about onboarding your LoRaWAN resources, see
[Connecting gateways and devices to
AWS IoT Core for LoRaWAN](lorawan-getting-started.md "lorawan-getting-started.md").

| List of summary metrics                           | Metric name | AWS account | Individual devices | Individual gateways |
| ------------------------------------------------- | ----------- | ----------- | ------------------ | ------------------- |
| Active devices/gateways                           | Yes         | –           | –                  |
| Uplink message count                              | Yes         | Yes         | Yes                |
| Downlink message count                            | Yes         | Yes         | Yes                |
| Join metrics                                      | Yes         | Yes         | Yes                |
| Message lost rate                                 | Yes         | Yes         | Yes                |
| Signal to noise ratio (SNR) average               | –           | Yes         | Yes                |
| Received signal strength indicator (RSSI) average | –           | Yes         | Yes                |
| Gateway availability                              | –           | –           | Yes                |

## How to view summary metrics?

To view the metrics for your LoRaWAN resources, you can activate the summary metrics
dashboard either from the console or using the AWS IoT Wireless API operations.
You activate summary metrics for all LoRaWAN resources in your AWS account, which
includes all LoRaWAN devices and gateways. The data can be aggregated to provide you
with hourly, daily, or weekly information for your resources.

The LoRaWAN metrics dashboard uses the compute API to display information for your
LoRaWAN resources. When you activate summary metrics, charges might be incurred for
using the LoRaWAN dashboard. To avoid incurring additional charges, you can deactivate
summary metrics. For information about pricing, see [https://aws.amazon.com//iot-core/pricing](https://aws.amazon.com//iot-core/pricing "https://aws.amazon.com//iot-core/pricing") AWS IoT Core pricing.

###### Note

The summary metrics have an expiration time. Hourly metrics expire after six
months, and daily and weekly metrics expire after 12 months.

###### Topics

- [Activate summary metrics
  (console)](#iot-lorawan-metrics-how-console "#iot-lorawan-metrics-how-console")
- [Activate summary metrics (CLI)](#iot-lorawan-metrics-how-cli "#iot-lorawan-metrics-how-cli")

### Activate summary metrics

(console)

1. Go to the [**Monitor**](https://console.aws.amazon.com/iot/home#/dashboard "https://console.aws.amazon.com/iot/home#/dashboard") dashboard of the AWS IoT console
   and choose **LoRaWAN metrics**.
2. Choose **Activate summary metrics** and specify the
   period that you want to use for data to be aggregated, which can be
   **Daily**,**Hourly**, or
   **Weekly**.

You'll see data flowing through the dashboard and displayed for your resources in
the **LoRaWAN overview** widget and in the widget corresponding to
each metric. If you don't see any data displayed, check whether you have correctly
configured your LoRaWAN resources and performed the join procedure for your LoRaWAN
devices so that they can start sending uplink data.

### Activate summary metrics (CLI)

To activate summary metrics and see data flowing through the dashboard, use the
[`UpdateMetricConfiguration`](../apireference/API_UpdateMetricConfiguration.md "../apireference/API_UpdateMetricConfiguration.md") API operation or the [`update-metric-configuration`](../../../cli/latest/reference/iotwireless/update-metric-configuration.md "../../../cli/latest/reference/iotwireless/update-metric-configuration.md") CLI command. The following
code shows a sample request body.

```
{
    "SummaryMetricQueries": [
        {

            "AggregationPeriod": "`OneWeek`",
            "Dimensions": [
                {
                    "name": "`DeviceId`",
                    "value": "`30758fe6-56f1-4f32-8c4c-f17f000e01d3`"
                }
            ],
            "EndTimestamp": `1699574400`,
            "MetricName": "DeviceUplinkLostRate",
            "QueryId": "DeviceUplinkLostRate",
            "StartTimestamp": `1698969600`
        }
    ]
}
```

After you've activated summary metrics, you can use the [`GetMetrics`](../apireference/API_GetMetrics.md "../apireference/API_GetMetrics.md")
API operation or the [`get-metrics`](../../../cli/latest/reference/iotwireless/get-metrics.md "../../../cli/latest/reference/iotwireless/get-metrics.md") CLI
command.

```
{
  "SummaryMetric": {
      "Status": Disabled
  }
}
```

You can then use the [`GetMetricConfiguration`](../apireference/API_GetMetricConfiguration.md "../apireference/API_GetMetricConfiguration.md") API operation or the [`get-metric-configuration`](../../../cli/latest/reference/iotwireless/get-metric-configuration.md "../../../cli/latest/reference/iotwireless/get-metric-configuration.md") CLI command to view the
metric configuration status. The following shows a sample response.

```
{
  "SummaryMetric": {
      "Status": Disabled
  }
}
```

## LoRaWAN metrics

After you activate summary metrics, you can view metrics pertaining to historical data
for all LoRaWAN devices and gateways in your AWS account. You can also find metrics
for each of your LoRaWAN devices and gateways. The following sections describe the
overall metrics for all your resources in general, and for each resource in your
AWS account.

If you don't see any data in the widgets for the metrics, make sure that you have
performed the activation steps correctly for viewing the metrics. You can also configure
logging and use the network analyzer to debug any issues.

###### Note

In the console, you can drag the widgets for the metrics to different locations on
the dashboard. Relocating the widgets might temporarily change the layout of the
dashboard.

The following shows the metrics that you can see in the dashboard and in the details
pages of your gateways and devices on the console.

To view the summary metrics for all resources, go to the [**Monitor**](https://console.aws.amazon.com/iot/home#/dashboard "https://console.aws.amazon.com/iot/home#/dashboard") dashboard of
the AWS IoT console and then choose the **LoRaWAN metrics**
tab.

- An overview of key LoRaWAN summary metrics.
- The activation steps and their progress.
- The number of active devices and gateways.
- The count of uplink and downlink messages.
- The message loss rate, which shows the ratio of the total number of
  packets that are lost.
- The join metrics, which shows the number of join requests and join
  accepts.
  You can view metrics showing historical data for each LoRaWAN device that you
  onboarded to AWS IoT Core for LoRaWAN. You'll find similar metrics as in the
  **Monitor** dashboard with some additional metrics such as
  the average received signal strength indicator (RSSI) and signal to noise ratio
  (SNR).

You can also find a summary of the metrics for all your LoRaWAN devices in the
[**Devices**](https://console.aws.amazon.com/iot/home#/wireless/devices/ "https://console.aws.amazon.com/iot/home#/wireless/devices/") hub of the AWS IoT console. This
includes:

- The number of active devices within the specified time duration,
  which can be the last hour, day, or week
- The total number of devices that have been provisioned up to the
  specified timestamp range, which can be the last hour, day, or
  week.
- The uplink packet loss rate, which corresponds to the ratio of total
  number of uplink packets that are lost during transmission.
- The individual device metrics, go to the [**Devices**](https://console.aws.amazon.com/iot/home#/wireless/devices/ "https://console.aws.amazon.com/iot/home#/wireless/devices/") hub of the AWS IoT console and
  then choose the device for which you want to see the metrics. For
  information about activating these metrics, see [How to view summary metrics?](#iot-lorawan-metrics-how "#iot-lorawan-metrics-how").
  You can view the following metrics for each LoRaWAN device.

###### Note

If you don't see any data in the widgets for the metrics, make sure that
you have onboarded your device correctly for viewing the metrics. You can
also configure logging and use the network analyzer to debug any
issues.

- A summary of key LoRaWAN device metrics
- The count of uplink and downlink messages
- The uplink packet loss rate, which shows the ratio of the total number
  of packets that are lost.
- The join metrics, which shows the number of join requests and join
  accepts.
- The average received signal strength indicator (RSSI) and signal to
  noise ratio (SNR).
  You can view metrics showing historical data for each LoRaWAN gateway that you
  onboarded to AWS IoT Core for LoRaWAN. You'll find similar metrics as in the
  **Monitor** dashboard with some additional metrics such as
  the average received signal strength indicator (RSSI), signal to noise ratio
  (SNR), and gateway availability. You can also find a summary of the metrics for
  all your LoRaWAN gateways in the **Gateways** hub of the AWS IoT
  console.

You can also find a summary of the metrics for all your LoRaWAN gateways in
the [**Gateways**](https://console.aws.amazon.com/iot/home#/wireless/gateways/ "https://console.aws.amazon.com/iot/home#/wireless/gateways/") hub of the AWS IoT console. This
includes:

- The number of uplink and downlink messages that were exchanged between
  the devices and the cloud using the gateways within the specified time
  duration, which can be the last hour, day, or week.
- The total number of gateways that have been provisioned up to the
  specified timestamp range, which can be the last hour, day, or
  week.
  You can view the following metrics for each LoRaWAN gateway.

###### Note

If you don't see any data in the widgets for the metrics, make sure that
you have onboarded your gateway correctly for viewing the metrics. You can
also configure logging and use the network analyzer to debug any
issues.

- A summary of key LoRaWAN gateway metrics
- The count of uplink and downlink messages
- The uplink packet loss rate, which shows the ratio of the total number
  of packets that are lost.
- The join metrics, which shows the number of join requests and join
  accepts.
- The gateway availability information.
- The average received signal strength indicator (RSSI) and signal to
  noise ratio (SNR).
  After you've onboarded your gateways and devices to AWS IoT Core for LoRaWAN, your
  devices will start exchanging messages with the cloud. This metric displays the
  number of active LoRaWAN devices and gateways within a specified time duration
  in your AWS account. Active devices and gateways are those devices that have
  transmitted or received any uplink or downlink data, or gateways that facilitate
  such data transmission.

In the Monitor dashboard, you can use the LoRaWAN overview section to see the
total number of gateways and devices that have been provisioned, and the number
of gateways and devices that are active. Using this information, you can
identify what percentage of devices and gateways that have been provisioned are
active.

This metric displays the number of uplink messages that are sent within a
specified time duration for all active gateways and devices in your
AWS account. Uplink messages are messages that are sent from your device to
AWS IoT Core for LoRaWAN.

The count of uplink messages includes the total number of uplink messages and
the number of uplink messages that are sent from your device to AWS IoT Core for LoRaWAN
using a public network. You can use this information to identify the volume of
uplink messages and the quantity of uplink messages that are arriving at the
cloud over the public network during that period.

This metric displays the number of downlink messages that are sent within a
specified time duration for all active gateways and devices in your
AWS account. Downlink messages are messages that are sent from AWS IoT Core for LoRaWAN
to your devices.

The count of downlink messages includes the total number of downlink messages
and the number of downlink messages that are sent from AWS IoT Core for LoRaWAN to your
devices using a public network. You can use this information to identify the
volume of downlink messages and the quantity of downlink messages that are
arriving at your devices over the public network during that period.

After you've added your device and connected to AWS IoT Core for LoRaWAN, your device can
initiate an uplink message to start exchanging messages with the cloud. You can
use this metric to then track the rate of uplink messages that are lost. Uplink
messages are lost due to the loss of signal during radio transmission from the
device to gateway.

The rate of uplink message loss is indicated by non-sequential frame counters
(FCnt) over the specified time duration. This information can be used to assess
the stability of the connection. An increase in the message loss rate can
indicate that the connection is unstable. To improve the stability of the
connection, you can use adaptive data rate (ADR) by setting the ADR bit in the
frame header of your devices. If the connection still doesn't improve, you can
move the device closer to the gateway or add more gateways around your
devices.

After you've added your device and gateway, you perform a join procedure so
that your device can send uplink data and communicate with AWS IoT Core for LoRaWAN. You
can use this metric to obtain information about join metrics for all active
devices in your AWS account.

This metric displays the rate of total number of device join requests and join
accepts under a gateway within a certain time duration. This information can be
used to determine the total number of join requests and the proportion of
requests that have been approved.

If all join requests haven't been accepted, you can use network analyzer or
configure CloudWatch Logs to check whether AWS IoT Core for LoRaWAN receives the join
requests and if the requests get accepted. If your LoRaWAN devices are setup
correctly, the number of join requests and join accepts must be equal. If all
requests are not accepted, check whether you specified the correct DevEUI and
root key or session keys when provisioning the device.

You can use this metric to monitor the average RSSI (Received signal strength
indicator) within the specified time duration.

This metric can be used with the average SNR (signal to noise ratio) to
measure signal strength and provide information about connectivity status. RSSI
is a measurement that indicates if the signal is strong enough for a good
wireless connection. The RSSI average is an average of all RSSI values for the
device over a specified time duration, which can help provide information about
the device's connection for that duration.

The RSSI value is negative and must be closer to zero for a strong wireless
connection. If the signal is weak, you can use adaptive data rate (ADR) by
setting the ADR bit in the frame header of your devices to make it stronger. If
the connection still doesn't improve, you can move the device closer to the
gateway or add more gateways around your device.

You can use this metric to monitor the average SNR (Signal to noise ratio)
within the specified time duration.

This metric can be used with RSSI to measure signal strength and provide
information about connectivity status. SNR is a measurement that indicates if
the received signal is strong enough compared to the noise level for a good
wireless connection. The SNR average is an average of all SNR values for the
device over a specified time duration, which can help provide information about
the device's connection for that duration.

The SNR value is positive and must be greater than zero to indicate that the
signal power is stronger than the noise power. If the signal is weak, you can
use adaptive data rate (ADR) by setting the ADR bit in the frame header of your
devices to make it stronger. If the connection still doesn't improve, you can
move the device closer to the gateway or add more gateways around your
device.

You can use this metric to obtain information about the availability of this
gateway within a specified time duration.

This metric displays the websocket connection time of this gateway for a
specified time duration. This connection time includes the gateway up time and
the gateway down time. You can use this information to identify when a gateway
was available. It can also be used with the message loss rate to identify when a
packet got lost in transmission.
