# Detection Test Plan: SSH Brute Force

## Objective
Determine whether repeated failed SSH authentication attempts are logged and whether the configured Wazuh rules generate an appropriate alert.

## Preconditions
- Use only a lab host you own or are authorized to test.
- Confirm SSH is enabled on the intended target.
- Confirm authentication logs are collected by Wazuh.
- Use a small, controlled test; do not test third-party systems.

## Procedure
1. Record the target, source, test window, and timezone.
2. Generate a controlled series of failed logins using a test account.
3. Inspect the target's authentication logs.
4. Search Wazuh for the same time window and source.
5. Record whether the event sequence and a relevant alert were observed.
6. Check for successful logins and other related events.
7. Document limitations and remediation recommendations.

## Required evidence
- Original authentication log entries
- Wazuh event/alert details, if any
- Actual rule ID and level, if an alert was generated
- Test timestamp and redacted source/target identifiers

## Status
**Author-reported status:** Tested and alert observed in the lab. Public evidence is pending. Add a genuine screenshot and sanitized source-log/alert details before claiming independently verifiable detection.
