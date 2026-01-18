# Clean up

1. ###### From your local machine, delete the cluster.

````
`$` `pcluster delete-cluster --cluster-name `"ad-cluster"` --region `"region-id"```{
 "cluster": {
 "clusterName": "ad-cluster",
 "cloudformationStackStatus": "DELETE_IN_PROGRESS",
 "cloudformationStackArn": "arn:aws:cloudformation:region-id:123456789012:stack/ad-cluster/1234567-abcd-0123-def0-abcdef0123456",
 "region": "region-id",
 "version": "3.14.1",
 "clusterStatus": "DELETE_IN_PROGRESS"
 }
}`
````

2. ###### Check the progress of the cluster being deleted.

```
`$` `pcluster describe-cluster --cluster-name `"ad-cluster"` --region `"region-id"` --query "clusterStatus"``"DELETE_IN_PROGRESS"`
```

After the cluster is successfully deleted, proceed to the next step.

###### Delete the Active Directory resources

1. From [https://console.aws.amazon.com/cloudformation/](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. In the navigation pane, choose **Stacks**.
3. From the list of stacks, choose the AD stack (for example, `pcluster-ad`).
4. Choose **Delete**.
5. ###### Delete the Amazon EC2 instance.
   1. From [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/"), choose **Instances** in the navigation
      pane.
   2. From the list of instances, choose the instance that you created to add users to the directory.
   3. Choose **Instance state**, then **Terminate instance**.

6. ###### Delete the hosted zone.
   1. Create a `recordset-delete.json` with the following content. In this example, HostedZoneId is the canonical hosted zone ID
      of the load balancer.

   ```
   {
     "Changes": [
       {
         "Action": "DELETE",
         "ResourceRecordSet": {
           "Name": "corp.example.com",
           "Type": "A",
           "Region": `"region-id"`,
           "SetIdentifier": "pcluster-active-directory",
           "AliasTarget": {
             "HostedZoneId": `"Z2IFOLAFXWLO4F"`,
             "DNSName": "CorpExampleCom-NLB-`3afe296bf4ba80d4`.elb.`region-id`.amazonaws.com",
             "EvaluateTargetHealth": true
           }
         }
       }
     ]
   }
   ```

   2. Submit the recordset change to the hosted zone using the hosted zone ID.

   ```
   ``$` aws route53 change-resource-record-sets --hosted-zone-id `Z09020002B5MZQNXMSJUB` \
    --change-batch file://recordset-delete.json``{
    "ChangeInfo": {
    "Id": "/change/C04853642A0TH2TJ5NLNI",
    "Status": "PENDING",
    "SubmittedAt": "2022-05-05T14:25:51.046000+00:00"
    }
   }`
   ```

   3. Delete the hosted zone.

   ````
   ``$` aws route53 delete-hosted-zone --id `Z09020002B5MZQNXMSJUB```{
    "ChangeInfo": {
    "Id": "/change/C0468051QFABTVHMDEG9",
    "Status": "PENDING",
    "SubmittedAt": "2022-05-05T14:26:13.814000+00:00"
    }
   }`
   ````

7. ###### Delete the LB listener.

```
``$` aws elbv2 delete-listener \
 --listener-arn arn:aws:elasticloadbalancing:`region-id`:`123456789012`:listener/net/CorpExampleCom-NLB`/3afe296bf4ba80d4/a8f9d97318743d4b` --region `region-id``
```

4. ###### Delete the target group.

```
``$` aws elbv2 delete-target-group \
 --target-group-arn arn:aws:elasticloadbalancing:`region-id`:`123456789012`:targetgroup/CorpExampleCom-Targets/`44577c583b695e81` --region `region-id``
```

5. ###### Delete the load balancer.

```
``$` aws elbv2 delete-load-balancer \
 --load-balancer-arn arn:aws:elasticloadbalancing:`region-id`:`123456789012`:loadbalancer/net/CorpExampleCom-NLB/`3afe296bf4ba80d4` --region `region-id``
```

6. ###### Delete the policy that the cluster uses to read the certificate from Secrets Manager.

```
``$` aws iam delete-policy --policy-arn arn:aws:iam::`123456789012`:policy/ReadCertExample`
```

7. ###### Delete the secret that contains the domain certificate.

````
``$` aws secretsmanager delete-secret \
 --secret-id arn:aws:secretsmanager:`region-id`:`123456789012`:secret:example-cert-`123abc` \
 --region `region-id```{
 "ARN": "arn:aws:secretsmanager:region-id:123456789012:secret:example-cert-123abc",
 "Name": "example-cert",
 "DeletionDate": "2022-06-04T16:27:36.183000+02:00"
}`
````

8. ###### Delete the certificate from ACM.

```
``$` aws acm delete-certificate \
 --certificate-arn arn:aws:acm:`region-id`:`123456789012`:certificate/`343db133-490f-4077-b8d4-3da5bfd89e72` --region `region-id``
```

9. ###### Delete the Active Directory (AD) resources.
   1. Get the following resource IDs from the output of the python script `ad.py`:
      - AD ID
      - AD subnet IDs
      - AD VPC ID

   2. Delete the directory by running the following command.

   ````
   ``$` aws ds delete-directory --directory-id `d-abcdef0123456789` --region `region-id```{
    "DirectoryId": "d-abcdef0123456789"
   }`
   ````

   3. List the security groups in the VPC.

   ```
   ``$` aws ec2 describe-security-groups --filters '[{"Name":"vpc-id","Values":["vpc-07614ade95ebad1bc"]}]' --region `region-id``
   ```

   4. Delete the custom security group.

   ```
   ``$` aws ec2 delete-security-group --group-id `sg-021345abcdef6789` --region `region-id``
   ```

   5. Delete the subnets.

   ```
   ``$` aws ec2 delete-subnet --subnet-id `subnet-1234567890abcdef` --region `region-id``
   ```

   ```
   ``$` aws ec2 delete-subnet --subnet-id `subnet-021345abcdef6789` --region `region-id``
   ```

   6. Describe internet gateway.

   ````
   ``$` aws ec2 describe-internet-gateways \
    --filters Name=attachment.vpc-id,Values=`vpc-021345abcdef6789` \
    --region `region-id```{
    "InternetGateways": [
    {
    "Attachments": [
    {
    "State": "available",
    "VpcId": "vpc-021345abcdef6789"
    }
    ],
    "InternetGatewayId": "igw-1234567890abcdef",
    "OwnerId": "123456789012",
    "Tags": []
    }
    ]
   }`
   ````

   7. Detach the internet gateway.

   ```
   ``$` aws ec2 detach-internet-gateway \
    --internet-gateway-id `igw-1234567890abcdef` \
    --vpc-id `vpc-021345abcdef6789` \
    --region `region-id``
   ```

   8. Delete the internet gateway.

   ```
   ``$` aws ec2 delete-internet-gateway \
    --internet-gateway-id `igw-1234567890abcdef` \
    --region `region-id``
   ```

   9. Delete the VPC.

   ```
   ``$` aws ec2 delete-vpc \
    --vpc-id `vpc-021345abcdef6789` \
    --region `region-id``
   ```

   10. Delete the secret that contains the `ReadOnlyUser` password.

   ```
   ``$` aws secretsmanager delete-secret \
    --secret-id arn:aws:secretsmanager:`region-id`:`123456789012`:secret:ADSecretPassword-`1234`" \
    --region `region-id``
   ```
