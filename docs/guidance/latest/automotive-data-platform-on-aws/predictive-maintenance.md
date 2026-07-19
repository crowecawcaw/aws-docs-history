# Predictive Maintenance

This guidance was developed from operational experience running predictive maintenance algorithms across large commercial vehicle fleets. The architecture patterns, data processing pipelines, and ML approach reflect production-grade patterns proven at fleet scale, but customers connect their own telemetry data sources and tune thresholds to their fleet operations.

The Redshift data source integration reflects a Redshift-based fleet data architecture pattern. For customers using the [CMS](../connected-mobility-on-aws/developer-guide.md "../connected-mobility-on-aws/developer-guide.md"), the telemetry pipeline can be connected directly to this predictive maintenance system — see the integration guide in the [source repository](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws "https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws") for details on signal catalog mapping, batch and real-time integration options, and feeding alerts back to the Fleet Manager UI.

###### Note

The code implementing this pattern is real and present in this same repository at `guidance-for-predictive-maintenance/` — including a complete `TirePredictiveMaintenanceStack` CDK application, Lambda functions, Step Functions ML pipelines, and training notebooks. This directory is not deployed by the `platform-foundation/` foundation deploy’s default path, but it exists, is fully browsable, and can be deployed independently by a customer who wants this specific pattern. This is distinct from how this guide references CMS (a separate product and repository) — `guidance-for-predictive-maintenance/` is real code, right here in this repository, just not wired into the default deploy path.

## Beyond tires: a general pattern for asset failure prediction

This chapter’s reference implementation predicts tire failures from pressure and temperature telemetry — but the underlying pattern is not specific to tires, or even to vehicles. The same shape of problem shows up anywhere a physical asset emits time-series sensor data and an organization wants advance warning before failure: predicting bearing wear from vibration sensors on a manufacturing line, forecasting HVAC compressor failure from temperature and current draw, anticipating battery degradation in stationary energy storage, or scheduling wind-turbine gearbox maintenance from acoustic and torque signals. What generalizes across all of these is the architecture, not the domain: ingest time-series telemetry, engineer features that capture trend and rate-of-change, train an anomaly-detection or forecasting model on data representing normal operation, run inference on new readings, and route high-confidence alerts to a maintenance workflow. Swap the sensor schema and the domain-specific feature engineering, and this same five-stage architecture — ingestion, feature engineering, model training, inference, and alert consolidation — applies to any asset class with a maintenance program.

## Choosing an approach: beyond Random Cut Forest

The reference implementation uses Amazon SageMaker’s Random Cut Forest (RCF) algorithm because it fits this specific case well: it is unsupervised, so it does not require historical examples of tire failures (which are rare and expensive to label), and it scores multivariate signals (pressure, temperature, and their rates of change together) rather than thresholding any single signal in isolation. RCF is a reasonable default when labeled failure data is scarce, but it is one of several AWS-native options, and the right choice depends on what data the asset actually produces:

| Approach                                           | Best fit when                                                                                                                                                                                             | AWS service                                                                                                                                  |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Unsupervised anomaly detection (Random Cut Forest) | Failures are rare, unlabeled, or you cannot wait to accumulate labeled failure examples before shipping a model                                                                                           | [Amazon SageMaker built-in RCF algorithm](../../../sagemaker/latest/dg/randomcutforest.md "../../../sagemaker/latest/dg/randomcutforest.md") |
| Supervised classification (gradient-boosted trees) | You have a history of labeled failure/no-failure events (from work orders, warranty claims, or service records) and want a model that learns the specific signal combinations that preceded past failures | [Amazon SageMaker built-in XGBoost algorithm](../../../sagemaker/latest/dg/xgboost.md "../../../sagemaker/latest/dg/xgboost.md")             |
| Time-series forecasting (remaining useful life)    | You want to forecast a continuous degradation curve (e.g., days until a signal crosses a critical threshold) rather than a binary failure/no-failure classification                                       | [Amazon SageMaker DeepAR+ forecasting algorithm](../../../sagemaker/latest/dg/deepar.md "../../../sagemaker/latest/dg/deepar.md")            |
| No-code model building                             | Domain experts (reliability engineers, maintenance planners) need to build and iterate on models without a data-science team writing training code                                                        | [Amazon SageMaker Canvas](https://aws.amazon.com/sagemaker/canvas/ "https://aws.amazon.com/sagemaker/canvas/")                               |

The filter-based statistical approach in this chapter’s reference implementation (leak-rate regression, threshold alerting) is domain-agnostic in the same way — any asset with a slowly-degrading continuous signal (pressure, vibration amplitude, current draw, temperature) can use the same moving-average-and-slope technique as a lower-cost complement to a trained model, exactly as this chapter’s dual-pipeline design does for tires.

The rest of this chapter walks through the tire reference implementation in full, since a concrete worked example is more useful than an abstract one. Wherever the text below is tire-specific — the pressure schema, the 28 PSI threshold, the leak-rate math — treat it as a stand-in for whatever telemetry and threshold your asset actually produces; the architecture around it is what carries over.

## Key Capabilities

The solution delivers:

- **Advanced Tire Health Monitoring**: Ingests and analyzes tire-related telemetry data from connected vehicles
- **Dual Prediction Approaches**:

  - Machine learning models using Amazon SageMaker Random Cut Forest algorithm
  - Filter-based algorithmic approach for real-time anomaly detection

- **Early Warning System**: Predicts tire failures 7-14 days before they would occur
- **Automated Data Processing**: Root ETL pipeline transforms and merges data from multiple sources using AWS Glue
- **Integration Ready**: Provides alerts in formats compatible with existing maintenance scheduling systems
- **Configurable Alerting**: Customizable thresholds and parameters to optimize alert accuracy and reduce false positives

## Solution Components

The solution consists of four main components:

## Data Ingestion Layer

- **Amazon Redshift Data Source**: Connects to existing telemetry data via Redshift Datashare or S3 unload
- **AWS Glue Root ETL**: Hourly processing pipeline that transforms raw telemetry into analysis-ready formats
- **Data Consolidation**: Merges data from multiple tables into unified datasets for both ML and filtering approaches

## Machine Learning Approach

- **ML ETL Pipeline**: Prepares historical data for model training with feature engineering
- **ML Training Pipeline**: Trains Random Cut Forest models on large pre-processed telemetry datasets
- **ML Inference Pipeline**: Runs batch predictions using Amazon SageMaker to identify anomalies

## Filter-Based Approach

- **Algorithm-Based Detection**: Applies statistical filters to identify tire pressure anomalies in real-time
- **Leak Rate Calculation**: Computes pressure loss rates to determine severity
- **Threshold-Based Alerting**: Generates alerts when leak rates exceed configurable thresholds

## Alert Management System

- **Alert Consolidation**: Combines predictions from both ML and filter-based approaches
- **Severity Classification**: Categorizes alerts by urgency and leak rate
- **Status Tracking**: Monitors alert lifecycle from detection through resolution
- **Integration APIs**: Provides alerts to downstream maintenance scheduling systems
