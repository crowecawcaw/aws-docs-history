# Manage recipes in Image Builder

An EC2 Image Builder recipe defines the base image to use as your starting point to create a new
image, along with the set of components that you add to customize your image and verify that
everything works as expected. Image Builder provides automatic version choices for each component.
By default, you can apply up to 20 components to a recipe. This includes both build and
test components.

After you create a recipe, you can't modify or replace it. To update components
after you create a recipe, you must create a new recipe or recipe version. You can
always apply tags to your existing recipes. For more information about tagging your resources using Image Builder commands
in the AWS CLI, see the [Tag resources](tag-resources.md "tag-resources.md")
section of this guide.

###### Tip

You can use Amazon managed components in your recipes, or you can develop your own custom
components. For more information, see [Develop custom components for your Image Builder image](create-custom-components.md "create-custom-components.md").
For image recipes that create output AMIs, you can also use AWS Marketplace image products and
components. For more information about integration with AWS Marketplace products, see
[AWS Marketplace integration in Image Builder](integ-marketplace.md "integ-marketplace.md").

This section covers how to list, view, and create recipes.

###### Contents

- [List and view image recipe details](image-recipe-details.md "image-recipe-details.md")
- [List and view container recipe details](container-recipe-details.md "container-recipe-details.md")
- [Create a new version of an image recipe](create-image-recipes.md "create-image-recipes.md")
- [Create a new version of a container recipe](create-container-recipes.md "create-container-recipes.md")
- [Clean up resources](#recipes-cleanup "#recipes-cleanup")

## Clean up resources

To avoid unexpected charges, make sure to clean up resources
and pipelines that you created from the examples in this guide.
For more information about deleting resources in Image Builder, see
[Delete outdated or unused Image Builder resources](delete-resources.md "delete-resources.md").
