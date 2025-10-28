# Update a global network using AWS Network Manager

Update a global network by modifying the description or tags.

###### To update your global network

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. Choose **Edit**.
5. For **Description**, enter a new description for the global
   network.
6. For **Tags**, choose **Remove tag** to
   remove an existing tag, or choose **Add tag** to add a new
   tag.
7. Choose **Edit global network**.

###### To update a global network using the AWS CLI

Use the [update-global-network](../../../cli/latest/reference/networkmanager/update-global-network.md "../../../cli/latest/reference/networkmanager/update-global-network.md") command to update the description. Use the [tag-resource](../../../cli/latest/reference/networkmanager/tag-resource.md "../../../cli/latest/reference/networkmanager/tag-resource.md") and [untag-resource](../../../cli/latest/reference/networkmanager/untag-resource.md "../../../cli/latest/reference/networkmanager/untag-resource.md") commands to update the tags.
