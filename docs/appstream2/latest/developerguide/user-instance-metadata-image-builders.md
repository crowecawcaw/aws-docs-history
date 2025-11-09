# Instance Metadata for WorkSpaces Applications

Image Builders

WorkSpaces Applications image builder instances have instance metadata available through Windows
environment variables. You can use the following environment variables in your applications
and scripts to modify your environment based on the image builder instance details.

| Environment Variable    | Context | Description                                                                                  |
| ----------------------- | ------- | -------------------------------------------------------------------------------------------- |
| AppStream_Image_Arn     | Machine | The ARN of the image that was used to create the streaming<br>instance.                      |
| AppStream_Instance_Type | Machine | The instance type of the streaming instance. For example,<br>`stream.standard.medium`.       |
| AppStream_Resource_Type | Machine | The type of WorkSpaces Applications resource. The value is either `fleet` or `imagebuilder`. |
| AppStream_Resource_Name | Machine | The name of the image builder.                                                               |

On Linux image builders, environment variables are exported through the script at
**/etc/profile.d/appstream_system_vars.sh**. To access the environment
variables, you can explicitly source this file in your application.
