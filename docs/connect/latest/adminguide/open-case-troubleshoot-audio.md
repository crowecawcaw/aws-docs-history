

# Open a case for call quality issues
<a name="open-case-troubleshoot-audio"></a>

If your contact center has call quality issues that persist even after performing the [recommended troubleshooting steps](sop-audio-qa.md), open a case for Support to help you investigate the issue. Provide the following information in your case.

**Important**  
Provide information for at least 3–5 examples of call quality issues. The examples must not be older than 24 hours. 

1. The ARN of your Connect Customer instance. For instructions on finding your instance ARN, see [Find your Connect Customer instance ID or ARN](find-instance-arn.md).

1. A description of the audio quality issue observed.

1. Contact IDs of the affected calls and a snapshot of the contact records that contains all the details. 

1. Call recording attachments, attached to the case.

1. Share the findings from the tests you have performed, and your observations:

   1. Confirm whether you have followed all the requirements specified for the [network](ccp-networking.md), [agent workstation](ccp-agent-hardware.md) and [browser](connect-supported-browsers.md). 

   1. Provide your observations from testing the following:

      1. Browsers. Specify which browsers you tested and the results.

      1. Networks. Specify the different networks you tested and the results.

      1. Ask the affected agent to sign in on a different machine to determine the behavior pattern. This helps isolate whether the issue is specific to one machine. 

   1. Confirm whether the agent's workstation meets the [minimum hardware requirements](ccp-agent-hardware.md).

   1. Provide details about the agent's environment: virtual private network (VPN), firewall, and virtual desktop infrastructure (VDI) configuration, along with a description.

   1. Specify the type of Contact Control Panel (CCP) your agent is using (is it customized with the Connect Customer Streams API or the default version). Share your observation from the default CCP along with the [downloaded CCP logs](download-ccp-logs.md) of the affected calls.

1. Specify the frequency of the issue. 

1. Provide an impact assessment and date and time when it started. Provide in UTC format.

1. Provide your observations after running Ping and MTR (My Traceroute).

1. Provide an export of your [Endpoint Test Utility](check-connectivity-tool.md) results. 