# Choose application images and hardware plans for

Lightsail for Research

When you create an Amazon Lightsail for Research virtual computer, you select an application and a
hardware plan (plan) for it.

An _application_ provides a software configuration (for example, an
application and operating system). A _plan_ provides the hardware of
the virtual computer, such as the number of vCPUs, memory, storage space, and monthly
data transfer allowance. Together, the application and plan make up the virtual computer
configuration.

###### Note

You can't change the application or plan of your virtual computer after it's
created. However, you can create a snapshot of the virtual computer, and then choose
a new plan when creating a new virtual computer from the snapshot. For more
information about snapshots, see [Backup virtual computers and disks with Lightsail for Research snapshots](snapshots.md "snapshots.md").

###### Topics

- [Applications](#blueprints "#blueprints")
- [Plans](#plans "#plans")

## Applications

Amazon Lightsail for Research provides and manages machine images that contain the application and
operating system required to launch a virtual computer. You choose from a list of
applications when you create a virtual computer in Lightsail for Research. All Lightsail for Research application
images use the Ubuntu (Linux) operating system.

The following applications are available in Lightsail for Research:

- **JupyterLab** – JupyterLab is a
  web-based Integrated Development Environment (IDE) for notebooks, code, and
  data. With its flexible interface you can configure and arrange workflows in
  data science, scientific computing, computational journalism, and machine
  learning. For more information, see the [Jupyter Project
  Documentation](https://docs.jupyter.org/en/latest/ "https://docs.jupyter.org/en/latest/").
- **RStudio** – RStudio is an
  open-source Integrated Development Environment (IDE) for R, a programming
  language for statistical computing and graphics, and Python. It combines a
  source code editor, build automation tools and a debugger, as well as tools
  for plotting and workspace management. For more information, see the [RStudio
  IDE](https://posit.co/products/open-source/rstudio/ "https://posit.co/products/open-source/rstudio/").
- **VSCodium** – VSCodium is a
  community-driven, binary distribution of Microsoft’s editor VS Code. For
  more information, see [VSCodium](https://vscodium.com/ "https://vscodium.com/").
- **Scilab** – Scilab is an open source
  numerical computational package, and a high-level, numerically oriented
  programming language. For more information, see [Scilab](https://www.scilab.org/ "https://www.scilab.org/").
- **Ubuntu 20.04 LTS** – Ubuntu is an
  open source Linux distribution based on Debian. Lean, fast and powerful,
  Ubuntu Server delivers services reliably, predictably and economically. It's
  a great base on which to build your virtual computers. For more information,
  see [Ubuntu
  releases](https://releases.ubuntu.com/focal/ "https://releases.ubuntu.com/focal/").

## Plans

A plan provides the hardware specifications and determines the pricing for your
Lightsail for Research virtual computer. A plan includes a fixed amount of memory (RAM), compute
(vCPUs), SSD-based storage volume (disk) space, and a monthly data transfer
allowance. Plans are charged on an hourly, on-demand basis, so you only pay for the
time your virtual computer is running.

The plan that you choose might depend on the resources that your workload
requires. Lightsail for Research offers the following plans types:

- **Standard** – Standard plans are
  compute-optimized and ideal for compute-bound applications that benefit from
  high-performance processors.
- **GPU** – GPU plans provide a
  cost-effective, high-performance platform for general purpose GPU computing.
  You can use these plans to accelerate scientific, engineering, and rendering
  applications and workloads.

### Standard plans

Following are the hardware specifications of the standard plans available in
Lightsail for Research.

| Plan name    | vCPUs | Memory | Storage space | Monthly data transfer allowance |
| ------------ | ----- | ------ | ------------- | ------------------------------- |
| Standard XL  | 4     | 8 GB   | 50 GB         | 512 GB                          |
| Standard 2XL | 8     | 16 GB  | 50 GB         | 512 GB                          |
| Standard 4XL | 16    | 32 GB  | 50 GB         | 512 GB                          |

### GPU plans

Following are the hardware specifications of the GPU plans available in
Lightsail for Research.

| Plan name | vCPUs | Memory | Storage space | Monthly data transfer allowance |
| --------- | ----- | ------ | ------------- | ------------------------------- |
| GPU XL    | 4     | 16 GB  | 50 GB         | 1 TB                            |
| GPU 2XL   | 8     | 32 GB  | 50 GB         | 1 TB                            |
| GPU 4XL   | 16    | 64 GB  | 50 GB         | 1 TB                            |
