# Evidence collection log

Authentic historical screenshots are included in `../screenshots/`. The network-scan screenshot visibly shows Wazuh event rows labelled `Nmap Scan Detected: Windows Firewall blocked TCP connection from Kali`, rule ID `100100`, level `10`. The Windows authentication screenshot shows Windows logon-failure events (rule ID `60122`); it is not proof of an SSH-specific alert. A separate SSH-specific alert screenshot/event is still needed.

The Windows Firewall source-log screenshot includes `DROP TCP` entries with source/destination IP columns redacted. It does not independently prove that the custom Wazuh firewall rule fired end-to-end.

For each new test, record:

| Field | Value to record |
|---|---|
| Test name | SSH brute-force / network scan / other |
| Date and timezone | Actual value from the test |
| Source and target | Sanitized lab identifiers |
| Source log | Actual log source and event excerpt |
| Wazuh alert | Actual rule ID, level, timestamp, and description |
| Correlation | How the alert matches the source event(s) |
| Outcome | Detected / event collected only / not detected / inconclusive |
| Evidence | Relative path to real screenshot or sanitized log |
| Limitations | Missing telemetry, false-positive possibilities, or scope limits |

Never put passwords, tokens, private keys, or unnecessary personal data in this repository.
