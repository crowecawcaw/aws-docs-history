

# Extend Slurm functionality on AWS PCS with SPANK plugins
<a name="spank"></a>

Use SPANK (Slurm Plug-in Architecture for Node and job Kontrol) plugins to extend and modify Slurm's behavior during job launch and execution on AWS PCS clusters. SPANK plugins provide a generic interface to intercept and modify job launch stages.

Install SPANK plugins on your compute node AMI and configure them to customize your Slurm cluster's behavior for your workload requirements. For more information about SPANK, see the [SPANK documentation](https://slurm.schedmd.com/spank.html) on the SchedMD website.

**Contents**
+ [Install SPANK plugins on AWS PCS](spank_install.md)
+ [Configure SPANK plugins on AWS PCS](spank_configure.md)
+ [Frequently asked questions about SPANK plugins on AWS PCS](spank_faq.md)