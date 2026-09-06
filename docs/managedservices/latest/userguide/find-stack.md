

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Find stack IDs in AMS
<a name="find-stack"></a>

To find a Stack ID, you can use either the Amazon EC2 console, AMS console, or the AMS SKMS API/CLI.

AMS Console:
+ In the navigation pane, select **RFCs**, and then click the RFC that created the stack. Use the filter option at the top to reduce the list. The RFC details page opens and includes the run output with the stack ID.
+ Alternatively, you can select **Stacks in the navigation pane** to open the stacks list page, and then page through the stack list to the stack you're interested in. This method is more useful if you know the subject of the stack you are looking for.

Amazon EC2 Console:

In the navigation pane, select **Instances** or **Load Balancers** or **Auto Scaling Groups**.

AMS SKMS API ListStackSummaries or CLI:
**Note**  
The AMS CLI must be installed for these commands to work. To install the AMS API or CLI, go to the AMS console **Developers Resources** page. For reference material on the AMS CM API or AMS SKMS API, see the AMS Information Resources section in the User Guide. You may need to add a `--profile` option for authentication; for example, `aws amsskms {{ams-cli-command}} --profile SAML`. You may also need to add the `--region` option as all AMS commands run out of us-east-1; for example `aws amscm {{ams-cli-command}} --region=us-east-1`.
**Note**  
The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1` when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.

To view a list of stacks in the current account, run the ListStackSummaries operation of the SKMS API (CLI: `list-stack-summaries`). To get complete information about a particular stack instance, by StackId, run GetStack.
+ In the following examples, the first command requests a list of summaries for all stack instances in the account. The second command requests the list of stack instances, with a query filter to list only those of a specific stack template, and output the VpcId, Name, and StackId. 

  ```
  aws amsskms list-stack-summaries --output table
  ```

  ```
  --------------------------------------------------------------------
  |                                    ListStackSummaries            |
  |                                     StackSummaries               |   
  +------------+----------------------+---------------------+--------+
  |   VpcId    |         StackId      |  StackTemplateId    |  Name  | 
  +------------+----------------------+---------------------+--------+
  |vpc-0123abcd|stack-1fb7fe2212345678|stm-sdhopvbb123456789|Test ELB|  
  |vpc-0123abcd|stack-8323cc0e12345678|stm-s2b72beb123456789|S3 store| 
  |vpc-0123abcd|stack-2309fa0712345678|stm-sdhopvbb123456789|ELB     |  
  |vpc-0123abcd|stack-5e61a70512345678|stm-sdpabqbb123456789|PatchSim|  
  |vpc-0123abcd|stack-bd0e080d12345678|stm-s2b72beb123456789|CLI demo|   
  +------------+----------------------+---------------------+--------+
  ```

For information about using CLI queries, see [ How to Filter the Output with the --query Option](https://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html#controlling-output-filter) and the query language reference, [JMESPath Specification](http://jmespath.org/specification.html)..

**Note**  
For information on using instance IDs for access, see also [Accessing instances using bastions](using-bastions.md).