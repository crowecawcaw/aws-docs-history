

# Import a AWS Glue DataBrew recipe in AWS Glue Studio
<a name="glue-studio-data-preparation-import-recipe"></a>

 In AWS Glue DataBrew, a recipe is a set of data transformation steps. AWS Glue DataBrew recipes prescribes how to transform data that have already been read and doesn't describe where and how to read data, as well as how and where to write data. This is configured in Source and Target nodes in AWS Glue Studio. For more information on recipes, see [ Creating and using AWS Glue DataBrew recipes ](https://docs.aws.amazon.com/databrew/latest/dg/recipes.html). 

 To use AWS Glue DataBrew recipes in AWS Glue Studio, begin with creating recipes in AWS Glue DataBrew. If you have recipes you want to use, you can skip this step. 

## IAM permissions for AWS Glue DataBrew
<a name="glue-studio-databrew-permissions"></a>

 This topic provides information to help you understand the actions and resources that you an IAM administrator can use in an AWS Identity and Access Management (IAM) policy for the Data Preparation Recipe transform. 

 For additional information about security in AWS Glue, see [Access Management](https://docs.aws.amazon.com/glue/latest/dg/security.html). 

**Note**  
 The following table lists the permissions that a user needs if importing an existing AWS Glue DataBrew recipe. 


**Data Preparation Recipe transform actions**  

| Action | Description | 
| --- | --- | 
| databrew:ListRecipes | Grants permission to retrieve AWS Glue DataBrew recipes. | 
| databrew:ListRecipeVersions | Grants permission to retrieve AWS Glue DataBrew recipe versions. | 
| databrew:DescribeRecipe | Grants permission to retrieve AWS Glue DataBrew recipe description. | 



 The role you’re using for accessing this functionality should have a policy that allows several AWS Glue DataBrew actions. You can achieve this by either using the `AWSGlueConsoleFullAccess` policy that includes the necessary actions or add the following inline policy to your role: 

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
        "databrew:ListRecipes",
        "databrew:ListRecipeVersions",
        "databrew:DescribeRecipe"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

------



 To use the Data Preparation Recipe transform, you must add the `IAM:PassRole` action to the permissions policy. 


**Additional required permissions**  

| Action | Description | 
| --- | --- | 
| iam:PassRole | Grants permission for IAM to allow the user to pass the approved roles. | 

Without these permissions the following error occurs:

```
"errorCode": "AccessDenied"
"errorMessage": "User: arn:aws:sts::account_id:assumed-role/AWSGlueServiceRole is not 
authorized to perform: iam:PassRole on resource: arn:aws:iam::account_id:role/service-role/AWSGlueServiceRole 
because no identity-based policy allows the iam:PassRole action"
```



## Importing an AWS Glue DataBrew recipe
<a name="glue-studio-databrew-import-steps"></a>

**To import an AWS Glue DataBrew recipe and use in AWS Glue Studio:**

 If you have an existing **Data Preparation Recipe** node and you want to edit the recipe steps directly in AWS Glue Studio, you will have to import the recipe steps into your AWS Glue Studio job. 

1.  Start a AWS Glue job in AWS Glue Studio with a datasource. 

1.  Add the **Data Preparation Recipe** node to the job canvas.   
![The screenshot shows the Add node modal with data preparation recipe available for selection.](http://docs.aws.amazon.com/glue/latest/dg/images/glue-add-node-data-preparation-recipe.png)

1.  In the Transform panel, enter a name for your recipe. 

1.  Choose one or more parent nodes by selecting the available nodes on the canvas from the drop-down list. 

1.  Choose **Author Recipe**. If **Author Recipe** is grey it is unavailable until node parents have been selected and a data preview session has finished.   
![Author Recipe interface showing Name field, Node parents dropdown, and Plans S3 DataSource selected.](http://docs.aws.amazon.com/glue/latest/dg/images/glue-author-data-preparation-recipe.png)

1.  The data frame loads and shows you detailed information about your source data. 

    Select the **more actions** icon and choose **Import recipe**.   
![Import recipe option displayed in dropdown menu next to Recipe heading.](http://docs.aws.amazon.com/glue/latest/dg/images/glue-dataframe-import-recipe.png)

1.  Use the Import recipe wizard to complete the steps. In step 1, search for your recipe, select it, and choose **Next**.   
![Import recipe wizard showing step 1 with Populations Sample Project-recipe selected from list.](http://docs.aws.amazon.com/glue/latest/dg/images/import-recipe-step-1.png)

1.  In step 2, choose your import options. You can choose to Append a new recipe to an existing recipe or Overwrite an existing recipe. Choose **Next**.   
![Import options step showing Append and Overwrite radio buttons with imported recipe steps listed.](http://docs.aws.amazon.com/glue/latest/dg/images/import-recipe-step-2.png)

1.  In step 3, validate the recipe steps. Once you import your AWS Glue DataBrew recipe, you can edit this recipe directly in AWS Glue Studio.   
![Validating steps progress indicator showing 0 of 2 steps validated in Step 3 interface.](http://docs.aws.amazon.com/glue/latest/dg/images/import-recipe-step-3.png)  
![Step 3 validation screen showing all recipe steps validated with a green checkmark.](http://docs.aws.amazon.com/glue/latest/dg/images/import-recipe-step-3-validated-2.png)

1.  After this, the steps will be imported as part of your AWS Glue job. Make necessary configuration changes in the **Job details** tab, like naming your job and adjusting allocated capacity as needed. Choose **Save** to save your job and recipe. 
**Note**  
 JOIN, UNION, GROUP\_BY, PIVOT, UNPIVOT, TRANSPOSE are not supported for recipe import, nor will they be available in recipe authoring mode. 

1.  Optionally, you can finish authoring the job by adding other transformations nodes as needed and add Data target node(s). 

    If you reorder steps after you import a recipe, AWS Glue performs validation on those steps. For example, if you renamed and then deleted a column, and you moved the delete step on top, then the rename step would be invalid. You can then edit the steps to fix the validation error. 