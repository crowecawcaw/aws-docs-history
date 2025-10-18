# List tags for AWS CloudHSM resources

You can list tags for a cluster from the [AWS CloudHSM
 console](https://console.aws.amazon.com/cloudhsm/ "https://console.aws.amazon.com/cloudhsm/"), the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), or the AWS CloudHSM API.

###### To list tags (console)

1. Open the AWS CloudHSM console at
 [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. Choose the cluster whose tags you are listing.
3. Choose **Tags**.
###### To list tags (AWS CLI)

* At a command prompt, issue the [**list-tags**](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/list-tags.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/list-tags.html") command, specifying the ID of the cluster whose tags
 you are listing. If you don't know the cluster ID, issue the **[describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html")**
 command.



```
`$` `aws cloudhsmv2 list-tags --resource-id `<cluster ID>```{
 "TagList": [
 {
 "Key": "Cost Center",
 "Value": "12345"
 }
 ]
}`
```
###### To list tags (AWS CloudHSM API)

* Send a [ListTags](../APIReference/API_ListTags.md "../APIReference/API_ListTags.md")
 request, specifying the ID of the cluster whose tags you are listing.
