

# Streaming modes on Windows, Linux, and macOS clients
<a name="using-streaming-native"></a>

The steps depend on the client used.

------
#### [ Windows ]

1. Choose the **Settings** icon.

1. Select **Streaming Mode** from the drop-down list.

1. In the Streaming Mode window, choose one of the following options:
   + **Best responsiveness**
   + **Best quality**

1. Close the **Streaming Mode** window.  
![Settings button located in the top-left corner of the interface.](https://docs.aws.amazon.com/dcv/latest/userguide/images/streaming.png)

**Tip**  
For information about network performance, choose **Display Streaming Metrics**. For more information, see [Streaming metrics](#using-streaming-metrics-native).

------
#### [ macOS ]

1. In the menu bar, choose the **Connection** menu, then select **Display**.

1. Under **Optimize Streaming For**, choose one of the following options:
   + **Responsiveness**
   + **Image Quality**  
![Display menu showing Optimize Streaming For menu with Responsiveness and Image Quality options.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-streaming-mode.png)

**Tip**  
For information about network performance, choose the **Dashboard** toolbar button. For more information, see [Streaming metrics](#using-streaming-metrics-native).

------
#### [ Linux ]

1. Click on the **Display Settings** menu icon from the toolbar at the top.

1. In the **Streaming mode** section, choose one of the following options:
   + **Best responsiveness**
   + **Best image quality**  
![Display Settings menu showing the Streaming mode section with Best responsiveness selected and Best image quality below it.](https://docs.aws.amazon.com/dcv/latest/userguide/images/linux-pref-display-stream.png)

------

## Streaming metrics
<a name="using-streaming-metrics-native"></a>

The streaming metrics can be used to evaluate your network performance and determine which streaming mode is suitable for your network conditions.

**Note**  
Metrics are displayed for the current Amazon DCV session connection.

To view the streaming metrics, do one of the following depending on the client used.

------
#### [ Windows ]

Choose **Settings**, **Streaming Mode**, **Display Streaming Metrics**.

The streaming metrics provide the following real-time information:
+ **Framerate** – Indicates the number of frames received from the Amazon DCV server every second.
+ **Network latency** – Indicates the amount of time (in milliseconds) it takes for a packet of data to be sent to the Amazon DCV server and back to the client.
+ **Bandwidth usage** – Indicates the amount of data being sent and received over the network connection. The red line shows the peak network throughput. The yellow line shows the average throughput. The blue line shows the current (real-time) throughput. 

![example streaming metric data.](https://docs.aws.amazon.com/dcv/latest/userguide/images/metrics.png)


------
#### [ macOS ]

Choose the **Dashboard** toolbar button and select the **Metrics** tab.

**Tip**  
You can also open the Dashboard from the menu bar. Choose the **View** menu, then select **Dashboard…**.

The **Metrics** tab provides the following information:
+ **Connection status** – Healthy, Unstable, or Offline indicator.
+ **Time to first frame** – How long it took to display the remote desktop after connecting.
+ **Bandwidth usage** – Network usage over time.
+ **Framerate** – Frames per second received from the Amazon DCV server.
+ **Network latency** – Response time in milliseconds.

Each chart shows current, average, and peak values. Hover over the charts to see precise values at any point in time.

The Dashboard can be pinned as a sidebar or detached as a floating window. Choose **Copy** to copy metrics info to the clipboard.

![Streaming metrics showing bandwidth, framerate, and latency charts.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-dashboard-metrics.png)


**Tip**  
You can also display the streaming metrics directly in the toolbar by choosing the **View** menu, then selecting **Metrics in Toolbar**.  

![View menu showing the Metrics in Toolbar option.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-metrics-in-toolbar.png)


------
#### [ Linux ]

Click on the **Streaming Metrics** icon (the information icon) in the toolbar at the top, and then select the **Streaming Metrics** tab.

You can also configure the client to display the streaming metrics directly in the toolbar by turning on the **Streaming metrics in the toolbar** option.

The streaming metrics provide the following real-time information:
+ **Framerate** – Indicates the number of frames received from the Amazon DCV server every second.
+ **Network latency** – Indicates the amount of time (in milliseconds) it takes for a packet of data to be sent to the Amazon DCV server and back to the client.
+ **Bandwidth usage** – Indicates the amount of data being sent and received over the network connection. The red line shows the peak network throughput. The yellow line shows the average throughput. The blue line shows the current (real-time) throughput. 

![Streaming Metrics dialog showing Frame rate, Network latency, Protocol, and a Bandwidth usage graph with Current, Average, and Peak values.](https://docs.aws.amazon.com/dcv/latest/userguide/images/linux-streaming-metrics.png)


------