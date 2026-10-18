

# List and view container recipe details
<a name="container-recipe-details"></a>

This section describes the ways that you can find information and view details for your EC2 Image Builder container recipes.

**Topics**
+ [List container recipes](#list-container-recipes-console)
+ [View container recipe details](#view-container-recipe-details-console)
+ [Get container recipe policy details](#cli-get-container-recipe-policy)

## List container recipes
<a name="list-container-recipes-console"></a>

You can list all of your container recipes, or filter the results by owner. Use `Self` to list the recipes that you own, or `Shared` to list recipes that other accounts have shared with you.

------
#### [ Console ]

To see a list of the container recipes created under your account, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Container recipes** from the navigation pane. This shows a list of the container recipes that are created under your account.

1. To view details or create a new recipe version, choose the **Recipe name** link. This opens the detail view for the recipe.
**Note**  
You can also select the check box next to the **Recipe name**, and then choose **View details**.

------
#### [ AWS CLI ]

The following example shows how to list all of your container recipes, using the AWS CLI.

```
aws imagebuilder list-container-recipes
```

The command returns a summary for each container recipe, shown in the following example output.

```
{
    "requestId": "{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
    "containerRecipeSummaryList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:{{123456789012}}:container-recipe/{{my-container-recipe}}/1.0.0",
            "name": "{{my-container-recipe}}",
            "containerType": "DOCKER",
            "platform": "Linux",
            "owner": "{{123456789012}}",
            "dateCreated": "2024-01-15T10:30:00.000Z",
            "tags": {}
        }
    ]
}
```

The following example lists only the recipes that you own:

```
aws imagebuilder list-container-recipes --owner Self
```

------
#### [ PowerShell ]

The following example shows how to use the [Get-EC2IBContainerRecipeList](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBContainerRecipeList.html) cmdlet to list all of your container recipes:

```
Get-EC2IBContainerRecipeList
```

The following example lists only the recipes that you own:

```
Get-EC2IBContainerRecipeList -Owner Self
```

------

## View container recipe details
<a name="view-container-recipe-details-console"></a>

------
#### [ Console ]

To view details for a specific container recipe, select the container recipe to review, and use the steps described in [List container recipes](#list-container-recipes-console).

On the recipe detail page, you can do the following:
+ Delete the recipe. For more information on how to delete resources in Image Builder, see [Delete outdated or unused Image Builder resources](delete-resources.md).
+ Create a new version.
+ Create a pipeline from the recipe. After you choose **Create pipeline from this recipe**, the console opens the pipeline wizard. For more information about creating an Image Builder pipeline using the pipeline wizard, see [Tutorial: Create an image pipeline with output AMI from the Image Builder console wizard](start-build-image-pipeline.md)
**Note**  
When you create a pipeline from an existing recipe, the option to create a new recipe isn't available.

------
#### [ AWS CLI ]

The following example shows how to use an **imagebuilder** CLI command to get the details of a container recipe by specifying its ARN.

```
aws imagebuilder get-container-recipe --container-recipe-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:container-recipe/{{my-container-recipe}}/1.0.2
```

The command returns the full container recipe, shown in the following example output.

```
{
    "requestId": "{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
    "containerRecipe": {
        "arn": "arn:aws:imagebuilder:us-west-2:{{123456789012}}:container-recipe/{{my-container-recipe}}/1.0.2",
        "containerType": "DOCKER",
        "name": "{{my-container-recipe}}",
        "description": "{{My Linux Docker container image}}",
        "platform": "Linux",
        "components": [
            {
                "componentArn": "arn:aws:imagebuilder:us-west-2:{{123456789012}}:component/{{my-component}}/1.0.0/1"
            }
        ],
        "parentImage": "amazonlinux:latest",
        "dockerfileTemplateData": "FROM {{{ imagebuilder:parentImage }}}\n{{{ imagebuilder:environments }}}\n{{{ imagebuilder:components }}}",
        "targetRepository": {
            "service": "ECR",
            "repositoryName": "{{my-repo}}"
        },
        "dateCreated": "2024-01-15T10:30:00.000Z",
        "owner": "{{123456789012}}"
    }
}
```

------
#### [ PowerShell ]

The following example shows how to use the [Get-EC2IBContainerRecipe](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBContainerRecipe.html) cmdlet to get the details of a container recipe by specifying its Amazon Resource Name (ARN):

```
Get-EC2IBContainerRecipe -ContainerRecipeArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:container-recipe/{{my-container-recipe}}/1.0.2
```

------

## Get container recipe policy details
<a name="cli-get-container-recipe-policy"></a>

A recipe policy is a resource-based policy. It controls cross-account access to your recipe. When you share a recipe through AWS Resource Access Manager (AWS RAM), Image Builder creates the policy automatically. You can also set a custom policy with the `put-container-recipe-policy` command.

------
#### [ AWS CLI ]

The following example shows how to use an **imagebuilder** CLI command to get the details of a container recipe policy by specifying its ARN. If no policy is attached to the recipe, the response is empty.

```
aws imagebuilder get-container-recipe-policy --container-recipe-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:container-recipe/{{my-container-recipe}}/1.0.2
```

------
#### [ PowerShell ]

The following example shows how to use the [Get-EC2IBContainerRecipePolicy](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBContainerRecipePolicy.html) cmdlet to get the details of a container recipe policy by specifying its ARN:

```
Get-EC2IBContainerRecipePolicy -ContainerRecipeArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:container-recipe/{{my-container-recipe}}/1.0.2
```

The cmdlet returns the policy as a JSON string. If no policy is attached to the recipe, the cmdlet returns `{}`.

------