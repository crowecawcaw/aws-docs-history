# Render USD scenes with Houdini Husk on Deadline Cloud

The
[houdini\_husk\_usd\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/houdini_husk_usd_render "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/houdini_husk_usd_render")
job bundle on the GitHub website renders a USD scene using the Houdini [husk CLI](https://www.sidefx.com/docs/houdini/ref/utils/husk.html "https://www.sidefx.com/docs/houdini/ref/utils/husk.html")
on the SideFX website. By default, Husk renders with the Houdini Karma
renderer, but Husk
supports any Hydra-compatible USD render delegate. The bundle expands to a
task per frame using the Frames job parameter and limits execution to Linux
workers through host requirements.

To render with the `KarmaXPU` GPU engine, uncomment the
`amount.worker.gpu` host requirement in the job template so that
the job is scheduled on a worker with a GPU. The Karma renderer requires a
Karma license to run. Service-managed fleets provide usage-based Karma
licenses automatically.

This bundle also shows how to write a custom asset introspection tool
for job attachments. The included `generate_usd_job.py` script
inspects a USD file, finds all referenced asset files, and generates a job
bundle with job attachment references for those assets. To use the script,
install the `usd-core` and `deadline` Python libraries
and run:

```
python3 generate_usd_job.py `my_scene.usd`
```

The bundle also supports V-Ray and Redshift renderers through their
Hydra render delegates. To use these renderers, build a conda package with
the
[houdini-vray-7](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-vray-7 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-vray-7"),
[houdini-redshift-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2025"),
or
[houdini-redshift-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2026")
conda recipes on the GitHub website.

The bundle includes a `sample.usda` file with a cube and
sphere that has no external dependencies and can be rendered without
attaching any other files.
