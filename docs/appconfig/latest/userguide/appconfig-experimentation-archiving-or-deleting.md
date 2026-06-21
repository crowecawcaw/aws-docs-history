# Cleaning up an experiment

After an experiment completes, you can archive or permanently delete the experiment definition.

- **Archive** – The experiment definition is hidden from the active list but can be restored later. The experiment feature flag remains deployed and continues serving its current configuration. To stop serving the flag, disable it separately in your feature flag configuration.
- **Delete permanently** – The experiment definition and all associated run history are permanently deleted. This action cannot be undone.

###### To archive or delete an experiment

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/ "https://console.aws.amazon.com/systems-manager/appconfig/").
2. In the navigation pane, choose **Experiments**, and then choose an experiment. The experiment dashboard opens.
3. Choose **Actions**, and then choose **Delete experiment definition**.
4. In the **Choose an action** section, choose either **Archive** or **Delete permanently**.
5. In the **Confirmation** section, type `confirm`.
6. Choose the **Archive** or **Delete** button.
