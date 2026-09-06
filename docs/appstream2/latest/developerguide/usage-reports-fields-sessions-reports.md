

# Sessions Report Fields
<a name="usage-reports-fields-sessions-reports"></a>

The following table describes the fields included in WorkSpaces Applications sessions reports.


| Field name | Description | 
| --- | --- | 
| user\_session\_id | The unique identifier (ID) for the session. | 
| aws\_account\_id | The Amazon Web Services account ID. | 
| region | The AWS Region. | 
| session\_start\_time | The date and time that the session started. Must be specified in ISO 8601 format and as UTC. | 
| session\_end\_time | The date and time that the session ended. Must be specified in ISO 8601 format and as UTC. | 
| session\_duration\_in\_seconds | The duration of the session in seconds. | 
| user\_id | The unique ID for the user within the authentication type. | 
| user\_arn | The Amazon Resource Name (ARN) for the user. | 
| authentication\_type | The method used to authenticate the user.<br />Possible values: `CUSTOM` \| `SAML` \| `USERPOOL` | 
| authentication\_type\_user\_id | The concatenation of the user ID and authentication type, which uniquely identifies the user for the purpose of assessing user fees. For more information, see [WorkSpaces Applications Pricing](https://aws.amazon.com/appstream2/pricing/). | 
| fleet\_name | The name of the fleet associated with the session. | 
| stack\_name | The name of the stack associated with the session. | 
| instance\_type | The WorkSpaces Applications instance type used for the session. For a list of instance types, see [WorkSpaces Applications Pricing](https://aws.amazon.com/appstream2/pricing/). | 
| eni\_private\_ip\_address | The IP address of the elastic network interface used by the WorkSpaces Applications instance for network communications. | 
| connected\_at\_least\_once | Indicates whether the user connected to the session at least once.<br />Possible values: `true` \| `false` | 
| client\_ip\_addresses | The IP addresses associated with the user device or devices used to connect to the session. If the user connected and then disconnected from the session more than once, up to the last 10 distinct IP addresses are stored, separated by semicolons. | 
| google\_drive\_enabled | Indicates whether Google Drive was enabled as a persistent storage option for the session. For more information, see [Enable and Administer Google Drive for Your WorkSpaces Applications Users](google-drive.md). <br />Possible values: `true` \| `false` | 
| one\_drive\_enabled | Indicates whether OneDrive was enabled as a persistent storage option for the session. For more information, see [Enable and Administer Google Drive for Your WorkSpaces Applications Users](google-drive.md). <br />Possible values: `true` \| `false` | 
| home\_folders\_storage\_location | The Amazon S3 bucket used for files that are stored using home folders. | 
| user\_settings\_clipboard\_copy\_from\_local\_device | Indicates whether the user was able to copy data from the local device to the streaming session using the clipboard during the session.<br />Possible values: `ENABLED` \| `DISABLED` | 
| user\_settings\_clipboard\_copy\_to\_local\_device | Indicates whether the user was able to copy data from the streaming session to the local device using the clipboard during the session.<br />Possible values: `ENABLED` \| `DISABLED` | 
| user\_settings\_file\_upload | Indicates whether the user was able to upload files from the local device to the streaming session during the session.<br />Possible values: `ENABLED` \| `DISABLED` | 
| user\_settings\_file\_download | Indicates whether the user was able to download files from the streaming session to the local device during the session.<br />Possible values: `ENABLED` \| `DISABLED` | 
| user\_settings\_printing\_to\_local\_device | Indicates whether the user was able to print files from the streaming session to the local device during the session.<br />Possible values: `ENABLED` \| `DISABLED` | 
| application\_settings\_enabled | Indicates whether application settings persistence was enabled for the session.<br />Possible values: `true` \| `false` | 
| domain\_joined | Indicates whether the WorkSpaces Applications streaming instance was joined to an Active Directory domain at session launch. For more information, see [Using Active Directory with WorkSpaces Applications](active-directory.md). <br />Possible values: `Y` \| `N` | 
| max\_session\_duration | The maximum allowed duration of the session, in seconds. | 
| session\_type | The session type.<br />Possible values: `ALWAYS_ON` \| `ON_DEMAND` | 
| stream\_view | The stream view.<br />Possible values: `APPLICATION` \| `DESKTOP` | 
| streaming\_experience\_settings\_protocol | The protocol that the session ended streaming with.<br />Possible values: `UDP` \| `TCP` | 
| instance\_id | The instance ID associated with the user session. | 
| is\_multisession | Indicates whether the session belongs to a multi-session fleet.<br />Possible values: `true` \| `false` | 