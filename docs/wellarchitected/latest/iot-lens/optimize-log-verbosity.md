# Optimize log verbosity

Use debug levels to increase/decrease metric and log verbosity
based on the context. In normal operation, send the minimum set
of metrics and logs required to identify system health. If
runtime issues require additional verbosity, a more detailed log
level could be set either dynamically by the device software, or
by sending a new configuration to the devices that require it.
