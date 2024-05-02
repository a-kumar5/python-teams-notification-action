## Python teams notification github action

A GitHub Action that takes microsoft teams webhook url as input and send notification to teams channel

**Table of Contents**

<!-- toc -->

- [Usage](#usage)
- [License Summary](#license-summary)
- [Security Disclosures](#security-disclosures)

<!-- tocstop -->

## Usage

To send a message to a Teams channel, you'll need the following prerequisites:

**Teams Channel Webhook URL**: Obtain the webhook URL for the channel you want to send messages to. If you don't have it already, you can create a webhook in your Teams channel settings.

Once you have the webhook URL, follow these steps to integrate it into your workflow:

```yaml
    - name: Send Notification To Teams Channel
      uses: a-kumar5/python-teams-notification-action@v0.2.0-alpha
      with:
        url: "<REPLACE WITH YOU TEAMS CHANNEL WEBHOOK URL>"
        content: "pymsnotify sent this message from github actions."
        title: "HELLO_TEAMS"
```
To send a message to a Teams channel, you can utilize GitHub Secrets to securely fetch the webhook URL without directly exposing it in your workflow script. Follow these steps:

1. **Set Up GitHub Secrets**: First, ensure you have set up a secret in your GitHub repository to store the Teams channel webhook URL securely. You can do this by navigating to your repository's settings, then selecting "Secrets" or "Secrets and keys", and adding a new secret with a descriptive name (e.g., `TEAMS_URL`) and the corresponding webhook URL value.

2. **Access GitHub Secrets in Your Workflow**: Modify your workflow script to access the secret value during execution. GitHub automatically injects secrets as environment variables, making it easy to retrieve them within your workflow steps.

3. **Integrate the Webhook URL**: Use the retrieved webhook URL within your workflow script to send messages to the Teams channel. You can reference the secret directly as an environment variable, ensuring that the actual URL remains concealed.

Here's an example of how you might access the secret in a workflow step using the syntax `${{ secrets.YOUR_SECRET_NAME }}`:

```yaml
    - name: send_notification
      uses: a-kumar5/python-teams-notification-action@v0.2.0-alpha
      with:
        url: ${{ secrets.TEAMS_URL }}
        content: "pymsnotify sent this message from github actions."
        title: "HELLO_TEAMS"
```

## License Summary

This code is made available under the Apache License.

## Security Disclosures

If you would like to report a potential security issue in this project, please create a GitHub issue.