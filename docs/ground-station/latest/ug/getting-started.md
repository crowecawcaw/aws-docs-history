# Create mission profile

With the _configs_ constructed in the previous step, you have identified how
to track your satellite and the possible ways to communicate with your satellite. In this step
you will construct one or more mission profiles. A mission profile represents the aggregation of
the possible _configs_ into an expected behavior that can be then scheduled
and operated on.

For the latest parameters, please reference the
[AWS::GroundStation::MissionProfile CloudFormation resource type](../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.md")

1. Name your mission profile. This allows you to quickly understand its usage within your
   system. For example, you may have a _satellite-wideband-narrowband-nominal-operations_ and a
   _satellite-narrowband-emergency-operations_ if you have
   a separate narrowband carrier for emergency operations.
2. Set your tracking config.
3. Set your minimum viable contact durations. This allows you to filter potential contacts
   to meet your mission needs.
4. Set your _streamsKmsKey_ and _streamsKmsRole_ that
   are used to encrypt your data during transit. This is used for all AWS Ground Station Agent dataflows.
5. Set your dataflows. Create your dataflows to match your carrier signals using the
   configs you created in the previous step.
6. [Optional] Set your pre-pass and post-pass contact duration seconds. This is used to
   emit per-contact events prior-to and after the contact, respectively. See
   [Automate AWS Ground Station with
   Events](monitoring.md "monitoring.md")
   for more information.
7. [Optional] You can associate Tags to your mission profile. These can be used to help
   programmatically differentiate your mission profiles.

You can reference the [Example mission profile configurations](examples.md "examples.md"), to see just some of
the potential configurations.
