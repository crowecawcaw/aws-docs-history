

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with container-based products using the AWS Marketplace APIs
<a name="work-with-container-products"></a>

You can use the AWS Marketplace Catalog API to automate tasks for working with container-based products. 

For information about creating a container-based product using the Catalog API, see [Create a product](work-with-seller-products.md#create-product).

The following topics describe how to use the Catalog API to perform actions on your container-based products:

**Topics**
+ [Add a new version](#container-add-version)
+ [Update the visibility for an Amazon EKS add-on](#update-delivery-option-visibility)
+ [Create repositories and resources](#container-repos)
+ [Update version information](#container-update-version)
+ [Restrict a version](#container-restrict-version)

## Add a new version
<a name="container-add-version"></a>

If you already have a container-based product in AWS Marketplace, you can use the AWS Marketplace Catalog API to add a new version. This requires that you have already created repositories in AWS Marketplace for each container image or artifact that is part of your product, and that you can copy them from your local Docker and Helm files.

**Note**  
For details about creating a container-based product using the AWS Marketplace Management Portal, see [Getting started with container products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html) in the *AWS Marketplace Seller Guide*.  
For details about adding a new version, including creating repositories and building Docker and Helm files into those repositories, by using the AWS Marketplace Management Portal, see [Add a new version of your product](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#container-add-version) in the *AWS Marketplace Seller Guide*.  
If you have not already created new repositories, you can create them using the Catalog API, see [Create repositories and resources](#container-repos).

To add a new version, call the `StartChangeSet` API operation with the `AddDeliveryOptions` change type, as shown in the following example.

**Note**  
A version of a container-based product is made up of one or more delivery options. For example, you might have two delivery options, one that works with a noSQL database, and another that works with MySQL, so that your users can choose how they want to work with your product. You create the version of your product and add multiple delivery options in a single request with `AddDeliveryOptions`.

**Container Image Delivery Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "AddDeliveryOptions",
      "Entity":
      {
        "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12}}",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "Version":
        {
          "VersionTitle": "1.1",
          "ReleaseNotes": "{{Minor bug fix}}"
        },
        "DeliveryOptions":
        [
          {
            "DeliveryOptionTitle": "{{EKS Container image only delivery option}}",
            "Details":
            {
              "EcrDeliveryOptionDetails":
              {
                "ContainerImages":
                [
                  "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                ],
                "DeploymentResources":
                [
                  {
                    "Name": "HelmDeploymentTemplate",
                    "Url": "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
                  }
                ],
                "CompatibleServices":
                [
                  "EKS"
                ],
                "Description": "Sample Description",
                "UsageInstructions": "helm pull {{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
              }
            }
          }      
        ]
      }
    }
  ]
}
```

**Amazon Bedrock AgentCore Runtime delivery request syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "AddDeliveryOptions",
      "Entity":
      {
        "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12}}",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "Version":
        {
          "VersionTitle": "{{1.1}}",
          "ReleaseNotes": "{{Minor bug fix}}"
        },
        "DeliveryOptions":
        [
          {
            "DeliveryOptionTitle": "{{Amazon Bedrock AgentCore Runtime Delivery Option}}",
            "Details":
            {
              "EcrDeliveryOptionDetails":
              {
                "ContainerImages":
                [
                  "{{111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1}}"
                ],
                "CompatibleServices":
                [
                  "Bedrock-AgentCore"
                ],
                "AgenticType":
                [
                  "{{AGENT}}" 
                ], 
                "Description": "{{Sample Description}}",
                "UsageInstructions": "{{To launch and invoke this agent on Amazon Bedrock AgentCore Runtime}}",
                "EnvironmentVariables":
                [
                  {
                    "Name": "{{HTTP_PORT}}",
                    "Description": "{{Port of the server}}",
                    "DefaultValue": "{{8080}}"
                  },
                  {
                    "Name": "{{API_KEY}}",
                    "Description": "{{Provide your unique API key here.}}"
                  }
                ]
              }
            }
          }      
        ]
      }
    }
  ]
}
```

**Helm Chart Delivery Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "AddDeliveryOptions",
      "Entity":
      {
        "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12}}",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "Version":
        {
          "VersionTitle": "1.1",
          "ReleaseNotes": "{{Minor bug fix}}"
        },
        "DeliveryOptions":
        [
          {
            "DeliveryOptionTitle": "{{HelmChartDeliveryOption}}",
            "Details":
            {
              "HelmDeliveryOptionDetails":
              {
                "CompatibleServices":
                [
                  "EKS",
                  "EKS-Anywhere"
                ],
                "ContainerImages":
                [
                  "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                ],
                "HelmChartUri": "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1",
                "Description": "{{Helm chart description}}",
                "UsageInstructions": "{{Usage instructions}}",
                "MarketplaceServiceAccountName": "{{Service account name}}",
                "ReleaseName": "{{Optional release name}}",
                "Namespace": "{{Optional Kubernetes namespace}}",
                "OverrideParameters":
                [
                  {
                    "Key": "{{HelmKeyName1}}",
                    "DefaultValue": "${{{AWSMP_LICENSE_SECRET}}}"
                  },
                  {
                    "Key": "{{HelmKeyName2}}",
                    "DefaultValue": "${{{AWSMP_SERVICE_ACCOUNT}}}"
                  }
                ]
              }
            }
          }
        ]
      }
    }
  ]
}
```

**Amazon EKS Add-On Delivery Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json
{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "AddDeliveryOptions",
      "Entity": {
        "Type": "ContainerProduct@1.0",
        "Identifier": "$CreateProductChange.Entity.Identifier"
      },
      "DetailsDocument": {
        "Version": {
          "VersionTitle": "1.1",
          "ReleaseNotes": "{{New Add-on Release}}"
        },
        "DeliveryOptions": [
          {
            "DeliveryOptionTitle": "{{AWS Marketplace Test AddOn from CAPI 1}}",
            "Visibility": "Limited",
            "Details": {
              "EksAddOnDeliveryOptionDetails": {
                "ContainerImages": [
                  "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/test-seller/canary-test-repo-product-6:mongo"
                ],
                "HelmChartUri": "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/rocket/rocket-product-helm:1.0",
                "Description": "{{Description for delivery option provided by ISV}}",
                "UsageInstructions": "{{Usage instructions with launch instructions}}",
                "AddOnName": "{{aws-mp-test}}",
                "AddOnVersion": "{{1.2.1}}",
                "AddOnType": "networking",
                "CompatibleKubernetesVersions": [
                  "1.25",
                  "1.26"
                ],
                "SupportedArchitectures": [
                  "amd64",
                  "arm64"
                ],
                "Namespace": "{{my-test-namespace}}",
                "EnvironmentOverrideParameters": [
                  {
                    "Key": "cluster-name",
                    "Value": "${{{AWS_EKS_CLUSTER_NAME}}}"
                  },
                  {
                    "Key": "region-name",
                    "Value": "${{{AWS_REGION}}}"
                  }
                ]
              }
            }
          }
        ]
      },
      "ChangeName": "{{PublishAddonNew}}"
    }
  ]
}
```

Provide information for the fields to add the `AddDeliveryOptions` change type:
+ `Entity` (object) (required) – Your container-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `ContainerProduct@1.0`. 
+ `DetailsDocument` (object) (required) – Details of the request. It includes all the information about the version that you are adding. This field is a string field.
  + `Version` (object) – Details about the version that you are adding to your product.
    + `VersionTitle` (string) – The title of the version that you are creating. Typically this is a description of the version, like **Version 1.1** or simply **1.1**. Your buyers will be able to choose the version to deploy from a list of version titles.
    + `ReleaseNotes` (string) – The detailed notes about this version. Must be less than 30,000 characters.
  + `DeliveryOptions` (array of objects) – An array of delivery options, where each is a method of delivery for your product version. For example, if you have one delivery option for Amazon Elastic Container Service (Amazon ECS) and another for Amazon Elastic Kubernetes Service (Amazon EKS), you must have two delivery options.
    + `DeliveryOptionTitle` (string) – A short description that helps your buyer to choose between your delivery options.
    + `Details` (object) – The resources used for this delivery option. This is a details field within the details field. You do not need to doubly escape characters in this field.
      + `AddOnName – `A unique add-on name that buyers will see in the Amazon EKS catalog. This name will add a prefix later using `SellerAlias`. For example, where `isv-alias_` is the ISV provided add-on name.
      + `AddOnType – `The type of add-on chosen from a list of supported values from Amazon EKS: Gitops \| monitoring \| logging \| cert-management \| policy-management \| cost-management \| autoscaling \| storage \| kubernetes-management \| service-mesh \| etcd-backup \| ingress-service-type \| load-balancer \| local-registry\| networking \| Security \| backup \| ingress-controller \| observability
      + `AddOnVersion – `A semantic version so that buyer can choose a specific version of AddOn they need to install or upgrade.
      + `CompatibleKubernetesVersions` – The Amazon EKS Kubernetes versions that this software is compatible with.
      + `CompatibleServices` (array of strings) – An array of services that the release is compatible with. Valid options: `ECS`, `EKS`, `ECS-Anywhere`, `EKS-Anywhere`, and `Bedrock-AgentCore`.
      + `ContainerImages` (array of strings) – An array of container image URLs used by this version. The path will be the repository that you have uploaded the image to, with the tag for the image used by this version. The list must include all needed images, even images that have not changed from previous versions. See the next section for information about creating repositories using the Catalog API.
      + `Description` (string) – A longer description of the delivery option to give details to your buyer. You can also include a link to more instructions provided elsewhere.
      + `EcrDeliveryOptionDetails` – `AgenticType` – The type of runtime agent. Valid options: `AGENT`, `MCP_SERVER`, or `A2A_SERVER`.
      + `EcrDeliveryOptionDetails` – `EnvironmentVariables` – List of environment variables that are required by the AgentCore Runtime container and that will be pre-populated for buyers upon deployment. For each variable, provide an object with the *name* as expected by your container, a *description*, and an optional *defaultValue*. For variables such as credentials or API keys that are unique, do not provide a default value. You can use the description to specify details about the variable as well as possible values. All of the provided variables with their default values will be pre-populated when buyers launch your product.
      + `EcrDeliveryOptionDetails – ``DeploymentResources (array of objects)` – An array of other resources needed for the version, such as Helm charts. Each resource includes a `Name` to describe it, and a `URL` that points at the resource.
      + `EnvironmentOverrideParameters – `List of system parameters to be used by the add-on. Some of the ISV provided AddOn (HelmChart) might require configurations with information derived from the Amazon EKS execution environment state (/system information). For example, `EksClusterRegion`, `EKSClusterName`, and others. You can avoid additional actions from Buyer by dynamically substituting these values at Amazon EKS AddOn launch. Amazon EKS System already supports automatic substitutions of system param for add-ons. AWS Marketplace ISV experience can be extended to collect this params which would require substitution.

        The generic system information to be substituted can be indicated by providing a AWS Marketplace specified constant following convention similar to Helm substitution. The supported values are `${AWS_REGION}` and `${AWS_EKS_CLUSTER_NAME}`.

        ```
         "EnvironmentOverrideParameters" : [ {
           "Key" : "my-field.region"
           "Value" : "${{{AWS_REGION}}}"
           },
           {
           "Key" : "my-second-field"
           "Value" : "${{{AWS_EKS_CLUSTER_NAME}}}"
           },
        ```
      + `HelmDeliveryOptionDetails` – `HelmChartUri (string)` – The URL to the Helm chart hosted in Amazon ECR that the buyer will install to launch the software.
      + `HelmDeliveryOptionDetails – ``MarketplaceServiceAccountName (string)` – *Optional * – The name of the Kubernetes service account. The service account will be used to connect to AWS Identity and Access Management (IAM) for permissions to call AWS services.
      + `HelmDeliveryOptionDetails – ``ReleaseName (string)` – *Optional * – The name for the Helm release provided to the `helm install` command that buyers use to launch the software. If not included, Helm will provide an automatically generated release name for you.
      + `HelmDeliveryOptionDetails – ``Namespace (string)` – *Optional * – The Kubernetes namespace where the Helm chart will be installed.
      + `HelmDeliveryOptionDetails – ``OverrideParameters (array of objects)` – Parameters that will be used in the Helm commands that launch the application. Buyers can override the default values.
**Note**  
For Amazon EKS Anywhere products, provide at least 1 override parameter for the license secret. Provide `DefaultValue` of `"${AWSMP_LICENSE_SECRET}"`.  
For paid products, provide at least 1 override parameter for service account configuration. Provide `DefaultValue` of `"${AWSMP_SERVICE_ACCOUNT}"`.
        + `Key` (string) – The key for the parameter in dot notation (override.example.key).
        + `DefaultValue` (string) – The default value for this override parameter.
      + `Namespace – `The ISV provided namespace for add-on installation.
      + `SupportedArchitectures – `The list of supported architectures, like amd64 and arm64.
      + `UsageInstructions` (string) – Provide instructions about the usage for this delivery option. Can be up to 4,000 characters.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed, including scanning the container images and other information to ensure that it meets the [AWS Marketplace guidelines for container products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-policies.html). This process can take a few minutes to hours, depending on the number and size of your containers. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets). For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors).

**Asynchronous Errors**

The following errors are specific to `AddDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT\_STATUS | Use an existing limited or public product. | 
| INCOMPATIBLE\_SERVICES | The service list contains incompatible services. [incompatible\_services] Provide a valid list of compatible services. | 
| NO\_SERVICE\_SPECIFIED | Provide at least 1 compatible service.  | 
| DUPLICATE\_COMPATIBLE\_AWS\_SERVICES | The service list contains duplicate entries. Remove them. Each entry must be unique.  | 
| INVALID\_VERSION\_TITLE | Remove spaces before the trademark symbol.  | 
| INVALID\_VERSION\_TITLE | Remove the following unsupported characters: [x, y, z]  | 
| INVALID\_VERSION\_TITLE | Remove spaces from the beginning of the version title.  | 
| INVALID\_VERSION\_TITLE | Provide version title with fewer than [x] characters.  | 
| DUPLICATE\_VERSION\_TITLE | The version title [duplicate\_version\_title] is a duplicate. Remove or change the title. | 
| INVALID\_RELEASE\_NOTES | Remove spaces before the trademark symbol.  | 
| INVALID\_RELEASE\_NOTES | Remove unsupported characters: [x, y, z]  | 
| INVALID\_RELEASE\_NOTES | Remove spaces from the beginning of release notes.  | 
| INVALID\_RELEASE\_NOTES | Provide release notes with fewer than (x) characters.  | 
| INVALID\_USAGE\_INSTRUCTIONS | Remove spaces before the trademark symbol.  | 
| INVALID\_USAGE\_INSTRUCTIONS | Remove unsupported characters: [x, y, z]  | 
| INVALID\_USAGE\_INSTRUCTIONS | Provide usage instructions with fewer than (x) characters. | 
| INVALID\_USAGE\_INSTRUCTIONS | Provide usage instructions.  | 
| MISSING\_CONTAINER\_IMAGES | Provide at least 1 container image.  | 
| NO\_LICENSE\_SECRET\_KEYS | For Amazon EKS Anywhere products, provide 1 override parameter for license secret. Needs DefaultValue of "${AWSMP\_LICENSE\_SECRET}", see example in section.  | 
| TOO\_MANY\_CONTAINER\_IMAGES | Provide fewer than 50 container images.  | 
| DUPLICATE\_CONTAINER\_IMAGES | The container image list contains duplicate images: [duplicate\_images]. Provide a list with unique images.  | 
| INVALID\_CONTAINER\_IMAGES | Provide a valid URI for the container image.  | 
| INVALID\_CONTAINER\_IMAGE\_URI | The image [invalid\_image\_uri] doesn't have access to this product. Upload the image to its corresponding product repository. For information about uploading, see [Getting started with container products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html). | 
| INVALID\_CONTAINER\_IMAGE\_TAG | Avoid using 'latest' tag.  | 
| DUPLICATE\_DELIVERY\_OPTION\_TITLES | Duplicate delivery option titles: [duplicate\_titles]. Remove the duplicates | 
| INVALID\_DELIVERY\_OPTION\_TITLES | The delivery option titles [existing\_titles] already exist. Provide a different title. | 
| INVALID\_FULFILLMENT\_OPTION\_TITLE | Provide delivery option title with fewer than (x) characters.  | 
| NO\_SERVICE\_ACCOUNT\_CONFIGURATION | For paid products, provide 1 override parameter for service account configuration. Needs DefaultValue of "${AWSMP\_SERVICE\_ACCOUNT}", see example in section.  | 
| INVALID\_DETAILS  | Provided Details is not valid. | 
| EMPTY\_RESOURCE\_NAME | Provide resource name.  | 
| EMPTY\_RESOURCE\_URL | Provide resource URL.  | 
| INVALID\_RESOURCE\_NAME | Provide resource name with fewer than 256 characters.  | 
| INVALID\_RESOURCE\_URL | Provide resource URL with fewer than 256 characters.  | 
| INVALID\_SHORT\_DESCRIPTION | Provide a short description with fewer than 1,000 characters.  | 
| INVALID\_SHORT\_DESCRIPTION | Provide short description.  | 
| SCAN\_ERROR | Fix security vulnerability ""[y]"" on Image ""[x]"".  | 
| IMAGE\_NOT\_FOUND | The public image URI [invalid\_image\_uri] is invalid. Provide a valid URI. | 
| INVALID\_ARN | Provide a valid ARN for image access.  | 
| IMAGE\_INACCESSIBLE | Provide a valid ARN for image access.  | 
| DUPLICATE\_ADDON\_NAME | The AddOn name you provided is already in use by a different product. Provide a different name.  | 
| DUPLICATE\_ADDON\_VERSION | The add-on version title [duplicate\_version\_title] is already in use. Provide a different title. | 
| INVALID\_ADDON\_TYPE | The add-on types [invalid\_types] are invalid. Provide a type from the supported list: [eks\_addon\_do\_supported\_types]. | 
| INVALID\_KUBERNETES\_VERSION | The Kubernetes versions [invalid\_versions] are invalid. Provide versions from the supported list: [eks\_addon\_do\_supported\_kubernetes\_versions]. | 
| DUPLICATE\_KUBERNETES\_VERSIONS | Duplicate Kubernetes versions: [duplicate\_versions]. Provide a list with unique versions. | 
| INVALID\_ARCHITECTURE | The architectures [invalid\_architectures] are invalid. Provide architectures from the Amazon EKS supported architectures : [eks\_addon\_do\_supported\_architectures]. | 
| DUPLICATE\_SUPPORTED\_ARCHITECTURES | Duplicate architectures: [duplicate\_architectures]. Provide a list of unique, supported architectures. | 
| INVALID\_VISIBILITY\_STATE | The states [invalid\_states] are invalid for the {EKS\_DO} delivery option. Provide a valid visibility state from the following allowed values: Limited. | 
| INVALID\_ENVIRONMENT\_OVERRIDE\_PARAMETER\_VALUE | The override parameter values [invalid\_values] are invalid. Provide a valid value from the following list: [eks\_addon\_do\_environment\_override\_parameter\_values]. | 
| DUPLICATE\_ENVIRONMENT\_OVERRIDE\_PARAMETER\_KEY | The environment override parameters contain duplicate keys: [duplicate\_keys]. Remove them. | 
| TOO\_MANY\_EKS\_ADDON\_DELIVERY\_OPTIONS | Provide only one Amazon EKS add-on delivery option for the version.  | 
| INCOMPATIBLE\_ADDON\_NAME | The add-on name [provided\_name] does not match the existing name. Reuse the existing name from the public version, or previous versions, of this add-on. You can only use one add-on name for each product. | 
| INCOMPATIBLE\_ADDON\_TYPE | The add-on type [provided\_type] does not match the existing type. Reuse the existing type from the public version, or previous versions, of this add-on. You can only use one add-on type for each product. | 
| INCOMPATIBLE\_ADDON\_NAMESPACE | The add-on namespace [provided\_namespace] does not match the existing namespace . Reuse the existing namespace from the public version, or previous versions, of this add-on. You can only use one add-on namespace for each product. | 
| INVALID\_HELM\_CHART\_URI | The Helm chart URI [invalid\_uri] is invalid. Provide a URI in the SemVer 2 format. | 
| INCOMPATIBLE\_HELM\_OBJECTS(INVALID\_HELM\_OBJECTS) | Provide a Helm chart without using the following unsupported Helm Objects: <unsupported-objects>.  | 
| INVALID\_DEPENDENT\_HELM\_CHARTS | Provide a Helm chart that contains the following dependent charts directly in the parent chart directory and not externally sourced: <invalid-subcharts>.  | 
| INVALID\_HELM\_SENSITIVE\_CONFIG | Provide an advanced configuration schema without sensitive information or secrets. Keywords: <sensitive-parameters-identified>  | 
| INVALID\_HELM\_UNDECLARED\_IMAGES | Provide the following Helm chart images within the delivery option of the request: <list-of-images>.  | 
| INVALID\_HELM\_CHART\_IMAGES | Provide a Helm chart containing images within repositories created via the AddRepositories change type. External images: <images-identified>.  | 
| INVALID\_HELM\_LINT | Provide a Helm chart that successfully passes Helm lint.  | 
| INVALID\_HELM\_TEMPLATE | Provide a Helm chart that successfully passes Helm template.  | 
| INVALID\_HELM\_CHART | Provide a Helm chart that adheres to AWS Marketplace guidance identified in [Helm Charts bulleted list](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-policies.html) in the AWS Marketplace Seller Guide.  | 
| INVALID\_ADDON\_NAME | Provide an AddOn name that follows the following regex pattern: xx  | 
| INVALID\_ADDON\_NAMESPACE | The namespace values [invalid\_namespaces] are invalid. The namespace must follow the  {EKS\_ADD\_ON\_NAMESPACE\_REGEX} regular expression. For example, namespace, namespace-test. | 
| INVALID\_ADDON\_NAME\_PATTERN | Provide an add-on name that starts with a letter or digit, and then a combination of letters, digits, and hyphens. For example, test-addon, eksaddon  | 
| INVALID\_ADDON\_VERSION\_PATTERN | Provide an add-on version using the following pattern: "<major>.<minor>.<patch>" (for example, 1.2.3, 0.1.2, 0.1.1)  | 
| EMPTY\_DELIVERY\_OPTION\_IDS | Provide a list of delivery option IDs.  | 
| INVALID\_DELIVERY\_OPTIONS\_INPUT | The list contains one or more invalid delivery options. Provide a valid list, and ensure that each option has a single delivery method. | 
| OVERRIDE\_PARAMETER\_KEYS\_CONTAINS\_SPECIAL\_CHARS | The override parameter keys [invalid\_keys] contain invalid characters. You keys must use only letters, numbers, double quotes (" ") and plus signs (\+). | 
| INVALID\_CONTAINER\_IMAGE\_REPOSITORY | The repositories [invalid\_repositories] are invalid. Provide repositories created through the AddRepositories change type. | 
| INVALID\_CONTAINER\_IMAGE\_TAG\_FORMAT | The container image tag [invalid\_image\_tag] is invalid. Provide a tag conforming to the {CONTAINER\_IMAGE\_TAG\_REGEX} regular expression. | 
| DUPLICATE\_OVERRIDE\_PARAMETER\_KEYS | The override parameters contain duplicate keys [duplicate\_keys]. Remove the duplicates. | 
| UNSUPPORTED\_CONTAINER\_IMAGE\_URI | The container image [unsupported\_image] is unsupported. Provide an image that follows the [Image Manifest V 2, Schema 1](https://docker-docs.uclv.cu/registry/spec/manifest-v2-1/). | 
| DUPLICATE\_REPOSITORY\_NAMES | Duplicate repository names: [duplicate\_repo\_names]. Provide unique names. | 
| INVALID\_NAMESPACE | The namespace values [invalid\_namespaces] are invalid. Provide values that conform to the {HELM\_RELEASE\_PARAM\_REGEX} regular expression. | 
| INVALID\_RELEASE\_NAME | The releaseName values [invalid\_release\_names] are invalid. Provide values that conform to the {HELM\_RELEASE\_PARAM\_REGEX} regular expression. | 
| OVERRIDE\_PARAMETER\_KEYS\_CONTAINS\_RESERVED\_PARAMETER\_KEYS | The override parameter key for delivery option titles [invalid\_keys] is reserved. Reserved keys: [reserved\_param\_keys]. Provide a different key. | 

## Update the visibility for an Amazon EKS add-on
<a name="update-delivery-option-visibility"></a>

You can use the Catalog API to update visibility for an Amazon EKS add-on delivery option of your product version in AWS Marketplace. Container and Helm delivery options for your container product are automatically created with 'Public' visibility status.

**Note**  
The ability to update visibility of your product version is supported only for the Amazon EKS add-on delivery option from the listed versions. If your product isn't 'Public' already, submit a request to publish the product with 'Public' visibility status by using the AWS Marketplace Management Portal.

By default, when you create a version with the Amazon EKS add-on delivery option, it's published in 'Limited' status. A 'Limited' status means the product isn't publicly available across all the Regions for your buyers to use and deploy in an Amazon EKS cluster. You can update the visibility of the delivery option from 'Limited' to 'Public' by calling the `StartChangeSet` API operation with the `UpdateDeliveryOptionsVisibility` change type. Specify the `DeliveryOptions Id` from your product version that corresponds to the Amazon EKS add-on delivery option.

**Request Syntax**

```
{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateDeliveryOptionsVisibility",
      "Entity":
      {
        "Identifier": "{{prod-example12345}}",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptions":
        [
          {
            "Id": "do-{{1234567891234567891234}}",
            "TargetVisibility": "Public"
          }
        ]
      }
    }
  ]
}
```

To add the `UpdateDeliveryOptionsVisibility` change type, provide information for the following fields :
+ `Entity` (object) (required) – Your container-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product uses: `ContainerProduct@1.0`. 
+ `DetailsDocument` (object) (required) – Details of the request, including the information about the repositories that you want to create. The following fields are all required.
  + `DeliveryOptions` (list of objects) – List of `DeliveryOption` objects, including the details of each:
    + `Id` (string) – Unique identifier for the `DeliveryOption`. (To get the unique identifier for the `DeliveryOption`, call the `DescribeEntity` action on the product that you're updating.
    + `TargetVisibility` – The intended new visibility of the product.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set.

```
{
"ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed, including scanning the container images and other information to ensure that it meets the [AWS Marketplace guidelines for container products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-policies.html). This process can take a few minutes to hours, depending on the number and size of your containers. 

You can check the status of the request through the AWS Marketplace Management Portal, or through the AWS Marketplace Catalog API by using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets). For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors).

