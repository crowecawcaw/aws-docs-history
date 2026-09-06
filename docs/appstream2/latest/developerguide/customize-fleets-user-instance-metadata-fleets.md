

# User and Instance Metadata for Amazon WorkSpaces Applications Fleets
<a name="customize-fleets-user-instance-metadata-fleets"></a>

WorkSpaces Applications fleet instances have user and instance metadata available through Windows environment variables. You can use the following environment variables in your applications and scripts to modify your environment based on the fleet instance details.


| Environment Variable | Context | Description | 
| --- | --- | --- | 
| AppStream\_Stack\_Name | User | The name of the stack from which the streaming session started. | 
| AppStream\_User\_Access\_Mode | User | The access mode used to manage user access to the stream. The available values are custom, userpool, or saml. | 
| AppStream\_Session\_Reservation\_DateTime | User | The date and time when the user's streaming session started. | 
| AppStream\_UserName | User | The user name associated with the user. | 
| AppStream\_Session\_ID | User | The session identifier for the user's streaming session. | 
| APPSTREAM\_SESSION\_CONTEXT | Machine | Contains the parameters passed to your streaming application when a session is started. For more information, see [Session Context in Amazon WorkSpaces Applications](managing-stacks-fleets-session-context.md). This environment variable is only available after the first application launch.  | 
| AppStream\_Image\_Arn | Machine | The ARN of the image that was used to create the streaming instance. | 
| AppStream\_Instance\_Type | Machine | The streaming instance's type. For example, stream.standard.medium. | 
| AppStream\_Resource\_Type | Machine | The type of WorkSpaces Applications resource. The value is either fleet or image-builder. | 
| AppStream\_Resource\_Name | Machine | The fleet's name. | 