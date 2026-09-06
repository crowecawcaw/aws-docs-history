

# Set up OPC UA servers to trust the AWS IoT SiteWise Edge gateway
<a name="enable-source-trust"></a>

If you choose a `messageSecurityMode` other than **None** when configuring your OPC UA source, you must enable your source servers to trust the AWS IoT SiteWise Edge gateway. The SiteWise Edge gateway generates a certificate that your source server might require. The process varies depending on your source servers. For more information, see the documentation for your servers.

The following procedure outlines the basic steps.

**To enable an OPC UA server to trust the SiteWise Edge gateway**

1. Open the interface for configuring your OPC UA server.

1. Enter the user name and password for the OPC UA server administrator.

1. Locate **Trusted Clients** in the interface, and then choose **AWS IoT SiteWise Gateway Client**.

1. Choose **Trust**.

## Exporting the OPC UA client certificate
<a name="export-opc-ua-client-certificate"></a>

Some OPC UA servers require access to the OPC UA client certificate file to trust the SiteWise Edge gateway. If this applies to your OPC UA servers, you can use the following procedure to export the OPC UA client certificate from the SiteWise Edge gateway. Then, you can import the certificate on your OPC UA server.

**To export the OPC UA client certificate file for a source**

1. Run the following command to change to the directory that contains the certificate file. Replace {{sitewise-work}} with the local storage path for the {{aws.iot.SiteWiseEdgeCollectorOpcua}} Greengrass work folder and replace {{source-name}} with the name of the data source. 

   By default, the Greengrass work folder is {{/greengrass/v2/work/aws.iot.SiteWiseEdgeCollectorOpcua}} on Linux and {{C:/greengrass/v2/work/aws.iot.SiteWiseEdgeCollectorOpcua}} on Microsoft Windows. 

   ```
   cd /{{sitewise-work}}/{{source-name}}/opcua-certificate-store
   ```

1. The SiteWise Edge gateway's OPC UA client certificate for this source is in the `aws-iot-opcua-client.pfx` file.

   Run the following command to export the certificate to a `.pem` file called `aws-iot-opcua-client-certificate.pem`.

   ```
   keytool -exportcert -v -alias aws-iot-opcua-client -keystore aws-iot-opcua-client.pfx -storepass amazon -storetype PKCS12 -rfc > aws-iot-opcua-client-certificate.pem
   ```

1. Transfer the certificate file, `aws-iot-opcua-client-certificate.pem`, from the SiteWise Edge gateway to the OPC UA server.

   To do so, you can use common software such as the `scp` program to transfer the file using the SSH protocol. For more information, see [Secure copy](https://en.wikipedia.org/wiki/Secure_copy) on *Wikipedia*.
**Note**  
If your SiteWise Edge gateway is running on Amazon Elastic Compute Cloud (Amazon EC2) and you're connecting to it for the first time, you must configure prerequisites to connect. For more information, see [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) in the *Amazon EC2 User Guide*.

1. Import the certificate file, `aws-iot-opcua-client-certificate.pem`, on the OPC UA server to trust the SiteWise Edge gateway. Steps can vary depending on the source server that you use. Consult the documentation for the server.