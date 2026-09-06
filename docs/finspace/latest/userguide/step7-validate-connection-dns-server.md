

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Step 7: Validating connection using the DNS server configuration
<a name="step7-validate-connection-dns-server"></a>

 As an example, create a private hosted zone in your account that has an A record rule for *example.com* and Private IP DNS name of *customerEc2Instance*. 

 To create a private hosted zone, see [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) in the *Amazon Route 53 User Guide*. To create a record rule, see [this](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) section. 

 Start a q process and connect to the RDB cluster on port *5005* by using the following example command. 

```
q)cs_rdb1: <RDB cluster connection string> 
q)cs_rdb1: ssr[cs_rdb1;"\n";""] 
q)conn: hopen cs_rdb1 
q)conn hopen(":<Private IP DNS name of customerEc2Instance 5005"; 10)
```

 Next, run the following command to test connection on port *5005* by using the DNS name *example.com*. 

```
q)cs_rdb1: <RDB cluster connection string> 
q)cs_rdb1: ssr[cs_rdb1;"\n";""] 
q)conn: hopen cs_rdb1 
q)conn hopen(":example.com:5005"; 10)
```

 The connection test using the DNS name should work successfully. 