# Wazuh Local Rules

`local_rules.example.xml` is a placeholder, not a finished detection rule. It intentionally contains no fabricated matching logic.

Before publishing an actual rule:
1. Remove sensitive data from the file.
2. Use a valid, unused rule ID.
3. Confirm the event decoder and field names.
4. Validate the XML and Wazuh configuration.
5. Test a matching and a non-matching event.
6. Record the observed alert and any false positives.
7. Include the tested Wazuh version and rollback instructions.

Do not upload the entire private `ossec.conf` or secrets.
