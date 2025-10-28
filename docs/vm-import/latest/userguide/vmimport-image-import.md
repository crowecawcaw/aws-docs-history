# Import a VM to Amazon EC2 as an image using VM Import/Export

###### Tip

To import your virtual machines (VMs) with a console-based experience, you can use the
_Import virtual machine images to AWS_ template in the [Migration Hub Orchestrator console](https://console.aws.amazon.com/migrationhub/orchestrator "https://console.aws.amazon.com/migrationhub/orchestrator"). For more
information, see the [_AWS Migration Hub Orchestrator
User Guide_](../../../migrationhub-orchestrator/latest/userguide/import-vm-images.md "../../../migrationhub-orchestrator/latest/userguide/import-vm-images.md").

You can use VM Import/Export to import virtual machine (VM) images from your virtualization
environment to Amazon EC2 as Amazon Machine Images (AMI), which you can use to launch instances.
Subsequently, you can export the VM images from an instance back to your virtualization environment.
This enables you to leverage your investments in the VMs that you have built to meet your IT security,
configuration management, and compliance requirements by bringing them into Amazon EC2.

###### Contents

- [Export your VM from its virtualization environment](export-vm-image.md "export-vm-image.md")
- [Programmatic modifications made to VMs by VM Import/Export](import-modify-vm.md "import-modify-vm.md")
- [Import your VM as an image](import-vm-image.md "import-vm-image.md")
- [Monitor an import image task](check-import-task-status.md "check-import-task-status.md")
- [Cancel an import image task](cancel-upload.md "cancel-upload.md")
- [Create an EC2 instance from an imported image](import-vm-next-steps.md "import-vm-next-steps.md")
