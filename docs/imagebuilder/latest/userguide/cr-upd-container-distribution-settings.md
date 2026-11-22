

# Create and update distribution settings for container images

This section covers creating and updating distribution settings for Image Builder container images.

**Topics**
+ [Create distribution settings for Image Builder container images](#cli-create-container-distribution-configuration)
+ [Update distribution settings for your container image](#cli-update-container-distribution-configuration)

## Create distribution settings for Image Builder container images
<a name="cli-create-container-distribution-configuration"></a>

A distribution configuration enables you to specify the name and description of your output container image and replicate the container image to other AWS Regions. You can also apply separate tags to the distribution configuration resource and to the container images within each Region.

You can create distribution settings for your container image from the AWS CLI or AWS Tools for PowerShell.

------
#### [ AWS CLI ]

1. 

**Create a CLI input JSON file**

   Use your favorite file-editing tool to create a JSON file with the keys shown in the following example, plus values that are valid for your environment. This example uses a file named `create-container-distribution-configuration.json`:

   ```json
   {
   	"name": "distribution-configuration-name",
   	"description": "Distributes container image to Amazon ECR repository in two Regions.",
   	"distributions": [
   		{
   			"region": "us-west-2",
   			"containerDistributionConfiguration": {
   				"description": "My test image.",
   				"targetRepository": {
   					"service": "ECR",
   					"repositoryName": "testrepo"
   				},
   				"containerTags": ["west2", "image1"]
   			}
   		},
   		{
   			"region": "us-east-1",
   			"containerDistributionConfiguration": {
   				"description": "My test image.",
   				"targetRepository": {
   					"service": "ECR",
   					"repositoryName": "testrepo"
   				},
   			   "containerTags": ["east1", "imagedist"]
   			}
   		}
   	],
   	"tags": {
   	   "DistributionConfigurationTestTagKey1": "DistributionConfigurationTestTagValue1",
   	   "DistributionConfigurationTestTagKey2": "DistributionConfigurationTestTagValue2"
   	}
   }
   ```

1. 

**Run the following command, using the file you created as input.**

   ```
   aws imagebuilder create-distribution-configuration --cli-input-json file://{{create-container-distribution-configuration.json}}
   ```
**Note**  
You must include the `file://` notation at the beginning of the JSON file path.
The path for the JSON file should follow the appropriate convention for the base operating system where you are running the command. For example, Windows uses the backslash (\\) to refer to the directory path, while Linux and macOS use the forward slash (/).

   For more detailed information, see [create-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html) in the *AWS CLI Command Reference*.

------
#### [ PowerShell ]

The following example uses the same settings as the AWS CLI example. Each top-level JSON key is a cmdlet parameter, such as `Name`, `Description`, `Distribution`, and `Tag`. Build each distribution as an `Amazon.Imagebuilder.Model.Distribution` object. The `Tag` parameter takes a hashtable.

The following example shows how to use the [New-EC2IBDistributionConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2IBDistributionConfiguration.html) cmdlet to create distribution settings for a container image:

```ps
Import-Module AWS.Tools.Imagebuilder
$usWest2 = [Amazon.Imagebuilder.Model.Distribution]@{
    Region = "us-west-2"
    ContainerDistributionConfiguration = [Amazon.Imagebuilder.Model.ContainerDistributionConfiguration]@{
        Description = "My test image."
        TargetRepository = [Amazon.Imagebuilder.Model.TargetContainerRepository]@{
            Service = "ECR"
            RepositoryName = "testrepo"
        }
        ContainerTags = @("west2", "image1")
    }
}

$usEast1 = [Amazon.Imagebuilder.Model.Distribution]@{
    Region = "us-east-1"
    ContainerDistributionConfiguration = [Amazon.Imagebuilder.Model.ContainerDistributionConfiguration]@{
        Description = "My test image."
        TargetRepository = [Amazon.Imagebuilder.Model.TargetContainerRepository]@{
            Service = "ECR"
            RepositoryName = "testrepo"
        }
        ContainerTags = @("east1", "imagedist")
    }
}

New-EC2IBDistributionConfiguration -Name distribution-configuration-name `
    -Description "Distributes container image to Amazon ECR repository in two Regions." `
    -Distribution $usWest2, $usEast1 `
    -Tag @{
        DistributionConfigurationTestTagKey1 = "DistributionConfigurationTestTagValue1"
        DistributionConfigurationTestTagKey2 = "DistributionConfigurationTestTagValue2"
    }
```

------

## Update distribution settings for your container image
<a name="cli-update-container-distribution-configuration"></a>

You can update distribution settings for your container image from the AWS CLI or AWS Tools for PowerShell. You can also update tags for the container images within each Region. To update tags for your distribution configuration resource, see the [Tag resources](tag-resources.md) section.

**Note**  
The **update-distribution-configuration** command and the [Update-EC2IBDistributionConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-EC2IBDistributionConfiguration.html) cmdlet replace the entire distribution configuration. The distributions list that you provide replaces the existing distributions—include every Region that you want to keep.  
To prevent unintended removal of existing settings, retrieve the current configuration with the **get-distribution-configuration** command or the [Get-EC2IBDistributionConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBDistributionConfiguration.html) cmdlet, and use the output as the basis for your update request.

------
#### [ AWS CLI ]

The following example shows how to use the [update-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-distribution-configuration.html) command to update distribution settings for your container image, using the AWS CLI.

1. 

**Create a CLI input JSON file**

   Use your favorite file-editing tool to create a JSON file with keys shown in the following example, plus values that are valid for your environment. This example uses a file named `update-container-distribution-configuration.json`:

   ```json
   {
   	"distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/update-container-distribution-configuration",
   	"description": "Distributes container image to Amazon ECR repository in two Regions.",
   	"distributions": [
   		{
   			"region": "us-west-2",
   			"containerDistributionConfiguration": {
   				"description": "My test image.",
   				"targetRepository": {
   					"service": "ECR",
   					"repositoryName": "testrepo"
   				},
   				"containerTags": ["west2", "image1"]
   			}
   		},
   		{
   			"region": "us-east-2",
   			"containerDistributionConfiguration": {
   				"description": "My test image.",
   				"targetRepository": {
   					"service": "ECR",
   					"repositoryName": "testrepo"
   				},
   			   "containerTags": ["east2", "imagedist"]
   			}
   		}
   	]
   }
   ```

1. 

**Run the following command, using the file you created as input:**

   ```
   aws imagebuilder update-distribution-configuration --cli-input-json file://{{update-container-distribution-configuration.json}}
   ```
**Note**  
You must include the `file://` notation at the beginning of the JSON file path.
The path for the JSON file should follow the appropriate convention for the base operating system where you are running the command. For example, Windows uses the backslash (\\) to refer to the directory path, while Linux and macOS use the forward slash (/).

   For more detailed information, see [update-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-distribution-configuration.html) in the *AWS CLI Command Reference*.

------
#### [ PowerShell ]

The following example uses the same settings as the AWS CLI example. Each top-level JSON key is a cmdlet parameter, such as `DistributionConfigurationArn`, `Description`, and `Distribution`. Build each distribution as an `Amazon.Imagebuilder.Model.Distribution` object.

The following example shows how to use the `Update-EC2IBDistributionConfiguration` cmdlet to update distribution settings for your container image:

```ps
Import-Module AWS.Tools.Imagebuilder
$usWest2 = [Amazon.Imagebuilder.Model.Distribution]@{
    Region = "us-west-2"
    ContainerDistributionConfiguration = [Amazon.Imagebuilder.Model.ContainerDistributionConfiguration]@{
        Description = "My test image."
        TargetRepository = [Amazon.Imagebuilder.Model.TargetContainerRepository]@{
            Service = "ECR"
            RepositoryName = "testrepo"
        }
        ContainerTags = @("west2", "image1")
    }
}

$usEast2 = [Amazon.Imagebuilder.Model.Distribution]@{
    Region = "us-east-2"
    ContainerDistributionConfiguration = [Amazon.Imagebuilder.Model.ContainerDistributionConfiguration]@{
        Description = "My test image."
        TargetRepository = [Amazon.Imagebuilder.Model.TargetContainerRepository]@{
            Service = "ECR"
            RepositoryName = "testrepo"
        }
        ContainerTags = @("east2", "imagedist")
    }
}

Update-EC2IBDistributionConfiguration -DistributionConfigurationArn arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/update-container-distribution-configuration `
    -Description "Distributes container image to Amazon ECR repository in two Regions." `
    -Distribution $usWest2, $usEast2
```

------