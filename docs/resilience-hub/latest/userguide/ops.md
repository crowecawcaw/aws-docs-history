# Reviewing operational recommendations

Operational recommendations contain recommendations to set up alarms, SOPs, and
AWS FIS experiments through AWS CloudFormation templates.

AWS Resilience Hub provides AWS CloudFormation template files for you to download and manage the
application's infrastructure as code. As a result, we supply recommendations in
AWS CloudFormation so that you can add them to your application code. If the size of
AWS CloudFormation template file is more than one MB and contains more than 500 resources,
AWS Resilience Hub generates more than one AWS CloudFormation template file where the size of each
file is not more than one MB and contains up to 500 resources. If the AWS CloudFormation
template file is split into multiple files, the AWS CloudFormation template file names will
be appended with `partXofY`, where `X` denotes the file number
in the sequence and `Y` denotes the total number of files the AWS CloudFormation
template file is divided into. For example, if the template file
`big-app-template5-Alarm-104849185070-us-west-2.yaml` is divided into
four files, the file names would be as follows:

- `big-app-template5-Alarm-104849185070-us-west-2-part1of4.yaml`
- `big-app-template5-Alarm-104849185070-us-west-2-part2of4.yaml`
- `big-app-template5-Alarm-104849185070-us-west-2-part3of4.yaml`
- `big-app-template5-Alarm-104849185070-us-west-2-part4of4.yaml`
  However, in case of large AWS CloudFormation templates, you are requested to provide the
  Amazon Simple Storage Service URI instead of using CLI/API with local file as input.

In AWS Resilience Hub, you can perform the following actions:

- You can provision the selected alarms, SOPs, and AWS FIS experiments. To
  provision alarms, SOPs, and AWS FIS experiments, select the appropriate
  recommendation and enter a unique name. AWS Resilience Hub creates a template based
  on your selected recommendations. In **Templates**, you can
  access your created templates through an Amazon Simple Storage Service (Amazon S3) URL.
- You can include or exclude selected alarms, SOPs, and AWS FIS experiments
  that were recommended for your application at any point of time. For more
  information see, [Including or excluding operational
  recommendations](exclude-recommend.md "exclude-recommend.md").
- You can also search, create, add, remove, and manage tags, for an
  application and see all the tags associated with it.
