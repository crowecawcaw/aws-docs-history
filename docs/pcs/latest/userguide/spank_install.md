# Install SPANK plugins on AWS PCS

Follow the plugin's documentation to install SPANK plugins on your AMI.

Compile SPANK plugins for the specific Slurm version on your cluster.
The Slurm installer provided by AWS PCS stores Slurm in `/opt/aws/pcs/scheduler/slurm-`version``. When you compile the plugin, specify the Slurm version.

The following example shows how to specify the Slurm version for some plugins:

```
export CFLAGS="-I/opt/aws/pcs/scheduler/slurm-`version`/include"
```

If you have multiple Slurm versions in the AMI, compile the plugin for each version. Store the compiled plugins in versioned folders.

The following example shows how to specify the destination folder for some plugins:

```
export DESTDIR="`your-preferred-versioned-path`"
```

###### Important

Plugins might require different variables. See the official documentation for the plugin that you're installing.
