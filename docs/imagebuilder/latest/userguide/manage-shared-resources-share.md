# Create an AWS RAM resource share for your Image Builder resources

To share an Image Builder component, image, or recipe, you must add it to an AWS Resource Access Manager resource share.
The resource share specifies the resources to share and the consumers with whom they are shared.

The following options are available for sharing your resources.

## Option 1: Create a RAM resource share

When you create a RAM resource share, you can share a component, image, or recipe that
you own in a single step. Use one of the following methods to create your resource share:

- ###### Console

To create your resource share using the AWS RAM console, see [Share
AWS resources owned by you](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create") in the _AWS RAM User Guide_.

- ###### AWS CLI

To create your resource share using the AWS RAM command line interface, run
the **[create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md")** command in the AWS CLI.

## Option 2: Apply a resource policy and

promote to an existing resource share

The second option for sharing your resources involves two steps, running commands in
the AWS CLI for both. The first step uses Image Builder commands in the AWS CLI to apply resource-based
policies to the shared resource. The second step promotes the resource to a RAM resource share
using the **[promote-resource-share-created-from-policy](../../../cli/latest/reference/ram/promote-resource-share-created-from-policy.md "../../../cli/latest/reference/ram/promote-resource-share-created-from-policy.md")** AWS RAM command in the AWS CLI to ensure that
the resource is visible to all principals with whom you've shared it.

1. ###### Apply the resource policy

To successfully apply the resource policy, you must ensure that the account
with which you are sharing has permission to access any underlying resources.

Choose the tab that matches your resource type for the applicable command.

Image
You can apply a resource policy to an image, to allow others to use it as the
base image in their recipes.

Run the **[put-image-policy](../../../cli/latest/reference/imagebuilder/put-image-policy.md "../../../cli/latest/reference/imagebuilder/put-image-policy.md")**
Image Builder command in the AWS CLI, to identify the AWS principals to share the image with.

```
aws imagebuilder put-image-policy --image-arn arn:aws:imagebuilder:us-west-2:123456789012:image/my-example-image/2019.12.03/1 --policy '{ "Version": "2012-10-17",		 	 	  "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": ["imagebuilder:GetImage", "imagebuilder:ListImages"], "Resource": [ "arn:aws:imagebuilder:us-west-2:123456789012:image/my-example-image/2019.12.03/1" ] } ] }'
```

Component
You can apply a resource policy to a build or test component to enable cross-account
sharing. This command gives other accounts permission to use your component in their recipes.
To successfully apply the resource policy, you must ensure that the account with which you are
sharing has permission to access any resources referenced by the shared component, such as files
hosted on private repositories.

Run the **[put-component-policy](../../../cli/latest/reference/imagebuilder/put-component-policy.md "../../../cli/latest/reference/imagebuilder/put-component-policy.md")**
Image Builder command in the AWS CLI, to identify the AWS principals to share the component with.

```
aws imagebuilder put-component-policy --component-arn arn:aws:imagebuilder:us-west-`2:123456789012`:component/`my-example-component`/2019.12.03/1 --policy '{ "Version": "2012-10-17",		 	 	  "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": [ "imagebuilder:GetComponent", "imagebuilder:ListComponents" ], "Resource": [ "arn:aws:imagebuilder:us-west-`2:123456789012`:component/`my-example-component`/2019.12.03/1" ] } ] }'
```

Image recipe
You can apply a resource policy to an image recipe to enable cross-account sharing. This command
gives other accounts permission to use your recipe to create images in their accounts. To
successfully apply the resource policy, you must ensure that the account with which you are
sharing has permission to access any resources that the recipe references, such as the base image,
or selected components.

Run the **[put-image-recipe-policy](../../../cli/latest/reference/imagebuilder/put-image-recipe-policy.md "../../../cli/latest/reference/imagebuilder/put-image-recipe-policy.md")**
Image Builder command in the AWS CLI, to identify the AWS principals to share the image with.

```
aws imagebuilder put-image-recipe-policy --image-recipe-arn arn:aws:imagebuilder:us-west-`2:123456789012`:image-recipe/`my-example-image-recipe`/2019.12.03 --policy '{ "Version": "2012-10-17",		 	 	  "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": [ "imagebuilder:GetImageRecipe", "imagebuilder:ListImageRecipes" ], "Resource": [ "arn:aws:imagebuilder:us-west-`2:123456789012`:image-recipe/`my-example-image-recipe`/2019.12.03" ] } ] }'
```

Container recipe
You can apply a resource policy to a container recipe to enable cross-account sharing. This command
gives other accounts permission to use your recipe to create images in their accounts. To
successfully apply the resource policy, you must ensure that the account with which you are
sharing has permission to access any resources that the recipe references, such as the base image,
or selected components.

Run the **[put-container-recipe-policy](../../../cli/latest/reference/imagebuilder/put-container-recipe-policy.md "../../../cli/latest/reference/imagebuilder/put-container-recipe-policy.md")**
Image Builder command in the AWS CLI, to identify the AWS principals to share the image with.

```
aws imagebuilder put-container-recipe-policy --container-recipe-arn arn:aws:imagebuilder:us-west-`2:123456789012`:container-recipe/`my-example-container-recipe`/2021.12.03 --policy '{ "Version": "2012-10-17",		 	 	  "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": [ "imagebuilder:GetContainerRecipe", "imagebuilder:ListContainerRecipes" ], "Resource": [ "arn:aws:imagebuilder:us-west-`2:123456789012`:container-recipe/`my-example-container-recipe`/2021.12.03" ] } ] }'
```

###### Note

To set the correct policies for sharing and unsharing a resource, the resource
owner must have `imagebuilder:put*` permissions. 2. ###### Promote as a RAM resource share

To ensure that the resource is visible to all principals with whom you've
shared it, run the **[promote-resource-share-created-from-policy](../../../cli/latest/reference/ram/promote-resource-share-created-from-policy.md "../../../cli/latest/reference/ram/promote-resource-share-created-from-policy.md")** AWS RAM command
in the AWS CLI.
