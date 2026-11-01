

# Finding guides in AWS Partner Central
<a name="guides"></a>

Use **Guides** in AWS Partner Central to find AWS Partner content in one place. The content covers topics such as AWS Partner Network programs, benefits, co-selling with AWS, AWS Marketplace, and AWS services. You can browse the content by category, search for it, read guides in the console, and download resources to use in your own work.

**Topics**
+ [Content types](#guides-content-types)
+ [Who can access content](#guides-access)
+ [Finding guides and resources](#guides-find)
+ [Reading a guide](#guides-read)
+ [Downloading a resource](#guides-download)

## Content types
<a name="guides-content-types"></a>

**Guides** contains two types of content:

Guides  
Articles that you read in AWS Partner Central. A guide can include images and links to other guides and categories.

Downloadable resources  
Files, such as presentations, documents, and templates, that you download and use outside of AWS Partner Central.

AWS groups guides and downloadable resources by category. Each category contains topics, and some topics contain more specific subtopics.

## Who can access content
<a name="guides-access"></a>

Most guides and resources are available to all AWS Partners. Some content is available only to partners that participate in a specific AWS Partner program:
+ AWS Solution Provider Program
+ AWS Distribution Program

If your organization doesn't participate in one of these programs, the content for that program doesn't appear when you browse or search.

### Required permissions
<a name="guides-permissions"></a>

To use **Guides**, your IAM role must have permission to view AWS Partner Central content. You can grant this permission in either of the following ways:
+ Attach an AWS managed policy for AWS Partner Central that includes access to Guides, such as `AWSPartnerCentralFullAccess`, `AWSPartnerCentralOpportunityManagement`, `AWSPartnerCentralChannelManagement`, `AWSPartnerCentralMarketingManagement`, or `PartnerCentralIncentiveBenefitManagement`. For more information, see [AWS managed policies for AWS Partner Central users](https://docs.aws.amazon.com/partner-central/latest/getting-started/managed-policies.html).
+ Create a customer managed policy that grants access only to AWS Partner Central content. The following example policy grants permission to search, list, and view AWS Partner Central content.

  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "PartnerCentralContentAccess",
        "Effect": "Allow",
        "Action": [
          "partnercentral:GetPartnerCentralContentDocument",
          "partnercentral:GetPartnerCentralContentMetadata",
          "partnercentral:ListPartnerCentralContent",
          "partnercentral:SearchPartnerCentralContent"
        ],
        "Resource": "*"
      }
    ]
  }
  ```

## Finding guides and resources
<a name="guides-find"></a>

Use the **Guides** page to browse by category, search by keyword, see recently updated content, and return to content that you opened before.

### Browsing by category
<a name="guides-browse"></a>

Browse by category to find the guides and resources for a topic.

**To browse guides and resources**

1. Sign in to the [AWS Partner Central console](https://console.aws.amazon.com/partnercentral).

1. In the navigation pane, choose **Guides**.

1. In the **Explore topics** section, choose a category, such as **Funding Benefits for AWS Partners**. To show the topics in every category, choose **All**.

1. Choose a topic, such as **Get started**. The first guide in the topic opens.

1. To open another guide in the topic, choose it in the navigation pane on the left.

1. To return to the **Guides** page, choose **Guides** in the breadcrumb at the top of the page.

**Tip**  
To share a guide or resource, open it and choose **Copy URL**. You can also bookmark the page in your browser.

### Searching by keyword
<a name="guides-search"></a>

Search to find guides and resources by keyword across all categories that you have access to.

**To search guides and resources**

1. On the **Guides** page, enter one or more keywords in the search box, and then press Enter.

1. Review the results. Each result shows the title, description, content type, category, and last updated date. The number of matches appears next to the filters.

1. (Optional) To narrow or reorder the results, use the following options:
   + **Sort by**: Choose **Relevance** or **Most recent**.
   + **Category**: Select one or more categories. To find a category in the list, enter its name in the search box at the top of the list.
   + **Availability**: Choose **Downloadable** to show only downloadable resources. Choose **All** to show guides and downloadable resources.

1. If the results span more than one page, use the page numbers at the top of the results to see more.

1. Choose a result to open the guide or to view the resource details.

To ask a question in your own words, enter it in the search box, and then choose the generative AI icon next to the search icon. A chat with Partner Central agents opens with your question so that you can explore the answer in more detail.

### Viewing recently updated content
<a name="guides-recently-updated"></a>

The **Recently updated** section on the **Guides** page shows guides and resources with recent changes that are relevant to your organization.

Each item shows its title, description, and last updated date. Downloadable resources also show their file format, such as PDF or PPT.

To open an item, choose its title. To see all recently updated content, choose **View all**. The search results page opens with a list of recently updated guides and downloadable resources. To narrow the list, use the **Category** and **Availability** filters.

### Returning to recently visited content
<a name="guides-recently-visited"></a>

To return to a guide or resource that you opened before, choose the search box on the **Guides** page. Before you enter any keywords, a **Recently visited** list appears.

Each item in the list shows its category. Downloadable resources show their file format instead. Choose an item to open it.

## Reading a guide
<a name="guides-read"></a>

When you open a guide, AWS Partner Central displays the full guide, including its images. The page also shows the following:
+ The categories that contain the guide, so you can browse related content.
+ The last updated date of the guide.
+ An **On this page** panel with links to each section of the guide, so you can go directly to the section that you need.

Links inside a guide can open another guide, a downloadable resource, or a category in **Guides**.

## Downloading a resource
<a name="guides-download"></a>

**To download a resource**

1. Browse or search for the resource, and then choose it to view its details.

1. If the resource is available in more than one language, choose the language that you want.

1. Choose **Download**.

1. In the **Download terms** dialog box, review the terms, and then choose **Acknowledge and download**.

**Important**  
Downloaded documents are confidential and intended only for your organization. Don't share them outside your organization. Sharing them can result in loss of access to partner resources.

**Note**  
For security, each download link expires shortly after AWS Partner Central creates it. If a download doesn't start, return to the resource and choose **Download** again.