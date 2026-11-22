

# AI-assisted product listing

AI-assisted product listing helps you create and improve AWS Marketplace product listings from your existing digital assets. It drafts content, rates your listing against the standards that drive buyer engagement, and returns recommendations on the individual fields that need work. You review each one and choose whether to accept it.

For solutions, see [AI-assisted solution listing](ai-assisted-solution-listing.md).

AI-assisted product listing is not available in AWS GovCloud (US) Regions or the China Regions.

**Topics**
+ [What it does](#what)
+ [Prerequisites](#prereq)
+ [Drafting a listing from your existing content](#drafting)
+ [Working with recommendations](#recommendations)
+ [Improving a listing you have already published](#improving)
+ [Understanding listing strength](#strength)
+ [Supported product types](#types)
+ [Supported inputs](#inputs)
+ [Programmatic access](#api)
+ [Frequently asked questions](#faq)

## What it does
<a name="what"></a>

**Drafts product content from your existing assets.** Point it at a website URL or upload a document, and it drafts your product information.

**Rates your listing.** The rating tells you where your listing stands relative to the AWS Marketplace listing standards. See [Understanding listing strength](#strength).

**Returns field-level recommendations.** Each recommendation names the field it applies to, so you can see what to change and where.

**Writes for discoverability.** Recommendations are generated against AWS Marketplace listing standards, AWS Marketplace search ranking signals, and search engine optimization (SEO) and generative engine optimization (GEO) guidance. Your listing content is read by AWS Marketplace search, Agent Mode, and the Solutions Matching Engine, so recommendations target the vocabulary buyers actually search. For more information, see [Optimizing your AWS Marketplace products for search](search-engine-optimization.md).

**Applies your own standards.** Upload your **Branding Guidelines** document and it uses it as a guardrail when generating content.

It doesn't publish anything. You review every recommendation and choose when to publish.

## Prerequisites
<a name="prereq"></a>
+ An AWS account linked to AWS Partner Central
+ The `AWSMarketplaceSellerFullAccess` permission, or equivalent

## Drafting a listing from your existing content
<a name="drafting"></a>

1. Sign in to the AWS Partner Central console and open your product from the **Products and services** page, or choose **Create product** to start a new one.

1. On the product information step, choose **Generate with AI**.

1. Provide a source: a website URL, an uploaded document, or a description of your product.

1. Review the drafted fields and work through the recommendations.

For best results with a URL, use a specific product page rather than a general landing page.

## Working with recommendations
<a name="recommendations"></a>

Recommendations appear inline on the fields they apply to. For each one, you can choose from the following controls.


| Control | What it does | 
| --- | --- | 
| **Apply** | Accepts the recommendation and writes it into the field. | 
| **Refine with AI** | Generates an alternative for that field. You can keep going by asking the listing assistant follow-up questions until the wording is right, for example *Make this shorter*, *Use the words our buyers search for*, *Lead with the outcome rather than the feature*, or *Rewrite this for a healthcare buyer*. | 
| **Dismiss** | Declines the recommendation. | 
| Edit the field directly | Your own text always wins. | 

To get recommendations across every field at once rather than field by field, choose **Ask listing assistant**.

If the recommendations need to go to a colleague rather than being applied now, choose the **List all recommendations so I can share them with my marketing team** prompt in the listing assistant. It returns them in a form you can paste into an email or a document.

## Improving a listing you have already published
<a name="improving"></a>

A listing written before buyers searched the way they do now carries the vocabulary of that time. You can rate and improve a published product without recreating it.

1. Open the product from the **Products and services** page.

1. Choose the **Listing strength** tab.

1. Review the improvement groups.

1. For a group you want to work on, choose **Start**. This opens the page where that group's fields live, with recommendations inline.

1. Apply, refine, edit, or dismiss each recommendation.

Improvement groups cover product details, use cases, case studies, promotional media, engagement options, free trial, and quick launch.

## Understanding listing strength
<a name="strength"></a>

Listing strength is a position on a four-point scale, not a numeric score. The following table shows the ratings.


| Position | Rating | 
| --- | --- | 
| 1 of 4 | Needs improvement | 
| 2 of 4 | Basic | 
| 3 of 4 | Strong | 
| 4 of 4 | Excellent | 

Two values are not ratings. **Loading** appears while the rating is being read. A hyphen (**-**) appears when a product has not been rated yet, or when the rating could not be read.

Your rating also appears in the **Listing strength** column on the **Products and services** page, so you can see your whole portfolio at once. See [Creating a product in AWS Marketplace](creating-a-product.md).

To raise a rating, work the groups marked **Required** first. They have the largest effect.

**Notes**
+ You cannot sort the **Listing strength** column. Ratings are read after the rows load, so the order would change as they arrive.
+ If every row in that column shows a hyphen, your account might not be enabled for listing assessment. Contact AWS Marketplace Seller Operations on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1) in the AWS Partner Central console.

## Supported product types
<a name="types"></a>
+ SaaS products
+ Server products, both AMI and container
+ Machine learning products
+ Data products on AWS Data Exchange
+ AI agents and tools, both SaaS API-based and container-based
+ Professional services products
+ Solutions. See [AI-assisted solution listing](ai-assisted-solution-listing.md).

## Supported inputs
<a name="inputs"></a>
+ A product website URL.
+ An uploaded document.
+ A description typed directly into the chat.

You can combine these. For example, provide a URL and then upload a one-pager to enrich the recommendations.

### How your uploaded content is used
<a name="inputs-how-content-used"></a>

Uploaded files are stored in an AWS Marketplace-managed location scoped to your seller account. The content is used only to inform recommendations for your listing. Files are not used to train models and are not shared with other AWS Marketplace sellers.

If the sources you provide do not contain enough information to complete a field, AWS Marketplace supplements them with third-party information about your product where it is available, such as your G2 profile. Fields drafted this way name the sources they came from, so you can see the origin of the content and edit it.

## Programmatic access
<a name="api"></a>

The same capabilities are available through the [Partner Agent MCP server](https://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-getting-started.html).

## Frequently asked questions
<a name="faq"></a>

### Does AI-assisted product listing publish my listing automatically?
<a name="pl-faq-publish-automatically"></a>

No. It drafts content and returns recommendations. You review each one, apply or edit or dismiss it, and choose when to publish.

### Can I still use it from the assistant chat?
<a name="pl-faq-assistant-chat"></a>

Yes. For more information, see [AWS Partner Central Agents](partner-assistant.md).

### What happens to my data when I upload a document?
<a name="pl-faq-data-upload"></a>

See [How your uploaded content is used](#inputs-how-content-used).

### Why is my product's listing strength a hyphen?
<a name="pl-faq-strength-hyphen"></a>

Either it has not been rated yet, or the rating could not be read. A new or newly updated product is rated after you save it; refresh the page to pick up the rating. If the hyphen persists, or if every product shows a hyphen, your account might not be enabled for listing assessment. Contact AWS Marketplace Seller Operations on the AWS Partner Central and Marketplace Support page in the AWS Partner Central console.