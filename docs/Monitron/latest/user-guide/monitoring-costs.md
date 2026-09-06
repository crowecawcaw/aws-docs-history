

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Monitoring costs
<a name="monitoring-costs"></a>

Amazon Monitron assigns [AWS–generated tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html) to each sensor: a project tag and a site tag. If you use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), you can use these assigned tag values to get cost reports filtered to specific Amazon Monitron projects and sites.

**Topics**
+ [Conceptual overview](#monitoring-use-case)
+ [Billing tag keys and tag values](#billing-tag-values)
+ [Retrieving project tag values](#retrieving-tag-values-project)
+ [Retrieving site tag values](#retrieving-tag-values-site)
+ [Activating billing tags](#using-billing-tags)
+ [Viewing cost reports](#viewing-cost-reports)

## Conceptual overview
<a name="monitoring-use-case"></a>

When you set up Amazon Monitron, you create a project in which you configure and install your Amazon Monitron resources. Every project, in turn, can be linked to mutliple sites, or organized collections of assets, gateways, and sensors linked together based on either a common location or function. 

Each site can contain multiple Amazon Monitron sensors, attached to multiple assets or machines, transmitting the asset data collected through multiple gateways.

While all your sites, assets, gateways, and sensors exist conveniently within one project, your Amazon Monitron setup might be more distributed in practice. For example, your company may own one project to monitor sites located in different geographical locations, or grouped together by different business use cases and needs. Or you may own multiple projects, each with its own specific configuration. Partners who integrate Amazon Monitron, may also wish to assign a project to each of their own customers 

 While getting an overall understanding of your Amazon Monitron costs is useful, what your business may need is a more granular understanding of the usage and costs attached to each project, location, or business use case. This may also be necessary for internal cost allocation purpose between different divisions.

In these situations, using Amazon Monitron assigned [AWS–generated tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html) in [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) can help you understand and plan your business resources better.

## Billing tag keys and tag values
<a name="billing-tag-values"></a>

Amazon Monitron uses [AWS–generated tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html) to internally assign project and site level tag values. You can use these tags to find your projects and sites on the AWS Cost Explorer console. The tag keys are of the following format:
+ **Project** – `aws:monitron:project`
+ **Site** – `aws:monitron:location_level4`

## Retrieving project tag values
<a name="retrieving-tag-values-project"></a>

You can retrieve your assigned project value using your Amazon Monitron web app. The tag value for your project is the project ID.

**To retrieve the specific tag value assigned to your Amazon Monitron project:**

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/).

1. Choose **Create Project**. 

1. In the navigation pane, choose **Projects**. 

   The list of projects is displayed under **Projects**.   
![Projects page showing Test_Project with its Project Id highlighted in the table.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/billing-tags-1.png)

1. Choose the project that you want to get details on.

1. Copy the tag value from your **Project Id**.

   You can use this project id to filter costs in AWS Cost Explorer console.

## Retrieving site tag values
<a name="retrieving-tag-values-site"></a>

You can retrieve your assigned site tag value using your Amazon Monitron web app. The tag value for your site is the Id.

**To retrieve the specific tag value assigned to your Amazon Monitron site:**

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/).

1. Choose **Create project**.

1. If you're creating a project for the first time, follow the steps outlined in [Creating a project](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-creating-project.html).

   If you're choosing an existing project, from the left navigation menu, select **Projects**, and then select the project you want to create custom asset classes for.

1. From the project details page, choose **Open in Amazon Monitron web app**.  
![Open in Monitron web app button highlighted in the project details page header.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/billing-tags-2.png)

1. From the left navigation pane, choose **Sites**. 

   The list of sites is displayed.   
![Sites page showing Site 1 in the list with its corresponding Id field highlighted.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/billing-tags-3.png)

1. Choose the site that you want to get details on.

1. Copy the tag value from your **Id**.

   You can use this id to filter costs in AWS Cost Explorer console.

## Activating billing tags
<a name="using-billing-tags"></a>

To begin using project and site level cost tracker tags, you must do the following:

1. **Prerequisite** – You must activate AWS Cost Explorer on the AWS Management Console. This requires minimal setup. We recommend you follow the steps outlined in the [AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) guide. 

1. **Activate the Amazon Monitron [AWS–generated tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html)** in your AWS billing account.

   **From your **AWS Billing and Cost Management** left navigation pane:**

   1. From **Cost Organization**, select **Cost allocation tags**. You will find the **AWS generated cost allocation tags** in this section.

   1. Select the tags you want to use and choose **Activate**.   
![Cost Allocation Tags page showing AWS generated tags tab with Activate button highlighted.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/billing-tags-4.png)
**Note**  
It takes up to 96 hours for the tags to be activated. The billing data starts being tagged only after the tags are active.

## Viewing cost reports
<a name="viewing-cost-reports"></a>

After your Amazon Monitron AWS generated tags have been activated and are active, you can view usage and cost reports filtered by these tags using AWS Cost Explorer on the AWS Cost Management console.

You can filter usage and cost history by choosing a tag key value pair. For example, if you want to view usage reports a particular project, you would first choose a tag value `aws:monitron:project` and then select the project id value from the options available.

**To generate cost and usage reports**

1. Open the AWS Cost Management console at [https://console.aws.amazon.com/costmanagement](https://console.aws.amazon.com/costmanagement).

1. From the left navigation pane, select **Cost Explorer**.

1. From the **New cost and usage report** page, from the right navigation menu, in **Filters**, choose Amazon Monitron as the **Service**. 

1. From the right navigation menu, for **Tags** choose the assigned tag key for your project or site from the dropdown options. 

1. Then, choose the Amazon Monitron assigned tag value for your project or site.  
![Cost Explorer interface showing Service and Tag filter dropdowns in the right panel.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/billing-tags-5.png)

**Note**  
You can save the report with the filters selected to the report library to easily review it later. You can also adjust and customize your report further, including the date range and granularity of your report.