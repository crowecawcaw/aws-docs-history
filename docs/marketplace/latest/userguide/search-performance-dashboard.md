

# Search performance dashboard
<a name="search-performance-dashboard"></a>

The **Search Performance** dashboard helps you optimize your product discoverability with comprehensive search insights for both external search engines, such as Google, as well as AWS Marketplace search.

## Overview
<a name="search-performance-overview"></a>

The **Search Performance** dashboard provides AWS Marketplace Sellers with comprehensive analytics to improve product listing discoverability across multiple search channels. This dashboard includes both external search engine optimization (SEO) insights as well as internal AWS Marketplace search data and recommendations.

To open the dashboard, start the AWS Marketplace Management Portal and go to the **Insights** tab. For more information about controlling access to the dashboard, see [Seller dashboards](dashboards.md), earlier in this section.

In the **Search Performance** dashboard, you can optimize your product visibility on external search engines like Google, as well as within AWS Marketplace search results with:
+ Keyword performance analytics
+ Optimization recommendations for key fields including product description and short description
+ Discover new keyword recommendations to aid in content optimization

## Accessing the dashboard
<a name="search-performace-access"></a>

To unlock this dashboard, you must enroll or be a member of the [AWS Marketplace Seller Prime Program](https://pages.awscloud.com/aws-marketplace-seller-prime.html).

After you are eligible, you can access SEO insights via Partner Central:

**How to Access in existing Partner Central**

1. [Log into](https://partnercentral.awspartner.com/partnercentral2/s/) your Partner Central account.

1. Navigate to **Analytics**.

1. Choose **AWS Marketplace Insights** from the drop down.

1. Select the **Search Performance** section at the top for new SEO Insights.

**How to Access in new Partner Central**

1. [Sign in](https://docs.aws.amazon.com/partner-central/latest/getting-started/signing-in.html) to learn more about getting started with Partner Central.

1. Log into your Partner Central account.

1. Use the left-hand navigation to open **AWS Marketplace Insights**.

1. Select **Search Performance** for new SEO Insights.

System administrators can also create an AWS Identity and Access Management (IAM) policy to provide access for specific dashboards to other users in the seller company.

**Note**  
As of September 2023, we no longer support access to seller dashboards enabled by legacy IAM permissions. Use the new Amazon Resource Name (ARN) format as shown in the following examples to update your IAM permissions.  
For more information about creating policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html), in the *AWS Identity and Access Management User Guide*.

### Using policies to control access
<a name="search-performance-access-policies"></a>

Use one of the following policies to provide access to the listing performance dashboard.

The following example provides access to all current and future AWS Marketplace resources, including dashboards and reports, regardless of current or future data feeds.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "aws-marketplace:GetSellerDashboard"
    ],
    "Resource": "arn:aws:aws-marketplace:{{us-east-1}}:{{111122223333}}:AWSMarketplace/*"
    }
    ]
    }
```

------

The following example provides access to the **Search performance** dashboard by including its ARN.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "aws-marketplace:GetSellerDashboard"
    ],
    "Resource": "arn:aws:aws-marketplace:{{us-east-1}}:{{111122223333}}:AWSMarketplace/ReportingData/Marketing_V1/Dashboard/SearchPerformance_V1"
    }
    ]
    }
```

------

## Search Performance Insights
<a name="search-performance-seo-insights"></a>

What are SEO Insights?

SEO Insights help you optimize your public AWS Marketplace product listings for better visibility in external search engines, as well as within AWS Marketplace search. This feature provides data-driven recommendations to improve your search rankings and drive more qualified traffic to your products. These recommendations also improve visibility in AI-powered discovery, where AI agents recommend products, generate comparisons, and help customers create proposals. **Disclaimer**: This dashboard provides data-driven recommendations powered by BrightEdge and AI. These recommendations are advisory only and are provided to assist sellers in optimizing their listings; however, they do not guarantee any specific outcomes or results. For more information on general SEO best practices see [here](https://docs.aws.amazon.com/marketplace/latest/userguide/search-engine-optimization.html).

*Key Capabilities*
+ **Keyword Performance Insights**
  + View top performing keywords currently driving organic traffic from search engines to your listing(s)
  + See monthly search volumes and current ranking positions
+ **Keyword Recommendations**
  + Discover up to 5 new keyword opportunities
  + Access search volume data for strategic planning
+ **AI-Powered Content Optimization Recommendations**
  + Receive optimized product title suggestions
  + Get short description optimization recommendations

## Section 1: Use filters to select a product and time frame
<a name="search-perf-filters"></a>

In order to see search performance data, you must select a product and month from the drop down at the top of the dashboard. Data is refreshed monthly, when updated the insights reflect data from prior month. For example, data published in December will show November trends.


| Control name | Description | 
| --- | --- | 
| Product title | The title of the product.<br />This filter affects **Current and recommended product title and description**, **Current top performing keywords**, and **Recommended keywords**. | 

For more information about filtering, see [Filtering data on Quick](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html), in the *Quick User Guide*.

## Section 2: Current and recommended product title and description
<a name="search-perf-title-description"></a>

This section of the **Search performance** dashboard pulls title and description information from your public product listing. Recommended product title and description are generated using AI and Brightedge SEO Insights.

## Section 3: Current top performing keywords and Recommended keywords
<a name="search-perf-keywords"></a>

Current top performing keywords come from Brightedge SEO Insights as well as Google Search Console. These are the keywords that are currently driving the most traffic to your product listing. The dashboard provides search volume, and ranking information. You want to ensure to maintain these keywords throughout your listing to maintain performance.

Recommended keywords are generated using Brightedge insights and AI. You can incorporate relevant keywords by naturally integrating them throughout your product detail page to improve ranking for those respective terms. For AWS Marketplace AI-powered discovery, integrate keywords naturally alongside specific details like AWS service names, compliance standards (SOC2, HIPAA), and quantifiable benefits. AI agents use these specifics to match your product to customer intent.

**Note**  
Rank: The current position, which the listing is ranking for in search engine page results (SERP) for that respective keyword.  
Search volume: Estimated monthly search volume for that specific term in Google.  
Not ranked: Your listing is not yet ranking on search engine page results for this term.

Glossary of terms:


| Column names | Description | 
| --- | --- | 
| Product title | The title of the product in your listing. The link takes you to the product overview page in the AWS Marketplace Management Portal, where you can manage and edit your listings. | 
| Short Description | The short description field on your listing, which is also used as a meta description field for Google. | 
| Top performing keywords | The keywords that appear in the top five customer searches for your product. It is recommended this field be 150 characters max. | 
| Recommended keywords | Highly search keywords that may be relevant for your listing. | 

## Addition SEO and Listing Engagement Best Practices
<a name="search-perf-best-practices"></a>

While keywords are important, other factors can affect search results and click through rates. To optimize your listing:
+ Optimize each section of your listing, including product title, as well as short and long descriptions.
+ Complete all available metadata fields; incomplete listings may be less competitive in search results.
+ Consider offering features such as free trials, videos, and promotional media to enhance your listing's appeal.
+ Encourage customers to leave reviews that highlight specific benefits like ease of integration and deployment speed.
+ Configure [Express Private Offers](https://docs.aws.amazon.com/marketplace/latest/userguide/express-private-offers.html) to streamline the procurement process for buyers.
+ Ensure pricing is transparent and uses standard units that buyers can easily compare.
+ Use measurable claims and specific product capabilities rather than generic marketing language.