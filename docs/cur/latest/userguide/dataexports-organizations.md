

# Using Data Exports with AWS Organizations
<a name="dataexports-organizations"></a>

Data Exports can work with AWS Organizations so that management accounts can generate exports with data for all accounts in your organization. Member accounts can also create data exports, but these exports only contain the billing and cost management data for that specific member account. The settings that control whether the management account receives data for all member accounts varies across the Data Exports tables. Refer to the following sections for information about how it is determined whether to include member account data for each table.
+ [Cost and usage report 2.0 (CUR 2.0)](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2.html#cur2-table-organizations)
+ [Cost optimization recommendations (from Cost Optimization Hub)](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cor.html#cor-table-organizations)
+ [FOCUS 1.0 with AWS columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-focus-1-0-aws.html#focus-1-0-table-organizations)
+ [Cost and usage dashboard](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur-dashboard.html#cur-dashboard-table-organizations)
+ [Carbon emissions](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-carbon-emissions.html#carbon-emissions-table-organizations)

The IAM policies that allow or restrict the ability to create an export are the same for both management and member accounts.

If you are an administrator of an AWS Organizations management account and you don’t want member accounts to create an export, you can apply a service control policy (SCP) that prevents member accounts from creating exports. While the SCP prevents member accounts from creating new exports, it doesn’t delete previously created exports.

**Note**  
SCPs apply only to member accounts. To prevent a management account from creating an export, modify the IAM policies attached to the user roles in the management account.