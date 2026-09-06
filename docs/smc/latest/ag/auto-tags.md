

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring automated tags for AWS Service Catalog
<a name="auto-tags"></a>

The AWS Service Management Connector v1.9.0 enables Jira administrators to add tags (metadata) to AWS Service Catalog provisioned products globally across the add-on or granularly at the portfolio level. These tags are not visible to end users.

Two tag types are available in this release:
+ Generic tags in which the admin can enter the key and value.
+ AWS Service Catalog Request Type tags in which the admin can enter the following syntax for key and value:


**AWS Service Catalog Request Type tags**  

|  |  | 
| --- |--- |
| Key | Value | 
| Project Code | ${PROJECT\_CODE} | 
| Project Name | ${PROJECT\_NAME} | 
| Project Name | ${ISSUE\_ID} | 
| Username | ${USERNAME} | 
| Opened By | ${OPENED\_BY} | 

**To add generic AWS tags to AWS Service Catalog provisioned products in Jira Service Management**

1. In the left navigation menu, under **AWS Service Management**, select **Automated Tags**.

1. For Global level tags, enter the Key and Value entries. Under **Portfolio**, select** Global** (set by default). Choose the **\+** icon to insert.

1. For Portfolio level tags, enter the Key and Value entries. Under **Portfolio**, select the Portfolio dropdown to choose the portfolio associated to associate tag. Choose the **\+ **icon to insert.

**To add in-scope request type AWS tags to AWS Service Catalog provisioned products derived from Jira Service Management**

1. In the left navigation menu, under **AWS Service Management**, choose **Automated Tags**.

1. For Global level tags, enter the Key and Value entries. Under **Portfolio**, select** Global** (set by default). Select the **\+** icon to insert.

1. For Portfolio level tags, enter the Key and Value entries. Under **Portfolio**, select the Portfolio dropdown to choose the portfolio to associate with the tag. Choose the **\+** icon to insert.

   After the product provisions, you can see in the AWS console that these tags are associated to the resource.