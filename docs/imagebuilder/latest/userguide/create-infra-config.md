# Create an infrastructure configuration

This section describes how you can use the Image Builder console or
**imagebuilder** commands in the AWS CLI to create an infrastructure
configuration,

Console
To create an infrastructure configuration resource from the Image Builder console, follow these
steps:

1.  Open the EC2 Image Builder console at
    [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2.  From the navigation pane, choose **Infrastructure
    configuration**.
3.  Choose **Create infrastructure configuration**.
4.  In the **General** section, enter the following required information:
    - Enter the **Name** of your infrastructure
      configuration resource.
    - Select an **IAM role** that you want to
      associate with the instance profile for component permissions on
      your build and test instances. Image Builder uses these permissions to
      download and run your components, upload logs to CloudWatch, and perform
      any additional actions that the components in your recipe
      specify.

5.  In the **AWS infrastructure** panel, you can configure remaining
    infrastructure settings that are available. Enter the following required information:

        * **Instance type** – You can specify one or more instance
         types to use for this build. The service will pick one of these instance types based
         on availability.


        ###### Note

        Mac instances run on `.metal` instance types on
         a Dedicated Host. Your instance type must match one of the types that are
         defined for the host that it runs on. For more information
         about Mac instances and a list of instance types that natively support the
         macOS operating system, see [Amazon EC2 Mac instances](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md")
         in the *Amazon EC2 User Guide*.
        * **SNS topic (optional)** – Select an SNS topic to receive
         notifications and alerts from EC2 Image Builder.

    If you do not supply values for the following settings, they use service-specific
    defaults, where applicable.

        * **VPC, subnet, and security groups** – Image Builder uses your default
         VPC and subnet. For more information about configuring VPC
         interface endpoints, see [Image Builder and AWS PrivateLink interface VPC endpoints](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
        * In the **Troubleshooting settings** section, you can configure the
         following values:




        	+ By default, the **Terminate instance on failure** check box is
        	 selected. However, when a build fails, you can log
        	 on to the EC2 instance to troubleshoot. If you want
        	 your instance to continue to run after a build
        	 failure, clear the check box.
        	+ **Key pair** – If your EC2 instance continues to run after
        	 a build failure, you can create a key pair or use an
        	 existing key pair to log on to the instance and
        	 troubleshoot.
        	+ **Logs** – You can specify an S3 bucket where Image Builder can
        	 write application logs to help troubleshoot your
        	 build and tests. If you don't specify an S3 bucket,
        	 Image Builder writes the application logs to the
        	 instance.
        * In the **Instance metadata settings** section, you can configure the
         following values to apply to the EC2 instances that Image Builder
         uses to build and test your image:




        	+ Select the **Metadata version** to determine if EC2 requires a
        	 signed token header for instance metadata retrieval
        	 requests.




        		- **V1 and V2 (token optional)** – Default value if you
        		 don't select anything.
        		- **V2 (token required)**
        	###### Note

        	We recommend that you configure all EC2 instances that Image Builder launches from a pipeline
        	 build to use IMDSv2 so that instance metadata retrieval requests require a signed token header.
        	+ **Metadata token response hop limit** – The number
        	 of network hops that the metadata token can travel. Minimum hops: 1, maximum
        	 hops: 64, with a default of one hop.
        * In the **Instance placement settings** section, you can configure
         the following values to apply to the EC2 instances that Image Builder uses to build and
         test your image:




        	+ You can select the **Availability Zone**
        	 where Image Builder launches instances during image creation.
        	+ Optionally select **Tenancy** for the servers that
        	 run the instances that you launch. By default, EC2 instances run on
        	 shared tenancy hardware. This means that multiple AWS accounts
        	 might share the same physical hardware. An instance with `dedicated`
        	 tenancy runs on single-tenant hardware. An instance with `host`
        	 tenancy runs on a Dedicated Host.


        	Mac instances require a Dedicated Host that's created as a
        	 prerequisite before you build a custom image. Select
        	 `host` for your macOS image. You can then select a target
        	 host or host resource group to launch instances, but it's not required
        	 if your Dedicated Host has auto-placement enabled. For more information,
        	 see [Auto-placement](../../../AWSEC2/latest/UserGuide/dedicated-hosts-understanding.md#dedicated-hosts-auto-placement "../../../AWSEC2/latest/UserGuide/dedicated-hosts-understanding.md#dedicated-hosts-auto-placement") in the *Amazon EC2 User Guide*.




        		- **Tenancy host ID** – The ID of the
        		 Dedicated Host on which the instances run.
        		- **Tenancy host resource group** – The
        		 Amazon Resource Name (ARN) of the host resource group in which to
        		 launch the instances.

6.  In the **Infrastructure tags** section (optional), you can
    assign metadata tags to the Amazon EC2 instance that Image Builder launches during the
    build process. Tags are entered as key value pairs.
7.  In the **Tags** section (optional), you can
    assign metadata tags to the infrastructure configuration resource that Image Builder
    creates as output. Tags are entered as key value pairs.

AWS CLI
The following procedure shows how to configure the infrastructure for your image with the
Image Builder **[create-infrastructure-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-infrastructure-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-infrastructure-configuration.html")** command in the AWS CLI. The
command in step 2 takes in the file that you create in step 1. For these examples, the
file from step 1 is called `create-infrastructure-configuration.json`.

1. ###### Create a CLI input JSON file

The following examples show variations of the JSON file that you might
create for infrastructure configuration. Use a file editing tool to create
a JSON file of your own.

**Example 1: Configuration to retain an instance from a failed build**

This example specifies two instance types, `m5.large` and
`m5.xlarge`. We recommend that you specify more than one instance type because
this allows Image Builder to launch an instance from a pool with sufficient capacity. This
can reduce your transient build failures.

The `instanceProfileName` specifies the instance profile that
provides the instance with the permissions that the profile requires to perform
customization activities.
For example, if you have a component that retrieves
resources from Amazon S3, the instance profile requires permissions to access those files.
The instance profile also requires a minimal set of permissions for EC2 Image Builder to
successfully communicate with the instance. For more information, see
[Get set up to build custom images with Image Builder](set-up-ib-env.md "set-up-ib-env.md").

```
{
    "name": "`ExampleInfraConfigDontTerminate`",
    "description": "`An example that will retain instances of failed builds`",
    "instanceTypes": [
        "m5.large", "m5.xlarge"
    ],
    "instanceProfileName": "`myIAMInstanceProfileName`",
    "securityGroupIds": [
        "sg-`12345678`"
    ],
    "subnetId": "sub-`12345678`",
    "logging": {
        "s3Logs": {
            "s3BucketName": "`my-logging-bucket`",
            "s3KeyPrefix": "`my-path`"
        }
    },
    "keyPair": "`myKeyPairName`",
    "terminateInstanceOnFailure": false,
    "snsTopicArn": "arn:aws:sns:us-west-`2:123456789012`:`MyTopic`"
}
```

###### Example 2: macOS configuration with auto-placement

This example specifies instance types and placement for a Mac instance
where the Dedicated Host has auto-placement enabled.

```
{
   "name": "`macOSInfraConfigAutoPlacement`",
   "description": "`An example infrastructure configuration for macOS.`",
   "instanceProfileName": "`EC2InstanceProfileForImageBuilder`",
   "instanceTypes": ["mac1.metal, mac2.metal"],
   "terminateInstanceOnFailure": false,
   "placement": {
      "tenancy": "host"
   }
}
```

###### Example 3: macOS configuration with Host ID specified

This example specifies instance type and placement for a Mac instance
that targets a specific Dedicated Host.

```
{
   "name": "`macOSInfraConfigHostPlacement`",
   "description": "`An example infrastructure configuration for macOS.`",
   "instanceProfileName": "`EC2InstanceProfileForImageBuilder`",
   "instanceTypes": ["mac2-m1ultra.metal"],
   "terminateInstanceOnFailure": false,
   "placement": {
      "tenancy": "host",
      "hostId" : "`h-1234567890abcdef0`"
   }
}
```

2. ###### Use the file you created as input when you run the following command.

```
aws imagebuilder create-infrastructure-configuration --cli-input-json file://`create-infrastructure-configuration.json`
```
