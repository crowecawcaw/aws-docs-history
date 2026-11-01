

# Create an AWS RAM resource share for your Image Builder resources
<a name="manage-shared-resources-share"></a>

To share an Image Builder component, image, or recipe, you must add it to an AWS Resource Access Manager resource share. The resource share specifies the resources to share and the consumers with whom they are shared.

The following options are available for sharing your resources.

## Option 1: Create a RAM resource share
<a name="share-opt1-create-resource-share"></a>

When you create a RAM resource share, you can share a component, image, or recipe that you own in a single step. Use one of the following methods to create your resource share:
+ 

**Console**  
To create your resource share using the AWS RAM console, see [Share AWS resources owned by you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.
+ 

**AWS CLI**  
To create your resource share using the AWS RAM command line interface, run the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command in the AWS CLI.
+ 

**PowerShell**  
To create your resource share using AWS Tools for PowerShell, run the [New-RAMResourceShare](https://docs.aws.amazon.com/powershell/latest/reference/items/New-RAMResourceShare.html) cmdlet from the `AWS.Tools.RAM` module.

## Option 2: Apply a resource policy and promote to an existing resource share
<a name="share-opt2-promote-resource-share"></a>

The second option for sharing your resources involves two steps, running commands in the AWS CLI or AWS Tools for PowerShell for both. The first step uses Image Builder commands to apply resource-based policies to the shared resource. The second step promotes the resource to a RAM resource share, so that the resource is visible to all principals with whom you've shared it.

1. 

**Apply the resource policy**

   To successfully apply the resource policy, you must make sure that the account that you share with has permission to access any underlying resources.

   For each resource type that you can share, choose the tab for the tool that you use.

   In the PowerShell examples, each cmdlet takes the Amazon Resource Name (ARN) of the resource and the policy document. The `Policy` parameter takes the policy JSON as a string. Each example stores the policy in the `$policy` variable as a single-quoted here-string.

**Image**  
You can apply a resource policy to an image, to allow others to use it as the base image in their recipes. 

------
#### [ AWS CLI ]

   To identify the AWS principals to share the image with, run the [put-image-policy](https://docs.aws.amazon.com/cli/latest/reference//imagebuilder/put-image-policy.html) Image Builder command in the AWS CLI:

   ```
   aws imagebuilder put-image-policy \
       --image-arn arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-image/2019.12.03/1 \
       --policy '{
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "444455556666"
                   ]
               },
               "Action": [
                   "imagebuilder:GetImage",
                   "imagebuilder:ListImages"
               ],
               "Resource": [
                   "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-image/2019.12.03/1"
               ]
           }
       ]
   }'
   ```

------
#### [ PowerShell ]

   To identify the AWS principals to share the image with, run the [Write-EC2IBImagePolicy](https://docs.aws.amazon.com/powershell/latest/reference/items/Write-EC2IBImagePolicy.html) cmdlet:

   ```
   $policy = @'
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "444455556666"
                   ]
               },
               "Action": [
                   "imagebuilder:GetImage",
                   "imagebuilder:ListImages"
               ],
               "Resource": [
                   "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-image/2019.12.03/1"
               ]
           }
       ]
   }
   '@
   Write-EC2IBImagePolicy -ImageArn arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-image/2019.12.03/1 `
       -Policy $policy
   ```

------

**Component**  
You can apply a resource policy to a build or test component to enable cross-account sharing. This policy gives other accounts permission to use your component in their recipes. The account that you share with must have permission to access any resources that the component references. For example, the component might reference files in private repositories.

------
#### [ AWS CLI ]

   To identify the AWS principals to share the component with, run the [put-component-policy](https://docs.aws.amazon.com/cli/latest/reference//imagebuilder/put-component-policy.html) Image Builder command in the AWS CLI:

   ```
   aws imagebuilder put-component-policy \
       --component-arn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:component/{{my-example-component}}/2019.12.03/1 \
       --policy '{
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "444455556666"
                   ]
               },
               "Action": [
                   "imagebuilder:GetComponent",
                   "imagebuilder:ListComponents"
               ],
               "Resource": [
                   "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:component/{{my-example-component}}/2019.12.03/1"
               ]
           }
       ]
   }'
   ```

------
#### [ PowerShell ]

   To identify the AWS principals to share the component with, run the [Write-EC2IBComponentPolicy](https://docs.aws.amazon.com/powershell/latest/reference/items/Write-EC2IBComponentPolicy.html) cmdlet:

   ```
   $policy = @'
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "444455556666"
                   ]
               },
               "Action": [
                   "imagebuilder:GetComponent",
                   "imagebuilder:ListComponents"
               ],
               "Resource": [
                   "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:component/{{my-example-component}}/2019.12.03/1"
               ]
           }
       ]
   }
   '@
   Write-EC2IBComponentPolicy -ComponentArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:component/{{my-example-component}}/2019.12.03/1 `
       -Policy $policy
   ```

