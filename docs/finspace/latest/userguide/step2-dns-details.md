After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Step 2: Adding DNS details to your network connection

The **Network** tab on the Kdb environments details page allows you to
add custom DNS server name and IP address. This is used when you have a custom DNS server that
you want to query for internal host names. The DNS server IP is used for DNS resolution of
queries.

###### To add DNS details

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. Under **DNS details**, choose **Add details**.
5. On **Add DNS details** page, enter _example.com_ as the DNS server name and _173.31.0.2_ as the DNS server IP. This means that any DNS queries for _example.com_ from the FinSpace clusters will return the DNS resolver at
   _172.31.0.2_ in the your VPC.

###### Note

The IP _172.31.0.2_ is the second IP address in the
default VPC CIDR and corresponds to the IP of the DNS Resolver for an Amazon VPC. Any DNS queries
for _example.com_ from the FinSpace clusters will return
the DNS resolver at _172.31.0.2_ in your custom VPC. 6. Choose **Add DNS details**. The **environment
details** page opens and the DNS details are added in the **DNS details** section, from where you can edit the
DNS details.
