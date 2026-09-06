

# List and view container recipe details
<a name="container-recipe-details"></a>

This section describes the ways that you can find information and view details for your EC2 Image Builder container recipes.

**Topics**
+ [List container recipes in the console](#list-container-recipes-console)
+ [List container recipes with the AWS CLI](#cli-list-container-recipes)
+ [View container recipe details in the console](#view-container-recipe-details-console)
+ [Get container recipe details with the AWS CLI](#cli-get-container-recipe)
+ [Get container recipe policy details with the AWS CLI](#cli-get-container-recipe-policy)

## List container recipes in the console
<a name="list-container-recipes-console"></a>

To see a list of the container recipes that have been created under your account in the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Container recipes** from the navigation pane. This shows a list of the container recipes that are created under your account.

1. To view details or create a new recipe version, choose the **Recipe name** link. This opens the detail view for the recipe.
**Note**  
You can also select the check box next to the **Recipe name**, and then choose **View details**.

## List container recipes with the AWS CLI
<a name="cli-list-container-recipes"></a>

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

You can filter the results by owner to control which recipes the command returns. Use `Self` to list the recipes that you own, or `Shared` to list recipes that other accounts have shared with you.

```
aws imagebuilder list-container-recipes --owner Self
```

To limit the number of results that the command returns on each page, use the `--max-results` parameter. If more results are available, the response includes a `nextToken` value that you pass to the next command to retrieve the following page.

```
aws imagebuilder list-container-recipes --max-results 10 --next-token "{{eyJuZXh0VG9rZW4...}}"
```

## View container recipe details in the console
<a name="view-container-recipe-details-console"></a>

To view details for a specific container recipe with the Image Builder console, select the container recipe to review, and use the steps described in [List container recipes in the console](#list-container-recipes-console).

On the recipe detail page, you can do the following:
+ Delete the recipe. For more information on how to delete resources in Image Builder, see [Delete outdated or unused Image Builder resources](delete-resources.md).
+ Create a new version.
+ Create a pipeline from the recipe. After you choose **Create pipeline from this recipe**, the console opens the pipeline wizard. For more information about creating an Image Builder pipeline using the pipeline wizard, see [Tutorial: Create an image pipeline with output AMI from the Image Builder console wizard](start-build-image-pipeline.md)
**Note**  
When you create a pipeline from an existing recipe, the option to create a new recipe isn't available.

## Get container recipe details with the AWS CLI
<a name="cli-get-container-recipe"></a>

The following example shows how to use an **imagebuilder** CLI command to get the details of a container recipe by specifying its ARN.

```
aws imagebuilder get-container-recipe --container-recipe-arn arn:aws:imagebuilder:us-west-{{2:123456789012}}:container-recipe/{{my-container-recipe}}/1.0.2
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

## Get container recipe policy details with the AWS CLI
<a name="cli-get-container-recipe-policy"></a>

A recipe policy is a resource-based policy. It controls cross-account access to your recipe. When you share a recipe through AWS Resource Access Manager (AWS RAM), Image Builder creates the policy automatically. You can also set a custom policy with the `put-container-recipe-policy` command.

The following example shows how to use an **imagebuilder** CLI command to get the details of a container recipe policy by specifying its ARN. If no policy is attached to the recipe, the response is empty.

```
aws imagebuilder get-container-recipe-policy --container-recipe-arn arn:aws:imagebuilder:us-west-{{2:123456789012}}:container-recipe/{{my-container-recipe}}/1.0.2
```