------

**Image recipe**  
You can apply a resource policy to an image recipe to enable cross-account sharing. This policy gives other accounts permission to use your recipe to create images in their accounts. The account that you share with must have permission to access any resources that the recipe references. These can include the base image and the selected components.

------
#### [ AWS CLI ]

   To identify the AWS principals to share the image recipe with, run the [put-image-recipe-policy](https://docs.aws.amazon.com/cli/latest/reference//imagebuilder/put-image-recipe-policy.html) Image Builder command in the AWS CLI:

   ```
   aws imagebuilder put-image-recipe-policy \
       --image-recipe-arn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-recipe/{{my-example-image-recipe}}/2019.12.03 \
       --policy '{
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "444455556666"
                   ]
               },
               "Action": [
                   "imagebuilder:GetImageRecipe",
                   "imagebuilder:ListImageRecipes"
               ],
               "Resource": [
                   "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-recipe/{{my-example-image-recipe}}/2019.12.03"
               ]
           }
       ]
   }'
   ```

------
#### [ PowerShell ]

   To identify the AWS principals to share the image recipe with, run the [Write-EC2IBImageRecipePolicy](https://docs.aws.amazon.com/powershell/latest/reference/items/Write-EC2IBImageRecipePolicy.html) cmdlet:

   ```
   $policy = @'
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "444455556666"
                   ]
               },
               "Action": [
                   "imagebuilder:GetImageRecipe",
                   "imagebuilder:ListImageRecipes"
               ],
               "Resource": [
                   "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-recipe/{{my-example-image-recipe}}/2019.12.03"
               ]
           }
       ]
   }
   '@
   Write-EC2IBImageRecipePolicy -ImageRecipeArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-recipe/{{my-example-image-recipe}}/2019.12.03 `
       -Policy $policy
   ```

------

**Container recipe**  
You can apply a resource policy to a container recipe to enable cross-account sharing. This policy gives other accounts permission to use your recipe to create images in their accounts. The account that you share with must have permission to access any resources that the recipe references. These can include the base image and the selected components.

------
#### [ AWS CLI ]

   To identify the AWS principals to share the container recipe with, run the [put-container-recipe-policy](https://docs.aws.amazon.com/cli/latest/reference//imagebuilder/put-container-recipe-policy.html) Image Builder command in the AWS CLI:

   ```
   aws imagebuilder put-container-recipe-policy \
       --container-recipe-arn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:container-recipe/{{my-example-container-recipe}}/2021.12.03 \
       --policy '{
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "444455556666"
                   ]
               },
               "Action": [
                   "imagebuilder:GetContainerRecipe",
                   "imagebuilder:ListContainerRecipes"
               ],
               "Resource": [
                   "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:container-recipe/{{my-example-container-recipe}}/2021.12.03"
               ]
           }
       ]
   }'
   ```

------
#### [ PowerShell ]

   To identify the AWS principals to share the container recipe with, run the [Write-EC2IBContainerRecipePolicy](https://docs.aws.amazon.com/powershell/latest/reference/items/Write-EC2IBContainerRecipePolicy.html) cmdlet:

   ```
   $policy = @'
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "444455556666"
                   ]
               },
               "Action": [
                   "imagebuilder:GetContainerRecipe",
                   "imagebuilder:ListContainerRecipes"
               ],
               "Resource": [
                   "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:container-recipe/{{my-example-container-recipe}}/2021.12.03"
               ]
           }
       ]
   }
   '@
   Write-EC2IBContainerRecipePolicy -ContainerRecipeArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:container-recipe/{{my-example-container-recipe}}/2021.12.03 `
       -Policy $policy
   ```

------
**Note**  
To set the correct policies for sharing and unsharing a resource, the resource owner must have `imagebuilder:put*` permissions.

1. 

**Promote as a RAM resource share**

   To make the resource visible to all principals that you shared it with, run the [promote-resource-share-created-from-policy](https://docs.aws.amazon.com/cli/latest/reference/ram/promote-resource-share-created-from-policy.html) AWS RAM command in the AWS CLI.

   To promote the resource share with AWS Tools for PowerShell, run the [Convert-RAMPolicyBasedResourceShareToPromoted](https://docs.aws.amazon.com/powershell/latest/reference/items/Convert-RAMPolicyBasedResourceShareToPromoted.html) cmdlet from the `AWS.Tools.RAM` module.