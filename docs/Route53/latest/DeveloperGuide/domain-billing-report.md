# Downloading a domain billing report

If you manage multiple domains and you want to view charges by domain for a specified time period, you can download a
domain billing report. This report includes all charges that apply to domain registration, including the following:

- Registering a domain
- Renewing registration for a domain
- Transferring a domain to Amazon Route 53
- Changing the owner of a domain (for some TLDs, this operation is free)
  Sometimes your billing report can show billing periods into the future. This happens because
  the domain auto renewal process starts the month before the domain expires. Therefore,
  for example, in your August report, you might see a billing period that starts the
  September after and runs until the September of the following year.

When you run the report using the console, you can choose the following options:

- **Last 12 months**: The report includes charges from one year
  before you ran the report until the current day. For example, if you run the
  report on June 3, it includes charges from June 3 the previous year until the
  current day.
- **Individual months in the last year**: The report includes charges for the specified month.
  If you run the report programmatically, you can get charges for any date range, starting with July 31, 2014. That's the date that
  Route 53 started to support domain registration. For example, see
  [view-billing](../../../cli/latest/reference/route53domains/view-billing.md "../../../cli/latest/reference/route53domains/view-billing.md")
  in the _AWS CLI Command Reference_.

The billing report is in CSV format, and the contents are described by the [ViewBilling](../APIReference/API_domains_ViewBilling.md "../APIReference/API_domains_ViewBilling.md") API.

###### To download a domain billing report

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Registered Domains**.
3. Choose **Domain billing report**.
4. Choose the date range for the report, and then choose **Download domain report**.
5. Follow the prompts to open the report or to save it.
6. If you encounter issues while downloading a domain billing report, you can contact AWS Support for free.
   For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").
