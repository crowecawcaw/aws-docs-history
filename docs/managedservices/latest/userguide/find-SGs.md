End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Find security group (SG) IDs, AMS

Amazon EC2 create and OpenSearch create domain CTs require a security group ID. This will be in the form
`sg-02ce123456e7893c7`. Your account has at least two default security groups; see [Security groups](about-security-groups.md "about-security-groups.md").
Additionally, you may have security groups that you created for specific purposes. To discover your security groups:

- AWS Console: Use the EC2 or VPC console to view all security groups for the selected VPC.
- API/CLI (when logged into your AMS account):

List your security groups:

```
aws ec2 describe-security-groups
```
