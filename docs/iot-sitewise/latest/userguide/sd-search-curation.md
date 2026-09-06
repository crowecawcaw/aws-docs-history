

# Scenario Discovery search and curation of datasets
<a name="sd-search-curation"></a>

## Overview
<a name="sd-search-curation-overview"></a>

In the Discover section, Scenario Discovery Search and Curation combines natural-language understanding with agentic execution to enable you to discover scenarios, build comprehensive datasets, and get feedback on scenario coverage. You can search through your data with natural language and get back a list of video recording segments. Scenario Discovery provides faster agentic curation of datasets: describe what you need in natural language and receive a training-ready dataset. It acts as a productivity multiplier, augmenting your existing team capacity at a fraction of the cost.

From the SiteWise Console, choose the URI link to open the Scenario Discovery landing page:

![Scenario Discovery landing page](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image31.png)


![Scenario Discovery search interface](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image32.png)


## Data curation concepts
<a name="sd-curation-concepts"></a>
+ **Video Search** — Instantly queries your videos to retrieve a broad set of candidate clips. Best for fast exploration to check if relevant video data is available. Example: "Find pedestrians walking."
+ **Multi-modal Search** — High-precision, multi-modal query that uses videos and structured data (like telemetry, annotations) to surface the most relevant clips. Best when you need higher-precision matches. Example: "Find pedestrians and the car is driving at 30 mph."
+ **AI Curation** — Build comprehensive training datasets through a guided, automated workflow. Describe your research objective in natural language, and the AI agent generates a discovery plan, executes targeted queries across your data, and curates a balanced, representative dataset. This is ideal for model development and building training sets that cover the specific conditions your autonomous system needs to handle.

**Distribution:** AI Curation automatically balances the representation of retrieved scenarios across key dimensions, such as class types (Pedestrian, Scooter rider, Vulnerable user), behaviors, and environmental conditions, using None/Low/Medium/High sliders to ensure your final dataset is not over-indexed on any single condition.

The parameter categories (Weather Conditions, Time of Day, Ego Behavior, and Driving Environment) define the system's internal dimensions, ensuring retrieved scenarios fall within the validated operating envelope (for example, highway, heavy rain, 30 mph) for which you are testing your perception system.

**Parameter Distribution:** You assign each parameter category a target frequency (None → Low → Medium → High) that the AI uses to shape search results. For example, you might set "Rainy" to High and "Snowy" to Low so the curated dataset reflects your intended test coverage priorities rather than raw data availability.

## Running a Video Search
<a name="sd-quick-search"></a>

The following are example search queries you can try. Type a query in plain language to quickly retrieve matching video segments with very low latency.


| Category | Selected Query | 
| --- | --- | 
| Environmental | "Show me a car driving through fog" | 
| Infrastructure | "Show me a traffic light changing from red to green" | 
| Traffic | "Find clips where a vehicle is driving in the wrong lane" | 
| Temporal | "Show me daytime driving clips" | 
| Multi-actor | "Show me all driving scenarios with a bus" | 
| Behavioral | "Find scenarios where my vehicle turns right at an intersection in the rain" | 

### Step 1: Running a search query
<a name="sd-quick-step1-search"></a>

![Running a Video Search query](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image33.png)


### Step 2: Saving a curation
<a name="sd-quick-step2-save"></a>

Save promising selections without committing to a full dataset export. Use these manually saved discoveries to run quick model prototypes on your end.

To save a curation, complete the following steps:

1. Run a search query and review the returned video segments.

1. Select the relevant results you want to include in your curation.

1. Choose **Save Curation** to preserve your selection.

1. Provide a name and optional description for your saved curation.

1. Confirm to save. Your curation is now accessible from the Discover page for review, refinement, or export.

![Saving your curation selection](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image34.png)


![Naming your saved curation](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image35.png)


### Step 3: Finding your saved curation
<a name="sd-quick-step3-find"></a>

![Finding your saved curation on the Discover page](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image36.png)


### Step 4: Exporting your saved curation
<a name="sd-quick-step4-export"></a>

![Exporting your saved curation](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image37.png)


### Step 5: Export saved curation into your S3 bucket
<a name="sd-quick-step5-s3-export"></a>

![Configuring S3 bucket export destination](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image38.png)


### Step 6: Export job running
<a name="sd-quick-step6-running"></a>

![Export job running](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image39.png)


### Step 7: Export completed
<a name="sd-quick-step7-completed"></a>

![Export job completed successfully](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image40.png)


### Step 8: View export job in S3
<a name="sd-quick-step8-view-s3"></a>

