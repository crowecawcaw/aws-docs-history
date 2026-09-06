

# List and view image recipe details
<a name="image-recipe-details"></a>

This section describes the various ways that you can find information and view details for your EC2 Image Builder image recipes.

**Topics**
+ [List image recipes from the console](#list-image-recipes-console)
+ [List image recipes from the AWS CLI](#cli-list-image-recipes)
+ [View image recipe details from the console](#view-image-recipe-details-console)
+ [Get image recipe details from the AWS CLI](#cli-get-image-recipe)
+ [Get image recipe policy details from the AWS CLI](#cli-get-image-recipe-policy)

## List image recipes from the console
<a name="list-image-recipes-console"></a>

To see a list of the image recipes created under your account in the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Image recipes** from the navigation pane. This shows a list of the image recipes that are created under your account.

1. To view details or create a new recipe version, choose the **Recipe name** link. This opens the detail view for the recipe.
**Note**  
You can also select the check box next to the **Recipe name**, then choose **View details**.

## List image recipes from the AWS CLI
<a name="cli-list-image-recipes"></a>

The following example shows how to list all of your image recipes, using the AWS CLI.

```
aws imagebuilder list-image-recipes
```

The command returns a summary for each image recipe, shown in the following example output.

```
{
    "requestId": "{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
    "imageRecipeSummaryList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:{{123456789012}}:image-recipe/{{my-recipe}}/1.0.0",
            "name": "{{my-recipe}}",
            "platform": "Linux",
            "owner": "{{123456789012}}",
            "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/{{amazon-linux-2023-x86}}/x.x.x",
            "dateCreated": "2024-01-15T10:30:00.000Z",
            "tags": {
                "Environment": "Production"
            }
        }
    ]
}
```

You can filter the results by owner to control which recipes the command returns.

```
aws imagebuilder list-image-recipes --owner Self
```

Use `Self` to list the recipes that you own, or `Shared` to list recipes that other accounts have shared with you.

```
aws imagebuilder list-image-recipes --owner Shared
```

To limit the number of results that the command returns on each page, use the `--max-results` parameter. If more results are available, the response includes a `nextToken` value that you pass to the next command to retrieve the following page.

```
aws imagebuilder list-image-recipes --max-results 10 --next-token "{{eyJuZXh0VG9rZW4...}}"
```

## View image recipe details from the console
<a name="view-image-recipe-details-console"></a>

To view details for a specific image recipe using the Image Builder console, select the image recipe to review, using the steps described in [List image recipes from the console](#list-image-recipes-console).

On the recipe detail page, you can:
+ Delete the recipe. For more information about deleting resources in Image Builder, see [Delete outdated or unused Image Builder resources](delete-resources.md).
+ Create a new version.
+ Create a pipeline from the recipe. After choosing **Create pipeline from this recipe**, you are taken to the pipeline wizard. For more information about creating an Image Builder pipeline using the pipeline wizard, see [Tutorial: Create an image pipeline with output AMI from the Image Builder console wizard](start-build-image-pipeline.md)
**Note**  
When you create a pipeline from an existing recipe, the option to create a new recipe is not available.

## Get image recipe details from the AWS CLI
<a name="cli-get-image-recipe"></a>

The following example shows how to use an **imagebuilder** CLI command to get the details of an image recipe by specifying its Amazon Resource Name (ARN).

```
aws imagebuilder get-image-recipe --image-recipe-arn arn:aws:imagebuilder:us-west-{{2:123456789012}}:image-recipe/{{my-recipe}}/1.0.0
```

The command returns the full image recipe, shown in the following example output.

```
{
    "requestId": "{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
    "imageRecipe": {
        "arn": "arn:aws:imagebuilder:us-west-2:{{123456789012}}:image-recipe/{{my-recipe}}/1.0.0",
        "name": "{{my-recipe}}",
        "description": "{{My Linux image recipe}}",
        "platform": "Linux",
        "version": "1.0.0",
        "components": [
            {
                "componentArn": "arn:aws:imagebuilder:us-west-2:{{123456789012}}:component/{{my-component}}/1.0.0/1"
            }
        ],
        "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/{{amazon-linux-2023-x86}}/x.x.x",
        "dateCreated": "2024-01-15T10:30:00.000Z",
        "tags": {},
        "owner": "{{123456789012}}"
    }
}
```

## Get image recipe policy details from the AWS CLI
<a name="cli-get-image-recipe-policy"></a>

A recipe policy is a resource-based policy. It controls cross-account access to your recipe. When you share a recipe through AWS Resource Access Manager (AWS RAM), Image Builder creates the policy automatically. You can also set a custom policy with the `put-image-recipe-policy` command.

**Note**  
If you set the resource policy directly with `put-image-recipe-policy`, you must then promote the resource to a AWS RAM resource share so that it's visible to the principals you share it with. For more information, see [Option 2: Apply a resource policy and promote to an existing resource share](manage-shared-resources-share.md#share-opt2-promote-resource-share).

The following example shows how to use an **imagebuilder** CLI command to get the details of an image recipe policy by specifying its ARN. If no policy is attached to the recipe, the response is empty.

```
aws imagebuilder get-image-recipe-policy --image-recipe-arn arn:aws:imagebuilder:us-west-{{2:123456789012}}:image-recipe/{{my-recipe}}/1.0.0
```