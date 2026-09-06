

# Creating a data export for your Capacity Manager data
<a name="create-cm-export"></a>

To create a data export, you can use the Data Exports page in the Capacity Manager console or the AWS CLI.

## Prerequisites
<a name="cm-export-prerequisites"></a>

You must create an Amazon Simple Storage Service (Amazon S3) bucket. You must make sure of the following:
+ Your S3 bucket must be in the same AWS Region where you enabled Capacity Manager. 
+ Your S3 bucket has the required permissions policy for the Capacity Manager service to deliver files. 

For more information, see [Setting up an Amazon S3 bucket for Capacity Manager data exports](cm-set-up-s3-export.md).

## Procedure
<a name="cm-export-procedure"></a>

You can export your Capacity Manager data using the AWS Console, the AWS CLI, or PowerShell.

------
#### [ Console ]

**To create a data export**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Manager**.

1. Choose the **Data exports** tab.

1. Choose **Create data export**.

1. Configure your export properties, delivery location, and tags (optional).

1. Choose **Create**.

------
#### [ AWS CLI ]

**To create a data export**  
Use the following command to create a data export with the specified configuration:

```
aws ec2 create-capacity-manager-data-export \
    --s3-bucket-name my-exports-bucket \
    --s3-bucket-prefix capacity-data-exports \
    --schedule hourly \
    --output-format {{parquet/CSV}} \
    --tag-specifications 'ResourceType=capacity-manager-data-export,Tags=[{Key=environment,Value=production}]'
```

**Note**  
The `--tag-specifications` parameter in the command above applies resource tags to the data export resource itself (for example, for cost allocation or organization). These are separate from monitored tag keys, which determine the tag columns included in your exported data. For more information about monitored tag keys, see [Managing monitored tag keys](managing-monitored-tag-keys.md).

------
#### [ PowerShell ]

**To create a data export**  
Use the [New-EC2CapacityManagerDataExport](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2CapacityManagerDataExport.html) cmdlet.

```
New-EC2CapacityManagerDataExport `
    -S3BucketName "my-exports-bucket" `
    -S3BucketPrefix "capacity-data-exports" `
    -Schedule "hourly" `
    -OutputFormat "{{parquet}}" `
    -TagSpecification @([Amazon.EC2.Model.TagSpecification]@{
        ResourceType = "capacity-manager-data-export"
        Tags = @([Amazon.EC2.Model.Tag]@{
            Key   = "environment"
            Value = "production"
        })
    })
```

------

## Tag columns in data exports
<a name="create-export-tag-columns"></a>

Newly created data exports include tag values as additional columns for activated monitored tag keys and Capacity Manager-provided tags. For more information, see [Tags in data exports](managing-monitored-tag-keys.md#tags-in-data-exports) in [Managing monitored tag keys](managing-monitored-tag-keys.md).

**Note**  
If you have not activated any monitored tag keys, your exports will still include columns for Capacity Manager-provided tags (for example, `aws:autoscaling:groupName`, `aws:eks:cluster-name`, `eks:kubernetes-node-pool-name`, and `karpenter.sh/nodepool`).