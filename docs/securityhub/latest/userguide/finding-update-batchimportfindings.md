# BatchImportFindings for finding

providers

Finding providers can use the [BatchImportFindings](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") operation to create new findings in
AWS Security Hub CSPM. They can also use this operation to update findings that they created.
Finding providers can't update findings that they didn't create.

Customers, SIEMs, ticketing, SOAR, and other types of tools must use the [BatchUpdateFindings](../../1.0/APIReference/API_BatchUpdateFindings.md "../../1.0/APIReference/API_BatchUpdateFindings.md") operation to make updates related to
their investigation of findings from finding providers. For more information, see [BatchUpdateFindings for
customers](finding-update-batchupdatefindings.md "finding-update-batchupdatefindings.md").

When Security Hub CSPM receives a `BatchImportFindings` request to create or update a
finding, it automatically generates a \*\*Security Hub Findings

- Imported\*\* event in Amazon EventBridge. You can take automated action
  on that event. For more information, see [Using EventBridge for automated response and remediation](securityhub-cloudwatch-events.md "securityhub-cloudwatch-events.md").

## Prerequisites for using

`BatchImportFindings`

`BatchImportFindings` must be called by one of the following:

- The account that is associated with the findings. The identifier of the
  associated account must match the value of the `AwsAccountId`
  attribute for the finding.
- An account that is allow-listed as an official Security Hub CSPM partner
  integration.

Security Hub CSPM can only accept finding updates for accounts that have Security Hub CSPM enabled. The
finding provider also must be enabled. If Security Hub CSPM is disabled, or the finding provider
integration is not enabled, then the findings are returned in the
`FailedFindings` list, with an `InvalidAccess`
error.

## Determining whether to create

or update a finding

To determine whether to create or update a finding, Security Hub CSPM checks the
`ID` field. If the value of `ID` doesn't match an existing
finding, Security Hub CSPM creates a new finding.

If `ID` matches an existing finding, Security Hub CSPM checks the
`UpdatedAt` field for the update, and proceeds as follows:

- If `UpdatedAt` on the update matches or occurs before
  `UpdatedAt` on the existing finding, Security Hub CSPM ignores the update
  request.
- If `UpdatedAt` on the update occurs after
  `UpdatedAt` on the existing finding, Security Hub CSPM updates the
  existing finding.

## Restrictions on finding

updates with `BatchImportFindings`

Finding providers can't use `BatchImportFindings` to update the
following attributes of an existing finding:

- `Note`
- `UserDefinedFields`
- `VerificationState`
- `Workflow`

Security Hub CSPM ignores any content provided in a `BatchImportFindings` request
for these attributes. Customers, or entities acting on their behalf (such as
ticketing tools), can use `BatchUpdateFindings` to update these
attributes.

## Updating findings with

FindingProviderFields

Finding providers also shouldn't use `BatchImportFindings` to update
the following top-level attributes in the AWS Security Finding Format (ASFF):

- `Confidence`
- `Criticality`
- `RelatedFindings`
- `Severity`
- `Types`

Instead, finding providers should use the [FindingProviderFields](asff-top-level-attributes.md#asff-findingproviderfields "asff-top-level-attributes.md#asff-findingproviderfields")
object to provide values for these attributes.

**Example**

```
"FindingProviderFields": {
    "Confidence": 42,
    "Criticality": 99,
    "RelatedFindings":[
      {
        "ProductArn": "arn:aws:securityhub:us-west-2::product/aws/guardduty",
        "Id": "123e4567-e89b-12d3-a456-426655440000"
      }
    ],
    "Severity": {
        "Label": "MEDIUM",
        "Original": "MEDIUM"
    },
    "Types": [ "Software and Configuration Checks/Vulnerabilities/CVE" ]
}
```

For `BatchImportFindings` requests, Security Hub CSPM handles values in the
top-level attributes and in [FindingProviderFields](asff-top-level-attributes.md#asff-findingproviderfields "asff-top-level-attributes.md#asff-findingproviderfields") as follows.

**(Preferred) `BatchImportFindings` provides a value for an
attribute in [FindingProviderFields](asff-top-level-attributes.md#asff-findingproviderfields "asff-top-level-attributes.md#asff-findingproviderfields"), but does not provide a
value for the corresponding top-level attribute.**

For example, `BatchImportFindings` provides
`FindingProviderFields.Confidence`, but does not provide
`Confidence`. This is the preferred option for
`BatchImportFindings` requests.

Security Hub CSPM updates the value of the attribute in
`FindingProviderFields`.

It replicates the value to the top-level attribute only if the
attribute wasn't already updated by
`BatchUpdateFindings`.

**`BatchImportFindings` provides a value for a top-level
attribute, but does not provide a value for the corresponding attribute in
`FindingProviderFields`.**

For example, `BatchImportFindings` provides
`Confidence`, but does not provide
`FindingProviderFields.Confidence`.

Security Hub CSPM uses the value to update the attribute in
`FindingProviderFields`. It overwrites any existing
value.

Security Hub CSPM updates the top-level attribute only if the attribute was not
already updated by `BatchUpdateFindings`.

**`BatchImportFindings` provides a value for both a top-level
attribute and the corresponding attribute in
`FindingProviderFields`.**

For example, `BatchImportFindings` provides both
`Confidence` and
`FindingProviderFields.Confidence`.

For a new finding, Security Hub CSPM uses the value in
`FindingProviderFields` to populate both the top-level
attribute and the corresponding attribute in
`FindingProviderFields`. It doesn't use the provided
top-level attribute value.

For an existing finding, Security Hub CSPM uses both values. However, it updates
the top-level attribute value only if the attribute was not already
updated by `BatchUpdateFindings`.
