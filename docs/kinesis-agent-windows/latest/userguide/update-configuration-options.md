# Configuring Automatic Updates

Use the `appsettings.json` configuration file to enable automatic
updating of Amazon Kinesis Agent for Microsoft Windows and the configuration file for Kinesis Agent for Windows. To control the update behavior,
specify the `Plugins` key-value pair at the same level in the configuration file as
`Sources`, `Sinks`, and `Pipes`.

The `Plugins` key-value pair specifies the additional general functionality to
use that does not fall specifically under the categories of sources, sinks, and pipes. For
example, there is a plugin for updating Kinesis Agent for Windows, and there is a plugin for updating the
`appsettings.json` configuration file. Plugins are represented as JSON
objects and always have a `Type` key-value pair. The `Type` determines
what other key-value pairs can be specified for the plugin. The following plugin types are
supported:

`PackageUpdate`

Specifies that Kinesis Agent for Windows should periodically check a package version configuration file.
If the package version file indicates that a different version of Kinesis Agent for Windows should be
installed, then Kinesis Agent for Windows downloads that version and installs it. The
`PackageUpdate` plugin key-value pairs include:

`Type`

The value must be the string `PackageUpdate`, and it is
required.

`Interval`

Specifies how often to check the package version file for any changes in minutes
represented as a string. This key-value pair is optional. If it is not specified,
the default value is 60 minutes. If the value is less than 1, no update checking
occurs.

`PackageVersion`

Specifies the location of the package version JSON file. The file can reside on
a file share (`file://`), a website (`http://`), or Amazon S3
(`s3://`). For example, a value of
`s3://mycompany/config/agent-package-version.json` indicates that Kinesis Agent for Windows
should check the contents of the `config/agent-package-version.json` file
in the `mycompany` Amazon S3 bucket. It should perform updates based on the
contents of that file.

###### Note

The value of the `PackageVersion` key-value pair is case sensitive
for Amazon S3.

The following is an example of the contents of a package
version file:

```
{
    "Name": "AWSKinesisTap",
    "Version": "1.0.0.106",
    "PackageUrl": "https://s3-us-west-2.amazonaws.com/kinesis-agent-windows/downloads/AWSKinesisTap.{Version}.nupkg"
}
```

The `Version` key-value pair specifies what version of Kinesis Agent for Windows should
be installed if it is not already installed. The `{Version}` variable
reference in the `PackageUrl` resolves the value you specify for the
`Version` key-value pair. In this example, the variable resolves to the
string `1.0.0.106`. This variable resolution is provided so that there
can be a single place in the package version file where the specific desired version
is stored. You can use multiple package version files to control the pace of rolling
out new versions of Kinesis Agent for Windows to validate a new version before a larger deployment. To
roll back a deployment of Kinesis Agent for Windows, change one or more package version files to specify
an earlier version of Kinesis Agent for Windows that is known to work in your environment.

