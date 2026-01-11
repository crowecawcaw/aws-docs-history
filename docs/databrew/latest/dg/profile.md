# Creating a ruleset with data

quality rules

In the following procedure, you can find an example of creating a ruleset and
applying it to a dataset. A _ruleset_ is a set of
rules that compare different data metrics against expected values. You then can use this ruleset in a profile job to validate the data quality rules that it
includes.

###### To create an example ruleset with data quality rules

1. Sign in to the AWS Management Console and open the DataBrew console at
   [https://console.aws.amazon.com/databrew/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **DQ RULES** from the navigation pane, and
   then choose **Create data quality ruleset**.
3. Enter a name for your ruleset. Optionally, enter a description for
   your ruleset.
4. Under **Associated dataset**, choose a dataset to associate with the
   ruleset.

After you select a dataset, you can view the **Dataset
preview** pane at right. 5. Use the preview in the **Dataset preview** pane to
explore the values and schema for the dataset as you determine the data
quality rules to create. The preview can give you insight about
potential issues that you might have with the data.

Some data sources, such as databases, don't support data preview. In
that case, you can run a profile job without validating the data quality
rules first. Then you can get information about the data schema and values
distribution by using the data profile. 6. Check the **Recommendations** tab, which lists
some rule suggestions that you can use when creating your ruleset. You can
select all, some, or none of the recommendations.

After selecting relevant recommendations, choose
**Add to ruleset**.

This will add rules to your ruleset. Inspect and modify parameters if needed. Note that only columns of simple types such as _string_,
_numbers_ and _boolean_ can be used in data quality rules. 7. Choose **Add another rule** to add a rule not covered by recommendations.
You can change rule names to make it easier to interpret validation results later. 8. Use **Data quality check scope** to choose whether individual columns will be selected per each check in this rule or
whether they should be applied to a group of columns you select. For example, if your dataset has several numeric columns that should have values
between 0 and 100, you can define the rule once and select all these columns to be checked by this rule. 9. If your rule will have more than one check, then in the **Rule success criteria** dropdown, choose whether all checks should be met or which ones meet the criteria. 10. Select a check that will be performed to verify this rule in the **Data quality check** dropdown.
For more information about available checks, see [Available checks](profile.md "profile.md"). 11. If you chose **Individual check for each column** in the **Data quality check scope**, choose a column. Select or type the column name for this check. 12. Select parameters depending on the check. Some conditions accept only provided custom values and some also support reference to another column. 13. If you choose checks for **Column values** such as _Contains_ condition for string values,
then you can specify “passing” threshold. For example, if you want at least 95 percent of values to satisfy the condition, you need to choose
_Greater than equals_ as a threshold’s **Condition**, enter 95 as a **Threshold** and leave
_"%(percent) rows"_ in the next dropdown in the **Threshold** section.
Or if you want no more than 10 rows where _value is missing_ condition is true, then you can select _Less than equals_
as a **Condition**, enter 10 for **Threshold** and choose **rows** in the next dropdown.
Please note that you might get different results if you're using samples of different size during validation. 14. Add more rules if needed. 15. Choose **Create ruleset**.
