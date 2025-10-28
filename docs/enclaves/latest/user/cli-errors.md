# Nitro Enclaves CLI error codes

This section lists the possible errors that the Nitro CLI can return.

**`E01`**

**Missing mandatory argument.** At least one
mandatory argument has not been specified. Ensure that all mandatory
arguments have been specified.

**`E02`**

**Conflicting arguments.** The command
includes two or more incompatible arguments. Ensure that you specify only
one of the conflicting arguments. For example, you cannot specify
`--cpu-count` and `--cpu-ids` in the same
`run-enclave` command.

**`E03`**

**Invalid argument provided.** A value of the
incorrect type has been specified for one or more arguments. For example, a
string was specified for an argument that expects an integer. Ensure that
all values are of the expected type.

**`E04`**

**Socket pair creation failure.** The
Nitro CLI attempted to open a stream pair with the enclave, but the
stream initialization has failed. Either there is insufficient memory
available for the Nitro CLI process, or the system-wide maximum number of
open descriptors was reached. Retry the command. If that fails, reboot the
instance and then retry the command.

**`E05`**

**Process spawn failure.** The Nitro CLI
failed to spawn the enclave process while running the
`run-enclave` command. Either the system has reached its
maximum number of threads, or there is insufficient memory available to
spawn the new process. Ensure that the system has enough free memory and
then retry the command. If that fails, reboot the instance and then retry
the command.

**`E06`**

**Daemonize process failure.** An error
occurred while attempting to daemonize the newly spawned enclave process.
Possible reasons are that the system has reached its maximum number of
threads, there is insufficient memory available to spawn the new process, or
the configuration of the Nitro CLI main process is not allowing the daemon
creation process. Ensure that the system has enough free memory and then
retry the command. If that fails, reboot the instance and then retry the
command.

**`E07`**

**Read from disk failure.** The
Nitro CLI failed to read content from the enclave's socket directory
(typically `/var/run/nitro_enclaves/`) while running the
`describe-enclave` command. Ensure that the directory exists
and that it has the correct permissions. Alternatively, run the Nitro Enclaves
configuration script to reconfigure the environment.

**`E08`**

**Unusable connection error.** The
Nitro CLI is unable to connect to an enclave. Ensure that it exists and
that it is in the `running` state.

**`E09`**

**Socket close error.** The Nitro CLI is
unable to close the communication channel. The socket close operation was
interrupted by another signal. Retry the command.

**`E10`**

**Socket connect set timeout error.** The
Nitro CLI failed to configure a specific timeout for the specified
socket. Ensure that the operation is being performed on a valid
socket.

**`E11`**

**Socket error.** An unexpected error
occurred with the socket.

**`E12`**

**Epoll error.** The Nitro CLI failed to
register the enclave descriptor for event monitoring with
`epoll`. Either the system has insufficient memory to handle the
requested operation, or the per-user maximum number of watches was reached
while trying to register a new descriptor on an epoll instance. Ensure that
the system has enough free memory and then retry the command. If that fails,
reboot the instance and then retry the command.

**`E13`**

**Inotify error.** The Nitro CLI failed
to configure a socket for monitoring. Either the system has insufficient
memory to handle the requested operation, or the user limit of inotify
watches has been reached. Ensure that the system has enough free memory and
then retry the command. If that fails, reboot the instance and then retry
the command.

**`E14`**

**Invalid command.** An unknown command or
command argument was specified. Verify the command and argument
names.

**`E15`**

**Lock acquire failure.** The Nitro CLI
failed to obtain a lock on an object with concurrent access, such as a
structure containing information about a running enclave. A previous thread
failed an operation while holding the lock. Retry the command. If that
fails, reboot the instance and then retry the command.

**`E16`**

**Thread join failure.** The Nitro CLI failed to
join a thread after it finished executing. Retry the command.

**`E17`**

**Serde error.** An error occurred while
serializing or deserializing a command or command response. The JSON in the
supplied command might not be valid. If you are supplying command arguments
in the JSON file, ensure that the supplied JSON is valid.

**`E18`**

**File permissions error.** You do not have
permission to modify the logging file (typically
`/var/log/nitro_enclaves/nitro_enclaves.log`). Ensure that
your user is part of the `ne` user group. For more information,
see [Install the Nitro Enclaves CLI on Linux](nitro-enclave-cli-install.md "nitro-enclave-cli-install.md").

**`E19`**

**File operation failure.** The system failed
to perform the requested file operations. Ensure that the file on which the
operation is performed exists and that you have permission to modify
it.

**`E20`**

**Invalid CPU configuration.** The same CPU
ID has been specified more than once for the `--cpu-ids`
argument. Ensure that each vCPU ID is specified only once.

**`E21`**

**No such CPU available in the pool.** One or more of
the specified CPU IDs does not exist in the CPU pool. Either retry the
command and specify different vCPU
IDs, or preallocate the environment resources so that the vCPU pool includes
the vCPU IDs that you want to
use. For more information, see [Install the Nitro Enclaves CLI on Linux](nitro-enclave-cli-install.md "nitro-enclave-cli-install.md").

**`E22`**

**Insufficient CPUs available in the pool.** The number of
requested vCPUs is greater than the number of available vCPUs. Either
specify a number of vCPUs less than or equal to the configured vCPU pool
size, or preallocate the environment resources so that the vCPU pool
includes the number of vCPUs that you want to use. For more information, see
[Install the Nitro Enclaves CLI on Linux](nitro-enclave-cli-install.md "nitro-enclave-cli-install.md").

**`E23`**

**Malformed CPU ID error.** This error
appears when a `lscpu` line is malformed and it reports an online
CPUs list that is not valid. Ensure that the `lscpu` output is
not corrupt.

