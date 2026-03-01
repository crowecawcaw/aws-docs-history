# Step 3: Test your revocation function

Use the CloudFront console to test your Connection Function with sample certificates.
Navigate to the Connection Function in the console and use the Test tab.

**Test with sample certificates**

1. Paste a sample certificate in PEM format into the test interface
2. Optionally specify a client IP address for testing IP-based logic
3. Choose **Test function** to see the execution
   results
4. Review the execution logs to verify your function logic
   Test with both valid and revoked certificates to ensure your function handles both
   scenarios correctly. The execution logs show console.log output and any errors that
   occur during function execution.
