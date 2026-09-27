

# Managing Resolver on Outpost
<a name="outpost-resolver-manage"></a>

How you manage Resolver on Outpost depends on your AWS Outposts generation:
+ For first-generation AWS Outposts, you can edit, view, and delete Resolver.
+ For second-generation AWS Outposts, you can't edit or delete Resolver. You can only view it.
+ If you don't want to use Resolver with second-generation AWS Outposts, you must contact [AWS Support](https://console.aws.amazon.com/support/home) to opt out.
+ If Resolver fails on second-generation AWS Outposts, AWS contacts you to help resolve the issue.

**Topics**
+ [Editing Resolver on Outpost (first-generation AWS Outposts only)](#outpost-edit-resolver)
+ [Viewing Resolver on Outpost status](#outpost-view-resolver-status)
+ [Deleting Resolver on Outpost (first-generation AWS Outposts only)](#outpost-delete-resolver)

## Editing Resolver on Outpost (first-generation AWS Outposts only)
<a name="outpost-edit-resolver"></a>

To edit a Resolver on Outpost, perform the following procedure.<a name="resolver-outpost-resolver-managing-edit-procedure"></a>

**To edit a Resolver on Outpost**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the left navigation pane, expand **Resolver**, and then navigate to **Outposts**.

1. On the navigation bar, choose the Region where your AWS Outposts is located.

1. Select the checkmark next to the VPC Resolver that is in operational state and choose **Edit**. 

1. You can edit the following information:
   + The VPC Resolver name
   + The instance type
   + The number of instances

1. After you are done editing, choose **Save changes**.

## Viewing Resolver on Outpost status
<a name="outpost-view-resolver-status"></a>

To view the status for Resolver on Outpost, perform the following procedure.<a name="resolver-outpost-viewing-status-procedure"></a>

**To view the status for an inbound endpoint**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the left navigation pane, expand **Resolver**, and then navigate to **Outposts**.

1. On the navigation bar, choose the Region where your AWS Outposts is located.

1. Select the checkmark next to the VPC Resolver that is in operational state and choose **View details**. 

1. The **Status** column in the **Resolver on Outpost** page, contains one of the following values:  
**Creating**  
The Resolver on Outpost is in the process of being created.  
**Operational**  
The Resolver on Outpost is correctly configured.  
**Updating**  
The Resolver on Outpost is updating instance types.  
**Action needed**  
This VPC Resolver is unhealthy and can't be automatically recovered. To resolve the problem, we recommend that you make sure the instance AWS Outposts can support Resolver on Outpost.  
**Deleting**  
The Resolver on Outpost is in the process of being deleted.  
**Failed creation**  
The creation of Resolver on Outpost failed.  
**Failed deletion**  
The deletion of Resolver on Outpost failed. To fix this issue, try again in a few minutes.

## Deleting Resolver on Outpost (first-generation AWS Outposts only)
<a name="outpost-delete-resolver"></a>

**Note**  
Before you can delete a Resolver on Outpost, you must first delete any endpoints associated with it.

To delete a Resolver on Outpost, perform the following procedure.<a name="resolver-outpost-delete-procedure"></a>

**To delete a Resolver on Outpost**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the left navigation pane, expand **Resolver**, and then navigate to **Outposts**.

1. On the navigation bar, choose the Region where your AWS Outposts is located.

1. Select the check box next to the VPC Resolver that is in operational state and choose **Delete**. 

1. In the **Delete VPC Resolver** dialog box, enter **delete** in the text box, and choose **Delete**.