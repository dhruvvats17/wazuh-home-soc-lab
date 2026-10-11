# Portfolio walkthrough: how to explain this project

Use this as a speaking guide, not as a claim of production experience.

## 60-second overview

“I built a personal Wazuh home SOC lab to practice SOC Level 1 tasks. My environment uses Ubuntu Server for the Wazuh stack, a Windows 11 endpoint with the Wazuh Agent and Sysmon, and Kali Linux for controlled testing. I practiced reviewing endpoint telemetry, investigating SSH authentication failures and network-scan alerts, and documenting findings. I am continuing to add sanitized screenshots and evidence so the results can be reviewed independently.”

## How to explain an alert investigation

1. State the alert title and timestamp from the actual dashboard.
2. Identify the source and target using sanitized lab labels.
3. Review the rule ID, severity, and original event fields.
4. Correlate with nearby events and the source log.
5. Explain why the behavior is expected or suspicious in the test context.
6. State limitations and next steps without claiming compromise unless evidence supports it.

## Interview honesty checklist

- Never invent a rule ID, severity, count, timestamp, or screenshot.
- If evidence is not in GitHub, say that the test was performed but the public evidence is still being documented.
- Explain what you personally configured and what you are still learning.
- Be ready to demonstrate the live lab if asked.
