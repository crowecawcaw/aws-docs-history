# Troubleshoot Errors

This section contains information about how to understand and prevent common
errors, the error messages they generate, and guidance on how to resolve these
errors. Before moving on, ask yourself the following questions:

**Did you encounter an error before you deployed your model?** If yes,
see [Troubleshoot
Neo Compilation Errors](neo-troubleshooting-compilation.md "neo-troubleshooting-compilation.md").

**Did you encounter an error after you compiled your model?** If yes, see
[Troubleshoot
Neo Inference Errors](neo-troubleshooting-inference.md "neo-troubleshooting-inference.md").

**Did you encounter an error trying to compile your model for Ambarella devices?** If yes, see
[Troubleshoot
Ambarella Errors](neo-troubleshooting-target-devices-ambarella.md "neo-troubleshooting-target-devices-ambarella.md").

## Error Classification Types

This list classifies the _user errors_ you can receive from
Neo. These include access and permission errors and load errors for each of the
supported frameworks. All other errors are _system
errors_.

Neo passes the errors for these straight through from the dependent service.

- _Access Denied_ when calling sts:AssumeRole
- _Any 400_ error when calling Amazon S3 to download or upload
  a client model
- _PassRole_ error
  Assuming that the Neo compiler successfully loaded .tar.gz from Amazon S3,
  check whether the tarball contains the necessary files for compilation.
  The checking criteria is framework-specific:

- **TensorFlow**: Expects only
  protobuf file (\*.pb or \*.pbtxt). For saved models, expects one
  variables folder.
- **Pytorch**: Expect only one
  pytorch file (\*.pth).
- **MXNET**: Expect only one symbol
  file (\*.json) and one parameter file (\*.params).
- **XGBoost**: Expect only one
  XGBoost model file (\*.model). The input model has size
  limitation.
  Assuming that the Neo compiler successfully loaded .tar.gz from Amazon S3,
  and that the tarball contains necessary files for compilation. The checking criteria is:

- **OperatorNotImplemented**: An
  operator has not been implemented.
- **OperatorAttributeNotImplemented**: The attribute in
  the specified operator has not been implemented.
- **OperatorAttributeRequired**: An
  attribute is required for an internal symbol graph, but it is not
  listed in the user input model graph.
- **OperatorAttributeValueNotValid**: The value of the
  attribute in the specific operator is not valid.

###### Topics

- [Troubleshoot Neo Compilation Errors](neo-troubleshooting-compilation.md "neo-troubleshooting-compilation.md")
- [Troubleshoot Neo Inference Errors](neo-troubleshooting-inference.md "neo-troubleshooting-inference.md")
- [Troubleshoot
  Ambarella Errors](neo-troubleshooting-target-devices-ambarella.md "neo-troubleshooting-target-devices-ambarella.md")
