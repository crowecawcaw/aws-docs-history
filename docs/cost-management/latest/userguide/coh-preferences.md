# Customizing your Cost Optimization Hub preferences

In **Cost Management preferences**, you can customize various Cost Optimization Hub
settings, including how savings are estimated and your commitment preferences.

## Savings estimation mode preferences

You can customize how your estimated monthly savings are calculated. Savings estimation
mode supports the following two options:

- **After discounts**: Cost Optimization Hub estimates savings incorporating all
  discounts with AWS, such as Reserved Instances and Savings Plans.
- **Before discounts**: Cost Optimization Hub estimates savings by using AWS public
  (On-Demand) pricing, without incorporating any discounts.

###### To customize how estimated monthly savings are calculated

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management
   preferences**.
3. On the **Preferences page**, choose the **Cost Optimization Hub**
   tab.
4. Under **Savings estimation mode**, choose **After
   discounts** or **Before discounts**.
5. Choose **Save preferences**.

## Commitment preferences

You can customize your preferred term length and payment option for reservations and
Savings Plans, which populates the overall estimated savings in the Cost Optimization Hub dashboard. For
example, if you prefer 1-year no upfront commitments, configure these preferences and Cost Optimization Hub
will reflect them in the dashboard within 24 hours. The resulting estimated monthly savings
reflect the savings you can achieve with your preferred commitment term length and payment
option.

**To customize your preferred term length and payment
option:**

Console

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management
   preferences**.
3. On the **Preferences** page, choose the
   **Cost Optimization Hub** tab.
4. For **Term length**, choose between **Highest overall
   savings**, **1-year term**, or **3-year
   term**.
5. For **Payment option**, choose between **Highest
   overall savings**, **No upfront**, **Partial
   upfront**, or **All upfront**.
6. Choose **Save preferences**.

###### Note

If your preferred commitment type isn't available, such as for specific Regions or
instance types, Cost Optimization Hub automatically recommends Savings Plans or reservations with the
highest overall savings.

CLI

1. Log in to your account.
2. Open a terminal or command prompt window.
3. Use the `UpdatePreferences` API operation to update your preferred
   term and payment option:

```
aws cost-optimization-hub update-preferences
                  --preferred-commitment '{"term":"OneYear", "paymentOption": "NoUpfront"}'
```

You can change either the term or payment option, but both fields must be
included in the request. For example, to change only the term to
`ThreeYear` while maintaining your current payment option:

```
aws cost-optimization-hub update-preferences
                  --preferred-commitment '{"term":"ThreeYear", "paymentOption": "NoUpfront"}'
```

To use the default 3-year term (highest savings), either omit the term field or
set it to null:

```
aws cost-optimization-hub update-preferences
                  --preferred-commitment '{"paymentOption": "NoUpfront"}'
```

To use the default for both fields (highest savings), use an empty
object:

```
aws cost-optimization-hub update-preferences
                  --preferred-commitment '{}'
```
