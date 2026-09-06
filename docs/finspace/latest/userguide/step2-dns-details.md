

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Step 2: Adding DNS details to your network connection
<a name="step2-dns-details"></a>

The **Network** tab on the Kdb environments details page allows you to add custom DNS server name and IP address. This is used when you have a custom DNS server that you want to query for internal host names. The DNS server IP is used for DNS resolution of queries. 

**To add DNS details**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Kdb environments**.

1. From the kdb environments table, choose the name of the environment.

1. Under **DNS details**, choose **Add details**.

1. On **Add DNS details** page, enter *example.com* as the DNS server name and *173.31.0.2* as the DNS server IP. This means that any DNS queries for *example.com* from the FinSpace clusters will return the DNS resolver at *172.31.0.2* in the your VPC.
**Note**  
The IP *172.31.0.2* is the second IP address in the default VPC CIDR and corresponds to the IP of the DNS Resolver for an Amazon VPC. Any DNS queries for *example.com* from the FinSpace clusters will return the DNS resolver at *172.31.0.2* in your custom VPC.

1. Choose **Add DNS details**. The **environment details** page opens and the DNS details are added in the **DNS details** section, from where you can edit the DNS details.