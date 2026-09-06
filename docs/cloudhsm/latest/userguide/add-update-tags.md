

# Add or update tags for AWS CloudHSM resources
<a name="add-update-tags"></a>

You can add or update tags from the [AWS CloudHSM console](https://console.aws.amazon.com/cloudhsm/), the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/), or the AWS CloudHSM API.

**To add or update tags (console)**

1. Open the AWS CloudHSM console at [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home).

1. Choose the cluster that you are tagging.

1. Choose **Tags**.

1. To add a tag, do the following:

   1. Choose **Edit Tag** and then choose **Add Tag**.

   1. For **Key**, type a key for the tag.

   1. (Optional) For **Value**, type a value for the tag.

   1. Choose **Save**.

1. To update a tag, do the following:

   1. Choose **Edit Tag**.
**Note**  
If you update the tag key for an existing tag, the console deletes the existing tag and creates a new one.

   1. Type the new tag value.

   1. Choose **Save**.

**To add or update tags (AWS CLI)**

1. At a command prompt, issue the [**tag-resource**](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/tag-resource.html) command, specifying the tags and the ID of the cluster that you are tagging. If you don't know the cluster ID, issue the **[describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html)** command.

   ```
   $ aws cloudhsmv2 tag-resource --resource-id {{<cluster ID>}} \
                                 --tag-list Key="{{<tag key>}}",Value="{{<tag value>}}"
   ```

1. To update tags, use the same command but specify an existing tag key. When you specify a new tag value for an existing tag, the tag is overwritten with the new value.

**To add or update tags (AWS CloudHSM API)**
+ Send a [TagResource](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_TagResource.html) request. Specify the tags and the ID of the cluster that you are tagging.