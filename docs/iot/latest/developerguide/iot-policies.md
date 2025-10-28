# AWS IoT Core policies

AWS IoT Core policies are JSON documents. They follow the same conventions as IAM
policies. AWS IoT Core supports named policies so many identities can reference the same
policy document. Named policies are versioned so they can be easily rolled back.

AWS IoT Core policies allow you to control access to the AWS IoT Core data plane. The
AWS IoT Core data plane consists of operations that allow you to connect to the AWS IoT Core
message broker, send and receive MQTT messages, and get or update a thing's Device
Shadow.

An AWS IoT Core policy is a JSON document that contains one or more policy statements.
Each statement contains:

- `Effect`, which specifies whether the action is allowed or
  denied.
- `Action`, which specifies the action the policy is allowing or
  denying.
- `Resource`, which specifies the resource or resources on which the
  action is allowed or denied.
  Changes made to a policy can take anywhere between 6 and 8 minutes to become effective
  because of how AWS IoT caches the policy documents. That is, it may take a few minutes to
  access a resource that has recently been granted access, and a resource may be
  accessible for several minutes after its access has been revoked.

AWS IoT Core policies can be attached to X.509 certificates, Amazon Cognito identities, and thing
groups. The policies attached to a thing group apply to any thing within that group. For
the policy to take effect, the `clientId` and the thing name must match.
AWS IoT Core policies follow the same policy evaluation logic as IAM policies. By
default, all policies are implicitly denied. An explicit allow in any identity-based or
resource-based policy overrides the default behavior. An explicit deny in any policy
overrides any allows. For more information, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow") in the _AWS Identity and Access Management User
Guide_.

###### Topics

- [AWS IoT Core policy actions](iot-policy-actions.md "iot-policy-actions.md")
- [AWS IoT Core action resources](iot-action-resources.md "iot-action-resources.md")
- [AWS IoT Core policy variables](iot-policy-variables.md "iot-policy-variables.md")
- [Cross-service confused deputy
  prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")
- [AWS IoT Core policy examples](example-iot-policies.md "example-iot-policies.md")
- [Authorization with Amazon Cognito identities](cog-iot-policies.md "cog-iot-policies.md")
