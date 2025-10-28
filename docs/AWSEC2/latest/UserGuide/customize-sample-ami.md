# Customize the sample Amazon Linux 2023 image description for your workload

You can customize the sample Amazon Linux 2023 image description and include the software packages,
scripts, and files that are needed for your specific workload. Customizations are achieved by adding to or
modifying various elements in the KIWI NG image description.

###### Topics

- [Repository management](#prepare-custom-image-repos "#prepare-custom-image-repos")
- [Package management](#customize-sample-ami-packages "#customize-sample-ami-packages")
- [Adding files and directories](#customize-sample-ami-overlay "#customize-sample-ami-overlay")
- [Adding custom scripts](#customize-sample-ami-script "#customize-sample-ami-script")

## Repository management

By default, the sample image description includes a single `<repository>` element that
points to a mirror endpoint for the Amazon Linux 2023 core repositories. If needed, you can add references to
other repositories from which to install your required software.

The sample image description uses the `dnf` package manager, as defined in the
`<packagemanager>` element.

For more information about adding repositories, see
[Setting up Repositories](https://osinside.github.io/kiwi/concept_and_workflow/repository_setup.html "https://osinside.github.io/kiwi/concept_and_workflow/repository_setup.html").

## Package management

By default, the sample image description includes all of the packages needed to create an Amazon Linux 2023
Attestable AMI for an isolated compute environment with an `erofs` read-only file system.

You can include additional software packages in the image description by adding them to the
`<packages>` element in the image description. The `<packages>` element
defines all of the software that should be installed into the AMI.

You can also use the `<packages>` element to uninstall or delete specific software
packages.

For more information about adding or removing packages in the image description, see
[Adding and Removing
Packages](https://osinside.github.io/kiwi/concept_and_workflow/packages.html# "https://osinside.github.io/kiwi/concept_and_workflow/packages.html#").

## Adding files and directories

The sample image description includes an overlay tree directory (`/root/`). The
overlay tree directory is a directory that contains files and directories that will be copied into the
image during the image build process. Any files and directories that you place into the overlay tree
directory will be copied directly into the root filesystem of the image during the image building
process.

The overlay tree directory is copied into the image after all the packages have been installed.
New files are added and existing files are overwritten.

## Adding custom scripts

The sample image description includes a single custom script, `edit_boot_install.sh`.
This script includes the commands that are needed to run the `nitro-tpm-pcr-compute`
utility, which generates the reference measurements based on the image content. This script is called immediately
after the bootloader is installed.

If needed, you can include your own custom scripts in the image description to perform tasks or
configurations during the image build process or at first boot of the image. Using scripts enables you to
customize your images in ways that cannot be achieved using the image description alone.

To include custom scripts in your image description, you need to name them correctly based on the
type of script, and add them to the same directory as the `appliance.kiwi` file. KIWI NG
automatically detects and executes the scripts if they are named correctly and placed in the correct
location, without the need to explicitly reference them in the image description file.

For more information about the scripts supported by KIWI NG, see
[User-Defined Scripts](https://osinside.github.io/kiwi/concept_and_workflow/shell_scripts.html "https://osinside.github.io/kiwi/concept_and_workflow/shell_scripts.html").
