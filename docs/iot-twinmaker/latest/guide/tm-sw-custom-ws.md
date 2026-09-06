

# Using a custom workspace
<a name="tm-sw-custom-ws"></a>

Review these prerequisites before turning on asset sync.

## Prerequisites
<a name="tm-sw-asset-sync-use-prereqs"></a>

Before using AWS IoT SiteWise, the following must be completed:
+ You have an AWS IoT TwinMaker workspace.
+ You have assets and asset models in AWS IoT SiteWise. For more information, see [Creating asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-asset-models.html).
+ An existing IAM role with read permissions for the following AWS IoT SiteWise actions: 
  + `ListAssets`
  + `ListAssetModels`
  +  `DescribeAsset`
  + `DescribeAssetModel`
+ The IAM role must have the following write permissions for AWS IoT TwinMaker:
  + `CreateEntity`
  + `UpdateEntity`
  + `DeleteEntity`
  + `CreateComponentType`
  + `UpdateComponentType`
  + `DeleteComponentType`
  + `ListEntities`
  + `GetEntity`
  + `ListComponentTypes`

  Use the following IAM role as a template for the required role:

  ```
                              
  // trust relationships
   {
      {
          "Version": "2012-10-17",		 	 	 
          "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
              "Service": [
              "iottwinmaker.amazonaws.com"
              ]
          },
              "Action": "sts:AssumeRole"
          }
      ]
  }
  
  // permissions - replace ACCOUNT_ID, REGION, WORKSPACE_ID with actual values
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [{
              "Sid": "SiteWiseAssetReadAccess",
              "Effect": "Allow",
              "Action": [
                  "iotsitewise:DescribeAsset"
              ],
              "Resource": [
                  "arn:aws:iotsitewise:{{REGION:ACCOUNT_ID}}:asset/*"
              ]
          },
          {
              "Sid": "SiteWiseAssetModelReadAccess",
              "Effect": "Allow",
              "Action": [
                  "iotsitewise:DescribeAssetModel"
              ],
              "Resource": [
                  "arn:aws:iotsitewise:{{REGION:ACCOUNT_ID}}:asset-model/*"
              ]
          },
          {
              "Sid": "SiteWiseAssetModelAndAssetListAccess",
              "Effect": "Allow",
              "Action": [
                  "iotsitewise:ListAssets",
                  "iotsitewise:ListAssetModels"
              ],
              "Resource": [
                  "*"
              ]
          },
          {
              "Sid": "TwinMakerAccess",
              "Effect": "Allow",
              "Action": [
                  "iottwinmaker:GetEntity",
                  "iottwinmaker:CreateEntity",
                  "iottwinmaker:UpdateEntity",
                  "iottwinmaker:DeleteEntity",
                  "iottwinmaker:ListEntities",
                  "iottwinmaker:GetComponentType",
                  "iottwinmaker:CreateComponentType",
                  "iottwinmaker:UpdateComponentType",
                  "iottwinmaker:DeleteComponentType",
                  "iottwinmaker:ListComponentTypes"
              ],
              "Resource": [
                  "arn:aws:iottwinmaker:{{REGION:ACCOUNT_ID}}:workspace/{{WORKSPACE_ID}}",
                  "arn:aws:iottwinmaker:{{REGION:ACCOUNT_ID}}:workspace/{{WORKSPACE_ID}}/*"          
              ]
          }
      ]
  }
  ```

Use the following procedure to turn on and configure AWS IoT SiteWise asset sync.

1. In the [AWS IoT TwinMaker console](https://console.aws.amazon.com/iottwinmaker/), navigate to the **Settings** page.

1. Open the **Model sources** tab.  
![The AWS IoT TwinMaker console Setting page with the Model sources tab open.](http://docs.aws.amazon.com/iot-twinmaker/latest/guide/images/asset-sync-settings.png)

1. Choose **Connect workspace** to link your AWS IoT TwinMaker workspace to your AWS IoT SiteWise assets.
**Note**  
You can only use asset sync with a single AWS IoT TwinMaker workspace. You must disconnect the sync from one workspace and connect to another workspace to if you wish to sync in a different workspace.

1. Next, navigate to the workspace in which you want to use asset sync.

1. Choose **Add sources**. This opens the **Add entity model source** page.  
![The Add entity model source page.](http://docs.aws.amazon.com/iot-twinmaker/latest/guide/images/add-model-source.png)

1. On the **Add entity model source** page, confirm that the source field displays **AWS IoT SiteWise**. Select the IAM role you created as a prerequisite for the **IAM role**.

1. You have now turned on AWS IoT SiteWise asset sync. You should see a conformation banner appear at the top of the selected **Workspace** page confirming that asset sync is active. You should also now see a sync source listed in the **Entity model sources** section.  
![The workspace page showing the list of Entity model sources.](http://docs.aws.amazon.com/iot-twinmaker/latest/guide/images/success-sync.png)