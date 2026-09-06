

# Render V-Ray standalone scenes on Deadline Cloud
<a name="examples-jb-vray-render"></a>

The [vray\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vray_render) job bundle on the GitHub website creates a V-Ray rendering job for Deadline Cloud.

To run this bundle, you need:
+ A V-Ray conda package hosted on a conda channel. For the recipe, see [V-Ray conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vray) on the GitHub website.
+ A sample `.vrscene` file and its dependencies. For sample scenes, see [Sample Scenes](https://docs.chaos.com/display/ENVISION/Sample+Scenes) on the Chaos website. Sample Scene 01 in the ENVISION documentation includes `.vrscene` files.

Submit the bundle with the GUI submitter:

```
deadline bundle gui-submit vray_render
```

Or submit a Chaos ENVISION sample from the CLI:

```
SAMPLE_DIR={{path-to-sample}}
deadline bundle submit vray_render \
    -p VraySceneFile="$SAMPLE_DIR"/Building.vrscene \
    -p InputAssetDir="$SAMPLE_DIR"/Building.data
```

For all customization options, see [V-Ray Standalone Command Line Options](https://docs.chaos.com/display/VNS/V-Ray+Standalone+Command+Line+Options) on the Chaos website.