The value of the `PackageVersion` key-value pair is affected by
variable substitution to facilitate the automatic selection of different package
version files. For more information about variable substitution, see [Configuring Sink Variable
Substitutions](sink-object-declarations.md#configuring-kinesis-agent-windows-sink-variable-substitution "sink-object-declarations.md#configuring-kinesis-agent-windows-sink-variable-substitution").

`AccessKey`

Specifies which access key to use when authenticating access to the package
version file in Amazon S3. This key-value pair is optional. We do not recommend using
this key-value pair. For alternative authentication approaches that are recommended,
see [Configuring Authentication](sink-object-declarations.md#configuring-kinesis-agent-windows-authentication "sink-object-declarations.md#configuring-kinesis-agent-windows-authentication").

`SecretKey`

Specifies which secret key to use when authenticating access to the package
version file in Amazon S3. This key-value pair is optional. We do not recommend using
this key-value pair. For alternative authentication approaches that are recommended,
see [Configuring Authentication](sink-object-declarations.md#configuring-kinesis-agent-windows-authentication "sink-object-declarations.md#configuring-kinesis-agent-windows-authentication").

`Region`

Specifies what Region endpoint to use when accessing the package version file
from Amazon S3. This key-value pair is optional.

`ProfileName`

Specifies which security profile to use when authenticating access to the
package version file in Amazon S3. For more information, see [Configuring Authentication](sink-object-declarations.md#configuring-kinesis-agent-windows-authentication "sink-object-declarations.md#configuring-kinesis-agent-windows-authentication"). This key-value pair is
optional.

`RoleARN`

Specifies which role to assume when authenticating access to the package version
file in Amazon S3 in a cross-account scenario. For more information, see [Configuring Authentication](sink-object-declarations.md#configuring-kinesis-agent-windows-authentication "sink-object-declarations.md#configuring-kinesis-agent-windows-authentication"). This key-value pair is
optional.

If no `PackageUpdate` plugin is specified, then no package version files
are checked to determine if an update is required.

`ConfigUpdate`

Specifies that Kinesis Agent for Windows should periodically check for an updated
`appsettings.json` configuration file stored in a file share,
website, or Amazon S3. If an updated configuration file exists, it is downloaded and installed
by Kinesis Agent for Windows. `ConfigUpdate` key-value pairs include the following:

`Type`

The value must be the string `ConfigUpdate`, and it is
required.

`Interval`

Specifies how often to check for a new configuration file in minutes represented
as a string. This key-value pair is optional, and if not specified, defaults to 5
minutes. If the value is less than 1, then the configuration file update is not
checked.

`Source`

Specifies where to look for an updated configuration file. The file can reside
on a file share (`file://`), a website (`http://`), or Amazon S3
(`s3://`). For example, a value of
`s3://mycompany/config/appsettings.json` indicates that Kinesis Agent for Windows should
check for updates to the `config/appsettings.json` file in the
`mycompany` Amazon S3 bucket.

###### Note

The value of the `Source` key-value pair is case-sensitive for
Amazon S3.

The value of the `Source` key-value pair is affected by variable
substitution to facilitate the automatic selection of different configuration files.
For more information about variable substitution, see [Configuring Sink Variable
Substitutions](sink-object-declarations.md#configuring-kinesis-agent-windows-sink-variable-substitution "sink-object-declarations.md#configuring-kinesis-agent-windows-sink-variable-substitution").

`Destination`

Specifies where to store the configuration file on the local machine. This can
be a relative path, an absolute path, or a path containing environment variable
references such as `%PROGRAMDATA%`. If the path is relative, it is
relative to the location where Kinesis Agent for Windows is installed. Typically the value should be
`.\appsettings.json`. This key-value pair is required.

`AccessKey`

Specifies which access key to use when authenticating access to the
configuration file in Amazon S3. This key-value pair is optional. We do not recommend
using this key-value pair. For alternative authentication approaches that are
recommended, see [Configuring Authentication](sink-object-declarations.md#configuring-kinesis-agent-windows-authentication "sink-object-declarations.md#configuring-kinesis-agent-windows-authentication").

`SecretKey`

Specifies which secret key to use when authenticating access to the
configuration file in Amazon S3. This key-value pair is optional. We do not recommend
using this key-value pair. For alternative authentication approaches that are
recommended, see [Configuring Authentication](sink-object-declarations.md#configuring-kinesis-agent-windows-authentication "sink-object-declarations.md#configuring-kinesis-agent-windows-authentication").

`Region`

Specifies what Region endpoint to use when accessing the configuration file from
Amazon S3. This key-value pair is optional.

`ProfileName`

Specifies which security profile to use when authenticating access to the
configuration file in Amazon S3. For more information, see [Configuring Authentication](sink-object-declarations.md#configuring-kinesis-agent-windows-authentication "sink-object-declarations.md#configuring-kinesis-agent-windows-authentication"). This key-value pair is
optional.

`RoleARN`

Specifies which role to assume when authenticating access to the configuration
file in Amazon S3 in a cross-account scenario. For more information, see [Configuring Authentication](sink-object-declarations.md#configuring-kinesis-agent-windows-authentication "sink-object-declarations.md#configuring-kinesis-agent-windows-authentication"). This key-value pair is
optional.

If no `ConfigUpdate` plugin is specified, then no configuration files are
checked to determine whether a configuration file update is required.

The following is an example `appsettings.json` configuration file that
demonstrates using the `PackageUpdate` and `ConfigUpdate` plugins. In this
example, there is package version file located in the `mycompany` Amazon S3 bucket named
`config/agent-package-version.json`. This file is checked for any changes
approximately every 2 hours. If a different version of Kinesis Agent for Windows is specified in the package version
file, the specified agent version is installed from the specified location in the package
version file.

In addition, there is an `appsettings.json` configuration file stored in
the `mycompany` Amazon S3 bucket named `config/appsettings.json`. Approximately
every 30 minutes, that file is compared against the current configuration file. If they are
different, the updated configuration file is downloaded from Amazon S3 and installed to the typical
local location for the `appsettings.json` configuration file.

```
{
  "Sources": [
    {
      "Id": "ApplicationLogSource",
      "SourceType": "DirectorySource",
      "Directory": "C:\\LogSource\\",
      "FileNameFilter": "*.log",
      "RecordParser": "SingleLine"
    }
  ],
  "Sinks": [
    {
       "Id": "ApplicationLogKinesisFirehoseSink",
       "SinkType": "KinesisFirehose",
       "StreamName": "ApplicationLogFirehoseDeliveryStream",
       "Region": "us-east-1"
    }
    ],
  "Pipes": [
    {
      "Id": "ApplicationLogSourceToApplicationLogKinesisFirehoseSink",
      "SourceRef": "ApplicationLogSource",
      "SinkRef": "ApplicationLogKinesisFirehoseSink"
    }
  ],
  "Plugins": [
    {
      "Type": "PackageUpdate"
      "Interval": "120",
      "PackageVersion": "s3://mycompany/config/agent-package-version.json"
    },
    {
      "Type": "ConfigUpdate",
      "Interval": "30",
      "Source": "s3://mycompany/config/appsettings.json",
      "Destination": ".\appSettings.json"
    }
  ]
}
```
