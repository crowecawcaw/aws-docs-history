# Autogenerating ETL Scripts API

The ETL script-generation API describes the datatypes and API for generating
ETL scripts in AWS Glue.

## Data types

- [CodeGenNode structure](#aws-glue-api-etl-script-generation-CodeGenNode "#aws-glue-api-etl-script-generation-CodeGenNode")
- [CodeGenNodeArg structure](#aws-glue-api-etl-script-generation-CodeGenNodeArg "#aws-glue-api-etl-script-generation-CodeGenNodeArg")
- [CodeGenEdge structure](#aws-glue-api-etl-script-generation-CodeGenEdge "#aws-glue-api-etl-script-generation-CodeGenEdge")
- [Location structure](#aws-glue-api-etl-script-generation-Location "#aws-glue-api-etl-script-generation-Location")
- [CatalogEntry structure](#aws-glue-api-etl-script-generation-CatalogEntry "#aws-glue-api-etl-script-generation-CatalogEntry")
- [MappingEntry structure](#aws-glue-api-etl-script-generation-MappingEntry "#aws-glue-api-etl-script-generation-MappingEntry")

## CodeGenNode structure

Represents a node in a directed acyclic graph (DAG)

###### Fields

- `Id` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Identifier string pattern](aws-glue-api-common.md#aws-glue-api-regex-id "aws-glue-api-common.md#aws-glue-api-regex-id").

A node identifier that is unique within the node's graph.

- `NodeType` – _Required:_ UTF-8 string.

The type of node that this is.

- `Args` – _Required:_ An array of [CodeGenNodeArg](#aws-glue-api-etl-script-generation-CodeGenNodeArg "#aws-glue-api-etl-script-generation-CodeGenNodeArg") objects, not more than 50 structures.

Properties of the node, in the form of name-value pairs.

- `LineNumber` – Number (integer).

The line number of the node.

## CodeGenNodeArg structure

An argument or property of a node.

###### Fields

- `Name` – _Required:_ UTF-8 string.

The name of the argument or property.

- `Value` – _Required:_ UTF-8 string.

The value of the argument or property.

- `Param` – Boolean.

True if the value is used as a parameter.

## CodeGenEdge structure

Represents a directional edge in a directed acyclic graph (DAG).

###### Fields

- `Source` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Identifier string pattern](aws-glue-api-common.md#aws-glue-api-regex-id "aws-glue-api-common.md#aws-glue-api-regex-id").

The ID of the node at which the edge starts.

- `Target` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Identifier string pattern](aws-glue-api-common.md#aws-glue-api-regex-id "aws-glue-api-common.md#aws-glue-api-regex-id").

The ID of the node at which the edge ends.

- `TargetParameter` – UTF-8 string.

The target of the edge.

## Location structure

The location of resources.

###### Fields

- `Jdbc` – An array of [CodeGenNodeArg](#aws-glue-api-etl-script-generation-CodeGenNodeArg "#aws-glue-api-etl-script-generation-CodeGenNodeArg") objects, not more than 50 structures.

A JDBC location.

- `S3` – An array of [CodeGenNodeArg](#aws-glue-api-etl-script-generation-CodeGenNodeArg "#aws-glue-api-etl-script-generation-CodeGenNodeArg") objects, not more than 50 structures.

An Amazon Simple Storage Service (Amazon S3) location.

- `DynamoDB` – An array of [CodeGenNodeArg](#aws-glue-api-etl-script-generation-CodeGenNodeArg "#aws-glue-api-etl-script-generation-CodeGenNodeArg") objects, not more than 50 structures.

An Amazon DynamoDB table location.

## CatalogEntry structure

Specifies a table definition in the AWS Glue Data Catalog.

###### Fields

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The database in which the table metadata resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table in question.

## MappingEntry structure

Defines a mapping.

###### Fields

- `SourceTable` – UTF-8 string.

The name of the source table.

- `SourcePath` – UTF-8 string.

The source path.

- `SourceType` – UTF-8 string.

The source type.

- `TargetTable` – UTF-8 string.

The target table.

- `TargetPath` – UTF-8 string.

The target path.

- `TargetType` – UTF-8 string.

The target type.

## Operations

- [CreateScript action (Python: create_script)](#aws-glue-api-etl-script-generation-CreateScript "#aws-glue-api-etl-script-generation-CreateScript")
- [GetDataflowGraph action (Python: get_dataflow_graph)](#aws-glue-api-etl-script-generation-GetDataflowGraph "#aws-glue-api-etl-script-generation-GetDataflowGraph")
- [GetMapping action (Python: get_mapping)](#aws-glue-api-etl-script-generation-GetMapping "#aws-glue-api-etl-script-generation-GetMapping")
- [GetPlan action (Python: get_plan)](#aws-glue-api-etl-script-generation-GetPlan "#aws-glue-api-etl-script-generation-GetPlan")

## CreateScript action (Python: create_script)

Transforms a directed acyclic graph (DAG) into code.

###### Request

- `DagNodes` – An array of [CodeGenNode](#aws-glue-api-etl-script-generation-CodeGenNode "#aws-glue-api-etl-script-generation-CodeGenNode") objects.

A list of the nodes in the DAG.

- `DagEdges` – An array of [CodeGenEdge](#aws-glue-api-etl-script-generation-CodeGenEdge "#aws-glue-api-etl-script-generation-CodeGenEdge") objects.

A list of the edges in the DAG.

- `Language` – UTF-8 string (valid values: `PYTHON` | `SCALA`).

The programming language of the resulting code from the DAG.

###### Response

- `PythonScript` – UTF-8 string.

The Python script generated from the DAG.

- `ScalaCode` – UTF-8 string.

The Scala code generated from the DAG.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetDataflowGraph action (Python: get_dataflow_graph)

Transforms a Python script into a directed acyclic graph (DAG).

###### Request

- `PythonScript` – UTF-8 string.

The Python script to transform.

###### Response

- `DagNodes` – An array of [CodeGenNode](#aws-glue-api-etl-script-generation-CodeGenNode "#aws-glue-api-etl-script-generation-CodeGenNode") objects.

A list of the nodes in the resulting DAG.

- `DagEdges` – An array of [CodeGenEdge](#aws-glue-api-etl-script-generation-CodeGenEdge "#aws-glue-api-etl-script-generation-CodeGenEdge") objects.

A list of the edges in the resulting DAG.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetMapping action (Python: get_mapping)

Creates mappings.

###### Request

- `Source` – _Required:_ A [CatalogEntry](#aws-glue-api-etl-script-generation-CatalogEntry "#aws-glue-api-etl-script-generation-CatalogEntry") object.

Specifies the source table.

- `Sinks` – An array of [CatalogEntry](#aws-glue-api-etl-script-generation-CatalogEntry "#aws-glue-api-etl-script-generation-CatalogEntry") objects.

A list of target tables.

- `Location` – A [Location](#aws-glue-api-etl-script-generation-Location "#aws-glue-api-etl-script-generation-Location") object.

Parameters for the mapping.

###### Response

- `Mapping` – _Required:_ An array of [MappingEntry](#aws-glue-api-etl-script-generation-MappingEntry "#aws-glue-api-etl-script-generation-MappingEntry") objects.

A list of mappings to the specified targets.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `EntityNotFoundException`

## GetPlan action (Python: get_plan)

Gets code to perform a specified mapping.

###### Request

- `Mapping` – _Required:_ An array of [MappingEntry](#aws-glue-api-etl-script-generation-MappingEntry "#aws-glue-api-etl-script-generation-MappingEntry") objects.

The list of mappings from a source table to target tables.

- `Source` – _Required:_ A [CatalogEntry](#aws-glue-api-etl-script-generation-CatalogEntry "#aws-glue-api-etl-script-generation-CatalogEntry") object.

The source table.

- `Sinks` – An array of [CatalogEntry](#aws-glue-api-etl-script-generation-CatalogEntry "#aws-glue-api-etl-script-generation-CatalogEntry") objects.

The target tables.

- `Location` – A [Location](#aws-glue-api-etl-script-generation-Location "#aws-glue-api-etl-script-generation-Location") object.

The parameters for the mapping.

- `Language` – UTF-8 string (valid values: `PYTHON` | `SCALA`).

The programming language of the code to perform the mapping.

- `AdditionalPlanOptionsMap` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

A map to hold additional optional key-value parameters.

Currently, these key-value pairs are supported:

    + `inferSchema`  —  Specifies whether
     to set `inferSchema` to true or false for the default script generated
     by an AWS Glue job. For example, to set `inferSchema`
     to true, pass the following key value pair:


    `--additional-plan-options-map '{"inferSchema":"true"}'`

###### Response

- `PythonScript` – UTF-8 string.

A Python script to perform the mapping.

- `ScalaCode` – UTF-8 string.

The Scala code to perform the mapping.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
