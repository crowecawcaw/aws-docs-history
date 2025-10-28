# Port information

Use the following port numbers so that Amazon MSK can communicate with client machines:

- To communicate with brokers in plaintext, use port 9092.
- To communicate with brokers with TLS encryption, use port 9094 for access
  from within AWS and port 9194 for public access.
- To communicate with brokers with SASL/SCRAM, use port 9096 for access
  from within AWS and port 9196 for public access.
- To communicate with brokers in a cluster that is set up to use [IAM access control](iam-access-control.md "iam-access-control.md"), use port 9098 for access
  from within AWS and port 9198 for public access.
- To communicate with Apache ZooKeeper by using TLS encryption, use port 2182. Apache ZooKeeper nodes use port 2181 by default.
