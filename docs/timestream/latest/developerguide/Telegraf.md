For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Installing Telegraf with the Timestream for LiveAnalytics

output plugin

As of version 1.16, the Timestream for LiveAnalytics output plugin is available in the official Telegraf
release. To install the output plugin on most major operating systems, follow the steps
outlined in the [InfluxData Telegraf Documentation](https://docs.influxdata.com/telegraf/v1.16/introduction/installation/ "https://docs.influxdata.com/telegraf/v1.16/introduction/installation/"). To install on the Amazon Linux 2 OS,
follow the instructions below.

## Installing

Telegraf with the Timestream for LiveAnalytics output plugin on Amazon Linux 2

To install Telegraf with the Timestream Output Plugin on Amazon Linux 2, perform
the following steps.

1. Install Telegraf using the `yum` package manager.

```
cat <<EOF | sudo tee /etc/yum.repos.d/influxdb.repo
[influxdb]
name = InfluxDB Repository - RHEL \$releasever
baseurl = https://repos.influxdata.com/rhel/\$releasever/\$basearch/stable
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdb.key
EOF
```

2. Run the following command.

```
sudo sed -i "s/\$releasever/$(rpm -E %{rhel})/g" /etc/yum.repos.d/influxdb.repo
```

3. Install and start Telegraf.

```
sudo yum install telegraf
sudo service telegraf start
```
