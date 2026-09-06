# Amazon DocumentDB features and configurations

The following tables compare features, capabilities, and supported instance types across
Amazon DocumentDB engine versions and elastic clusters. Use these tables to determine which engine version
best fits your workload requirements.

## Engine status

Engine status by version| Feature / Capability | v3.6 | v4.0 | v5.0 | v8.0 |
| --- | --- | --- | --- | --- |
| Support status | EOL: Mar 2026 | Active | Active (LTS available) | Active (GA Nov 2025) |
| Extended Support available | Yes (paid, until Mar 2029) | N/A | N/A | N/A |
| LTS release available | No | No | Yes (v5.0 LTS) | No |
| Elastic clusters | No | No | Yes | No |

## Cluster types

Cluster types by version| Cluster Type | v3.6 | v4.0 | v5.0 | v8.0 | Elastic clusters |
| --- | --- | --- | --- | --- | --- |
| Instance-based cluster | Yes | Yes | Yes | Yes | Yes |
| Serverless instances | No | No | Yes | Yes | No |

## Features

Features and configurations by engine version| Feature | v3.6 | v4.0 | v5.0 | v8.0 | Elastic clusters |
| --- | --- | --- | --- | --- | --- |
| Global clusters | No | Yes | Yes | Yes | No |
| Multi-AZ (3 AZs) | Yes | Yes | Yes | Yes | Yes (per shard) |
| Read replicas supported | 15 | 15 | 15 | 15 | 15 per shard |
| ACID transactions | No | Yes | Yes | Yes | No |
| Change streams | Yes | Yes | Yes | Yes | No |
| Vector search | No | No | Yes | Yes | No |
| Performance Insights | Yes | Yes | Yes | Yes | No |
| In-place major version upgrade (MVU) | Yes (to 5.0 or 8.0) | Yes (to 5.0 or 8.0) | Yes (to 8.0) | No (target only) | No |
| Client-side field level encryption (FLE) | No | No | Yes | Yes | No |
| I/O-Optimized storage | No | No | Yes | Yes | No |
| TLS certificate rotation (no reboot) | Yes (patch 1.0.208662+) | Yes (patch 2.0.10179+) | Yes (patch 3.0.4780+) | Yes | Yes |
| Cross-Region snapshot copy | Yes | Yes | Yes | Yes | Yes |
| Cross-account snapshot sharing | Yes | Yes | Yes | Yes | No |
| Audit and slow query logs | Yes | Yes | Yes | Yes | Yes |
| Dual-stack IPv4/IPv6 | No | Yes (patch 2.0.11747+) | Yes (patch 3.0.15902+) | Yes | N/A |
| Collation | No | No | No | Yes | No |
| Views | No | No | No | Yes | No |
| Compression Support | No | No | LZ4 | LZ4/Ztsd | No |
| Text Index | No | No | V1 | V2 | No |
| FedRAMP (GovCloud) | No | No | Yes | Yes | No |

## Instance types

Instance type support by version| Instance Type | v3.6 | v4.0 | v5.0 | v8.0 |
| --- | --- | --- | --- | --- |
| db.r4 (previous generation) | Yes | No | No | No |
| db.r5 | Yes | Yes | Yes | Yes |
| db.r6g (Graviton2) | No | Yes | Yes | Yes |
| db.r6gd (NVMe-backed Graviton2) | No | No | Yes | Yes |
| db.r8g (Graviton4) | No | No | Yes | Yes |
| db.t3.medium | Yes | Yes | Yes | Yes |
| db.t4g.medium (Graviton2) | No | Yes | Yes | Yes |
| serverless | No | No | Yes | Yes |

## AWS integrations

AWS integration support by version| AWS Integration / Feature | v3.6 | v4.0 | v5.0 | v8.0 | Elastic clusters |
| --- | --- | --- | --- | --- | --- |
| AWS Backup | Yes | Yes | Yes | Yes | No |
| AWS Secrets Manager | Yes | Yes | Yes | Yes | No |
| AWS Lambda (native ESM) | No | Yes | Yes | No | No |
| Amazon OpenSearch Service Ingestion (Zero-ETL) | No | Yes | Yes | Yes | No |
| AWS DMS migration support | Yes | Yes | Yes | Yes (from 5.0 via AWS DMS) | Yes |
| AWS Identity and Access Management authentication | No | No | Yes (5.0 instance-based) | Yes | No |
| AWS CloudShell | No | No | Yes | Yes | No |
| AWS Key Management Service | Yes | Yes | Yes | Yes | Yes |
| AWS CloudTrail | Yes | Yes | Yes | Yes | Yes |
