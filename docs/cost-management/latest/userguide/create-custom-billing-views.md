# Creating custom billing views

Custom billing views allow you to grant accounts, both within and outside of your organization, specific,
controlled access to cost management data. A custom billing view contains a subset of the cost
management data contained in your management account's primary billing view. Once created, these
custom billing view resources can then be shared with the relevant accounts, enabling
tailored data visibility across your organization. Additionally, you can consolidate cost management data across multiple organizations by creating a custom billing view that combines data from multiple shared custom billing views, enabling centralized cost monitoring across your entire enterprise. If you're using AWS Billing Conductor, a
custom billing view contains cost management data based on your standard AWS bill, even when
being accessed by an account belonging to a billing group.

###### Note

To create custom billing views, you must use fine-grained AWS Cost Management actions.
For more information, see [Prerequisites](billing-view-getting-started.md#billing-view-prerequisite "billing-view-getting-started.md#billing-view-prerequisite").

###### To create a custom billing view with your organization's data

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management Preferences**.
3. Choose the **Billing View** tab.
4. Choose **Create view**.
5. Choose a single dimension to filter and specify the values to include in the custom billing view.
   - **Cost allocation tags**: This filter is recommended if you use
     cost allocation tags to organize and manage your spend. This field is restricted to one
     key, but allows multiple values within that key. For example, you can create a custom
     billing view containing all usage records with the cost allocation tag where the key is
     Cost Center and the values are 80432 or 78925. For more information about cost
     allocation tags, see [Organizing and tracking costs using AWS cost allocation
     tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md").
   - **Accounts**: This filter allows you to include cost management
     data for specific accounts in the custom billing view by selecting one or more account
     IDs. This is useful for creating custom billing views that focus on particular accounts
     or groups of accounts within your organization.
   - **No filter (all data):** This filter includes all cost
     management data from your organization.

6. For **Custom billing view name**, enter a short, descriptive name that
   helps users identify the custom billing view's data content. This helps users quickly
   understand the custom billing view’s content when selecting it from the **Choose
   billing view** menu in the navigation pane.
7. (Optional) For **Custom billing view description**, enter details about
   the custom billing view's content. This description will be visible in the **Billing
   View** tab.
8. (Optional) Add a tag to your custom billing view. For more information about tags, see
   [Tagging AWS
   resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference
   guide_.
   1. Choose **Add new tag**.
   2. Enter the key and value for the tag.
   3. Choose **Add new tag** to add additional tags. The maximum number
      of tags that you can add is 50.

9. Review your selections and choose **Create**. Once created, the custom
   billing view is assigned a unique Amazon Resource Name (ARN), which serves as its
   identifier.

###### To create a custom billing view with multiple sources

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management Preferences**.
3. Choose the **Billing View** tab.
4. Choose **Create multi-source view**.
5. Choose up to 20 source views. Your new view will include the cost management data from each selected source view.
6. Choose **Next**.
7. Choose a single dimension to filter and specify the values to include in the custom billing view.
   - **Cost allocation tags**: This filter is recommended if you use
     cost allocation tags to organize and manage your spend. This field is restricted to one
     key, but allows multiple values within that key. For example, you can create a custom
     billing view containing all usage records with the cost allocation tag where the key is
     Cost Center and the values are 80432 or 78925. For more information about cost
     allocation tags, see [Organizing and tracking costs using AWS cost allocation
     tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md").
   - **Accounts**: This filter allows you to include cost management
     data for specific accounts in the custom billing view by selecting one or more account
     IDs. This is useful for creating custom billing views that focus on particular accounts
     or groups of accounts within your organization.
   - **No filter (all data):** This filter includes all cost
     management data from your organization.

8. For **Custom billing view name**, enter a short, descriptive name that
   helps users identify the custom billing view's data content. This helps users quickly
   understand the custom billing view’s content when selecting it from the **Choose
   billing view** menu in the navigation pane.
9. (Optional) For **Custom billing view description**, enter details about
   the custom billing view's content. This description will be visible in the **Billing
   View** tab.
10. (Optional) Add a tag to your custom billing view. For more information about tags, see
    [Tagging AWS
    resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference
    guide_.
    1. Choose **Add new tag**.
    2. Enter the key and value for the tag.
    3. Choose **Add new tag** to add additional tags. The maximum number
       of tags that you can add is 50.

11. Choose **Next**.
12. Review your selections and choose **Create**. Once created, the custom
    billing view is assigned a unique Amazon Resource Name (ARN), which serves as its
    identifier.
    After creating a custom billing view, it is only available in your account. You can access
    it from the **Choose billing view** menu in the navigation pane from your own
    account to access its contents using Cost Explorer. You can also see the custom billing view
    definition details in the **Billing View** tab on the **Cost Management
    Preferences** page. You can choose to share the custom billing view with other
    accounts. Shared accounts can access the custom billing view from the **Choose billing
    view** menu, allowing them to access the cost management data defined in the custom
    billing view. To learn more, see [Sharing custom billing views](share-custom-billing-views.md "share-custom-billing-views.md").
