AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Choosing a filter view for managed node

summaries

The **Explore nodes** page in Systems Manager lets you view aggregated data
about your fleet according to a number of available filter views.

###### To choose a filter view for managed node summaries

1.  Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2.  In the navigation pane, choose **Explore nodes**.
3.  For **Filter view**, select one of the filter options and
    optionally further refine the report:

        * **Managed nodes** – In the search (
        ![The search icon](images/search-icon.png)
        ) box, you can select a property and delimiter,
         such as `Node type = Managed EC2 instances`.
        * **Operating systems** – In the
         **Filter Operating system versions** list, you
         can select an OS version number. In the search (
        ![The search icon](images/search-icon.png)
        ) box, you can select a property and delimiter,
         such as `Node type = Managed EC2 instances`.
        * **SSM Agent versions** – In the
         **Filter Operating systems** list, you can
         select an OS name. In the search (
        ![The search icon](images/search-icon.png)
        ) box, you can select a property and delimiter,
         such as `Node type = Managed EC2 instances`.
        * **Node types** – In the **Filter
         Operating systems** list, you can select an OS name. In
         the search (
        ![The search icon](images/search-icon.png)
        ) box, you can select a property and delimiter,
         such as `Node type = Managed EC2 instances`.

    After optionally filtering the list, you can view details about a specific managed
    node by choosing its ID in the **Node ID** column. From that
    detailed view, you can perform a number of actions on the node.
