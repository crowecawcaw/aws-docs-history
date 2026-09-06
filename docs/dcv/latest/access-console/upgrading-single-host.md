

# Upgrading Amazon DCV Access Console on a single host
<a name="upgrading-single-host"></a>

The Wizard will update the components for the Access Console, reload and restart all of the Access Console components. The components can be downloaded using steps in [Preparing the components and the Setup Wizard](https://docs.aws.amazon.com/dcv/latest/access-console/prepare-environment.html).

## Running the Setup Wizard in interactive mode
<a name="upgrading-single-interactive"></a>

Interactive mode is the default update mode for the Amazon DCV Access Console. It will guide you through the update process.

1. Navigate to the folder where you extracted the latest Amazon DCV Access Console components.

1. Run the following command:

   ```
   $  python3 wizard.py update
   ```

1. Provide the path to the folder where the installers for the three components can be found. By default, it looks in the current directory.

The Wizard will first validate the processes are running, update them, reload and restart the Amazon DCV Access Console components.

## Running the Setup Wizard in non-interactive mode
<a name="upgrading-single-noninteractive"></a>

Non-interactive mode of the update wizard will allow for it be used in scripts.

1. Navigate to the folder where you extracted the latest Amazon DCV Access Console components.

1. Run the following command:

   ```
   $  python3 wizard.py update --component-installers-location
   ```

The Wizard will first validate the processes are running, update them, reload and restart the Amazon DCV Access Console components.