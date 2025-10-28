# Managing storage lifecycle

You can manage your file systems so that they have cost-effective storage throughout their
lifecycle. Use lifecycle management to automatically transition data between storage classes
according to the lifecycle configuration for the file system. The lifecycle configuration
comprises of three _lifecycle policies_ that you set for the file
system.

Lifecycle policies instruct lifecycle management when to transition files into and out
of the EFS Infrequent Access (IA) and EFS Archive storage classes.
Transition time is based on when the files were last accessed in the Standard
storage class. To determine last accessed time in the Standard storage class,
an internal timer tracks when a file was last accessed (not the POSIX file system attributes
that are publicly viewable). Whenever a file in Standard is accessed, the
lifecycle management timer is reset.

Lifecycle policies apply to the entire EFS file system.

The EFS lifecycle policies are:

- **Transition into IA** – Instructs lifecycle management when to move
  files in to the Infrequent Access (IA) storage class, which is cost-optimized
  for data that is accessed only a few times each quarter. By default, files that are not
  accessed in Standard storage fclass or 30 days are transitioned into
  IA.
- **Transition into Archive** – Instructs lifecycle management when to
  move files from the Standard or IA storage class in to the
  Archive storage class, which is cost-optimized for data that is accessed
  only a few times each year or less. By default, files that are not accessed in the
  Standard storage class for 90 days are transitioned in to the
  Archive storage class.
- **Transition into Standard** – Instructs lifecycle management whether to
  transition files out of the IA or Archive storage class and
  back in to the Standard storage class when the files are accessed in the
  IA or Archive storage class. By default, files are not moved
  back to the Standard storage class, and they remain in the IA
  or Archive storage class when they are accessed.

For performance-sensitive use cases that demand the fastest latency performance
(such as applications that work with a large volume of small files), choose to
transition files into Standard storage **On first
access**.
For more information about configuring the lifecycle policies for a file system, see [Configuring lifecycle policies](enable-lifecycle-management.md "enable-lifecycle-management.md").

## File system operations for lifecycle management

File system operations for lifecycle management have a lower priority than operations
for EFS file system workloads. The time required to transition files in to or out
of IA and Archive storage varies depending on the file size and
file system workload. For example, transitioning millions of small files may take longer
than transitioning fewer larger files of the same total storage size.

File metadata, including file names, ownership information, and file system directory
structure, is always stored in Standard to help ensure consistent metadata
performance.

Metadata operations for file systems in IA or Archive
storage, such as listing the contents of a directory, don't count as file access.
During the process of transitioning a file's content to the IA or
Archive storage classes, the file is stored in the Standard
storage class and is billed at that storage rate.

All write operations to files in the file system's IA or
Archive storage classes are first written to Standard storage
classes, and are then eligible to be transitioned to the applicable storage class after 24
hours.
