

# Inbox placement rates
<a name="vdm-gd-inbox-placement-rates"></a>

Inbox placement rates provides ISP-level inbox placement data for your monitored domains. This data is powered by analytics and updated hourly. These metrics are based on a representative sample of data and do not reflect the full volume of emails sent.

**What inbox placement rates provides**  
For each monitored domain, inbox placement rates displays the following information:
+ *ISP-level breakdown* – Inbox rate, spam rate, inbox count, and spam count for each major mailbox provider (Gmail, Outlook, Yahoo, and others).
+ *Aggregate metrics* – Overall inbox rate and spam rate across all ISPs for the selected domain.
+ *Trend data* – A time-series chart showing inbox placement rates by ISP over the selected date range.

## Viewing inbox placement rates using the Amazon SES console
<a name="vdm-gd-inbox-placement-rates-console"></a>

**To view inbox placement rates using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Inbox placement rates** under **Global deliverability** in the **Virtual Deliverability Manager** section.

1. Select a monitored domain from the domain selector.

1. (Optional) Adjust the date range using the date range picker. You can select relative ranges (7, 14, 30, or 90 days) or specify an absolute date range.

1. Review the ISP breakdown table and the trend chart to identify any ISPs where inbox placement is lower than expected.

**Note**  
Inbox placement data is provided by analytics and updated hourly. These metrics are based on a sample of data and do not reflect the full volume of emails sent.