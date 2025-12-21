# Preconfigured

alerts

The Amazon SageMaker HyperPod (SageMaker HyperPod) observability add-on enables default
alerts for your cluster and workloads to notify you when the system detects
common early indicators of cluster under-performance. These alerts are defined
within the Amazon Managed Grafana built-in alerting system. For information about how to
modify these pre-configured alerts or create new ones, see [Alerts
in Grafana version 10](../../../grafana/latest/userguide/v10-alerts.md "../../../grafana/latest/userguide/v10-alerts.md") in the _Amazon Managed Grafana User
Guide_. The following YAML shows the default alerts.

```
groups:
- name: sagemaker_hyperpod_alerts
  rules:
  # GPU_TEMP_ABOVE_80C
  - alert: GPUHighTemperature
    expr: DCGM_FI_DEV_GPU_TEMP > 80
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "GPU Temperature Above 80C"
      description: "GPU {{ $labels.gpu }} temperature is {{ $value }}°C."

  # GPU_TEMP_ABOVE_85C
  - alert: GPUCriticalTemperature
    expr: DCGM_FI_DEV_GPU_TEMP > 85
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "GPU Temperature Above 85C"
      description: "GPU {{ $labels.gpu }} temperature is {{ $value }}°C."

  # GPU_MEMORY_ERROR
  # Any ECC double-bit errors indicate serious memory issues requiring immediate attention
  - alert: GPUMemoryErrorDetected
    expr: DCGM_FI_DEV_ECC_DBE_VOL_TOTAL > 0 or DCGM_FI_DEV_ECC_DBE_AGG_TOTAL > DCGM_FI_DEV_ECC_DBE_AGG_TOTAL offset 5m
    labels:
      severity: critical
    annotations:
      summary: "GPU ECC Double-Bit Error Detected"
      description: "GPU {{ $labels.gpu }} has detected ECC double-bit errors."

  # GPU_POWER_WARNING
  # Sustained power limit violations can impact performance and stability
  - alert: GPUPowerViolation
    expr: DCGM_FI_DEV_POWER_VIOLATION > 100
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "GPU Power Violation"
      description: "GPU {{ $labels.gpu }} has been operating at power limit for extended period."

  # GPU_NVLINK_ERROR
  # NVLink errors above threshold indicate interconnect stability issues
  - alert: NVLinkErrorsDetected
    expr: DCGM_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_TOTAL > 0 or DCGM_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_TOTAL > 10
    labels:
      severity: warning
    annotations:
      summary: "NVLink Errors Detected"
      description: "GPU {{ $labels.gpu }} has detected NVLink errors."

  # GPU_THERMAL_VIOLATION
  # Immediate alert on thermal violations to prevent hardware damage
  - alert: GPUThermalViolation
    expr: increase(DCGM_FI_DEV_THERMAL_VIOLATION[5m]) > 0
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "GPU Thermal Violation Detected"
      description: "GPU {{ $labels.gpu }} has thermal violations on node {{ $labels.Hostname }}"

  # GPU_XID_ERROR
  # XID errors indicate driver or hardware level GPU issues requiring investigation
  - alert: GPUXidError
    expr: DCGM_FI_DEV_XID_ERRORS > 0
    for: 0m
    labels:
      severity: critical
    annotations:
      summary: "GPU XID Error Detected"
      description: "GPU {{ $labels.gpu }} experienced XID error {{ $value }} on node {{ $labels.Hostname }}"

  # MIG_CONFIG_FAILURE
  # MIG configuration failures indicate issues with GPU partitioning setup
  - alert: MIGConfigFailure
    expr: kubelet_node_name{nvidia_com_mig_config_state="failed"} > 0
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "MIG Configuration Failed"
      description: "MIG configuration failed on node {{ $labels.instance }}"

  # DISK_SPACE_WARNING
  # 90% threshold ensures time to respond before complete disk exhaustion
  - alert: NodeDiskSpaceWarning
    expr: (node_filesystem_size_bytes - node_filesystem_free_bytes) / node_filesystem_size_bytes * 100 > 90
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High Disk Usage"
      description: "Node {{ $labels.instance }} disk usage is above 90%"

  # FSX_STORAGE_WARNING
  # 80% FSx utilization allows buffer for burst workloads
  - alert: FsxLustreStorageWarning
    expr: fsx_lustre_storage_used_bytes / fsx_lustre_storage_capacity_bytes * 100 > 80
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High FSx Lustre Usage"
      description: "FSx Lustre storage usage is above 80% on file system {{ $labels.filesystem_id }}"
```
