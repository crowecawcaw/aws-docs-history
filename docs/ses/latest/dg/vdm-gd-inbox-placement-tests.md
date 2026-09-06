

# Inbox placement tests
<a name="vdm-gd-inbox-placement-tests"></a>

Inbox placement testing sends your campaign to seed accounts across major mailbox providers before you send to real subscribers, so you can catch placement and authentication issues before they reach your audience. Results are typically available in 2–4 hours.

**What inbox placement tests provide**  
Each completed test provides the following information:
+ *Overall results* – Inbox percentage, spam percentage, and missing percentage across all tested ISPs.
+ *ISP breakdown* – Per-ISP inbox, spam, and missing percentages for Gmail, Outlook, Yahoo, and other major providers.
+ *Test details* – Report ID, subject line, from address, creation date, and test status.

Your global deliverability subscription includes inbox placement tests each month. For pricing details including included quantities and overage charges, see [Amazon SES Pricing](https://aws.amazon.com/ses/pricing/).

## Creating an inbox placement test
<a name="vdm-gd-inbox-placement-tests-create"></a>

**To create an inbox placement test using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Inbox placement tests** under **Global deliverability** in the **Virtual Deliverability Manager** section.

1. Choose **Create test**.

1. Select the identity to send from. You can choose either a verified email address or specify a local part with a verified domain.

1. Enter the **Subject** line for the test email.

1. Enter the email **Content** (HTML or plain text) that you want to test.

1. Choose **Create test**.

   The test appears in the tests list with a status of *In progress*. Results are typically available in 2–4 hours.

## Viewing test results
<a name="vdm-gd-inbox-placement-tests-view"></a>

**To view inbox placement test results using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Inbox placement tests** under **Global deliverability** in the **Virtual Deliverability Manager** section.

1. Choose the test name from the tests list to view its details.

1. Review the **Test details** section for overall results and the **ISP breakdown** table for per-provider placement data.