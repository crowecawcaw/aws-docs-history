# Connect customer-managed fleets to a license endpoint

The AWS Deadline Cloud usage-based license server provides on-demand licenses for select third-party
products. With usage-based licenses, you can pay as you go. You are only charged for the time
you use. Usage-based licensing provides licenses for your Deadline Cloud workers to render, it doesn't
provide licenses for your DCC applications.

The Deadline Cloud usage-based license server can be used with any fleet type as long as the Deadline Cloud
workers can communicate with the license server. This is automatically set up in service-managed
fleets. This setup is only needed for customer-managed fleets.

To create the license server, you need a security group for your farm's VPC that allows
traffic for third-party licenses.

###### Topics

- [Step 1: Create a security group](#cmf-ubl-step-1 "#cmf-ubl-step-1")
- [Step 2: Set up the license endpoint](#cmf-ubl-step-2 "#cmf-ubl-step-2")
- [Step 3: Connect a rendering application to an
  endpoint](#w49aac32c15c15 "#w49aac32c15c15")
- [Step 4: Delete a license endpoint](#w49aac32c15c17 "#w49aac32c15c17")

## Step 1: Create a security group

Use the [Amazon VPC Console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc") to create a security group
for your farm's VPC. Configure the security group to allow the following inbound rules:

- Autodesk Maya and Arnold – 2701 - 2702, TCP, IPv4, IPv6
- Autodesk 3ds Max – 2704, TCP, IPv4, IPv6
- Cinema 4D – 7057, TCP, IPv4, IPv6
- KeyShot – 2703, TCP, IPv4, IPv6
- Foundry Nuke – 6101, TCP, IPv4, IPv6
- Red Giant – 7055, TCP, IPV4
- Redshift – 7054, TCP, IPv4, IPv6
- SideFX Houdini, Mantra, and Karma – 1715 - 1717, TCP, IPv4, IPv6
- VRay – 30304, TCP, IPV4

The source for each inbound rule is the fleet's worker security group.

For more information about creating a security group, see [Create a security group](../../../vpc/latest/userguide/working-with-security-groups.md#creating-security-groups "../../../vpc/latest/userguide/working-with-security-groups.md#creating-security-groups") in the _Amazon Virtual Private Cloud user guide_.

## Step 2: Set up the license endpoint

A _license endpoint_ provides access to license servers for third-party
products. License requests are sent to the license endpoint. The endpoint routes them to the
appropriate license server. The license server tracks usage limits and entitlements. Creating
a license endpoint in Deadline Cloud provisions an AWS PrivateLink interface endpoint in your VPC. These
endpoints are billed according to standard AWS PrivateLink pricing. For more information, see [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing "https://aws.amazon.com/privatelink/pricing").

With the appropriate permissions, you can create your license endpoint. For the required
policy to create a license endpoint, see [Policy to allow creating a license endpoint](../userguide/security_iam_id-based-policy-examples.md#security_iam-id-based-policy-examples-create-endpoint "../userguide/security_iam_id-based-policy-examples.md#security_iam-id-based-policy-examples-create-endpoint").

You can create your license endpoint from your dashboard in the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").

1. From the left navigation pane, choose **License endpoints**, then choose
   **Create license endpoint**.
2. From the Create license endpoint page, complete the following:
   - Select a VPC.
   - Select the subnets that contain your Deadline Cloud workers. You can select up to 10 subnets.
   - Select the security group you created in step 1. You can select up to 10 security
     groups for more complicated scenarios.
   - (Optional) Choose **Add new tag** and add one or more tags. You can
     add up to 50 tags.

3. Choose **Create license endpoint**. When the license endpoint creates, it
   displays on the license endpoints page.
4. From the metered products section, choose **Add products**, and then
   select the products you want to add to your license endpoint. Choose **Add**.

To remove a product from a license endpoint, in the metered products section, select the product
and then choose **Remove**. In the confirmation, choose **Remove** again.

## Step 3: Connect a rendering application to an

endpoint

After the license endpoint is set up, applications use it the same as they use a
third-party license server. You typically configure the license server for the application by
setting an environment variable or other system setting, such as a Microsoft Windows registry
key, to a license server port and address.

To get the license endpoint DNS name, select the license endpoint in the console and then
choose the copy icon in the DNS Name section.

### Configuration examples

###### Example – Autodesk Maya and Arnold

###### Note

You can use Autodesk Maya and Arnold together or separately. Use port 2702 for Autodesk Maya and port 2701 for Arnold.

For Autodesk Maya, set the environment variable `ADSKFLEX_LICENSE_FILE` to:

```
2702@`VPC_Endpoint_DNS_Name`
```

For Arnold, set the environment variable `ADSKFLEX_LICENSE_FILE` to:

```
2701@`VPC_Endpoint_DNS_Name`
```

For Autodesk Maya and Arnold, set the environment variable `ADSKFLEX_LICENSE_FILE` to:

```
2702@`VPC_Endpoint_DNS_Name`:2701@`VPC_Endpoint_DNS_Name`
```

###### Note

For Windows workers, use a semi-colon (;) instead of a colon (:) to separate
endpoints.

###### Example – Autodesk 3ds Max

Set the environment variable `ADSKFLEX_LICENSE_FILE` to:

```
2704@`VPC_Endpoint_DNS_Name`
```

###### Example – Cinema 4D

Set the environment variable `g_licenseServerRLM` to:

```
`VPC_Endpoint_DNS_Name:7057`
```

After you create the environment variable, you should be able to render a an image
using a command line similar to this one:

```
"C:\Program Files\Maxon Cinema 4D 2025\Commandline.exe" -render ^
    "C:\Users\User\MyC4DFileWithRedshift.c4d" -frame 0 ^
    -oimage "C:\Users\Administrator\User\MyOutputImage.png
```

###### Example – KeyShot

Set the environment variable `LUXION_LICENSE_FILE` to:

```
2703@`VPC_Endpoint_DNS_Name`
```

After you install KeyShot and run `pip install
 deadline-cloud-for-keyshot` you can test the license is working using the
following command. The script validates your settings but does not render anything.

```
"C:\Program Files\KeyShot12\bin\keyshot_headless.exe" ^
    -floating_feature keyshot2 ^
    -floating_license_server 2703@`VPC_Endpoint_DNS_Name` ^
    -script "C:\Program Files\Python311\Lib\site-packages\deadline\keyshot_adaptor\KeyShotClient\keyshot_handler.py"
```

The response should contain the following without any error messages:

```
Connecting to floating license server
```

###### Example – Foundry Nuke

Set the environment variable `foundry_LICENSE` to:

```
6101@`VPC_Endpoint_DNS_Name`
```

To test that licensing is working properly, you can run Nuke in a terminal:

```
~/nuke/Nuke14.0v5/Nuke14.0 -x
```

###### Example – Red Giant

Set the environment variable `redshift_LICENSE` to:

```
7055@`VPC_Endpoint_DNS_Name`
```

Note that Red Giant and Redshift have the same `redshift_LICENSE` environment variable.
If you want to use both applications, you can set the environment variable to:

```
7054@`VPC_Endpoint_DNS_Name`:7055@`VPC_Endpoint_DNS_Name`
```

###### Note

For Windows workers, use a semi-colon (;) instead of a colon (:) to separate
endpoints.

To test that licensing is working properly, ensure you have After Effects and Red Giant installed.
Then, you can render a project using a command similar to this one:

```
C:\Program Files\Adobe\Adobe After Effects 2025\Support Files\aerender.exe -comp "Comp 1" -project
          C:\Users\MyUser\`myAfterEffectsProjectUsingRedGiant`.aep -output
            C:\Users\MyUser\`myMovieWithRedGiant`.mp4
```

###### Example – Redshift

Set the environment variable `redshift_LICENSE` to:

```
`7054@VPC_Endpoint_DNS_Name`
```

After you create the environment variable, you should be able to render an image
using a command line similar to this one:

```
C:\ProgramData\redshift\bin\redshiftCmdLine.exe ^
    C:\demo\proxy\RS_Proxy_Demo.rs ^
    -oip C:\demo\proxy\images
```

###### Example – SideFX Houdini, Mantra, and Karma

Run the following command:

```
/opt/hfs19.5.640/bin/hserver -S "http://`VPC_Endpoint_DNS_Name`:1715;http://`VPC_Endpoint_DNS_Name`:1716;http://`VPC_Endpoint_DNS_Name`:1717;"
```

To test that licensing is working properly, you can render a Houdini scene via this
command:

```
/opt/hfs19.5.640/bin/hython ~/forpentest.hip -c "hou.node('/out/mantra1').render()"
```

###### Example – VRay

Set the environment variable `VRAY_AUTH_CLIENT_SETTINGS` to:

```
licset://`VPC_Endpoint_DNS_Name`:30304
```

Set the environment variable `VRAY_AUTH_CLIENT_FILE_PATH` to:

```
`/null`
```

To test that licensing is working properly, you can render an image in VRay using a command similar to this one:

```
/usr/Chaos/V-Ray/bin/vray -sceneFile=/root/`my_scene`.vrscene -display=0
```

## Step 4: Delete a license endpoint

When deleting your customer-managed fleet, remember to delete your license endpoint.
If you don't delete the license endpoint, you will continue to be charged for AWS PrivateLink
fixed costs

You can delete your license endpoint from your dashboard in the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").

1. From the left navigation pane, choose **License endpoints**.
2. Select the endpoint you want to delete and choose **delete**, then
   choose **delete** again to confirm.
