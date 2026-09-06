

# What gets created with your Simple AD
<a name="simple_ad_what_gets_created"></a>

When you create a Active Directory with Simple AD, Directory Service performs the following tasks on your behalf:
+ Sets up a Samba-based directory within the VPC.
+ Creates a directory administrator account with the user name `Administrator` and the specified password. You use this account to manage your directory.
**Important**  
Be sure to save this password. Directory Service does not store this password, and it cannot be retrieved. However, you can reset a password from the Directory Service console or by using the [ResetUserPassword](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html) API.
+ Creates a security group for the directory controllers. 
+ Creates an account with the name `AWSAdminD-{{xxxxxxxx}}` that has domain admin privileges. This account is used by Directory Service to perform automated operations for directory maintenance operations, such as taking directory snapshots and FSMO role transfers. The credentials for this account are securely stored by Directory Service.
+ Automatically creates and associates an elastic network interface (ENI) with each of your domain controllers. Each of these ENIs are essential for connectivity between your VPC and Directory Service domain controllers and should never be deleted. You can identify all network interfaces reserved for use with Directory Service by the description: "AWS created network interface for directory *directory-id*". For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide*. The default DNS Server of the AWS Managed Microsoft AD Active Directory is the VPC DNS server at Classless Inter-Domain Routing (CIDR)\+2. For more information, see [Amazon DNS server](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#AmazonDNS) in *Amazon VPC User Guide*.
**Note**  
Domain controllers are deployed across two Availability Zones in a region by default and connected to your Amazon Virtual Private Cloud (VPC). Backups are automatically taken once per day, and the Amazon Elastic Block Store (EBS) volumes are encrypted to ensure that data is secured at rest. Domain controllers that fail are automatically replaced in the same Availability Zone using the same IP address, and a full disaster recovery can be performed using the latest backup.