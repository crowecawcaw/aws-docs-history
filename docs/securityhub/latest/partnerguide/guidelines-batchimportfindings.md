# Guidelines for using the

`BatchImportFindings` API

When using the [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") API operation to send findings to AWS Security Hub, use the
following guidelines.

- You must call [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") using the account that is associated with the
  findings. The identifier of the associated account is the value of the
  `AwsAccountId` attribute for the finding.
- Send the largest batch that you can. Security Hub accepts up to 100 findings per batch, up to 240
  KB per finding, and up to 6 MB per batch.
- The throttle rate limit is 10 TPS per account per Region, with a burst of 30 TPS.
- You must implement a mechanism to retain the state of findings if throttling or network
  issues exist. You also need the finding state so that you can submit finding updates as a
  finding moves in and out of compliance.
- For information about the maximum lengths of strings and other limitations, see [AWS
  Security Finding Format (ASFF)](../userguide/securityhub-findings-format.md "../userguide/securityhub-findings-format.md") in the _AWS Security Hub User Guide_.
