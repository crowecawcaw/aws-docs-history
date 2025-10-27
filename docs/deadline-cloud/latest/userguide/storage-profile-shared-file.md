# Storage profiles for shared file systems

You can configure your Deadline Cloud fleets to mount shared file systems by using [VPC resource endpoints on service-managed fleets](../developerguide/smf-vpc.md "../developerguide/smf-vpc.md"),
or by configuring the hosts of a customer-managed fleet on AWS or on-premises. When workstations have the same shared file systems
mounted as your fleets, you can create file system locations of the shared type in your storage profiles to configure where each shared
file system appears as a local path.

For example, suppose you have one shared file system for projects and another one for tools. Your workstations and fleets include
the three operating systems Windows, macOS, and Linux. You can create one storage profile for each operating system with the following values:

- **Storage profile name**: Linux-Host, **operating system family**: Linux.
  - **File system location name**: Projects, **path**: /mnt/projects, **type**: Shared.
  - **File system location name**: Tools, **path**: /mnt/projects, **type**: Shared.

- **Storage profile name**: Windows-Host, **operating system family**: Windows.
  - **File system location name**: Projects, **path**: X:\projects, **type**: Shared.
  - **File system location name**: Tools, **path**: Z:, **type**: Shared.

- **Storage profile name**: MacOS-Host, **operating system family**: MacOS.

      + **File system location name**: Projects, **path**: /Volumes/Projects, **type**: Shared.
      + **File system location name**: Tools, **path**: /Volumes/Tools, **type**: Shared.

  When you submit a job from Windows that uses a path X:\Projects\ProjectA\Textures\texture.jpg, Deadline Cloud will add a field containing the Windows-Host storage profile id to the job.

If the job runs on a Linux fleet worker host, Deadline Cloud will create two path mapping rules for the job based on corresponding file system location names: X:\Projects -> /mnt/projects, Z: -> /mnt/tools.
The job will apply these rules to resolve the original paths to where the Linux host sees them.

If job attachments are also configured for your queue, any paths that are not under a file system location of type shared will be attached to the job and uploaded to the job attachments S3 bucket.
This lets you attach data files to the job instead of requiring that they always be copied to a shared file system. For example, providing auxiliary files defined by the job bundle you submit.
