

# AI-assisted product listing
<a name="ai-assisted-product-listing"></a>

AI-assisted product listing is a capability in AWS Partner Assistant. It helps you create high-quality AWS Marketplace product listings of all product types from your existing digital assets.

Any seller with the `AWSPartnerCentralFullAccess` permission can access this capability through the AWS Partner Assistant chat window.

With AI-assisted product listing, you can:
+ Generate product information from a website URL or uploaded documents (PDFs, case studies, product documentation).
+ Score the strength of any product listing against AWS Marketplace standards.
+ Receive field-level recommendations for product information to improve listing quality and buyer discoverability before publishing.
+ Apply your own brand voice or listing standards by uploading a style guide that the chat uses as a guardrail when generating product information.

**Topics**
+ [How to access AI-assisted product listing](#how-to-access-ai-assisted-product-listing)
+ [What you can ask the chat](#what-you-can-ask-chat)
+ [Supported product types](#supported-product-types)
+ [Supported input modalities](#supported-input-modalities)
+ [Search and discoverability optimization](#search-and-discoverability-optimization)
+ [Programmatic access](#programmatic-access)
+ [Frequently asked questions](#ai-assisted-product-listing-faq)

## How to access AI-assisted product listing
<a name="how-to-access-ai-assisted-product-listing"></a>

You can access AI-assisted product listing in two locations:

1. Sign in to AWS Partner Central or AWS Marketplace Management Portal (AMMP).

1. Open the AWS Partner Assistant chat window:
   + In AWS Partner Central, choose the **Amazon Q** chat button in the dashboard header.
   + In AMMP, choose the **AI sparkle** icon on any product creation, update, or detail page.
   + If you are a newly registered seller, you can also access this chat through the **Create your first listing** tile.

1. Ask the agent to help you with your product listing. The agent recognizes the intent, hands off to AI-assisted product listing, and returns content you can review and copy into your AWS Marketplace listing.

Sellers complete their product listings in AMMP.

## What you can ask the chat
<a name="what-you-can-ask-chat"></a>

Use these prompts to get started:
+ "Help me build my product information from my website: [URL]"
+ "Import content from this document for my SaaS listing" (with a PDF or supported file attached)
+ "Score the quality of my listing"
+ "How can I improve my listing quality?"
+ "Make my listing more discoverable"
+ "Apply my brand voice to my listing" (with a style guide attached)
+ "What makes a strong AWS Marketplace listing?"

## Supported product types
<a name="supported-product-types"></a>

AI-assisted product listing is available for the following product types:
+ SaaS products
+ Server (AMI and container) products
+ Data products on AWS Data Exchange
+ Machine learning products
+ AI agents and tools (SaaS API-based and container-based)
+ Professional services products

## Supported input modalities
<a name="supported-input-modalities"></a>

You can provide content to AWS Partner Assistant in the following ways:
+ A product website URL. For best results, provide the URL of a specific product page rather than a generic landing page.
+ An uploaded document. Supported file types include PDF, DOCX, XLSX, CSV, and image files.
+ A direct text description of your product in the chat.

You can combine these inputs in a single conversation. For example, you can provide a website URL and then upload a one-pager to enrich the recommendations.

## Search and discoverability optimization
<a name="search-and-discoverability-optimization"></a>

AWS Partner Assistant generates product information recommendations based on AWS Marketplace standards, search ranking signals, and search engine optimization (SEO) and generative engine optimization (GEO) guidance.

For more information about how AWS Marketplace ranks search results and how to optimize your product detail page for discoverability, see [Optimizing your AWS Marketplace products for search](search-engine-optimization.md).

## Programmatic access
<a name="programmatic-access"></a>

You can also access the same capabilities programmatically through the Partner Central agents MCP Server. For more information, see [Partner Central agents MCP Server](https://docs.aws.amazon.com/partner-central/latest/APIReference/partner-central-mcp-server.html) in the *AWS Partner Central API Reference*.

## Frequently asked questions
<a name="ai-assisted-product-listing-faq"></a>

### Does AI-assisted product listing publish my listing automatically?
<a name="faq-does-ai-listing-publish-automatically"></a>

No. AWS Partner Assistant generates listing content and recommendations. You review the content, copy and paste it into the listing input/update page, make any adjustments, and choose when to publish.

### What happens to my data when I upload a document?
<a name="faq-data-when-upload-document"></a>

When you upload a document to AWS Partner Assistant, the file is stored in an AWS Marketplace-managed storage location. This location is scoped to your seller account. The agent uses your uploaded content only to inform its recommendations. These files are not used to train models or shared with other AWS Marketplace sellers. You can upload up to 3 files per message and up to 5 total files against a listing. Supported formats are PDF, DOCX, DOC, XLSX, JPEG, and PNG, with a maximum size of 4.5 MB per document and 3.75 MB per image. Examples include product datasheets, solution briefs, case studies, and technical whitepapers. PowerPoint (PPTX) is not supported at this time. Convert decks to PDF before uploading.

Two important guidelines:
+ Do not upload files containing credentials, secrets, or other sensitive information. While storage is ephemeral, sensitive data should not be passed through the agent at all.
+ You can review and remove generated content before publishing. AI-generated content is shown in the chat for your review; nothing is published to your AWS Marketplace listing without your explicit action.

### Does AI-assisted product listing replace the AWS Marketplace product review process?
<a name="faq-replace-product-review"></a>

No. Listings created or updated using AI-assisted product listing follow the same AWS Marketplace product review process as listings created manually.

### Can I provide my company's brand voice to the agent?
<a name="faq-provide-brand-voice"></a>

Yes. Upload a brand voice or style guide document, and the agent uses those rules as a guardrail when generating listing content.