# Create an AWS Cloud WAN attachment routing policy

Attachment routing policies are used to associate one or more route policies to attachments. Attachment route policy consists of a list of match-action rules that map one or more route policies to a route policy label which is a string identifier (max 256 characters). You will need to associate this route policy label with an attachment via the create-attachment-routing-policy-label API.

###### To create an attachment routing policy

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Cloud WAN**.
3. On the **Global networks** page, choose the global network ID that for the core network you want to create a policy version for, and then choose **Core network**.
4. In the navigation pane, choose **Policy versions**.
5. Choose **Create policy version**.
6. In **Choose policy view mode**, choose **Visual editor**.
7. Choose the **Attachment policies** tab.
8. In the **Attachment routing policies rules** section, choose
   **Create**.
9. For **Rule number**, enter a unique number from 1 to 9,999.
   Rules are processed in numerical order.
10. (Optional) Enter a **Rule description**. The description can be no longer than 256 characters, using a-z, A-Z, 0-9, and hyphens (-). White spaces are not allowed.
11. (Optional) Choose the **Edge locations** that this attachment routing rule is applicable to. You can only choose those edge locations that you set up in your network configuration. You can configure this option for Direct Connect attachments that can associate with multiple CNEs. This option allows you to associate the routing policy to a select CNE. By default routing policy applies to all CNEs associated with the Direct Connect attachment.
12. For **Condition - Routing policy label**, enter the label for the routing policy you want to use for attachment association. All attachments with the same routing label will be automatically associated with this attachment routing policy. You can add a label to attachment when you create that attachment, or you can modify an existing attachment to add a routing label. For more information about adding labels to an attachment, see the applicable steps for the type of attachment you're creating in [Attachments](cloudwan-create-attachment.md "cloudwan-create-attachment.md").
13. For **Action - Associate with these routing policies**, choose the Cloud WAN routing policies you want to associate with label defined in the previous step.
    For more information on the parameters used in the JSON file, see [Core network policy version parameters in
    AWS Cloud WAN](cloudwan-policies-json.md "cloudwan-policies-json.md").

```
{
    "attachment-routing-policy-rules": [
        {
            "rule-number": 500,
            "description": "Attachment Route Filters",
            "edge-locations": ["us-west-1", "us-east-1"],
            "conditions":[
                {
                    "type": "routing-policy-label",
                    "value": "attachmentRoutingFilter"
                }
            ],
            "action": {
                "associate-routing-policies": ["routingFilter"]
            }
        }
    ]
}
```
