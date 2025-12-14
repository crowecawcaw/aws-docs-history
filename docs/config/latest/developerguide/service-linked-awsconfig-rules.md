# Service-Linked AWS Config Rules

A service-linked AWS Config rule is a unique type of AWS Config managed rules that supports other
AWS services to create AWS Config rules in your account. Service-linked rules are
predefined to include all the permissions required to call other AWS services on your
behalf. These rules are similar to standards that an AWS service recommends in your
AWS account for compliance verification.

These service-linked AWS Config rules are owned by AWS service teams. The AWS service team
creates these rules in your AWS account. You have read-only access to these rules. You
cannot edit or delete these rules if you are subscribed to AWS service that these rules
are linked to.

**Service-linked rules and the AWS Command Line Interface**

With the AWS CLI, the [PutConfigRule](../APIReference/API_PutConfigRule.md "../APIReference/API_PutConfigRule.md"), [DeleteConfigRule](../APIReference/API_DeleteConfigRule.md "../APIReference/API_DeleteConfigRule.md"),
and [DeleteEvaluationResults](../APIReference/API_DeleteEvaluationResults.md "../APIReference/API_DeleteEvaluationResults.md") APIs return access denied with the following error
message:

`INSUFFICIENT_SLCR_PERMISSIONS = "An AWS service owns ServiceLinkedConfigRule. You do
 not have permissions to take action on this rule."`

**Service-linked rules and the AWS Config console**

In the AWS Config console, the service-linked AWS Config rules are visible in the **Rules** page. The
**Edit** and **Delete
results** buttons are greyed in the console to
restrict you from editing the rule. You can view details of the rule by choosing the rule.

**Service-linked rules, remediation actions, and conformance packs**

To add remediation actions to a service-linked rules in a conformance pack,
you need to add the remediation action to the conformance pack template itself, and then update the conformance pack with your updated template.
For information on updating conformance packs, see [Deploying a Conformance Pack (Console)](conformance-pack-console.md "conformance-pack-console.md"), [Deploying a Conformance Pack (AWS CLI)](conformance-pack-cli.md "conformance-pack-cli.md") and [Managing Organizational Conformance Packs](conformance-pack-organization-apis.md "conformance-pack-organization-apis.md").

**Editing and deleting service-linked rules**

To edit or delete a service-linked rule, contact the AWS service that created the rule.
For example, for service-linked rules created by AWS Security Hub CSPM, you can remove a service-linked rule by following these steps in the _AWS Security Hub CSPM User Guide_: [Disabling a security standard](../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md "../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md").
