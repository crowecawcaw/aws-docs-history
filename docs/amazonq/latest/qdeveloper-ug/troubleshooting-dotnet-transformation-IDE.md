# Troubleshooting issues with

.NET transformations in the IDE

Use the following sections to troubleshoot common issues with .NET transformations in
the IDE with Amazon Q Developer.

## How do I know if a job is progressing?

If Amazon Q appears to be spending a long time on a step in the
Transformation
Hub, you can check whether the job is still active in the output
logs. If diagnostic messages are being generated, the job is still active.

To check the outputs, choose the **Output** tab in Visual Studio. In the
**Show output from:** menu, choose **Amazon Q Language
Client**.

The following screenshot shows an example of the outputs Amazon Q generates during a transformation.

![Screenshot of the Amazon Q Developer Code Transformation Hub, showing the output from the Amazon Q Language Client.](images/code-transform-troubleshoot4.png)

## Why are some projects not selected for transformation?

Amazon Q can only transform supported project types in the C# language. Currently,
Amazon Q does not support porting UI layer components or projects written in the
VB.NET or F# languages. For a list of supported project types and other
prerequisites for transforming your .NET projects, see
[Step 1: Prerequisites](port-dotnet-application.md#transform-dotnet-prerequisites "port-dotnet-application.md#transform-dotnet-prerequisites").

## How can I get support if my project or solution isn’t transforming?

If you aren’t able to troubleshoot issues on your own, you can reach out to Support
or your AWS account team to submit a support case.

To get support, provide the transformation job ID so AWS can investigate a
failed job. To find a transformation job ID, choose the **Output**
tab in Visual Studio. In the **Show output from:** menu, choose
**Amazon Q Language Client**.

## How can I prevent my firewall from

interfering with transformation jobs?

If your organization uses a firewall, it might interfere with transformations in
Visual Studio. You can temporarily disable security checks in Node.js to troubleshoot or test
what is preventing the transformation from running.

The environment variable `NODE_TLS_REJECT_UNAUTHORIZED` controls important security
checks. Setting `NODE_TLS_REJECT_UNAUTHORIZED` to "0" disables Node.js's rejection of
unauthorized TLS/SSL certificates. This means:

- Self-signed certificates will be accepted
- Expired certificates will be allowed
- Certificates with mismatched hostnames will be permitted
- Any other certificate validation errors will be ignored

If your proxy uses a self-certificate, you can set the following environment variables instead of disabling
`NODE_TLS_REJECT_UNAUTHORIZED`:

```
NODE_OPTIONS = —use-openssl-ca
NODE_EXTRA_CA_CERTS = Path/To/Corporate/Certs
```

Otherwise, you must specify the CA certs used by the proxy to disable
`NODE_TLS_REJECT_UNAUTHORIZED`.

######

To disable NODE_TLS_REJECT_UNAUTHORIZED on Windows:

1. Open the Start menu and search for **Environment Variables**.
2. Choose **Edit the system environment variables**.
3. In the **System Properties** window, choose **Environment Variables**.
4. Under **System variables**, choose **New**.
5. Set **Variable name** to NODE_TLS_REJECT_UNAUTHORIZED and **Variable value** to 0.
6. Choose **OK** to save the changes.
7. Restart Visual Studio.
