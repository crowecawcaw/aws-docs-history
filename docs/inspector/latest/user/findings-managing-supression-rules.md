# Suppressing Amazon Inspector findings

You can create suppression rules to hide findings that match criteria.
For example, you can create a suppression rule to hide findings based on their severity ratings.
If Amazon Inspector generates a finding that matches your suppression rule, Amazon Inspector suppresses the finding and hides it from view.
Amazon Inspector stores suppressed findings until they're remediated.
Once a suppressed finding is remediated, Amazon Inspector closes the finding.
You can view suppressed findings in the console.

You create suppression rules to prioritize your most important findings.
Suppression rules don't have any impact on your findings, as they only hide findings from view.
You cannot create a suppression rule that closes or remediates findings.
You can also [suppress unwanted findings in AWS Security Hub CSPM with an Amazon EventBridge rule](https://aws.amazon.com/blogs/security/how-to-create-auto-suppression-rules-in-aws-security-hub/ "https://aws.amazon.com/blogs/security/how-to-create-auto-suppression-rules-in-aws-security-hub/").
The procedures in this section describe how to create, view, edit, and delete a suppression rule.

###### Note

Only the delegated administrator for an organization can create and manage suppression rules.

## Creating a suppression

rule

You can create suppression rules to filter the list of findings that are shown by
default. You can create a suppression rule programmatically by using the [CreateFilter](../../v2/APIReference/API_CreateFilter.md "../../v2/APIReference/API_CreateFilter.md") API and specifying `SUPPRESS` as the value for `action`.

###### Note

Only stand alone accounts and Amazon Inspector delegated administrators can create and manage suppression rules. Members in an organization will not see an option for suppression rules in the navigation pane.

**To create a suppression rule (console)**

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. In the navigation pane, choose **Suppression
   rules**. Then choose **Create
   rule**.
3. For each criterion, do the following:
   - Select the filter bar to see a list of filter criteria that you
     can add to your suppression rule.
   - Select the filter criteria for your suppression rule.

4. When you have finished adding criteria, enter a name for the rule and an
   optional description.
5. Choose **Save rule**. Amazon Inspector immediately
   applies the new suppression rule and hides any findings that match the
   criteria.

## Viewing suppressed

findings

By default, Amazon Inspector does not display suppressed findings in the Amazon Inspector console.
However, you can view the findings suppressed by a particular rule.

**To view suppressed findings**

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. In the navigation pane, select **Suppression
   rules**.
3. In the suppression rules list, select the title of the rule.

## Editing a suppression rule

You can make changes to suppression rules at any time.

**To modify suppression rules**

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. From the navigation pane, choose **Suppression rules**.
3. Choose the name of the suppression rule that you want to change, and then choose **Edit**.
4. Make your intended changes, and then choose **Save**.

## Deleting a suppression

rule

You can delete suppression rules. If you delete a suppression rule, Amazon
Inspector stops suppressing new and existing occurrences of findings that meet the
rule criteria and that aren't suppressed by other rules.

After you delete a suppression rule, new and existing occurrences of findings that
met the rule's criteria have a status of **Active**. This means
that they appear by default on the Amazon Inspector console. In addition, Amazon Inspector publishes these
findings to AWS Security Hub CSPM and Amazon EventBridge as events.

**To delete a suppression rule**

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. In the navigation pane, select **Suppression
   rules**.
3. Select the check box next to the title of the suppression rule you want to
   delete.
4. Choose **Delete**, and then confirm your choice to
   permanently delete the rule.
