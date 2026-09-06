# Build a V-Ray Standalone conda package for Deadline Cloud

The
[vray](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vray "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vray")
conda recipe on the GitHub website builds a V-Ray Standalone renderer conda package. For more information about V-Ray Standalone, see
[V-Ray
Standalone Home](https://docs.chaos.com/display/VNS/V-Ray+Standalone+Home "https://docs.chaos.com/display/VNS/V-Ray+Standalone+Home") on the Chaos website.

To build the recipe, download the V-Ray Standalone archive
(`vraystd_adv_71000_rhel8_clang-gcc-11.2` for x86 or
`vraystd_adv_71000_rhel8_arm64_clang-gcc-11.2` for ARM) from
the [Chaos download page](https://download.chaos.com/?platform=47&product=47 "https://download.chaos.com/?platform=47&product=47")
on the Chaos website.
A Chaos account is required. Place the file in the
`conda_recipes/archive_files` directory of your samples
repository clone.

Submit the build:

```
./submit-package-job vray
```

The queue's IAM role needs `s3:PutObject` permission for
the `Conda/*` prefix in the job attachments bucket to publish
the built package.

For a job bundle that uses this package, see
[Render V-Ray standalone scenes on Deadline Cloud](examples-jb-vray-render.md "examples-jb-vray-render.md").
