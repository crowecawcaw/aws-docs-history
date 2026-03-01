# Examples of configuration files

**Basic system metrics configuration**

```
{
  "agent": {
    "metrics_collection_interval": 60,
    "region": "us-east-1"
  },
  "metrics": {
    "namespace": "MySystem",
    "metrics_collected": {
      "cpu": {
        "resources": ["*"],
        "measurement": ["usage_active", "usage_system", "usage_user"]
      },
      "mem": {
        "measurement": ["used_percent"]
      },
      "disk": {
        "resources": ["/"],
        "measurement": ["used_percent"]
      }
    },
    "append_dimensions": {
      "InstanceId": "${aws:InstanceId}"
    }
  }
}

```

**Web server monitoring configuration**

```
{
  "agent": {
    "metrics_collection_interval": 60,
    "region": "us-east-1"
  },
  "metrics": {
    "namespace": "WebServer",
    "metrics_collected": {
      "cpu": {
        "resources": ["*"],
        "measurement": ["usage_active"]
      },
      "mem": {
        "measurement": ["used_percent"]
      },
      "net": {
        "resources": ["eth0"],
        "measurement": ["bytes_sent", "bytes_recv"]
      }
    }
  },
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/apache2/access.log",
            "log_group_name": "apache-access-logs",
            "log_stream_name": "{instance_id}-access"
          },
          {
            "file_path": "/var/log/apache2/error.log",
            "log_group_name": "apache-error-logs",
            "log_stream_name": "{instance_id}-error"
          }
        ]
      }
    }
  }
}


```

**Database server configuration**

```
{
  "agent": {
    "metrics_collection_interval": 30,
    "region": "us-east-1"
  },
  "metrics": {
    "namespace": "DatabaseServer",
    "metrics_collected": {
      "cpu": {
        "resources": ["*"],
        "measurement": ["usage_active", "usage_iowait"]
      },
      "mem": {
        "measurement": ["used_percent", "available_percent"]
      },
      "disk": {
        "resources": ["/", "/data"],
        "measurement": ["used_percent", "inodes_free"]
      },
      "diskio": {
        "resources": ["*"],
        "measurement": ["read_bytes", "write_bytes", "io_time"]
      }
    },
    "append_dimensions": {
      "InstanceId": "${aws:InstanceId}",
      "InstanceType": "${aws:InstanceType}",
      "AutoScalingGroupName": "${aws:AutoScalingGroupName}"
    }
  }
}

```
