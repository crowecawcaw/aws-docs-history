

# Send instruction actions
<a name="testing-simulation-action-send-instruction"></a>

Send Instruction actions to simulate customer inputs during your test, allowing you to mimic how a real customer would interact with your contact center experience.

## DTMF input (keypad presses)
<a name="testing-simulation-action-dtmf"></a>

Simulates a customer pressing keys on their phone keypad. This is commonly used for IVR menu navigation where customers select options by pressing numbers.

Configuration options:
+ **Action** – Select "Send Instruction" from the dropdown
+ **Input type** – Choose "DTMF Input"
+ **Parameter** – Enter the key(s) to press (numbers 0-9, \*, or \#)

Use cases:
+ Navigating through menu options ("Press 1 for Sales, Press 2 for Support")
+ Entering account numbers or reference codes
+ Confirming selections with \# or \*

![Action block configuration showing Send Instruction with DTMF Input type selected.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-dtmf-input.png)


## Text and voice input
<a name="testing-simulation-action-text-voice"></a>

Simulates customer speaking or typing text responses. This is essential for testing conversational AI, chatbots, and voice-enabled flows.

Configuration options:
+ **Action** – Select "Send Instruction" from the dropdown
+ **Input type** – Choose "Text/Utterance input"
+ **Parameter** – Provide the customer's response using plain text that the customer would say or type

Use cases:
+ Responding to bot questions ("I need help with my order")
+ Providing information requested by the system ("My account number is 12345")

![Action block configuration showing Send Instruction with Text/Utterance input type selected.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-text-voice-input.png)


## Disconnect
<a name="testing-simulation-action-disconnect"></a>

Simulates a customer ending the call. This is useful for testing how your flow handles customer-initiated disconnections at various points.

Configuration options:
+ **Action** – Select "Send Instruction" from the dropdown
+ **Input type** – Choose "Disconnect"

Use cases:
+ Testing disconnect processes when customers hang up
+ Ensuring no errors occur during unexpected disconnections

![Action block configuration showing Send Instruction with Disconnect input type selected.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-disconnect.png)
