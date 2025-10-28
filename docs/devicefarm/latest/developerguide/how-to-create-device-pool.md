# Creating a device pool in AWS Device Farm

You can use the Device Farm console, AWS CLI, or API to create a device pool.

###### Topics

- [Prerequisites](#how-to-create-device-pool-prerequisites "#how-to-create-device-pool-prerequisites")
- [Create a device pool (console)](#how-to-create-device-pool-console "#how-to-create-device-pool-console")
- [Create a device pool (AWS CLI)](#how-to-create-device-pool-cli "#how-to-create-device-pool-cli")
- [Create a device pool (API)](#how-to-create-device-pool-api "#how-to-create-device-pool-api")

## Prerequisites

- Create a run in the Device Farm console. Follow the instructions in [Creating a test run in Device Farm](how-to-create-test-run.md "how-to-create-test-run.md"). When you get to the
  **Select devices** page, continue with the instructions in this section.

## Create a device pool (console)

1. On the **Projects** page, choose your project. In the
   **Project details** page, choose **Project settings**. In the **Device
   pools** tab, choose **Create device pool**.
2. For **Name**, enter a name that makes this device pool easy to identify.
3. For **Description**, enter a description that makes this device pool easy to
   identify.
4. If you want to use one or more selection criteria for the devices in this device pool, do the
   following:
   1. Choose **Create dynamic device pool**.
   2. Choose **Add a rule**.
   3. For **Field**
      (first
      drop-down list), choose one of the following:
      - To include devices by their manufacturer name, choose **Device
        Manufacturer**.
      - To include devices by their form factor (tablet or phone),
        choose **Form Factor**.
      - To include devices by their availability status based on load,
        choose **Availability**.
      - To include only public or private devices, choose
        **Fleet Type**.
      - To include devices by their operating system, choose
        **Platform**.
      - Some devices have an additional label tag or description about
        the device. You can find devices based on their label contents
        by choosing **Instance
        labels**.
      - To include devices by their operating system version, choose
        **OS Version**.
      - To include devices by their model, choose
        **Model**.

   4. For **Operator** (second drop-down list), choose a
      logical operation (EQUALS, CONTAINS, etc.) to include devices based on
      the query. For example, you could choose `Availability
EQUALS AVAILABLE` to include devices that currently
      have the `Available` status.
   5. For **Value** (third drop-down list), enter or choose
      the value you want to specify for the **Field** and
      **Operator** values. Values are limited based on
      your **Field** choice. For example, if you
      choose **Platform** for **Field**, the
      only available selections are **ANDROID** and
      **IOS**. Similarly, if you choose **Form
      Factor** for **Field**, the only available
      selections are **PHONE** and
      **TABLET**.
   6. To add another rule, choose **Add a rule**.

   After you create the first rule, in the list of devices, the box next
   to each device that matches the rule is selected. After you create or
   change rules, in the list of devices, the box next to each device that
   matches those combined rules is selected. Devices with selected boxes
   are included in the device pool. Devices with cleared boxes are
   excluded. 7. Under **Max devices**, enter the number
   of devices you want to use in your device pool. If you do not enter the
   max number of devices, Device Farm will pick all devices in the fleet that
   match the rule(s) you created. To avoid additional charges, set this
   number to an amount that matches your actual parallel execution and
   device variety requirements. 8. To delete a rule, choose **Remove rule**.

5. If you want to manually include or exclude individual devices, do the following:
   1. Choose **Create static device pool**.
   2. Select or clear the box next to each device. You can select or clear the boxes only if you
      do not have any rules specified.

6. If you want to include or exclude all displayed devices, select or clear the
   box in the column header row of the list. If you want to view private device
   instances only, choose **See private device instances
   only**.

###### Important

Although you can use the boxes in the column header row to change the list of displayed
devices, this does not mean that the remaining displayed devices are the only ones included or
excluded. To confirm which devices are included or excluded, be sure to clear the contents of
all of the boxes in the column header row, and then browse the boxes. 7. Choose **Create**.

## Create a device pool (AWS CLI)

###### Tip

If you do not enter the max number of devices, Device Farm will pick all devices in the
fleet that match the rule(s) you created. To avoid additional charges, set this
number to an amount that matches your actual parallel execution and device variety
requirements.

- Run the [**create-device-pool**](../../../cli/latest/reference/devicefarm/create-device-pool.md "../../../cli/latest/reference/devicefarm/create-device-pool.md") command.

For information about using Device Farm with the AWS CLI, see [AWS CLI reference](cli-ref.md "cli-ref.md").

## Create a device pool (API)

###### Tip

If you do not enter the max number of devices, Device Farm will pick all devices in the
fleet that match the rule(s) you created. To avoid additional charges, set this
number to an amount that matches your actual parallel execution and device variety
requirements.

- Call the [`CreateDevicePool`](../APIReference/API_CreateDevicePool.md "../APIReference/API_CreateDevicePool.md") API.

For information about using the Device Farm API, see [Automating Device Farm](api-ref.md "api-ref.md").
