

# AI-assisted solution listing

AI-assisted solution listing helps you create high-quality solution listings from your existing digital assets. It generates and validates solution content and rates your solution against the AWS Marketplace solution quality rubric. It returns field-level recommendations so you know which fields to improve before you publish.

It extends AI-assisted product listing to solutions. For products, see [AI-assisted product listing](ai-assisted-product-listing.md).

AI-assisted solution listing is not available in AWS GovCloud (US) Regions or the China Regions.

**Topics**
+ [What it does](#what-it-does)
+ [Prerequisites](#prerequisites)
+ [Creating a solution](#creating-a-solution)
+ [Improving an existing solution](#improving-an-existing-solution)
+ [Understanding listing quality](#understanding-the-score)
+ [How duplicate detection works](#duplicate-detection)
+ [Supported inputs](#supported-inputs)
+ [Programmatic access](#programmatic-access)
+ [Frequently asked questions](#solution-faqs)

## What it does
<a name="what-it-does"></a>

**Generates solution content from your existing assets.** Import information from a website URL, a PDF, a case study, or product documentation, and AI-assisted solution listing drafts your solution details.

**Rates your solution against the AWS Marketplace solution quality rubric.** Your listing quality indicates where your listing stands relative to the standards that drive buyer engagement. Recommendations are field-level, so each one names the field it applies to.

**Writes for discoverability.** Recommendations are generated against AWS Marketplace listing standards, AWS Marketplace search ranking signals, and search engine optimization (SEO) and generative engine optimization (GEO) guidance. Your solution content is read by AWS Marketplace search, Agent Mode, and the Solutions Matching Engine, so recommendations target the vocabulary customers actually search. For more information, see [Optimizing your AWS Marketplace products for search](search-engine-optimization.md).

**Recommends the use cases to cover.** AI-assisted solution listing reads opportunities you have already closed and recommends use cases based on them.

**Flags duplicate solutions.** It checks each solution against your product listing and against your other solutions, and flags any that duplicate them. See [How duplicate detection works](#duplicate-detection).

**Attaches your case studies.** Each case study does two jobs: it shows a customer what you delivered for customers like them, and it tells AWS Marketplace which use cases your solution solves. The use case is what search matches against the customer's query.

## Prerequisites
<a name="prerequisites"></a>
+ An AWS account linked to AWS Partner Central.
+ The `AWSMarketplaceSellerFullAccess` permission, or equivalent.
+ At least one product, because every solution requires a product behind it. For how to decide what to create, see [Deciding what to list in AWS Marketplace](deciding-what-to-list.md).

## Creating a solution
<a name="creating-a-solution"></a>

**To create a solution with AI-assisted solution listing**

1. Sign in to the AWS Partner Central console at `https://us-east-1.console.aws.amazon.com/partnercentral/home`.

1. In the left navigation pane, under **Build**, choose **Solutions**.

1. Choose **Create solution**.

1. On the first step, choose **Generate with AI** and provide a source: a website URL, an uploaded document, or a text description of the solution. AI-assisted solution listing drafts your solution details from it.

1. On the second step, review the drafted fields. For each field you can:
   + Choose **Apply** to accept the recommendation.
   + Choose **Refine with AI** to generate an alternative.
   + Edit the field directly.
   + Choose **Dismiss** to decline the recommendation.

   To get recommendations for every field at once rather than field by field, choose **Ask listing assistant**.

1. On the third step, add your use cases. Choose **Generate use case details** to have AI-assisted solution listing draft them, or select them yourself. Where AI-assisted solution listing has a better-matching use case, it surfaces a use-case suggestion callout that you can apply.

1. Attach your case studies and link the product that delivers the solution.

1. Publish the solution.

AI-assisted solution listing does not publish anything automatically. You review every recommendation and choose when to publish.

## Improving an existing solution
<a name="improving-an-existing-solution"></a>

A solution written before customers searched by outcome carries the vocabulary of that time. You can rate and improve a published solution without recreating it.

**To improve an existing solution**

1. Open the solution's detail page.

1. Choose the **Listing quality** tab.

1. Review the improvement groups. Each group is tiered **Required** or **Recommended**. You must complete every **Required** improvement before you can publish the solution publicly. **Recommended** improvements are not required to publish. Completing them raises your listing quality further, which improves how well customers discover your solution.

1. For a group you want to act on, choose **Start**. This takes you to the relevant page, where recommendations render inline on each field.

1. Apply, refine, edit, or dismiss each recommendation.

## Understanding listing quality
<a name="understanding-the-score"></a>

Your listing quality is a position on a four-point scale, not a numeric score:


| Position | Rating | 
| --- | --- | 
| 1 of 4 | Needs improvement | 
| 2 of 4 | Basic | 
| 3 of 4 | Strong | 
| 4 of 4 | Excellent | 

It reflects how your solution compares with the standards that drive buyer engagement.

To raise it, open the **Listing quality** tab on your solution. Improvements are grouped, and each group is marked **Required** or **Recommended**. Choose **Start** on a group to go to the page where recommendations appear inline on each field. Completing the Required groups has the largest effect.

Two values are not ratings. **Loading** appears while the rating is being read. A hyphen (**-**) appears when your solution has not been rated yet, or when the rating could not be read.

Products use the same four ratings, shown in the **Listing strength** column on the Products and services page and on the **Listing strength** tab of a product. See [Creating a product in AWS Marketplace](creating-a-product.md).

## How duplicate detection works
<a name="duplicate-detection"></a>

AI-assisted solution listing checks each solution against your product listing and against your other solutions, and flags any solution that duplicates them.

Duplicate detection is a publishing requirement, not advice. If your solution duplicates your product listing or another of your solutions, you cannot publish it until you differentiate it. AWS Marketplace search cannot reliably tell near-identical solutions apart, so it cannot return the right one for a customer's query.

Sellers often ask how many solutions to create. AWS Marketplace does not set a number. Duplicate detection makes each solution you create distinct, which removes the reason to create overlapping solutions. For the guidance on how many to create, see [Deciding how many solutions to create](deciding-what-to-list.md#how-many-solutions).

## Supported inputs
<a name="supported-inputs"></a>

You can provide content in the following ways:
+ A website URL. For best results, provide the URL of a specific page rather than a generic landing page.
+ An uploaded document.
+ A direct text description in the chat.

You can combine these in a single conversation. For example, provide a website URL and then upload a case study to enrich the recommendations.

### How your uploaded content is used
<a name="supported-inputs-how-content-used"></a>

When you upload a document, the file is stored in an AWS Marketplace-managed storage location scoped to your seller account. The content is used only to inform recommendations for your listing. Files are not used to train models and are not shared with other AWS Marketplace sellers.

If the sources you provide do not contain enough information to complete a field, AWS Marketplace supplements them with third-party information about your product where it is available, such as your G2 profile. Fields drafted this way name the sources they came from, so you can see the origin of the content and edit it.

## Programmatic access
<a name="programmatic-access"></a>

You can reach the same capabilities programmatically through the [Partner Agent MCP server](https://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-getting-started.html).

## Frequently asked questions
<a name="solution-faqs"></a>

### Does AI-assisted solution listing publish my solution automatically?
<a name="sl-faq-publish-automatically"></a>

No. It generates content and recommendations. You review each one, apply or edit or dismiss it, and choose when to publish.

### My solution is already public. Do I need this?
<a name="sl-faq-already-public"></a>

A solution written before customers searched by outcome carries the vocabulary of that time. Open the **Listing quality** tab and it reports which fields are missing or weak. See [Improving an existing solution](#improving-an-existing-solution).

### How many solutions should I create?
<a name="sl-faq-how-many"></a>

AWS Marketplace does not set a number. Create one solution for each outcome you sell to. Duplicate detection flags near-identical solutions, so creating them does not increase what customers discover. See [Deciding how many solutions to create](deciding-what-to-list.md#how-many-solutions).

### Does this help my solution get found outside AWS Marketplace?
<a name="sl-faq-external-search"></a>

Yes. Recommendations are generated against search engine optimization (SEO) and generative engine optimization (GEO) guidance as well as AWS Marketplace listing standards and AWS Marketplace search ranking signals, so the content it writes is written to be found by external search engines and AI answer engines as well as within AWS Marketplace. AWS Marketplace does not guarantee a ranking position on any external search engine. For more information, see [Optimizing your AWS Marketplace products for search](search-engine-optimization.md).

### Can I get the recommendations as a list to send to a colleague?
<a name="sl-faq-recommendations-list"></a>

Yes. Choose the **List all recommendations so I can share them with my marketing team** prompt in the listing assistant. It returns the recommended changes laid out against your existing content, formatted to paste into an email or a document.

### What happens if I leave my solution in Limited state?
<a name="sl-faq-limited-state"></a>

It stays in Limited and no customer discovers it. Linking a product and raising the solution's quality is what moves it to public. See [If you already have listings](deciding-what-to-list.md#if-you-already-have-listings).