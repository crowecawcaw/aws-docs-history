# Data Onboarding

## 1. Glossary

- **Data Agent** – AI-powered assistant that helps automate data integration tasks
- **Source Flow** – Process that imports data from your source systems into
- **Dataset** – A structured representation of your source data in
- **S3 Bucket** – Amazon S3 storage location containing your source data files
- **Destination (Transformation) Flow** – Process that converts your source data format to the AWS Canonical Data Model (CDM) format
- **CDM** – Canonical Data Model, the standardized data structure used by
- **Data Mapping** – Process of matching fields from your source data to CDM structure

## 2. Purpose

This guide provides step-by-step instructions for onboarding your supply chain data into
using the Data Agent, an AI-powered assistant that helps automate data onboarding
tasks and troubleshoot issues.

## 3. What is Data Onboarding for ?

Data onboarding is the process of integrating your existing supply chain data into
. For to use your data for planning and forecasting, it needs to be in a
structured format within the Canonical Data Model (CDM), ’s standardized data
structure. Data onboarding translates your source data into this format by mapping your
fields to CDM entities, transforming data types and formats, and validating data quality.
This ensures can generate accurate forecasts and recommendations based on your
source data.

### The Process

Data onboarding follows five phases:

1. **Prepare**: Gather source data from your
   systems (see [Prerequisites](connecting-your-data.md#connecting-your-data-prerequisites "connecting-your-data.md#connecting-your-data-prerequisites"))
2. **Upload**: Upload your supply chain data as
   CSV files
3. **Map**: Match your source datasets to CDM
   destination datasets as well as source fields to CDM entities (for example,
   mapping your “item\_number” field to CDM’s
   “product\_id”)
4. **Validate**: Run quality checks and resolve
   any data issues

Throughout this process, ’s Data Agent serves as your AI-powered
assistant data onboarding assistant. It will persist on the left side of your screen,
and you interact with it using natural language to help automate data onboarding
tasks including:

- **Discovers schemas**: Automatically scans
  your uploaded data to identify structure and relationships
- **Generates source-to-destination mappings**:
  Analyzes your source data and suggests which CDM destination tables best
  match your data
- **Creates SQL transformation queries**:
  Automatically generates SQL to map your source fields to CDM destination
  fields
- **Provides mapping rationale**: Explains why
  specific mappings were suggested based on overlapping data
- **Troubleshoots issues**: Identifies why
  mappings or data loads failed and recommends specific fixes
- **Answers questions**: Explains concepts,
  clarifies mappings, and provides guidance throughout the process
