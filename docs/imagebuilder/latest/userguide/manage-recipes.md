

# Manage recipes in Image Builder
<a name="manage-recipes"></a>

An EC2 Image Builder recipe is the blueprint for creating a customized machine image. A recipe specifies three key elements:

1. **Base image** – The starting point for your image (an AMI, a container image, or an imported VM).

1. **Components** – The build and test steps that customize your image. Components are optional. This design supports testing and distribution-only workflows.

1. **Configuration** – Storage volumes, instance settings, the working directory, and other build-time parameters.

Image Builder supports two types of recipes:
+ **Image recipes** produce Amazon Machine Images (AMIs) that you can use to launch Amazon EC2 instances.
+ **Container recipes** produce Docker container images stored in Amazon ECR repositories.

Recipes are immutable. After you create a recipe, you can't modify or replace it. To update components or any other configuration, you must create a new recipe or recipe version. Image Builder retains all previous versions. This lets you trace image lineage back to the exact recipe that produced each output. You can always apply tags to your existing recipes. For more information about tagging your resources using Image Builder commands in the AWS CLI, see the [Tag resources](tag-resources.md) section of this guide.

**Tip**  
You can use Amazon managed components in your recipes, or you can develop your own custom components. For more information, see [Develop custom components for your Image Builder image](create-custom-components.md). For image recipes that create output AMIs, you can also use AWS Marketplace image products and components. For more information about integration with AWS Marketplace products, see [AWS Marketplace integration in Image Builder](integ-marketplace.md).

Use the topics in this section to manage your EC2 Image Builder recipes, including listing existing recipes, viewing their details, and creating new recipe versions.

**Topics**
+ [Image recipes compared to container recipes](#recipe-types-comparison)
+ [Recipe versioning](#recipe-versioning)
+ [Recipe constraints and limits](#recipe-constraints)
+ [List and view image recipe details](image-recipe-details.md)
+ [List and view container recipe details](container-recipe-details.md)
+ [Create a new version of an image recipe](create-image-recipes.md)
+ [Create a new version of a container recipe](create-container-recipes.md)
+ [Track AMI lineage with watermarks](ami-watermarks.md)
+ [Clean up resources](#recipes-cleanup)

## Image recipes compared to container recipes
<a name="recipe-types-comparison"></a>

The following table compares the features of image recipes and container recipes.


| Feature | Image recipe | Container recipe | 
| --- | --- | --- | 
| Output | AMI | Docker container image in Amazon ECR | 
| Base image sources | AMI ID, Image Builder image ARN, SSM parameter, AWS Marketplace product | Docker Hub image, Amazon ECR image, Amazon-managed image, Image Builder image ARN | 
| Dockerfile | Not applicable | Required (template with contextual variables) | 
| Target repository | Not applicable | Amazon ECR (required) | 
| Storage configuration | Block device mappings for the output AMI | Block device mappings for the build instance | 
| User data | Supported (overrides default cloud-init) | Not supported at recipe level | 
| Systems Manager agent control | Configurable (uninstall after build) | Not configurable | 
| AWS Marketplace components | Supported | Not supported | 
| Platform override | Not applicable (detected from AMI) | Available for Amazon ECR and Docker Hub images | 

## Recipe versioning
<a name="recipe-versioning"></a>

Every recipe uses semantic versioning in the format *<major>.<minor>.<patch>*. Each version node accepts values from 0 to 1,073,741,823 (2^30 - 1).

You can use a wildcard (`x`) in one position to enable automatic version incrementing. When you create a recipe with a wildcard version, Image Builder replaces the `x` with the next available number for that position.


| Pattern | Behavior | Example sequence | 
| --- | --- | --- | 
| 1.0.x | Increments the patch number | 1.0.1, 1.0.2, 1.0.3, ... | 
| 1.x.0 | Increments the minor number | 1.1.0, 1.2.0, 1.3.0, ... | 
| x.0.0 | Increments the major number | 1.0.0, 2.0.0, 3.0.0, ... | 

The following rules apply to wildcard versions:
+ Only one `x` wildcard is allowed per version string.
+ The wildcard can appear in any single position (major, minor, or patch).
+ The numeric values in the remaining positions must be explicit integers.

**Tip**  
Use wildcard versions in your CI/CD automation so that you don't have to track and increment recipe versions by hand. Each time you create a recipe with the same wildcard, Image Builder resolves the next available version. For example, a recipe that always uses `1.0.x` resolves to `1.0.1`, then `1.0.2`, and so on. To learn more about semantic versioning for Image Builder resources, see [Semantic versioning in Image Builder](ibhow-semantic-versioning.md).

## Recipe constraints and limits
<a name="recipe-constraints"></a>

Before you create a recipe, review the following constraints.


| Constraint | Limit | Notes | 
| --- | --- | --- | 
| Components per recipe | 20 (default) | Includes both build and test components. You can request an increase through AWS Support. | 
| Maximum recipe size | 25 KB | The cumulative size of all component configurations, including parameter values. | 
| Product codes per output image | 9 | Combined from the base image and AWS Marketplace components. | 
| Component uniqueness | One per recipe | The same component (regardless of version) can appear only once. | 
| Version node maximum | 1,073,741,823 | Per node (major, minor, or patch). | 
| Recipe name | Cannot be changed | The name is fixed after creation. Create a new recipe for a different name. | 

Components must also meet the following compatibility requirements:
+ Components must match the recipe's platform (Linux, Windows, or macOS).
+ Components must support the parent image's OS version, when OS version metadata is available.
+ Components with a `DEPRECATED` or `DISABLED` status can't be added to new recipes.
+ CIS hardening components require a CIS-published parent image.

## Clean up resources
<a name="recipes-cleanup"></a>

To avoid unexpected charges, make sure to clean up resources and pipelines that you created from the examples in this guide. For more information about deleting resources in Image Builder, see [Delete outdated or unused Image Builder resources](delete-resources.md).