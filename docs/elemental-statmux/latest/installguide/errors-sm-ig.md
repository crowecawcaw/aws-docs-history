This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Install Error Messages

During install, you might see the error message `Hardware and license
 validation failed` at the command line. The table below provides a list
of possible problems and causes that might result in this error.

| Possible Problem      | Possible Reason                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eth0 is not set up    | You didn't specify the address for eth0. Review the prompts in [Step C: Install the AWS Elemental Software](install-sm-ig-install-sw.md "install-sm-ig-install-sw.md").         |
| Products do not match | You might have requested and installed a license for one product (for example, AWS Elemental Statmux) and then installed a different product (for example, AWS Elemental Live). |
