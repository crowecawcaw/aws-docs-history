# Jupyter Enterprise Gateway (JEG) configuration

options

Amazon EMR on EKS uses Jupyter Enterprise Gateway (JEG) to turn on interactive endpoints. You
can set the following values for the allow-listed JEG configurations when you create the endpoint.

- **`RemoteMappingKernelManager.cull_idle_timeout`** – Timeout
  in seconds (integer), after which a kernel is considered idle and ready to be culled.
  Values of `0` or lower deactivate culling. Short timeouts might result in kernels being
  culled for users with poor network connections.
- **`RemoteMappingKernelManager.cull_interval`** – The
  interval in seconds (integer) on which to check for idle kernels that exceed the cull
  timeout value.
