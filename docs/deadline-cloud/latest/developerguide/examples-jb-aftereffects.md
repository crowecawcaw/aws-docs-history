# Render Adobe After Effects projects on Deadline Cloud

The
[afterfx\_render\_one\_task](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/afterfx_render_one_task "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/afterfx_render_one_task")
job bundle on the GitHub website uses `aerender` to render an After Effects frame
range as a single task. The entire workload runs on one worker as one
command. The bundle accepts the following job parameters:

- Project file
- Comp name
- Input directory
- Output directory
- Start frame
- End frame
  This bundle expects an input directory that contains all file references
  required to render. Place the project file inside the input directory to
  preserve relative paths.

To run this bundle, you need After Effects installed on Windows worker
hosts. You can use the
[After
Effects host configuration script](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/aftereffects "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/aftereffects") on the GitHub website to
install After Effects with Red Giant plugins on a Windows service-managed
fleet. The
[aftereffects-25.1
conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-25.1 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-25.1") on the GitHub website builds an After Effects conda
package as an alternative.
