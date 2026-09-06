

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Launch template cleanup and fixing
<a name="ec2-considerations"></a>

AWS Transform MGN runs a mechanism every hour to ensure that the settings selected are correct. This mechanism can fix issues such as an incorrect instance type, but it cannot fix other settings and augmentations. Ensure that you follow the instructions in the following sections and do not change or edit any fields that should not be changed. 

If you encounter any issues with the launch template, you can negate all of your changes and fix all issues rapidly by choosing the original default launch template that was first automatically created by MGN upon Agent installation.