

# Delivering HLS output to MediaPackage version 2
<a name="output-empV4"></a>

This section describes how to deliver an HLS output from AWS Elemental Live to an AWS Elemental MediaPackage channel that uses MediaPackage v2. You can optionally configure the video output for low latency, to support a glass-to-glass low latency workflow. 

The information in this section assumes that you are familiar with the general steps for creating an event. 

1. Obtain the following information from the MediaPackage operator:
   + The URL for each destination for the output group. For delivery to MediaPackage v2, the URL will always include the string `mediapackagev2`. 
   + The credentials that Elemental Live must include to deliver this output to MediaPackage v2. For example:

     An *access key ID* that looks like this: **AKIAIOSFODNN7EXAMPLE**

     A *secret access key* that looks like this: **wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY**

1. In the Elemental Live event, go to **Output Groups**, then to **Apple HLS**.

1. Set up the output group in the usual way. Complete the following fields as specified:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/output-empV4.html)

1. If you want to implement low latency in the encoder, follow the guidance for these fields:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/output-empV4.html)