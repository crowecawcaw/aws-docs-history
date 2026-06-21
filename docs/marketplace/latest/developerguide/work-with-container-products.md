The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Work with container-based products using the AWS Marketplace APIs

You can use the AWS Marketplace Catalog API to automate tasks for working with
container-based products.

For information about creating a container-based product using the Catalog API, see
[Create a product](work-with-seller-products.md#create-product "work-with-seller-products.md#create-product").

The following topics describe how to use the Catalog API to perform actions on your
container-based products:

###### Topics

- [Add a new version](#container-add-version "#container-add-version")
- [Update the visibility for an Amazon EKS add-on](#update-delivery-option-visibility "#update-delivery-option-visibility")
- [Create repositories and resources](#container-repos "#container-repos")
- [Update version information](#container-update-version "#container-update-version")
- [Restrict a version](#container-restrict-version "#container-restrict-version")

## Add a new version

If you already have a container-based product in AWS Marketplace, you can use the AWS Marketplace Catalog API
to add a new version. This requires that you have already created repositories in
AWS Marketplace for each container image or artifact that is part of your product, and that
you can copy them from your local Docker and Helm
files.

###### Note

For details about creating a container-based product using the AWS Marketplace Management Portal, see
[Getting started with container products](../userguide/container-product-getting-started.md "../userguide/container-product-getting-started.md") in the _AWS Marketplace
Seller Guide_.

For details about adding a new version, including creating repositories and
building Docker and Helm files into those
repositories, by using the AWS Marketplace Management Portal, see [Add a new version of your product](../userguide/container-product-getting-started.md#container-add-version "../userguide/container-product-getting-started.md#container-add-version") in the _AWS Marketplace Seller
Guide_.

If you have not already created new repositories, you can create them using
the Catalog API, see [Create repositories and resources](#container-repos "#container-repos").

To add a new version, call the `StartChangeSet` API operation with the
`AddDeliveryOptions` change type, as shown in the following
example.

###### Note

A version of a container-based product is made up of one or more delivery
options. For example, you might have two delivery options, one that works with a
noSQL database, and another that works with MySQL, so that your users can choose
how they want to work with your product. You create the version of your product
and add multiple delivery options in a single request with
`AddDeliveryOptions`.

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
        "Identifier": "`example1-abcd-1234-5ef6-7890abcdef12`",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "Version":
        {
          "VersionTitle": "1.1",
          "ReleaseNotes": "`Minor bug fix`"
        },
        "DeliveryOptions":
        [
          {
            "DeliveryOptionTitle": "`EKS Container image only delivery option`",
            "Details":
            {
              "EcrDeliveryOptionDetails":
              {
                "ContainerImages":
                [
                  "`111122223333`.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                ],
                "DeploymentResources":
                [
                  {
                    "Name": "HelmDeploymentTemplate",
                    "Url": "`111122223333`.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
                  }
                ],
                "CompatibleServices":
                [
                  "EKS"
                ],
                "Description": "Sample Description",
                "UsageInstructions": "helm pull `111122223333`.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame2:mychart1.1"
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
        "Identifier": "`example1-abcd-1234-5ef6-7890abcdef12`",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "Version":
        {
          "VersionTitle": "`1.1`",
          "ReleaseNotes": "`Minor bug fix`"
        },
        "DeliveryOptions":
        [
          {
            "DeliveryOptionTitle": "`Amazon Bedrock AgentCore Runtime Delivery Option`",
            "Details":
            {
              "EcrDeliveryOptionDetails":
              {
                "ContainerImages":
                [
                  "`111122223333.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1`"
                ],
                "CompatibleServices":
                [
                  "Bedrock-AgentCore"
                ],
                "AgenticType":
                [
                  "`AGENT`"
                ],
                "Description": "`Sample Description`",
                "UsageInstructions": "`To launch and invoke this agent on Amazon Bedrock AgentCore Runtime`",
                "EnvironmentVariables":
                [
                  {
                    "Name": "`HTTP_PORT`",
                    "Description": "`Port of the server`",
                    "DefaultValue": "`8080`"
                  },
                  {
                    "Name": "`API_KEY`",
                    "Description": "`Provide your unique API key here.`"
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

**Helm Chart Delivery Request
Syntax**

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
        "Identifier": "`example1-abcd-1234-5ef6-7890abcdef12`",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "Version":
        {
          "VersionTitle": "1.1",
          "ReleaseNotes": "`Minor bug fix`"
        },
        "DeliveryOptions":
        [
          {
            "DeliveryOptionTitle": "`HelmChartDeliveryOption`",
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
                  "`111122223333`.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:1.1"
                ],
                "HelmChartUri": "`111122223333`.dkr.ecr.us-east-1.amazonaws.com/sellername/reponame1:helmchart1.1",
                "Description": "`Helm chart description`",
                "UsageInstructions": "`Usage instructions`",
                "MarketplaceServiceAccountName": "`Service account name`",
                "ReleaseName": "`Optional release name`",
                "Namespace": "`Optional Kubernetes namespace`",
                "OverrideParameters":
                [
                  {
                    "Key": "`HelmKeyName1`",
                    "DefaultValue": "${`AWSMP_LICENSE_SECRET`}"
                  },
                  {
                    "Key": "`HelmKeyName2`",
                    "DefaultValue": "${`AWSMP_SERVICE_ACCOUNT`}"
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
          "ReleaseNotes": "`New Add-on Release`"
        },
        "DeliveryOptions": [
          {
            "DeliveryOptionTitle": "`AWS Marketplace Test AddOn from CAPI 1`",
            "Visibility": "Limited",
            "Details": {
              "EksAddOnDeliveryOptionDetails": {
                "ContainerImages": [
                  "`111122223333`.dkr.ecr.us-east-1.amazonaws.com/test-seller/canary-test-repo-product-6:mongo"
                ],
                "HelmChartUri": "`111122223333`.dkr.ecr.us-east-1.amazonaws.com/rocket/rocket-product-helm:1.0",
                "Description": "`Description for delivery option provided by ISV`",
                "UsageInstructions": "`Usage instructions with launch instructions`",
                "AddOnName": "`aws-mp-test`",
                "AddOnVersion": "`1.2.1`",
                "AddOnType": "networking",
                "CompatibleKubernetesVersions": [
                  "1.25",
                  "1.26"
                ],
                "SupportedArchitectures": [
                  "amd64",
                  "arm64"
                ],
                "Namespace": "`my-test-namespace`",
                "EnvironmentOverrideParameters": [
                  {
                    "Key": "cluster-name",
                    "Value": "${`AWS_EKS_CLUSTER_NAME`}"
                  },
                  {
                    "Key": "region-name",
                    "Value": "${`AWS_REGION`}"
                  }
                ]
              }
            }
          }
        ]
      },
      "ChangeName": "`PublishAddonNew`"
    }
  ]
}
```

Provide information for the fields to add the `AddDeliveryOptions`
change type:

- `Entity` (object) (required) – Your container-based
  product.

  - `Identifier` (string) (required) – Your product
    ID. For more information, see [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").
  - `Type` (string) (required) – The
    `Type` is based on the delivery method (product type)
    that your product will be using: `ContainerProduct@1.0`.

- `DetailsDocument` (object) (required) – Details of the
  request. It includes all the information about the version that you are
  adding. This field is a string field.

  - `Version` (object) – Details about the version
    that you are adding to your product.

    - `VersionTitle` (string) – The title of
      the version that you are creating. Typically this is a
      description of the version, like `Version
1.1` or simply `1.1`.
      Your buyers will be able to choose the version to deploy
      from a list of version titles.
    - `ReleaseNotes` (string) – The detailed
      notes about this version. Must be less than 30,000
      characters.

  - `DeliveryOptions` (array of objects) – An array
    of delivery options, where each is a method of delivery for your
    product version. For example, if you have one delivery option for
    Amazon Elastic Container Service (Amazon ECS) and another for Amazon Elastic Kubernetes Service (Amazon EKS), you must have two
    delivery options.

    - `DeliveryOptionTitle` (string) – A short
      description that helps your buyer to choose between your
      delivery options.
    - `Details` (object) – The resources used
      for this delivery option. This is a details field within the
      details field. You do not need to doubly escape characters
      in this field.

      - `AddOnName –` A unique add-on
        name that buyers will see in the Amazon EKS catalog. This
        name will add a prefix later using
        `SellerAlias`. For example, where
        `isv-alias_` is the ISV provided add-on
        name.
      - `AddOnType –` The type of add-on
        chosen from a list of supported values from Amazon EKS:
        Gitops | monitoring | logging | cert-management |
        policy-management | cost-management | autoscaling |
        storage | kubernetes-management | service-mesh |
        etcd-backup | ingress-service-type | load-balancer |
        local-registry| networking | Security | backup |
        ingress-controller | observability
      - `AddOnVersion –` A semantic
        version so that buyer can choose a specific version
        of AddOn they need to install or upgrade.
      - `CompatibleKubernetesVersions` –
        The Amazon EKS Kubernetes versions that this software is
        compatible with.
      - `CompatibleServices` (array of strings)
        – An array of services that the release is
        compatible with. Valid options: `ECS`,
        `EKS`, `ECS-Anywhere`,
        `EKS-Anywhere`, and
        `Bedrock-AgentCore`.
      - `ContainerImages` (array of strings)
        – An array of container image URLs used by
        this version. The path will be the repository that
        you have uploaded the image to, with the tag for the
        image used by this version. The list must include
        all needed images, even images that have not changed
        from previous versions. See the next section for
        information about creating repositories using the
        Catalog API.
      - `Description` (string) – A
        longer description of the delivery option to give
        details to your buyer. You can also include a link
        to more instructions provided elsewhere.
      - `EcrDeliveryOptionDetails` –
        `AgenticType` – The type of
        runtime agent. Valid options: `AGENT`,
        `MCP_SERVER`, or `A2A_SERVER`.
      - `EcrDeliveryOptionDetails` –
        `EnvironmentVariables` – List of environment variables that are required by the AgentCore Runtime container and that will be pre-populated for buyers upon deployment. For each variable, provide an object with the _name_ as expected by your container, a _description_, and an optional _defaultValue_. For variables such as credentials or API keys that are unique, do not provide a default value. You can use the description to specify details about the variable as well as possible values. All of the provided variables with their default values will be pre-populated when buyers launch your product.
      - `EcrDeliveryOptionDetails –` `DeploymentResources (array of
objects)` – An array of other
        resources needed for the version, such as
        Helm charts. Each resource includes
        a `Name` to describe it, and a
        `URL` that points at the
        resource.
      - `EnvironmentOverrideParameters –` List of system parameters to be used by the
        add-on. Some of the ISV provided AddOn (HelmChart)
        might require configurations with information
        derived from the Amazon EKS execution environment state
        (/system information). For example,
        `EksClusterRegion`,
        `EKSClusterName`, and others. You can
        avoid additional actions from Buyer by dynamically
        substituting these values at Amazon EKS AddOn launch.
        Amazon EKS System already supports automatic
        substitutions of system param for add-ons. AWS Marketplace ISV
        experience can be extended to collect this params
        which would require substitution.

      The generic system information to be substituted
      can be indicated by providing a AWS Marketplace specified
      constant following convention similar to
      Helm substitution. The supported
      values are `${AWS_REGION}` and
      `${AWS_EKS_CLUSTER_NAME}`.

      ```

       "EnvironmentOverrideParameters" : [ {
         "Key" : "my-field.region"
         "Value" : "${`AWS_REGION`}"
         },
         {
         "Key" : "my-second-field"
         "Value" : "${`AWS_EKS_CLUSTER_NAME`}"
         },

      ```
      - `HelmDeliveryOptionDetails` –
        `HelmChartUri (string)` – The
        URL to the Helm chart hosted in Amazon ECR
        that the buyer will install to launch the
        software.
      - `HelmDeliveryOptionDetails –` `MarketplaceServiceAccountName
(string)` – _Optional_ – The name of the Kubernetes
        service account. The service account will be used to
        connect to AWS Identity and Access Management (IAM) for permissions to call
        AWS services.
      - `HelmDeliveryOptionDetails –` `ReleaseName (string)` –
        _Optional_ – The name
        for the Helm release provided to the
        `helm install` command that buyers use
        to launch the software. If not included,
        Helm will provide an automatically
        generated release name for you.
      - `HelmDeliveryOptionDetails –` `Namespace (string)` –
        _Optional_ – The
        Kubernetes namespace where the
        Helm chart will be
        installed.
      - `HelmDeliveryOptionDetails –` `OverrideParameters (array of
objects)` – Parameters that will be
        used in the Helm commands that launch
        the application. Buyers can override the default
        values.

      ###### Note

      For Amazon EKS Anywhere products, provide at least
      1 override parameter for the license secret.
      Provide `DefaultValue` of
      `"${AWSMP_LICENSE_SECRET}"`.

      For paid products, provide at least 1 override
      parameter for service account configuration.
      Provide `DefaultValue` of
      `"${AWSMP_SERVICE_ACCOUNT}"`.

          + `Key` (string) – The key
           for the parameter in dot notation
           (override.example.key).
          + `DefaultValue` (string) –
           The default value for this override
           parameter.
      - `Namespace –` The ISV provided
        namespace for add-on installation.
      - `SupportedArchitectures –` The
        list of supported architectures, like amd64 and
        arm64.
      - `UsageInstructions` (string) –
        Provide instructions about the usage for this
        delivery option. Can be up to 4,000
        characters.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "`example123456789012abcdef`",
   "ChangeSetArn": "arn:aws:aws-marketplace:`us-east-1`:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}
```

The change request is added to a queue and processed, including scanning the
container images and other information to ensure that it meets the [AWS Marketplace
guidelines for container products](../userguide/container-product-policies.md "../userguide/container-product-policies.md"). This process can take a few minutes
to hours, depending on the number and size of your containers.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").
For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors "work-with-seller-products.md#seller-product-change-set-errors").

**Asynchronous Errors**

The following errors are specific to `AddDeliveryOptions` actions in
the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                                               | Error message                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| INCOMPATIBLE_PRODUCT_STATUS                              | Use an existing limited or public product.                                                                                                                                                                                                                                                                                     |
| INCOMPATIBLE_SERVICES                                    | The service list contains incompatible services.<br>[incompatible\_services] Provide a valid list of compatible<br>services.                                                                                                                                                                                                   |
| NO_SERVICE_SPECIFIED                                     | Provide at least 1 compatible service.                                                                                                                                                                                                                                                                                         |
| DUPLICATE_COMPATIBLE_AWS_SERVICES                        | The service list contains duplicate entries. Remove them. Each<br>entry must be unique.                                                                                                                                                                                                                                        |
| INVALID_VERSION_TITLE                                    | Remove spaces before the trademark symbol.                                                                                                                                                                                                                                                                                     |
| INVALID_VERSION_TITLE                                    | Remove the following unsupported characters: [x, y, z]                                                                                                                                                                                                                                                                         |
| INVALID_VERSION_TITLE                                    | Remove spaces from the beginning of the version title.                                                                                                                                                                                                                                                                         |
| INVALID_VERSION_TITLE                                    | Provide version title with fewer than [x] characters.                                                                                                                                                                                                                                                                          |
| DUPLICATE_VERSION_TITLE                                  | The version title [duplicate\_version\_title] is a duplicate.<br>Remove or change the title.                                                                                                                                                                                                                                   |
| INVALID_RELEASE_NOTES                                    | Remove spaces before the trademark symbol.                                                                                                                                                                                                                                                                                     |
| INVALID_RELEASE_NOTES                                    | Remove unsupported characters: [x, y, z]                                                                                                                                                                                                                                                                                       |
| INVALID_RELEASE_NOTES                                    | Remove spaces from the beginning of release notes.                                                                                                                                                                                                                                                                             |
| INVALID_RELEASE_NOTES                                    | Provide release notes with fewer than (x) characters.                                                                                                                                                                                                                                                                          |
| INVALID_USAGE_INSTRUCTIONS                               | Remove spaces before the trademark symbol.                                                                                                                                                                                                                                                                                     |
| INVALID_USAGE_INSTRUCTIONS                               | Remove unsupported characters: [x, y, z]                                                                                                                                                                                                                                                                                       |
| INVALID_USAGE_INSTRUCTIONS                               | Provide usage instructions with fewer than (x)<br>characters.                                                                                                                                                                                                                                                                  |
| INVALID_USAGE_INSTRUCTIONS                               | Provide usage instructions.                                                                                                                                                                                                                                                                                                    |
| MISSING_CONTAINER_IMAGES                                 | Provide at least 1 container image.                                                                                                                                                                                                                                                                                            |
| NO_LICENSE_SECRET_KEYS                                   | For Amazon EKS Anywhere products, provide 1 override parameter for<br>license secret. Needs `DefaultValue` of<br>`"${AWSMP_LICENSE_SECRET}"`, see example in section.                                                                                                                                                          |
| TOO_MANY_CONTAINER_IMAGES                                | Provide fewer than 50 container images.                                                                                                                                                                                                                                                                                        |
| DUPLICATE_CONTAINER_IMAGES                               | The container image list contains duplicate images:<br>[duplicate\_images]. Provide a list with unique images.                                                                                                                                                                                                                 |
| INVALID_CONTAINER_IMAGES                                 | Provide a valid URI for the container image.                                                                                                                                                                                                                                                                                   |
| INVALID_CONTAINER_IMAGE_URI                              | The image [invalid\_image\_uri] doesn't have access to this<br>product. Upload the image to its corresponding product repository.<br>For information about uploading, see [Getting started with container<br>products](../userguide/container-product-getting-started.md "../userguide/container-product-getting-started.md"). |
| INVALID_CONTAINER_IMAGE_TAG                              | Avoid using 'latest' tag.                                                                                                                                                                                                                                                                                                      |
| DUPLICATE_DELIVERY_OPTION_TITLES                         | Duplicate delivery option titles: [duplicate\_titles]. Remove the<br>duplicates                                                                                                                                                                                                                                                |
| INVALID_DELIVERY_OPTION_TITLES                           | The delivery option titles [existing\_titles] already exist.<br>Provide a different title.                                                                                                                                                                                                                                     |
| INVALID_FULFILLMENT_OPTION_TITLE                         | Provide delivery option title with fewer than (x) characters.                                                                                                                                                                                                                                                                  |
| NO_SERVICE_ACCOUNT_CONFIGURATION                         | For paid products, provide 1 override parameter for service<br>account configuration. Needs `DefaultValue` of<br>`"${AWSMP_SERVICE_ACCOUNT}"`, see example in section.                                                                                                                                                         |
| INVALID_DETAILS                                          | Provided Details is not valid.                                                                                                                                                                                                                                                                                                 |
| EMPTY_RESOURCE_NAME                                      | Provide resource name.                                                                                                                                                                                                                                                                                                         |
| EMPTY_RESOURCE_URL                                       | Provide resource URL.                                                                                                                                                                                                                                                                                                          |
| INVALID_RESOURCE_NAME                                    | Provide resource name with fewer than 256 characters.                                                                                                                                                                                                                                                                          |
| INVALID_RESOURCE_URL                                     | Provide resource URL with fewer than 256 characters.                                                                                                                                                                                                                                                                           |
| INVALID_SHORT_DESCRIPTION                                | Provide a short description with fewer than 1,000 characters.                                                                                                                                                                                                                                                                  |
| INVALID_SHORT_DESCRIPTION                                | Provide short description.                                                                                                                                                                                                                                                                                                     |
| SCAN_ERROR                                               | Fix security vulnerability ""[y]"" on Image ""[x]"".                                                                                                                                                                                                                                                                           |
| IMAGE_NOT_FOUND                                          | The public image URI [invalid\_image\_uri] is invalid. Provide a<br>valid URI.                                                                                                                                                                                                                                                 |
| INVALID_ARN                                              | Provide a valid ARN for image access.                                                                                                                                                                                                                                                                                          |
| IMAGE_INACCESSIBLE                                       | Provide a valid ARN for image access.                                                                                                                                                                                                                                                                                          |
| DUPLICATE_ADDON_NAME                                     | The AddOn name you provided is already in use by a different<br>product. Provide a different name.                                                                                                                                                                                                                             |
| DUPLICATE_ADDON_VERSION                                  | The add-on version title [duplicate\_version\_title] is already in<br>use. Provide a different title.                                                                                                                                                                                                                          |
| INVALID_ADDON_TYPE                                       | The add-on types [invalid\_types] are invalid. Provide a type from<br>the supported list: [eks\_addon\_do\_supported\_types].                                                                                                                                                                                                  |
| INVALID_KUBERNETES_VERSION                               | The Kubernetes versions [invalid\_versions] are invalid. Provide<br>versions from the supported list:<br>[eks\_addon\_do\_supported\_kubernetes\_versions].                                                                                                                                                                    |
| DUPLICATE_KUBERNETES_VERSIONS                            | Duplicate Kubernetes versions: [duplicate\_versions]. Provide a<br>list with unique versions.                                                                                                                                                                                                                                  |
| INVALID_ARCHITECTURE                                     | The architectures [invalid\_architectures] are invalid. Provide<br>architectures from the Amazon EKS supported architectures :<br>[eks\_addon\_do\_supported\_architectures].                                                                                                                                                  |
| DUPLICATE_SUPPORTED_ARCHITECTURES                        | Duplicate architectures: [duplicate\_architectures]. Provide a<br>list of unique, supported architectures.                                                                                                                                                                                                                     |
| INVALID_VISIBILITY_STATE                                 | The states [invalid\_states] are invalid for the {EKS_DO} delivery<br>option. Provide a valid visibility state from the following allowed<br>values: Limited.                                                                                                                                                                  |
| INVALID_ENVIRONMENT_OVERRIDE_PARAMETER_VALUE             | The override parameter values [invalid\_values] are invalid.<br>Provide a valid value from the following list:<br>[eks\_addon\_do\_environment\_override\_parameter\_values].                                                                                                                                                  |
| DUPLICATE_ENVIRONMENT_OVERRIDE_PARAMETER_KEY             | The environment override parameters contain duplicate keys:<br>[duplicate\_keys]. Remove them.                                                                                                                                                                                                                                 |
| TOO_MANY_EKS_ADDON_DELIVERY_OPTIONS                      | Provide only one Amazon EKS add-on delivery option for the version.                                                                                                                                                                                                                                                            |
| INCOMPATIBLE_ADDON_NAME                                  | The add-on name [provided\_name] does not match the existing name.<br>Reuse the existing name from the public version, or previous<br>versions, of this add-on. You can only use one add-on name for each<br>product.                                                                                                          |
| INCOMPATIBLE_ADDON_TYPE                                  | The add-on type [provided\_type] does not match the existing type.<br>Reuse the existing type from the public version, or previous<br>versions, of this add-on. You can only use one add-on type for each<br>product.                                                                                                          |
| INCOMPATIBLE_ADDON_NAMESPACE                             | The add-on namespace [provided\_namespace] does not match the<br>existing namespace . Reuse the existing namespace from the public<br>version, or previous versions, of this add-on. You can only use one<br>add-on namespace for each product.                                                                                |
| INVALID_HELM_CHART_URI                                   | The Helm chart URI [invalid\_uri] is invalid. Provide a URI in the<br>SemVer 2 format.                                                                                                                                                                                                                                         |
| INCOMPATIBLE_HELM_OBJECTS(INVALID_HELM_OBJECTS)          | Provide a Helm chart without using the following<br>unsupported Helm Objects: <unsupported-objects>.                                                                                                                                                                                                                           |
| INVALID_DEPENDENT_HELM_CHARTS                            | Provide a Helm chart that contains the following dependent charts<br>directly in the parent chart directory and not externally sourced:<br><invalid-subcharts>.                                                                                                                                                                |
| INVALID_HELM_SENSITIVE_CONFIG                            | Provide an advanced configuration schema without sensitive<br>information or secrets. Keywords:<br><sensitive-parameters-identified>                                                                                                                                                                                           |
| INVALID_HELM_UNDECLARED_IMAGES                           | Provide the following Helm chart images within the delivery<br>option of the request: <list-of-images>.                                                                                                                                                                                                                        |
| INVALID_HELM_CHART_IMAGES                                | Provide a Helm chart containing images within repositories<br>created via the AddRepositories change type. External images:<br><images-identified>.                                                                                                                                                                            |
| INVALID_HELM_LINT                                        | Provide a Helm chart that successfully passes Helm lint.                                                                                                                                                                                                                                                                       |
| INVALID_HELM_TEMPLATE                                    | Provide a Helm chart that successfully passes Helm template.                                                                                                                                                                                                                                                                   |
| INVALID_HELM_CHART                                       | Provide a Helm chart that adheres to AWS Marketplace guidance identified in<br>[Helm Charts bulleted list](../userguide/container-product-policies.md "../userguide/container-product-policies.md") in the _AWS Marketplace Seller<br>Guide_.                                                                                  |
| INVALID_ADDON_NAME                                       | Provide an AddOn name that follows the following regex pattern:<br>xx                                                                                                                                                                                                                                                          |
| INVALID_ADDON_NAMESPACE                                  | The namespace values [invalid\_namespaces] are invalid. The<br>namespace must follow the  {EKS_ADD_ON_NAMESPACE_REGEX} regular<br>expression. For example, namespace, namespace-test.                                                                                                                                          |
| INVALID_ADDON_NAME_PATTERN                               | Provide an add-on name that starts with a letter or digit, and<br>then a combination of letters, digits, and hyphens. For example,<br>test-addon, eksaddon                                                                                                                                                                     |
| INVALID_ADDON_VERSION_PATTERN                            | Provide an add-on version using the following pattern:<br>"<major>.<minor>.<patch>" (for example, 1.2.3,<br>0.1.2, 0.1.1)                                                                                                                                                                                                      |
| EMPTY_DELIVERY_OPTION_IDS                                | Provide a list of delivery option IDs.                                                                                                                                                                                                                                                                                         |
| INVALID_DELIVERY_OPTIONS_INPUT                           | The list contains one or more invalid delivery options. Provide a<br>valid list, and ensure that each option has a single delivery<br>method.                                                                                                                                                                                  |
| OVERRIDE_PARAMETER_KEYS_CONTAINS_SPECIAL_CHARS           | The override parameter keys [invalid\_keys] contain invalid<br>characters. You keys must use only letters, numbers, double quotes<br>(“ ”) and plus signs (+).                                                                                                                                                                 |
| INVALID_CONTAINER_IMAGE_REPOSITORY                       | The repositories [invalid\_repositories] are invalid. Provide<br>repositories created through the AddRepositories change<br>type.                                                                                                                                                                                              |
| INVALID_CONTAINER_IMAGE_TAG_FORMAT                       | The container image tag [invalid\_image\_tag] is invalid. Provide a<br>tag conforming to the {CONTAINER_IMAGE_TAG_REGEX} regular<br>expression.                                                                                                                                                                                |
| DUPLICATE_OVERRIDE_PARAMETER_KEYS                        | The override parameters contain duplicate keys [duplicate\_keys].<br>Remove the duplicates.                                                                                                                                                                                                                                    |
| UNSUPPORTED_CONTAINER_IMAGE_URI                          | The container image [unsupported\_image] is unsupported. Provide<br>an image that follows the [Image Manifest V 2, Schema 1](https://docker-docs.uclv.cu/registry/spec/manifest-v2-1/ "https://docker-docs.uclv.cu/registry/spec/manifest-v2-1/").                                                                             |
| DUPLICATE_REPOSITORY_NAMES                               | Duplicate repository names: [duplicate\_repo\_names]. Provide<br>unique names.                                                                                                                                                                                                                                                 |
| INVALID_NAMESPACE                                        | The namespace values [invalid\_namespaces] are invalid. Provide<br>values that conform to the {HELM_RELEASE_PARAM_REGEX} regular<br>expression.                                                                                                                                                                                |
| INVALID_RELEASE_NAME                                     | The releaseName values [invalid\_release\_names] are invalid.<br>Provide values that conform to the {HELM_RELEASE_PARAM_REGEX}<br>regular expression.                                                                                                                                                                          |
| OVERRIDE_PARAMETER_KEYS_CONTAINS_RESERVED_PARAMETER_KEYS | The override parameter key for delivery option titles<br>[invalid\_keys] is reserved. Reserved keys: [reserved\_param\_keys].<br>Provide a different key.                                                                                                                                                                      |

## Update the visibility for an Amazon EKS add-on

You can use the Catalog API to update visibility for an Amazon EKS add-on delivery
option of your product version in AWS Marketplace. Container and Helm delivery
options for your container product are automatically created with ‘Public’
visibility status.

###### Note

The ability to update visibility of your product version is supported only for
the Amazon EKS add-on delivery option
from
the listed versions. If your product isn't 'Public' already,
submit a request to publish the product with 'Public' visibility status by using
the AWS Marketplace Management Portal.

By default, when you create a version with the Amazon EKS add-on delivery option, it's
published in ‘Limited’ status. A ‘Limited’ status means the product isn't publicly
available across all the Regions for your buyers to use and deploy in an Amazon EKS
cluster. You can update the visibility of the delivery option from ‘Limited’ to
‘Public’ by calling the `StartChangeSet` API operation with the
`UpdateDeliveryOptionsVisibility` change type. Specify the
`DeliveryOptions Id` from your product version that corresponds to
the Amazon EKS add-on delivery option.

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
        "Identifier": "`prod-example12345`",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptions":
        [
          {
            "Id": "do-`1234567891234567891234`",
            "TargetVisibility": "Public"
          }
        ]
      }
    }
  ]
}
```

To add the `UpdateDeliveryOptionsVisibility` change type, provide
information for the following fields :

- `Entity` (object) (required) – Your container-based
  product.

  - `Identifier` (string) (required) – Your product
    ID. For more information, see [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").
  - `Type` (string) (required) – The
    `Type` is based on the delivery method (product type)
    that your product uses: `ContainerProduct@1.0`.

- `DetailsDocument` (object) (required) – Details of the
  request, including the information about the repositories that you want to
  create. The following fields are all required.

  - `DeliveryOptions` (list of objects) – List of
    `DeliveryOption` objects, including the details of
    each:

    - `Id` (string) – Unique identifier for
      the `DeliveryOption`. (To get the unique
      identifier for the `DeliveryOption`, call the
      `DescribeEntity` action on the product that
      you're updating.
    - `TargetVisibility` – The intended new
      visibility of the product.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change
set.

```

{
"ChangeSetId": "`example123456789012abcdef`",
   "ChangeSetArn": "arn:aws:aws-marketplace:`us-east-1`:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}
```

The change request is added to a queue and processed, including scanning the
container images and other information to ensure that it meets the [AWS Marketplace
guidelines for container products](../userguide/container-product-policies.md "../userguide/container-product-policies.md"). This process can take a few minutes
to hours, depending on the number and size of your containers.

You can check the status of the request through the AWS Marketplace Management Portal, or through the
AWS Marketplace Catalog API by using the `DescribeChangeSet` API operation.

For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").
For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors "work-with-seller-products.md#seller-product-change-set-errors").

**Asynchronous Errors**

The following table shows errors that are specific to
`AddDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors are
returned when you call `DescribeChangeSet` after a change set is
processing. For more information about using `DescribeChangeSet` to get
the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                    | Error message                                                                                                                                                                                                                             |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EMPTY_DELIVERY_OPTION_IDS     | Provide a list of delivery option IDs.                                                                                                                                                                                                    |
| INVALID_VISIBILITY_STATE      | The `TargetVisibility` option you provided is not<br>supported. Please try again with an allowed option. The allowed<br>option(s) are: `Public`                                                                                           |
| INVALID_DELIVERY_OPTION_IDS   | You provided invalid delivery option details. Provide delivery<br>option IDs that can be found in the product. IDs not found:<br>[x]                                                                                                      |
| DUPLICATE_DELIVERY_OPTION_IDS | Duplicate delivery option IDs: [duplicate\_ids]. Provide unique<br>delivery option IDs.                                                                                                                                                   |
| AUDIT_ERROR                   | You haven't completed independent software vendor (ISV) testing<br>for all compatible Amazon EKS cluster versions for your Amazon EKS add-on<br>version(s).<br>You must complete testing before we can release the delivery<br>option(s). |
| INVALID_DELIVERY_OPTION_TYPE  | The delivery option type you provided is not valid. Ensure that<br>your delivery option is of type: `EksAddOn` and try<br>again.                                                                                                          |
| INCOMPATIBLE_HELM_OBJECTS     | Provide a Helm chart without unsupported<br>Helm Objects: Unsupported Helm<br>objects are as follows: all Release objects (except .Name and<br>.Namespace), Helm hooks, and lookup<br>functions.                                          |
| INCOMPATIBLE_ADDON_NAME       | The add-on name [provided\_name] does not match the public version<br>name. Update the public name before releasing.                                                                                                                      |
| NCOMPATIBLE_ADDON_TYPE        | The add-on types don't match. Reuse the existing add-on type from<br>the public add-on version or previous add-on versions of this<br>product. Only one add-on is supported for each product.                                             |
| INCOMPATIBLE_ADDON_NAMESPACE  | The provided add-on namespace [provided\_namespace] does not match<br>the public version namespace. Update the add-on namespace before<br>releasing.                                                                                      |

## Create repositories and resources

To create a new version of a container-based product, you must have the resources
for the version available in AWS Marketplace repositories. You create the repositories and
then push (upload) the Docker (and Helm) resources
into the repositories. To learn how to create the repositories through the
AWS Marketplace Management Portal, see [Add a new version of your product](../userguide/container-product-getting-started.md#container-add-version "../userguide/container-product-getting-started.md#container-add-version") in the _AWS Marketplace Seller
Guide_.

To create new repositories, call `StartChangeSet` with the
`AddRepositories` change type, as shown in the following
example.

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
        "Identifier": "`example1-abcd-1234-5ef6-7890abcdef12`",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "Repositories":
        [
          {
            "RepositoryName": "`new-repo-1`",
            "RepositoryType": "ECR"
          },
          {
            "RepositoryName": "`new-repo-2`",
            "RepositoryType": "ECR"
          }
        ]
      }
    }
  ]
}

```

Provide information for the fields to add the `AddRepositories` change
type:

For more information about creating repositories, see [Adding a new version](../userguide/ami-single-ami-products.md#single-ami-adding-version "../userguide/ami-single-ami-products.md#single-ami-adding-version") in the _AWS Marketplace Seller
Guide_.

- `Entity` (object) (required) – Your container-based
  product.

  - **Identifier** (string) (required)
    – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").
  - `Type` (string) (required) – The
    `Type` is based on the delivery method (product type)
    that your product will be using: `ContainerProduct@1.0`.

- `DetailsDocument` (object) (required) – Details of the
  request. It includes the information about the repositories that you want to
  create. The included fields are all required.

  - `Repositories` (array of structures) – A list of
    repository objects. Each repository object includes a name and
    type.

    - `RepositoryName` (string) – The name of
      the repository to create.
    - `RepositoryType` (string) – The type of
      the repository to create. The only allowed value is
      `ECR`.

###### Note

You can have up to 70 repositories per product, although you can add multiple
resources, and versions of resources, to a single repository by giving them
different tags when you push them.

After you create one or more repositories, you add your resources to the
repositories. For information about how to push resources to repositories, see
[Pushing an image](../../../AmazonECR/latest/userguide/image-push.md "../../../AmazonECR/latest/userguide/image-push.md") in the _Amazon Elastic Container Registry User Guide_. For
information about the specific push commands needed for one of your repositories,
see [Adding a new version](../userguide/ami-single-ami-products.md#single-ami-adding-version "../userguide/ami-single-ami-products.md#single-ami-adding-version") in the _AWS Marketplace Seller
Guide_.

**Asynchronous Errors**

The following errors are specific to `AddRepositories` actions in the
AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet`
after a change set is processing. For more information about using
`DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                     | Error message                                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------------------------- |
| INVALID_ECR_REPOSITORY_NAME    | Provide repository name in the format: 'nginx-web-app'                                                |
| DUPLICATE_ECR_REPOSITORY_NAME  | The repository [duplicate\_repo\_names] already exists. Choose a<br>different name.                   |
| MISSING_REPOSITORY_INFORMATION | Provide at least 1 repository name.                                                                   |
| INVALID_ECR_REPOSITORY_NAME    | Maximum character length 256 reached. Character length count is<br>inclusive of the seller namespace. |

## Update version information

You can use the Catalog API to update the details of an existing version of your
container-based product in AWS Marketplace.

###### Note

When a product is publicly available, you cannot update the version title,
container images, delivery option title, or deployment resources for the
version. If you need to update these aspects of a product, create a new version
instead.

To update an existing version of your container-based product, call the
`StartChangeSet` API operation with the
`UpdateDeliveryOptions` change type, as shown in the following
example. This updates the detail information for the delivery options that you
specify, as well as the associated version. You must include at least one delivery
option.

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
            "Identifier":"`example1-abcd-1234-5ef6-7890abcdef12`",
            "Type":"ContainerProduct@1.0"
         },
         "DetailsDocument":{
            "Version":{
               "ReleaseNotes":"New release notes",
               "VersionTitle":"Version 1.2"
            },
            "DeliveryOptions":[
               {
                  "Id":"`example4-2222-cccc-2222-cccccccccccc`",
                  "Details":{
                     "EcrDeliveryOptionDetails":{
                        "DeliveryOptionTitle":"`New Delivery Option Title`",
                        "Description":"New description",
                        "UsageInstructions":"`New usage instructions`",
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

**Helm Chart Delivery Request
Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
   "Catalog":"AWSMarketplace",
   "ChangeSet":[
      {
         "ChangeType":"UpdateDeliveryOptions",
         "Entity":{
            "Identifier":"`example1-abcd-1234-5ef6-7890abcdef12`",
            "Type":"ContainerProduct@1.0"
         },
         "DetailsDocument":{
            "Version":{
               "ReleaseNotes":"New release notes",
               "VersionTitle":"Version 1.2"
            },
            "DeliveryOptions":[
               {
                  "Id":"`example5-2222-cccc-2222-cccccccccccc`",
                  "Details":{
                     "HelmDeliveryOptionDetails":{
                        "DeliveryOptionTitle":"`New Delivery Option Title`",
                        "ContainerImages":[
                           "`111122223333`.dkr.ecr.us-east-1.amazonaws.com/sellername/imagename:1.0"
                        ],
                        "HelmChartUri":"`111122223333`.dkr.ecr.us-east-1.amazonaws.com/sellername/helmname:1.0",
                        "CompatibleServices":[
                           "EKS-Anywhere"
                        ],
                        "Description":"`New description`",
                        "UsageInstructions":"`New usage instructions`",
                        "MarketplaceServiceAccountName":"`new-service-account-name`",
                        "ReleaseName":"`new-release-name`",
                        "Namespace":"`new-cluster-namespace`",
                        "OverrideParameters":[
                           {
                              "Key":"new.parameter.key",
                              "DefaultValue":"`New parameter default value`"
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
            "Identifier":"`example1-abcd-1234-5ef6-7890abcdef12`",
            "Type":"ContainerProduct@1.0"
         },
         "DetailsDocument":{
            "Version":{
               "ReleaseNotes":"`New release notes`",
               "VersionTitle":"`Version 1.2`"
            },
            "DeliveryOptions":[
               {
                  "Id":"`example4-2222-cccc-2222-cccccccccccc`",
                  "Details":{
                     "EksAddOnDeliveryOptionDetails":{
                        "ContainerImages":[
                           "`709825985650`.dkr.ecr.us-east-1.amazonaws.com/`test-seller`/`canary-test-repo-product-6`:mongo"
                        ],
                        "Description":"`Description for delivery option provided by ISV`",
                        "UsageInstructions":"`Usage instructions with launch instructions`",
                        "HelmChartUri":"`709825985650`.dkr.ecr.us-east-1.amazonaws.com/`rocket`/`rocket-product-helm`:1.0",
                        "AddOnName":"`aws-mp-test`",
                        "AddOnVersion":"`1.2.1`",
                        "AddOnType":"networking",
                        "CompatibleKubernetesVersions":[
                           "1.19",
                           "1.20"
                        ],
                        "SupportedArchitectures":[
                           "amd64",
                           "arm64"
                        ],
                        "Namespace":"`my-test-namespace`",
                        "EnvironmentOverrideParameters":[
                           {
                              "Key":"my-field",
                              "Value":"${`AWS_EKS_CLUSTER_NAME`}"
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

Provide information for the fields to add the `UpdateDeliveryOptions`
change type:

For more information about these fields, see [Adding a new version](../userguide/ami-single-ami-products.md#single-ami-adding-version "../userguide/ami-single-ami-products.md#single-ami-adding-version") in the _AWS Marketplace Seller
Guide_.

- `Entity` (object) (required) – Your container-based
  product.

  - `Identifier` (string) (required) – Your product
    ID. For more information, see [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").
  - `Type` (string) (required) – The
    `Type` is based on the delivery method (product type)
    that your product will be using: `ContainerProduct@1.0`.

- `DetailsDocument` (object) (required) – Details of the
  request. It includes any information about the version of your
  container-based product that you would like to update. The included fields
  are all optional, but you must include at least one field to update.

  - `Version` (object) – Details about the software
    version.

    - `VersionTitle` (string) – The title of
      the version that you are creating. Typically this is a
      description of the version, such as `Version
1.1` or simply `1.1`.
      Your buyers will be able to choose the version to deploy
      from a list of all version titles.

    This property can't be updated if the product is already
    published publicly.
    - `ReleaseNotes` (string) – Notes for
      buyers to tell them about changes from one version to the
      next.

  - `DeliveryOptions` (list of objects) – List of
    `DeliveryOption` objects, including the details of
    each:

    - `Id` (string) – Unique identifier for
      the `DeliveryOption` (you can get the unique
      identifier for the `DeliveryOption` by calling
      the `DescribeEntity` action on the product you
      are updating).
    - `Details` (object) – Holds the details
      of a delivery option. Note that this nested details object
      does _not_ need to be
      double-escaped.

      - `EcrDeliveryOptionDetails` (object)
        – The details of the container image delivery
        option.

        - `DeliveryOptionTitle` (string)
          – A short description that allows your
          buyer to choose between your delivery
          options.

        This property can't be updated if the
        product is already published publicly.
        - `ContainerImages` (array of
          strings) – An array of container image URLs
          used by this version. The path will be the
          repository that you have uploaded the image to,
          with the tag for the image used by this version.
          If this field is included, the list must include
          all needed images, even images that are not
          changing.

        This property can't be updated if the
        product is already published publicly.
        - `DeploymentResources` (array of
          objects) – An array of other deployment
          resources needed for the version, such as links to
          Helm charts or other documentation.
          Each resource includes a name to describe it and a
          URL that points at the resource. On the launch
          page for your version, this displays as a list of
          links.

        This property can't be updated if the
        product is already published publicly.

            - `Name` (string) – The text
             of the hyperlink that is shown to the
             buyer.
            - `Url` (string) – The URL
             of the hyperlink shown to the buyer.
        - `CompatibleServices` (array of
          strings) – An array of services that the
          release is compatible with. Valid options:
          `ECS`, `EKS`,
          `ECS-Anywhere`,
          `EKS-Anywhere`, and
          `Bedrock-AgentCore`.
        - `AgenticType` The type of runtime agent. Valid options: `AGENT`,
          `MCP_SERVER`, or `A2A_SERVER`.
        - `Description` (string) – A
          longer description of the delivery option to give
          details to your buyer. You can also include a link
          to more instructions hosted elsewhere.
        - `UsageInstructions` (string)
          – Provide instructions on how to deploy and
          use your product. You can also add a link to usage
          instructions hosted elsewhere. Can be up to 4,000
          characters.
        - `EnvironmentVariables` – List of environment variables that are required by the AgentCore Runtime container and that will be pre-populated for buyers upon deployment. For each variable, provide an object with the _name_ as expected by your container, a _description_, and an optional _defaultValue_. For variables such as credentials or API keys that are unique, do not provide a default value. You can use the description to specify details about the variable as well as possible values. All of the provided variables with their default values will be pre-populated when buyers launch your product.

    - `Id` (string) – Unique identifier for
      the `DeliveryOption` (you can get the unique
      identifier for the `DeliveryOption` by calling
      the `DescribeEntity` action on the product you
      are updating).
    - `Details` (object) – Holds the details
      of a delivery option. Note that this nested details object
      does _not_ need to be
      double-escaped.

      - `HelmDeliveryOptionDetails` (object)
        – The details of the Helm
        chart delivery option.

        - `DeliveryOptionTitle` (string)
          – A short description that allows your
          buyer to choose between your delivery
          options.

        This property can't be updated if the
        product is already published publicly.
        - `ContainerImages` (array of
          strings) – An array of container image URLs
          used by this version. The path will be the
          repository that you have uploaded the image to,
          with the tag for the image used by this version.
          The list must include all needed images, even
          images that have not changed from previous
          versions. See the next section for information
          about creating repositories using the Catalog
          API.
        - `HelmChartUri` (string) –
          The URL to the Helm chart hosted in
          Amazon ECR that the buyer will install to launch the
          software.
        - `CompatibleServices` (array of
          strings) – An array of services that the
          release is compatible with. Valid options are
          `ECS` and `EKS`.
        - `Description` (string) – A
          longer description of the delivery option to give
          details to your buyer. You can also include a link
          to more instructions provided elsewhere.
        - `UsageInstructions` (string)
          – Provide instructions about the usage for
          this delivery option. Can be up to 4,000
          characters.
        - `MarketplaceServiceAccountName`
          (string) – The name of the
          Kubernetes service account. The
          service account will be used to connect to
          AWS Identity and Access Management for permissions to call AWS
          services.
        - `ReleaseName` (string) –
          The name for the Helm release
          provided to the `helm install` command
          that buyers use to launch the software.
        - `Namespace` (string) – The
          Kubernetes namespace where the
          Helm chart will be
          installed.
        - `OverrideParameters` (array of
          objects) – Parameters that will be used in
          the Helm commands that launch the
          application. Buyers can override the default
          values.

          - `Key` (string)– The key
            for the parameter in dot notation
            (override.example.key).
          - `DefaultValue` (string) –
            The default value for this override
            parameter.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "`example123456789012abcdef`",
   "ChangeSetArn": "arn:aws:aws-marketplace:`us-east-1`:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}
```

The change request is added to a queue and processed, including scanning the
container images and other information to ensure that it meets the [AWS Marketplace
guidelines for container products](../userguide/container-product-policies.md "../userguide/container-product-policies.md"). This process can take a few minutes
to hours, depending on the number and size of your containers.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").
For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors "work-with-seller-products.md#seller-product-change-set-errors").

**Asynchronous Errors**

The following errors are specific to `UpdateDeliveryOptions` actions in
the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                                               | Error message                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| INCOMPATIBLE_PRODUCT_STATUS                              | Use an existing limited or public product.                                                                                                                                                                                                                                                                                     |
| INCOMPATIBLE_SERVICES                                    | The service list contains incompatible services.<br>[incompatible\_services] Provide a valid list of compatible services.                                                                                                                                                                                                      |
| NO_SERVICE_SPECIFIED                                     | Provide at least 1 compatible service.                                                                                                                                                                                                                                                                                         |
| DUPLICATE_COMPATIBLE_AWS_SERVICES                        | The service list contains duplicate entries. Remove them. Each<br>entry must be unique.                                                                                                                                                                                                                                        |
| INVALID_VERSION_TITLE                                    | Remove spaces before the trademark symbol.                                                                                                                                                                                                                                                                                     |
| INVALID_VERSION_TITLE                                    | Remove the following unsupported characters: [x, y, z]                                                                                                                                                                                                                                                                         |
| INVALID_VERSION_TITLE                                    | Remove spaces from the beginning of the version title.                                                                                                                                                                                                                                                                         |
| INVALID_VERSION_TITLE                                    | Provide version title with fewer than [x] characters.                                                                                                                                                                                                                                                                          |
| DUPLICATE_VERSION_TITLE                                  | The version title [duplicate\_version\_title] is a duplicate.<br>Remove or change the title.                                                                                                                                                                                                                                   |
| INVALID_RELEASE_NOTES                                    | Remove spaces before the trademark symbol.                                                                                                                                                                                                                                                                                     |
| INVALID_RELEASE_NOTES                                    | Remove unsupported characters: [x, y, z]                                                                                                                                                                                                                                                                                       |
| INVALID_RELEASE_NOTES                                    | Remove spaces from the beginning of release notes.                                                                                                                                                                                                                                                                             |
| INVALID_RELEASE_NOTES                                    | Provide release notes with fewer than (x) characters.                                                                                                                                                                                                                                                                          |
| INVALID_USAGE_INSTRUCTIONS                               | Remove spaces before the trademark symbol.                                                                                                                                                                                                                                                                                     |
| INVALID_USAGE_INSTRUCTIONS                               | Remove unsupported characters: [x, y, z]                                                                                                                                                                                                                                                                                       |
| INVALID_USAGE_INSTRUCTIONS                               | Provide usage instructions with fewer than (x) characters.                                                                                                                                                                                                                                                                     |
| INVALID_USAGE_INSTRUCTIONS                               | Provide usage instructions.                                                                                                                                                                                                                                                                                                    |
| MISSING_CONTAINER_IMAGES                                 | Provide at least 1 container image.                                                                                                                                                                                                                                                                                            |
| TOO_MANY_CONTAINER_IMAGES                                | Provide fewer than 50 container images.                                                                                                                                                                                                                                                                                        |
| DUPLICATE_CONTAINER_IMAGES                               | The container image list contains duplicate images:<br>[duplicate\_images]. Provide a list with unique images.                                                                                                                                                                                                                 |
| INVALID_CONTAINER_IMAGES                                 | Provide a valid URI for the container image.                                                                                                                                                                                                                                                                                   |
| INVALID_CONTAINER_IMAGE_URI                              | The image [invalid\_image\_uri] doesn't have access to this<br>product. Upload the image to its corresponding product repository.<br>For information about uploading, see [Getting started with container<br>products](../userguide/container-product-getting-started.md "../userguide/container-product-getting-started.md"). |
| INVALID_CONTAINER_IMAGE_TAG                              | Avoid using 'latest' tag.                                                                                                                                                                                                                                                                                                      |
| MISSING_DELIVERY_OPTION_IDS                              | Provide delivery option from existing list of Ids.                                                                                                                                                                                                                                                                             |
| EMPTY_DELIVERY_OPTION_IDS                                | Provide non-empty list of delivery option IDs.                                                                                                                                                                                                                                                                                 |
| DUPLICATE_DELIVERY_OPTION_IDS                            | Duplicate delivery option IDs: [duplicate\_ids]. Provide unique<br>delivery option IDs.                                                                                                                                                                                                                                        |
| DUPLICATE_DELIVERY_OPTION_TITLES                         | Duplicate delivery option titles: [duplicate\_titles]. Remove the<br>duplicates                                                                                                                                                                                                                                                |
| INVALID_DELIVERY_OPTION_TITLES                           | The delivery option titles [existing\_titles] already exist.<br>Provide a different title.                                                                                                                                                                                                                                     |
| INVALID_FULFILLMENT_OPTION_TITLE                         | Provide delivery option title with fewer than (x) characters.                                                                                                                                                                                                                                                                  |
| EMPTY_RESOURCE_NAME                                      | Provide resource name.                                                                                                                                                                                                                                                                                                         |
| EMPTY_RESOURCE_URL                                       | Provide resource URL.                                                                                                                                                                                                                                                                                                          |
| INVALID_RESOURCE_NAME                                    | Provide resource name with fewer than 256 characters.                                                                                                                                                                                                                                                                          |
| INVALID_RESOURCE_URL                                     | Provide resource URL with fewer than 256 characters.                                                                                                                                                                                                                                                                           |
| INVALID_SHORT_DESCRIPTION                                | Provide a short description with fewer than 1,000 characters.                                                                                                                                                                                                                                                                  |
| INVALID_SHORT_DESCRIPTION                                | Provide short description.                                                                                                                                                                                                                                                                                                     |
| NO_LICENSE_SECRET_KEYS                                   | For Amazon EKS Anywhere products, provide 1 override parameter for<br>license secret. Needs `DefaultValue` of<br>`"${AWSMP_LICENSE_SECRET}"`, see example in section.                                                                                                                                                          |
| NO_SERVICE_ACCOUNT_CONFIGURATION                         | For paid products, provide 1 override parameter for service<br>account configuration. Needs `DefaultValue` of<br>`"${AWSMP_SERVICE_ACCOUNT}"`, see example in section.                                                                                                                                                         |
| SCAN_ERROR                                               | Fix security vulnerability ""[y]"" on Image ""[x]"".                                                                                                                                                                                                                                                                           |
| FIELD_NOT_ALLOWED_TO_CHANGE                              | Field [x] cannot be changed.                                                                                                                                                                                                                                                                                                   |
| INVALID_DELIVERY_OPTIONS_STATUS                          | The delivery option IDs [invalid\_ids] are invalid. Provide<br>delivery options in the limited or public state.                                                                                                                                                                                                                |
| NO_CHANGE_FOUND                                          | Provide at least 1 change.                                                                                                                                                                                                                                                                                                     |
| MULTIPLE_VERSION_UPDATE                                  | Provide delivery option IDs from the same version.                                                                                                                                                                                                                                                                             |
| OVERRIDE_PARAMETER_KEYS_CONTAINS_SPECIAL_CHARS           | The override parameter keys [invalid\_keys] contain invalid<br>characters. You keys must use only letters, numbers, double quotes<br>(“ ”) and plus signs (+).                                                                                                                                                                 |
| INVALID_CONTAINER_IMAGE_REPOSITORY                       | The repositories [invalid\_repositories] are invalid. Provide<br>repositories created through the AddRepositories change<br>type.                                                                                                                                                                                              |
| INVALID_CONTAINER_IMAGE_TAG_FORMAT                       | The container image tag [invalid\_image\_tag] is invalid. Provide a<br>tag conforming to the {CONTAINER_IMAGE_TAG_REGEX} regular<br>expression.                                                                                                                                                                                |
| DUPLICATE_OVERRIDE_PARAMETER_KEYS                        | The override parameters contain duplicate keys [duplicate\_keys].<br>Remove the duplicates.                                                                                                                                                                                                                                    |
| UNSUPPORTED_CONTAINER_IMAGE_URI                          | The container image [unsupported\_image] is unsupported. Provide<br>an image that follows the [Image Manifest V 2, Schema 1](https://docker-docs.uclv.cu/registry/spec/manifest-v2-1/ "https://docker-docs.uclv.cu/registry/spec/manifest-v2-1/").                                                                             |
| INVALID_NAMESPACE                                        | The namespace values [invalid\_namespaces] are invalid. Provide<br>values that conform to the {HELM_RELEASE_PARAM_REGEX} regular<br>expression.                                                                                                                                                                                |
| INVALID_RELEASE_NAME                                     | The releaseName values [invalid\_release\_names] are invalid.<br>Provide values that conform to the {HELM_RELEASE_PARAM_REGEX}<br>regular expression.                                                                                                                                                                          |
| OVERRIDE_PARAMETER_KEYS_CONTAINS_RESERVED_PARAMETER_KEYS | The override parameter key for delivery option titles<br>[invalid\_keys] is reserved. Reserved keys: [reserved\_param\_keys].<br>Provide a different key.                                                                                                                                                                      |
| INCOMPATIBLE_ADDON_NAME                                  | The add-on name [provided\_name] does not match the existing name.<br>Reuse the existing name from the public version, or previous<br>versions, of this add-on. You can only use one add-on name for each<br>product.                                                                                                          |
| INCOMPATIBLE_ADDON_NAMESPACE                             | The add-on namespace [provided\_namespace] does not match the<br>existing namespace . Reuse the existing namespace from the public<br>version, or previous versions, of this add-on. You can only use one<br>add-on namespace for each product.                                                                                |

## Restrict a version

You can use the Catalog API to restrict a version of your container-based product
in AWS Marketplace. This prevents new buyers from being able to use that version. There must
be at least one publicly available version in a product. You cannot restrict the
only remaining publicly available version for a product.

To restrict a version, call the `StartChangeSet` API operation with the
`RestrictDeliveryOptions` change type, as shown in the following
example.

###### Note

Restricting one or more, but not all, delivery options from a version will
remove those options from being available to your buyers. Restricting all
delivery options for a version will remove that version from the AWS Marketplace
catalog.

Restricting an Amazon EKS add-on is currently not supported through the Catalog
API.

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
        "Identifier": "`example1-abcd-1234-5ef6-7890abcdef12`",
        "Type": "ContainerProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptionIds":
        [
          "`example1-2222-cccc-2222-cccccccccccc`"
        ]
      }
    }
  ]
}

```

Provide information for the fields to add the `RestrictDeliveryOptions`
change type:

- `Entity` (object) (required) – Your container-based
  product.

  - `Identifier` (string) (required) – Your product
    ID. For more information, see [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").
  - `Type` (string) (required) – The
    `Type` is based on the delivery method (product type)
    that your product will be using: `ContainerProduct@1.0`.

- `DetailsDocument` (object) (required) – Details of the
  request. It includes IDs for the delivery options of your container-based
  product that you would like to restrict.

  - `DeliveryOptionIds` (array of strings) – List of
    `DeliveryOption` IDs for the versions that you want
    to restrict. You can get the unique identifier for the
    `DeliveryOption` by calling the
    `DescribeEntity` action on the product you are
    restricting.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "`example123456789012abcdef`",
   "ChangeSetArn": "arn:aws:aws-marketplace:`us-east-1`:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}
```

The change request is added to a queue and processed. This process can take a few
minutes to hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").
For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors "work-with-seller-products.md#seller-product-change-set-errors").

**Asynchronous Errors**

The following errors are specific to `RestrictDeliveryOptions` actions
in the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                              | Error message                                                                                        |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| INCOMPATIBLE_PRODUCT_STATUS             | Use a public product.                                                                                |
| MISSING_DELIVERY_OPTION_IDS             | Provide delivery option from existing list of IDs.                                                   |
| INVALID_DELIVERY_OPTIONS_STATUS         | The delivery option IDs [invalid\_ids] are invalid. Provide<br>delivery options in the public state. |
| EMPTY_DELIVERY_OPTION_IDS               | Provide non-empty list of delivery option IDs.                                                       |
| INVALID_MINIMUM_PUBLIC_DELIVERY_OPTIONS | Cannot restrict all delivery option IDs.                                                             |
| DUPLICATE_DELIVERY_OPTION_IDS           | Duplicate delivery option IDs: [duplicate\_ids]. Provide unique<br>delivery option IDs.              |
