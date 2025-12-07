# Preparing your solution listing

## What is a solution?

A solution shows customers how multiple AWS Marketplace products work together. Solutions help customers discover and understand your complete offering.

## Prerequisites

Before creating a solution, make sure you have:

1. Active AWS Partner Network (APN) membership.
2. ACE (APN Customer Engagement) eligibility to enable **Request private offer** and receive leads.
3. At least two public product listings on AWS Marketplace. At least one public product must be your own.
4. For solutions that include other sellers' products:
   1. Consent from other sellers to include their products in your solution listing
   2. Selling authorization from other sellers if you plan to resell their products in transactions

## Define your solution strategy

Before you start, consider these key questions:

- **Customer problem**: What specific business challenge does your solution address?
- **Product integration**: How do your products work together to solve the customer's problem?
- **Target use cases**: Which industries or scenarios benefit most from your solution?
- **Value proposition**: What unique benefits does your bundled solution provide compared to purchasing products individually?

## Common solution applications

Create solutions for these business models:

- **ISV service package**: Combine your software products with professional services (such as SaaS with implementation services)
- **Channel partner reselling**: Bundle your services with authorized ISV products you resell
- **Multi-partner solutions**: Create comprehensive solutions using products from multiple AWS Partners
- **Renewal upselling**: Offer solutions that combine renewed products with new capabilities
- **Hybrid deployment**: Package solutions where some components run on AWS while others run elsewhere (such as on-premises)

## Supported product types

Include these AWS Marketplace product types in your solution:

- SaaS (Software-as-a-Service)
- Amazon Machine Image (AMI)
- Container products
- Professional services
- Machine Learning
- AI agents

###### Note

Solution listings do not currently support Amazon Data Exchange (ADX) products.

## Creating a solution listing

Solution listings provide customers with a dedicated page to discover and understand your multi-product offering.

### Getting started

To create a solution listing:

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/partners/management-tour "https://aws.amazon.com/marketplace/partners/management-tour") with your seller credentials, or go directly to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/dashboard?region=us-east-1 "https://us-east-1.console.aws.amazon.com/partnercentral/dashboard?region=us-east-1").
2. Go to [Solutions](https://us-east-1.console.aws.amazon.com/partnercentral/solutions "https://us-east-1.console.aws.amazon.com/partnercentral/solutions") on the left-hand navigation pane.
3. Choose **Create solution** to begin.

###### Note

If you have existing data in legacy Partner Central, you must migrate your partner solutions data to new AWS Partner Central and AWS Marketplace catalog before creating new solutions.

### Step 1: Enter solution details

Complete the following information about your solution:

- **Solution name** (1-100 characters): Create a clear, descriptive name that represents your multi-product solution.
- **External solution title** (1-255 characters): The solution title that buyers see if you list your solution on AWS Marketplace. It can be the same as the solution name, or something different.
- **Value proposition** (1-1,000 characters): Articulate what differentiates your solution and why customers should choose it.
- **Long description** (1-5,000 characters): Explain the comprehensive value your solution delivers to customers.
- **Integration details**: Write a 2-3 sentence overview explaining how the products in your solution integrate or work together. This helps customers understand the technical and functional relationships between components.
- **Solution logo**: Upload a solution-specific logo or your company logo. Supported formats: PNG, JPG, or GIF. Maximum 5MB. Size: 240x120 to 640x640 pixels. We recommend square (1:1) or wide (2:1) aspect ratios with transparent or white backgrounds.

###### Tip

Focus on customer outcomes rather than product features. Use clear, simple language that your target audience understands. Provide specific examples of customer-focused language that highlight the benefits of using the products together.

### Step 2: Add products to your solution

Add products using one of these methods:

#### AWS Marketplace products you own

1. Select the product type.
2. Select from public or limited products owned by your AWS Marketplace account.

#### AWS Marketplace products owned by others

1. Obtain the Product ID from the product owner.
2. Enter the Product ID. The system validates this is a public product listing on AWS Marketplace.

###### Note

This must be the Product ID from AWS Marketplace Management Portal, AWS Partner Central, or AWS Marketplace catalog API. Do not use the Listing ID from the website that starts with prodview-. Products not owned by this account must be public or targeted to this account, if limited.

#### Non-AWS Marketplace products

1. Choose this if the solution includes external or custom products.
2. Select the product type and enter details manually.
3. Add a description (1-220 characters) and URL for each non-AWS Marketplace product.

### Step 3: Choose use cases

You must choose at least one use case (maximum of three) to publish your solution to the AWS Marketplace catalog.

1. Search the predefined use cases using keywords.
2. Choose up to 3 use cases that best match your solution.
3. For each chosen use case, write a description (1-500 characters) explaining how your solution addresses that specific customer need. This description appears to buyers on the public listing page.

### Step 4: Review and submit

1. Review all solution details on the summary page.
2. The system validates that all required fields and relationships are set.
3. Once submitted, the solution changes from Draft to Limited status. Limited status means your solution is visible to you but not yet public to customers. You can still make edits to the solution while it's in Limited status.
4. Choose **Preview in AWS Marketplace** to see how your solution will appear to customers.

## Solution overview page

This page shows your solution details and provides update options. To update your solution, choose the edit button for the area you want to edit.

The page includes:

- **Summary**: status, solution ID, ARN, last modified.
- **Overview tab**: solution detail, buyer engagement options, additional resources, images and videos, tags.
  - For a detailed guide on adding images and videos, see [Enhance your AWS Marketplace product with promotional media](promotional-media.md "promotional-media.md").
  - AWS lets buyers with unique or enterprise use cases request a private offer for your product directly from the product detail page. If you are an AWS Partner Network (APN) partner who is eligible for [APN Customer Engagements (ACE)](https://aws.amazon.com/partners/programs/ace/ "https://aws.amazon.com/partners/programs/ace/") and you would like to offer this option to buyers, see [Adding private offer and demo request buttons](creating-private-offer.md#private-offer-requests-demos "creating-private-offer.md#private-offer-requests-demos") for more information.

- **Products tab**: AWS Marketplace products, non-AWS Marketplace products, integration guide.
- **Use cases**: list of use cases and details.
- **Offer sets**: list of offer sets connected to this solution for tracking.
- **Change history**: log of changes made to the solution.

## Making your solution public

To make your solution public, choose **Update Visibility** in the upper right of the overview page. By default, the system enables the **Request private offer** button for all solutions going public to ensure customers can engage with the seller. Your solution must meet all criteria below. After you submit your request, the AWS Marketplace seller operations team will review and approve or reject it.

Requirements:

- Include at least two public AWS Marketplace products. Solutions cannot include draft, limited, or restricted products.
- At least one public product must be owned by your own account.
- At least one use case must be chosen.
- You must enable **Request private offer**.
- If your solution includes products from other AWS Marketplace sellers, confirm the following:
  - You coordinated with the product owner to obtain product IDs.
  - The product owner is ready to provide selling authorization to create channel partner private offers.
  - You obtained consent from the product owner to showcase their product in your public solution listing.

- No more than five public solutions live on AWS Marketplace.
