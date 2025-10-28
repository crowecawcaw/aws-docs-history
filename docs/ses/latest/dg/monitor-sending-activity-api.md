# Monitoring your usage statistics using the

Amazon SES API

The Amazon SES API provides the `GetSendStatistics` operation, which returns
information about your service usage. We recommend that you check your sending statistics
regularly, so that you can make adjustments if needed.

When you call the `GetSendStatistics` operation, you receive a list of data
points representing the last two weeks of your sending activity. Each data point in this
list represents 15 minutes of activity and contains the following information for that
period:

- The number of hard bounces
- The number of complaints
- The number of delivery attempts (corresponds to the number of emails you have
  sent)
- The number of rejected send attempts
- A timestamp for the analysis period
  For a complete description of the `GetSendStatistics` operation, see the [Amazon Simple Email Service API Reference](../APIReference/GetSendStatistics.md "../APIReference/GetSendStatistics.md").

In this section, you will find the following topics:

- [Calling the
  GetSendStatistics API operation using the AWS CLI](#monitor-sending-activity-api-cli "#monitor-sending-activity-api-cli")
- [Calling the
  GetSendStatistics operation programmatically](#monitor-sending-activity-api-sdk "#monitor-sending-activity-api-sdk")

## Calling the

`GetSendStatistics` API operation using the AWS CLI

The easiest way to call the `GetSendStatistics` API operation is to use the
[AWS Command Line Interface](https://aws.amazon.com/cli "https://aws.amazon.com/cli") (AWS CLI).

###### To call the `GetSendStatistics` API operation using the AWS CLI

1. If you have not already done so, install the AWS CLI. For more information, see
   "[Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md")" in the _AWS Command Line Interface User
   Guide_.
2. If you have not already done so, configure the AWS CLI to use your AWS
   credentials. For more information, see "[Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")" in the _AWS Command Line Interface User
   Guide_.
3. At the command line, run the following command:

```
aws ses get-send-statistics
```

If the AWS CLI is properly configured, you see a list of sending statistics in
JSON format. Each JSON object includes aggregated sending statistics for a
15-minute period.

## Calling the

`GetSendStatistics` operation programmatically

You can also call the `GetSendStatistics` operation using the AWS SDKs.
This section includes code examples for the AWS SDKs for Go, PHP, Python, and Ruby.
Choose one of the following links to view code examples for that language:

- [Code example for the
  AWS SDK for Go](#code-example-getsendstatistics-golang "#code-example-getsendstatistics-golang")
- [Code example for the
  AWS SDK for PHP](#code-example-getsendstatistics-php "#code-example-getsendstatistics-php")
- [Code example for the
  AWS SDK for Python (Boto)](#code-example-getsendstatistics-python "#code-example-getsendstatistics-python")
- [Code example for the
  AWS SDK for Ruby](#code-example-getsendstatistics-ruby "#code-example-getsendstatistics-ruby")

###### Note

These code examples assume that you have created an AWS shared credentials file
that contains your AWS access key ID, your AWS secret access key, and your
preferred AWS Region. For more information, see [Shared credentials
and config files](../../../credref/latest/refdocs/creds-config-files.md "../../../credref/latest/refdocs/creds-config-files.md").

### Calling

`GetSendStatistics` using the AWS SDK for Go

```
package main

import (
    "fmt"

    //go get github.com/aws/aws-sdk-go/...
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/ses"
    "github.com/aws/aws-sdk-go/aws/awserr"
)

const (
    // Replace us-west-2 with the AWS Region you're using for Amazon SES.
    AwsRegion = "`us-west-2`"
)

func main() {

    // Create a new session and specify an AWS Region.
    sess, err := session.NewSession(&aws.Config{
        Region:aws.String(AwsRegion)},
    )

    // Create an SES client in the session.
    svc := ses.New(sess)
    input := &ses.GetSendStatisticsInput{}

    result, err := svc.GetSendStatistics(input)

    // Display error messages if they occur.
    if err != nil {
        if aerr, ok := err.(awserr.Error); ok {
            switch aerr.Code() {
            default:
                fmt.Println(aerr.Error())
            }
        } else {
            // Print the error, cast err to awserr.Error to get the Code and
            // Message from an error.
            fmt.Println(err.Error())
        }
        return
    }

    fmt.Println(result)
}
```

### Calling

`GetSendStatistics` using the AWS SDK for PHP

```
<?php

// Replace path_to_sdk_inclusion with the path to the SDK as described in
// http://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/basic-usage.html
define('REQUIRED_FILE','`path_to_sdk_inclusion`');

// Replace us-west-2 with the AWS Region you're using for Amazon SES.
define('REGION','`us-west-2`');

require REQUIRED_FILE;

use Aws\Ses\SesClient;

$client = SesClient::factory(array(
    'version'=> 'latest',
    'region' => REGION
));

try {
     $result = $client->getSendStatistics([]);
	 echo($result);
} catch (Exception $e) {
     echo($e->getMessage()."\n");
}

?>
```

### Calling

`GetSendStatistics` using the AWS SDK for Python (Boto)

```
import boto3 #pip install boto3
import json
from botocore.exceptions import ClientError

client = boto3.client('ses')

try:
    response = client.get_send_statistics(
)
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print(json.dumps(response, indent=4, sort_keys=True, default=str))
```

### Calling

`GetSendStatistics` using the AWS SDK for Ruby

```
require 'aws-sdk' # gem install aws-sdk
require 'json'

# Replace us-west-2 with the AWS Region you're using for Amazon SES.
awsregion = "`us-west-2`"

# Create a new SES resource and specify a region
ses = Aws::SES::Client.new(region: awsregion)

begin

  resp = ses.get_send_statistics({
  })
  puts JSON.pretty_generate(resp.to_h)

# If something goes wrong, display an error message.
rescue Aws::SES::Errors::ServiceError => error
  puts error

end
```
