# Case Events

Case Created by AWS Responder

```

            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Created",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T00:00:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "createdBy": "AWS Responder"
              }
            }

```

Case Created by Service

```

            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Created",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T00:00:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "createdBy": "security-ir.amazonaws.com"
              }
            }

```

Case Created by Customer

```

            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Created",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T00:00:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "createdBy": "111122223333"
              }
            }

```

Case Updated by AWS Responder

```

            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Updated",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T01:30:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "updatedBy": "AWS Responder"
              }
            }

```

Case Updated by AWS Customer

```

            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Updated",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T02:15:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "updatedBy": "111122223333"
              }
            }

```

Case Updated by AWS Security Incident Response Service

```

            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Updated",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T03:45:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "updatedBy": "security-ir.amazonaws.com"
              }
            }

```

Case Closed

```

            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Closed",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-15T14:22:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890"
              }
            }

```
