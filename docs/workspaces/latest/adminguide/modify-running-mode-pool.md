

# Modify the running mode
<a name="modify-running-mode-pool"></a>

You can switch between running modes when a WorkSpaces Pool is in stopped state.

**To modify the running mode of a WorkSpaces Pool**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces** and **Pools**.

1. Select the WorkSpaces Pool to modify and cofirm it’s in stopped state. Then, choose **Actions** and **Modify running mode**.

1. Select the new running mode, **AlwaysOn** or **AutoStop**, and then choose **Save**.

**To modify the running mode of a WorkSpaces Pool using the AWS CLI**
+ Use the [update-workspaces-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/update-workspaces-pool.html) command.