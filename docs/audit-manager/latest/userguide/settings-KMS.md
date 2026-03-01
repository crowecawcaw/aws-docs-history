# Configuring your data encryption settings

You can choose how you encrypt your data in AWS Audit Manager. Audit Manager automatically creates a
unique AWS managed key for the secure storage of your data. By default, your Audit Manager data
is encrypted with this KMS key. However, if you want to customize your data encryption
settings, you can specify your own symmetric encryption customer managed key. Using your own
KMS key gives you more flexibility, including the ability to create, rotate, and
disable keys.

## Prerequisites

If you provide a customer managed key, it must be in the same AWS Region as your
assessment in order to generate assessment reports and export evidence finder search
results successfully.

## Procedure

You can update your data encryption settings using the Audit Manager console, the AWS Command Line Interface
(AWS CLI), or the Audit Manager API.

###### Note

When you change your Audit Manager data encryption settings, these changes apply to any
new assessments that you create. This includes any assessment reports and
evidence finder exports that you create from your new assessments.

The changes don't apply to existing assessments that you created before you
changed your encryption settings. This includes new assessment reports and CSV
exports that you create from existing assessments, in addition to existing
assessment reports and CSV exports. Existing assessments—and all their
assessment reports and CSV exports—continue to use the old KMS key. If
the IAM identity that generates the assessment report can't use the old
KMS key, grant permissions at the key policy level.

Audit Manager console

###### To update your data encryption settings on the Audit Manager console

1. From the **General** settings tab, go to the
   **Data encryption** section.
2. To use the default KMS key that's provided by Audit Manager, clear
   the **Customize encryption settings
   (advanced)** check box.
3. To use a customer managed key, select the **Customize encryption settings (advanced)** check
   box. You can then choose an existing KMS key, or create a new
   one.

AWS CLI

###### To update your data encryption settings in the AWS CLI

Run the [update-settings](../../../cli/latest/reference/auditmanager/update-settings.md "../../../cli/latest/reference/auditmanager/update-settings.md") command and use the
`--kms-key` parameter to specify your own
customer managed key.

In the following example, replace the `placeholder
 text` with your own information.

```
aws auditmanager update-settings --kms-key `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
```

Audit Manager API

###### To update your data encryption settings using the API

Call the [UpdateSettings](../APIReference/API_UpdateSettings.md "../APIReference/API_UpdateSettings.md") operation and use the [kmsKey](../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-kmsKey "../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-kmsKey") parameter to specify your own customer managed key.

For more information, choose the previous links to read more in the
_Audit Manager API Reference_. This includes
information about how to use this operation and parameter in one of the
language-specific AWS SDKs.

## Additional resources

- For instructions on how to create keys, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md")
  in the _AWS Key Management Service User Guide_.
- For instructions on how to grant permissions at the key policy level, see
  [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the
  _AWS Key Management Service Developer Guide_.
