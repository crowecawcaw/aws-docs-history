

# Getting started with global deliverability
<a name="vdm-gd-get-started"></a>

To start using global deliverability, you enable it from the Virtual Deliverability Manager Settings page in the Amazon SES console. After enabling, you select which of your verified sending domains to monitor.

## Enabling global deliverability using the Amazon SES console
<a name="vdm-gd-get-started-console"></a>

**To enable global deliverability using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Settings** under **Virtual Deliverability Manager**.

1. In the **Global deliverability** panel, choose **Enable global deliverability**.

1. In the confirmation dialog, review the subscription details and choose **Enable global deliverability**.

   The subscription includes monitored domains, dedicated IP monitoring, and inbox placement tests. For pricing details, see [Amazon SES Pricing](https://aws.amazon.com/ses/pricing/).

1. After enabling, choose **Edit domains** to select which of your verified sending domains to monitor.

## Disabling global deliverability
<a name="vdm-gd-disable"></a>

**To disable global deliverability using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Settings** under **Virtual Deliverability Manager**.

1. In the **Global deliverability** panel, choose **Disable global deliverability**.

1. In the confirmation dialog, enter `disable` in the confirmation field, and then choose **Disable global deliverability**.

**Important**  
Disabling global deliverability removes access to campaign analytics, inbox placement testing, and reputation monitoring.