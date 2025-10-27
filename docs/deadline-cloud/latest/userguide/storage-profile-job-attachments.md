# Storage profiles for job attachments

You can configure your Deadline Cloud queue to use job attachments for transferring asset data referenced by your jobs to and from AWS. When workstations mount the same shared file systems,
but your fleets do not, you can create file system locations of the local type in your storage profiles. This lets you configure where you will upload and download files from, and how to
map paths between operating systems.

For example, suppose you have one shared file system for projects and another one for tools. Your workstations and fleets include the three operating systems Windows, macOS, and Linux.
Everything is the same as in the **Storage profiles for shared file systems** topic except the file systems are not shared with the farm. They are for the local area
network containing your workstations. You can create one storage profile for each operating system with the following values:

- **Storage profile name**: Linux-Host, **operating system family**: Linux.
  - **File system location name**: Projects, **path**: /mnt/projects, **type**: Local.
  - **File system location name**: Tools, **path**: /mnt/projects, **type**: Local.

- **Storage profile name**: Windows-Host, **operating system family**: Windows.
  - **File system location name**: Projects, **path**: X:\projects, **type**: Local.
  - **File system location name**: Tools, **path**: Z:, **type**: Local.

- **Storage profile name**: MacOS-Host, **operating system family**: MacOS.

      + **File system location name**: Projects, **path**: /Volumes/Projects, **type**: Local.
      + **File system location name**: Tools, **path**: /Volumes/Tools, **type**: Local.

  When you submit a job from Windows that uses a path X:\Projects\ProjectA\Textures\texture.jpg, Deadline Cloud will add a field containing the Windows-Host storage profile id to the job and
  upload the file to the job attachments S3 bucket if it wasn't uploaded already.

If the job runs on a Linux fleet worker host, Deadline Cloud will make the texture file available in a local temporary directory, then create a path mapping rule from one of the directories
containing the texture to the temporary directory. For example X:\Projects\ProjectA -> /sessions/session-123/projects, so that X:\Projects\ProjectA\Textures\texture.jpg maps to
/sessions/session-123/projects/Textures/texture.jpg. When a task of the job is complete, it collects the output from directories specified by the job. Suppose
/sessions/session-123/projects/Output/frame0032.png is an output file. This output is recorded on the job as X:\Projects\ProjectA\Output\frame0032.jpg, matching on the storage profile
for the workstation submitting the job.

When you download the job output on a macOS workstation, Deadline Cloud will create path mapping rules from the Windows workstation: X:\Projects -> /Volumes/Projects, Z: -> /Volumes/Tools.
It applies the rule to all output paths, downloading the example output file to /Volumes/Projects/ProjectA/Output/frame0032.jpg.

If an output file path of a job is not contained under any of the storage profile file system locations, Deadline Cloud will not be able to determine its path for download when the storage profile
is different from the submitting workstation. Depending on the command you use for download, that file will either be skipped or you will have to manually select a download directory.
