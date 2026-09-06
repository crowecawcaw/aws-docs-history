# Render Redshift scenes on Deadline Cloud

The
[redshift-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/redshift-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/redshift-2025")
job bundle on the GitHub website renders Redshift scenes using the standalone
`redshiftCmdLine.exe` renderer that ships with Cinema 4D 2025.
The bundle is designed for Windows systems. Cinema 4D is used because it is
available in the `deadline-cloud` conda channel and includes the
Redshift CLI renderer.

The bundle installs Cinema 4D 2025 through the `cinema4d=2025`
conda package, configures Windows host requirements, and uses
`redshiftCmdLine.exe` directly for rendering. The executable is
located at
`%CONDA_PREFIX%\cinema4d\RedshiftData\bin\redshiftCmdLine.exe`,
which resolves automatically when the Cinema 4D conda package is
installed.

To run this bundle, you need:

- A Windows operating system
- A Redshift compatible GPU
- The `cinema4d=2025` conda package
- A valid Redshift scene file (`.rs`)
  You can create a `.rs` file in Cinema 4D with Redshift
  materials and lighting, then export the scene as a Redshift scene file.

Submit the bundle:

```
deadline bundle gui-submit redshift-2025
```

A Deadline Cloud Windows GPU service-managed fleet works with no further
configuration. Make sure that the queue has access to the
`cinema4d=2025` conda package and Redshift licensing.
