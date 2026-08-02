# Test run fails with an access denied error

**Symptom:** A test run fails with an
`AccessDenied` error from AWS FIS or one of the targeted services.

The following table lists possible causes and solutions.

| Cause                                                    | Solution                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Execution role trust policy doesn't allow AWS FIS        | Verify the role trusts `fis.amazonaws.com` and that the<br>`aws:SourceAccount` and `aws:SourceArn` conditions match<br>your account. For the trust policy, see [IAM execution roles for resilience testing](next-gen-resilience-testing-iam.md "next-gen-resilience-testing-iam.md"). |
| Execution role missing permissions for the test template | Each test template runs a different set of AWS FIS actions. Attach the permissions policy<br>for the template you are running. For the policies, see [IAM execution roles for resilience testing](next-gen-resilience-testing-iam.md "next-gen-resilience-testing-iam.md").           |
| Multi-account role chain not configured                  | For a multi-account test, verify the orchestrator role can assume the target role in<br>each account that contains targeted resources.                                                                                                                                                |
