

# EC2 Windows troubleshooting utilities
<a name="windows-troubleshooting-utils"></a>

The `EC2WinUtil` driver provides the following types of troubleshooting support for your Windows instance.

**Crash call stacks**  
`EC2WinUtil` collects basic crash information from your instance and writes it out to the serial console. The following list includes some of the key details that the utility writes to the console.  
+ Identification of the module that generated the fault.
+ The Windows error code associated with the event.
+ A stack trace of the most recent calls.
With these details, you can perform initial root cause analysis and determine if further analysis is needed. Output to the serial console also enables AWS to track crash trends for Amazon EC2 drivers, and diagnose large scale crash events.  
`EC2WinUtil` doesn't collect any customer data in its crash call stacks.

For driver release notes, see [EC2 Windows Utility Driver version history](ec2winutil-driver-version-history.md)