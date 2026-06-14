# Amazon Fleet Tire Predictive Maintenance

This guidance was developed in collaboration with Amazon’s Middle Mile Transportation team, who operate one of the world’s largest commercial vehicle fleets. The predictive maintenance algorithms and data pipelines were built using real-world fleet telemetry data — tire pressure readings, temperature data, and vehicle operating conditions collected across thousands of vehicles over multiple years.

While the specific algorithms and thresholds may differ from what Amazon uses internally in production, the architecture patterns, data processing pipelines, and ML approach are directly informed by that operational experience. Customers can use this guidance the same way it was built for Amazon’s fleet operations team: deploy the infrastructure, connect your telemetry data source, train the models on your fleet’s data, and tune the alert thresholds to match your maintenance workflows.

The Redshift data source integration reflects the internal architecture used by Amazon’s fleet team. For customers using the [Connected Mobility Guidance](../connected-mobility-on-aws/developer-guide.md "../connected-mobility-on-aws/developer-guide.md"), the CMS telemetry pipeline can be connected directly to this predictive maintenance system — see the integration guide in the [source repository](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws "https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws") for details on signal catalog mapping, batch and real-time integration options, and feeding alerts back to the Fleet Manager UI.

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
