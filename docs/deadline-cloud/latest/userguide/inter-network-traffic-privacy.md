# Inter-network traffic privacy

AWS Deadline Cloud supports Amazon Virtual Private Cloud (Amazon VPC) to secure connections. Amazon VPC provides features that
you can use to increase and monitor the security for your virtual private cloud (VPC).

You can set up a customer-managed fleet (CMF) with Amazon Elastic Compute Cloud (Amazon EC2) instances that run
inside a VPC. By deploying Amazon VPC endpoints to use AWS PrivateLink, traffic between workers in
your CMF and the Deadline Cloud endpoint stays within your VPC. Furthermore, you can configure your VPC
to restrict internet access to your instances.

In service-managed fleets, workers aren't reachable from the internet, but they do have
internet access and connect to the Deadline Cloud service over the internet. Each service-managed fleet
runs in its own isolated network, and worker instances remain dedicated to individual customers.
