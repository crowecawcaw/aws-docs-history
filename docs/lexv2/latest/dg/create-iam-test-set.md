

# Create an IAM role for the Test Workbench
<a name="create-iam-test-set"></a>

**To create an IAM role for the Test Workbench**

1. Follow the steps at [ Create an IAM user](https://docs.aws.amazon.com/lexv2/latest/dg/gs-account.html#gs-account-user) to create an IAM user which can be used to access test-workbench console.

1. Select the **Create role** button.   
![The roles screen in the IAM console.](http://docs.aws.amazon.com/lexv2/latest/dg/images/testworkbench/testworkbench-iam1.png)

1. Select the option for **Custom trust policy**.   
![Select trusted entity](http://docs.aws.amazon.com/lexv2/latest/dg/images/testworkbench/testworkbench-iam2.png)

1. Enter the trust policy below and click **Next**. 

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "sid4",
         "Effect": "Allow",
         "Principal": {
           "Service": "lexv2.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

1. Select the **Create policy** button. 

1. A new tab will open in your browser where you can enter the below policy and click on **Next: Tags** button. 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "s3:*"
               ],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "logs:FilterLogEvents"
               ],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "lex:*"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Enter a policy name, for example ‘LexTestWorkbenchPolicy’ and then click on the **Create Policy**. 

1. Return to the previous tab in your browser and Refresh list of policies by clicking the **Refresh** button as shown below.   
![Refresh the screen to see the new policy.](http://docs.aws.amazon.com/lexv2/latest/dg/images/testworkbench/testworkbench-iam3.png)

1. Search in list of policies by entering policy name that you used in the 6th step and choose the policy. 

1. Select the **Next** button. 

1. Enter role name and then click the **Create Role** button. 

1. Choose your new IAM role when prompted in the Amazon Lex V2 console for Test Workbench. 