**Asynchronous Errors**

The following table shows errors that are specific to `AddDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| EMPTY\_DELIVERY\_OPTION\_IDS | Provide a list of delivery option IDs. | 
| INVALID\_VISIBILITY\_STATE | The TargetVisibility option you provided is not supported. Please try again with an allowed option. The allowed option(s) are: Public | 
| INVALID\_DELIVERY\_OPTION\_IDS | You provided invalid delivery option details. Provide delivery option IDs that can be found in the product. IDs not found: [x] | 
| DUPLICATE\_DELIVERY\_OPTION\_IDS | Duplicate delivery option IDs: [duplicate\_ids]. Provide unique delivery option IDs. | 
| AUDIT\_ERROR | You haven't completed independent software vendor (ISV) testing for all compatible Amazon EKS cluster versions for your Amazon EKS add-on version(s). You must complete testing before we can release the delivery option(s). | 
| INVALID\_DELIVERY\_OPTION\_TYPE | The delivery option type you provided is not valid. Ensure that your delivery option is of type: EksAddOn and try again. | 
| INCOMPATIBLE\_HELM\_OBJECTS | Provide a Helm chart without unsupported Helm Objects: Unsupported Helm objects are as follows: all Release objects (except .Name and .Namespace), Helm hooks, and lookup functions. | 
| INCOMPATIBLE\_ADDON\_NAME | The add-on name [provided\_name] does not match the public version name. Update the public name before releasing. | 
| NCOMPATIBLE\_ADDON\_TYPE | The add-on types don't match. Reuse the existing add-on type from the public add-on version or previous add-on versions of this product. Only one add-on is supported for each product. | 
| INCOMPATIBLE\_ADDON\_NAMESPACE | The provided add-on namespace [provided\_namespace] does not match the public version namespace. Update the add-on namespace before releasing. | 

## Create repositories and resources
<a name="container-repos"></a>

To create a new version of a container-based product, you must have the resources for the version available in AWS Marketplace repositories. You create the repositories and then push (upload) the Docker (and Helm) resources into the repositories. To learn how to create the repositories through the AWS Marketplace Management Portal, see [ Add a new version of your product](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#container-add-version) in the *AWS Marketplace Seller Guide*.

To create new repositories, call `StartChangeSet` with the `AddRepositories` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "AddRepositories",
      "Entity":
      {
        "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12}}",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "Repositories":
        [
          {
            "RepositoryName": "{{new-repo-1}}",
            "RepositoryType": "ECR"
          },
          {
            "RepositoryName": "{{new-repo-2}}",
            "RepositoryType": "ECR"
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `AddRepositories` change type:

For more information about creating repositories, see [ Adding a new version](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-adding-version) in the *AWS Marketplace Seller Guide*.
+ `Entity` (object) (required) – Your container-based product. 
  + **Identifier** (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `ContainerProduct@1.0`. 
+ `DetailsDocument` (object) (required) – Details of the request. It includes the information about the repositories that you want to create. The included fields are all required.
  + `Repositories` (array of structures) – A list of repository objects. Each repository object includes a name and type.
    + `RepositoryName` (string) – The name of the repository to create. 
    + `RepositoryType` (string) – The type of the repository to create. The only allowed value is `ECR`. 

**Note**  
You can have up to 70 repositories per product, although you can add multiple resources, and versions of resources, to a single repository by giving them different tags when you push them.

After you create one or more repositories, you add your resources to the repositories. For information about how to push resources to repositories, see [ Pushing an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-push.html) in the *Amazon Elastic Container Registry User Guide*. For information about the specific push commands needed for one of your repositories, see [ Adding a new version](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-adding-version) in the *AWS Marketplace Seller Guide*.

**Asynchronous Errors**

The following errors are specific to `AddRepositories` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_ECR\_REPOSITORY\_NAME | Provide repository name in the format: 'nginx-web-app' | 
| DUPLICATE\_ECR\_REPOSITORY\_NAME | The repository [duplicate\_repo\_names] already exists. Choose a different name. | 
| MISSING\_REPOSITORY\_INFORMATION | Provide at least 1 repository name. | 
| INVALID\_ECR\_REPOSITORY\_NAME | Maximum character length 256 reached. Character length count is inclusive of the seller namespace. | 

## Update version information
<a name="container-update-version"></a>

You can use the Catalog API to update the details of an existing version of your container-based product in AWS Marketplace.

**Note**  
When a product is publicly available, you cannot update the version title, container images, delivery option title, or deployment resources for the version. If you need to update these aspects of a product, create a new version instead.

To update an existing version of your container-based product, call the `StartChangeSet` API operation with the `UpdateDeliveryOptions` change type, as shown in the following example. This updates the detail information for the delivery options that you specify, as well as the associated version. You must include at least one delivery option.

**Container Image Delivery Request Syntax**

```
POST /StartChangeSet HTTP/1.1 
Content-type: application/json

