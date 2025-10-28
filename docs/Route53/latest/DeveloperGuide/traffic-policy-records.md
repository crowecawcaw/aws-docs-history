# Creating and managing policy records

To route internet traffic to the resources that you specified when you created a
[traffic policy](traffic-policies.md "traffic-policies.md"), you create one or more policy records.
Each policy record identifies the hosted zone where you want to create the policy record and the domain or subdomain name that you want to
route traffic for. For example, if you want to route traffic for www.example.com, you specify the hosted zone ID for the example.com
hosted zone, and you specify www.example.com for the **Policy record DNS name**.

If you want to use the same traffic policy to route traffic for more than one domain or subdomain name, you have two options:

- You can create a policy record for each domain or subdomain name.
- You can create one policy record and then create CNAME or alias records that refer to the policy record.
  For example, if you want to use the same traffic policy for example.com, example.net, and example.org, you can do either of the following:

- Create one policy record for each of them.
- Create a policy record for one of them and then create CNAME records in the hosted zones for the other two.
  In the two CNAME records, you specify the record name that you created a policy record for.
  If you want to use the same traffic policy for a domain and its subdomains, such as example.com and www.example.com,
  you can create a policy record for one name and then create alias records for the rest. For example, you can create a
  policy record for example.com and then create an alias record for www.example.com that has the example.com record as the alias target.

###### Note

There's a monthly charge for each policy record that you create. If you want to use the same traffic policy for multiple domain or
subdomain names, you can use CNAME or alias records to reduce your charges:

- If you create one policy record and one or more CNAME records that refer to the policy record,
  you pay only for the policy record and for DNS queries for the CNAME records.
- If you create one policy record and one or more alias records in the same hosted zone that refer to the policy record,
  you pay only for the policy record and for DNS queries for the alias records.

###### Topics

