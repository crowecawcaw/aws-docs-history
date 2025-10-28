# List and view container recipe details

This section describes the ways that you can find information and view details for your
EC2 Image Builder container recipes.

###### Container recipe details

- [List container recipes in the
  console](#list-container-recipes-console "#list-container-recipes-console")
- [List container recipes with the
  AWS CLI](#cli-list-container-recipes "#cli-list-container-recipes")
- [View container recipe details in
  the console](#view-container-recipe-details-console "#view-container-recipe-details-console")
- [Get container recipe details with the
  AWS CLI](#cli-get-container-recipe "#cli-get-container-recipe")
- [Get container recipe policy details
  with the AWS CLI](#cli-get-container-recipe-policy "#cli-get-container-recipe-policy")

## List container recipes in the

console

To see a list of the container recipes that have been created under your account in
the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Container recipes**
   from the navigation pane. This shows a list of the
   container recipes that are created under your account.
3. To view details or create a new recipe version, choose
   the **Recipe name** link. This opens the
   detail view for the recipe.

###### Note

You can also select the check box next to the **Recipe
name**, and then choose **View
details**.

## List container recipes with the

AWS CLI

The following example shows how to list all of your container
recipes, using the AWS CLI.

```
aws imagebuilder list-container-recipes
```

## View container recipe details in

the console

To view details for a specific container recipe with the Image Builder console, select the
container recipe to review, and use the steps described in [List container recipes in the
console](#list-container-recipes-console "#list-container-recipes-console").

On the recipe detail page, you can do the following:

- Delete the recipe. For more information on how to delete resources in Image Builder,
  see [Delete outdated or unused Image Builder resources](delete-resources.md "delete-resources.md").
- Create a new version.
- Create a pipeline from the recipe. After ou choose **Create pipeline
  from this recipe**, you are taken to the pipeline wizard. For more
  information on how to create an Image Builder pipeline using the pipeline wizard, see
  [Tutorial: Create an image
  pipeline with output AMI from the Image Builder console wizard](start-build-image-pipeline.md "start-build-image-pipeline.md")

###### Note

When you create a pipeline from an existing recipe, the option to create a
new recipe isn't available.

## Get container recipe details with the

AWS CLI

The following example shows how to use an **imagebuilder**
CLI command to get the details of a container recipe by specifying its ARN.

```
aws imagebuilder get-container-recipe --container-recipe-arn arn:aws:imagebuilder:us-west-`2:123456789012`:container-recipe/`my-example-recipe`/2020.12.03
```

## Get container recipe policy details

with the AWS CLI

The following example shows how to use an **imagebuilder** CLI command
to get the details of a container recipe policy by specifying its ARN.

```
aws imagebuilder get-container-recipe-policy --container-recipe-arn arn:aws:imagebuilder:us-west-`2:123456789012`:container-recipe/`my-example-recipe`/2020.12.03
```
