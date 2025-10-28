# ADVPERF04-BP01 Choose a data management strategy that matches your availability, latency, and access requirements

Customers need to have a clear data management strategy for their
advertising workload datastores. The factors to consider are
latency needs, availability needs which will help them chose the
right AWS data service

## Implementation guidance

The following are the most common data stores available in adtech:

- **User data:** Demographic data (age, gender, and
  location), behavioral data (browsing history, interests, and purchase history), and
  device data (device type, operating system, and browser).
- **Audience data:** Segmentation data (personas and target
  audiences) and geo-location data (IP addresses and GPS coordinates).
- **Campaign data:** Ad creative data (like images, videos,
  and text), ad placement data (websites, apps, and platforms), and campaign performance
  data (impressions, clicks, and conversions)
- **Inventory data:** Publisher data (website or app details
  and traffic data) and ad space data (ad sizes, formats, or placements)
- **Pricing and bidding data:** Bid data (bid prices and bid
  strategies) and auction data (bid landscape and winning bids).
- **Third-party data:** Data from Data Management Platforms
  (DMPs) and data from data exchanges or marketplaces.
- **Analytics and reporting data:** Conversion data (sales,
  leads, and actions), attribution data (tracking user journeys), and engagement data
  (view-through rates and dwell times)

For latency, consider the following:

- **Low-latency data (real-time or near real-time):** This
  data needs to be processed and acted upon within milliseconds to ensure optimal ad
  delivery, real-time bidding, and accurate tracking of user interactions.
  - Bid (bid requests, bid responses, and auction data)
  - User (device data, location data, and contextual data)
  - Ad impression (ad requests and ad responses)
  - Real-time campaign performance (clicks, impressions, and conversions)

- **Medium-latency data (near real-time or batch
  processing):** This data can be processed in near real-time (within minutes
  or hours) or in batches, as it is used for audience targeting, campaign optimization,
  and attribution analysis.
  - User behavior (browsing history and interests)
  - Audience segmentation
  - Campaign optimization (performance metrics and engagement data)
  - Attribution (user journeys and conversion paths)

- **High-latency data (batch processing or offline)**: This
  data can be processed in batches or offline, as it is typically used for analysis,
  reporting, and long-term decision-making rather than real-time ad delivery or
  optimization.
  - Historical campaign
  - Detailed analytics and reporting
  - Third-party (from DMPs or data exchanges)
  - Ad creative (images and videos)

## Resources

- [Architecture III: Picking the Right Data Store for Your Workload](https://aws.amazon.com/blogs/startups/how-to-pick-the-right-data-store-for-your-workload-1/ "https://aws.amazon.com/blogs/startups/how-to-pick-the-right-data-store-for-your-workload-1/")
