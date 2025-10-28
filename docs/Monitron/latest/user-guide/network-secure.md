Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Securing your network

In order to allow your Amazon Monitron gateways to send data back to AWS, you should
allow the following with regard to your local network traffic:

- Protocol UDP, port 53 - standard DNS port
- Protocol UDP, ports 67 and 68 - standard DHCP ports
- TCP ports 443 and 8883
- For Amazon Monitron gateways commissioned before 19th January, 2024:
  - Domains ending in `*.amazonaws.com`

- For Amazon Monitron gateways commissioned after 19th January, 2024:
  - Asia Pacific (Sydney) (ap-southeast-2) – 54.79.215.104 and
    54.79.23.89
  - Europe (Ireland) (eu-west-1) – 54.72.131.46, 34.251.27.192,
    and 52.213.71.97
  - US East (N. Virginia) (us-east-1) – 3.215.69.205, 52.86.131.66,
    and 18.210.44.199

###### Note

There's no regression with new static IPs being enabled by default for previously
commissioned devices as they have already been allow listed for IP domains ending in
`*.amazonaws.com` (which already includes the new static IP domain of
`amazonaws.com`). Decommissioning and recomissioning a gateway will
switch it to static IP. You can't revert a gateway network configuration from a
static IP to a dynamic IP.

If you are using an **Android mobile device** to
provision your gateways and sensors, then you should allow the following with regard to
your local network traffic:

- TCP ports 443, 5228, 5229, and 5230
- Domains ending in `*.google.com`,
  `*.googleapis.com`
- Any ports required by your telecom provider
- TCP port 5094 for SSL communications used on

**_Vodafone devices_**
If you are using an **Apple mobile device** to provision
your gateways and sensors, then you should allow the following with regard to your local
network traffic:

- TCP ports 443, 2197, and 5223
- Subnets 17.249.0.0/16, 17.252.0.0/16, 17.57.144.0/22, 17.188.128.0/18, and
  17.188.20.0/23
- See also: [Apple’s list
  of required ports and hosts](https://support.apple.com/en-us/HT203609 "https://support.apple.com/en-us/HT203609")
  Note: Amazon Monitron, Android, and Apple do not (per their respective documentation)
  require the following ports to be open:

- UDP port 443
- TCP port 80
