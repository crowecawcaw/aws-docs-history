# Securing your Amazon Neptune database with Amazon VPC

An Amazon Neptune DB cluster can _only_ be created in an Amazon Virtual Private Cloud
(Amazon VPC), and its endpoints are accessible within that VPC, usually from an Amazon Elastic Compute Cloud
(Amazon EC2) instance running in that VPC. Alternatively, it can be accessed using a public endpoint. For more
information on public endpoints, see
[Neptune public endpoints](neptune-public-endpoints.md "neptune-public-endpoints.md").

You can secure your Neptune data by limiting access to the VPC where your
Neptune DB cluster is located, as described in [Connecting to an Amazon Neptune cluster](get-started-connecting.md "get-started-connecting.md").
