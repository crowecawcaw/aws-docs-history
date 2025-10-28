Defect Detection App is in preview release and is subject to change.

# Creating the station for your edge device

A [station](dda-components.md#dda-component-station "dda-components.md#dda-component-station") manages the [workflows](dda-components.md#dda-component-workflow "dda-components.md#dda-component-workflow"), and [models](dda-components.md#dda-component-model "dda-components.md#dda-component-model") on your [edge device](dda-components.md#dda-component-edge-device "dda-components.md#dda-component-edge-device"). In this step you create and
activate a station on your edge device.

When you create a station, you specify the following:

- The number of [workflows](dda-components.md#dda-component-workflow "dda-components.md#dda-component-workflow") that you want your station to
  have.
- The target hardware configuration for the edge device that the station is deployed to.
  You can choose an ARM64 or an x86_64 CPU configuration, with or without GPU accelerated workflows.
  - NVIDIA Jetson Xavier Series (LINUX | ARM64 | NVIDIA)
    — GPU accelerated workflows on an edge device with an ARM64 CPU architecture.
  - Generic Linux x86 NVIDIA GPU (LINUX | X86_64 |
    CPU) — CPU accelerated workflows on an edge device with a X86_64 CPU architecture.
  - Accelerated CPU Linux x86 (LINUX | X86_64) — Edge device wtih X84_64 CPU architecture.
  - Generic Linux ARM (LINUX | ARM64) — Edge device with ARM64 CPU architecture.
  - Generic Linux x86 (LINUX | X86_64) — Edge device wtih X84_64 CPU architecture.

- If your edge device uses a GPU, we provide the following compiler settings,
  with default settings for each type of GPU.

      + `gpu-code` — Specifies the gpu code of the
       core device that runs the model component.
      + `trt-ver` — Specifies the TensorRT version
       in x.y.z. format.
      + `cuda-ver` — Specifies the CUDA version in
       x.y format. The value must be `10.2`.

  For information about the GPUs that we haved tested with Defect Detection App, see
  [Graphic Processing Unit (GPU) for accelerated workflows](dda-set-up-device-station.md#dda-required-software-tested-gpu "dda-set-up-device-station.md#dda-required-software-tested-gpu").

###### Important

You are charged a monthly subscription fee for each active workflow.

During station creation, Defect Detection App generates a zip that contains configuration files and
install script (`installGreengrassCore.sh`). During station creation, you run
the install script on the device to activate and configure the station. Configuration does the
following:

- Installs drivers and dependencies (including the AWS IoT Greengrass Version 2 components needed
  to to deploy models to the device)
- Installs certificates used for authentication
- Starts components needed to deploy and run the model on the device
  Configuring the station takes 15 - 20 minutes, longer if you have a slow internet
  connection.

Information about the install script is in the file `README.md`.

The zip file also contains an uninstall file that you run on the device after deleting
the station. For more information, see [Delete a station](dda-delete-station.md "dda-delete-station.md").

To manage stations that you have created, see [Managing Defect Detection App](dda-managing-resources.md "dda-managing-resources.md").

###### To create a station for an edge device

1. Make sure that your edge device is online.
2. On the edge device, [sign in](dda-signin-dda-web-app.md "dda-signin-dda-web-app.md") to
   the Defect Detection App Console.
3. In the top navigation pane, choose **Stations**.
4. On the stations page, choose **Create station**.
5. On the Station details page, enter the following:
   - A name for the station
   - (optional) A description for the station
   - The number of workflows that you want on the station. You can change this value later.
   - The target hardware configuration for the edge device that the station is deployed to.
     You can choose an ARM64 or X86 configuration, with or without GPU accelerated workflows.
     - **NVIDIA Jetson Xavier Series (LINUX | ARM64 | NVIDIA)** — GPU accelerated workflows.
     - **Generic Linux x86 NVIDIA GPU (LINUX | X86_64 |
       NVIDIA)** — GPU accelerated workflows.
     - **Accelarated CPU Linux x86 (LINUX | X86_64 | CPU)**
     - **Generic Linux ARM (LINUX | ARM64)**
     - **Generic Linux x86 (LINUX | X86_64)**

   - (optional) If your edge device uses a GPU, you can change the
     `trt-ver`and `cuda-ver` compiler settings in
     **Advanced settings**. The value for `gpu-code`
     must be `10.2`.

   You specify the settings in JSON. For example:

   ```
   {
       "cudaVer": "10.2",   "gpuCode": "sm_72",   "trtVer": "8.2.1"
   }
   ```

6. Choose **Create and start activation**.
7. Follow the instructions to activate the station on the device. Remember to
   unzip and use the configuration files on the edge device that you want to active
   the station. If you are using the the Defect Detection App Console from a different location,
   you need to copy the configuration files to the edge device.
8. Wait until the station is active and then choose **Next**. If
   set up fails, check that the edge device is online and try again by choosing
   **try again**. After succesfully setting up the station,
   the Defect Detection App Console displays the **Stations** page.
9. Next step: [Adding an image source](dda-configure-image-source.md "dda-configure-image-source.md").
