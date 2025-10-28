# Reviewing suppressed findings in

Macie

If you suppress findings with a suppression rule, Amazon Macie continues to generate
findings for subsequent occurrences of sensitive data and potential policy violations
that match the rule's criteria. However, Macie automatically changes the status of the
findings to _archived_. This means that the findings
don't appear by default on the Amazon Macie console, but they persist in Macie until they
expire. (Macie stores findings for 90 days.) This also means that Macie doesn't publish
the findings to Amazon EventBridge as events or to AWS Security Hub.

Because suppressed findings persist in Macie for up to 90 days, you can access and
review them before they expire. In addition to broadening your analysis of findings,
this can help you determine whether to adjust your suppression criteria. To adjust the
criteria, [change the suppression
rules](findings-suppression-rule-change.md "findings-suppression-rule-change.md") for your account.

You can review suppressed findings on the Amazon Macie console by changing your filter
settings.

###### To review suppressed findings on the console

1.  Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2.  In the navigation pane, choose **Findings**. The
    **Findings** page displays findings that Macie created or
    updated for your account in the current AWS Region during the past 90 days. By
    default, this doesn't include findings that were suppressed by a suppression
    rule.
3.  To pivot on and review the findings by a predefined logical group, choose
    **By bucket**, **By type**, or
    **By job** in the navigation pane (under
    **Findings**).
4.  For **Finding status**, do one of the following:

        * To display only suppressed findings, choose
         **Archived**.
        * To display both suppressed and unsuppressed findings, choose
         **All**.
        * To hide suppressed findings again, choose
         **Current**.

    You can also access suppressed findings by using the Amazon Macie API. To retrieve a list
    of suppressed findings, use the [ListFindings](../APIReference/findings.md "../APIReference/findings.md") operation. In
    your request, include a filter condition that specifies `true` for the
    `archived` field. For an example of how to do this by using the AWS Command Line Interface
    (AWS CLI), see [Filtering findings
    programmatically](findings-filter-procedure.md#findings-filter-procedure-api "findings-filter-procedure.md#findings-filter-procedure-api"). To then retrieve the details
    of one or more suppressed findings, use the [GetFindings](../APIReference/findings-describe.md "../APIReference/findings-describe.md")
    operation. In your request, specify the unique identifier for each finding to
    retrieve.

###### Note

As you review the findings, note that suppression rules can work differently for
accounts that are part of an organization. This depends on a finding's category and
whether you have a Macie administrator or member account:

- **Policy findings** – Only a
  Macie administrator can suppress policy findings for the organization's
  accounts.

If you have a Macie administrator account and you created a suppression rule, Macie applies the rule
to policy findings for all the accounts in your organization unless you
configured the rule to exclude specific accounts. If you have a member
account and you want to suppress policy findings for your account, work with
your Macie administrator to suppress the findings.

- **Sensitive data findings** – A
  Macie administrator and individual members can suppress sensitive data findings that
  their sensitive data discovery jobs produce. A Macie administrator can also suppress
  findings that Macie generates while performing automated sensitive data discovery for the
  organization.

Only the account that creates a sensitive data discovery job can suppress
or otherwise access sensitive data findings that the job produces. Only the
Macie administrator account for an organization can suppress or otherwise access
findings that automated sensitive data discovery produces for accounts in the organization.
For more information about the tasks that administrators and members can perform,
see [Macie administrator and member account
relationships](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md").
