# Build a Blender conda package for Deadline Cloud

The samples repository includes conda recipes for the following Blender
versions and add-ons. Each recipe builds for Linux 64-bit and Windows
64-bit, and downloads source archives from the Blender Foundation:

- [blender-4.2](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2")
- [blender-4.3](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.3 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.3")
- [blender-4.4](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.4 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.4")
- [blender-4.5](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5")
- [blender-5.0](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-5.0 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-5.0")
- [blender-5.1](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-5.1 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-5.1")
- [blender-flipfluids](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-flipfluids "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-flipfluids"): FLIP Fluids physics simulation add-on for Blender.
- [blender-plugin-bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-plugin-bundle "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-plugin-bundle"): A bundle of Blender plugins packaged together.
  Submit a Blender 4.5 build job from the
  `conda_recipes` directory of the samples repository:

```
./submit-package-job blender-4.5
```

For details on the Blender packaging approach, see the
[blender-4.5
recipe README](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5"). To install Blender add-ons,
place the `.py` or `.zip` file in a known location
inside `$INSTALL_DIR` and modify the activate script to install
the add-on with Blender's Python.
