

# Direct Connect in Local Zones
<a name="local-zones-connectivity-direct-connect"></a>

With Direct Connect, you transfer data privately and directly from your data center into and out of Local Zones using a Public Virtual Interface (VIF) or Private VIF. Direct Connect provides similar benefits to using a software-based VPN on Amazon EC2, but bypasses the public internet and reduces the overheard required to manage the connection to Local Zones.

For more information, see the [Direct Connect User Guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html).

The following diagram shows a Direct Connect connection between a Local Zones and data center.

![An AWS Region with a VPC. The VPC contains an Availability Zone and a Local Zone. Each zone has a private subnet. The diagram also shows an on-premise data center with a customer gateway outside the AWS Region. A Direct Connect connection facilitates traffic between the Local Zone and the data center.](http://docs.aws.amazon.com/local-zones/latest/ug/images/local-zones-direct-connect.png)


During a hybrid cloud migration, you can migrate your applications to Local Zones while using Direct Connect to communicate back to other parts of your applications in the data center. An example is migrating the front end of an application to Amazon EC2, Amazon ECS, or Amazon EKS in a Local Zone and having the back-end database remain in the data center. Eventually, you can migrate the database to the Local Zone and the entire application to an AWS Region.