# Step 6: Test your inbound

configuration

Testing ensures your complete inbound workflow functions correctly before processing
real business documents. This validates that all components work together and helps
identify any configuration issues.

###### To test your configuration

1. Create a test EDI file named `test-850.edi` with this
   content:

```
ISA*00*          *00*          *ZZ*SUPPLIER       *ZZ*ACMECORP       *230101*1200*U*00401*000000001*0*P*>~
GS*PO*SUPPLIER*ACMECORP*20230101*1200*1*X*004010~
ST*850*0001~
BEG*00*SA*TEST123**20230101~
N1*ST*ACME CORPORATION~
N3*456 TEST AVENUE~
N4*TESTCITY*CA*90210*US~
PO1*1*5*EA*15.50**BP*TEST001*VN*TEST-WIDGET~
PID*F****TEST PREMIUM WIDGET~
SE*8*0001~
GE*1*1~
IEA*1*000000001~
```

2. Upload the test file to your input bucket:
   1. Navigate to
      `my-b2bi-input-bucket-`your-account-id``
      in the Amazon S3 console.
   2. Choose **Upload**.
   3. Select your `test-850.edi` file.
   4. Choose **Upload**.

3. Monitor the transformation:
   - Wait 2-3 minutes for processing
   - Check your output bucket for the transformed JSON file
   - The output will be in a directory structure like:
     ``partnership-id`/`capability-id`/processed/`

4. Verify the JSON output contains the expected purchase order data.

## Expected results

- JSON file appears in output bucket within 2-3 minutes
- File contains properly formatted purchase order data
- CloudWatch logs show successful transformation (if logging enabled)
