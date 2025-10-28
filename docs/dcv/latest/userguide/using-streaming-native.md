# Streaming modes on Windows, Linux, and macOS clients

## Streaming modes on Windows clients

1. Choose the **Settings** icon.
2. Select **Streaming Mode** from the drop-down list.
3. In the Streaming Mode window, choose one of the following options:
   - **Best responsiveness**
   - **Best quality**

4. (Optional) For information about network performance, choose **Display Streaming
   Metrics**. For more information, see [Streaming metrics](#using-streaming-metrics-native "#using-streaming-metrics-native").

![Settings button located in the top-left corner of the interface.](images/streaming.png) 5. Close the **Streaming Mode** window.

## Streaming modes on macOS clients

1. Choose the **DCV Viewer** icon at the top of the window.
2. Select **Preferences** from the drop-down menu.
3. Select the **Display** tab in the **Preferences** window.
4. Choose one of the following options:
   - **Best responsiveness**
   - **Best image quality**

5. (Optional) For information about network performance, choose **Display Streaming
   Metrics**. For more information, see [Streaming metrics](#using-streaming-metrics-native "#using-streaming-metrics-native").

![Settings button located in the top-left corner of the interface.](images/mac-preferences-display-stream.png) 6. Close the **Preferences** window.

## Streaming modes on Linux clients

1. Choose the **Settings** icon at the top of the window. **Streaming Mode**.
2. Select the **Display** tab in the **Preferences** window.
3. Choose one of the following options:
   - **Best responsiveness**
   - **Best image quality**

4. (Optional) For information about network performance, choose **Display Streaming
   Metrics**. For more information, see [Streaming metrics](#using-streaming-metrics-native "#using-streaming-metrics-native").

![Settings button located in the top-left corner of the interface.](images/linux-pref-display-stream.png) 5. Close the **Preferences** window.

## Streaming metrics

The streaming metrics can be used to evaluate your network performance and determine which
streaming mode is suitable for your network conditions. To view the streaming metrics, choose
**Settings**, **Streaming Mode**, **Display
Streaming Metrics**.

The streaming metrics provide the following real-time information:

###### Note

Metrics are displayed for the current Amazon DCV session connection.

- **Framerate**—Indicates the number of frames received from
  the Amazon DCV server every second.
- **Network latency**—Indicates the amount of time (in milliseconds)
  it takes for a packet of data to be sent to the Amazon DCV server and back to the client.
- **Bandwidth usage**—Indicates the amount of data being
  sent and received over the network connection. The red line shows the peak network
  throughput. The yellow line shows the average throughput. The blue line shows the current
  (real-time) throughput.
  The following image shows example streaming metric data.

![example streaming metric data.](images/metrics.png)
