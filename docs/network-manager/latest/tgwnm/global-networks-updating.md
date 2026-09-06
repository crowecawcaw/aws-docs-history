

# Update a global network using AWS Network Manager
<a name="global-networks-updating"></a>

Update a global network by modifying the description or tags. 

**To update your global network**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. Choose **Edit**.

1. For **Description**, enter a new description for the global network.

1. For **Tags**, choose **Remove tag** to remove an existing tag, or choose **Add tag** to add a new tag.

1. Choose **Edit global network**.

**To update a global network using the AWS CLI**  
Use the [update-global-network](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/update-global-network.html) command to update the description. Use the [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/untag-resource.html) commands to update the tags.