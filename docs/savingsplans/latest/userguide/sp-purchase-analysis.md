

# Running a Savings Plan purchase analysis
<a name="sp-purchase-analysis"></a>

Use Purchase Analyzer to configure multiple parameters for your planned Savings Plan purchase analysis.<a name="sp-rec-customize-howto"></a>

**To run a purchase analysis**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Purchase Analyzer**.

1. Choose **Compute Savings Plans**, **Database Savings Plans**, **EC2 Instance Savings Plans**, or **SageMaker AI Savings Plans**.

1. For **EC2 Instance Savings Plans**, choose a **Region** and **Instance family**.

1. Under **Analysis level**, choose **Payer** or **Linked account**.

1. If you chose **Linked account**, select a linked account from the dropdown menu.

1. Under **Term**, choose a **1-year** or **3-year** commitment term.

1. Under **Payment option**, choose **All upfront**, **Partial upfront**, or **No upfront**.

1. Under **Lookback period**, choose a lookback period within the last 60 days.

1. Under **Exclude expiring Savings Plans**, select Savings Plans expiring within the next 90 days that you’d like to exclude from the analysis.

1. Under **Commitment**, choose **Recommended**, **Target coverage (%)**, or **Custom**.

1. If you chose **Target coverage (%)**, under **Target coverage (%)**, enter your target coverage percentage.

1. If you chose **Custom**, under **Hourly commitment ($)**, enter your preferred hourly commitment amount.

1. Choose **Run analysis**.