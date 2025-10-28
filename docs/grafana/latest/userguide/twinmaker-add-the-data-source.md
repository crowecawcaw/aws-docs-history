# Manually adding the AWS IoT TwinMaker data

source

## Prerequisites

Before you begin, ensure that you have access to **AWS IoT TwinMaker**
from your AWS account.

To learn how to add permission to your workspace IAM role to access AWS IoT TwinMaker,
see [Adding the permission for AWS IoT TwinMaker to your
workspace user role](AMG-iot-twinmaker.md#twinmaker-add-permission "AMG-iot-twinmaker.md#twinmaker-add-permission").

###### To add the AWS IoT TwinMaker data source:

1. Ensure that your user role is admin or editor.
2. In the Grafana console side menu, hover over the **Configuration** (gear) icon and then choose **Data Sources**.
3. Choose **Add data source**.
4. Choose the **AWS IoT TwinMaker** data source. If necessary, you can
   start typing `TwinMaker` in the search box to help you find
   it.
5. This opens the **Connection Details** page. Follow the steps
   in configuring the [AWS IoT TwinMaker connection details
   settings](AMG-iot-twinmaker.md#twinmaker-connection-details "AMG-iot-twinmaker.md#twinmaker-connection-details").
