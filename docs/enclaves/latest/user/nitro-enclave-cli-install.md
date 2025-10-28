# Install the Nitro Enclaves CLI on Linux

The following instructions are for installing or uninstalling the AWS Nitro Enclaves CLI
on or from a parent instance running Amazon Linux 2023 or Amazon Linux 2. For instructions for
installing the Nitro CLI on different Linux distributions, see the [Nitro CLI github
repository](https://github.com/aws/aws-nitro-enclaves-cli "https://github.com/aws/aws-nitro-enclaves-cli").

Amazon Linux 2023

###### To install the Nitro CLI on an instance running AL2023

1. Install the Nitro CLI.

```
`$` sudo dnf install aws-nitro-enclaves-cli -y
```

2. Install the Nitro Enclaves development tools needed to build enclave
   images. The development tools also includes some sample
   applications.

```
`$` sudo dnf install aws-nitro-enclaves-cli-devel -y
```

3. Add your user to the `ne` user group.

```
`$` sudo usermod -aG ne `username`
```

4. Add your user to the `docker` user group.

```
`$` sudo usermod -aG docker `username`
```

###### Important

For the permissions changes to take effect, log out of the instance and
then reconnect to it. 5. Verify that the Nitro CLI installed correctly.

```
`$` nitro-cli --version
```

The command should return version information about the Nitro
CLI. 6. Preallocate the memory and the vCPUs that you intend to use for
the enclaves.

###### Important

Nitro Enclaves uses an allocator service to preallocate vCPUs and
memory to the enclaves. The amount of vCPUs and memory to
preallocate are defined in the allocator service configuration
file (`/etc/nitro_enclaves/allocator.yaml`).
By default, the configuration file is set up to preallocate 512
MiB of memory and 2 vCPUs for use by the enclaves. In some
cases, you might need to manually update the configuration file
to preallocate a different number vCPUs or amount of memory. For
example:

    * If you launched an AWS Graviton-based instance with
     2 vCPUs, you must configure the allocate service to
     preallocate only 1 vCPU.
    * If you launched an instance with 4 or more vCPUs, you
     can configure the allocator service to preallocate more
     vCPUs to the enclave.
    * If you are going to run multiple enclaves, you must
     configure the allocator service to preallocate enough
     vCPUs and memory for all of the enclaves. For example,
     to run 3 enclaves with 4 vCPUs and 2 GiB memory each,
     you must configure the allocator service to preallocate
     12 vCPUs and 6 GiB of memory.If you need to change the configuration file, use your

preferred text editor to open
`/etc/nitro_enclaves/allocator.yaml`. Then, for
`memory_mib` and `cpu_count`, specify
the overall amount of memory (in MiB) and the number of vCPUs
that you want to preallocate. Save and close the file and then
run the command below.

If you want to preallocate the default 512 MiB of memory and 2
vCPUs, you do not need to make any changes to the configuration
file.

Run the following command to allocate the resource specified in
the configuration file and to ensure that they are automatically
allocated every time the instance starts.

```
`$` sudo systemctl enable --now nitro-enclaves-allocator.service
```

###### Note

When you create an enclave, the requested memory and vCPUs
must be less than or equal to the values that you specified
here. If you need to create an enclave with more memory or vCPUs
in the future, you must update the values in this file and
restart the service. 7. Start the Docker service and ensure that it starts every time the
instance starts.

```
`$` sudo systemctl enable --now docker
```

Amazon Linux 2

###### To install the Nitro CLI on an instance running AL2

1. Install the Nitro CLI.

```
`$` sudo amazon-linux-extras install aws-nitro-enclaves-cli -y
```

2. Install the Nitro Enclaves development tools needed to build enclave
   images. The development tools also includes some sample
   applications.

```
`$` sudo yum install aws-nitro-enclaves-cli-devel -y
```

3. Add your user to the `ne` user group.

```
`$` sudo usermod -aG ne `username`
```

4. Add your user to the `docker` user group.

```
`$` sudo usermod -aG docker `username`
```

###### Important

For the permissions changes to take effect, log out of the instance and
then reconnect to it. 5. Verify that the Nitro CLI installed correctly.

```
`$` nitro-cli --version
```

The command should return version information about the Nitro
CLI. 6. Preallocate the memory and the vCPUs that you intend to use for
the enclaves.

###### Important

Nitro Enclaves uses an allocator service to preallocate vCPUs and
memory to the enclaves. The amount of vCPUs and memory to
preallocate are defined in the allocator service configuration
file (`/etc/nitro_enclaves/allocator.yaml`).
By default, the configuration file is set up to preallocate 512
MiB of memory and 2 vCPUs for use by the enclaves. In some
cases, you might need to manually update the configuration file
to preallocate a different number vCPUs or amount of memory. For
example:

    * If you launched an AWS Graviton-based instance with
     2 vCPUs, you must configure the allocate service to
     preallocate only 1 vCPU.
    * If you launched an instance with 4 or more vCPUs, you
     can configure the allocator service to preallocate more
     vCPUs to the enclave.
    * If you are going to run multiple enclaves, you must
     configure the allocator service to preallocate enough
     vCPUs and memory for all of the enclaves. For example,
     to run 3 enclaves with 4 vCPUs and 2 GiB memory each,
     you must configure the allocator service to preallocate
     12 vCPUs and 6 GiB of memory.If you need to change the configuration file, use your

preferred text editor to open
`/etc/nitro_enclaves/allocator.yaml`. Then, for
`memory_mib` and `cpu_count`, specify
the overall amount of memory (in MiB) and the number of vCPUs
that you want to preallocate. Save and close the file and then
run the command below.

If you want to preallocate the default 512 MiB of memory and 2
vCPUs, you do not need to make any changes to the configuration
file.

Run the following command to allocate the resource specified in
the configuration file and to ensure that they are automatically
allocated every time the instance starts.

```
`$` sudo systemctl enable --now nitro-enclaves-allocator.service
```

###### Note

When you create an enclave, the requested memory and vCPUs
must be less than or equal to the values that you specified
here. If you need to create an enclave with more memory or vCPUs
in the future, you must update the values in this file and
restart the service. 7. Start the Docker service and ensure that it starts every time the
instance starts.

```
`$` sudo systemctl enable --now docker
```
