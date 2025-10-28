# Grouping findings in Security Hub CSPM

You can group findings in AWS Security Hub CSPM based on the values of a
selected attribute.

When you group the findings, the list of findings is replaced with a list of values for the
selected attribute in the matching findings. For each value, the list displays the number of
matching findings.

For example, if you group the findings by AWS account ID, you see a list of account
identifiers, with the number of matching findings for each account.

Security Hub CSPM can display up to 100 values for a selected attribute. If there are more than 100 values,
you only see the first 100.

When you choose an attribute value, Security Hub CSPM displays the list of matching findings for that value.

###### To group the findings in a findings list (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. To display a findings list, take one of the following actions from the navigation pane:
   - Choose **Findings**.
   - Choose **Insights**. Choose an insight.
     Then, on the results list, choose an insight result.
   - Choose **Integrations**. Choose
     **See findings** for an integration.

3. In the **Group by** drop down, choose the attribute to use for the grouping.

To remove a grouping attribute, choose the **x** icon. When you remove the grouping
attribute, the list changes from the list of attribute values to a list of findings.
