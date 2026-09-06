

# Identify your cross-account resources in Global Accelerator
<a name="cross-account-resources.identify-cross-account"></a>

Resource owners and principals can identify shared resources by using the AWS Global Accelerator console or by using the AWS CLI with Global Accelerator operations. For example, you can do the following:
+ As an owner, you can see a list of your cross-account attachments, and view the principals and resources in each attachment.
+ As a principal, you can view all cross-account attachments that you're listed in, and you can list the resources that you can add as endpoints or IP address ranges for an accelerator, for a specific attachment.

For more information about using API operations to view cross-account attachments and shared resources, see [AWS Global Accelerator API Reference Guide](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

## As an owner: Identify your cross-account resources in Global Accelerator
<a name="cross-account-resources.identify-cross-account-owner"></a>

As an owner, you can view your cross-account attachments in the AWS Management Console, or by using the AWS Command Line Interface with Global Accelerator API operations.

## To see your cross-account attachments

+ In the Global Accelerator console, choose **Cross-accounts attachments**.

## To see the information included in a cross-account attachment


1. In the Global Accelerator console, on the **Cross-accounts attachments** page, choose an attachment, and then choose **View details**.

   —OR—

1. Use the API operation [ListCrossAccountResources](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCrossAccountResources.html), for example, by using the AWS Command Line Interface. This operation returns a list of unique attachment-resource pairs, for every resource, in every attachment, in the account.

   For example, if you have two cross-account attachments, and the first includes two endpoints and a CIDR block, while the second includes three endpoints, `ListCrossAccountResources` returns six attachment-resource pairs: attachment1-endpoint1, attachment1-endpoint2, attachment1-CIDR, attachment2-endpoint3, attachment2-endpoint4, and attachment2-endpoint5.

## As a principal: Identify your cross-account resources in Global Accelerator
<a name="cross-account-resources.identify-cross-account-principal"></a>

As a principal, after you're authorized by a cross-account attachment to add a resource to an accelerator as an endpoint, there is no additional action to take before you can add a resource as an endpoint.

You can see the AWS accounts that have created a cross-account attachment that you're listed as a principal in. You can also see the resources specified in the attachment that each account has created, that you can add as endpoints or IP address ranges for an accelerator.

## To see the accounts that have created a cross-account attachment that you're listed as a principal in


1. In the Global Accelerator console, on the **Endpoint details** page for an accelerator, choose **Add endpoint**.

1. On the **Add endpoints** page, select **Add a resource specified in a cross-account attachment**.

1. In the drop-down menu for **Select account ID of the cross-account attachment owner**, view the account or accounts that give you permission in a cross-account attachment to add resources to the accelerator.

## To see the endpoint resources specified in the attachment that each account has created


1. In the Global Accelerator console, on the **Endpoint details** page for an accelerator, choose **Add endpoint**.

1. On the **Add endpoints** page, select **Add a resource specified in a cross-account attachment**.

1. In the drop-down menu, select an account that gives you permission in a cross-account attachment to add resources to the accelerator.

1. For **Endpoint type**, choose a type of resource.

   Note that only the resource types included in the cross-account attachment appear in the drop-down menu.

1. In the **Endpoint** drop-down menu is a list of the resources. These are the resources that you are authorized by the account that created the cross-account attachment to add as endpoints, for a specific resource type.

1. To see the resources that you can add that are specified in the cross-account attachment created by a different account, do the following: In the drop-down menu for **Select account ID of the cross-account attachment owner**, select a different AWS account.

## To see the IP address resources specified in the attachment that an account has created


1. In the Global Accelerator console, choose **Create accelerator**.

1. On the **Enter name** page, for IP address type, select **IPv4**.

1. Under IP address pool selection, select **Use a shared IP address pool specified in a cross-account attachment**.

1. Select an account that gives you permission in a cross-account attachment to choose IP addresses from a shared IP address pool.

1. For **IP address pool**, in the drop-down list, you can view shared IP address pools.

   Note that only the shared IP address pools included in a cross-account attachment that you are permitted to use appear in the drop-down menu.