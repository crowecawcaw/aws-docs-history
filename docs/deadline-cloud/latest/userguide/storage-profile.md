# Storage profiles in Deadline Cloud

When you use workstations and fleet worker hosts from multiple operating systems or with
different file system mounts, you can create storage profiles in your farm to indicate where
the same file systems are mounted on different systems. When Deadline Cloud runs a job on a different
storage profile than on the workstation it was submitted from, it will transform file system
paths that are in directories configured in the storage profiles.

Using storage profiles in your Deadline Cloud farm enables the following behaviors:

- When submitting a job to a queue, the files that the job references will be categorized by
  the workstation storage profile:
  - Files that are under a shared file system location will be left alone.
  - Files that are under a local file system location will be attached to the job by uploading
    them to the job attachments S3 bucket. Files that were previously uploaded are not uploaded again.
  - Files that are not under any file system location will be attached to the job as well. The job
    submitter will warn about these file paths unless they are under a known path in the local Deadline Cloud settings.

- When jobs are running on a fleet worker host with a different operating system or storage profile
  than the submitting workstation, file paths used by the job will be mapped from the submitting storage
  profile to the fleet storage profile.
- When downloading job output, jobs that were submitted for a different operating system or storage
  profile will have their paths mapped from the submitting storage profile to the local workstation storage profile.
  For more information, see [Storage
  profiles and path mapping](../developerguide/storage-profiles-and-path-mapping.md "../developerguide/storage-profiles-and-path-mapping.md") in the _AWS Deadline Cloud Developer Guide_.

###### To create a storage profile

1. Open the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. From **Get started**, choose **Go to Deadline Cloud dashboard**.
3. Choose a farm, and then choose the **Storage profiles** tab.
4. Choose **Create storage profile**.
5. From the dropdown, select an **Operating system**.
6. Enter a **Storage profile name**. The name is how you choose a storage profile
   for a workstation. For example, names like _Windows-Workstation_ or _Windows-OnPremFleet_
   can make it easy to identify it later.
7. Create a file system location of **Shared** type for each shared file system that is mounted on both workstations and fleet worker hosts.
   1. Enter a **name** that identifies the mount, such as _Projects_ for a shared file
      system that contains project data, or _Tools_ for a shared file system with tools to use.
   2. Enter the mount location for the chosen shared file system on the operating system of the storage profile.

8. Create a file system location of **Local** type for each shared file system that is only for workstations.
   For example when your fleets are on AWS and you want job attachments to handle the data transfer. You can also create this kind
   of file system location for directories that are local to each workstation, to specify equivalent paths on different operating
   systems even if they are not mounted storage.
   1. Enter a **name** that identifies the mount, such as _Projects_ for a shared file system
      that contains project data, or _Tools_ for a shared file system with tools to use.
   2. Enter the chosen file system location on the operating system of the storage profile.

9. (Optional) To add another file system location, choose **Add new required file system location** and enter the required data.
10. After you have added all of the required file system locations, choose **Create**.

###### To set up your storage profile for use

1. Navigate to the queue that you want to use this storage profile with, and select the **Allowed storage profiles** tab.
2. Choose **Configure storage profiles**.
3. From the dropdown list to associate storage profiles, select the storage profile you created.
4. In the Required file system location list, select the **file system location names** that you want to ensure are available on any storage profile for the associated fleets.
5. (Optional) If you created the storage profile for a fleet, navigate to the fleet and select the **Configurations** tab.
   1. From the Storage profiles section, choose **Configure storage profile**.
   2. Select the storage profile, and then choose **Save changes**.

###### To configure a storage profile on a workstation

On each workstation that will submit jobs to a queue, use the settings dialog to select its default storage profile.

1. To open the Deadline Cloud settings dialog, complete one of the following steps:
   1. Select the **Settings** button in a Deadline Cloud submitter.

   **OR** 2. Run the CLI command `deadline config gui`.

2. After you have configured the default farm and queue, select the default storage profile from the dropdown list.
