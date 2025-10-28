# Configuring Amazon Kinesis Agent for Microsoft Windows

Before starting Amazon Kinesis Agent for Microsoft Windows, you must create a configuration file and deploy it. The
configuration file provides the necessary information to collect, transform, and stream data on
Windows servers and desktop computers to various AWS services. Configuration files define sets
of sources, sinks, and pipes that connect sources to sinks, along with optional transformations.

The Kinesis Agent for Windows configuration file is named `appsettings.json`. Deploy this
file to `%PROGRAMFILES%\Amazon\AWSKinesisTap`.

###### Topics

- [Basic Configuration Structure](basic-configuration-structure.md "basic-configuration-structure.md")
- [Source Declarations](source-object-declarations.md "source-object-declarations.md")
- [Sink Declarations](sink-object-declarations.md "sink-object-declarations.md")
- [Pipe Declarations](pipe-object-declarations.md "pipe-object-declarations.md")
- [Configuring Automatic Updates](update-configuration-options.md "update-configuration-options.md")
- [Kinesis Agent for Windows Configuration Examples](configuring-kaw-examples.md "configuring-kaw-examples.md")
- [Configuring Telemetrics](telemetrics-configuration-option.md "telemetrics-configuration-option.md")
