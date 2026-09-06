# Render POV-Ray 3.7 scenes on Deadline Cloud

The
[povray-3.7
job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/povray-3.7 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/povray-3.7") on the GitHub website renders POV-Ray (Persistence of
Vision Raytracer) scenes on Deadline Cloud with full parameter control over
resolution, quality (0-11), and antialiasing. POV-Ray is available from the
`conda-forge` channel, and this bundle overrides
`CondaChannels` to enable that channel.

The bundle includes a sample POV-Ray scene
(`sample/sample.pov`) that demonstrates 3D shapes and textures.
Submit the bundle to a queue that supports conda with a
`CondaChannels` parameter:

```
deadline bundle gui-submit povray-3.7/
```
