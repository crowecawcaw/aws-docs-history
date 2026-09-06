

# Manage resources with Tags
<a name="manage-resources"></a>

Use resource tagging in Amazon Location to create tags to categorize your resources by purpose, owner, environment, or criteria. Tagging your resources helps you manage, identify, organize, search, and filter your resources. For example, with AWS Resource Groups, you can create groups of AWS resources based on one or more tags or portions of tags. You can also create groups based on their occurrence in an AWS CloudFormation stack. Using Resource Groups and Tag Editor, you can consolidate and view data for applications that consist of multiple services, resources, and Regions in one place. For more information on [Common Tagging Strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html), see the *AWS General Reference*.

Each tag is a label consisting of a key and value that you define: 
+ **Tag key** – A general label that categorizes the tag values. For example, `CostCenter`. 
+ **Tag value** – An optional description for the tag key category. For example, `MobileAssetTrackingResourcesProd`. 

This topic helps you get started with tagging by reviewing tagging restrictions. It also shows you how to create tags and use tags to track your AWS cost for each active tag by using cost allocation reports. 

For more information about: 
+ Tagging best practices, see [Tagging AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in the *AWS General Reference*.
+ Using tags to control access to AWS resources, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *AWS Identity and Access Management User Guide*. 

## Restrictions
<a name="manage-resources_restrictions"></a>

**Note**  
If you add a new tag with the same tag key as an existing tag, the new tag overwrites the existing tag.

Tagging allows you to organize and manage your resources more effectively. This page outlines the specific rules and constraints that govern the use of tags within Amazon Location Service. By understanding these tagging restrictions, you can ensure compliance with best practices and avoid potential issues when implementing tagging strategies for your location-based resources and applications. 

The following basic restrictions apply to tags: 
+ Maximum tags per resource: 50 
+ For each resource, each tag key must be unique, and each tag key can have only one value. 
+ Maximum key length: 128 Unicode characters in UTF-8 
+ Maximum value length: 256 Unicode characters in UTF-8 
+ The allowed characters across services are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @. 
+ Tag keys and values are case-sensitive. 
+ The `aws:` prefix is reserved for AWS use. If a tag has a tag key with this prefix, then you can't edit or delete the tag's key or value. Tags with the aws: prefix don't count against your tags per resource limit. 

## Grant permission to tag resources
<a name="manage-resources_grant-permission"></a>

You can use IAM policies to control access to your Amazon Location resources and grant permission to tag a resource on creation. In addition to granting permission to create resources, the policy can include Action permissions to allow tagging operations: 
+ `geo:TagResource` – Allows a user to assign one or more tags to a specified Amazon Location resource. 
+ `geo:UntagResource` – Allows a user to remove one or more tags from a specified Amazon Location resource. 
+ `geo:ListTagsForResource` – Allows a user to list all the tags assigned to an Amazon Location resource. 

The following is a policy example to allow a user to create a geofence collection and tag resources: 

```
{
"Version": "2012-10-17",		 	 	 
    "Statement": [
        {
"Sid": "AllowTaggingForGeofenceCollectionOnCreation",
            "Effect": "Allow",
            "Action": [
                "geo:CreateGeofenceCollection",
                "geo:TagResource"
            ],
            "Resource": "arn:aws:geo:region:accountID:geofence-collection/*"
    ]
}
```

## Add a tag to a resource
<a name="manage-resources_add-tag"></a>

 You can add tags when creating your resources using the Amazon Location console, the AWS CLI, or the Amazon Location APIs: 
+ [Manage your geofence collection resources](managing-geofence-collections.md) 
+ [Create a tracker](start-create-tracker.md) 

**To tag existing resources, edit or delete tags**

1.  Open the [Amazon Location console](https://console.aws.amazon.com/location). 

1.  In the left navigation pane, choose the resource you want to tag. For example, **Maps**. 

1.  Choose a resource from the list. 

1.  Choose **Manage tags** to add, edit, or delete your tags. 

## How to use tags
<a name="manage-resources_how-to"></a>

 You can use tags for cost allocation to track your AWS cost in detail. After you activate the cost allocation tags, AWS uses the cost allocation tags to organize your resource billing on your cost allocation report. This helps you categorize and track your usage costs. 

Amazon Location supports [User-defined](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html) – Tags. These are custom tags that you create. The user-defined tags use the `user:` prefix, for example, `user:CostCenter`.

 You must activate each tag type individually. After your tags are activated, you can [enable AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) or view your monthly cost allocation report. 

**To activate user-defined tags**

1.  Open the [Billing and Cost Management console](https://console.aws.amazon.com/billing). 

1.  In the left navigation pane, choose **Cost Allocation Tags**. 

1.  Under the **User-Defined Cost Allocation Tags** tab, select the tag keys you want to activate. 

1.  Choose **Activate**. 

 After you activate your tags, AWS generates a [monthly Cost Allocation Report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html) for your resource usage and cost. This cost allocation report includes all of your AWS costs for each billing period, including tagged and untagged resources. For more information, see [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*. 

### Control access to resources using tags
<a name="manage-resources_control-access"></a>

 AWS Identity and Access Management (IAM) policies support tag-based conditions, which enables you to manage authorization for your resources based on specific tags key and values. For example, an IAM role policy can include conditions to limit access to specific environments, such as development, test, or production, based on tags. For more information, see the topic on [control resource access based on tags](https://docs.aws.amazon.com/location/latest/developerguide/security-iam.html#security_iam_id-based-policy-examples). 