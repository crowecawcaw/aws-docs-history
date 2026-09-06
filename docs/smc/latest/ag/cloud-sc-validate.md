

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Service Catalog integration in Jira Service Management Cloud
<a name="cloud-sc-validate"></a>

 This section describes how you can use service integration features to validate AWS Service Management Connector for Jira Service Management Cloud installation. 

****To order a Service Catalog product using the Jira Customer Portal****
**Note**  
You can only order a Service Catalog product using the Jira Customer Portal if you have enabled Jira projects for the connector and added the Service Catalog request form to the portal. For more information about the Service Catalog request form, review [Enable the AWS Service Catalog Request Type in Jira Customer Portal](customer-portal.md). 

1. Log in to your Jira Service Management Customer Portal. 

1. Select the portal group that corresponds with the Service Catalog request form. 

1. Select the product you want to provision. 

1. Enter the product request details, including the **product reference name**, **parameters**, and **tags**. 

1. Choose **Send** to submit the JSM request and provision the Service Catalog product. 

When the product is ready to provision, users receive a notification that the product is launching. 

****To view provisioned products using the Jira Customer Portal****

1. Log in to your Jira Service Management Customer Portal. 

1. Choose **Requests** at the top right corner. 

1. Select the desired provisioned product to open the issue. 

1. Review the provisioned product details, including the **Status** of the product request, **Product events**, **Activities**, and any available **Self-service actions**. 

**To perform post-provisioning actions**

1. Log in to your Jira Service Management Customer Portal. 

1. Choose **Requests** at the top right corner. 

1. Select a **service action** from the Self-service actions list, and then choose **Execute**. 

When the product is in the `Available` status, internal customers and Jira agents can request post-provision operations, including **Request update** and **Request termination** from the **Actions** menu at the top right corner of the Issues page. 

****To order a Service Catalog product using the Jira Agent view****

1. Log in to the Jira Service Management agent view as the internal customer or Jira agent. 

1. Open the Jira project and navigate to apps **AWS Service Catalog - Order Product**. 

1. Select a product to provision. 

1. Fill in the product request details, including the product reference name, parameters, and tags. 

1. Choose **Order** to submit the Jira Service Management request and provision the AWS Service Catalog product

1. After the request processes, a message appears indicating that your request was created. When the product is ready to provision, the internal customers or Jira agents receives a notification that the product is launching.

****To view provisioned products using the Jira Agent view****

1. Log in to your Jira Service Management Agent View as the internal customer or Jira agent. 

1. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/) to show only issues with the Issue Type **AWS Service Catalog Request**. 

1. Open a Jira issue.

1. Choose the **AWS Service Catalog** panel. 

1. Review the AWS provisioned product details, including the status of the product request, product events, activities, and available Self-Service Actions. 

1. If Self-Service Actions are available, you can select a service action from the list, and then choose **Execute**. 

1. After the product is in the `Available` status, internal customers and Jira agents can request post-provision operations including **Request update** and **Request termination** from the **Actions** menu at the top right corner of the issue page. 