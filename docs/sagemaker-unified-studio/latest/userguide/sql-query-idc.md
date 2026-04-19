# Query editor in IdC domains

If your Amazon SageMaker Unified Studio domain uses IAM Identity Center (IdC), the query editor
experience differs from IAM-based domains in several ways.

| Feature                 | IAM domain                                                                                                 | IdC domain                                                                                 |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Data Agent              | Multi-turn conversational SQL with step-by-step planning,<br>auto-injection of SQL cells, and Fix with AI. | Single-turn SQL generation. Multi-turn conversations and Fix with AI<br>are not available. |
| Adding SQL to querybook | Agent automatically creates cells in your querybook. You can accept,<br>reject, or accept and run.         | You manually copy the generated SQL and paste it into a SQL<br>cell.                       |
