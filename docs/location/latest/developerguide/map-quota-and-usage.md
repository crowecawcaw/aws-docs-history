# Map quotas and usage

Amazon Location Service imposes specific service quotas and usage limits for both dynamic and static
maps. These limits are put in place to ensure fair usage and performance efficiency
across all users. Below are the service quotas and adjustable limits for each
service.

## Service quotas

Amazon Location Service sets default quotas for APIs to help manage service capacity, which can
be viewed in the [AWS service
quotas management console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas"). You can request an increase in quotas through
the [self-service console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas"), for up to twice the default limit for each API.

For quota limits exceeding twice the default limit, request through the self
service console and it will automatically submit a support ticket. Alternately,
connect with your premium support team.

There are no direct charges for quota increase requests, but higher usage levels
may lead to increased service costs based on the additional resources consumed. For
more information, see [Manage quotas with Service Quotas](manage-quotas.md "manage-quotas.md").

### Dynamic map

| API name   | Default | Max adjustable limit | More than Adjustable Max limit                                                                                                                                                                                                                     |
| ---------- | ------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GetTiles` | 2000    | 4000                 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact support<br>team |

### Static map

| API name       | Default | Max adjustable limit | More than Adjustable Max limit                                                                                                                                                                                                                     |
| -------------- | ------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GetStaticMap` | 50      | 100                  | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact support<br>team |

## Usage limits

| API name             | Limit                                     | Value |
| -------------------- | ----------------------------------------- | ----- |
| `GetStyleDescriptor` | Max requests, per second, per IP address. | 5000  |
| `GetGlyphys`         | Max requests, per second, per IP address. | 5000  |
| `GetSprites`         | Max requests, per second, per IP address. | 5000  |
| `GetStaticMap`       | Response payload size after compression.  | 6MB   |
| `GetTiles`           | Response payload size after compression.  | 6MB   |

## Terms

For more information, see [Terms of use and data attribution](data-attribution.md "data-attribution.md").
