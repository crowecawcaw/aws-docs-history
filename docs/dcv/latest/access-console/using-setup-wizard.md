# Using the Setup Wizard

The Setup Wizard is a CLI designed to help you install the Amazon DCV Access Console, and configure the hosts you plan to install the components on.
The Setup Wizard can be used whether you install the Access Console components all on the same host, or on separate hosts. If you install the components
on a single host, it will install the components and dependencies for the Access Console for you. If you install the components on separate hosts, the Setup
Wizard will help you create the configuration files needed for each component. The Setup Wizard can optionally:

- Install MariaDB using the OS package manager to act as a datastore. If you choose to use Amazon DynamoDB, no additional packages need to be installed.
- Create the necessary database in your chosen datastore
- Install NGINX using the OS package manager
- Generate and saves a self-signed certificate
- Install the Amazon DCV Access Console components
- Configure the Authentication Server with PAM authentication
- Start the datastore, NGNIX and the Amazon DCV Access Console components
- Create a user with the Admin role
- Validate that each component started correctly

###### Note

Through the Setup Wizard you may install certain third-party software that you can use in conjunction with the Amazon DCV Access Console. You are
solely responsible for complying with any applicable terms and conditions for use of such third-party software, including obtaining any required licenses
from the relevant third parties to use their technology and paying any necessary royalties or fees.

## Running the wizard

The Setup Wizard in the Amazon DCV Access Console packaged components, available on [Amazon DCV Downloads](http://download.amazondcv.com "http://download.amazondcv.com").

You can use the Setup Wizard in interactive or non-interactive mode to complete the setup of the Amazon DCV Access Console. The Setup Wizard will finish by
validating the installation was successful then print the public DNS of the host you provided. The Amazon DCV Access Console will be accessible at that address
and any user present on that host will be able to login.

###### Interactive mode

By default, the Setup Wizard runs in interactive mode. This mode prompts you to complete the required inputs. Run the Setup Wizard (see Run the Setup Wizard
documentation for more details), and answer each prompt with the necessary requirements to setup the Amazon DCV Access Console.

###### Non-interactive mode

You can also choose to run the Setup Wizard in non-interactive mode. Using this mode, you manually fill in either the `onebox_wizard_input.json` or `wizard_input.json` file that
comes with it or by using command-line options. The instructions for non-interactive mode are different, whether you install the Amazon DCV Access Console components
on one host, or separate hosts.

## Modifying setup wizard parameters

When in non-interactive mode, the Setup Wizard supports several ways of inputting parameter values.

### Loading a JSON file

You can specify the input parameters by loading a JSON file to the Setup Wizard, where the key-value pairs are the name of the parameter and specified value. Two starter files
are provided with the Setup Wizard: `wizard_input.json` for setting up on multiple hosts and `onebox_wizard_input.json` for setting up on a single host.

For example, this file specifies the `broker-client-id` and the `broker-client-password`:

```
{
    "broker-client-id": "`client_id`"
    "broker-client-password": "`client_password`"
}
```

Then load the file into the Setup Wizard by specifying its path (absolute or relative) with the `--input-json` option. The Setup Wizard will prompt for any
parameter not specified in the JSON file, unless the `--quiet` flag is used.

For a full list of the available options and flags, navigate to the folder where you extracted the Amazon DCV Access Console components:

```
`$` python3 wizard.py --help
```

### Command-line options

You can also specify the input parameters by using command-line options, for example `--broker-address`.

For a full list of the available options and flags, navigate to the folder where you extracted the Amazon DCV Access Console components and invoke:

```
`$` python3 wizard.py --help
```
