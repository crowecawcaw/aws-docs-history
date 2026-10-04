

# Predictive Maintenance
<a name="predictive-maintenance"></a>

## Overview
<a name="overview"></a>

Predictive maintenance is a first-class use case on the ADP platform. The tire-focused predictive maintenance pipeline demonstrates how to build intelligent maintenance applications — with a roadmap to consume platform-foundation governed data products.

 **Shipped (v0.2.3\+)**: The modernized PM reference implementation includes security updates, the `tire_health` governed data product (now available in the foundation), and a pipeline architecture structured for integration with the foundation’s DataZone subscriptions and Lake Formation access control.

 **In development (v0.2.4)**: The ML pipeline is being refactored to consume governed data products via DataZone instead of standing alone — this enables the pattern shown below where PM reads `vehicle_telemetry_aggregated`, `service_records`, and `tire_health` via Lake Formation-governed Athena queries.

The architecture, when fully integrated, flows through three stages:

1.  **Subscribe to platform data**: DataZone subscription → Lake Formation automatic access grant (planned v0.2.4)

1.  **Join for insights**: Use Athena to query `vehicle_telemetry_aggregated`, `service_records`, and `tire_health` governed products (planned v0.2.4)

1.  **Train and predict**: Build supervised and unsupervised models in Amazon SageMaker to forecast tire failures (reference implementation, v0.2.3\+)

This chapter walks through a concrete worked example: predicting tire wear and pressure anomalies that indicate imminent failure. The same architecture applies to any asset class with rich telemetry and maintenance history — battery health, brake wear, bearing vibration, or any physical component emitting time-series sensor data.

### Why governed data matters for ML (and the roadmap)
<a name="why-governed-data-matters-for-ml-and-the-roadmap"></a>

Traditional predictive maintenance builds from raw telemetry silos — Redshift here, IoT data lake there, maintenance records in a different warehouse. This fragmentation means weeks of data engineering before the first model trains.

Governed data products invert this: they are pre-joined, quality-tested, and discoverable via DataZone. The tire-health product (shipped v0.2.3) combines tire-specific telemetry (pressure, temperature, tread depth), service history (tire rotations, replacements), and vehicle context (VIN, model, fleet) in a single Iceberg table, partitioned for efficient querying, and structured for ML feature engineering.

 **Current state (v0.2.3)**: The PM reference implementation is updated to the latest dependencies and includes the `tire_health` product in the foundation seed data. The PM stack is de-deprecated and first-class, with full source code and test coverage.

 **Roadmap (v0.2.4)**: The next phase wires PM’s ML pipeline to read `tire_health`, `vehicle_telemetry_aggregated`, and `service_records` via Lake Formation-governed Athena instead of from self-contained buckets — which unlocks the full benefit of governed data: shared schema governance, automatic access control, and cross-consumer visibility of which analyses consume which data products.

**Note**  
The reference implementation code is real and present in this same repository at `guidance-for-predictive-maintenance/` — including a complete `TirePredictiveMaintenanceStack` CDK application that provisions the DataZone subscription, Glue ETL roles, and SageMaker notebook instance. See the source repository at [guidance-for-automotive-data-platform-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws) for the full implementation.

### Beyond tires: a general pattern for asset failure prediction
<a name="beyond-tires-a-general-pattern-for-asset-failure-prediction"></a>

This chapter’s reference implementation predicts tire failures from pressure and temperature telemetry — but the underlying pattern is not specific to tires, or even to vehicles. The same shape of problem shows up anywhere a physical asset emits time-series sensor data and an organization wants advance warning before failure: predicting bearing wear from vibration sensors on a manufacturing line, forecasting HVAC compressor failure from temperature and current draw, anticipating battery degradation in stationary energy storage, or scheduling wind-turbine gearbox maintenance from acoustic and torque signals. What generalizes across all of these is the architecture, not the domain: ingest time-series telemetry, engineer features that capture trend and rate-of-change, train an anomaly-detection or forecasting model on data representing normal operation, run inference on new readings, and route high-confidence alerts to a maintenance workflow. Swap the sensor schema and the domain-specific feature engineering, and this same five-stage architecture — ingestion, feature engineering, model training, inference, and alert consolidation — applies to any asset class with a maintenance program.

### Choosing an approach: beyond Random Cut Forest
<a name="choosing-an-approach-beyond-random-cut-forest"></a>