**`E24`**

**CPU error.** A CPU line interval is not
valid. Ensure that the `lscpu` output is not corrupt.

**`E25`**

**No such hugepage flag error.** The enclave
process attempted to use a hugepage size that is not valid for initializing
the enclave memory. Make sure that the Nitro CLI code has not been modified
to include hugepage sizes that are not valid.

**`E26`**

**Insufficient memory requested.**
Insufficient memory was requested for the enclave. The memory should be
equal to or greater than the size of the enclave image file. Preallocate
enough memory to ensure that the enclave image file fits in the enclave's
memory. For more information, see [Install the Nitro Enclaves CLI on Linux](nitro-enclave-cli-install.md "nitro-enclave-cli-install.md").

**`E27`**

**Insufficient memory available.** The amount
of requested memory is greater than the amount of available memory. The
enclave memory should not be greater than the size of the configured
hugepage memory. For example, if you request 100 MiB of memory while the
allocated hugepage memory is 80MiB, the request fails. Preallocate enough
memory for the enclave. For more information, see [Install the Nitro Enclaves CLI on Linux](nitro-enclave-cli-install.md "nitro-enclave-cli-install.md"). Alternatively, specify a
smaller amount of memory with the `run-enclave` command.

**`E28`**

**Invalid enclave descriptor.**
`NE_CREATE_VM ioctl` returned an error. Review the error
backtrace for more information.

**`E29`**

**Ioctl failure.** An unexpected
`ioctl` error occurred. Review the error backtrace for more
information.

**`E30`**

**Ioctl image get load info failure.** The
`ioctl` used for getting the memory load information failed.
Review the error backtrace for more information.

**`E31`**

**Ioctl set memory region failure.** The
`ioctl` used for setting a given memory region has failed.
Review the error backtrace for more information.

**`E32`**

**Ioctl add vCPU failure.** The
`ioctl` used for adding a vCPU failed. Review the error
backtrace for more information.

**E33**

**Ioctl start enclave failure.** The
`ioctl` used for starting an enclave has failed. Review the
error backtrace for more information.

**`E34`**

**Memory overflow.** An error occurred while
loading the enclave image file in memory regions that will be conceded to
the future enclave. For example, this can occur if the regions offset plus
the enclave image file size exceeds the maximum address of the target
platform.

**`E35`**

**EIF file parsing error.** Failed to fill a
memory region with a section of the enclave image file.

**`E36`**

**Enclave boot failure.** The enclave failed
to return a `ready` signal after booting. For example, if booting
from an enclave image file that is not valid, the enclave process exits
immediately, before returning a ready signal. Ensure that the enclave image
file is not corrupt. Review the error backtrace for more information.

**`E37`**

**Enclave event wait error.** Failed to
monitor an enclave descriptor for events.

**`E38`**

**Enclave process command not executed
error.** At least one enclave process failed to provide the
description information.

**`E39`**

**Enclave process connection failure.** The
enclave manager failed to connect to at least one enclave process for
retrieving the description information.

**`E40`**

**Socket path not found.** The Nitro CLI
failed to build the corresponding socket path starting from a given enclave
ID.

**`E41`**

**Enclave process send reply failure.** The
enclave process failed to report its status to the requesting
command.

**`E42`**

**Enclave mmap error.** Failed to allocate
memory to the enclave. Make sure that the system has enough free memory
available. Retry the command. If that fails, reboot the instance and then
retry the command.

**`E43`**

**Enclave munmap error.** Failed to unmap an
enclave's memory. Make sure that the Nitro CLI code has not been modified to
pass flags to the memory region unmapping operation that are not
valid.

**`E44`**

**Enclave console connection failure.** The
Nitro CLI failed to establish a connection with a running enclave's
console. Make sure that the enclave has been started with the
`--debug` flag.

**`E45`**

**Enclave console read error.** Failed to
read from a running enclave's console. Retry the command.

**`E46`**

**Enclave console write output error.**
Failed to write the information retrieved from a running enclave's console
to a stream. Retry the command.

**`E47`**

Integer parsing error. Unable to connect to a running enclave's console
because the CID could not be parsed. Use the `nitro-cli
 describe-enclaves` command to confirm the CID, and to ensure that
it is a valid number.

**`E48`**

**EIF building error.** An error occurred
while building the enclave image file. Review the error backtrace for more
information.

**`E49`**

**Docker image build error.** An error
occurred while building the enclave image file because the specified Docker
image could not be built. Review the error backtrace for more
information.

**`E50`**

**Docker image pull error.** An error
occurred while building the enclave image file because the specified Docker
image could not be pulled. Review the error backtrace for more
information.

**`E51`**

**Artifacts path environment variable not
set.** An error occurred while building the enclave image file
because the artifacts path environment variable has not been set.

**`E52`**

**Blobs path environment variable not set.**
An error occurred while building the enclave image file because the blobs
path environment variable has not been set. Retry the command.

**`E53`**

**Clock skew error.** Failed to measure the
elapsed time between consecutive reads from a running enclave's console.
Retry the command.

**`E54`**

**Signal masking error.** Failed to mask
specific signals after creating an enclave process. Retry the
command.

**`E55`**

**Signal unmasking error.** Failed to unmask
specific signals after creating an enclave process. Retry the
command.

**`E56`**

**Logger error.** An error occurred while
initializing the underlying logging system. Review the error backtrace for
more information.

**`E57`**

**Hasher error.** An I/O error occurred while
initializing a hasher or while writing bytes to the hasher.

**`E58`**

**Naming error.** The specified enclave name
does not exist.

**`E59`**

**EIF signature checker error.** An error
occurred while validating the signing certificate.
