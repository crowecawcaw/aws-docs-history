# Creating an IAM role for a console user

Complete the following procedure if you are using the AWS Entity Resolution console.

###### To create an IAM role

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")) with your administrator
   account.
2. Under **Access management**, choose
   **Roles**.

You can use **Roles** to create short-term
credentials, which is recommended for increased security. You can also choose
**Users** to create long-term credentials. 3. Choose **Create role**. 4. In the **Create role** wizard, for **Trusted entity
type**, choose **AWS account**. 5. Keep the option **This account** selected, and then choose
**Next**. 6. For **Add permissions**, choose **Create
Policy**.

A new tab opens.

    1. Select the **JSON** tab, and then add policies
     depending on the abilities granted to the console user. AWS Entity Resolution offers
     the following managed policies based on common use cases:




    	* [AWS managed policy:
    	 AWSEntityResolutionConsoleFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-fullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-fullaccess")
    	* [AWS managed policy:
    	 AWSEntityResolutionConsoleReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-readonly "security-iam-awsmanpol.md#security-iam-awsmanpol-readonly")
    2. Choose **Next: Tags**, add tags (optional), and then
     choose **Next: Review**.
    3. For **Review policy**, enter a
     **Name** and **Description**, and
     review the **Summary**.
    4. Choose **Create policy**.


    You have created a policy for a collaboration member.
    5. Go back to your original tab and under **Add
     permissions**, enter the name of the policy that you just
     created. (You might need to reload the page.)
    6. Select the check box next to the name of the policy that you created,
     and then choose **Next**.

7. For **Name, review, and create**, enter the **Role
   name** and **Description**.
   1. Review **Select trusted entities**, enter the
      AWS account for the person or persons who will assume the role (if
      necessary).
   2. Review the permissions in **Add permissions**, and
      edit if necessary.
   3. Review the **Tags**, and add tags if
      necessary.
   4. Choose **Create role**.
