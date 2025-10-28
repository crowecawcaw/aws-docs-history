# Quotas in Device Farm desktop browser testing

Exceeding the following limits will result in session creation failure:

- You may have up to 50 sessions in an `active` state at any time.
- You may create up to 5 sessions per second.
- You may call `createTestGridUrl` up to 10 times a second.
- No `POST` payload may be greater than 30MB.
  If you have too many open sessions or create them too fast, session creation will fail.
  If you require more than 50 concurrent sessions, open a technical support case with your use
  case. For more information about increasing your service quota, see [AWS Service
  Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").
