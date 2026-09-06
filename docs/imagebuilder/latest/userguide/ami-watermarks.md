

# Track AMI lineage with watermarks
<a name="ami-watermarks"></a>

AMI watermarks are simple text labels that track the history of your machine images. You add watermark names to your image recipe, and Image Builder attaches them to the output AMI during the build process.

When you copy or distribute an AMI to other Regions or accounts, the watermarks copy automatically. All copies of your AMI carry the same watermarks. This helps you trace the history of your images.

You cannot make watermarked AMIs public. If your recipe includes watermarks or your source AMI has watermarks, Image Builder rejects distribution configurations that set launch permissions to public.

Key characteristics of AMI watermarks:
+ **Purpose** – Track AMI lineage across copies and distributions.
+ **Scope** – Metadata only. Watermarks do not affect instance performance or runtime behavior.
+ **Visibility restriction** – Watermarked AMIs cannot be made public.

**Topics**
+ [Watermark constraints](#ami-watermarks-constraints)
+ [Prerequisites](#ami-watermarks-prereqs)
+ [Add watermarks to an image recipe](#ami-watermarks-add)
+ [View watermarks on an existing recipe](#ami-watermarks-view)
+ [Considerations](#ami-watermarks-considerations)

## Watermark constraints
<a name="ami-watermarks-constraints"></a>

The following constraints apply to AMI watermarks in Image Builder image recipes.


| Constraint | Value | 
| --- | --- | 
| Watermarks per recipe | 1 to 5 | 
| Name length | 3 to 128 characters | 
| Allowed characters | Letters, numbers, spaces, and the following special characters: `( ) [ ] . / - ' @ _` | 
| Edge characters | Names cannot begin or end with a space | 
| Case sensitivity | Watermark names are case-sensitive | 
| Duplicates | Duplicate names within the same recipe are not permitted | 
| Total per output AMI | Source AMI watermarks plus recipe watermarks cannot exceed 5 | 

## Prerequisites
<a name="ami-watermarks-prereqs"></a>

Before you use AMI watermarks, verify the following requirements.
+ AMI watermarks are supported only for image recipes, not container recipes.
+ Your Image Builder execution role must include the `ec2:AttachImageWatermark` permission on `arn:aws:ec2:*::image/*`. If you use the Image Builder service-linked role, this permission is included automatically.

## Add watermarks to an image recipe
<a name="ami-watermarks-add"></a>

You can add watermarks when you create an image recipe or a new version of an existing recipe. Choose one of the following tabs for instructions.

------
#### [ Console ]

**To add watermarks to an image recipe**

1. When you create or version an image recipe, in the recipe configuration section, expand **AMI watermarks**.

1. Enter a watermark name (3 to 128 characters). Choose **Add watermark** to add more names (up to 5 total).

1. Complete the remaining recipe creation steps, and then choose **Create recipe**.

------
#### [ AWS CLI ]

To add watermarks with the AWS CLI, include the `amiWatermarks` parameter in your JSON input file for the **create-image-recipe** command.

The following example shows a recipe JSON file with watermarks configured.

```
{
    "name": "{{MyWatermarkedRecipe}}",
    "description": "{{Recipe with AMI watermarks for lineage tracking.}}",
    "parentImage": "{{ami-1234567890abcdef1}}",
    "semanticVersion": "1.0.0",
    "components": [
        {
            "componentArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:component/{{my-component/1.0.0/1}}"
        }
    ],
    "amiWatermarks": [
        "{{ProductionV1}}",
        "{{team-alpha}}"
    ]
}
```

Run the following command to create the recipe.

```
aws imagebuilder create-image-recipe --cli-input-json file://{{create-watermarked-recipe.json}}
```

The following list describes the `amiWatermarks` parameter.
+ **amiWatermarks** (array of strings, optional) – A list of watermark names to attach to output AMIs built from this recipe. Specify 1 to 5 names. Each name must be 3 to 128 characters, and can include letters, numbers, spaces, and the following special characters: `( ) [ ] . / - ' @ _`

------
#### [ CloudFormation ]

You can specify AMI watermarks in an `AWS::ImageBuilder::ImageRecipe` resource by using the `AmiWatermarks` property.

The following example shows a minimal image recipe template with watermarks configured.

```
Resources:
  WatermarkedRecipe:
    Type: AWS::ImageBuilder::ImageRecipe
    Properties:
      Name: {{MyWatermarkedRecipe}}
      Version: {{1.0.0}}
      ParentImage: arn:aws:imagebuilder:{{us-west-2}}:aws:image/amazon-linux-2023-x86/x.x.x
      Components:
        - ComponentArn: arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:component/{{my-component/1.0.0/1}}
      AmiWatermarks:
        - {{ProductionV1}}
        - {{team-alpha}}
```

You can set the `AmiWatermarks` property only at creation time. Because image recipes are immutable, changing watermarks requires a new recipe version.

For more information about the `AmiWatermarks` property, see [AWS::ImageBuilder::ImageRecipe](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-imagerecipe.html) in the *AWS CloudFormation Template Reference*.

------

## View watermarks on an existing recipe
<a name="ami-watermarks-view"></a>

You can view the watermarks configured for a recipe by calling the **get-image-recipe** command in the AWS CLI.

```
aws imagebuilder get-image-recipe --image-recipe-arn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-recipe/{{my-watermarked-recipe}}/{{1.0.0}}
```

The response includes the `amiWatermarks` array if watermarks were configured for that recipe version.

## Considerations
<a name="ami-watermarks-considerations"></a>

Keep the following points in mind when you use AMI watermarks.
+ Watermarks from a source AMI plus watermarks defined in the recipe combine on the output AMI. The total cannot exceed 5. If the combined count exceeds 5, the build fails.
+ If you distribute a watermarked AMI to other Regions or accounts, the watermarks propagate automatically.
+ Image Builder validates that watermarked AMIs are not set to public at image creation time. If your recipe has watermarks (or the source AMI has watermarks) and the distribution configuration sets launch permissions to public, Image Builder returns an `InvalidParameterCombinationException` error.