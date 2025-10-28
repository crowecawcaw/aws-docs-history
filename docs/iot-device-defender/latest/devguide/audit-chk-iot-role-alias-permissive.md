# Role alias overly

permissive

AWS IoT role alias provides a mechanism for connected devices to authenticate to AWS IoT
using X.509 certificates and then obtain short-lived AWS credentials from an IAM
role that is associated with an AWS IoT role alias. The permissions for these credentials
must be scoped down using access policies with authentication context variables. If your
policies are not configured correctly, you could leave yourself exposed to an escalation
of privilege attack. This audit check ensures that the temporary credentials provided by
AWS IoT role aliases are not overly permissive.

This check is triggered if one of the following conditions are found:

- The policy provides administrative permissions to any services used in the
  past year by this role alias (for example, "iot:\*", "dynamodb:\*", "iam:\*", and
  so on).
- The policy provides broad access to thing metadata actions, access to
  restricted AWS IoT actions, or broad access to AWS IoT data plane actions.
- The policy provides access to security auditing services such as "iam",
  "cloudtrail", "guardduty", "inspector", or "trustedadvisor".
  This check appears as `IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK` in the CLI
  and API.

Severity: **Critical**

## Details

The following reason codes are returned when this check finds a noncompliant IoT
policy:

- ALLOWS_BROAD_ACCESS_TO_USED_SERVICES
- ALLOWS_ACCESS_TO_SECURITY_AUDITING_SERVICES
- ALLOWS_BROAD_ACCESS_TO_IOT_THING_ADMIN_READ_ACTIONS
- ALLOWS_ACCESS_TO_IOT_NON_THING_ADMIN_ACTIONS
- ALLOWS_ACCESS_TO_IOT_THING_ADMIN_WRITE_ACTIONS
- ALLOWS_BROAD_ACCESS_TO_IOT_DATA_PLANE_ACTIONS

## Why it

matters

By limiting permissions to those that are required for a device to perform its
normal operations, you reduce the risks to your account if a device is
compromised.

## How to fix

it

Follow these steps to fix any noncompliant policies attached to things, thing
groups, or other entities:

1. Follow the steps in [Authorizing
   direct calls to AWS services using AWS IoT Core credential
   provider](../../../iot/latest/developerguide/authorizing-direct-aws.md "../../../iot/latest/developerguide/authorizing-direct-aws.md") to apply a more restrictive policy to your role
   alias.

You can use mitigation actions to:

- Apply the `PUBLISH_FINDINGS_TO_SNS` mitigation action if you
  want to implement a custom action in response to the Amazon SNS message.

For more information, see [Mitigation actions](dd-mitigation-actions.md "dd-mitigation-actions.md").