![Viewing the export job in S3](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image41.png)


### Step 9: View export job completed in console
<a name="sd-quick-step9-view-console"></a>

![Export job confirmed in console](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image42.png)


## Running a Multi-modal Search
<a name="sd-deep-search"></a>

When your query contains both semantic and structured components, use the Multi-modal Search feature. It first retrieves scenes matching the semantic description (for example, "pedestrians"), then applies structured filters (for example, car speed = 30 mph) to narrow results. The results rank videos from highest to lowest relevance level. This search takes several minutes and delivers more focused, relevant results.

![Multi-modal Search results with relevance ranking](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image43.png)


Each search result relevance score tells you how well it matches your query compared to other results in the same search — higher means a better match. Scores cannot be compared across different searches, so use result ranking (not score values) when evaluating results from separate queries. You can follow the manual selection of results that are relevant to your search to export. The export follows the same manually selected process as described in the Video Search section.

**Important**  
For structured search — querying telemetry values, annotations, dataset metadata, and data segments by exact criteria — you use the Scenario Discovery `StartQuery` API with SQL statements. See [Scenario Discovery query language reference](sd-query-language.md) for more details.

## Running an AI Curation
<a name="sd-ai-curation"></a>

The following walkthrough demonstrates how to use AI Curation to build a curated dataset for a parking feature scenario. Each step shows how the system guides you from objective definition through to a final, quality-scored dataset.

### Step 1: Define your curation objective
<a name="sd-ai-step1-objective"></a>

"Object detection for highway lane-changing scenarios"

### Step 2: Configure parameter distribution
<a name="sd-ai-step2-params"></a>

Enter a natural language description of your curation objective (for example, object detection for highway lane-changing scenarios). The AI generates a structured discovery plan. Then adjust the parameter sliders to control how scenarios are balanced across class type, behavior, and time of day. Expected duration: The AI Curation workflow duration depends on dataset size, query complexity, and the number of parameter categories you configure. The system provides real-time progress updates as it generates queries, retrieves scenarios, and assembles the curated dataset.

![AI Curation discovery plan](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image44.png)


![Defining curation objective and parameter distribution](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image45.png)


### Step 3: Execute the AI Curation workflow
<a name="sd-ai-step3-execute"></a>

The AI agent automatically executes the multi-step curation workflow, from generating search queries to classifying and curating matching scenarios. This helps save hours of manual work while ensuring consistent methodology across runs.

![AI Curation workflow executing](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image46.png)


### Step 4: Review curated results
<a name="sd-ai-step4-review"></a>

Review the curated results including quality score, dataset size, and diversity metrics across scenario classifications. This validates dataset completeness before committing to model training.

![Curated results with quality score and diversity metrics](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image47.png)


Your Overall Quality Score is a single percentage that tells you how ready your curated dataset is for model training or validation. It is calculated as a weighted blend of four factors: Size Adequacy (30%) evaluates whether you have enough scenarios relative to your use case's minimum and recommended thresholds; Completeness (30%) measures whether all required object types, behaviors, environmental conditions, and critical scenarios are represented; Diversity (25%) assesses how evenly your scenarios are distributed across conditions like weather, time of day, and driving environment compared to an ideal target distribution; and Redundancy (15%) penalizes duplicate or near-duplicate scenarios that inflate volume without adding value. A score of 70% or greater indicates high confidence in dataset readiness, 50%–69% signals moderate gaps worth reviewing, and below 50% means significant improvements are needed.

The Dataset Size and Diversity Score cards shown alongside the Overall Quality Score are not independent metrics — they feed directly into the composite calculation. Dataset Size maps to the Size Adequacy component, where your raw scenario count is evaluated against use-case-specific thresholds. The Diversity Score maps to the Diversity component, where statistical comparison (KL divergence) measures how closely your actual distributions match the target. To improve a low score, navigate to the Parameter Results tab to identify exactly which scenario variations are missing or underrepresented, then add, rebalance, or de-duplicate your data accordingly and re-run the assessment.

### Step 5: Access saved curations
<a name="sd-ai-step5-saved"></a>

![Accessing saved curation](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image48.png)


![Accessing and exporting saved curation](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image49.png)


Follow the same export path described in the Video Search section. Your data is now ready for simulation or model training.

**Important**  
While your Overall Quality Score is an indicator for how ready your dataset is for model training or validation, these are AI-generated predictions based on patterns in data. You are responsible for evaluating your datasets for accuracy as appropriate for your use case, including by employing human review.