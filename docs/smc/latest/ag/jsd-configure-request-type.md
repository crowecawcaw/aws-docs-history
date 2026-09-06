

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring project request type groups
<a name="jsd-configure-request-type"></a>

The AWS request type must be in a group for users to be able to access it in Jira Service Management. Enabling Jira projects, as described in [Configuring Connector Settings (Jira Project Enablement and Request Type)](jsd-configure-connector.md), makes AWS product request types available, but Jira Service Management users won't see the request type until you add it to a **Request Type Group**.

**To configure request types**

1. In the AWS Service Management Connector for Jira Service Management, go to the **Connector settings ** page.

1. In the **Projects** section, choose **add the AWS request type**.

1. Choose **Add existing request type** in the upper right-hand corner.

1. Choose **Request AWS product** from the available request type.

1. Choose **Edit Groups** for the **Request AWS product** request type.

1. On the **Edit groups** form, choose **General**, then choose **Save**.

**Note**  
When you create a custom **Request AWS Product** request type for the Connector for Jira Service Management, you do not need to edit to the **Request AWS Product** request type. You can add a request type to an existing group. If you don't have a group, create a new group and add the request type to it.