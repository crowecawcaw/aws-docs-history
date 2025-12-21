On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Formatting your data

You've [set up your account](getting-started-brain.md "getting-started-brain.md") and created your project. Soon, you'll organize your data so as
to help Lookout for Equipment determine an appropriate schema. But first, you must ensure that your data is
formatted properly.

To monitor your equipment, you must provide Amazon Lookout for Equipment with time-series data from the
sensors on your equipment. The data that you're providing to Lookout for Equipment is a series of numerical
measurements from the sensors. You provide this data from either a data historian or
Amazon Simple Storage Service (Amazon S3). A data historian is a software program that records and retrieves sensor
data from your equipment.

To provide Amazon Lookout for Equipment with time-series data from the sensors, you must use properly
formatted .csv files to create a dataset. Creating a dataset aggregates the data in a format
that is suitable for analysis. You create a dataset for a single piece of equipment, or
_asset_. You train an ML model on the dataset that you create. You
then use that model to monitor your asset. You don't have to use all the data from the
sensors to train a model. You train a model using data from some of the sensors in the
dataset.

You can store the data for your asset in one of the following ways:

- Using one .csv file for each sensor (recommended)
- Storing all of the sensor data in one .csv file
  Each .csv file must have at least two columns. The first column of the file is a timestamp
  that indicates the date and time. You must have at least one additional column containing
  the data from a sensor. Each subsequent column can have data from a different sensor.

To store the data for your asset in one .csv file, you arrange the data in the
following format.

| _AssetData.csv_ | Timestamp | Sensor 1 | Sensor 2 |
| --------------- | --------- | -------- | -------- |
| 1/1/2020 0:00   | 2         | 12       |
| 1/1/2020 0:05   | 3         | 11       |
| 1/1/2020 0:10   | 5         | 10       |
| 1/1/2020 0:15   | 3         | 9        |
| 1/1/2020 0:20   | 4         | 12       |

The following example shows the information from the preceding table as a .csv
file.

```

Timestamp,Sensor 1,Sensor 2
1/1/2020 0:00,2,12
1/1/2020 0:05,3,11
1/1/2020 0:10,5,10
1/1/2020 0:15,3,9
1/1/2020 0:20,4,12

```

You can choose your column names. We recommend using `"Timestamp"` as
the name for the column with the time-series data. For the names of the columns with
data from your sensors, we recommend using names that distinguish one sensor from
another.

If your are storing the data from each sensor in one .csv file, use the following
table to see how to format the data.

| _SensorData.csv_ | Timestamp | Sensor 3 |
| ---------------- | --------- | -------- |
| 1/1/2020 0:00    | 34        |
| 1/1/2020 0:05    | 33        |
| 1/1/2020 0:10    | 35        |
| 1/1/2020 0:15    | 33        |
| 1/1/2020 0:20    | 34        |

The following example shows the information from the preceding table as a .csv
file.

```

Timestamp,Sensor 3
1/1/2020 0:00,34
1/1/2020 0:05,33
1/1/2020 0:10,35
1/1/2020 0:15,33
1/1/2020 0:20,34

```

We recommend using `"Timestamp"` as the name for the column with the
time-series data. For the column with data from the sensor, we recommend using a
name that distinguishes it from other sensors.

You must have a double (numerical) as the data type for your sensor data. You can only
train your model on numeric data.

When you are preparing your data, you should keep the following information in
mind:

| Category                                              | Limit          |
| ----------------------------------------------------- | -------------- |
| minimum date range                                    | 180 days       |
| maximum sensors per dataset                           | 3000           |
| maximum sensors per model                             | 300            |
| maximum length of a sensor name                       | 200 characters |
| maximum size of each .csv file                        | 5 GB           |
| maximum historical dataset size (combined .csv files) | 50 GB          |
| maximum files per historical dataset                  | 1,000          |

- You can use the following delimiters for the data in the timestamp column: \_ -
  (hyphen) and space
- The timestamp column can use the following formats:
  - yyyy-MM-dd-HH-mm-ss
  - yyyy-MM-dd'T'HH:mm:ss
  - yyyy-MM-dd HH:mm:ss
  - yyyy-MM-dd-HH:mm:ss
  - yyyy-MM-dd'T'HH:mm
  - yyyy-MM-dd HH:mm
  - yyyy-MM-dd-HH:mm
  - yyyy/MM/dd'T'HH:mm:ss
  - yyyyMMdd'T'HH:mm
  - yyyyMMdd HH:mm
  - yyyyMMddHHmm
  - yyyy/MM/dd HH:mm:ss
  - yyyyMMdd'T'HH:mm:ss
  - yyyyMMdd HH:mm:ss
  - yyyyMMddHHmmss
  - yyyy/MM/dd'T'HH:mm
  - yyyy/MM/dd HH:mm
  - yyyy MM dd'T'HH:mm:ss
  - yyyy MM dd HH:mm:ss
  - yyyy MM dd'T'HH:mm
  - yyyy MM dd HH:mm

- The valid characters that you can use in the column names of the dataset are
  A-Z, a-z, 0-9, and . \ \_ - (hyphen)
  To learn more about the formats listed above, see [the ISO 86021 standard](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations "https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations").

Now that your data is formatted properly, it's time to organize your files.
