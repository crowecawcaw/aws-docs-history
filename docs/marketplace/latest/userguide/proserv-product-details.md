

# Providing details for a professional services product in AWS Marketplace

When you publish a professional services product on AWS Marketplace, you must provide the product metadata. Product metadata includes product settings for visibility and pricing and product information that provide buyers with more information about your professional services product. You can edit product descriptions, additional resources, pricing dimensions, and product visibility. The following sections provide information that you can use as you prepare or edit your product details.

**Note**  
For information about guidelines and requirements for professional services products, see [Requirements for professional services products on AWS Marketplace](proserv-product-guidelines.md). 

**Topics**
+ [Product descriptions](#proserv-product-descriptions)
+ [Additional resources](#proserv-additional-resources)
+ [Support information](#proserv-support-information)
+ [Pricing dimensions](#proserv-pricing-dimensions)
+ [Product visibility](#proserv-product-visibility)

## Product descriptions
<a name="proserv-product-descriptions"></a>

**Use AI-assisted product listing**  
You can use AI-assisted product listing in AWS Partner Central Agents to generate product information for this step from a website URL or uploaded documents. The tool scores listing quality against AWS Marketplace standards and provides field-level recommendations to improve discoverability and buyer engagement before you submit. For more information, see [AI-assisted product listing](ai-assisted-product-listing.md).

The product descriptions section in the product details is the core of your product. It describes your product to your potential buyers so that they can make a purchasing decision. This section of the product details includes the following data:
+ **Product title** – The name of your product. This is used to identify your product; it's visible on the product page and within search results. Provide a meaningful name for your product. It must be unique within AWS Marketplace.

  The title can have 2 to 72 characters, using only Windows-1252 characters.
+ **SKU** – (Optional) Used to track your products on AWS Marketplace. This information is for your own use; buyers don't see it. 

  The SKU can have up to 100 characters.
+ **Short description** – A concise description of your product that appears on the tiles and underneath the product title in the AWS Marketplace product catalog. 

  The short description can have up to 1,000 characters.
+ **Long description** – A longer description that describes the details of your product to buyers. List the product features, benefits, usage, and other information specific to the product.

  The long description can have up to 5,000 characters.
+ **Product logo** – An image file that represents your product. Choose **File upload** or **Amazon S3 link**. The image must be a PNG or JPG file of up to 5 MB. It must be 120 to 640 pixels wide and tall, with a 1:1 or 2:1 (wide) ratio and a transparent or white background.

  If you don't have a logo that meets these requirements yet, choose **Use a temporary placeholder logo**. Replace it with your own logo before you make the product public.
**Note**  
The Amazon S3 URL that you provide must be publicly available. This is a property of the Amazon S3 bucket in which the file resides. For more information, see [How do I edit public access settings for Amazon S3 buckets?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/block-public-access-bucket.html) in the Amazon Simple Storage Service Console User Guide.
+ **Highlights** – A set of one to three short points about your product, describing its key features or differentiators. At least one highlight is required.

  Each highlight can have up to 500 characters.
+ **Product categories** – The types of service that you provide. You must choose at least one, and up to three, categories. There are many categories to choose from, but professional services products must include at least one of the following:  
**Assessments**  
Evaluation of the customer's current operating environment to find the right solutions for their organization.  
**Implementation**  
Help with configuration, setup, and deployment of third-party software.  
**Premium Support**  
Access to guidance and assistance from experts, designed for the customer's needs.  
**Managed Services**  
End-to-end environment management on the customer's behalf.  
**Training**  
Tailored workshops, programs, and educational tools provided by experts to help the customer employees learn best practices.
+ **Keywords for AWS Marketplace search results** – Keywords that buyers might use to search for your product. Enter 1 to 15 keywords separated by commas, each up to 50 characters.
+ **Associated products** – *optional* – Public products from AWS Marketplace that your service either works with or supports. AWS Marketplace uses these products as input when selecting products to show on your product's details page or in **Related products** for those products.

  Choose up to 10 products on the separate **Associated products** card.

## Additional resources
<a name="proserv-additional-resources"></a>

In the product details, you can provide links to resources that you have created to help your customers. This is an optional set of one to three downloadable resources that are stored online. Examples of resources include product information sheets, whitepapers, or product manuals. For each resource, provide a name and a URL for the resource.

Add resources under **Learning resources** in the **Support information** section. Each **Resource name** can have up to 500 characters, and each **Resource URL** must begin with https://.

## Support information
<a name="proserv-support-information"></a>

Use this section to describe the support that you provide for your service.

Customers expect support on issues, such as using the services, troubleshooting, and requesting refunds (if applicable). You must provide at least one of the following for your product's support: an email address, a phone number, or one or more support URLs. Include a description of the level of support buyers can expect when they purchase your product.

Enter this information in the required **Support details** field, up to 2,000 characters.

## Pricing dimensions
<a name="proserv-pricing-dimensions"></a>

Pricing dimensions for professional services are packages that you offer. For example you might offer *Silver*, *Gold*, and *Platinum* support. Or you might offer 10, 20, or 50 hours of consulting. For each dimension you want to offer (up to 200), specify a name and a description. When you create a private offer for the product by working with a buyer directly, you set the price. With **Upfront payment**, you set a price for each dimension. With **Variable payments**, you set a **Contract total** instead.

**Note**  
For information about how pricing dimensions are used, and how prices are set, see [Create private offers](proserv-getting-started.md#proserv-create-offer).

## Product visibility
<a name="proserv-product-visibility"></a>

Products can be visible in AWS Marketplace to just your own account, to a small set of test accounts, or to all AWS accounts. A new product starts with **Draft** visibility and moves to **Limited** when you choose **Advance to add-ons**. To change the product visibility, see [Edit product visibility](proserv-getting-started.md#proserv-edit-visibility).