- [Creating policy records](#traffic-policy-records-creating "#traffic-policy-records-creating")
- [Values that you specify when you create or update a policy record](#traffic-policy-records-creating-values "#traffic-policy-records-creating-values")
- [Updating policy records](#traffic-policy-records-updating "#traffic-policy-records-updating")
- [Deleting policy records](#traffic-policy-records-deleting "#traffic-policy-records-deleting")

## Creating policy records

To create a policy record, perform the following procedure.

###### Important

For each policy record that you create, you incur a monthly charge. If you later delete the
policy record, the charge is prorated. For more information, see the section "Traffic Flow" on the
[Amazon Route 53 Pricing](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/") page.

###### Note

We're updating the Traffic Flow console for Route 53. During the transition period, you can continue
to use the old console.

Choose the tab for the console you are using.

- [New console](#traffic-policy-records-creating-new-console "#traffic-policy-records-creating-new-console")
- [Old console](#traffic-policy-records-creating-old-console "#traffic-policy-records-creating-old-console")

New console

###### To create a policy record

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Policy records**.
3. On the **Policy records** page, choose **Create policy records**.
4. On the **Create policy records** page, specify the applicable values. For more information,
   see [Values that you specify when you create or update a policy record](#traffic-policy-records-creating-values "#traffic-policy-records-creating-values").
5. To add additional records to the same hosted zone, Choose **Add policy record**.
6. Choose **Create policy records**.

It can take several minutes for the status of created policy record to display as
**Applied**. 7. If you want to create policy records in another hosted zone, repeat steps 3 through 5.

###### Note

If the policy record status is **Failed**, choose the **info** button
next to the status to get more information about the failure. If you need further help and want to contact AWS support, see
[How do I get technical support from AWS?](https://repost.aws/knowledge-center/get-aws-technical-support "https://repost.aws/knowledge-center/get-aws-technical-support")

Old console

###### To create a policy record

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Policy records**.
3. On the **Policy records** page, choose **Create policy records**.
4. On the **Create policy records** page, specify the applicable values. For more information,
   see [Values that you specify when you create or update a policy record](#traffic-policy-records-creating-values "#traffic-policy-records-creating-values").
5. Choose **Create policy records**.

It can take several minutes for the status of created policy record to display as
**Applied**. 6. If you want to create policy records in another hosted zone, repeat steps 3 through 5.

###### Note

If the policy record status is **Failed**, choose the **info** button
next to the status to get more information about the failure. If you need further help and want to contact AWS support, see
[How do I get technical support from AWS?](https://repost.aws/knowledge-center/get-aws-technical-support "https://repost.aws/knowledge-center/get-aws-technical-support")

## Values that you specify when you create or update a policy record

###### Note

We're updating the Traffic Flow console for Route 53. During the transition period, you can continue
to use the old console. The following list applies for both console, except where noted.

When you create or update a policy record, you specify the following values

- [Traffic policy](#traffic-policy-records-creating-values-traffic-policy "#traffic-policy-records-creating-values-traffic-policy")
- [Version](#traffic-policy-records-creating-values-version "#traffic-policy-records-creating-values-version")
- [Hosted zone](#traffic-policy-records-creating-values-hosted-zone "#traffic-policy-records-creating-values-hosted-zone")
- [Policy record DNS name](#traffic-policy-records-creating-values-policy-record-dns-name "#traffic-policy-records-creating-values-policy-record-dns-name")
- [TTL](#traffic-policy-records-creating-values-ttl "#traffic-policy-records-creating-values-ttl")

**Traffic policy**
Choose the traffic policy whose configuration you want to use for this policy record.

**Version**
Choose the version of the traffic policy whose configuration you want to use for this policy record.

If you're updating an existing policy record, you must choose a version for which the DNS type matches the
current DNS type of the policy record. For example, if the DNS type of the policy record is **A**,
you must choose a version for which the DNS type is **A**.

**Hosted zone**
Choose the hosted zone in which you want to create a policy record by using the specified traffic policy
and version. You can't change the value of **Hosted zone** after you create a policy record.

**DNS name (new console), Policy record DNS name (old console)**
When you're creating a policy record, enter the domain name or subdomain name for which you want Route 53
to respond to DNS queries by using the configuration in the specified traffic policy and version.

To use the same configuration for more than one domain name or subdomain name in the specified hosted zone,
choose **Add policy record** (new console), or **Add another policy record** (old console), and enter the applicable domain name or subdomain name and TTL.

You can't change the value of **Policy record DNS name** after you create a policy record.

**TTL (in seconds)**
Enter the amount of time, in seconds, that you want DNS recursive resolvers to cache information
about this record. If you specify a longer value (for example, 172800 seconds, or two days),
you pay less for Route 53 service because recursive resolvers send requests to Route 53 less often. However, it takes
longer for changes to the records (for example, a new IP address) to take effect because
recursive resolvers use the values in their cache for longer periods instead of asking Route 53 for the latest information.

## Updating policy records

To update the settings in a policy record, perform the following procedure.

###### Note

We're updating the Traffic Flow console for Route 53. During the transition period, you can continue
to use the old console.

Choose the tab for the console you are using.

- [New console](#traffic-policy-records-updating-new-console "#traffic-policy-records-updating-new-console")
- [Old console](#traffic-policy-records-updating-old-console "#traffic-policy-records-updating-old-console")

New console

###### To update a policy record

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Policy records**.
3. On the **Policy records** page, select the check box for the policy record that you want to update,
   and choose **Edit**.
4. On the **Edit policy record** page, specify the applicable values. For more information,
   see [Values that you specify when you create or update a policy record](#traffic-policy-records-creating-values "#traffic-policy-records-creating-values").
5. Choose **Edit policy record**.

It can take several minutes for the status of created policy record to display as
**Applied**. 6. If you want to update another policy record, repeat steps 3 through 5.

###### Note

If the policy record status is **Failed**, choose the **info** button
next to the status to get more information about the failure. If you need further help and want to contact AWS support, see
[How do I get technical support from AWS?](https://repost.aws/knowledge-center/get-aws-technical-support "https://repost.aws/knowledge-center/get-aws-technical-support")

Old console

###### To update a policy record

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Policy records**.
3. On the **Policy records** page, select the check box for the policy record that you want to update,
   and choose **Edit policy record**.
4. On the **Edit policy record** page, specify the applicable values. For more information,
   see [Values that you specify when you create or update a policy record](#traffic-policy-records-creating-values "#traffic-policy-records-creating-values").
5. Choose **Edit policy record**.

It can take several minutes for the status of created policy record to display as
**Applied**. 6. If you want to update another policy record, repeat steps 3 through 5.

###### Note

If the policy record status is **Failed**, choose the **info** button
next to the status to get more information about the failure. If you need further help and want to contact AWS support, see
[How do I get technical support from AWS?](https://repost.aws/knowledge-center/get-aws-technical-support "https://repost.aws/knowledge-center/get-aws-technical-support")

## Deleting policy records

To delete policy records, perform the following procedure.

###### Important

If you delete policy records that Amazon Route 53 is using to respond to DNS queries, Route 53 will stop responding to
queries for the corresponding DNS names. For example, if Route 53 is using the policy record for www.example.com to respond to
DNS queries for www.example.com and you delete the policy record, your users will not be able to access your website or
web application by using the domain name www.example.com.

###### Note

We're updating the Traffic Flow console for Route 53. During the transition period, you can continue
to use the old console.

Choose the tab for the console you are using.

- [New console](#traffic-policy-records-deleting-new-console "#traffic-policy-records-deleting-new-console")
- [Old console](#traffic-policy-records-deleting-old-console "#traffic-policy-records-deleting-old-console")

New console

###### To delete a policy record

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Policy records**.
3. On the **Policy records** page, select the check boxes for the policy records that you want to delete,
   and choose **Delete**.
4. On the **Delete policy record** dialog box, choose **Confirm**.

Wait several minutes and refresh the page to make sure the policy record disappears from the list.

Old console

###### To delete a policy record

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Policy records**.
3. On the **Policy records** page, select the check boxes for the policy records that you want to delete,
   and choose **Delete policy record**.

Wait several minutes and refresh the page to make sure the policy record disappears from the list.
