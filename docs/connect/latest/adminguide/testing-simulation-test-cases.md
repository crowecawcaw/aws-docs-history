# Create test cases

## Create test case

The following procedure shows how to create a test case.

###### To create a test case

1. Open the Amazon Connect console at
   [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. In the main navigation pane, choose **Routing**, and then
   **Tests** to open the Test case management page to view list
   of existing test cases.

![Test case management page showing list of test cases with status, channel, and actions columns.](images/test-management-page.png) 3. Choose **Create Test**. 4. Once a test is saved or published, choose the **Details** tab to enter basic information about this test case including, name, description, and tags.

![Details tab showing Name, Description , and ARN fields, plus Tags section with Language and Env keys.](images/test-detail.png) 5. On the **Settings** tab, specify the channel for your test case. The following channels are supported:

    * **Voice call** – Configure the starting point by specifying the contact flow, incoming phone number, and any contact data to be initialized during test case execution.
    * **Chat** – Configure the starting point by specifying the contact flow and any contact data to be initialized during test case execution.

![Test settings page showing simulation configuration options including channel, starting point, flow selection, and JSON attributes editor.](images/test-settings.png) 6. Choose the **Design** tab to design your test. 7. Choose
**New interaction** to create a new interaction. This represents a simulated interaction with a contact center.

![Designer canvas with New interaction button highlighted in the toolbar.](images/GIF/test-create-interaction-gif.gif) 8. For each interaction group, specify an observe block to validate the
expected interaction from the system with a matching type (Contains and
Similarity match). Then, add check or actions blocks if necessary. For
more information, see
[Interaction groups](testing-simulation-concepts.md#testing-simulation-concepts-interaction-groups "testing-simulation-concepts.md#testing-simulation-concepts-interaction-groups").

![Interaction 1 designer showing an Observe block with a dropdown menu to add check or action blocks.](images/GIF/test-add-check-action-block-gif.gif)
