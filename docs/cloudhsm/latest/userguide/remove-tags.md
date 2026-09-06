

# Remove tags from AWS CloudHSM resources
<a name="remove-tags"></a>

You can remove tags from an AWS CloudHSM cluster by using the [AWS CloudHSM console](https://console.aws.amazon.com/cloudhsm/), the [AWS CLI](https://aws.amazon.com/cli/), or the AWS CloudHSM API.

**To remove tags (console)**

1. Open the AWS CloudHSM console at [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home).

1. Choose the cluster whose tags you are removing.

1. Choose **Tags**.

1. Choose **Edit Tag** and then choose **Remove tag** for the tag you want to remove.

1. Choose **Save**.

**To remove tags (AWS CLI)**
+ At a command prompt, issue the [**untag-resource**](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/untag-resource.html) command, specifying the tag keys of the tags that you are removing and the ID of the cluster whose tags you are removing. When you use the AWS CLI to remove tags, specify only the tag keys, not the tag values.

  ```
  $ aws cloudhsmv2 untag-resource --resource-id {{<cluster ID>}} \
                                  --tag-key-list "{{<tag key>}}"
  ```

**To remove tags (AWS CloudHSM API)**
+ Send an [UntagResource](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_UntagResource.html) request in the AWS CloudHSM API, specifying the ID of the cluster and the tags that you are removing.