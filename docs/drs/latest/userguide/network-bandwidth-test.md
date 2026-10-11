

# Running a network bandwidth test to an EC2 endpoint
<a name="network-bandwidth-test"></a>

This procedure measures throughput over TLS on TCP port 1500 between a source server and an Amazon Elastic Compute Cloud instance that you launch as a disposable endpoint. The test exercises the same encrypted path that replication uses. As a result, it reveals TLS interception by a middlebox and the maximum transmission unit (MTU) effects that a plain TCP test can hide. You run the test from one of two clients that drive the same endpoint, on the same port, with the same certificate: a command-line client or a browser. Use the command-line client; it produces the figure you should quote and is the only client that lets you set the number of concurrent streams. Choose the browser instead when the source server has a desktop, or when you want to watch the test run.

**Note**  
This procedure uses a self-signed certificate with a manually supplied trust anchor. Treat the result as a measurement of the network path, not as confirmation that Elastic Disaster Recovery certificate validation will succeed.

Replace every value shown as a {{placeholder}} with one from your own account. Each task sets the shell variables it needs at the point where you use them, on the host that uses them.

## Security considerations for the test endpoint
<a name="bwtest-security"></a>

**Important**  
The test endpoint is unauthenticated. There is no login, token, or per-client authorization. Anyone who can reach port 1500 can run a test against it and consume your bandwidth. The only access control is the security group.

Keep the following in mind before you launch the endpoint:
+ **Scope ingress on port 1500 to the addresses you test from.** Because the endpoint is unauthenticated, every address the security group admits can run tests and spend your bandwidth. Narrower ranges mean less exposure. We recommend against opening the rule to a wide range such as `0.0.0.0/0`: an internet-open, unauthenticated, bandwidth-generating endpoint is an abuse target. If no narrower range is workable, make that decision knowingly, and tear the endpoint down as soon as you have your numbers.
+ **The instance is disposable and must be terminated.** The main cost risk is forgetting to terminate the instance, along with the data transfer that each run moves. See [Tear down the test rig](bwtest-teardown.md) and [Costs](bwtest-costs.md).
+ **Your organization's security tooling might isolate an internet-reachable endpoint.** Many organizations run automated detection that stops or isolates instances that expose an unauthenticated service, and it can act within hours.

## Choosing your connectivity path
<a name="bwtest-connectivity"></a>

The endpoint binds to `0.0.0.0:1500` and serves on every address the instance has, so the shape of the procedure is the same in all three cases. What changes is which address you put in the security group and which name you connect by.


| Your source server is | Endpoint needs a public IP? | Notes | 
| --- | --- | --- | 
| In the same VPC as the endpoint | No | The complete procedure, including full certificate verification, runs against an endpoint that has no public IP in a subnet with no internet route. | 
| On-premises over VPN or Direct Connect | No | The endpoint serves on its private address, and VPN or Direct Connect delivers to that same private address through Amazon VPC routing. Path MTU and any middlebox on your tunnel are exactly what this test exists to reveal, so they show up in your result. Connect by the endpoint's private IP address, not a DNS name; see [Write the server list](bwtest-cli-test.md#bwtest-cli-serverlist). | 
| On the public internet | Yes | The endpoint is reachable from the internet. See [Security considerations for the test endpoint](#bwtest-security). | 

The private path is the default in this procedure. The only step that needs internet access from the endpoint is the software download in [Install the endpoint software](bwtest-software-install.md), and that step is separable.

**Note**  
From inside the VPC, an instance's public DNS name resolves to its private IP. That is a convenience when you want the private path and an obstacle when you want the public one. The name you connect by has to match the path you intend to measure, not only the certificate.

## Prerequisites
<a name="bwtest-prerequisites"></a>


| You need | Notes | 
| --- | --- | 
| An AWS account and an AWS Region to test into | Use the Region you replicate to. | 
| Permission to launch and terminate an Amazon EC2 instance and to edit its security group | The exact actions depend on how you launch and connect to the instance, so this list cannot be complete for every method. Grant the permissions that your chosen launch and access method require. | 
| The address each source server reaches the endpoint from | For a source server in the same VPC, this is its private IP. For a source server on-premises over VPN or Direct Connect, it is the private address it presents inside the VPC. Only for a source server on the public internet is it the public egress address, which you get from the source server with curl -sS https://checkip.amazonaws.com. Getting this wrong is the most common reason the pre-flight check in [Run the measurement](bwtest-cli-test.md#bwtest-cli-run) reports that the server is not responding. | 
| A VPC and subnet | No internet route is needed unless a source server is on the public internet. | 
| A way to open a shell on the new instance | You need interactive shell access to run [Install the endpoint software](bwtest-software-install.md). Use whichever method suits your network. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the Amazon EC2 User Guide. | 

**Topics**
+ [Security considerations for the test endpoint](#bwtest-security)
+ [Choosing your connectivity path](#bwtest-connectivity)
+ [Prerequisites](#bwtest-prerequisites)
+ [Launch the endpoint instance](bwtest-instance-setup.md)
+ [Install the endpoint software](bwtest-software-install.md)
+ [Test with the command line](bwtest-cli-test.md)
+ [Test with the browser](bwtest-browser-test.md)
+ [Tear down the test rig](bwtest-teardown.md)
+ [Interpreting the result](bwtest-interpreting.md)
+ [Costs](bwtest-costs.md)
+ [Troubleshooting the bandwidth test](bwtest-troubleshooting.md)