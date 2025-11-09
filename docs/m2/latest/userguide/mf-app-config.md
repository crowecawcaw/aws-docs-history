AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Configure the Rocket Software (formerly Micro Focus) managed

application

You can configure your applications with Rocket Software runtime engine to customize additional
properties including integrations.

###### Topics

- [Supported third party integrations for
  Rocket Software](mf-app-config.md#mf-app-config-integations "mf-app-config.md#mf-app-config-integations")
  - [Printers](mf-app-config.md#mf-app-config-integations-printers "mf-app-config.md#mf-app-config-integations-printers")

## Supported third party integrations for

Rocket Software

To make use of third party integrations, your AWS Mainframe Modernization managed environment must use a Rocket Software
engine version that supports this type of configuration. Engine versions with the
postfix R (e.g., version 9.0.9.R) are supported. That means, engine version 9.0.9.R
includes client installation support for the party integrations, but 9.0.9
doesn't.

### Printers

Printer resources are configured through the Rocket Software application definition as
described in the [Printers - optional](applications-m2-definition.md#applications-m2-definition-mf-details-printers "applications-m2-definition.md#applications-m2-definition-mf-details-printers") section.

A printer definition may define a custom or service-provided exit module for the
printer. Some examples of possible exit module configurations are:

1. Example of loading service provided binary.

```
...
{
    "name": "p1",
    "classes": [
        "AB"
    ],
    "description": "Using service managed LRS Queue exit module",
    "exit-module": {
        "name": "lrsprte6"
    }
},
...
```

2. Example of providing binary from S3.

```
"exit-module": {
        "name": "s3Exit",
        "module": "${s3-source}/3pa/s3Exit.so"
}
```

3. Example of providing binary from EFS.

###### Note

To use EFS mount, it must be attached during the creation of the environment,
along with some additional values to be set such as
`program-path`.

```
...
"batch-settings": {
    "jes-printers": [
        {
            "name": "p3",
            "classes": [
                "EF"
            ],
            "description": "Using binary from customer provided exit module on EFS Mount",
            "exit-module": {
                "name": "efsExit"
            }
        }
    ],
    "program-path": "$EFS_MOUNT/path/to/directory/containing/binaries/"
},
"runtime-settings": {
    "environment-variables": {
        "EFS_MOUNT": "/m2/mount/efs"
    }
}
...
```

**LRS queue - optional**

To use LRS queue, you must be using a Rocket Software engine that supports third party
artifacts (i.e. engines ending with `.R`). In addition to setting up a
printer with an exit module pointing to `lrsprte6` as the exit module’s
entry name, LRS queue requires an additional environment variable, as defined in the
pre-existing “runtime-settings” block of the Rocket Software application definition.

**LRSQ_ADDRESS**

(Required) Specifies the LRS server address for the LRSQ print
exit module to send to.

**LRS printers** - Configuring an LRS Printer
requires the definition of a jes printer as specified in the [Printers - optional](applications-m2-definition.md#applications-m2-definition-mf-details-printers "applications-m2-definition.md#applications-m2-definition-mf-details-printers") section.

Additionally, the LRSQ_ADDRESS must be specified as part of the
`runtime-settings` field in the application definition.

```
"runtime-settings": {
    "environment-variables": {
        "LRSQ_ADDRESS": "<lrsq-address>"
    }
}
```
