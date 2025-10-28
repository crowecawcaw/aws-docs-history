# List lifecycle management policies for Image Builder

image resources

You can get a list of your image lifecycle management policies that includes key detail
columns on the **Lifecycle policies** list page in the AWS Management Console, or with
commands or actions in the Image Builder API, SDKs, or AWS CLI.

You can use one of the following methods to list Image Builder image lifecycle policy resources
in your AWS account. For the API action, see [ListLifecyclePolicies](../APIReference/API_ListLifecyclePolicies.md "../APIReference/API_ListLifecyclePolicies.md") in the
_EC2 Image Builder API Reference_. For the associated SDK request, refer to the [See
Also](../APIReference/API_ListLifecyclePolicies.md#API_ListLifecyclePolicies_SeeAlso "../APIReference/API_ListLifecyclePolicies.md#API_ListLifecyclePolicies_SeeAlso") link on the same page.

AWS Management Console
The following details are shown in the console for your existing policies. You can
select any column to change the sort order for your results. The policy list is initially
sorted by **Policy name**. The column name for the current sort order
is bold.

If you have more than one page of results, the paging arrows in the top right corner
of the panel become active. You can filter results by policy name, policy status, output
image type and image resource ARN with the search bar.

- **Policy name** – The name of the policy.
- **Policy status** – Whether the policy is active
  or inactive.
- **Type** – The type of output image that Image Builder
  distributes when you create a new image version (AMI or container image).
- **Last execution date** – The last time the lifecycle
  policy ran.
- **Date created** – The timestamp from the creation
  of the lifecycle policy.
- **ARN** – The Amazon Resource Name (ARN) of the lifecycle
  policy resource.

To list lifecycle policies in the AWS Management Console, follow these steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Select **Lifecycle policies** from the navigation pane.
   This shows a list of image lifecycle policies in your account.

###### Available actions

You can also perform the following actions for your lifecycle policy from the
**Lifecycle policies** list page.

To create a new image lifecycle policy, choose **Create lifecycle policy**.
For more information about how to create a policy, see [Create lifecycle policies](create-lifecycle-policies.md "create-lifecycle-policies.md").

For all of the following actions, you must select the policy first. To select a policy,
you can select the check box next to the **Policy name**.

- To turn the policy off or on, select **Disable policy** or
  **Enable policy** from the **Actions** menu.
- To change the policy, select **Edit policy** from the
  **Actions** menu.
- To delete a policy, select **Delete policy** from the
  **Actions** menu.
- To create a new policy that uses your selected policy for baseline settings,
  select **Clone policy** from the **Actions** menu.

AWS CLI
The following command example shows how to use the AWS CLI to list image
lifecycle policies for a specific AWS Region. For more
information about the parameters and options that you can use with this command, see the
[list-lifecycle-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-policies.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-policies.html")
command in the AWS CLI Command Reference.

**Example:**

```
`aws imagebuilder list-lifecycle-policies \
--region `us-west-1``
```

**Output:**

```
`{
 "lifecyclePolicySummaryList": [
 {
 "arn": "arn:aws:imagebuilder:us-west-2:`111122223333`:lifecycle-policy/sample-lifecycle-policy1",
 "name": "sample-lifecycle-policy1",
 "status": "DISABLED",
 "executionRole": "arn:aws:iam::`111122223333`:role/sample-lifecycle-role",
 "resourceType": "AMI_IMAGE",
 "dateCreated": "2023-11-07T14:57:01.603000-08:00",
 "tags": {}
 },
 {
 "arn": "arn:aws:imagebuilder:us-west-2:`111122223333`:lifecycle-policy/sample-lifecycle-policy2",
 "name": "sample-lifecycle-policy2",
 "status": "ENABLED",
 "executionRole": "arn:aws:iam::`111122223333`:role/sample-lifecycle-role",
 "resourceType": "AMI_IMAGE",
 "dateCreated": "2023-09-06T10:43:21.436000-07:00",
 "dateLastRun": "2023-11-13T04:43:46.106000-08:00",
 "tags": {}
 },
 {
 "arn": "arn:aws:imagebuilder:us-west-2:`111122223333`:lifecycle-policy/sample-lifecycle-policy3",
 "name": "sample-lifecycle-policy3",
 "status": "ENABLED",
 "executionRole": "arn:aws:iam::`111122223333`:role/sample-lifecycle-role",
 "resourceType": "AMI_IMAGE",
 "dateCreated": "2023-10-19T15:16:40.046000-07:00",
 "dateUpdated": "2023-10-21T20:07:15.958000-07:00",
 "dateLastRun": "2023-11-12T09:27:45.830000-08:00"
}]}`
```

###### Note

To use your default AWS Region, run this command without the
`--region` parameter.
