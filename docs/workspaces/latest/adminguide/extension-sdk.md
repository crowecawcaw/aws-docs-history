

# SDK extension supported by DCV
<a name="extension-sdk"></a>

DCV enables high-performance remote access to WorkSpaces instances for a wide range of workloads and use cases. With the Amazon DCV Extension SDK, developers can customize DCV WorkSpaces experience for end users, including:
+ Facilitating custom hardware support.
+ Enhancing the usability of third-party applications in remote sessions. For example, adding local audio termination for VoIP applications or local video playback for conferencing applications
+ Providing accessibility software like screen readers with information about the remote session and applications running remotely.
+ Allowing security software to analyze the security posture of the local endpoint to allow conditional access policies.
+ Performing arbitrary data transfers over an established remote session.

To get started with Amazon DCV Extension SDK, see [Amazon DCV Extension SDK](https://docs.aws.amazon.com/dcv/latest/extsdkguide/what-is.html) documentation. You can find the SDK itself at [Amazon DCV Extension SDK GitHub repository](https://github.com/aws-samples/dcv-extension-sdk). In addition, you can also find integration examples of SDK at [Amazon DCV Extension SDK samples GitHub repository](https://github.com/aws-samples/dcv-extension-sdk-samples).

The following are supported by WorkSpaces.
+ Streaming protocol – DCV
+ WorkSpaces Windows client 5.9.0.4110 and above.
**Note**  
WorkSpaces Android, iOS clients, web access does not support DCV Extension SDK.
+ WorkSpaces macOS client 5.31.0 and above.
+ WorkSpaces Linux client 2025.1 and above.
+ WorkSpaces supported – Windows, Linux, and Ubuntu servers