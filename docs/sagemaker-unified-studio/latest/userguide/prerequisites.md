# Prerequisites

Before connecting VS Code, Kiro, or Cursor remotely to a SageMaker Unified Studio
Space, ensure that you have the following prerequisites:

- Access to an existing domain in Amazon SageMaker Unified Studio.
- A supported IDE and AWS Toolkit version, as listed in the following
  table.

| IDE     | Minimum version | Minimum AWS Toolkit version |
| ------- | --------------- | --------------------------- |
| VS Code | 1.90 or later   | 3.97 or later               |
| Kiro    | 0.8.0 or later  | 3.97 or later               |
| Cursor  | 2.6.18 or later | 3.100 or later              |

- The AWS Toolkit extension installed from the Extensions marketplace in your
  IDE.
- One of the following supported operating systems:
  - macOS 13 or later
  - Windows 10 or Windows 11
  - Linux (requires the official Microsoft VS Code distribution for VS
    Code and Cursor)

- A Space instance that meets the following requirements:
  - Memory: Minimum 8 GB RAM. We recommend instances with 8 GB or more
    memory for optimal performance.
  - Unsupported instance types: `ml.t3.medium`,
    `ml.c7i.large`, `ml.c6i.large`,
    `ml.c6id.large`, `ml.c5.large`

- A compatible image:
  - SageMaker Distribution: Version 2.8 or later
  - Custom images: Must follow SageMaker custom image
    specifications

- Extension compatibility: Not all VS Code extensions support remote
  development.

###### Important

Remote Space connections are not supported for TIP (Trusted Identity Propagation)
enabled projects. For instructions on how to set the
`enableTrustedIdentityPropagationPermissions` parameter to false to
use remote connection for Spaces, see [Trusted identity propagation](../adminguide/trusted-identity-propagation.md "../adminguide/trusted-identity-propagation.md").
