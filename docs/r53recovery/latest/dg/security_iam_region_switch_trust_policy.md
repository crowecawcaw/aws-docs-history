# Plan execution role trust policy

This is the trust policy required for the plan's execution role, so that ARC can run a Region switch plan.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "arc-region-switch.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
