# Running MPI jobs

As suggested in SchedMD, bootstrap MPI jobs using Slurm as the MPI bootstrapping method. For more information, refer to the official
[Slurm documentation](https://slurm.schedmd.com/mpi_guide.html#intel_mpi "https://slurm.schedmd.com/mpi_guide.html#intel_mpi") or the official documentation for your MPI
library.

For example, in the [IntelMPI official documentation](https://www.intel.com/content/www/us/en/develop/documentation/mpi-developer-reference-linux/top/environment-variable-reference/hydra-environment-variables.html "https://www.intel.com/content/www/us/en/develop/documentation/mpi-developer-reference-linux/top/environment-variable-reference/hydra-environment-variables.html"), you learn that when running a StarCCM job, you must set Slurm as process orchestrator by exporting the
environment variable `I_MPI_HYDRA_BOOTSTRAP=slurm`.

###### Note

Known issue

In the case where your MPI application relies on SSH as mechanism to spawn MPI jobs,
it's possible to incur in a [known bug in Slurm](https://bugs.schedmd.com/show_bug.cgi?id=13385 "https://bugs.schedmd.com/show_bug.cgi?id=13385") that causes the wrong resolution of the directory user name to
"nobody".

Either configure your application to use Slurm as the MPI bootstrapping method or refer to [Known issues with username resolution](troubleshooting-v3-multi-user.md#troubleshooting-v3-multi-user-name-resolution "troubleshooting-v3-multi-user.md#troubleshooting-v3-multi-user-name-resolution") in the Troubleshooting
section for further details and possible workarounds.
