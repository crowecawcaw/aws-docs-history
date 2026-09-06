

# Creating custom billing views
<a name="create-custom-billing-views"></a>

Custom billing views allow you to grant accounts, both within and outside of your organization, specific, controlled access to cost management data. A custom billing view contains a subset of the cost management data contained in your management account's primary billing view. Once created, these custom billing view resources can then be shared with the relevant accounts, enabling tailored data visibility across your organization. Additionally, you can consolidate cost management data across multiple organizations by creating a custom billing view that combines data from multiple shared custom billing views, enabling centralized cost monitoring across your entire enterprise. If you're using AWS Billing Conductor, a custom billing view contains cost management data based on your standard AWS bill, even when being accessed by an account belonging to a billing group.

**Note**  
To create custom billing views, you must use fine-grained AWS Cost Management actions. For more information, see [Prerequisites](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-view-getting-started.html#billing-view-prerequisite).

**To create a custom billing view with your organization's data**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Management Preferences**.

1. Choose the **Billing View** tab.

1. Choose **Create view**.

1. Choose a single dimension to filter and specify the values to include in the custom billing view.
   + **Cost allocation tags**: This filter is recommended if you use cost allocation tags to organize and manage your spend. This field is restricted to one key, but allows multiple values within that key. For example, you can create a custom billing view containing all usage records with the cost allocation tag where the key is Cost Center and the values are 80432 or 78925. For more information about cost allocation tags, see [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).
   + **Accounts**: This filter allows you to include cost management data for specific accounts in the custom billing view by selecting one or more account IDs. This is useful for creating custom billing views that focus on particular accounts or groups of accounts within your organization.
   + **No filter (all data):** This filter includes all cost management data from your organization.

1. For **Custom billing view name**, enter a short, descriptive name that helps users identify the custom billing view's data content. This helps users quickly understand the custom billing view’s content when selecting it from the **Choose billing view** menu in the navigation pane.

1. (Optional) For **Custom billing view description**, enter details about the custom billing view's content. This description will be visible in the **Billing View** tab.

1. (Optional) Add a tag to your custom billing view. For more information about tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference guide*.

   1. Choose **Add new tag**.

   1. Enter the key and value for the tag.

   1. Choose **Add new tag** to add additional tags. The maximum number of tags that you can add is 50.

1. Review your selections and choose **Create**. Once created, the custom billing view is assigned a unique Amazon Resource Name (ARN), which serves as its identifier.

**To create a custom billing view with multiple sources**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Management Preferences**.

1. Choose the **Billing View** tab.

1. Choose **Create multi-source view**.

1. Choose up to 20 source views. Your new view will include the cost management data from each selected source view.

1. Choose **Next**.

1. Choose a single dimension to filter and specify the values to include in the custom billing view.
   + **Cost allocation tags**: This filter is recommended if you use cost allocation tags to organize and manage your spend. This field is restricted to one key, but allows multiple values within that key. For example, you can create a custom billing view containing all usage records with the cost allocation tag where the key is Cost Center and the values are 80432 or 78925. For more information about cost allocation tags, see [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).
   + **Accounts**: This filter allows you to include cost management data for specific accounts in the custom billing view by selecting one or more account IDs. This is useful for creating custom billing views that focus on particular accounts or groups of accounts within your organization.
   + **No filter (all data):** This filter includes all cost management data from your organization.

1. For **Custom billing view name**, enter a short, descriptive name that helps users identify the custom billing view's data content. This helps users quickly understand the custom billing view’s content when selecting it from the **Choose billing view** menu in the navigation pane.

1. (Optional) For **Custom billing view description**, enter details about the custom billing view's content. This description will be visible in the **Billing View** tab.

1. (Optional) Add a tag to your custom billing view. For more information about tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference guide*.

   1. Choose **Add new tag**.

   1. Enter the key and value for the tag.

   1. Choose **Add new tag** to add additional tags. The maximum number of tags that you can add is 50.

1. Choose **Next**.

1. Review your selections and choose **Create**. Once created, the custom billing view is assigned a unique Amazon Resource Name (ARN), which serves as its identifier.

After creating a custom billing view, it is only available in your account. You can access it from the **Choose billing view** menu in the navigation pane from your own account to access its contents using Cost Explorer. You can also see the custom billing view definition details in the **Billing View** tab on the **Cost Management Preferences** page. You can choose to share the custom billing view with other accounts. Shared accounts can access the custom billing view from the **Choose billing view** menu, allowing them to access the cost management data defined in the custom billing view. To learn more, see [Sharing custom billing views](https://docs.aws.amazon.com/cost-management/latest/userguide/share-custom-billing-views.html).