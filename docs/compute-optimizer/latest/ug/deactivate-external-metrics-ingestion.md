# Opting out of external metrics

ingestion

This section provides you with instructions on how to opt out of external metric ingestion. You can
opt out external metric ingestion using the Compute Optimizer console or the AWS CLI.

## Procedure

Console

###### To opt out of external metric ingestion

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **General** in the navigation pane.
   Then, choose the **External metrics ingestion** tab.
3. If you’re an individual AWS account holder, skip to step 4.

If you’re the account manager or delegated administrator of your organization,
you can opt out all member accounts or an individual member account for external
metrics ingestion.

    * To opt out all member accounts, choose **All opted-in accounts** from the
     Preference level dropdown.
    * To opt out an individual member account, choose **Choose account** from the
     Preference level dropdown. In the prompt that appears, select the account you want to opt out.
     Then, choose **Set account level**.

4. Choose **Edit**.
5. In the prompt that appears, select **No external metrics provider**.
   Then, choose **Confirm**.

CLI

###### To opt out of external metric ingestion

1. Open a terminal or command prompt window.
2. Call the following API operation.
   - Replace `myRegion` with the source
     AWS Region.
   - Replace `123456789012` with your account ID.

```
`aws compute-optimizer delete-recommendation-preferences --region `myRegion` --resource-type=Ec2Instance --recommendation-preference-names='["ExternalMetricsPreference"]' --scope='{"name":"AccountId", "value":"`123456789012`"}'`
```

## Additional resources

- [Configuring external metrics
  ingestion](configure-external-metrics-ingestion.md "configure-external-metrics-ingestion.md")
- [External metrics ingestion](external-metrics-ingestion.md "external-metrics-ingestion.md")
