# Labeling category configuration file with

label category and frame attributes reference

When you create a 3D point cloud or video frame labeling job using the Amazon SageMaker API
operation `CreateLabelingJob`, you use a label category configuration file to
specify your labels and worker instructions. Optionally, you can also provide the following
in your label category attribute file:

- You can provide _label category attributes_ for
  video frame and 3D point cloud object tracking and object detection task types.
  Workers can use one or more attributes to give more information about an object. For
  example, you may want to use the attribute _occluded_ to have workers identify when an object is partially
  obstructed. You can either specify a label category attribute for a single label
  using the `categoryAttributes` parameter, or for all labels using the
  `categoryGlobalAttributes` parameter.
- You can provide _frame attributes_ for video
  frame and 3D point cloud object tracking and object detection task types using
  `frameAttributes`. When you create a frame attribute, it appears on
  each frame or point cloud in the worker task. In video frame labeling jobs, these
  are attributes that workers assign to an entire video frame. For 3D point cloud
  labeling jobs, these attributes are applied to a single point cloud. Use frame
  attributes to have workers provide more information about the scene in a specific
  frame or point cloud.
- For video frame labeling jobs, you use the label category configuration file to
  specify the task type (bounding box, polyline, polygon, or keypoint) sent to
  workers.
  For workers, specifying values for label category attributes and frame attributes will be
  optional.

###### Important

