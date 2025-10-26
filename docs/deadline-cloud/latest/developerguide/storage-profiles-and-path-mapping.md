# Storage profiles and path mapping

Use storage profiles to model the file systems on your workstation and worker hosts. Each
 storage profile describes the operating system and file system layout of one of your system
 configurations. This topic describes how to use storage profiles to model the file system
 configurations of your hosts so Deadline Cloud can generate path mapping rules for your jobs, and how
 those path mapping rules are generated from your storage profiles.

When you submit a job to Deadline Cloud you can provide an optional storage profile ID for the
 job. This storage profile describes the submitting workstation's file system. It describes the
 original file system configuration that the file paths in the job template use.

You can also associate a storage profile with a fleet. The storage profile describes the 
 file system configuration of all worker hosts in the fleet. If you have workers with different
 file system configuration, those workers must be assigned to a different fleet in your farm.

 Path mapping rules describe how paths should be remapped from how they are specified in
 the job to the path's actual location on a worker host. Deadline Cloud compares the file system
 configuration described in a job's storage profile with the storage profile of the fleet that
 is running the job to derive these path mapping rules. 

###### Topics

* [Model shared
 file system locations with storage profiles](modeling-your-shared-filesystem-locations-with-storage-profiles.md "modeling-your-shared-filesystem-locations-with-storage-profiles.md")
* [Configure storage profiles for
 fleets](configuring-storage-profiles-for-fleets.md "configuring-storage-profiles-for-fleets.md")
* [Configure storage profiles for queues](storage-profiles-for-queues.md "storage-profiles-for-queues.md")
* [Derive path mapping
 rules from storage profiles](deriving-path-mapping-rules-from-storage-profiles.md "deriving-path-mapping-rules-from-storage-profiles.md")
