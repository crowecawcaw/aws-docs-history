

# Custom Slurm settings for AWS PCS compute node groups
<a name="slurm-custom-settings-cng"></a>

The following custom Slurm settings are supported at the compute node group level:
+ [CpuSpecList](https://slurm.schedmd.com/slurm.conf.html#OPT_CpuSpecList)
+ [Features](https://slurm.schedmd.com/slurm.conf.html#OPT_Features)
+ [MemSpecLimit](https://slurm.schedmd.com/slurm.conf.html#OPT_MemSpecLimit)
+ [Parameters](https://slurm.schedmd.com/slurm.conf.html#OPT_Parameters)
**Note**  
AWS PCS supports `Parameters` on Slurm version 25.11 and later.
+ [RealMemory](https://slurm.schedmd.com/slurm.conf.html#OPT_RealMemory)
+ [Sockets](https://slurm.schedmd.com/slurm.conf.html#OPT_Sockets)
**Note**  
AWS PCS supports `Sockets` on Slurm version 25.11 and later.
+ [Weight](https://slurm.schedmd.com/slurm.conf.html#OPT_Weight)