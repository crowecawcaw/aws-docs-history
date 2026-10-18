

# macOS connection diagnostics
<a name="troubleshooting-macos-diagnostics"></a>

If you encounter a connection error on the macOS client, choose **Diagnose…** on the error screen to run automated connectivity checks.

![Connection error screen showing the Diagnose button.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-diagnostics-button.png)


The diagnostics run sequential steps, stopping at the first failure:


| Step | What it checks | 
| --- | --- | 
| Network | Local network interface availability (Wi-Fi, Ethernet, Cellular) | 
| Internet | Outbound connectivity | 
| DNS | General DNS resolution | 
| System Proxy | System proxy reachability (skipped if not using system proxy) | 
| Host Resolution | DNS resolution of the target hostname (skipped for IP addresses) | 
| TCP Port | TCP connection to the server's WebSocket port | 
| TLS Certificate | Verifying the server's security certificate | 
| UDP Port | Testing the UDP connection (skipped if using WebSocket only) | 
| DCV Authentication | Verifying your credentials | 
| DCV Connection | Establishing the session | 
| DCV Streaming | Starting the remote desktop stream | 

Each step shows whether it passed or failed, a description, and how long it took.

![Diagnostics results showing sequential connectivity checks with pass/fail status and timing.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-diagnostics-results.png)


Choose **Generate Report…** when diagnostics complete. The report is saved as a JSON file in the logs directory (`~/Library/Logs/com.nicesoftware.dcvviewer/`) and opened automatically. It includes system info, connection details, and all check results with timing.