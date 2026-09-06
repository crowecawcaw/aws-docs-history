

# Run storage types in HealthOmics workflows
<a name="workflows-run-types"></a>

When you start a run, HealthOmics allocates temporary run storage for the workflow engine to use during the run. HealthOmics provides the temporary run storage as a file system. 

For a given workflow or workflow run, you can choose dynamic or static run storage. By default, HealthOmics provides DYNAMIC run storage. 

**Note**  
Run storage usage incurs charges to your account. For pricing information about static and dynamic run storage, see *[ HealthOmics pricing](https://aws.amazon.com/healthomics/pricing/).*

The following sections provide information to consider when deciding which run storage type to use.

## Dynamic run storage
<a name="workflows-run-type-dynamic"></a>

We recommend using dynamic run storage for most runs, including runs that require faster start times, runs where you don’t know the storage needs in advance, and for iterative development testing cycles.

You don’t need to estimate the required storage or throughput for the run. HealthOmics dynamically scales the storage size up or down, based on file system utilization during the run. HealthOmics also dynamically scales throughput based on the workflow's needs. A run never fails due to an **Out of storage for file system** error.

Dynamic run storage provides faster provisioning/deprovisioning time than static run storage. Faster setup is an advantage for most workflows and is also an advantage during development/test cycles.

After the run completes (success path or fail path), the getRun API operation returns the maximum storage used by the run in the storageCapacity field. You can also find this information in the run manifest logs located in the **omics** log group. For a dynamic storage run that completes within 2 hours, the maximum storage value may not be available.

For dynamic run storage, the run provisions a filesystem that uses NFS protocol. NFS treats CREATE, DELETE, and RENAME file operations as non-idempotent, which may occasionally lead to race conditions for these operations that your code needs to handle gracefully. For example, your code should not fail if it tries to delete a file that does not exist. Before adopting dynamic run storage, we recommend adjusting your workflow code to make it resilient to non-idempotent file operations. See [Code examples for safe handling of non-idempotent operations](#idempotent-code-examples).

## Code examples for safe handling of non-idempotent operations
<a name="idempotent-code-examples"></a>

The following python example shows how to delete a file without failing if the file does not exist.

```
import os
import errno

def remove_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        # If the error is "No such file or directory", ignore it (or log it)
        if e.errno != errno.ENOENT:
            # Otherwise, raise the error
            raise
            
# Example usage
remove_file("myfile")
```

The following examples use the Bash shell. To safely remove a file even if it doesn't exist, use:

```
rm -f my_file
```

To safely move (rename) a file, run the move command only if the file `old_name` exists in the current directory. 

```
[ -f old_name ] && mv old_name new_name
```

For creating a directory, use the following command:

```
mkdir -p mydir/subdir/  
```

## Static run storage
<a name="workflows-run-type-static"></a>

For static run storage, the run provisions a filesystem that uses the Lustre protocol. This protocol is resilient to non-idempotent file operations by default. You do not need to adjust your workflow code to handle non-idempotent file operations. 

HealthOmics allocates a fixed amount of run storage. You specify this value when you start the run. The default run storage is 1200 GiB, if you don't specify a value. The supported storage sizes are 1,200 GiB or multiples of 2,400 GiB (for example, 2,400, 4,800, 7,200 GiB). If your requested size is not a supported value, the system rounds up to the nearest supported size.

For example, if you request 42,000 GiB, the run provisions 43,200 GiB (18 × 2,400 GiB) because 42,000 is not a multiple of 2,400. Similarly, a request for 5,000 GiB provisions 7,200 GiB (3 × 2,400 GiB), and a request for 1,000 GiB provisions the minimum size of 1,200 GiB.

For static run storage, HealthOmics provisions the following throughput values:
+ Baseline throughput of 200 MB/s per TiB of storage capacity provisioned. 
+ Burst throughput up to 1300 MB/s per TiB of storage capacity provisioned.

If the specified storage size is too low, the run fails with an **Out of storage for file system** error. Static run storage is a good fit for predictable workflows with known storage requirements. 

Static run storage is suitable for large, bursty workloads with high task concurrency (for example, a large volume of RNASeq samples processed in parallel). It provides higher file system throughput per GiB and lower cost per GiB than dynamic run storage.

## Calculating required static run storage
<a name="workflows-run-types-calc"></a>

A workflow requires additional capacity when it uses static run storage (compared with dynamic run storage) because the base file system installation uses 7% of the static file system capacity.

If you run a dynamic run storage workflow to measure the maximum storage used by the run, use the following calculation to determine the minimum amount of static storage required: 

```
  static storage required = 
         maximum storage in GiB used by the dynamic run storage  
           + (total static file system size in GiB * 0.07)
```

For example: 

```
     Maximum storage measured from a dynamic run storage workflow run:  500GiB
       File system size: 1200GiB
       7% of the file system size:  84GiB
       500 + 84 = 584GiB of static run storage required for this run.
```

 Therefore, 1200GiB (the minimum capacity for static run storage) is sufficient for this run. 

**Note**  
In addition to shared run storage, HealthOmics provides per-task ephemeral storage at `/tmp`. Redirecting scratch I/O to ephemeral storage can reduce demand on the shared run filesystem. For more information, see [Ephemeral storage for HealthOmics workflow tasks](workflows-ephemeral-storage.md).