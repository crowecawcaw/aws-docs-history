

# Inference strategy
<a name="pm-inference-strategy"></a>

This section explains the dual inference approach used for tire health prediction and the cost-driven reasoning behind each choice.

## Why two approaches
<a name="why-two-approaches"></a>

Tire failures have fundamentally different time scales that require different detection strategies:


| Failure Mode | Time Scale | Detection Window | Inference Needed | 
| --- | --- | --- | --- | 
| Slow leak | Days to weeks | 3-7 days before threshold | Daily batch | 
| Valve failure | Intermittent over weeks | Days | Daily batch | 
| Highway blowout | Minutes | Seconds to minutes | Real-time | 

## Daily batch: slow leak detection
<a name="daily-batch-slow-leak-detection"></a>

A slow leak drops 0.5-1.2 PSI per day. The window from "detectable trend" to the 28 PSI alert threshold is 3-7 days. Checking once per day gives 4\+ days of advance warning. Checking every 15 minutes gives the same 4\+ days of warning — the extra granularity adds cost without adding value for a condition that changes over days.

The daily batch Lambda queries the last 7 days of tire telemetry from DynamoDB, computes a linear regression slope per tire, and writes predictive warnings for tires losing pressure consistently (> 0.3 PSI/day with current pressure below 30 PSI).

 **When the ML model adds value over simple trend detection:** 
+ Temperature-related pressure changes (cold morning vs warm afternoon) look like leaks to a simple trend line, but the ML model accounts for ambient temperature correlation
+ Intermittent valve failures show irregular pressure patterns that linear regression misses
+ Altitude changes during mountain routes cause temporary pressure drops that are not leaks

 **Cost:** 


| Approach | Daily Cost | Monthly Cost | 
| --- | --- | --- | 
| Daily batch (Lambda \+ DynamoDB query) | $0.02 | $0.60 | 
| Real-time endpoint (ml.m5.large) | $2.76 | $83.00 | 

At 50 vehicles with approximately 2 slow leaks per year, the real-time approach costs $1,000/year to save $2,000-3,400. The daily batch costs $7/year for the same outcome.

## Real-time: highway blowout risk
<a name="real-time-highway-blowout-risk"></a>

A tire under combined stress — high speed, high temperature, low tread, and borderline pressure — can fail catastrophically in minutes. Each signal individually is within normal range: pressure at 29 PSI (above the 28 PSI threshold), temperature at 140°F (elevated but not alarming alone), tread at 3.5mm (above the 3mm threshold). But the combination is dangerous.

A rule-based system cannot catch this because no single threshold is crossed. The Random Cut Forest model recognizes the multi-signal pattern that preceded blowouts in the training data.

 **Pre-filtering to control cost:** 

The SageMaker endpoint is not called for every telemetry message. It is only invoked when:

1. Vehicle speed > 60 mph (highway driving), AND

1. Any tire pressure < 30 PSI OR tire temperature > 120°F

This filters over 90% of telemetry. Instead of 19,200 inferences per day (50 vehicles × 4 tires × 4 readings/hour × 24 hours), the endpoint receives approximately 50-100 inferences per day for vehicles in active risk conditions.

 **Cost justification:** 


| Item | Cost | 
| --- | --- | 
| SageMaker endpoint (ml.m5.large) | $83/month | 
| Highway blowout (tow, tire, cargo damage, downtime, liability) | $10,000\+ per incident | 
| At 5,000 vehicles: \~5 blowouts/year prevented | $50,000\+ saved | 
| ROI | 50x | 

## Training data
<a name="training-data"></a>

The model is trained on a synthetic dataset generated from realistic fleet patterns:
+ 721,024 records across 50 vehicles over 6 months
+ Normal driving patterns with seasonal temperature effects (Gay-Lussac’s law), city-specific climate variation (Dallas, Atlanta, Chicago, Phoenix, Seattle), rear tire load differential, and natural tread wear
+ Injected anomalies: slow leaks (8%), punctures (4%), valve failures (3%), overinflation (2%)
+ Features: pressure, temperature, delta\_pressure, delta\_temp
+ Model: SageMaker Random Cut Forest (unsupervised anomaly detection), trained on normal data only

The training dataset can be regenerated with `scripts/generate_training_data.py` and the model retrained with `scripts/train_model.py` in the [source repository](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws).

## Connected Mobility integration
<a name="connected-mobility-integration"></a>

When used with CMS, the prediction pipeline integrates as follows:

1. The CMS simulator or real FWE agent sends tire telemetry through IoT Core → MSK → Flink

1. The Flink MaintenanceProcessor evaluates rule-based thresholds from the event catalog (fires at 28 PSI)

1. The daily batch Lambda queries the CMS telemetry table and writes `prediction.tire_slow_leak` warnings

1. For highway vehicles with concerning signals, the real-time Lambda calls the SageMaker endpoint and writes `prediction.blowout_risk` alerts

1. Both prediction alert types appear in the CMS Fleet Manager UI alongside rule-based maintenance alerts

1. The CMS adapter (`source/lambda/cms_adapter.py`) transforms CMS canonical field names (`tire_pressure_fl`) to the per-tire format expected by the model