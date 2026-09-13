

# Custom Slurm settings for AWS PCS compute node groups
<a name="slurm-custom-settings-cng"></a>

The following custom Slurm settings are supported at the compute node group level:
+ [CpuSpecList](https://slurm.schedmd.com/slurm.conf.html#OPT_CpuSpecList)
+ [Features](https://slurm.schedmd.com/slurm.conf.html#OPT_Features)
+ [Gres](https://slurm.schedmd.com/slurm.conf.html#OPT_Gres_1)
**Note**  
Use `Gres` to declare the GRES that the compute node group makes schedulable. Every resource that you name here must also be declared as a `gres.conf` record in `gresCustomSettings`, and the counts and types of the two must be consistent. To configure the underlying GRES devices and for the full list of constraints, see [Configuring custom GRES settings in AWS PCS](gres-custom-settings.md).
+ [MemSpecLimit](https://slurm.schedmd.com/slurm.conf.html#OPT_MemSpecLimit)
+ [Parameters](https://slurm.schedmd.com/slurm.conf.html#OPT_Parameters)
**Note**  
AWS PCS supports `Parameters` on Slurm version 25.11 and later.
+ [RealMemory](https://slurm.schedmd.com/slurm.conf.html#OPT_RealMemory)
+ [Sockets](https://slurm.schedmd.com/slurm.conf.html#OPT_Sockets)
**Note**  
AWS PCS supports `Sockets` on Slurm version 25.11 and later.
+ [Weight](https://slurm.schedmd.com/slurm.conf.html#OPT_Weight)