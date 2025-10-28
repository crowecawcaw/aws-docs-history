# Monitor and manage your fleet operations to maximize sustainability

It is recommended that your solution be monitored and managed
efficiently across its lifecycle to reduce the carbon footprint
of your operations.  Common operational tasks such as inspecting
the connectivity state of a device, verifying device credentials
are configured correctly, and querying devices based on their
current state must be in place before launch so that your system
has the required visibility to troubleshoot applications and
reduce the need for site visits. From a sustainability point of
view, inaccurate information about device status can result in
delayed or erroneous actions such as unnecessary truck rolls or
mis-directed corrective actions. This can lead to decreased
efficiency and increased costs. 

Having an accurate view of the state of all devices is therefore
an imperative for operating at scale.  This is best done through
the use of tools, services and automation.  Here are some of the
key ways to monitor IoT operations using AWS IoT services:

- Use AWS IoT Device Management services to manage the entire
  lifecycle of your IoT devices, including firmware updates in
  the field.  This helps in the remote management of devices,
  reducing the need for site visits and lowering the carbon
  footprint of your operations.  For additional observability
  into your device's resource allocation, you can install
  the [AWS X-Ray daemon](../../../xray/latest/devguide/xray-daemon.md "../../../xray/latest/devguide/xray-daemon.md") to see how edge applications perform and
  where CPU utilization or other optimizations can be made to
  decrease power consumption or better allocate device
  resources.
- Monitor resource utilization periodically and set up an
  alerting system to notify appropriate stakeholders if the
  utilization goes above a specific threshold.  For simple
  threshold conditions, detection can be done on the device
  itself and alerts sent to the cloud.  During the development
  phase, cloud-based monitoring can be used to determine the
  appropriate threshold values for your workload.  It is
  recommended to configure automatic actions such as
  optimizing resource allocation or disabling processes to
  avoid system downtime caused by anomalous conditions.
  Regularly reviewing monitoring data and threshold
  adjustments will support accurate and timely notifications
  that reflect the current performance of the IoT device.
- [AWS IoT Core](../../../iot/latest/developerguide/what-is-aws-iot.md "../../../iot/latest/developerguide/what-is-aws-iot.md") provides a set of metrics that you can use
  to monitor the performance and health of your IoT devices
  and applications. These metrics include device connections,
  message delivery, and rule engine metrics. You can view
  these metrics using Amazon CloudWatch or the AWS IoT Core
  console.  In addition, you can monitor device metrics such
  as CPU and memory utilization, battery levels and the like
  using the
  [Fleet
  Metrics feature](../../../iot/latest/developerguide/iot-fleet-metrics.md "../../../iot/latest/developerguide/iot-fleet-metrics.md") of AWS IoT Core. These metrics can be
  used to proactively identify devices that are degrading or
  will soon need attention, averting service impact and the
  need for emergency truck rolls.
