

# How to Drain an Instance
<a name="how-to-drain"></a>

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the left pane, choose **Fleets**.

1. Select a multi-session fleet and choose **View Details** and **View Sessions**.

1. Select a session running on the instance you want to drain.

1. Choose **Drain Session Instance**.

The instance will immediately stop accepting new sessions. Existing sessions will continue uninterrupted. Once the last session ends, the instance is automatically terminated and replaced.