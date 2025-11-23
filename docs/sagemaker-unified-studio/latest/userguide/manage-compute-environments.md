# Manage compute environments

## Overview

Each notebook runs on a managed compute environment that provides the processing power for code execution. You can start, stop, and configure compute environments based on your workload requirements.

Compute environments support different instance types and sizes. You can also configure automatic shutdown to manage costs when the notebook is idle.

## Procedure

To start a compute environment:

1. Open your notebook if the compute environment is not already running.
2. The compute environment starts automatically when you execute your first cell.
3. Monitor the status in the kernel footer at the bottom right of the notebook.

To stop a compute environment:

1. Click the kernel status indicator in the notebook footer.
2. Select Stop to shut down the compute environment.
3. Your notebook content is preserved, but variables and session state are lost.

To change the instance type and storage:

1. Stop the current compute environment if it's running.
2. Click the kernel status indicator and select Configure.
3. Choose a different instance type and storage from the available options.
4. Start the compute environment with the new configuration.

To manage packages on kernel:

1. Open your notebook
2. Go to Packages on the left navigation
3. Add a new package or delete existing packages as required

To configure idle shutdown:

1. Access the idle shutdown setting through the left navigation.
2. Set the idle timeout period for automatic shutdown. The default shutdown is 1 hour.
3. The environment will automatically stop after the specified idle time.

To view Spark UI and Driver Logs:

1. Open your notebook
2. Navigate to the kernel footer at the bottom of the notebook, you can click on Spark UI and Driver Logs to open in a separate tab.
