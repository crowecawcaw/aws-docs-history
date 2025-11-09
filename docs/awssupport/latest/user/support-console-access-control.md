# Adding IAM policies for the Support Center Console API operations

Before June 1, 2026, you must create AWS Identity and Access Management policies for the Support Center Console API
operations. If you don't create these policies by June 1, 2026, you will receive
`AccessDenied` errors.

To add these operations to your IAM policies, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the _AWS Identity and Access Management User Guide_.

The following table summarizes the console operations.

###### Note

These operations are for the console only. They're not available for use in the AWS SDK
or the AWS CLI.

| Operation                 | Access level | Description                                                                                              |
| ------------------------- | ------------ | -------------------------------------------------------------------------------------------------------- |
| GetAccountState           | READ         | Grants permission for the console to show the current account state.                                     |
| GetAccountGovCloudEnabled | READ         | Grants permission to determine if your account is GovCloud enabled.                                      |
| GetCaseDraft              | READ         | Grants permission for the console to show the case draft that you previously created.                    |
| CreateCaseDraft           | WRITE        | Grants permission to create or update a case draft for the given case type.                              |
| DeleteCaseDraft           | WRITE        | Grants permission to delete a case draft for the given case type.                                        |
| GetBanner                 | READ         | Grants permission for the console to show the Support banner displayed during customer impacting events. |
| DescribeDynamicHelp       | READ         | Grants permission for the console to show dynamic help resources for the selected service and category.  |
| CreateContact             | WRITE        | Grants permission for the console to create an authenticated contact for the selected contact type.      |
| CheckSubscription         | READ         | Grants permission for the console to verify if your account has access to the selected product.          |
| GetQuestionnaire          | READ         | Grants permission for the console to show the customer feedback questionnaire.                           |
| SaveFeedback              | WRITE        | Grants permission to save questionnaire feedback.                                                        |

###### Note

If you have a custom VPN configuration, then your IAM policies must allow the
Support Center Console API endpoint in the [aws.sourceIP
conditions](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md"). If the Support Center Console API endpoint isn't allowed, then your ClientIp
address won't forward to the API correctly. The following table provides the Support Center Console API
endpoints by AWS Region.

| AWS Region                                                   | Support Center Console API endpoint |
| ------------------------------------------------------------ | ----------------------------------- |
| `https://api.us-east-1.prod.support-console.support.aws.dev` | US East (N. Virginia)               |
| `https://api.us-west-2.prod.support-console.support.aws.dev` | US West (Oregon)                    |
| `https://api.eu-west-1.prod.support-console.support.aws.dev` | Europe (Ireland)                    |
