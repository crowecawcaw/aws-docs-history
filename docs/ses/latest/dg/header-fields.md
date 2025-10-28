# Amazon SES header fields

Amazon SES can accept all email headers that follow the format described in [RFC 822](https://www.rfc-editor.org/rfc/rfc822.html "https://www.rfc-editor.org/rfc/rfc822.html").

The following fields can't appear more than once in the header section of a
message:

- `Accept-Language`
- `acceptLanguage`
- `Archived-At`
- `Auto-Submitted`
- `Bounces-to`
- `Comments`
- `Content-Alternative`
- `Content-Base`
- `Content-Class`
- `Content-Description`
- `Content-Disposition`
- `Content-Duration`
- `Content-ID`
- `Content-Language`
- `Content-Length`
- `Content-Location`
- `Content-MD5`
- `Content-Transfer-Encoding`
- `Content-Type`
- `Date`
- `Delivered-To`
- `Disposition-Notification-Options`
- `Disposition-Notification-To`
- `DKIM-Signature`
- `DomainKey-Signature`
- `Errors-To`
- `From`
- `Importance`
- `In-Reply-To`
- `Keywords`
- `List-Archive`
- `List-Help`
- `List-Id`
- `List-Owner`
- `List-Post`
- `List-Subscribe`
- `List-Unsubscribe`
- `List-Unsubscribe-Post`
- `Message-Context`
- `Message-ID`
- `MIME-Version`
- `Organization`
- `Original-From`
- `Original-Message-ID`
- `Original-Recipient`
- `Original-Subject`
- `Precedence`
- `Priority`
- `References`
- `Reply-To`
- `Return-Path`
- `Return-Receipt-To`
- `Sender`
- `Solicitation`
- `Sensitivity`
- `Subject`
- `Thread-Index`
- `Thread-Topic`
- `User-Agent`
- `VBR-Info`

###### Considerations

- The `acceptLanguage` field is non-standard. If possible, you should use
  the `Accept-Language` header instead.
- If you specify a `Date` header, Amazon SES overrides it with a timestamp
  that corresponds to the date and time in the UTC time zone when Amazon SES accepted the
  message.
- If you provide a `Message-ID` header, Amazon SES overrides the header with
  its own value.
- If you specify a `Return-Path` header, Amazon SES sends bounce and complaint
  notifications to the address that you specified. However, the message that your
  recipients receive contains a different value for the `Return-Path`
  header.
- If you use the Amazon SES API v2 `SendEmail` operation with either
  _Simple_ or _Templated_ content, or use
  the `SendBulkEmail` operation, you cannot set custom header content for
  headers that are set by SES; therefore, the following headers are disallowed
  as custom headers:
  - `BCC`, `CC`, `Content-Disposition`,
    `Content-Type`, `Date`, `From`,
    `Message-ID`, `MIME-Version`,
    `Reply-To`, `Return-Path`, `Subject`,
    `To`
