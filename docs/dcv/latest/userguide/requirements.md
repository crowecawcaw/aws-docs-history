

# Requirements
<a name="requirements"></a>

To use Amazon DCV, ensure that the client computers meet the following minimum requirements. Bear in mind that your experience is dependent on the number of pixels that are streamed from the Amazon DCV server to the Amazon DCV client.


<table>
<thead>
  <tr><th></th><th>Windows client</th><th>Web browser client</th><th>Linux client</th><th>macOS client</th></tr>
</thead>
<tbody>
  <tr><td><b>Software</b></td><td>The Windows client is supported on 64-bit versions of the following operating systems:<ul><li>Windows 10</li><li>Windows 11</li></ul><br />The client requires the following additional software:<ul><li> .NET Framework 4.6.2 </li><li> Microsoft Visual C++ Redistributable for Visual Studio. For more information and download instructions, see the <a href="https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads"> Microsoft Support</a> website. </li></ul></td><td>The web browser client is supported on the latest three major versions of the following browsers, across all major desktop operating systems (Windows, macOS, and Linux):<ul><li>Mozilla Firefox</li><li>Google Chrome</li><li>Microsoft Edge</li><li>Apple Safari</li></ul><br />The web browser client also requires WebGL and asm.js.The web browser client isn't supported on mobile operating systems, such as Android and iOS.</td><td>The Linux client is supported on the following modern Linux operating systems:<ul><li>RHEL 8.x and Rocky Linux 8.5 or later (x86_64)</li><li>RHEL 9, CentOS Stream 9, and Rocky Linux 9 (x86_64)</li><li>SUSE Linux Enterprise 15.x (x86_64)</li><li>Ubuntu 22.04 and 24.04 (x86_64 and ARM)</li></ul></td><td>macOS clients with Intel processors require macOS Monterey (12) or later.<br />macOS clients with Apple M1 processors require macOS Monterey (12).</td></tr>
  <tr><td><b>Network</b></td><td colspan="4">The client must connect to the Amazon DCV server, and it must communicate over the required port. By default, this is port 8443.</td></tr>
</tbody>
</table>


**Note**  
Amazon DCV does not support operating systems that have reached end of life. Contact your vendor regarding your operating system.

For more information about the Amazon DCV server requirements, see [ Amazon DCV server requirements](https://docs.aws.amazon.com/dcv/latest/adminguide/servers.html#requirements) in the *Amazon DCV Administrator Guide*.