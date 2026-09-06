

# Examples of using the AWS CLI with zonal autoshift
<a name="getting-started-cli-zonal-autoshift"></a>

This section walks through simple application examples of working with zonal autoshift, using the AWS Command Line Interface to work with the zonal autoshift capability in Amazon Application Recovery Controller (ARC) using API operations. The examples are intended to help you develop a basic understanding of how to work with zonal autoshift using the CLI.

Zonal autoshift is a capability in ARC. With zonal autoshift, you authorize AWS to shift away supported application resource traffic from an Availability Zone during events, on your behalf, to help reduce your time to recovery. For more information about resources that you can use with zonal autoshift, see [Supported resources](arc-zonal-shift.resource-types.md).

Zonal autoshift includes practice runs, which also shift traffic away from Availability Zones, to help verify that autoshifts are safe for your application.

For a list of zonal autoshift API actions and links to more information, see [Zonal autoshift API operations](actions.zonalautoshift.md). For more information about using the AWS CLI, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/arc-zonal-shift/index.html). 

**Topics**
+ [Create a practice run configuration](getting-started-cli-update-zonal_autoshift.create-practice-run.md)
+ [Enable or disable autoshifts](getting-started-cli-zonal-autoshift.update-autoshift.md)
+ [Start an on-demand practice run](getting-started-cli-zonal-autoshift.start-practice-run.md)
+ [Cancel an in-progress practice run](getting-started-cli-zonal-autoshift.cancel-practice-run.md)
+ [Cancel an in-progress autoshift](getting-started-cli-zonal-autoshift.cancel-autoshift.md)
+ [Edit a practice run configuration](getting-started-cli-zonal_autoshift.edit-practice-run-config.md)
+ [Delete a practice run configuration](getting-started-cli-zonal-autoshift.delete-practice-run-config.md)