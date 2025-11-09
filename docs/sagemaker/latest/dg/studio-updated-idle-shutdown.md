# Idle shutdown

Amazon SageMaker AI supports shutting down idle resources to manage costs and prevent cost overruns due
to cost accrued by idle, billable resources. It accomplishes this by detecting an app’s idle
state and performing an app shutdown when idle criteria are met.

SageMaker AI supports idle shutdown for the following applications. Idle shutdown must be set for
each application type independently.

- JupyterLab
- Code Editor, based on Code-OSS, Visual Studio Code - Open Source
  Idle shutdown can be set at either the domain or user profile level. When idle shutdown is
  set at the domain level, the idle shutdown settings apply to all applications created in the
  domain. When set at the user profile level, the idle shutdown settings apply only to the
  specific users that they are set for. User profile settings override domain settings. 

###### Note

Idle shutdown requires the usage of the `SageMaker-distribution` (SMD) image with
v2.0 or newer. Domains using an older SMD version can’t use the feature. These users must use
an LCC to manage auto-shutdown instead.

## Definition of idle

Idle shutdown settings only apply when the application becomes idle with no jobs running.
SageMaker AI doesn’t start the idle shutdown timing until the instance becomes idle. The definition on
idle differs based on whether the application type is JupyterLab or Code Editor.

For JupyterLab applications, the instance is considered idle when the following conditions
are met:

- No active Jupyter kernel sessions
- No active Jupyter terminal sessions

For Code Editor applications, the instance is considered idle when the following conditions are met:

- No text file or notebook changes
- No files being viewed
- No interaction with the terminal
