# How to use AWS IoT Device Defender detect

1. You can use AWS IoT Device Defender Detect with just cloud-side metrics, but if you plan to use
   device-reported metrics, you must first deploy the AWS IoT SDK on your AWS IoT connected
   devices or device gateways. For more information, see [Sending metrics from devices](detect-device-side-metrics.md#DetectMetricsMessages "detect-device-side-metrics.md#DetectMetricsMessages").
2. Consider viewing the metrics that your devices generate before you define behaviors
   and create alarms. AWS IoT can collect metrics from your devices so you can first identify
   usual or unusual behavior for a group of devices, or for all devices in your account. Use
   [CreateSecurityProfile](../../../iot/latest/apireference/API_CreateSecurityProfile.md "../../../iot/latest/apireference/API_CreateSecurityProfile.md"), but specify only those
   `additionalMetricsToRetain` that you're interested in. Don't specify
   `behaviors` at this point.

Use the AWS IoT console to look at your device metrics to see what constitutes typical
behavior for your devices. 3. Create a set of behaviors for your security profile. Behaviors contain metrics that
specify normal behavior for a group of devices or for all devices in your account. For
more information and examples, see [Cloud-side metrics](detect-cloud-side-metrics.md "detect-cloud-side-metrics.md") and [Device-side metrics](detect-device-side-metrics.md "detect-device-side-metrics.md"). After you create a set of behaviors, you can validate
them with [ValidateSecurityProfileBehaviors](../../../iot/latest/apireference/API_ValidateSecurityProfileBehaviors.md "../../../iot/latest/apireference/API_ValidateSecurityProfileBehaviors.md"). 4. Use the [CreateSecurityProfile](../../../iot/latest/apireference/API_CreateSecurityProfile.md "../../../iot/latest/apireference/API_CreateSecurityProfile.md") action to create a security profile that includes
your behaviors. You can use the `alertTargets` parameter to have alarms
sent to a target (an SNS topic) when a device violates a behavior. (If you send
alarms using SNS, be aware that these count against your AWS account's SNS topic
quota. It's possible that a large burst of violations can exceed your SNS topic
quota. You can also use CloudWatch metrics to check for violations. For more information,
see [Monitor AWS IoT alarms and metrics using Amazon CloudWatch](../../../iot/latest/developerguide/monitoring-cloudwatch.md "../../../iot/latest/developerguide/monitoring-cloudwatch.md") in the _AWS IoT Core Developer Guide_. 5. Use the [AttachSecurityProfile](../../../iot/latest/apireference/API_AttachSecurityProfile.md "../../../iot/latest/apireference/API_AttachSecurityProfile.md") action to attach the security
profile to a group of devices (a thing group), all registered things in your
account, all unregistered things, or all devices. AWS IoT Device Defender Detect starts checking for
abnormal behavior and, if any behavior violations are detected, sends alarms. You
might want to attach a security profile to all unregistered things if, for example,
you expect to interact with mobile devices that are not in your account's thing
registry. You can define different sets of behaviors for different groups of devices
to meet your needs.

To attach a security profile to a group of devices, you must specify the ARN of the
thing group that contains them. A thing group ARN has the following format.

```
arn:aws:iot:`region`:`account-id`:thinggroup/`thing-group-name`
```

To attach a security profile to all of the registered things in an AWS account
(ignoring unregistered things), you must specify an ARN with the following format.

```
arn:aws:iot:`region`:`account-id`:all/registered-things
```

To attach a security profile to all unregistered things, you must specify an ARN with
the following format.

```
arn:aws:iot:`region`:`account-id`:all/unregistered-things
```

To attach a security profile to all devices, you must specify an ARN with the
following format.

```
arn:aws:iot:`region`:`account-id`:all/things
```

6. You can also keep track of violations with the [ListActiveViolations](../../../iot/latest/apireference/API_ListActiveViolations.md "../../../iot/latest/apireference/API_ListActiveViolations.md") action, which lets you to see which
   violations were detected for a given security profile or target device.

Use the [ListViolationEvents](../../../iot/latest/apireference/API_ListViolationEvents.md "../../../iot/latest/apireference/API_ListViolationEvents.md") action to see which violations were
detected during a specified time period. You can filter these results by security profile, device, or alarm verification state. 7. You can verify, organize, and manage your alarms, by marking their verification state and
providing a description of that verification state, by using the [PutVerificationStateOnViolation](../../../iot/latest/apireference/API_PutVerificationStateOnViolation.md "../../../iot/latest/apireference/API_PutVerificationStateOnViolation.md")
action. 8. If your devices violate the defined behaviors too often, or not often enough, you
should fine-tune the behavior definitions. 9. To review the security profiles that you set up and the devices that are being
monitored, use the [ListSecurityProfiles](../../../iot/latest/apireference/API_ListSecurityProfiles.md "../../../iot/latest/apireference/API_ListSecurityProfiles.md"), [ListSecurityProfilesForTarget](../../../iot/latest/apireference/API_ListSecurityProfilesForTarget.md "../../../iot/latest/apireference/API_ListSecurityProfilesForTarget.md"), and [ListTargetsForSecurityProfile](../../../iot/latest/apireference/API_ListTargetsForSecurityProfile.md "../../../iot/latest/apireference/API_ListTargetsForSecurityProfile.md") actions.

Use the [DescribeSecurityProfile](../../../iot/latest/apireference/API_DescribeSecurityProfile.md "../../../iot/latest/apireference/API_DescribeSecurityProfile.md") action to get more details about a
security profile. 10. To update a security profile, use the [UpdateSecurityProfile](../../../iot/latest/apireference/API_UpdateSecurityProfile.md "../../../iot/latest/apireference/API_UpdateSecurityProfile.md") action. Use the [DetachSecurityProfile](../../../iot/latest/apireference/API_DetachSecurityProfile.md "../../../iot/latest/apireference/API_DetachSecurityProfile.md") action to detach a security profile
from an account or target thing group. Use the [DeleteSecurityProfile](../../../iot/latest/apireference/API_DeleteSecurityProfile.md "../../../iot/latest/apireference/API_DeleteSecurityProfile.md") action to delete a security profile
entirely.
