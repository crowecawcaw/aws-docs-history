# Configuring Spark compute

Amazon SageMaker Unified Studio provides a set of Jupyter magic commands. Magic commands, or magics, enhance
the functionality of the IPython environment. For more information about the magics that
Amazon SageMaker Unified Studio provides, run `%help` in a notebook.

Compute-specific configurations can be set by using the `%%configure` Jupyter
magic. The `%%configure` magic takes a JSON-formatted dictionary. To use
%%configure magic, specify the compute name in the argument `-n`. Including
`-f` will restart the session to forcefully apply the new configuration.
Otherwise, this configuration will apply when the next session starts.

For example: `%%configure -n `compute_name`
 -f`.
