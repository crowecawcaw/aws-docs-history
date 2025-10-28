# Set up US emergency calling in

Amazon Connect

By default 911 is enabled for all users in the following North America Regions: US
East (N. Virginia), US West (Oregon), and AWS GovCloud (US-West). If a user calls 911,
the call is routed through to emergency services.

Amazon Connect only supports direct calls from the agent CCP to 911. It does not support call
transfers to 911, or dialing 911 while on a call.

**What is Enhanced 911 (E911)?** For agents who are
physically located in the US, E911 enables location information to be sent to 911
dispatch when a 911 call is placed.

There are two steps to set up E911:

- [Get and store an agent's
  validated physical address in your Amazon Connect instance](get-and-store-agent-address-e911.md "get-and-store-agent-address-e911.md")
- [Retrieve an agent's address from Amazon Connect
  when they call 911](retrieve-agent-address-e911.md "retrieve-agent-address-e911.md")

## Place 911 calls from your Test

Environment

###### Important

Calling 911 for a non-emergency situation carries a penalty of $100 per
occurrence. To help you avoid penalties, we have set up 933 so you can test this
capability. Calls placed from an Amazon Connect Contact Control Panel (CCP) to 933 have
an audio playback message confirming:

- The number the call originated from.
- The physical address that was sent along with the call.

For more information about calling 911, see this [FAQ](https://www.911.gov/calling-911/frequently-asked-questions/ "https://www.911.gov/calling-911/frequently-asked-questions/")
about the national 911 program.
