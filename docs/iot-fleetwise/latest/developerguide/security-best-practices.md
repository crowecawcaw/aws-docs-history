# Security best practices for AWS IoT FleetWise

AWS IoT FleetWise provides a number of security features to consider as you develop and implement
your own security policies. The following best practices are general guidelines and don't
represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

To learn about security in AWS IoT see [Security best practices in
AWS IoT Core](../../../iot/latest/developerguide/security-best-practices.md "../../../iot/latest/developerguide/security-best-practices.md") in the _AWS IoT Developer Guide_

## Grant minimum possible permissions

Follow the principle of least privilege by using the minimum set of permissions in
IAM roles. Limit the use of the `*` wildcard for the `Action`
and `Resource` properties in your IAM policies. Instead, declare a finite
set of actions and resources when possible. For more information about least privilege
and other policy best practices, see [Policy best
practices](security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices "security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices").

## Don't log sensitive information

You should prevent the logging of credentials and other personally identifiable
information (PII). We recommend that you implement the following
safeguards:

- Don't use sensitive information in device names.
- Don't use sensitive information in the names and IDs of AWS IoT FleetWise resources,
  for example in the names of campaigns, decoder manifests, vehicle models, and
  signal catalogs, or the IDs of vehicles and fleets.

## Use AWS CloudTrail to view API call history

You can view a history of AWS IoT FleetWise API calls made on your account for security analysis
and operational troubleshooting purposes. To receive a history of AWS IoT FleetWise API calls made
on your account, simply turn on CloudTrail in the AWS Management Console. For more information, see [Log AWS IoT FleetWise API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

## Keep your device clock in sync

It's important to have an accurate time on your device. X.509 certificates have an
expiry date and time. The clock on your device is used to verify that a server
certificate is still valid. Device clocks can drift over time or batteries can get
discharged.

For more information, see the [Keep your device's
clock in sync](../../../iot/latest/developerguide/security-best-practices.md#device-clock "../../../iot/latest/developerguide/security-best-practices.md#device-clock") best practice in the _AWS IoT Core Developer
Guide_.
