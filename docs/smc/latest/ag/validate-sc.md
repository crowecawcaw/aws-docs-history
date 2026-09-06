

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validationg Service Catalog integration
<a name="validate-sc"></a>

 To validate Service Catalog integration, order a Service Catalog product or view provisioned products. 

**To order a Service Catalog product**

1. Log in to your Jira Service Management customer portal as the end user. 

1. In the Jira Service Management customer portal, choose **Request AWS product**.

1. Enter **Summary** details.

1. Open the **AWS product request detail** menu and select a product to provision.

1. Fill in the product request details, including product reference name, parameters, and tags.

1. Choose **Create** to submit the Jira Service Management request and provision the Service Catalog product.

1. After the request processes, a message appears indicating that your request was created. When the product is ready to provision, the end user receives a notification that the product is launching.

**To view provisioned products**

1. In the Jira Service Management customer portal, choose **Requests** in the upper right corner.

1. Choose **My Requests** in the Jira Service Management customer portal view.

1. Choose the AWS product you requested.

1. The AWS product details display, including the status of the product request, product events, and activities.

1. If that Connector feature is available, AWS Config information appears. You can expand **Configuration Items** or **Relationships** to see more information. Related resources can be loaded by continuing to expand them underneath the** Relationships** section.

1. Once the product is in the **Available** status, end users can request post-provision operations actions such as **Request update**, **Request termination**, and **Request self-service actions**. These actions render additional product events and activities within the request. Once the product terminates, the request closes in a resolved state.