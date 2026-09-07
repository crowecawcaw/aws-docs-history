

# MIDASEC07-BP01 Deploy continuous monitoring tools
<a name="midasec07-bp01"></a>

 Implement continuous monitoring of your industrial systems to detect and respond to threats in real time. Monitoring should span cloud, edge, and on-premises systems across both IT and OT environments. 

 **Desired outcome:** Security teams can detect anomalies and threats early, reducing the impact of potential breaches. 

 **Benefits of establishing this best practice:** Enables real-time visibility, faster incident response, and proactive threat mitigation. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-26"></a>

 Use AWS monitoring tools such as Amazon CloudWatch, AWS IoT Device Defender, and AWS Config to gather and analyze telemetry. 

### Implementation steps
<a name="implementation-steps-27"></a>
+  Enable Amazon CloudWatch metrics and logs for all AWS workloads. 
+  Deploy AWS IoT Device Defender to monitor device behavior and audit configurations. 
+  Use AWS Config to track configuration changes across resources. 
+  Integrate alerts with AWS SNS or AWS Security Hub CSPM for real-time response. 

## Resources
<a name="resources-27"></a>
+  [ What is AWS IoT Device Defender? ](https://docs.aws.amazon.com/iot-device-defender/latest/ug/what-is.html) 
+  [ What Is AWS Config? ](https://docs.aws.amazon.com/config/latest/developerguide/what-is-aws-config.html) 