

# Instance Metadata for WorkSpaces Applications Image Builders
<a name="user-instance-metadata-image-builders"></a>

WorkSpaces Applications image builder instances have instance metadata available through Windows environment variables. You can use the following environment variables in your applications and scripts to modify your environment based on the image builder instance details.


| Environment Variable | Context | Description | 
| --- | --- | --- | 
| AppStream\_Image\_Arn | Machine | The ARN of the image that was used to create the streaming instance. | 
| AppStream\_Instance\_Type | Machine | The instance type of the streaming instance. For example, stream.standard.medium. | 
| AppStream\_Resource\_Type | Machine | The type of WorkSpaces Applications resource. The value is either fleet or imagebuilder. | 
| AppStream\_Resource\_Name | Machine | The name of the image builder. | 

On Linux image builders, environment variables are exported through the script at **/etc/profile.d/appstream\_system\_vars.sh**. To access the environment variables, you can explicitly source this file in your application.