{
   "Catalog":"AWSMarketplace",
   "ChangeSet":[
      {
         "ChangeType":"UpdateDeliveryOptions",
         "Entity":{
            "Identifier":"{{example1-abcd-1234-5ef6-7890abcdef12}}",
            "Type":"ContainerProduct@1.0"
         },
         "DetailsDocument":{
            "Version":{
               "ReleaseNotes":"New release notes",
               "VersionTitle":"Version 1.2"
            },
            "DeliveryOptions":[
               {
                  "Id":"{{example4-2222-cccc-2222-cccccccccccc}}",
                  "Details":{
                     "EcrDeliveryOptionDetails":{
                        "DeliveryOptionTitle":"{{New Delivery Option Title}}",
                        "Description":"New description",
                        "UsageInstructions":"{{New usage instructions}}",
                        "CompatibleServices":[
                           "EKS"
                        ]
                     }
                  }
               }
            ]
         }
      }
   ]
}
```

**Helm Chart Delivery Request Syntax**

```
POST /StartChangeSet HTTP/1.1 
Content-type: application/json

{
   "Catalog":"AWSMarketplace",
   "ChangeSet":[
      {
         "ChangeType":"UpdateDeliveryOptions",
         "Entity":{
            "Identifier":"{{example1-abcd-1234-5ef6-7890abcdef12}}",
            "Type":"ContainerProduct@1.0"
         },
         "DetailsDocument":{
            "Version":{
               "ReleaseNotes":"New release notes",
               "VersionTitle":"Version 1.2"
            },
            "DeliveryOptions":[
               {
                  "Id":"{{example5-2222-cccc-2222-cccccccccccc}}",
                  "Details":{
                     "HelmDeliveryOptionDetails":{
                        "DeliveryOptionTitle":"{{New Delivery Option Title}}",
                        "ContainerImages":[
                           "{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/imagename:1.0"
                        ],
                        "HelmChartUri":"{{111122223333}}.dkr.ecr.us-east-1.amazonaws.com/sellername/helmname:1.0",
                        "CompatibleServices":[
                           "EKS-Anywhere"
                        ],
                        "Description":"{{New description}}",
                        "UsageInstructions":"{{New usage instructions}}",
                        "MarketplaceServiceAccountName":"{{new-service-account-name}}",
                        "ReleaseName":"{{new-release-name}}",
                        "Namespace":"{{new-cluster-namespace}}",
                        "OverrideParameters":[
                           {
                              "Key":"new.parameter.key",
                              "DefaultValue":"{{New parameter default value}}"
                           }
                        ]
                     }
                  }
               }
            ]
         }
      }
   ]
}
```

**Amazon EKS Add-On Delivery Request Syntax**

```
POST /StartChangeSet HTTP/1.1 
Content-type: application/json

