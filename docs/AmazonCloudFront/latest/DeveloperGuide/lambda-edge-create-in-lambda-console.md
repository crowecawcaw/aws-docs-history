# Create a Lambda@Edge
 function

To set up AWS Lambda to run Lambda functions that are based on CloudFront events, follow
 this procedure.

###### To create a Lambda@Edge
 function

1. Sign in to the AWS Management Console and open the AWS Lambda console at
 [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. If you already have one or more Lambda functions, choose **Create
 function**.


If you've don't have any functions, choose **Get Started
 Now**.
3. In the Region list at the top of the page, choose
 **US East (N. Virginia)**.
4. Create a function using your own code or create a function starting with a
 CloudFront blueprint.




	* To create a function using your own code, choose **Author
	 from scratch**.
	* To display a list of blueprints for CloudFront, enter
	 **cloudfront** in the filter field, and then
	 choose **Enter**.
	
	
	If you find a blueprint that you want to use, choose the name of
	 the blueprint.
5. In the **Basic information** section, specify the
 following values:


	1. **Name** – Enter a name for your
	 function.
	2. **Role** – To get started quickly, choose
	 **Create new role from template(s)**. You can
	 also choose **Choose an existing role** or
	 **Create a custom role**, and then follow the
	 prompts to complete the information for this section.
	3. **Role name** – Enter a name for the
	 role.
	4. **Policy templates** – Choose
	 **Basic Edge Lambda permissions**.
6. If you chose **Author from scratch** in step 4, skip to
 step 7.


If you chose a blueprint in step 4, the **cloudfront**
 section lets you create one trigger, which associates this function with a
 cache in a CloudFront distribution and a CloudFront event. We recommend that you choose
 **Remove** at this point, so there isn't a trigger for
 the function when it's created. Then you can add triggers later. 


###### Tip

We recommend that you test and debug the function before adding
 triggers. If you add a trigger now, the function will run as soon as you
 create the function and it finishes replicating to AWS locations
 around the world, and the corresponding distribution is deployed.
7. Choose **Create function**.


Lambda creates two versions of your function: $LATEST and Version 1. You
 can edit only the $LATEST version, but the console initially displays
 Version 1.
8. To edit the function, choose **Version 1** near the top
 of the page, under the ARN for the function. Then, on the
 **Versions** tab, choose **$LATEST**.
 (If you left the function and then returned to it, the button label is
 **Qualifiers**.)
9. On the **Configuration** tab, choose the applicable
 **Code entry type**. Then follow the prompts to edit or
 upload your code.
10. For **Runtime**, choose the value based on your
 function's code.
11. In the **Tags** section, add any applicable tags.
12. Choose **Actions**, and then choose **Publish new
 version**.
13. Enter a description for the new version of the function.
14. Choose **Publish**.
15. Test and debug the function. For more information about testing in the
 Lambda console, see [Invoke a Lambda function using the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html#get-started-invoke-manually "https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html#get-started-invoke-manually") in the
 *AWS Lambda Developer Guide*.
16. When you're ready to have the function execute for CloudFront events, publish
 another version and edit the function to add triggers. For more information,
 see [Add triggers for a Lambda@Edge
 function](lambda-edge-add-triggers.md "lambda-edge-add-triggers.md").
