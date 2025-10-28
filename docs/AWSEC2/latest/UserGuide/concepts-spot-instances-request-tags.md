# Tag Spot Instance requests

To help categorize and manage your Spot Instance requests, you can tag them with custom metadata.
You can assign a tag to a Spot Instance request when you create it, or afterward. You can
assign tags using the Amazon EC2 console or a command line tool.

When you tag a Spot Instance request, the instances and volumes that are launched by the
Spot Instance request are not automatically tagged. You need to explicitly tag the instances
and volumes launched by the Spot Instance request. You can assign a tag to a Spot Instance and volumes
during launch, or afterward.

For more information about how tags work, see [Tag your Amazon EC2 resources](Using_Tags.md "Using_Tags.md").

###### Contents

- [Prerequisites](#tag-spot-request-prereqs "#tag-spot-request-prereqs")
- [Tag a new Spot Instance request](#tag-new-spot-instance-request "#tag-new-spot-instance-request")
- [Tag an existing Spot Instance request](#tag-existing-spot-instance-request "#tag-existing-spot-instance-request")
- [View Spot Instance request tags](#view-spot-instance-request-tags "#view-spot-instance-request-tags")

## Prerequisites

Grant the user the permission to tag resources. For more information about IAM
policies and example policies, see [Example: Tag resources](ExamplePolicies_EC2.md#iam-example-taggingresources "ExamplePolicies_EC2.md#iam-example-taggingresources").

The IAM policy you create is determined by which method you use for creating a
Spot Instance request.

- If you use the launch instance wizard or `run-instances` to request Spot Instances, see [To grant a user the permission to tag resources when using the launch instance wizard or run-instances](#iam-run-instances "#iam-run-instances").
- If you use the `request-spot-instances` command to request Spot Instances, see [To grant a user the permission to tag resources when using request-spot-instances](#iam-request-spot-instances "#iam-request-spot-instances").

###### To grant a user the permission to tag resources when using the launch

instance wizard or run-instances

Create a IAM policy that includes the following:

- The `ec2:RunInstances` action. This grants the user
  permission to launch an instance.
- For `Resource`, specify `spot-instances-request`. This allows
  users to create Spot Instance requests, which request Spot Instances.
- The `ec2:CreateTags` action. This grants the user
  permission to create tags.
- For `Resource`, specify `*`. This allows users to tag all
  resources that are created during instance launch.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowLaunchInstances",
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1::image/*",
 "arn:aws:ec2:us-east-1:*:subnet/*",
 "arn:aws:ec2:us-east-1:*:network-interface/*",
 "arn:aws:ec2:us-east-1:*:security-group/*",
 "arn:aws:ec2:us-east-1:*:key-pair/*",
 "arn:aws:ec2:us-east-1:*:volume/*",
 "arn:aws:ec2:us-east-1:*:instance/*",
 "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
 ]
 },
 {
 "Sid": "TagSpotInstanceRequests",
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "*"
 }
 ]
}`

```

When you use the RunInstances action to create Spot Instance requests and tag the
Spot Instance requests on create, you need to be aware of how Amazon EC2 evaluates the
`spot-instances-request` resource in the RunInstances
statement it is evaluated in the IAM policy as follows:

- If you don't tag a Spot Instance request on create, Amazon EC2 does not evaluate the
  `spot-instances-request` resource in the RunInstances
  statement.
- If you tag a Spot Instance request on create, Amazon EC2 evaluates the
  `spot-instances-request` resource in the RunInstances
  statement.

Therefore, for the `spot-instances-request` resource, the following
rules apply to the IAM policy:

- If you use RunInstances to create a Spot Instance request and you don't intend to tag the Spot Instance
  request on create, you don’t need to explicitly allow the
  `spot-instances-request` resource; the call will
  succeed.
- If you use RunInstances to create a Spot Instance request and intend to tag the Spot Instance request on
  create, you must include the `spot-instances-request`
  resource in the RunInstances allow statement, otherwise the call
  will fail.
- If you use RunInstances to create a Spot Instance request and intend to tag the Spot Instance request on
  create, you must specify the `spot-instances-request`
  resource or include a `*` wildcard in the CreateTags
  allow statement, otherwise the call will fail.

For example IAM policies, including policies that are not supported for Spot Instance requests,
see [Work with Spot Instances](ExamplePolicies_EC2.md#iam-example-spot-instances "ExamplePolicies_EC2.md#iam-example-spot-instances").

###### To grant a user the permission to tag resources when using

request-spot-instances

Create a IAM policy that includes the following:

- The `ec2:RequestSpotInstances` action. This grants the user permission to
  create a Spot Instance request.
- The `ec2:CreateTags` action. This grants the user permission to create tags.
- For `Resource`, specify `spot-instances-request`. This allows
  users to tag only the Spot Instance request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TagSpotInstanceRequest",
 "Effect": "Allow",
 "Action": [
 "ec2:RequestSpotInstances",
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:spot-instances-request/*"
 }
 ]
}`

```

## Tag a new Spot Instance request

In the AWS CLI and PowerShell examples, configure the Spot Instance request as follows:

- For `ResourceType`, specify `spot-instances-request`. If you
  specify another value, the Spot Instance request will fail.
- For `Tags`, specify the key-value pair. You can specify more than one
  key-value pair.

Console

###### To tag a new Spot Instance request

1. Follow the [Manage your Spot Instances](using-spot-instances-request.md "using-spot-instances-request.md") procedure.
2. To add a tag, on the **Add Tags** page, choose **Add
   Tag**, and enter the key and value for the tag. Choose
   **Add another tag** for each additional tag.

For each tag, you can tag the Spot Instance request, the Spot Instances, and the volumes with the same
tag. To tag all three, ensure that **Instances**,
**Volumes**, and **Spot Instance Requests**
are selected. To tag only one or two, ensure that the resources you want
to tag are selected, and the other resources are cleared. 3. Complete the required fields to create a Spot Instance request, and then choose
**Launch**. For more information, see [Manage your Spot Instances](using-spot-instances-request.md "using-spot-instances-request.md").

AWS CLI

###### To tag a new Spot Instance request

Use the [request-spot-instances](../../../cli/latest/reference/ec2/request-spot-instances.md "../../../cli/latest/reference/ec2/request-spot-instances.md")
command with the `--tag-specification` option.

The tag specification adds two tags to the Spot Instance request:
`Environment=Production` and `Cost-Center=123`.

```
aws ec2 request-spot-instances \
    --instance-count `5` \
    --type "one-time" \
    --launch-specification file://`specification.json` \
    --tag-specification 'ResourceType=spot-instances-request,Tags=[{Key=`Environment`,Value=`Production`},{Key=`Cost-Center`,Value=`123`}]'
```

PowerShell

###### To tag a new Spot Instance request

Use the [Request-EC2SpotInstance](../../../powershell/latest/reference/items/Request-EC2SpotInstance.md "../../../powershell/latest/reference/items/Request-EC2SpotInstance.md")
cmdlet with the `-TagSpecification` parameter.

```
-TagSpecification $tagspec
```

The tag specification is defined as follows. It adds two tags to the Spot Instance request:
`Environment=Production` and `Cost-Center=123`.

```
$tag1 = @{Key="Environment"; Value="Production"}
$tag2 = @{Key="Cost-Center"; Value="123"}
$tagspec = New-Object Amazon.EC2.Model.TagSpecification
$tagspec.ResourceType = "spot-instances-request"
$tagspec.Tags = @($tag1,$tag2)
```

## Tag an existing Spot Instance request

Console

###### To tag an existing Spot Instance request

After you have created a Spot Instance request, you can add tags to the Spot Instance request using the
console.

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Select your Spot Instance request.
4. Choose the **Tags** tab and choose **Create
   Tag**.

###### To tag an existing Spot Instance using the

console

After your Spot Instance request has launched your Spot Instance, you can add tags to the instance using the
console. For more information, see [Add tags using the console](Using_Tags_Console.md#adding-or-deleting-tags "Using_Tags_Console.md#adding-or-deleting-tags").

AWS CLI

###### To tag an existing Spot Instance request or Spot Instance

Use the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") command to tag
existing resources. In the following example, the existing Spot Instance request and the
Spot Instance are tagged with `purpose=test`.

```
aws ec2 create-tags \
    --resources `sir-0e54a519c9EXAMPLE` `i-1234567890abcdef0` \
    --tags Key=`purpose`,Value=`test`
```

PowerShell

###### To tag an existing Spot Instance request or Spot Instance

Use the [New-EC2Tag](../../../powershell/latest/reference/items/New-EC2Tag.md "../../../powershell/latest/reference/items/New-EC2Tag.md")
cmdlet. The following example adds the tag `purpose=test`
to the existing Spot Instance request and the Spot Instance.

```
New-EC2Tag `
    -Resource `sir-0e54a519c9EXAMPLE`, `i-1234567890abcdef0` `
    -Tag @{Key="`purpose`"; Value="`test`"}
```

## View Spot Instance request tags

Console

###### To view Spot Instance request tags

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Select your Spot Instance request and choose the **Tags** tab.

AWS CLI

###### To describe Spot Instance request tags

Use the [describe-spot-instance-requests](../../../cli/latest/reference/ec2/describe-spot-instance-requests.md "../../../cli/latest/reference/ec2/describe-spot-instance-requests.md") command to view the configuration
of the specified Spot Instance request, which includes any tags that were specified for
the request.

```
aws ec2 describe-spot-instance-requests \
    --spot-instance-request-ids `sir-0e54a519c9EXAMPLE` \
    --query "SpotInstanceRequests[*].Tags"
```

The following is example output.

```
[
    [
        {
            "Key": "Environment",
            "Value": "Production"
        },
        {
            "Key": "Department",
            "Value": "101"
        }
    ]
]
```

PowerShell

###### To describe Spot Instance request tags

Use the [Get-EC2SpotInstanceRequest](../../../powershell/latest/reference/items/Get-EC2SpotInstanceRequest.md "../../../powershell/latest/reference/items/Get-EC2SpotInstanceRequest.md")
cmdlet.

```
(Get-EC2SpotInstanceRequest `
    -SpotInstanceRequestId `sir-0e54a519c9EXAMPLE`).Tags
```

The following is example output.

```
Key         Value
---         -----
Environment Production
Department  101
```
