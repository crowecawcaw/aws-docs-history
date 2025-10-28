# Deleting products using the AWS CLI

AWS Service Catalog allows you to use the [AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") (AWS CLI) to delete products from your portfolio. The AWS CLI is an open source tool that enables you to
interact with AWS services using commands in your command-line shell. The AWS Service Catalog force-delete function requires an
[AWS CLI alias](../../../cli/latest/userguide/cli-usage-alias.md "../../../cli/latest/userguide/cli-usage-alias.md"), which is
a shortcut you can create in the AWS CLI to shorten commands or scripts that you frequently use.

## Prerequisites

- Install and configure the AWS CLI. For more information, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Configuration basics](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md"). Use a minimum AWS CLI version of 1.11.24 or 2.0.0.
- The delete product CLI alias requires a bash-compatible terminal and the JQ command-line JSON processor.
  For more information about installing the Command-line JSON processor, see [Download jq](https://stedolan.github.io/jq/download/ "https://stedolan.github.io/jq/download/").
- Create a AWS CLI Alias to batch `Disassociation` API calls, enabling you to
  delete a product in a single command.

To successfully delete a product, you must disassociate all resources associated with the product first.
Examples of product resource associations include portfolio associations, budgets, Tag Options, and
Service Actions. When using the CLI to delete a product, the CLI `force-delete-product` alias enables
you to call the `Disassociate`
API to disassociate any resources that would prevent the `DeleteProduct` API. This avoids a seperate call for
individual disassociations.

###### Note

The file paths shown in the procedures below may vary depending on which operating system you use
to perform these actions.

## Creating an AWS CLI alias to delete AWS Service Catalog products

When using the AWS CLI to delete a AWS Service Catalog product, the CLI `force-delete-product` alias
enables you to call the
`Disassociate`
API to disassociate any resources that would prevent the `DeleteProduct` call.

###### Create an `alias` file in your AWS CLI configuration folder

1. In the AWS CLI console, navigate to the configuraiton folder. By default, the configuration folder
   path is `~/.aws/` on Linux and macOS, or `%USERPROFILE%\.aws\` on Windows.
2. Create a sub-folder named `cli` using file navigation or by entering the following
   command in your preferred terminal:

```

             $ mkdir -p ~/.aws/cli

```

The resulting `cli` folder default path is `~/.aws/cli/` on Linux and
MacOS, or `%USERPROFILE%\.aws\cli` on Windows. 3. In the new `cli` folder, create a text file named `alias` with no file
extension. You can
create the `alias` file using file navigation or by entering the following
command in your preferred terminal:

```

              $ touch ~/.aws/cli/alias

```

4. Enter `[toplevel]` on the first line.
5. Save the file.

Next, you can add the force-delete-product alias to your `alias` file by
manually pasting the alias script into the file,
or by using a command in the terminal window.

###### Manually add the force-delete-product alias to your `alias` file

1. In the AWS CLI console, navigate to your AWS CLI configuration folder and open the `alias`
   file.
2. Enter the following code alias into the file, below the `[toplevel]` line:

```

             [command servicecatalog]
          	 force-delete-product =
          	   !f() {
          	     if [ "$#" -ne 1 ]; then
          	         echo "Illegal number of parameters"
          	         exit 1
          	     fi

          	     if [[ "$1" != prod-* ]]; then
          	        echo "Please provide a valid product id."
          	        exit 1
          	     fi

          	     productId=$1
          	     describeProductAsAdminResponse=$(aws servicecatalog describe-product-as-admin --id $productId)
          	     listPortfoliosForProductResponse=$(aws servicecatalog list-portfolios-for-product --product-id $productId)

          	     tagOptions=$(echo "$describeProductAsAdminResponse" | jq -r '.TagOptions[].Id')
          	     budgetName=$(echo "$describeProductAsAdminResponse" | jq -r '.Budgets[].BudgetName')
          	     portfolios=$(echo "$listPortfoliosForProductResponse" | jq -r '.PortfolioDetails[].Id')
          	     provisioningArtifacts=$(echo "$describeProductAsAdminResponse" | jq -r '.ProvisioningArtifactSummaries[].Id')
          	     provisioningArtifactServiceActionAssociations=()

          	     for provisioningArtifactId in $provisioningArtifacts; do
          	       listServiceActionsForProvisioningArtifactResponse=$(aws servicecatalog list-service-actions-for-provisioning-artifact --product-id $productId --provisioning-artifact-id $provisioningArtifactId)
          	       serviceActions=$(echo "$listServiceActionsForProvisioningArtifactResponse" | jq -r '[.ServiceActionSummaries[].Id] | join(",")')
          	       if [[ -n "$serviceActions" ]]; then
          	         provisioningArtifactServiceActionAssociations+=("${provisioningArtifactId}:${serviceActions}")
          	       fi
          	     done

          	     echo "Before deleting a product, the following associated resources must be disassociated. These resources will not be deleted. This action may take some time, depending on the number of resources being disassociated."

          	     echo "Portfolios:"
          	     for portfolioId in $portfolios; do
          	       echo "\t${portfolioId}"
          	     done

          	     echo "Budgets:"
          	     if [[ -n "$budgetName" ]]; then
          	       echo "\t${budgetName}"
          	     fi

          	     echo "Tag Options:"
          	     for tagOptionId in $tagOptions; do
          	       echo "\t${tagOptionId}"
          	     done

          	     echo "Service Actions on Provisioning Artifact:"
          	     for association in "${provisioningArtifactServiceActionAssociations[@]}"; do
          	       echo "\t${association}"
          	     done

          	     read -p "Are you sure you want to delete ${productId}? y,n "
          	     if [[ ! $REPLY =~ ^[Yy]$ ]]; then
          	        exit
          	     fi

          	     for portfolioId in $portfolios; do
          	       echo "Disassociating ${portfolioId}"
          	       aws servicecatalog disassociate-product-from-portfolio --product-id $productId --portfolio-id $portfolioId
          	     done

          	     if [[ -n "$budgetName" ]]; then
          	       echo "Disassociating ${budgetName}"
          	       aws servicecatalog disassociate-budget-from-resource --budget-name "$budgetName" --resource-id $productId
          	     fi

          	     for tagOptionId in $tagOptions; do
          	       echo "Disassociating ${tagOptionId}"
          	       aws servicecatalog disassociate-tag-option-from-resource --tag-option-id $tagOptionId --resource-id $productId
          	     done

          	     for association in "${provisioningArtifactServiceActionAssociations[@]}"; do
          	       associationPair=(${association//:/ })
          	       provisioningArtifactId=${associationPair[0]}
          	       serviceActionsList=${associationPair[1]}
          	       serviceActionIds=${serviceActionsList//,/ }
          	       for serviceActionId in $serviceActionIds; do
          	         echo "Disassociating ${serviceActionId} from ${provisioningArtifactId}"
          	         aws servicecatalog disassociate-service-action-from-provisioning-artifact --product-id $productId --provisioning-artifact-id $provisioningArtifactId --service-action-id $serviceActionId
          	       done
          	     done

          	     echo "Deleting product ${productId}"
          	     aws servicecatalog delete-product --id $productId

          	   }; f

```

3. Save the file.

###### Use the terminal window to add the force-delete-product alias to your `alias` file

1. Open your terminal window and run the following command

`$ cat >> ~/.aws/cli/alias` 2. Paste the alias script to the terminal window, and then press _CTRL+D_ to exit the
`cat` command.

###### Call the force-delete-product alias

1. In your terminal window, run the following command to call the delete
   product alias

`$ aws servicecatalog force-delete-product {product-id}`

The example below shows the `force-delete-product` alias command and its
resulting response

```

              $ aws servicecatalog force-delete-product prod-123

```

```

              Before deleting a product, the following associated resources must be disassociated. These resources will not be deleted. This action may take some time, depending on the number of resources being disassociated.
              Portfolios:
                port-123
              Budgets:
                  budgetName
              Tag Options:
                  tag-123
              Service Actions on Provisioning Artifact:
                  pa-123:act-123
              Are you sure you want to delete prod-123? y,n

```

2. Enter `y` to confirm you want to delete the product.

After successfully deleting the product, the terminal window displays the following results

```

          Disassociating port-123
          Disassociating budgetName
          Disassociating tag-123
          Disassociating act-123 from pa-123
          Deleting product prod-123

```

## Additional resources

For more information about AWS CLI, using aliases, and deleting AWS Service Catalog products, review the following
resources:

- [Creating and using AWS CLI aliases](../../../cli/latest/userguide/cli-usage-alias.md "../../../cli/latest/userguide/cli-usage-alias.md") in the _AWS Command Line Interface (CLI)_ user guide.
- [AWS CLI alias repository](https://github.com/awslabs/awscli-aliases "https://github.com/awslabs/awscli-aliases") git
  repository.
- [Deleting AWS Service Catalog
  products](productmgmt-delete.md "productmgmt-delete.md").
- [AWS re:Invent 2016: The Effective
  AWS CLI User](https://youtu.be/Xc1dHtWa9-Q?t=1593 "https://youtu.be/Xc1dHtWa9-Q?t=1593") on _YouTube_.
