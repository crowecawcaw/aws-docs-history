

# Compute and hardware
<a name="compute-and-hardware"></a>


| IOTPERF02: How do you measure and maintain the performance of your IoT solution? | 
| --- | 
|   | 

 There are several key types of performance monitoring related to IoT deployments including device, cloud performance, and storage and analytics. Create appropriate performance metrics using data collected from logs with telemetry. Start with basic performance tracking and build on those metrics as your business core competencies expand. 

 Use Amazon CloudWatch Logs metric filters to transform your IoT application standard output into custom metrics through regular expression pattern matching. Create Amazon CloudWatch alarms based on your application's custom metrics to gain quick insight into your IoT application's behavior. 

 Set up fine-grained logs to track specific thing groups. During IoT solution development, enable `DEBUG` logging for a clear understanding of the progress of events about each IoT message as it passes from your devices through the message broker and the rules engine. In production, change the logging to `ERROR` and `WARN`. 

 In addition to cloud instrumentation, run instrumentation on devices prior to deployment to verify that the devices make the most efficient use of their local resources and that firmware code does not lead to unwanted scenarios such as memory leaks. Deploy code that is highly optimized for constrained devices and monitor the health of your devices using device diagnostic messages published to AWS IoT from your embedded application. 

## IOTPERF02-BP01 Implement comprehensive monitoring solutions to collect performance data from your IoT devices
<a name="iotperf02-bp01"></a>

 It is important to establish performance baselines and key performance indicators (KPIs) specific to your IoT devices and application requirements. These metrics may include device CPU and memory utilization, network bandwidth consumption, battery life, and embedded software-level metrics such as data throughput and latency. Additionally, depending on the programming language used, other memory metrics to consider are heap usage or garbage collection frequency (Java), memory leak detection and dynamic memory allocation ratio (C/C\+\+), and memory pool utilization (Python). 

 **Level of risk exposed if this best practice is not established:** Medium 

 **Prescriptive guidance IOTPERF02-BP01-01** *Analyze device metrics and compare to a standard baseline.* 

 Collecting historical performance data from your devices helps you understand regular behavior for your deployments and potentially detect anomalies by using machine learning strategies and tools. Use AWS IoT Device Defender to audit device configurations, monitor device metrics, and detect deviations from expected behavior. Additionally, services like Amazon CloudWatch can be integrated to collect and analyze device performance metrics, set alarms, and run automated actions based on predefined thresholds. 

## IOTPERF02-BP02 Evaluate the runtime performance of your application
<a name="iotperf02-bp02"></a>

 Application performance in production can be different from what you observe in a controlled test environment. Actively analyzing the performance of your application based on device health, network latency, and payload size provides insight on how to obtain performance improvements. By using different types of metrics, the health of each device in a multi-device setting can be obtained. 

 **Level of risk exposed if this best practice is not established:** High 

 **Prescriptive guidance IOTPERF02-BP02-1** *Analyze connection patterns, sensor data and set up a device security profile to detect anomalies.* 
+  Measuring changes in connection patterns of devices might indicate some devices having a jittery network connection. 
+  Comparing device-side timestamps from multiple devices to arrival times on the cloud-side might indicate local network latency or additional hops in device path. 

### Resources
<a name="resources-11"></a>
+  [Configure AWS IoT logging](https://docs.aws.amazon.com/iot/latest/developerguide/configure-logging.html) 
+  [Gather system health telemetry data from AWS IoT Greengrass core devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/telemetry.html) 
+  [AWS IoT Device Defender Detect](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-detect.html) 
+  [How to detect anomalies in device metrics and improve your security posture using AWS IoT Device Defender](https://aws.amazon.com/blogs/iot/how-to-detect-anomalies-in-device-metrics-and-improve-your-security-posture-using-aws-iot-device-defender-custom-metrics/) 