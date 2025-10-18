# Identity and access management for Network Synthetic Monitor

AWS Identity and Access Management (IAM) is an AWS service that helps an
 administrator securely control access to AWS resources. IAM administrators control
 who can be authenticated (signed in) and authorized (have permissions) to use Network Synthetic Monitor
 resources. IAM is an AWS service that you can use with no additional charge. You can
 use features of IAM to allow other users, services, and applications to use your AWS
 resources fully or in a limited way, without sharing your security credentials.

By default, IAM users don't have permission to create, view, or modify AWS
 resources. To allow an IAM user to access resources, such as a global network, and
 perform tasks, you must:


* Create an IAM policy that grants the user permission to use the specific
 resources and API actions they need
* Attach the policy to the IAM user or to the group to which the user
 belongs
When you attach a policy to a user or group of users, it allows or denies the user
 permissions to perform the specified tasks on the specified resources.


## Condition keys


The `Condition` element (or Condition block) lets you specify
 conditions in which a statement is in effect. The Condition element is optional. You
 can build conditional expressions that use condition operators, such as equals or
 less than, to match the condition in the policy with values in the request. For more
 information, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html") in the *AWS
 Identity and Access Management User Guide*.


If you specify multiple `Condition` elements in a statement, or
 multiple keys in a single `Condition` element, AWS evaluates them using
 a logical `AND` operation. If you specify multiple values for a single
 condition key, AWS evaluates the condition using a logical `OR`
 operation. All of the conditions must be met before the statement's permissions are
 granted.


You can also use placeholder variables when you specify conditions. For example,
 you can grant an IAM user permission to access a resource only if it is tagged
 with their IAM user name. 


You can attach tags to Network Synthetic Monitor resources or pass tags in a request to Cloud WAN.
 To control access based on tags, you provide tag information in the condition
 element of a policy using the `aws:ResourceTag/key-name`,
 `aws:RequestTag/key-name`, or `aws:TagKeys` condition
 keys. See [IAM JSON
 policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html") in the *AWS Identity and Access
 Management User Guide* for more information. 


To see all AWS global condition keys, see [AWS global
 condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html") in the *AWS Identity and Access
 Management User Guide*.


## Tag core network resources



A tag is a metadata label that either you or AWS assigns to an AWS resource.
 Each tag consists of a key and a value. For tags that you assign, you define the key
 and the value. For example, you might define the key as `purpose` and the
 value as `test` for one resource. Tags help you do the following:


* Identify and organize your AWS resources. Many AWS services support
 tagging, so you can assign the same tag to resources from different services to
 indicate that the resources are related.
* Control access to your AWS resources. For more information, see [Controlling
 access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html") in the *AWS Identify
 and Access Management User Guide*.

## Delete the service-linked role


If you no longer need to use Network Synthetic Monitor, we recommend that you delete the
 `AWSServiceRoleForNetworkMonitor` role. 


You can delete these service-linked roles only after you delete your monitors.
 For more information, see [Delete a monitor](https://docs.aws.amazon.com/  "https://docs.aws.amazon.com/ ").


You can use the IAM console, the IAM CLI, or the IAM API to delete
 service-linked roles. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role") in the
 *IAM User Guide*.


After you delete `AWSServiceRoleForNetworkMonitor`  Network Synthetic Monitor will create the role again when you
 create a new monitor.
