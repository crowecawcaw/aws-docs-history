# Tutorial: Bring your ASN to IPAM

If your applications are using trusted IP addresses and Autonomous System Numbers (ASNs) that your partners or customers have allow listed in their network, you can run these applications in AWS without requiring your partners or customers to change their allow lists.

An Autonomous System Number (ASN) is a globally unique number which enables a group of networks to be identified over the internet and exchange routing data with other networks dynamically using [Border Gateway Protocol](https://aws.amazon.com/what-is/border-gateway-protocol/ "https://aws.amazon.com/what-is/border-gateway-protocol/"). Internet service providers (ISPs), for example, use ASNs to identify the network traffic source. Not all organizations purchase their own ASNs, but for organizations which do, they can bring their ASN to AWS.

Bring your own autonomous system number (BYOASN) enables you to advertise the IPv4 or IPv6
addresses that you bring to AWS with your own public ASN instead of the AWS ASN. When
you use BYOASN, the traffic originating from your IP address carries your ASN instead of the
AWS ASN, and your workloads are reachable by customers or partners that have allow listed
traffic based on your IP address and ASN.

###### Important

- Complete this tutorial using the IPAM admin account in your IPAM’s home Region.
- This tutorial assumes you own the public ASN you’d like to bring to IPAM and that you’ve already brought a BYOIP CIDR to AWS and provisioned it to a pool in your public scope. You can bring an ASN to IPAM at any time, but to use it, you have to associate with a CIDR that you’ve brought to your AWS account. This tutorial assumes that you have already done that. For more information, see [Tutorial: Bring your IP addresses to IPAM](tutorials-byoip-ipam.md "tutorials-byoip-ipam.md").
- You can change between your advertising your own ASN or an AWS ASN without delay, but you are limited to changing from an AWS ASN to your own ASN once per hour.
- If your BYOIP CIDR is currently advertised, you do not have to withdraw it from advertising to associate with your ASN.

## Onboarding prerequisites for your ASN

You will need the following to complete this tutorial:

- Your public 2-byte or 4-byte ASN.
- If you've already brought an IP address range to AWS with [Tutorial: Bring your IP addresses to IPAM](tutorials-byoip-ipam.md "tutorials-byoip-ipam.md"), you need the IP address
  CIDR range. You'll also need a private key. You can use the private key that you created when
  you brought the IP address CIDR range to AWS or you can create a new private key as described
  in [Create a private key and
  generate an X.509 certificate](../../../AWSEC2/latest/UserGuide/prepare-for-byoip.md#byoip-certificate "../../../AWSEC2/latest/UserGuide/prepare-for-byoip.md#byoip-certificate") in the _Amazon EC2 User Guide_.
- When you bring an IPv4 or IPv6 address range to AWS with [Tutorial: Bring your IP addresses to IPAM](tutorials-byoip-ipam.md "tutorials-byoip-ipam.md"), you
  [create an
  X.509 certificate](../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-add-certificate "../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-add-certificate") and [upload
  the X.509 certificate to the RDAP record in your RIR](../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-add-certificate "../../../AWSEC2/latest/UserGuide/ec2-byoip.md#byoip-add-certificate"). You must
  upload the same certificate you created to the RDAP record in your RIR for the
  ASN. Be sure to include the `-----BEGIN CERTIFICATE-----` and
  `-----END CERTIFICATE-----` strings before and after the encoded
  portion. All of this content must be on a single, long line. The procedure for
  updating RDAP depends on your RIR:
  - For ARIN, use the [Account
    Manager portal](https://account.arin.net/public/secure/dashboard "https://account.arin.net/public/secure/dashboard") to add the certificate in the "Public
    Comments" section for the "Network Information" object representing your
    ASN by using the "Modify ASN" option. Do not add it to the comments
    section for your organization.
  - For RIPE, add the certificate as a new "descr" field to the “aut-num”
    object representing your ASN. These can usually be found in the "My
    Resources" section of the

  [RIPE Database portal](https://apps.db.ripe.net/db-web-ui/myresources/overview "https://apps.db.ripe.net/db-web-ui/myresources/overview") . Do not add it to the comments
  section for your organization or the "remarks" field of the “aut-num”
  object.
  - For APNIC, email the certificate to [helpdesk@apnic.net](mailto:helpdesk@apnic.net "mailto:helpdesk@apnic.net") to
    manually add it to the "remarks" field for your ASN. Send the email
    using the APNIC authorized contact for the ASN.

- When you bring an IP address range to IPAM, you create a ROA to verify that you control the IP address
  space that you are bringing to IPAM. In addition to that ROA, you must have a second ROA in your RIR
  with the ASN that you are bringing to IPAM. If you don’t have this second
  ROA for the ASN in your RIR, complete [3. Create a ROA object](../../../AWSEC2/latest/UserGuide/prepare-for-byoip.md#byoip-create-roa-object "../../../AWSEC2/latest/UserGuide/prepare-for-byoip.md#byoip-create-roa-object") in your RIR. Ignore the other steps.

## Tutorial steps

Complete the steps below using the AWS console or the AWS CLI.

AWS Management Console

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the left navigation pane, choose **IPAMs**.
3. Choose your IPAM.
4. Choose the **BYOASNs** tab and choose **Provision BYOASNs**.
5. Enter the **ASN**. As a result, the **Message** field is automatically populated with the message you will need to sign in the next step.
   - The format of the message is as follows, where ACCOUNT is your AWS account number, ASN is the ASN you are bringing to IPAM, and YYYYMMDD is the expiry date of the message (which defaults to the last day of the next month). Example:

   ```
   text_message="1|aws|ACCOUNT|ASN|YYYYMMDD|SHA256|RSAPSS"
   ```

6. Copy the message and replace the expiry date with your own value if you want to.
7. Sign the message using the private key. Example:

```
signed_message=$( echo -n $text_message | openssl dgst -sha256 -sigopt rsa_padding_mode:pss -sigopt rsa_pss_saltlen:-1 -sign private-key.pem -keyform PEM | openssl base64 | tr -- '+=/' '-_~' | tr -d "\n")
```

8. Under **Signature**, enter the signature.
9. (Optional) To provision another ASN, choose **Provision another ASN**. You
   can provision up to 5 ASNs. To increase this quota, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").
10. Choose **Provision**.
11. View the provisioning process in the **BYOASNs** tab. Wait for the
    **State** to change from _Pending-provision_ to _Provisioned_. BYOASNs in a _Failed-provision_ state are automatically removed after 7
    days. Once the ASN is successfully provisioned, you can associate it
    with a BYOIP CIDR.
12. In the left navigation pane, choose **Pools**.
13. Choose your public scope. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
14. Choose a regional pool that has a BYOIP CIDR provisioned to it. The pool must have **Service** set to **EC2** and must have a locale chosen.
15. Choose the **CIDRs** tab and select a BYOIP CIDR.
16. Choose **Actions** > **Manage BYOASN associations**.
17. Under **Associated BYOASNs**, choose the ASN you brought to AWS. If you have multiple ASNs, you can associate multiple ASNs to the BYOIP CIDR. You can associate as many ASNs as you can bring to IPAM. Note that you can bring up to 5 ASNs to IPAM by default. For more information, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").
18. Choose **Associate**.
19. Wait for the ASN association to complete. Once the ASN is successfully associated with the BYOIP CIDR, you can advertise the BYOIP CIDR again.
20. Choose the pool **CIDRs** tab.
21. Select the BYOIP CIDR and choose **Actions** > **Advertise**. As a result, your ASN options are displayed: the Amazon ASN and any ASNs you’ve brought to IPAM.
22. Select the ASN you brought to IPAM and choose **Advertise CIDR**. As a result, the BYOIP CIDR is advertised and the value in the **Advertising** column changes from Withdrawn to Advertised. The **Autonomous System Number** column displays the ASN associated with the CIDR.
23. (optional) If you decide that you want to change the ASN association back to the Amazon ASN, select the BYOIP CIDR and choose **Actions** > **Advertise** again. This time, choose the Amazon ASN. You can swap back to the Amazon ASN at any time, but you can only change to a custom ASN once every hour.

The tutorial is complete.

###### Cleanup

1. Disassociate the ASN from the BYOIP CIDR
   - To withdraw the BYOIP CIDR from advertising, in your pool in the public scope, choose the BYOIP CIDR and choose **Actions** > **Withdraw from advertising**.
   - To disassociate the ASN from the CIDR, choose **Actions** > **Manage BYOASN associations**.

2. Deprovision the ASN
   - To deprovision the ASN, in the BYOASNs tab, choose the ASN and choose **Deprovision
     ASN**. As a result, the ASN is deprovisioned.
     BYOASNs in a _Deprovisioned_
     state are automatically removed after 7 days.

Cleanup is complete.

Command line

1. Provision your ASN by including your ASN and authorization message. The signature is the
   message signed with your private key.

```
aws ec2 provision-ipam-byoasn --ipam-id $ipam_id --asn 12345 --asn-authorization-context Message="$text_message",Signature="$signed_message"
```

2. Describe your ASN to track the provisioning process. If the request succeeds, you should see
   the _ProvisionStatus_ set to _provisioned_ after a few minutes.

```
aws ec2 describe-ipam-byoasn
```

3. Associate your ASN with your BYOIP CIDR. Any custom ASN you wish to advertise from must first be associated with your CIDR.

```
aws ec2 associate-ipam-byoasn --asn 12345 --cidr xxx.xxx.xxx.xxx/n
```

4. Describe your CIDR to track the association process.

```
aws ec2 describe-byoip-cidrs --max-results 10
```

5. Advertise your CIDR with your ASN. If the CIDR is already advertised, this will swap the origin ASN from Amazon’s to yours.

```
aws ec2 advertise-byoip-cidr --asn 12345 --cidr xxx.xxx.xxx.xxx/n
```

6. Describe your CIDR to see the ASN state change from _associated_ to _advertised_.

```
aws ec2 describe-byoip-cidrs --max-results 10
```

The tutorial is complete.

###### Cleanup

1. Do one of the following:
   - To withdraw just your ASN advertisement and go back to using the Amazon ASNs while keeping the CIDR advertised you must call advertise-byoip-cidr with the special AWS value for the asn parameter. You can swap back to the Amazon ASN at any time, but you can only change to a custom ASN once every hour.

   ```
   aws ec2 advertise-byoip-cidr --asn AWS --cidr xxx.xxx.xxx.xxx/n
   ```

   - To withdraw your CIDR and ASN advertisement simultaneously, you can call withdraw-byoip-cidr.

   ```
   aws ec2 withdraw-byoip-cidr --cidr xxx.xxx.xxx.xxx/n
   ```

2. To clean up your ASN, you must first disassociate it from your BYOIP CIDR.

```
aws ec2 disassociate-ipam-byoasn --asn 12345 --cidr xxx.xxx.xxx.xxx/n
```

3. Once your ASN is disassociated from all the BYOIP CIDRs with which you associated it, you can deprovision it.

```
aws ec2 deprovision-ipam-byoasn --ipam-id $ipam_id --asn 12345
```

4. The BYOIP CIDR can also be deprovisioned once all ASN associations are removed.

```
aws ec2 deprovision-ipam-pool-cidr --ipam-pool-id ipam-pool-1234567890abcdef0 --cidr xxx.xxx.xxx.xxx/n
```

5. Confirm the deprovisioning.

```
aws ec2 get-ipam-pool-cidrs --ipam-pool-id ipam-pool-1234567890abcdef0
```

Cleanup is complete.
