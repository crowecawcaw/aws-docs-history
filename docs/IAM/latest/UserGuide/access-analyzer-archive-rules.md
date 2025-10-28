# Archive rules

Archive rules automatically archive new findings that meet the criteria you define when
you create the rule. You can also apply archive rules retroactively to archive existing
findings that meet the archive rule criteria. For example, you can create an archive rule to
automatically archive any findings for a specific Amazon S3 bucket that you regularly grant
access to. Or if you grant access to multiple resources to a specific principal, you can
create a rule that automatically archives any new finding generated for access granted to
that principal. This lets you focus only on active findings that may indicate a security
risk.

When you create an archive rule, only new findings that match the rule criteria are
automatically archived. Existing findings are not automatically archived. When you create a
rule, you can include up to 20 values per criterion in the rule. For a list of filter keys
that you can use to create or update an archive rule, see [IAM Access Analyzer filter keys](access-analyzer-reference-filter-keys.md "access-analyzer-reference-filter-keys.md").

###### Note

When you create or edit an archive rule, IAM Access Analyzer does not validate the values
you include in the filter for the rule. For example, if you add a rule to match an
AWS account, IAM Access Analyzer accepts any value in the field, even if it is not a valid
AWS account number.

###### To create an archive rule

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Access analyzer**, then choose **Analyzer
   settings**.
3. In the **Analyzers** section, choose the analyzer for which you
   want to create an archive rule.
4. On the **Archive rules** tab, choose **Create archive
   rule**.
5. Enter a name for the rule if you want to change the default name.
6. In the **Rule** section, under **Criteria**,
   select a property to match for the rule.
7. Choose an condition for the property value, such as **Contains**,
   **Is**, or **Not Equals**.

The operators available depend on the property you choose. 8. Optionally, add additional values for the property, or add additional criteria for
the rule. For external access findings, to ensure that your rule won’t archive new
findings for public access, you can also include the criterion **Public
access** and set it to **false**.

To add another value for a criterion, choose **Add another
value**. To add another criterion for the rule, choose **Add
criterion**. 9. When you finish adding criteria and values, choose **Create
rule** to apply the rule to new findings only. Choose **Create
and archive active findings** to archive new and existing findings
based on the rule criteria. In the **Results** section, you can
review the list of active findings the archive rule applies to.
For example, to create a rule for external access findings that automatically archives any
findings for Amazon S3 buckets: choose **Resource type**, and then
choose **Is** for the condition. Next choose **S3
bucket** from the **Value** list.

To create a rule for unused access findings that automatically archives any finding for a
particular account: choose **Resource Owner Account**, and then choose
**Equals** for the condition. Type the AWS account ID in the
**Value** text box.

Continue to define criteria to customize the rule as appropriate for your environment, and
then choose **Create rule**.

If you are create a new rule and add multiple criteria, you can remove a single criterion
from the rule by choosing **Remove this criterion**. You can remove a value
added for a criterion by choosing **Remove value**.

###### To edit an archive rule

1. Choose name of the rule to edit in the **Name** column.

You can edit only one archive rule at a time. 2. Add new criteria or remove the existing criteria and values for each
criterion. 3. Choose **Save changes** to apply the rule to new findings only.
Choose **Save and archive active findings** to archive new and
existing findings based on the rule criteria.

###### To delete an archive rule

1. Select the checkbox for the rules that you want to delete.
2. Choose **Delete**.
3. Type `delete` in the **Delete archive rule**
   confirmation dialog, and then choose **Delete**.
   The rules are deleted only from the analyzer in the current Region. You must delete
   archive rules separately for each analyzer that you created in other Regions.
