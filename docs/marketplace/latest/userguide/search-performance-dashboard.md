# Search performance dashboard

The **Search performance** dashboard provides metrics on how your AWS Marketplace
listings perform in the AWS Marketplace search experience. You use the dashboard to improve the
discoverability and performance of your listings. The dashboard tracks the number of
impressions, clicks, and click through rates. It also tracks the top keywords that you supply,
and that customers use, and it offers keyword suggestions based on common customer
searches.

The insights from the dashboard can help you refine your product listings to improve
visibility, match your keywords with customer preferences, and drive more qualified traffic to
your business on AWS Marketplace. 

To open the dashboard, start the AWS Marketplace Management Portal and go to the **Insights** tab.

For more information about controlling access to the dashboard, see [Seller dashboards](dashboards.md "dashboards.md"), earlier in this section.

## Section 1: Accessing the dashboard

To unlock this dashboard, you must be a member of the
[AWS Marketplace Seller Prime Program](https://pages.awscloud.com/aws-marketplace-seller-prime.html "https://pages.awscloud.com/aws-marketplace-seller-prime.html").

After you enroll in the Seller Prime program, system
administrators for seller accounts can use the **Insights** tab in
the AWS Marketplace Management Portal to start the **Search performance**
dashboard.

System administrators can also create an AWS Identity and Access Management (IAM) policy to provide access for specific dashboards to
other users in the seller company.

###### Note

As of September 2023, we no longer support access to seller
dashboards enabled by legacy IAM permissions. Use the new Amazon
Resource Name (ARN) format as shown in the following examples to
update your IAM permissions.

For more information about creating policies, see
[Creating
IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"), in the _AWS Identity and Access Management User Guide_.

### Using policies to control access

Use one of the following policies to provide access to the listing performance dashboard.

The following example provides access to all current and future AWS Marketplace resources, including dashboards and reports, regardless of current or future data feeds.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:GetSellerDashboard"
 ],
 "Resource": "arn:aws:aws-marketplace:`us-east-1`:`111122223333`:AWSMarketplace/*"
 }
 ]
 }`

```

The following example provides access to the **Search performance** dashboard by including its ARN. 

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:GetSellerDashboard"
 ],
 "Resource": "arn:aws:aws-marketplace:`us-east-1`:`111122223333`:AWSMarketplace/ReportingData/Marketing_V1/Dashboard/SearchPerformance_V1"
 }
 ]
 }`

```

## Section 2: Filters

This section of the dashboard provides the following filters. Use
them to refine your data.

| Control name      | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Product title** | The title of the product.<br>This filter affects the impressions, clicks, click-through rate, and **AWS Marketplace search keyword recommendations**. It doesn’t affect the \*_Top searched keywords by product category_<br>• table.                                                                                                                                                                  |
| **Date filter**   | You can filter on the past 30, 60, and 90 days, the trailing 12 months (TTM),<br>and the year to date (YTD). You can choose **Custom\*<br>• to use specific start and end date.<br>This filter affects the impressions, clicks, and click-through rate. it doesn’t affect the **AWS Marketplace search keyword recommendations*<br>• or<br>\*\*Top searched keywords by product category*<br>• tables. |

For more information about filtering, see
[Filtering
data on Amazon QuickSight](../../../quicksight/latest/user/adding-a-filter.md "../../../quicksight/latest/user/adding-a-filter.md"), in the _Amazon QuickSight
User Guide_.

## Section 3: AWS Marketplace search performance

This section of the dashboard displays key performance indicators
(KPIs) about the discoverability and performance of your AWS Marketplace listings. The dashboard provides KPIs for the number of
impressions, the number of clicks, and the click-through rate.

You can see year-over-year or period-over-period changes in volume
and percentage. You can also change date ranges.

| Metric                       | Description                                                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Impressions**              | The number of times your listings appear in the top 20 search results on AWS Marketplace.                                                                         |
| **Clicks**                   | The number of times users click your listings from the AWS Marketplace search results.                                                                            |
| **Click-through rate (CTR)** | The ratio between the number of clicks and the number of impressions. A measure of how effective your listings are at engaging customers from the search results. |

## Section 4: Monthly trend for impressions, clicks,

and click-through rate

This section of the dashboard provides monthly trends for a
given date range. It provides KPIs for the number of
impressions, the number of clicks, and the click-through rate.

## Section 5: AWS Marketplace search keyword recommendations

This section of the dashboard provides a table that lists your
current keywords, plus recommended keywords for each of your listings.

| Column names                 | Description                                                                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Product title**            | The title of the product. The link takes you to the product overview page in the<br>AWS Marketplace Management Portal, where you can manage and edit your listings. |
| **Current keywords**         | The keywords you provided in the \*_Update product information_<br>• section of the AWS Marketplace Management Portal.                                              |
| **Top performing keywords**  | The keywords that appear in the top five customer searches for your product.                                                                                        |
| **AWS-recommended keywords** | The keywords that customers use the most when searching for similar products.                                                                                       |
| **Estimated traffic gain %** | The potential traffic gain if you adopt the recommended keywords. Not affected by the date filter.                                                                  |

###### Note

While keywords are important, other factors can affect search results.

- Listing optimization
  - Optimize other parts of your listing, such as short and long
    descriptions.
  - Consider offering features such as free trials to enhance your listing's appeal.

- Matching keywords with listings and target customers
  - As much as possible, match your listings with frequently used keywords.
  - Use only the keywords relevant to your products and their features. Otherwise,
    your listings may appear in a larger number of searches, but fewer users will choose
    them.

- Understanding keyword variations
  - Remember that similar terms, such as "git" and "gitops" may be treated as the same search term.
  - Evaluate the relevance of any variations and adjust your keywords accordingly.

- Updating keywords
  1.  In the AWS Marketplace Management Portal, open the **Products** menu and select a product category.
  2.  Choose the link to your product, choose the **Product information** tab, and navigate to the
      **Provide product information** page.
  3.  Scroll down to the **AWS Marketplace discoverability** section, find
      **Keywords for AWS Marketplace search results**, and adjust your keywords.

## Section 6: Top searched keywords by product category

The top five customer search keywords in each product category for products similar to yours. Other product and date filters on this dashboard don't affect this data.
