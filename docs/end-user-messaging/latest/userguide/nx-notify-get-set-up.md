

# How to get set up
<a name="nx-notify-get-set-up"></a>

This topic takes you from a new AWS account to sending your first OTP or verification message with Notify. Notify spans two API namespaces, and which one you set up depends on who generates the passcode. Complete the prerequisites, then follow the step for the sending mode you want.


**Setup steps**  

| Step | What you do | 
| --- | --- | 
| [Prerequisites](nx-notify-get-set-up-prerequisites.md) | Set up your AWS account and IAM permissions, and choose which API namespace to use based on who generates the passcode. | 
| [Step 1: Create a notify code policy](nx-notify-get-set-up-policy.md) | If you want AWS End User Messaging to generate and validate the passcode, create a notify code configuration that defines your passcode policy. | 
| [Step 2: Create a Notify configuration](nx-notify-get-set-up-create.md) | Create a Notify configuration that represents your brand and messaging settings. Required for both sending modes. | 
| [Step 3: Request your own numbers (optional)](nx-notify-get-set-up-dedicated.md) | (Optional) Request your own phone numbers and add them to a pool to send from dedicated numbers. | 