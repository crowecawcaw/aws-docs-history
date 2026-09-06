

# Create mission profile
<a name="getting-started.step4"></a>

 With the *configs* constructed in the previous step, you have identified how to track your satellite, the possible ways to communicate with your satellite, and how to enable near real-time telemetry during contact execution. In this step you will construct one or more mission profiles. A mission profile represents the aggregation of the possible *configs* into an expected behavior that can be then scheduled and operated on. 

 For the latest parameters, please reference the [ AWS::GroundStation::MissionProfile CloudFormation resource type ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html) 

1. Name your mission profile. This allows you to quickly understand its usage within your system. For example, you may have a *satellite-wideband-narrowband-nominal-operations* and a *satellite-narrowband-emergency-operations* if you have a separate narrowband carrier for emergency operations. 

1. Set your tracking config.

1. Set your minimum viable contact durations. This allows you to filter potential contacts to meet your mission needs. 

1.  Set your *streamsKmsKey* and *streamsKmsRole* that are used to encrypt your data during transit. This is used for all AWS Ground Station Agent dataflows. 

1.  Set your dataflows. Create your dataflows to match your carrier signals using the configs you created in the previous step. 

1.  [Optional] Set your pre-pass and post-pass contact duration seconds. This is used to emit per-contact events prior-to and after the contact, respectively. See [Automate AWS Ground Station with Events](monitoring.automating-events.md) for more information. 

1.  [Optional] Set your *telemetrySinkConfigArn* to enable telemetry during contacts. This allows you to receive near real-time telemetry directly in your account for monitoring and analysis. See [Work with telemetry](telemetry.md) for more information. 

1.  [Optional] You can associate Tags to your mission profile. These can be used to help programmatically differentiate your mission profiles. 

 You can reference the [Example mission profile configurations](examples.md), to see just some of the potential configurations. 