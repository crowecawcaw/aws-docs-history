# Public broadcast satellite utilizing Amazon S3 data delivery

This example builds off the analysis done in the [JPSS-1 - Public broadcast satellite (PBS) -
Evaluation](examples.md#examples.pbs-definition "examples.md#examples.pbs-definition") section of the user guide.

For this example, you'll need to assume a scenario -- you want to capture
the HRD communication path as digital intermediate frequency and store it for future batch
processing. This saves off the raw radio frequency (RF) in-phase quadrature (I/Q) samples after
it has been digitized. Once the data is in your Amazon S3 bucket, you can demodulate and decode the
data using any software you desire. See the [MathWorks Tutorial](https://www.mathworks.com/help/satcom/ug/capture-satellite-data-using-aws-ground-station.html "https://www.mathworks.com/help/satcom/ug/capture-satellite-data-using-aws-ground-station.html") for a detailed example of processing. After using this example, you may consider
adding Amazon EC2 spot pricing components to process the data and lower your overall processing
costs.

## Communication paths

This section represents
[Plan your dataflow communication paths](getting-started.md "getting-started.md") of getting started.

All of the following template snippets belong in the Resources section of the AWS CloudFormation
template.

```

Resources:
  # Resources that you would like to create should be placed within the Resources section.

```

###### Note

For more information about the contents of a AWS CloudFormation template, see
[Template sections](../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md "../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md").

Given our scenario to deliver a single communication path to Amazon S3, you know that you'll have a
single asynchronous delivery path. Per the
[Asynchronous data delivery](getting-started.md#getting-started.step2.async-data-delivery "getting-started.md#getting-started.step2.async-data-delivery")
section, you must define a Amazon S3 bucket.

```

  # The S3 bucket where AWS Ground Station will deliver the downlinked data.
  GroundStationS3DataDeliveryBucket:
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    UpdateReplacePolicy: Retain
    Properties:
      # Results in a bucket name formatted like: aws-groundstation-data-{account id}-{region}-{random 8 character string}
      BucketName: !Join ["-", ["aws-groundstation-data", !Ref AWS::AccountId, !Ref AWS::Region, !Select [0, !Split ["-", !Select [2, !Split ["/", !Ref AWS::StackId]]]]]]

```

In addition, you will need to create the appropriate roles and policies in order to allow AWS Ground Station to use the bucket.

```

  # The IAM role that AWS Ground Station will assume to have permission find and write
  # data to your S3 bucket.
  GroundStationS3DataDeliveryRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Action:
              - 'sts:AssumeRole'
            Effect: Allow
            Principal:
              Service:
                - groundstation.amazonaws.com
            Condition:
              StringEquals:
                "aws:SourceAccount": !Ref AWS::AccountId
              ArnLike:
                "aws:SourceArn": !Sub "arn:aws:groundstation:${AWS::Region}:${AWS::AccountId}:config/s3-recording/*"

  # The S3 bucket policy that defines what actions AWS Ground Station can perform on your S3 bucket.
  GroundStationS3DataDeliveryBucketPolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyDocument:
        Statement:
          - Action:
              - 's3:GetBucketLocation'
            Effect: Allow
            Resource:
              - !GetAtt GroundStationS3DataDeliveryBucket.Arn
          - Action:
              - 's3:PutObject'
            Effect: Allow
            Resource:
              - !Join [ "/", [ !GetAtt GroundStationS3DataDeliveryBucket.Arn, "*" ] ]
      PolicyName: GroundStationS3DataDeliveryPolicy
      Roles:
        - !Ref GroundStationS3DataDeliveryRole

```

## AWS Ground Station configs

This section represents [Create configs](getting-started.md "getting-started.md") of getting started.

You'll need a _tracking-config_ to set your preference on using
autotrack. Selecting _PREFERRED_ as autotrack can improve the signal
quality, but it isn't required to meet the signal quality due to sufficient JPSS-1 ephemeris
quality.

```

  TrackingConfig:
    Type: AWS::GroundStation::Config
    Properties:
      Name: "JPSS Tracking Config"
      ConfigData:
        TrackingConfig:
          Autotrack: "PREFERRED"

```

Based on the communication path, you'll need to define an
_antenna-downlink_ config to represent the satellite portion as well as an
_s3-recording_ to refer to the Amazon S3 bucket you just created.

```

  # The AWS Ground Station Antenna Downlink Config that defines the frequency spectrum used to
  # downlink data from your satellite.
  JpssDownlinkDigIfAntennaConfig:
    Type: AWS::GroundStation::Config
    Properties:
      Name: "JPSS Downlink DigIF Antenna Config"
      ConfigData:
        AntennaDownlinkConfig:
          SpectrumConfig:
            Bandwidth:
              Units: "MHz"
              Value: 30
            CenterFrequency:
              Units: "MHz"
              Value: 7812
            Polarization: "RIGHT_HAND"

  # The AWS Ground Station S3 Recording Config that defines the S3 bucket and IAM role to use
  # when AWS Ground Station delivers the downlink data.
  S3RecordingConfig:
    Type: AWS::GroundStation::Config
    DependsOn: GroundStationS3DataDeliveryBucketPolicy
    Properties:
      Name: "JPSS S3 Recording Config"
      ConfigData:
        S3RecordingConfig:
          BucketArn: !GetAtt GroundStationS3DataDeliveryBucket.Arn
          RoleArn: !GetAtt GroundStationS3DataDeliveryRole.Arn

```

## AWS Ground Station mission profile

This section represents [Create mission profile](getting-started.md "getting-started.md") of getting started.

Now that you have the associated configs, you can use them to construct the dataflow. You'll use
the defaults for the remaining parameters.

```

  # The AWS Ground Station Mission Profile that groups the above configurations to define how to downlink data.
  JpssAsynchMissionProfile:
    Type: AWS::GroundStation::MissionProfile
    Properties:
      Name: "43013 JPSS Asynchronous Data"
      MinimumViableContactDurationSeconds: 180
      TrackingConfigArn: !Ref TrackingConfig
      DataflowEdges:
        - Source: !Ref JpssDownlinkDigIfAntennaConfig
          Destination: !Ref S3RecordingConfig

```

## Putting it together

With the above resources, you now have the ability to schedule JPSS-1 contacts for
asynchronous
data delivery from any of your onboarded AWS Ground Station [AWS Ground Station Locations](aws-ground-station-antenna-locations.md "aws-ground-station-antenna-locations.md").

The following is a complete AWS CloudFormation template that includes all resources described
in this section combined into a single template that can be directly used in AWS CloudFormation.

The AWS CloudFormation template named `AquaSnppJpss-1TerraDigIfS3DataDelivery.yml` contains
an Amazon S3 bucket and the required AWS Ground Station resources to schedule contacts and receive VITA-49
Signal/IP direct broadcast data.

If Aqua, SNPP, JPSS-1/NOAA-20, and Terra are not onboarded to your account, see
[Onboard satellite](getting-started.md "getting-started.md").

###### Note

You can access the template by accessing the customer onboarding Amazon S3 bucket using valid
AWS credentials. The links below use a regional Amazon S3 bucket.
Change the `us-west-2` region code to represent the corresponding region of which you want to create the AWS CloudFormation
stack in.

Additionally, the following instructions use YAML. However, the templates are available in
both YAML and JSON format. To use JSON, replace the `.yml` file extension with
`.json` when downloading the template.

To download the template using AWS CLI, use the following command:

```
aws s3 cp s3://groundstation-cloudformation-templates-us-west-2/AquaSnppJpss-1TerraDigIfS3DataDelivery.yml .
```

You can view and download the template in the console by navigating to the following URL
in your browser:

```
https://s3.console.aws.amazon.com/s3/object/groundstation-cloudformation-templates-us-west-2/AquaSnppJpss-1TerraDigIfS3DataDelivery.yml
```

You can specify the template directly in AWS CloudFormation using the following link:

```
https://groundstation-cloudformation-templates-us-west-2.s3.us-west-2.amazonaws.com/AquaSnppJpss-1TerraDigIfS3DataDelivery.yml
```
