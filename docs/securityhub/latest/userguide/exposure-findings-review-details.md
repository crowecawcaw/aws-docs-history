# Reviewing details for exposure findings

###### Note

AWS Security Hub is in preview release and is subject to change.

This topic describes how to review details about exposure findings in the
AWS Security Hub console and with the API.

## Reviewing details for

an exposure finding in the Security Hub console

###### To view details for an exposure finding in the Security Hub console

1. Sign in using your credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home " https://console.aws.amazon.com/securityhub/v2/home").
2. From the navigation pane, choose **Exposures**.
3. Choose an exposure finding that you want to view details.

## Reviewing details for an exposure finding with the API

You can review exposure findings with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") API or with the AWS CLI. You can
filter all exposure findings with the `metadata.product.feature.uid`
field with the `security-hub/Exposure` value. For more information,
see [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md").

###### Example command

The following is an AWS CLI example that retrieves the 10 most recently
generated exposure findings in your account. This example is formatted for
Linux, macOS, or Unix, and it uses the backslash (\) line-continuation
character to improve readability.

```
aws securityhub get-findings-v2 \
--max-results '10' \
--filter '{"CompositeFilters": [{"StringFilters": [{"FieldName":"metadata.product.feature.uid","Filter": {"Value":"security-hub/Exposure","Comparison":"EQUALS"}} ]}]}'

```
