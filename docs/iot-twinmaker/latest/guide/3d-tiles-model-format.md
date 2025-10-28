# 3D Tiles model format

## Using 3D Tiles in your scene

If you experience long wait times when you load 3D scenes in AWS IoT TwinMaker or have poor rendering
performance when you navigate a complex 3D model, then you may want to convert your models to
3D tiles. This section describes the 3D tiles format and available third-party tools. Read on
to decide if 3D Tiles are right for your use case and for help getting started.

### Complex model use case

A 3D model in your AWS IoT TwinMaker scene may cause performance issues like slow loading times and
lagging navigation if the model is:

- **Large**: its file size is larger than 100MB.
- **Dense**: it is made up of hundreds or thousands
  of distinct meshes.
- **Complex**: mesh geometry has millions of triangles
  to form complex shapes.

### 3D Tiles format

[The 3D Tiles format](https://www.ogc.org/standard/3dtiles/ "https://www.ogc.org/standard/3dtiles/") is a solution
for streaming model geometry and improving 3D rendering performance. It enables instantaneous
loading of 3D models in an AWS IoT TwinMaker scene, and optimizes 3D interactions by loading in chunks
of a model based on what is visible in the camera view.

The 3D Tiles format was created by [Cesium](https://cesium.com/ "https://cesium.com/"). Cesium
has a managed service to convert 3D models to 3D Tiles called
[Cesium Ion](https://cesium.com/platform/cesium-ion/ "https://cesium.com/platform/cesium-ion/"). This is currently
the best solution for creating 3D Tiles, and we recommend this for your complex models in the
[supported formats](https://cesium.com/learn/3d-tiling/tiler-data-formats/#supported-data-formats "https://cesium.com/learn/3d-tiling/tiler-data-formats/#supported-data-formats"). You can register Cesium and choose the appropriate subscription plan
based on your business requirements on [Cesium's pricing page](https://cesium.com/platform/cesium-ion/pricing/ "https://cesium.com/platform/cesium-ion/pricing/").

To prepare a 3D Tiles model that you can add to an AWS IoT TwinMaker scene, follow the
instructions documented by Cesium Ion:

- [Import a model
  to Cesium Ion](https://cesium.com/learn/3d-tiling/tiler-data-formats/ "https://cesium.com/learn/3d-tiling/tiler-data-formats/")

### Upload Cesium 3D tiles to AWS

Once your model has been converted to 3D Tiles, download the model files then upload them to
your AWS IoT TwinMaker workspace Amazon S3 bucket:

1. [Create and download your 3D Tiles model archive](https://cesium.com/learn/ion/cesium-ion-archives-and-exports/#create-and-download-an-asset-archive "https://cesium.com/learn/ion/cesium-ion-archives-and-exports/#create-and-download-an-asset-archive").
2. Unzip the archive into a folder.
3. Upload the entire 3D Tiles folder into the Amazon S3 bucket associated with your AWS IoT TwinMaker
   workspace. (See [Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the Amazon S3 User Guide.)
4. If your 3D Tiles model was uploaded successfully, you will see an Amazon S3 folder path
   in your AWS IoT TwinMaker [Resource Library](scenes-using-resource-library.md "scenes-using-resource-library.md")
   with type `Tiles3D`.

###### Note

The AWS IoT TwinMaker Resource Library doesn't support directly uploading 3D Tiles models.

### Using 3D Tiles in AWS IoT TwinMaker

AWS IoT TwinMaker is aware of any 3D Tiles model uploaded to your workspace S3 bucket. The model
must have a `tileset.json` and all dependent files (.gltf, .b3dm, .i3dm, .cmpt,
.pnts) available in the same Amazon S3 directory. The Amazon S3 directory path will appear in the
Resource Library with the type `Tiles3D`.

To add the 3D Tiles model to your scene, follow these steps:

1. On the scene composer page, choose the plus (**+**) sign, and
   then choose **Add 3D model**.
2. On the **Add resource from resource library** window, choose
   the path to your 3D Tiles model with the type `Tiles3D`, and then choose
   **Add**.
3. Click on the canvas to place the model in your scene.

#### 3D Tiles differences

3D Tiles does not currently support geometric and semantic metadata, which means that
the mesh hierarchy of the original model is not available for the sub-model selection
feature. You can still add widgets to your 3D Tiles model, but you cannot use features
fine-tuned to sub-models: model shader, separated 3D transformations, or entity binding
for a sub-model mesh.

It is recommended to use the 3D Tiles conversion for large assets that serve as context
for the background of a scene. If you want a sub-model to be further broken down and
annotated then it should be extracted as a separate glTF/glb asset and added directly to
the scene. This can be done with free and common 3D tools like
[Blender](https://www.blender.org/ "https://www.blender.org/").

**Example use case:**

- You have a 1GB model of a factory with detailed machine rooms and floors,
  electrical boxes, and plumbing pipes. The electrical boxes and pipes need to glow
  red when associated property data cross a threshold.
- You isolate the box and pipe meshes in the model and export it into a
  separate glTF using Blender.
- You convert the factory without electrical and plumbing elements into a 3D
  Tiles model and upload it to S3.
- You add both the 3D Tiles model and glTF model to an AWS IoT TwinMaker scene at the
  origin (0,0,0).
- You add model shader components to the electrical box and pipe sub-models
  of the glTF to make the meshes red based on property rules.
