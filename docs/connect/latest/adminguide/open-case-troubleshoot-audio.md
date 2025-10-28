# Open a case for call quality

issues

If your contact center has call quality issues that persist even after performing the
[recommended troubleshooting steps](sop-audio-qa.md "sop-audio-qa.md"), open a case
for Support to help you investigate the issue. Provide the following information in your
case.

###### Important

Provide information for at least 3-5 examples of call quality issues. The examples
must not be older than 24 hours.

1. The ARN of your Amazon Connect instance. For instructions, see [Find your Amazon Connect instance ID or ARN](find-instance-arn.md "find-instance-arn.md").
2. A description of the audio quality issue observed.
3. Contact IDs of the affected calls and a snapshot of the contact records that
   contains all the details.
4. Call recording attachments, attached to the case.
5. Share the findings from the tests you have performed, and your
   observations:
   1. Confirm whether you have followed all the requirements specified for
      the [network](ccp-networking.md "ccp-networking.md"), [agent workstation](ccp-agent-hardware.md "ccp-agent-hardware.md") and [browser](connect-supported-browsers.md "connect-supported-browsers.md").
   2. Provide your observations from testing the following:
      1. Browsers. Specify which browsers you tested and the
         results.
      2. Networks. Specify the different browsers you tested and the
         results.
      3. Ask the affected agent to login through a different machine to
         determine the behavior pattern. This will help isolate whether
         the issue pertains to a specific system.

   3. Confirm whether the agent's workstation meets the [minimum hardware
      requirements](ccp-agent-hardware.md "ccp-agent-hardware.md").
   4. Provide details about the agent's environment: VPN/Firewall/VDI
      configuration, along with a description.
   5. Specify the type of CCP your agent is using (is it customized with
      StreamsJs or the default version). Share your observation from the
      default CCP along with the [downloaded
      CCP logs](download-ccp-logs.md "download-ccp-logs.md") of the affected calls.

6. Specify the frequency of the issue.
7. Provide an impact assessment and date/time when it started. Provide in UTC
   format.
8. Provide your observations after running Ping and MTR.
9. Provide an export of your [Endpoint
   Test Utility](check-connectivity-tool.md "check-connectivity-tool.md") results.