{
   "Catalog":"AWSMarketplace",
   "ChangeSet":[
      {
         "ChangeType":"UpdateDeliveryOptions",
         "Entity":{
            "Identifier":"{{example1-abcd-1234-5ef6-7890abcdef12}}",
            "Type":"ContainerProduct@1.0"
         },
         "DetailsDocument":{
            "Version":{
               "ReleaseNotes":"{{New release notes}}",
               "VersionTitle":"{{Version 1.2}}"
            },
            "DeliveryOptions":[
               {
                  "Id":"{{example4-2222-cccc-2222-cccccccccccc}}",
                  "Details":{
                     "EksAddOnDeliveryOptionDetails":{
                        "ContainerImages":[
                           "{{709825985650}}.dkr.ecr.us-east-1.amazonaws.com/{{test-seller}}/{{canary-test-repo-product-6}}:mongo"
                        ],
                        "Description":"{{Description for delivery option provided by ISV}}",
                        "UsageInstructions":"{{Usage instructions with launch instructions}}",
                        "HelmChartUri":"{{709825985650}}.dkr.ecr.us-east-1.amazonaws.com/{{rocket}}/{{rocket-product-helm}}:1.0",
                        "AddOnName":"{{aws-mp-test}}",
                        "AddOnVersion":"{{1.2.1}}",
                        "AddOnType":"networking",
                        "CompatibleKubernetesVersions":[
                           "1.19",
                           "1.20"
                        ],
                        "SupportedArchitectures":[
                           "amd64",
                           "arm64"
                        ],
                        "Namespace":"{{my-test-namespace}}",
                        "EnvironmentOverrideParameters":[
                           {
                              "Key":"my-field",
                              "Value":"${{{AWS_EKS_CLUSTER_NAME}}}"
                           }
                        ]
                     }
                  }
               }
            ]
         }
      }
   ]
}
```

Provide information for the fields to add the `UpdateDeliveryOptions` change type:

For more information about these fields, see [ Adding a new version](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-adding-version) in the *AWS Marketplace Seller Guide*.
+ `Entity` (object) (required) – Your container-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `ContainerProduct@1.0`. 
+ `DetailsDocument` (object) (required) – Details of the request. It includes any information about the version of your container-based product that you would like to update. The included fields are all optional, but you must include at least one field to update.
  + `Version` (object) – Details about the software version.
    + `VersionTitle` (string) – The title of the version that you are creating. Typically this is a description of the version, such as **Version 1.1** or simply **1.1**. Your buyers will be able to choose the version to deploy from a list of all version titles.

      This property can't be updated if the product is already published publicly. 
    + `ReleaseNotes` (string) – Notes for buyers to tell them about changes from one version to the next. 
  + `DeliveryOptions` (list of objects) – List of `DeliveryOption` objects, including the details of each:
    + `Id` (string) – Unique identifier for the `DeliveryOption` (you can get the unique identifier for the `DeliveryOption` by calling the `DescribeEntity` action on the product you are updating).
    + `Details` (object) – Holds the details of a delivery option. Note that this nested details object does *not* need to be double-escaped.
      + `EcrDeliveryOptionDetails` (object) – The details of the container image delivery option.
        + `DeliveryOptionTitle` (string) – A short description that allows your buyer to choose between your delivery options.

          This property can't be updated if the product is already published publicly.
        + `ContainerImages` (array of strings) – An array of container image URLs used by this version. The path will be the repository that you have uploaded the image to, with the tag for the image used by this version. If this field is included, the list must include all needed images, even images that are not changing.

          This property can't be updated if the product is already published publicly.
        + `DeploymentResources` (array of objects) – An array of other deployment resources needed for the version, such as links to Helm charts or other documentation. Each resource includes a name to describe it and a URL that points at the resource. On the launch page for your version, this displays as a list of links.

          This property can't be updated if the product is already published publicly.
          + `Name` (string) – The text of the hyperlink that is shown to the buyer.
          + `Url` (string) – The URL of the hyperlink shown to the buyer.
        + `CompatibleServices` (array of strings) – An array of services that the release is compatible with. Valid options: `ECS`, `EKS`, `ECS-Anywhere`, `EKS-Anywhere`, and `Bedrock-AgentCore`.
        + `AgenticType` The type of runtime agent. Valid options: `AGENT`, `MCP_SERVER`, or `A2A_SERVER`.
        + `Description` (string) – A longer description of the delivery option to give details to your buyer. You can also include a link to more instructions hosted elsewhere.
        + `UsageInstructions` (string) – Provide instructions on how to deploy and use your product. You can also add a link to usage instructions hosted elsewhere. Can be up to 4,000 characters.
        + `EnvironmentVariables` – List of environment variables that are required by the AgentCore Runtime container and that will be pre-populated for buyers upon deployment. For each variable, provide an object with the *name* as expected by your container, a *description*, and an optional *defaultValue*. For variables such as credentials or API keys that are unique, do not provide a default value. You can use the description to specify details about the variable as well as possible values. All of the provided variables with their default values will be pre-populated when buyers launch your product.
    + `Id` (string) – Unique identifier for the `DeliveryOption` (you can get the unique identifier for the `DeliveryOption` by calling the `DescribeEntity` action on the product you are updating).
    + `Details` (object) – Holds the details of a delivery option. Note that this nested details object does *not* need to be double-escaped.
      + `HelmDeliveryOptionDetails` (object) – The details of the Helm chart delivery option.
        + `DeliveryOptionTitle` (string) – A short description that allows your buyer to choose between your delivery options.

          This property can't be updated if the product is already published publicly.
        + `ContainerImages` (array of strings) – An array of container image URLs used by this version. The path will be the repository that you have uploaded the image to, with the tag for the image used by this version. The list must include all needed images, even images that have not changed from previous versions. See the next section for information about creating repositories using the Catalog API.
        + `HelmChartUri` (string) – The URL to the Helm chart hosted in Amazon ECR that the buyer will install to launch the software.
        + `CompatibleServices` (array of strings) – An array of services that the release is compatible with. Valid options are `ECS` and `EKS`.
        + `Description` (string) – A longer description of the delivery option to give details to your buyer. You can also include a link to more instructions provided elsewhere.
        + `UsageInstructions` (string) – Provide instructions about the usage for this delivery option. Can be up to 4,000 characters.
        + `MarketplaceServiceAccountName` (string) – The name of the Kubernetes service account. The service account will be used to connect to AWS Identity and Access Management for permissions to call AWS services.
        + `ReleaseName` (string) – The name for the Helm release provided to the `helm install` command that buyers use to launch the software.
        + `Namespace` (string) – The Kubernetes namespace where the Helm chart will be installed.
        + `OverrideParameters` (array of objects) – Parameters that will be used in the Helm commands that launch the application. Buyers can override the default values.
          + `Key` (string)– The key for the parameter in dot notation (override.example.key).
          + `DefaultValue` (string) – The default value for this override parameter.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed, including scanning the container images and other information to ensure that it meets the [AWS Marketplace guidelines for container products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-policies.html). This process can take a few minutes to hours, depending on the number and size of your containers. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets). For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors).

**Asynchronous Errors**

The following errors are specific to `UpdateDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT\_STATUS | Use an existing limited or public product.  | 
| INCOMPATIBLE\_SERVICES | The service list contains incompatible services. [incompatible\_services] Provide a valid list of compatible services.  | 
| NO\_SERVICE\_SPECIFIED | Provide at least 1 compatible service.  | 
| DUPLICATE\_COMPATIBLE\_AWS\_SERVICES | The service list contains duplicate entries. Remove them. Each entry must be unique.  | 
| INVALID\_VERSION\_TITLE | Remove spaces before the trademark symbol.  | 
| INVALID\_VERSION\_TITLE | Remove the following unsupported characters: [x, y, z]  | 
| INVALID\_VERSION\_TITLE | Remove spaces from the beginning of the version title. | 
| INVALID\_VERSION\_TITLE | Provide version title with fewer than [x] characters.  | 
| DUPLICATE\_VERSION\_TITLE | The version title [duplicate\_version\_title] is a duplicate. Remove or change the title. | 
| INVALID\_RELEASE\_NOTES | Remove spaces before the trademark symbol.  | 
| INVALID\_RELEASE\_NOTES | Remove unsupported characters: [x, y, z]  | 
| INVALID\_RELEASE\_NOTES | Remove spaces from the beginning of release notes.  | 
| INVALID\_RELEASE\_NOTES | Provide release notes with fewer than (x) characters.  | 
| INVALID\_USAGE\_INSTRUCTIONS | Remove spaces before the trademark symbol.  | 
| INVALID\_USAGE\_INSTRUCTIONS | Remove unsupported characters: [x, y, z]  | 
| INVALID\_USAGE\_INSTRUCTIONS | Provide usage instructions with fewer than (x) characters.  | 
| INVALID\_USAGE\_INSTRUCTIONS | Provide usage instructions.  | 
| MISSING\_CONTAINER\_IMAGES | Provide at least 1 container image.  | 
| TOO\_MANY\_CONTAINER\_IMAGES | Provide fewer than 50 container images.  | 
| DUPLICATE\_CONTAINER\_IMAGES | The container image list contains duplicate images: [duplicate\_images]. Provide a list with unique images.  | 
| INVALID\_CONTAINER\_IMAGES | Provide a valid URI for the container image.  | 
| INVALID\_CONTAINER\_IMAGE\_URI | The image [invalid\_image\_uri] doesn't have access to this product. Upload the image to its corresponding product repository. For information about uploading, see [Getting started with container products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html). | 
| INVALID\_CONTAINER\_IMAGE\_TAG | Avoid using 'latest' tag.  | 
| MISSING\_DELIVERY\_OPTION\_IDS | Provide delivery option from existing list of Ids.  | 
| EMPTY\_DELIVERY\_OPTION\_IDS | Provide non-empty list of delivery option IDs.  | 
| DUPLICATE\_DELIVERY\_OPTION\_IDS | Duplicate delivery option IDs: [duplicate\_ids]. Provide unique delivery option IDs. | 
| DUPLICATE\_DELIVERY\_OPTION\_TITLES | Duplicate delivery option titles: [duplicate\_titles]. Remove the duplicates | 
| INVALID\_DELIVERY\_OPTION\_TITLES | The delivery option titles [existing\_titles] already exist. Provide a different title. | 
| INVALID\_FULFILLMENT\_OPTION\_TITLE | Provide delivery option title with fewer than (x) characters.  | 
| EMPTY\_RESOURCE\_NAME | Provide resource name.  | 
| EMPTY\_RESOURCE\_URL | Provide resource URL.  | 
| INVALID\_RESOURCE\_NAME | Provide resource name with fewer than 256 characters.  | 
| INVALID\_RESOURCE\_URL | Provide resource URL with fewer than 256 characters.  | 
| INVALID\_SHORT\_DESCRIPTION | Provide a short description with fewer than 1,000 characters.  | 
| INVALID\_SHORT\_DESCRIPTION | Provide short description.  | 
| NO\_LICENSE\_SECRET\_KEYS | For Amazon EKS Anywhere products, provide 1 override parameter for license secret. Needs DefaultValue of "${AWSMP\_LICENSE\_SECRET}", see example in section.  | 
| NO\_SERVICE\_ACCOUNT\_CONFIGURATION | For paid products, provide 1 override parameter for service account configuration. Needs DefaultValue of "${AWSMP\_SERVICE\_ACCOUNT}", see example in section.  | 
| SCAN\_ERROR | Fix security vulnerability ""[y]"" on Image ""[x]"".  | 
| FIELD\_NOT\_ALLOWED\_TO\_CHANGE | Field [x] cannot be changed.  | 
| INVALID\_DELIVERY\_OPTIONS\_STATUS | The delivery option IDs [invalid\_ids] are invalid. Provide delivery options in the limited or public state. | 
| NO\_CHANGE\_FOUND | Provide at least 1 change.  | 
| MULTIPLE\_VERSION\_UPDATE | Provide delivery option IDs from the same version.  | 
| OVERRIDE\_PARAMETER\_KEYS\_CONTAINS\_SPECIAL\_CHARS | The override parameter keys [invalid\_keys] contain invalid characters. You keys must use only letters, numbers, double quotes (" ") and plus signs (\+). | 
| INVALID\_CONTAINER\_IMAGE\_REPOSITORY | The repositories [invalid\_repositories] are invalid. Provide repositories created through the AddRepositories change type. | 
| INVALID\_CONTAINER\_IMAGE\_TAG\_FORMAT | The container image tag [invalid\_image\_tag] is invalid. Provide a tag conforming to the {CONTAINER\_IMAGE\_TAG\_REGEX} regular expression. | 
| DUPLICATE\_OVERRIDE\_PARAMETER\_KEYS | The override parameters contain duplicate keys [duplicate\_keys]. Remove the duplicates. | 
| UNSUPPORTED\_CONTAINER\_IMAGE\_URI | The container image [unsupported\_image] is unsupported. Provide an image that follows the [Image Manifest V 2, Schema 1](https://docker-docs.uclv.cu/registry/spec/manifest-v2-1/). | 
| INVALID\_NAMESPACE | The namespace values [invalid\_namespaces] are invalid. Provide values that conform to the {HELM\_RELEASE\_PARAM\_REGEX} regular expression. | 
| INVALID\_RELEASE\_NAME | The releaseName values [invalid\_release\_names] are invalid. Provide values that conform to the {HELM\_RELEASE\_PARAM\_REGEX} regular expression. | 
| OVERRIDE\_PARAMETER\_KEYS\_CONTAINS\_RESERVED\_PARAMETER\_KEYS | The override parameter key for delivery option titles [invalid\_keys] is reserved. Reserved keys: [reserved\_param\_keys]. Provide a different key. | 
| INCOMPATIBLE\_ADDON\_NAME | The add-on name [provided\_name] does not match the existing name. Reuse the existing name from the public version, or previous versions, of this add-on. You can only use one add-on name for each product. | 
| INCOMPATIBLE\_ADDON\_NAMESPACE | The add-on namespace [provided\_namespace] does not match the existing namespace . Reuse the existing namespace from the public version, or previous versions, of this add-on. You can only use one add-on namespace for each product. | 

## Restrict a version
<a name="container-restrict-version"></a>

You can use the Catalog API to restrict a version of your container-based product in AWS Marketplace. This prevents new buyers from being able to use that version. There must be at least one publicly available version in a product. You cannot restrict the only remaining publicly available version for a product.

To restrict a version, call the `StartChangeSet` API operation with the `RestrictDeliveryOptions` change type, as shown in the following example.

**Note**  
Restricting one or more, but not all, delivery options from a version will remove those options from being available to your buyers. Restricting all delivery options for a version will remove that version from the AWS Marketplace catalog.  
Restricting an Amazon EKS add-on is currently not supported through the Catalog API.  
Restricted versions are still available for existing customers.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "RestrictDeliveryOptions",
      "Entity":
      {
        "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12}}",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptionIds":
        [
          "{{example1-2222-cccc-2222-cccccccccccc}}"
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `RestrictDeliveryOptions` change type:
+ `Entity` (object) (required) – Your container-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `ContainerProduct@1.0`. 
+ `DetailsDocument` (object) (required) – Details of the request. It includes IDs for the delivery options of your container-based product that you would like to restrict.
  + `DeliveryOptionIds` (array of strings) – List of `DeliveryOption` IDs for the versions that you want to restrict. You can get the unique identifier for the `DeliveryOption` by calling the `DescribeEntity` action on the product you are restricting.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This process can take a few minutes to hours. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets). For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors).

**Asynchronous Errors**

The following errors are specific to `RestrictDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT\_STATUS | Use a public product. | 
| MISSING\_DELIVERY\_OPTION\_IDS | Provide delivery option from existing list of IDs. | 
| INVALID\_DELIVERY\_OPTIONS\_STATUS | The delivery option IDs [invalid\_ids] are invalid. Provide delivery options in the public state. | 
| EMPTY\_DELIVERY\_OPTION\_IDS | Provide non-empty list of delivery option IDs. | 
| INVALID\_MINIMUM\_PUBLIC\_DELIVERY\_OPTIONS | Cannot restrict all delivery option IDs. | 
| DUPLICATE\_DELIVERY\_OPTION\_IDS | Duplicate delivery option IDs: [duplicate\_ids]. Provide unique delivery option IDs. | 