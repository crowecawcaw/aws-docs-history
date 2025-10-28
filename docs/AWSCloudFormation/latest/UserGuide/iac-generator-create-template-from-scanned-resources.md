# Create a

CloudFormation template from resources scanned with IaC generator

This topic explains how to create a template from resources that were scanned using
the IaC generator feature.

## Create a template

from scanned resources (console)

###### To create a stack template from scanned resources

1. Open the [IaC
   generator page](https://console.aws.amazon.com/cloudformation/home?#iac-generator "https://console.aws.amazon.com/cloudformation/home?#iac-generator") of the CloudFormation console.
2. On the navigation bar at the top of the screen, choose the AWS Region
   that contains the scanned resources.
3. From the **Templates** section, choose **Create
   template**.
4. Choose **Start from a new template**.
   1. For **Template name**, provide a name for your
      template.
   2. (Optional) Configure your **Deletion policy** and
      **Update replace policy**.
   3. Choose **Next** to add scanned resources to the
      template.

5. For **Add scanned resources**, browse the list of scanned
   resources and select the resources you want to add to your template. You can
   filter the resources by resource identifier, resource type, or tags. The
   filters are mutually inclusive.
6. When you've added all needed resources to your template, choose
   **Next** to exit the **Add scanned
   resources** page and proceed to the **Add related
   resources** page.
7. Review a recommended list of related resources. Related resources, such as
   Amazon EC2 instances and security groups, are interdependent and typically belong
   to the same workload. Select the related resources that you want to include
   in the generated template.

###### Note

We suggest that you add all related resources to this template. 8. Review the template details, scanned resources, and related resources. 9. Choose **Create template** to exit the **Review
and create** page and create the template.

## Create a template from

scanned resources (AWS CLI)

###### To create a stack template from scanned resources

1. Use the [list-resource-scan-resources](../../../cli/latest/reference/cloudformation/list-resource-scan-resources.md "../../../cli/latest/reference/cloudformation/list-resource-scan-resources.md") command to list the resources
   found during the scan, optionally specifying the
   `--resource-identifier` option to limit the output. For the
   `--resource-scan-id` option, replace the sample ARN with the
   actual ARN.

```
aws cloudformation list-resource-scan-resources \
  --resource-scan-id `arn:aws:cloudformation:us-east-1:123456789012:resourceScan/0a699f15-489c-43ca-a3ef-3e6ecfa5da60` \
  --resource-identifier `MyApp`
```

The following is an example response, where `ManagedByStack`
indicates whether CloudFormation manages the resource already. Copy the output.
You need it for the next step.

```
{
    "Resources": [
        {
            "ResourceType": "AWS::EKS::Cluster",
            "ResourceIdentifier": {
                "ClusterName": "MyAppClusterName"
            },
            **"ManagedByStack": false**
        },
        {
            "ResourceType": "AWS::AutoScaling::AutoScalingGroup",
            "ResourceIdentifier": {
                "AutoScalingGroupName": "MyAppASGName"
            },
            **"ManagedByStack": false**
        }
    ]
}
```

For a description of the fields in the output, see [ScannedResource](../APIReference/API_ScannedResource.md "../APIReference/API_ScannedResource.md") in the
_AWS CloudFormation API Reference_. 2. Use the `cat` command to store the resource types and
identifiers in a JSON file named `resources.json` in your home
directory. The following is example JSON based on the example output in the
previous step.

```
$ cat > resources.json
[
    {
        "ResourceType": "AWS::EKS::Cluster",
        "ResourceIdentifier": {
            "ClusterName": "MyAppClusterName"
        }
    },
    {
        "ResourceType": "AWS::AutoScaling::AutoScalingGroup",
        "ResourceIdentifier": {
            "AutoScalingGroupName": "MyAppASGName"
        }
    }
]
```

3. Use the [list-resource-scan-related-resources](../../../cli/latest/reference/cloudformation/list-resource-scan-related-resources.md "../../../cli/latest/reference/cloudformation/list-resource-scan-related-resources.md") command, along with the
   `resources.json` file you created, to list the resources
   related to your scanned resources.

```
aws cloudformation list-resource-scan-related-resources \
  --resource-scan-id `arn:aws:cloudformation:us-east-1:123456789012:resourceScan/0a699f15-489c-43ca-a3ef-3e6ecfa5da60` \
  --resources `file://resources.json`
```

The following is an example response, where `ManagedByStack`
indicates whether CloudFormation manages the resource already. Add these
resources to the JSON file you created in the previous step. You'll need it
to create your template.

```
{
    "RelatedResources": [
        {
            "ResourceType": "AWS::EKS::Nodegroup",
            "ResourceIdentifier": {
                "NodegroupName": "MyAppNodegroupName"
            },
            **"ManagedByStack": false**
        },
        {
            "ResourceType": "AWS::IAM::Role",
            "ResourceIdentifier": {
                "RoleId": "arn:aws::iam::`account-id`:role/MyAppIAMRole"
            },
            **"ManagedByStack": false**
        }
    ]
}
```

For a description of the fields in the output, see [ScannedResource](../APIReference/API_ScannedResource.md "../APIReference/API_ScannedResource.md") in the
_AWS CloudFormation API Reference_.

###### Note

The input list of resources can't exceed a length of 100. To list
related resources for more than 100 resources, run the
**list-resource-scan-related-resources** command in
batches of 100 and consolidate the results.

Be aware that the output may contain duplicated resources in the
list. 4. Use the [create-generated-template](../../../cli/latest/reference/cloudformation/create-generated-template.md "../../../cli/latest/reference/cloudformation/create-generated-template.md") command to create a new stack
template, as follows, with these modifications:

    * Replace
     ``us-east-1``
     with the AWS Region that contains the scanned resources.
    * Replace ``MyTemplate`` with
     the name of the template to create.

```
aws cloudformation create-generated-template --region `us-east-1` \
 --generated-template-name `MyTemplate` \
  --resources `file://resources.json`
```

The following is an example `resources.json` file.

```
[
    {
        "ResourceType": "AWS::EKS::Cluster",
        "LogicalResourceId":"MyCluster",
        "ResourceIdentifier": {
            "ClusterName": "MyAppClusterName"
        }
    },
    {
        "ResourceType": "AWS::AutoScaling::AutoScalingGroup",
        "LogicalResourceId":"MyASG",
        "ResourceIdentifier": {
            "AutoScalingGroupName": "MyAppASGName"
        }
    },
    {
        "ResourceType": "AWS::EKS::Nodegroup",
        "LogicalResourceId":"MyNodegroup",
        "ResourceIdentifier": {
            "NodegroupName": "MyAppNodegroupName"
        }
    },
    {
        "ResourceType": "AWS::IAM::Role",
        "LogicalResourceId":"MyRole",
        "ResourceIdentifier": {
            "RoleId": "arn:aws::iam::`account-id`:role/MyAppIAMRole"
        }
    }
]
```

If successful, this command returns the following.

```
{
  "Arn":
    "arn:aws:cloudformation:`region`:`account-id`:generatedtemplate/`7fc8512c-d8cb-4e02-b266-d39c48344e48`",
  "Name": "`MyTemplate`"
}
```
