# Step 2. Create the AWS Service Catalog

product

To create an AWS Service Catalog product, follow the steps at [Creating
products](../../../servicecatalog/latest/adminguide/productmgmt-cloudresource.md "../../../servicecatalog/latest/adminguide/productmgmt-cloudresource.md") in the _AWS Service Catalog Administrator
Guide_. You'll add your account blueprint as a template when you
create the AWS Service Catalog product.

###### Important

As a result of HashiCorp's updated Terraform licensing, AWS Service Catalog changed support for
_Terraform Open Source_ products and provisioned products to a new product type, called
_External_. To learn more about how this change effects AFC, including how to update your existing account
blueprints to the External product type, review [Transition to External product type](af-customization-page.md#service-catalog-external-product-type "af-customization-page.md#service-catalog-external-product-type").

###### Summary of steps to create a blueprint

- Create or download an CloudFormation template or Terraform tar.gz configuration file that will become your account
  blueprint. Some template examples are given later in this section.
- Sign in to the AWS account where you store your Account Factory blueprints
  (sometimes called the hub account).
- Navigate to the AWS Service Catalog console. Choose **Product list**,
  and then choose **Upload new product**.
- In the **Product details** pane, enter details for your
  blueprint product, such as a name and description.
- Select **Use a template file** and then select
  **Choose file**. Select or paste the template or configuration file
  you've developed or downloaded for use as your blueprint.
- Choose **Create product** at the bottom of the console
  page.
  You can download an CloudFormation template from the AWS Service Catalog reference architecture
  repository. [One example from that repository helps set up a backup plan for your
  resources](https://github.com/aws-samples/aws-service-catalog-reference-architectures/blob/master/backup/backup-tagoptions.yml "https://github.com/aws-samples/aws-service-catalog-reference-architectures/blob/master/backup/backup-tagoptions.yml").

Here's an example template, for a fictitious company called **Best Pets**. It helps set up a connection to their pet
database.

```
Resources:
  ConnectionStringGeneratorLambdaRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - "sts:AssumeRole"
  ConnectionStringGeneratorLambda:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: !Join ['-', ['ConnectionStringGenerator', !Select [4, !Split ['-', !Select [2, !Split ['/', !Ref AWS::StackId]]]]]]
      Description: Retrieves the connection string for this account to access the Pet Database
      Role: !GetAtt ConnectionStringGeneratorLambdaRole.Arn
      Runtime: nodejs22.x
      Handler: index.handler
      Timeout: 5
      Code:
        ZipFile: >
           export const handler = async (event, context) => {
             const awsAccountId = context.invokedFunctionArn.split(“:”)[4]
             const connectionString= “fake connection for account ” + awsAccountId;
             const response = {
               statusCode: 200,
               body: connectionString
             };
           return response;
          };

  ConnectionString:
    Type: Custom::ConnectionStringGenerator
    Properties:
      ServiceToken: !GetAtt ConnectionStringGeneratorLambda.Arn

  PetDatabaseConnectionString:
    DependsOn: ConnectionString
    # For example purposes we're using SSM parameter store.
    # In your template, use secure alternatives to store
    # sensitive values such as connection strings.
    Type: AWS::SSM::Parameter
    Properties:
      Name: pet-database-connection-string
      Description: Connection information for the BestPets pet database
      Type: String
      Value: !GetAtt ConnectionString.Value

```
