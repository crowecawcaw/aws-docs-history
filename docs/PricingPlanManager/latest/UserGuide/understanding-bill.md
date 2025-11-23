# Understanding Your Bill

## AWS Invoice

Flat-rate plans appear as consolidated line items on your AWS invoice, grouped by service package and a consolidated charge line item for all plan tiers.

**Example Invoice**

```
Service: CloudFront Flat-Rate Plans
Active plans: 2x Free, 1x Pro, 3x Business, and 1x Premium

  Free plan (2 count)                       $0.00  {not on invoice}
  Pro plan (1 count)                       $15.00  {not on invoice}
  Business plan (3 count)                 $600.00  {not on invoice}
  Premium plan (1 count)                $1,000.00  {not on invoice}
  CloudFront Flat-Rate Plans            $1,615.00  {single line item on invoice}
```

## Bills Page

Flat-rate plans appear on the Bills page with a hierarchical structure.

**Example Bills Page Display**

```
CloudFront Flat-Rate Plans                                          USD 1015.00
└── Any                                                             USD 1015.00
    └── CloudFront Flat-Rate Plans CloudFrontPlan                   USD 1015.00
        └── $15.00 per Pro plan                     1.000 Count       USD 15.00
        └── $1000.00 per Premium plan               1.000 Count     USD 1000.00
```

### Key Display Elements

- Service Name: `CloudFront Flat-Rate Plans`
- Usage Quantity: Shows billing period fraction (e.g., "1.000 Count" for full month, "0.554 Count" for mid-cycle activation)
- Amount: Pro-rated charges based on billing period
- No Usage Metrics: Only charge information is displayed, not requests or data transfer
- Plan Aggregation: Multiple plans of the same tier are aggregated into a single line
- Mid-Cycle Charges: For pro-rated or partial month charges, the count reflects the portion of the month the plan was active. For example, two Premium plans activated on the 20th and 24th of a 30-day month would show counts of 0.367 and 0.233 respectively, totaling 0.600 Count.

## Pro-Ration Calculations

### Mid-Cycle Upgrades

```
Daily rate = Monthly cost ÷ Days in month
Pro-rated charge = Daily rate × Days remaining

Example (July 15 upgrade, 31-day month):
Pro tier: $15/month ÷ 31 days = $0.48/day
Business tier: $200/month ÷ 31 days = $6.45/day
Days remaining: 17 days

Calculation:
- Pro tier (full month): $15.00
- Business tier (17 days): $109.65
- Adjustment for tier difference (17 days): -$8.16
Net charge for the month: $116.49
```

### Mid-Cycle Downgrades

Downgrades take effect at the next billing cycle with no mid-cycle pro-ration.