You should only provide a label attribute name in `auditLabelAttributeName`
if you are running an audit job to verify or adjust labels. Use this parameter to input
the [LabelAttributeName](../APIReference/API_CreateLabelingJob.md#sagemaker-CreateLabelingJob-request-LabelAttributeName "../APIReference/API_CreateLabelingJob.md#sagemaker-CreateLabelingJob-request-LabelAttributeName") used in the labeling job that generated the annotations
you want your worker to adjust. When you create a labeling job in the console, if you
did not specify a label attribute name, the **Name** of your job is
used as the LabelAttributeName.

The following topics show examples of a label category configuration file for different
kinds of labeling jobs. They also explain the schema and quotas of a category configuration
file.

###### Topics

- [Examples: label category
  configuration files for 3D point cloud labeling jobs](#sms-label-cat-config-attributes-3d-pc "#sms-label-cat-config-attributes-3d-pc")
- [Examples: label category
  configuration files for video frame labeling jobs](#sms-label-cat-config-attributes-vid-frame "#sms-label-cat-config-attributes-vid-frame")
- [Label category configuration file schema](#sms-label-cat-config-attributes-schema "#sms-label-cat-config-attributes-schema")
- [Label and label category attribute
  quotas](#sms-point-cloud-label-cat-limits "#sms-point-cloud-label-cat-limits")

## Examples: label category

configuration files for 3D point cloud labeling jobs

The following topics show examples of 3D point cloud label category configuration
files for object detection, object tracking, semantic segmentation, adjustment, and
verification labeling jobs.

###### Topics

- [Example: 3D point cloud object
  tracking and object detection](#example-3d-point-cloud-object "#example-3d-point-cloud-object")
- [Example: 3D point cloud semantic segmentation](#example-3d-point-cloud-semantic "#example-3d-point-cloud-semantic")
- [Example: 3D point cloud adjustment](#example-3d-point-cloud-adjustment "#example-3d-point-cloud-adjustment")
- [Example: 3D point cloud
  verification](#example-3d-point-cloud-verification "#example-3d-point-cloud-verification")

### Example: 3D point cloud object

tracking and object detection

The following is an example of a label category configuration file that
includes label category attributes for a 3D point cloud object detection or
object tracking labeling job. This example includes a two frame attributes,
which will be added to all point clouds submitted to the labeling job. The
`Car` label will include four label category
attributes—`X`, `Y`, `Z`, and the
global attribute, `W`.

```
{
    "documentVersion": "2020-03-01",
    "frameAttributes": [
        {
            "name":"`count players`",
            "description":"`How many players to you see in the scene?`",
            "type":"`number`"
        },
        {
            "name":"`select one`",
            "description":"`describe the scene`",
            "type":"`string`",
            "enum":["`clear`","`blurry`"],
            "isRequired":`true`
        },
    ],
    "categoryGlobalAttributes": [
        {
            "name":"`W`",
            "description":"`label-attributes-for-all-labels`",
            "type":"`string`",
            "enum": ["`foo`", "`buzz`", "`biz`"]
        }
    ],
    "labels": [
        {
            "label": "`Car`",
            "categoryAttributes": [
                {
                    "name":"`X`",
                    "description":"`enter a number`",
                    "type":"`number`",
                },
                {
                    "name":"`Y`",
                    "description":"`select an option`",
                    "type":"`string`",
                    "enum":["`y1`", "`y2`"]
                },
                {
                    "name":"`Z`",
                    "description":"`submit a free-form response`",
                    "type":"`string`",
                }
            ]
        },
        {
            "label": "Pedestrian",
            "categoryAttributes": [`...`]
        }
    ],
    "instructions": {"shortInstruction":"`Draw a tight Cuboid`", "fullInstruction":"`<html markup>`"}
}
```

### Example: 3D point cloud semantic segmentation

The following is an example of a label category configuration file for a
3D point cloud semantic segmentation labeling job.

Label category attributes are not supported for 3D point cloud semantic
segmentation task types. Frame attributes are supported. If you provide
label category attributes for a semantic segmentation labeling job, they
will be ignored.

```
{
    "documentVersion": "2020-03-01",
    "frameAttributes": [
        {
            "name":"`count players`",
            "description":"`How many players to you see in the scene?`",
            "type":"`number`"
        },
        {
            "name":"`select one`",
            "description":"`describe the scene`",
            "type":"`string`",
            "enum":["`clear`","`blurry`"]
        },
    ],
    "labels": [
        {
            "label": "Car",
        },
        {
            "label": "Pedestrian",
        },
        {
            "label": "Cyclist",
        }
    ],
    "instructions": {"shortInstruction":"Select the appropriate label and paint all objects in the point cloud that it applies to the same color", "fullInstruction":"<html markup>"}
}
```

### Example: 3D point cloud adjustment

The following is an example of a label category configuration file for a
3D point cloud object detection or object tracking adjustment labeling job.
For 3D point cloud semantic segmentation adjustment labeling jobs,
`categoryGlobalAttributes` and `categoryAttributes`
are not supported.

You must include `auditLabelAttributeName` to specify the label
attribute name of the previous labeling job that you use to create the
adjustment labeling job. Optionally, you can use the
`editsAllowed` parameter to specify whether or not a label or
frame attribute can be edited.

```
{
    "documentVersion": "2020-03-01",
    "frameAttributes": [
        {
            "name":"`count players`",
            "description":"`How many players to you see in the scene?`",
            "type":"`number`"
        },
        {
            "name":"`select one`",
            "editsAllowed":"`none`",
            "description":"`describe the scene`",
            "type":"`string`",
            "enum":["`clear`","`blurry`"]
        },
    ],
    "categoryGlobalAttributes": [
        {
            "name":"`W`",
            "editsAllowed":"`any`",
            "description":"`label-attributes-for-all-labels`",
            "type":"`string`",
            "enum": ["`foo`", "`buzz`", "`biz`"]
        }
    ],
    "labels": [
        {
            "label": "`Car`",
            "editsAllowed":"`any`",
            "categoryAttributes": [
                {
                    "name":"`X`",
                    "description":"`enter a number`",
                    "type":"`number`"
                },
                {
                    "name":"`Y`",
                    "description":"`select an option`",
                    "type":"`string`",
                    "enum":["`y1`", "`y2`"],
                    "editsAllowed":"`any`"
                },
                {
                    "name":"`Z`",
                    "description":"`submit a free-form response`",
                    "type":"`string`",
                    "editsAllowed":"`none`"
                }
            ]
        },
        {
            "label": "Pedestrian",
            "categoryAttributes": [`...`]
        }
    ],
    "instructions": {"shortInstruction":"`Draw a tight Cuboid`", "fullInstruction":"`<html markup>`"},
    // include auditLabelAttributeName for label adjustment jobs
    "auditLabelAttributeName": "`myPrevJobLabelAttributeName`"
}
```

### Example: 3D point cloud

verification

The following is an example of a label category configuration file you may
use for a 3D point cloud object detection or object tracking verification
labeling job. For a 3D point cloud semantic segmentation verification
labeling job, `categoryGlobalAttributes` and
`categoryAttributes` are not supported.

You must include `auditLabelAttributeName` to specify the label
attribute name of the previous labeling job that you use to create the
verification labeling job. Additionally, you must use the
`editsAllowed` parameter to specify that no labels can be edited.

```
{
    "documentVersion": "2020-03-01",
    "frameAttributes": [
        {
            "name":"`count players`",
            "editsAllowed":"`any`",
            "description":"`How many players to you see in the scene?`",
            "type":"`number`"
        },
        {
            "name":"`select one`",
            "editsAllowed":"`any`",
            "description":"`describe the scene`",
            "type":"`string`",
            "enum":["`clear`","`blurry`"]
        },
    ],
    "categoryGlobalAttributes": [
        {
            "name":"`W`",
            "editsAllowed":"`none`",
            "description":"`label-attributes-for-all-labels`",
            "type":"`string`",
            "enum": ["`foo`", "`buzz`", "`biz`"]
        }
    ],
    "labels": [
        {
            "label": "`Car`",
            "editsAllowed":"`none`",
            "categoryAttributes": [
                {
                    "name":"`X`",
                    "description":"`enter a number`",
                    "type":"`number`",
                    "editsAllowed":"`none`"
                },
                {
                    "name":"`Y`",
                    "description":"`select an option`",
                    "type":"`string`",
                    "enum":["`y1`", "`y2`"],
                    "editsAllowed":"`any`"
                },
                {
                    "name":"`Z`",
                    "description":"`submit a free-form response`",
                    "type":"`string`",
                    "editsAllowed":"`none`"
                }
            ]
        },
        {
            "label": "Pedestrian",
            "editsAllowed":"`none`",
            "categoryAttributes": [`...`]
        }
    ],
    "instructions": {"shortInstruction":"`Draw a tight Cuboid`", "fullInstruction":"`<html markup>`"},
    // include auditLabelAttributeName for label verification jobs
    "auditLabelAttributeName": "`myPrevJobLabelAttributeName`"
}
```

## Examples: label category

configuration files for video frame labeling jobs

The annotation tools available to your worker and task type used depends on the value
you specify for `annotationType`. For example, if you want workers to use key
points to track changes in the pose of specific objects across multiple frames, you
would specify `Keypoint` for the `annotationType`. If you do not
specify an annotation type, `BoundingBox` will be used by default.

The following topics show examples of video frame category configuration files.

###### Topics

- [Example: video frame keypoint](#example-video-frame-keypoint "#example-video-frame-keypoint")
- [Example: video frame adjustment](#example-video-frame-adjustment "#example-video-frame-adjustment")
- [Example: video frame verification](#example-video-frame-verification "#example-video-frame-verification")

### Example: video frame keypoint

The following is an example of a video frame keypoint label category configuration
file with label category attributes. This example includes two frame attributes, which
will be added to all frames submitted to the labeling job. The `Car` label
will include four label category attributes—`X`, `Y`,
`Z`, and the global attribute, `W`.

```
{
    "documentVersion": "2020-03-01",
    "frameAttributes": [
        {
            "name":"`count players`",
            "description":"`How many players to you see in the scene?`",
            "type":"`number`"
        },
        {
            "name":"`select one`",
            "description":"`describe the scene`",
            "type":"`string`",
            "enum":["`clear`","`blurry`"]
        },
    ],
    "categoryGlobalAttributes": [
        {
            "name":"`W`",
            "description":"`label-attributes-for-all-labels`",
            "type":"`string`",
            "enum": ["`foo`", "`buz`", "`buz2`"]
        }
    ],
    "labels": [
        {
            "label": "`Car`",
            "categoryAttributes": [
                {
                    "name":"`X`",
                    "description":"`enter a number`",
                    "type":"`number`",
                },
                {
                    "name":"`Y`",
                    "description":"`select an option`",
                    "type":"`string`",
                    "enum": ["`y1`", "`y2`"]
                },
                {
                    "name":"`Z`",
                    "description":"`submit a free-form response`",
                    "type":"`string`",
                }
            ]
        },
        {
            "label": "Pedestrian",
            "categoryAttributes": [`...`]
        }
    ],
    "annotationType":"`Keypoint`",
    "instructions": {"shortInstruction":"`add example short instructions here`", "fullInstruction":"`<html markup>`"}
}
```

### Example: video frame adjustment

The following is an example of a label category configuration file you may
use for a video frame adjustment labeling job.

You must include `auditLabelAttributeName` to specify the label
attribute name of the previous labeling job that you use to create the
verification labeling job. Optionally, you can use the
`editsAllowed` parameter to specify whether or not labels, label
category attributes, or frame attributes can be edited.

```
{
    "documentVersion": "2020-03-01",
    "frameAttributes": [
        {
            "name":"`count players`",
            "editsAllowed":"`none`",
            "description":"`How many players to you see in the scene?`",
            "type":"`number`"
        },
        {
            "name":"`select one`",
            "description":"`describe the scene`",
            "type":"`string`",
            "enum":["`clear`","`blurry`"]
        },
    ],
    "categoryGlobalAttributes": [
        {
            "name":"`W`",
            "editsAllowed":"`any`",
            "description":"`label-attributes-for-all-labels`",
            "type":"`string`",
            "enum": ["`foo`", "`buz`", "`buz2`"]
        }
    ],
    "labels": [
        {
            "label": "`Car`",
            "editsAllowed":"`any`",
            "categoryAttributes": [
                {
                    "name":"`X`",
                    "description":"`enter a number`",
                    "type":"`number`",
                    "editsAllowed":"`any`"
                },
                {
                    "name":"`Y`",
                    "description":"`select an option`",
                    "type":"`string`",
                    "enum": ["`y1`", "`y2`"],
                    "editsAllowed":"`any`"
                },
                {
                    "name":"`Z`",
                    "description":"`submit a free-form response`",
                    "type":"`string`",
                    "editsAllowed":"`none`"
                }
            ]
        },
        {
            "label": "Pedestrian",
            "editsAllowed":"`none`",
            "categoryAttributes": [`...`]
        }
    ],
    "annotationType":"`Keypoint`",
    "instructions": {"shortInstruction":"`add example short instructions here`", "fullInstruction":"`<html markup>`"},
    // include auditLabelAttributeName for label adjustment jobs
    "auditLabelAttributeName": "`myPrevJobLabelAttributeName`"
}
```

### Example: video frame verification

The following is an example of a label category configuration file for a
video frame labeling job.

You must include `auditLabelAttributeName` to specify the label
attribute name of the previous labeling job that you use to create the
verification labeling job. Additionally, you must use the
`editsAllowed` parameter to specify that no labels can be edited.

```
{
    "documentVersion": "2020-03-01",
    "frameAttributes": [
        {
            "name":"`count players`",
            "editsAllowed":"`none`",
            "description":"`How many players to you see in the scene?`",
            "type":"`number`"
        },
        {
            "name":"`select one`",
            "editsAllowed":"`any`",
            "description":"`describe the scene`",
            "type":"`string`",
            "enum":["`clear`","`blurry`"]
        },
    ],
    "categoryGlobalAttributes": [
        {
            "name":"`W`",
            "editsAllowed":"`none`",
            "description":"`label-attributes-for-all-labels`",
            "type":"`string`",
            "enum": ["`foo`", "`buz`", "`buz2`"]
        }
    ],
    "labels": [
        {
            "label": "`Car`",
            "editsAllowed":"`none`",
            "categoryAttributes": [
                {
                    "name":"`X`",
                    "description":"`enter a number`",
                    "type":"`number`",
                    "editsAllowed":"`any`"
                },
                {
                    "name":"`Y`",
                    "description":"`select an option`",
                    "type":"`string`",
                    "enum": ["`y1`", "`y2`"],
                    "editsAllowed":"`any`"
                },
                {
                    "name":"`Z`",
                    "description":"`submit a free-form response`",
                    "type":"`string`",
                    "editsAllowed":"`none`"
                }
            ]
        },
        {
            "label": "Pedestrian",
            "editsAllowed":"`none`",
            "categoryAttributes": [`...`]
        }
    ],
    "annotationType":"`Keypoint`",
    "instructions": {"shortInstruction":"`add example short instructions here`", "fullInstruction":"`<html markup>`"},
    // include auditLabelAttributeName for label adjustment jobs
    "auditLabelAttributeName": "`myPrevJobLabelAttributeName`"
}
```

## Label category configuration file schema

The following table lists elements you can and must include in your label category
configuration file.

###### Note

The parameter `annotationType` is only supported for video frame
labeling jobs.

| Parameter                                                                                                            | Required                                                                      | Accepted Values                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ---- |
| `frameAttributes`                                                                                                    | No                                                                            | A list of JSON objects. **Required Parameters in each JSON Object:** `name`, `type`, `description` `minimum` and `maximum` are required if `type` is `"number"` **Optional Parameters in each JSON Object:** `enum`, `editsAllowed`, `isRequired` | Use this parameter to create a frame attribute that is applied to all frames or 3D point clouds in your labeling job.See the third table in this section for more information.                                                                                                                                                                                                                                                                                                                                                                                                 |
| `categoryGlobalAttributes`                                                                                           | No                                                                            | A list of JSON objects. **Required Parameters in each JSON Object:** `name`, `type` `minimum` and `maximum` are required if `type` is `"number"` **Optional Parameters in each JSON Object:** `description`, `enum`, `editsAllowed`, `isRequired` | Use this parameter to create label category attributes that are applied to all labels you specify in `labels`. See the third table in this section for more information.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `labels`                                                                                                             | Yes                                                                           | A list of up to 30 JSON objects **Required Parameters in each JSON Object:** `label` **Optional Parameters in each JSON Object:** `categoryAttributes`, `editsAllowed`                                                                            | Use this parameter to specify your labels, or classes. Add one `label` for each class. To add a label category attribute to a label, add `categoryAttributes` to that label. Use `editsAllowed` to specify whether or not a label can be edited in an adjustment labeling job. Set `editsAllowed` to `"none"` for verification labeling jobs. See the following table for more information.                                                                                                                                                                                    |
| `annotationType` (only supported for video frame labeling jobs)                                                      | No                                                                            | String **Accepted Parameters:** `BoundingBox`, `Polyline`, `Polygon`, `Keypoint` **Default:** `BoundingBox`                                                                                                                                       | Use this to specify the task type for your video frame labeling jobs. For example, for a polygon video frame object detection task, choose `Polygon`. If you do not specify an `annotationType` when you create a video frame labeling job, Ground Truth will use `BoundingBox` by default.                                                                                                                                                                                                                                                                                    |
| `instructions`                                                                                                       | No                                                                            | A JSON object**Required Parameters in each JSON Object:**`"shortInstruction"`, `"fullInstruction"`                                                                                                                                                | Use this parameter to add worker instructions to help your workers complete their tasks. For more information about worker instructions, see [Worker instructions](sms-point-cloud-general-information.md#sms-point-cloud-worker-instructions-general "sms-point-cloud-general-information.md#sms-point-cloud-worker-instructions-general"). Short instructions must be under 255 characters and long instruction must be under 2,048 characters. For more information, see [Create instruction pages](sms-creating-instruction-pages.md "sms-creating-instruction-pages.md"). |
| `auditLabelAttributeName`                                                                                            | Required for adjustment and verification task types                           | String                                                                                                                                                                                                                                            | Enter the [LabelAttributeName](../APIReference/API_CreateLabelingJob.md#sagemaker-CreateLabelingJob-request-LabelAttributeName "../APIReference/API_CreateLabelingJob.md#sagemaker-CreateLabelingJob-request-LabelAttributeName") used in the labeling job you want to adjust annotations of. Only use this parameter if you are creating an adjustment job for video frame and 3D point cloud object detection, object tracking, or 3D point cloud semantic segmentation.                                                                                                     | ### Labels object schema The following table describes the parameters that you can and must use to create a list of `Labels`. Each parameter should be included in a JSON object.                                                                                                                                                                                                                                                                                       |
| Parameter                                                                                                            | Required                                                                      | Accepted Values                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                  | ---                                                                           | ---                                                                                                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `label`                                                                                                              | Yes                                                                           | String                                                                                                                                                                                                                                            | The name of the label category that is displayed to workers. Each label category name must be unique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `categoryAttributes`                                                                                                 | No                                                                            | A list of JSON objects. **Required Parameters in each JSON Object:** `name`, `type` `minimum` and `maximum` required if `type` is `"number"` **Optional Parameters in each JSON Object:** `description`, `enum`, `editsAllowed`, `isRequired`     | Use this parameter to add label category attributes to specific labels you specify in `labels`. To add one or more label category attributes to a label, include the `categoryAttributes` JSON object in the same `labels` JSON object as that `label`.See the following table for more information.                                                                                                                                                                                                                                                                           |
| `editsAllowed`                                                                                                       | No                                                                            | String **Supported Values**: `"none"`: no modifications are not allowed. or `"any"` (Default): all modifications are allowed.                                                                                                                     | Specifies whether or not a label can be edited by workers. For video frame or 3D point cloud _adjustment_ labeling jobs, add this parameter to one or more JSON objects in the `labels` list to specify whether or not a worker can edit a label. For 3D point cloud and video frame _verification_ labeling jobs, add this parameter with the value `"none"` to each JSON object in the `labels` list. This will make all labels uneditable.                                                                                                                                  | ### frameAttributes and categoryGlobalAttributes schema The following table describes the parameters that you can and must use to create a frame attributes using `frameAttributes` and label category attribute using the `categoryGlobalAttributes` and `categoryAttributes` parameters.                                                                                                                                                                              |
| Parameter                                                                                                            | Required                                                                      | Accepted Values                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                  | ---                                                                           | ---                                                                                                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `name`                                                                                                               | Yes                                                                           | String                                                                                                                                                                                                                                            | Use this parameter to assign a name to your label category or frame attribute. This is the attribute name that workers see. Each label category attribute name in your label category configuration file must be unique. Global label category attributes and label specific label category attributes cannot have the same name.                                                                                                                                                                                                                                              |
| `type`                                                                                                               | Yes                                                                           | String **Required Values**: `"string"` or `"number"`                                                                                                                                                                                              | Use this parameter to define the label category or frame attribute type. If you specify `"string"` for `type` and provide an `enum` value for this attribute, workers will be able to choose from one of the choices you provide. If you specify `"string"` for `type` and do not provide an `enum` value, workers can enter free form text. If you specify `number` for `type`, worker can enter a number between the `minimum` and `maximum` numbers you specify.                                                                                                            |
| `enum`                                                                                                               | No                                                                            | List of strings                                                                                                                                                                                                                                   | Use this parameter to define options that workers can choose from for this label category or frame attribute. Workers can choose one value specified in `enum`. For example, if you specify `["foo", "buzz", "bar"`] for `enum`, workers can choose one of `foo`, `buzz`, or `bar`. You must specify `"string"` for `type` to use an `enum` list.                                                                                                                                                                                                                              |
| `description`                                                                                                        | `frameAttributes`: Yes `categoryAttributes` or `categoryGlobalAttributes`: No | String                                                                                                                                                                                                                                            | Use this parameter to add a description of the label category or frame attribute. You can use this field to give workers more information about the attribute. This field is only required for frame attributes.                                                                                                                                                                                                                                                                                                                                                               |
| `minimum` and `maximum`                                                                                              | Required if attribute `type` is `"number"`                                    | Integers                                                                                                                                                                                                                                          | Use these parameters to specify minimum and maximum (inclusive) values workers can enter for numeric label category or frame attributes. You must specify `"number"` for `type` to use `minimum` and `maximum`.                                                                                                                                                                                                                                                                                                                                                                |
| `editsAllowed`                                                                                                       | No                                                                            | String **Required Values**: `"none"`: no modifications are not allowed. or `"any"` (Default): all modifications are allowed.                                                                                                                      | Specifies whether or not a label category or frame attribute can be edited by workers. For video frame or 3D point cloud _adjustment_ and _verification_ labeling jobs, add this parameter to label category and frame attribute JSON objects to specify whether or not a worker can edit an attribute.                                                                                                                                                                                                                                                                        |
| `isRequired`                                                                                                         | No                                                                            | Boolean                                                                                                                                                                                                                                           | Specifies whether workers are required to annotate an attribute. Workers cannot submit the job until all required attributes are annotated.                                                                                                                                                                                                                                                                                                                                                                                                                                    | ## Label and label category attribute quotas You can specify up to 10 label category attributes per class. This 10-attribute quotas includes global label category attributes. For example, if you create four global label category attributes, and then assign three label category attributes to label `X`, that label will have 4+3=7 label category attributes in total. For all label category and label category attribute limits, refer to the following table. |
| Type                                                                                                                 | Min                                                                           | Max                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | --- | ---  |
| Labels (`Labels`)                                                                                                    | 1                                                                             | 30                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Label name character quota                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1   | 16   |
| Label category attributes per label (sum of `categoryAttributes` and `categoryGlobalAttributes`)                     | 0                                                                             | 10                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Free form text entry label category attributes per label (sum of `categoryAttributes` and `categoryGlobalAttributes`).                                                                                                                                                                                                                                                                                                                                                  | 0   | 5    |
| Frame attributes                                                                                                     | 0                                                                             | 10                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Free form text entry attributes in `frameAttributes`.                                                                                                                                                                                                                                                                                                                                                                                                                   | 0   | 5    |
| Attribute name character quota (`name`)                                                                              | 1                                                                             | 16                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Attribute description character quota (`description`)                                                                                                                                                                                                                                                                                                                                                                                                                   | 0   | 128  |
| Attribute type characters quota (`type`)                                                                             | 1                                                                             | 16                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Allowed values in the `enum` list for a `string` attribute                                                                                                                                                                                                                                                                                                                                                                                                              | 1   | 10   |
| Character quota for a value in `enum` list                                                                           | 1                                                                             | 16                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Maximum characters in free form text response for free form text `frameAttributes`                                                                                                                                                                                                                                                                                                                                                                                      | 0   | 1000 |
| Maximum characters in free form text response for free form text `categoryAttributes` and `categoryGlobalAttributes` | 0                                                                             | 80                                                                                                                                                                                                                                                |
