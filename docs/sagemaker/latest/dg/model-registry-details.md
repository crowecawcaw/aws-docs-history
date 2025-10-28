# Update the Details of a Model

Version

You can view and update details of a specific model version by using either the
AWS SDK for Python (Boto3) or the Amazon SageMaker Studio console.

###### Important

Amazon SageMaker AI integrates Model Cards into Model Registry. A model package registered in the
Model Registry includes a simplified Model Card as a component of the model package. For
more information, see [Model package model card schema
(Studio)](#model-card-schema "#model-card-schema").

## View and Update the Details of a

Model Version (Boto3)

To view the details of a model version by using Boto3, complete the following
steps.

1. Call the `list_model_packages` API operation to view the
   model versions in a Model Group.

```
sm_client.list_model_packages(ModelPackageGroupName="ModelGroup1")
```

The response is a list of model package summaries. You can get the
Amazon Resource Name (ARN) of the model versions from this list.

```
{'ModelPackageSummaryList': [{'ModelPackageGroupName': 'AbaloneMPG-16039329888329896',
   'ModelPackageVersion': 1,
   'ModelPackageArn': 'arn:aws:sagemaker:us-east-2:123456789012:model-package/ModelGroup1/1',
   'ModelPackageDescription': 'TestMe',
   'CreationTime': datetime.datetime(2020, 10, 29, 1, 27, 46, 46000, tzinfo=tzlocal()),
   'ModelPackageStatus': 'Completed',
   'ModelApprovalStatus': 'Approved'}],
 'ResponseMetadata': {'RequestId': '12345678-abcd-1234-abcd-aabbccddeeff',
  'HTTPStatusCode': 200,
  'HTTPHeaders': {'x-amzn-requestid': '12345678-abcd-1234-abcd-aabbccddeeff',
   'content-type': 'application/x-amz-json-1.1',
   'content-length': '349',
   'date': 'Mon, 23 Nov 2020 04:56:50 GMT'},
  'RetryAttempts': 0}}
```

2. Call `describe_model_package` to see the details of the
   model version. You pass in the ARN of a model version that you got in
   the output of the call to `list_model_packages`.

```
sm_client.describe_model_package(ModelPackageName="arn:aws:sagemaker:us-east-2:123456789012:model-package/ModelGroup1/1")
```

The output of this call is a JSON object with the model version
details.

```
{'ModelPackageGroupName': 'ModelGroup1',
 'ModelPackageVersion': 1,
 'ModelPackageArn': 'arn:aws:sagemaker:us-east-2:123456789012:model-package/ModelGroup/1',
 'ModelPackageDescription': 'Test Model',
 'CreationTime': datetime.datetime(2020, 10, 29, 1, 27, 46, 46000, tzinfo=tzlocal()),
 'InferenceSpecification': {'Containers': [{'Image': '257758044811.dkr.ecr.us-east-2.amazonaws.com/sagemaker-xgboost:1.0-1-cpu-py3',
    'ImageDigest': 'sha256:99fa602cff19aee33297a5926f8497ca7bcd2a391b7d600300204eef803bca66',
    'ModelDataUrl': 's3://sagemaker-us-east-2-123456789012/ModelGroup1/pipelines-0gdonccek7o9-AbaloneTrain-stmiylhtIR/output/model.tar.gz'}],
  'SupportedTransformInstanceTypes': ['ml.m5.xlarge'],
  'SupportedRealtimeInferenceInstanceTypes': ['ml.t2.medium', 'ml.m5.xlarge'],
  'SupportedContentTypes': ['text/csv'],
  'SupportedResponseMIMETypes': ['text/csv']},
 'ModelPackageStatus': 'Completed',
 'ModelPackageStatusDetails': {'ValidationStatuses': [],
  'ImageScanStatuses': []},
 'CertifyForMarketplace': False,
 'ModelApprovalStatus': 'PendingManualApproval',
 'LastModifiedTime': datetime.datetime(2020, 10, 29, 1, 28, 0, 438000, tzinfo=tzlocal()),
 'ResponseMetadata': {'RequestId': '12345678-abcd-1234-abcd-aabbccddeeff',
  'HTTPStatusCode': 200,
  'HTTPHeaders': {'x-amzn-requestid': '212345678-abcd-1234-abcd-aabbccddeeff',
   'content-type': 'application/x-amz-json-1.1',
   'content-length': '1038',
   'date': 'Mon, 23 Nov 2020 04:59:38 GMT'},
  'RetryAttempts': 0}}
```

### Model package model card schema

(Studio)

All details related to the model version are encapsulated in the model
package’s model card. The model card of a model package is a special usage
of the Amazon SageMaker Model Card and its schema is simplified. The model package model card
schema is shown in the following expandable dropdown.

```
{
  "title": "SageMakerModelCardSchema",
  "description": "Schema of a model package’s model card.",
  "version": "0.1.0",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "model_overview": {
      "description": "Overview about the model.",
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "model_creator": {
          "description": "Creator of model.",
          "type": "string",
          "maxLength": 1024
        },
        "model_artifact": {
          "description": "Location of the model artifact.",
          "type": "array",
          "maxContains": 15,
          "items": {
            "type": "string",
            "maxLength": 1024
          }
        }
      }
    },
    "intended_uses": {
      "description": "Intended usage of model.",
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "purpose_of_model": {
          "description": "Reason the model was developed.",
          "type": "string",
          "maxLength": 2048
        },
        "intended_uses": {
          "description": "Intended use cases.",
          "type": "string",
          "maxLength": 2048
        },
        "factors_affecting_model_efficiency": {
          "type": "string",
          "maxLength": 2048
        },
        "risk_rating": {
          "description": "Risk rating for model card.",
          "$ref": "#/definitions/risk_rating"
        },
        "explanations_for_risk_rating": {
          "type": "string",
          "maxLength": 2048
        }
      }
    },
    "business_details": {
      "description": "Business details of model.",
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "business_problem": {
          "description": "Business problem solved by the model.",
          "type": "string",
          "maxLength": 2048
        },
        "business_stakeholders": {
          "description": "Business stakeholders.",
          "type": "string",
          "maxLength": 2048
        },
        "line_of_business": {
          "type": "string",
          "maxLength": 2048
        }
      }
    },
    "training_details": {
      "description": "Overview about the training.",
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "objective_function": {
          "description": "The objective function for which the model is optimized.",
          "function": {
            "$ref": "#/definitions/objective_function"
          },
          "notes": {
            "type": "string",
            "maxLength": 1024
          }
        },
        "training_observations": {
          "type": "string",
          "maxLength": 1024
        },
        "training_job_details": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "training_arn": {
              "description": "SageMaker Training job ARN.",
              "type": "string",
              "maxLength": 1024
            },
            "training_datasets": {
              "description": "Location of the model datasets.",
              "type": "array",
              "maxContains": 15,
              "items": {
                "type": "string",
                "maxLength": 1024
              }
            },
            "training_environment": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "container_image": {
                  "description": "SageMaker training image URI.",
                  "type": "array",
                  "maxContains": 15,
                  "items": {
                    "type": "string",
                    "maxLength": 1024
                  }
                }
              }
            },
            "training_metrics": {
              "type": "array",
              "items": {
                "maxItems": 50,
                "$ref": "#/definitions/training_metric"
              }
            },
            "user_provided_training_metrics": {
              "type": "array",
              "items": {
                "maxItems": 50,
                "$ref": "#/definitions/training_metric"
              }
            },
            "hyper_parameters": {
              "type": "array",
              "items": {
                "maxItems": 100,
                "$ref": "#/definitions/training_hyper_parameter"
              }
            },
            "user_provided_hyper_parameters": {
              "type": "array",
              "items": {
                "maxItems": 100,
                "$ref": "#/definitions/training_hyper_parameter"
              }
            }
          }
        }
      }
    },
    "evaluation_details": {
      "type": "array",
      "default": [],
      "items": {
        "type": "object",
        "required": [
          "name"
        ],
        "additionalProperties": false,
        "properties": {
          "name": {
            "type": "string",
            "pattern": ".{1,63}"
          },
          "evaluation_observation": {
            "type": "string",
            "maxLength": 2096
          },
          "evaluation_job_arn": {
            "type": "string",
            "maxLength": 256
          },
          "datasets": {
            "type": "array",
            "items": {
              "type": "string",
              "maxLength": 1024
            },
            "maxItems": 10
          },
          "metadata": {
            "description": "Additional attributes associated with the evaluation results.",
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "maxLength": 1024
            }
          },
          "metric_groups": {
            "type": "array",
            "default": [],
            "items": {
              "type": "object",
              "required": [
                "name",
                "metric_data"
              ],
              "properties": {
                "name": {
                  "type": "string",
                  "pattern": ".{1,63}"
                },
                "metric_data": {
                  "type": "array",
                  "items": {
                    "anyOf": [
                      {
                        "$ref": "#/definitions/simple_metric"
                      },
                      {
                        "$ref": "#/definitions/linear_graph_metric"
                      },
                      {
                        "$ref": "#/definitions/bar_chart_metric"
                      },
                      {
                        "$ref": "#/definitions/matrix_metric"
                      }
                    ]

                  }
                }
              }
            }
          }
        }
      }
    },
    "additional_information": {
      "additionalProperties": false,
      "type": "object",
      "properties": {
        "ethical_considerations": {
          "description": "Ethical considerations for model users.",
          "type": "string",
          "maxLength": 2048
        },
        "caveats_and_recommendations": {
          "description": "Caveats and recommendations for model users.",
          "type": "string",
          "maxLength": 2048
        },
        "custom_details": {
          "type": "object",
          "additionalProperties": {
            "$ref": "#/definitions/custom_property"
          }
        }
      }
    }
  },
  "definitions": {
    "source_algorithms": {
      "type": "array",
      "minContains": 1,
      "maxContains": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "algorithm_name"
        ],
        "properties": {
          "algorithm_name": {
            "description": "The name of the algorithm used to create the model package. The algorithm must be either an algorithm resource in your SageMaker AI account or an algorithm in AWS Marketplace that you are subscribed to.",
            "type": "string",
            "maxLength": 170
          },
          "model_data_url": {
            "description": "Amazon S3 path where the model artifacts, which result from model training, are stored.",
            "type": "string",
            "maxLength": 1024
          }
        }
      }
    },
    "inference_specification": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "containers"
      ],
      "properties": {
        "containers": {
          "description": "Contains inference related information used to create model package.",
          "type": "array",
          "minContains": 1,
          "maxContains": 15,
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "image"
            ],
            "properties": {
              "model_data_url": {
                "description": "Amazon S3 path where the model artifacts, which result from model training, are stored.",
                "type": "string",
                "maxLength": 1024
              },
              "image": {
                "description": "Inference environment path. The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.",
                "type": "string",
                "maxLength": 255
              },
              "nearest_model_name": {
                "description": "The name of a pre-trained machine learning benchmarked by an Amazon SageMaker Inference Recommender model that matches your model.",
                "type": "string"
              }
            }
          }
        }
      }
    },
    "risk_rating": {
      "description": "Risk rating of model.",
      "type": "string",
      "enum": [
        "High",
        "Medium",
        "Low",
        "Unknown"
      ]
    },
    "custom_property": {
      "description": "Additional property.",
      "type": "string",
      "maxLength": 1024
    },
    "objective_function": {
      "description": "Objective function for which the training job is optimized.",
      "additionalProperties": false,
      "properties": {
        "function": {
          "type": "string",
          "enum": [
            "Maximize",
            "Minimize"
          ]
        },
        "facet": {
          "type": "string",
          "maxLength": 63
        },
        "condition": {
          "type": "string",
          "maxLength": 63
        }
      }
    },
    "training_metric": {
      "description": "Training metric data.",
      "type": "object",
      "required": [
        "name",
        "value"
      ],
      "additionalProperties": false,
      "properties": {
        "name": {
          "type": "string",
          "pattern": ".{1,255}"
        },
        "notes": {
          "type": "string",
          "maxLength": 1024
        },
        "value": {
          "type": "number"
        }
      }
    },
    "training_hyper_parameter": {
      "description": "Training hyperparameter.",
      "type": "object",
      "required": [
        "name",
        "value"
      ],
      "additionalProperties": false,
      "properties": {
        "name": {
          "type": "string",
          "pattern": ".{1,255}"
        },
        "value": {
          "type": "string",
          "pattern": ".{1,255}"
        }
      }
    },
    "linear_graph_metric": {
      "type": "object",
      "required": [
        "name",
        "type",
        "value"
      ],
      "additionalProperties": false,
      "properties": {
        "name": {
          "type": "string",
          "pattern": ".{1,255}"
        },
        "notes": {
          "type": "string",
          "maxLength": 1024
        },
        "type": {
          "type": "string",
          "enum": [
            "linear_graph"
          ]
        },
        "value": {
          "anyOf": [
            {
              "type": "array",
              "items": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "minItems": 1
            }
          ]
        },
        "x_axis_name": {
          "$ref": "#/definitions/axis_name_string"
        },
        "y_axis_name": {
          "$ref": "#/definitions/axis_name_string"
        }
      }
    },
    "bar_chart_metric": {
      "type": "object",
      "required": [
        "name",
        "type",
        "value"
      ],
      "additionalProperties": false,
      "properties": {
        "name": {
          "type": "string",
          "pattern": ".{1,255}"
        },
        "notes": {
          "type": "string",
          "maxLength": 1024
        },
        "type": {
          "type": "string",
          "enum": [
            "bar_chart"
          ]
        },
        "value": {
          "anyOf": [
            {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 1
            }
          ]
        },
        "x_axis_name": {
          "$ref": "#/definitions/axis_name_array"
        },
        "y_axis_name": {
          "$ref": "#/definitions/axis_name_string"
        }
      }
    },
    "matrix_metric": {
      "type": "object",
      "required": [
        "name",
        "type",
        "value"
      ],
      "additionalProperties": false,
      "properties": {
        "name": {
          "type": "string",
          "pattern": ".{1,255}"
        },
        "notes": {
          "type": "string",
          "maxLength": 1024
        },
        "type": {
          "type": "string",
          "enum": [
            "matrix"
          ]
        },
        "value": {
          "anyOf": [
            {
              "type": "array",
              "items": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 1,
                "maxItems": 20
              },
              "minItems": 1,
              "maxItems": 20
            }
          ]
        },
        "x_axis_name": {
          "$ref": "#/definitions/axis_name_array"
        },
        "y_axis_name": {
          "$ref": "#/definitions/axis_name_array"
        }
      }
    },
    "simple_metric": {
      "description": "Metric data.",
      "type": "object",
      "required": [
        "name",
        "type",
        "value"
      ],
      "additionalProperties": false,
      "properties": {
        "name": {
          "type": "string",
          "pattern": ".{1,255}"
        },
        "notes": {
          "type": "string",
          "maxLength": 1024
        },
        "type": {
          "type": "string",
          "enum": [
            "number",
            "string",
            "boolean"
          ]
        },
        "value": {
          "anyOf": [
            {
              "type": "number"
            },
            {
              "type": "string",
              "maxLength": 63
            },
            {
              "type": "boolean"
            }
          ]
        },
        "x_axis_name": {
          "$ref": "#/definitions/axis_name_string"
        },
        "y_axis_name": {
          "$ref": "#/definitions/axis_name_string"
        }
      }
    },
    "axis_name_array": {
      "type": "array",
      "items": {
        "type": "string",
        "maxLength": 63
      }
    },
    "axis_name_string": {
      "type": "string",
      "maxLength": 63
    }
  }
}
```

## View and Update the Details of a

Model Version (Studio or Studio Classic)

To view and update the details of a model version, complete the following
steps based on whether you use Studio or Studio Classic. In Studio Classic, you can
update the approval status for a model version. For details, see [Update the Approval Status of a
Model](model-registry-approve.md "model-registry-approve.md").
In Studio, on the other hand, SageMaker AI creates a model card for a model
package, and the model version UI provides options to update details in the
model card.

Studio

1. Open the SageMaker Studio console by following the
   instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose
   **Models** from the menu.
3. Choose the **Registered models** tab, if
   not selected already.
4. Immediately below the **Registered
   models** tab label, choose **Model
   Groups**, if not selected already.
5. Select the name of the model group containing the model
   version to view.
6. In the list of model versions, select the model version to
   view.
7. Choose one of the following tabs.
   - **Training**: To view or edit
     details related to your training job, including
     performance metrics, artifacts, IAM role and
     encryption, and containers. For more information,
     see [Add a training job
     (Studio)](model-registry-details-studio-training.md "model-registry-details-studio-training.md").
   - **Evaluate**: To view or edit
     details related to your training job, such as
     performance metrics, evaluation datasets, and
     security. For more information, see [Add an evaluation job
     (Studio)](model-registry-details-studio-evaluate.md "model-registry-details-studio-evaluate.md").
   - **Audit**: To view or edit
     high-level details related to the model’s business
     purpose, usage, risk, and technical details such as
     algorithm and performance limitations. For more
     information, see [Update audit (governance)
     information (Studio)](model-registry-details-studio-audit.md "model-registry-details-studio-audit.md").
   - **Deploy**: To view or edit the
     location of your inference image container and
     instances which compose the endpoint. For more
     information, see [Update deployment
     information (Studio)](model-registry-details-studio-deploy.md "model-registry-details-studio-deploy.md").

Studio Classic

1. Sign in to Amazon SageMaker Studio Classic. For more information, see
   [Launch
   Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. In the left navigation pane, choose the
   **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Choose **Models**, and then
   **Model registry**.
4. From the model groups list, select the name of the Model
   Group you want to view.
5. A new tab appears with a list of the model versions in the
   Model Group.
6. In the list of model versions, select the name of the
   model version for which you want to view details.
7. On the model version tab that opens, choose one of the
   following to see details about the model version:
   - **Activity**: Shows events for
     the model version, such as approval status
     updates.
   - **Model quality**: Reports
     metrics related to your Model Monitor model quality checks,
     which compare model predictions to Ground Truth. For more
     information about Model Monitor model quality checks, see
     [Model quality](model-monitor-model-quality.md "model-monitor-model-quality.md").
   - **Explainability**: Reports
     metrics related to your Model Monitor feature attribution
     checks, which compare the relative rankings of your
     features in training data versus live data. For more
     information about Model Monitor explainability checks, see
     [Feature
     attribution drift for models in production](clarify-model-monitor-feature-attribution-drift.md "clarify-model-monitor-feature-attribution-drift.md").
   - **Bias**: Reports metrics related
     to your Model Monitor bias drift checks, which compare the
     distribution of live data to training data. For more
     information about Model Monitor bias drift checks, see [Bias drift for models in
     production](clarify-model-monitor-bias-drift.md "clarify-model-monitor-bias-drift.md").
   - **Inference recommender**:
     Provides initial instance recommendations for
     optimal performance based on your model and sample
     payloads.
   - **Load test**: Runs load tests
     across your choice of instance types when you
     provide your specific production requirements, such
     as latency and throughput constraints.
   - **Inference specification**:
     Displays instance types for your real-time inference
     and transform jobs, and information about your Amazon ECR
     containers.
   - **Information**: Shows
     information such as the project with which the model
     version is associated, the pipeline that generated
     the model, the Model Group, and the model's location
     in Amazon S3.
