# Render KeyShot scenes on Deadline Cloud

The deadline-cloud-samples repository on the GitHub website includes the
[keyshot\_standalone](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/keyshot_standalone "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/keyshot_standalone")
job bundle, a Windows KeyShot job bundle that
renders a scene with each frame as a separate task. The bundle accepts the
following job parameters:

- `KeyShotFile`
- `Frames`
- `OutputName`
- `OutputDirectoryPath`
- `OutputFormat`
  Output file paths follow the pattern
  ``OutputDirectoryPath`/`OutputName`.`frame`.`extension``.
  All other render settings come from the scene file itself.

The bundle expects one of the following:

- An input directory that contains all file references required to
  render. The simplest way to create one is to save the entire scene as a
  KeyShot package (.ksp), which bundles external files and converts paths
  to relative. Open the .ksp and submit the unpacked directory as the
  input directory, with the modified scene as the input KeyShot file.
- All referenced files available through network storage or another
  method that isn't job attachments.
  To run this bundle, your queue needs KeyShot available through a queue
  environment. The
  [keyshot-2025
  conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025") on the GitHub website builds a KeyShot conda package
  you can publish to your queue's S3 conda channel.
