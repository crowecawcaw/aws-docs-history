# Build an Autodesk Maya conda package for Deadline Cloud

The samples repository on the GitHub website includes the following
Maya conda recipes. Each
recipe configures the `MAYA_MODULE_PATH` environment variable so
that Maya loads plugin `.mod` files placed in the standard
plugin paths:

[maya-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2025"),
[maya-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026"),
[maya-2027](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2027 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2027")

Recipes for Autodesk Maya 2025, 2026, and 2027.

[maya-mtoa-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2025"),
[maya-mtoa-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2026"),
[maya-mtoa-2027](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2027 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2027")

Maya to Arnold (MtoA) renderer plugin. The MtoA package also
provides the `kick` standalone renderer, which the
[Render Arnold .ass files on Deadline Cloud](examples-jb-arnold-render.md "examples-jb-arnold-render.md") bundle uses.

[maya-vray-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray-2025"),
[maya-vray-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray-2026"),
[maya-vray-7.2-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray-7.2-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray-7.2-2025"),
[maya-vray-7.2-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray-7.2-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray-7.2-2026")

V-Ray for Maya renderer plugin. The `maya-vray-7.2`
recipes package V-Ray 7.20.02 (Update 2 DR2) and require the V-Ray
for Maya archive from
[Chaos](https://www.chaos.com/vray/maya "https://www.chaos.com/vray/maya")
(account required).

[maya-redshift-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-redshift-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-redshift-2025"),
[maya-redshift-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-redshift-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-redshift-2026")

Redshift for Maya renderer plugin.

[maya-bifrost-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-bifrost-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-bifrost-2026")

Bifrost simulation framework for Maya 2026.

[maya-openjd](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-openjd "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-openjd")

Builds the Maya Open Job Description adaptor with rattler-build for Python
3.13.

To build the recipe, you need to provide the Maya source archive.
Download the Maya source archive from Autodesk and place it in the
`conda_recipes/archive_files` directory of your samples
repository clone. The exact filename varies by version — for example,
Maya 2025 uses `Autodesk_Maya_2025_Linux_64bit.tgz` while
Maya 2026 uses `Autodesk_Maya_2026_ML_Linux_64bit.tgz`. Refer
to each recipe's README for the expected filename.

The Maya Windows installer requires Administrator permissions that
aren't available in most conda package build environments. The
[maya-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2025")
recipe README includes step-by-step instructions for installing Maya on a
fresh EC2 Windows Server instance and creating a redistributable archive
that you can upload to your private Amazon S3 bucket and reuse for other Maya
recipes.

Submit the build:

```
./submit-package-job maya-2026
```

For details on the Maya packaging approach, see the
[maya-2026
recipe README](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026").
