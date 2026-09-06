

# Create test cases
<a name="testing-simulation-test-cases"></a>

## Create test case
<a name="testing-simulation-test-case-procedure"></a>

The following procedure shows how to create a test case. 

**To create a test case**

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. In the main navigation pane, choose **Routing**, and then **Tests** to open the Test case management page to view list of existing test cases.   
![Test case management page showing list of test cases with status, channel, and actions columns.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-management-page.png)

1. Choose **Create Test**.

1. Once a test is saved or published, choose the **Details** tab to enter basic information about this test case including, name, description, and tags.   
![Details tab showing Name, Description , and ARN fields, plus Tags section with Language and Env keys.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-detail.png)

1. On the **Settings** tab, specify the channel for your test case. The following channels are supported:
   + **Voice call** – Configure the starting point by specifying the contact flow, incoming phone number, and any contact data to be initialized during test case execution.
   + **Chat** – Configure the starting point by specifying the contact flow and any contact data to be initialized during test case execution.  
![Test settings page showing simulation configuration options including channel, starting point, flow selection.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-settings.png)

1. Choose the **Design** tab to design your test. 

1. Choose **New interaction** to create a new interaction. This represents a simulated interaction with a contact center.   
![Designer canvas with New interaction button toolbar.](http://docs.aws.amazon.com/connect/latest/adminguide/images/GIF/test-create-interaction-gif.gif)

1. For each interaction group, specify an observe block to validate the expected interaction from the system with a matching type (Contains and Similarity match). Then, add check or actions blocks if necessary. For more information, see [Interaction groups](testing-simulation-concepts.md#testing-simulation-concepts-interaction-groups).   
![Interaction 1 designer showing an Observe block with a dropdown menu to add check or action blocks.](http://docs.aws.amazon.com/connect/latest/adminguide/images/GIF/test-add-check-action-block-gif.gif)