The reference implementation uses Amazon SageMaker’s Random Cut Forest (RCF) algorithm as the current default because it fits this specific case well: it is unsupervised, so it does not require historical examples of tire failures (which are rare and expensive to label), and it scores multivariate signals (pressure, temperature, and their rates of change together) rather than thresholding any single signal in isolation. RCF is a reasonable default when labeled failure data is scarce.

 **In development**: The v0.2.4 roadmap includes support for supervised classification models (XGBoost) trained on the `tire_health` product’s `needs_replacement` and `wear_category` labels, which will give you an option to train on historical tire replacements (sourced from `service_records`) once the governed-data read path is wired.

RCF is one of several AWS-native options, and the right choice depends on what data the asset actually produces:


| Approach | Best fit when | AWS service | 
| --- | --- | --- | 
| Unsupervised anomaly detection (Random Cut Forest) | Failures are rare, unlabeled, or you cannot wait to accumulate labeled failure examples before shipping a model |  [Amazon SageMaker built-in RCF algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/randomcutforest.html)  | 
| Supervised classification (gradient-boosted trees) | You have a history of labeled failure/no-failure events (from work orders, warranty claims, or service records) and want a model that learns the specific signal combinations that preceded past failures |  [Amazon SageMaker built-in XGBoost algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html)  | 
| Time-series forecasting (remaining useful life) | You want to forecast a continuous degradation curve (e.g., days until a signal crosses a critical threshold) rather than a binary failure/no-failure classification |  [Amazon SageMaker DeepAR\+ forecasting algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar.html)  | 
| No-code model building | Domain experts (reliability engineers, maintenance planners) need to build and iterate on models without a data-science team writing training code |  [Amazon SageMaker Canvas](https://aws.amazon.com/sagemaker/canvas/)  | 

The filter-based statistical approach in this chapter’s reference implementation (leak-rate regression, threshold alerting) is domain-agnostic in the same way — any asset with a slowly-degrading continuous signal (pressure, vibration amplitude, current draw, temperature) can use the same moving-average-and-slope technique as a lower-cost complement to a trained model, exactly as this chapter’s dual-pipeline design does for tires.

The rest of this chapter walks through the tire reference implementation in full, since a concrete worked example is more useful than an abstract one. Wherever the text below is tire-specific — the pressure schema, the 28 PSI threshold, the leak-rate math — treat it as a stand-in for whatever telemetry and threshold your asset actually produces; the architecture around it is what carries over.

### Key Capabilities
<a name="key-capabilities"></a>

The solution delivers:
+  **Advanced Tire Health Monitoring**: Ingests and analyzes tire-related telemetry data from connected vehicles
+  **Dual Prediction Approaches**:
  + Machine learning models using Amazon SageMaker Random Cut Forest algorithm
  + Filter-based algorithmic approach for real-time anomaly detection
+  **Early Warning System**: Predicts tire failures 7-14 days before they would occur
+  **Automated Data Processing**: Root ETL pipeline transforms and merges data from multiple sources using AWS Glue
+  **Integration Ready**: Provides alerts in formats compatible with existing maintenance scheduling systems
+  **Configurable Alerting**: Customizable thresholds and parameters to optimize alert accuracy and reduce false positives

### Solution Components
<a name="solution-components"></a>

The solution consists of four main components:

### Data Ingestion Layer
<a name="data-ingestion-layer"></a>
+  **Amazon Redshift Data Source**: Connects to existing telemetry data via Redshift Datashare or S3 unload
+  **AWS Glue Root ETL**: Hourly processing pipeline that transforms raw telemetry into analysis-ready formats
+  **Data Consolidation**: Merges data from multiple tables into unified datasets for both ML and filtering approaches

### Machine Learning Approach
<a name="machine-learning-approach"></a>
+  **ML ETL Pipeline**: Prepares historical data for model training with feature engineering
+  **ML Training Pipeline**: Trains Random Cut Forest models on large pre-processed telemetry datasets
+  **ML Inference Pipeline**: Runs batch predictions using Amazon SageMaker to identify anomalies

### Filter-Based Approach
<a name="filter-based-approach"></a>
+  **Algorithm-Based Detection**: Applies statistical filters to identify tire pressure anomalies in real-time
+  **Leak Rate Calculation**: Computes pressure loss rates to determine severity
+  **Threshold-Based Alerting**: Generates alerts when leak rates exceed configurable thresholds

### Alert Management System
<a name="alert-management-system"></a>
+  **Alert Consolidation**: Combines predictions from both ML and filter-based approaches
+  **Severity Classification**: Categorizes alerts by urgency and leak rate
+  **Status Tracking**: Monitors alert lifecycle from detection through resolution
+  **Integration APIs**: Provides alerts to downstream maintenance scheduling systems