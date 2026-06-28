# Render V-Ray standalone scenes on Deadline Cloud

The
[vray\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vray_render "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vray_render")
job bundle creates a V-Ray rendering job for Deadline Cloud.

To run this bundle, you need:

- A V-Ray conda package hosted on a conda channel. Use the
  [V-Ray
  conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vray "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vray") in the samples repository to build the package.
- A sample `.vrscene` file and its dependencies. The
  [Chaos
  ENVISION documentation samples](https://docs.chaos.com/display/ENVISION/Sample+Scenes "https://docs.chaos.com/display/ENVISION/Sample+Scenes") include `.vrscene`
  files in Sample Scene 01.
  Submit the bundle with the GUI submitter:

```
deadline bundle gui-submit vray_render
```

Or submit a Chaos ENVISION sample from the CLI:

```
SAMPLE_DIR=`path-to-sample`
deadline bundle submit vray_render \
    -p VraySceneFile="$SAMPLE_DIR"/Building.vrscene \
    -p InputAssetDir="$SAMPLE_DIR"/Building.data
```

For all customization options, see the Chaos
[V-Ray
Standalone Command Line Options](https://docs.chaos.com/display/VNS/V-Ray+Standalone+Command+Line+Options "https://docs.chaos.com/display/VNS/V-Ray+Standalone+Command+Line+Options") documentation.
