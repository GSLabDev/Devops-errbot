# Devops-errbot

- [Introduction](#introduction)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
    - [Image Runtime Config](#image-runtime-config)
    - [Bot Runtime Config](#bot-runtime-config)
- [Persistence](#persistence)
- [Use your own config file](#use-your-own-config-file)
- [Run Err with extra arguments](#run-err-with-extra-arguments)
    - [Alternative config file](#alternative-config-file)
    - [Err Help](#err-help)
    - [Run with text debug backend](#run-with-text-debug-backend)
- [Exposed Ports](#exposed-ports)

# Introduction

Documentation for [Errbot](http://errbot.io) (the pluggable chatbot).

# Quick Start

```
docker run -d \
     --name err \
     -e BACKEND=Slack \
     -e BOT_ADMINS=bipeen.sawant@gslab.com \
     -e CHATROOM_PRESENCE=milind,iotspbot,bipeen.sawant \
     -e BOT_TOKEN=xoxb-197423219299-HtY88HbbQ9R9UzLCUlLBx1g1 \
     -e BOT_LOG_LEVEL=DEBUG \
     bipeen/devops-errbot

Once your container is up and running you can verify your slack is connected to errbot by running !help on the slack channel listed in BOT_ADMINS. This will also list down all the plugins commands with description. 

```

# Configuration

## Integrating chatopsbot to slack:
- First create a slack team https://slack.com/create
- Now create a bot user for your slack team https://my.slack.com/services/new/bot This bot user will enable to interact with any external service in our case its errbot.
Note the name of bot user created in step 2 we need it to set BOT_ADMINS env while building the devops-errbot.
- Also note the api-token of the created bot user and set it as BOT_TOKEN env.

## Linking to existing bot user in Slack.
- Log-in to your slack account
- To list your bot user go to https://my.slack.com/services/new/bot. Then note the api-token and bot user name of the existing bot user and set it as BOT_TOKEN and BOT_ADMINS env respectively.

## Image Runtime Config

- **WAIT**: Seconds to sleep before starting the bot. Defaults to `None`

## Bot Runtime Config

Below is the complete list of available options that can be used to customize your Err bot. See [config-template.py](https://raw.githubusercontent.com/gbin/err/master/errbot/config-template.py) for complete settings documentation.

- **BACKEND**: Chat server type. (XMPP, Text, HipChat, Slack, IRC). Defaults to `XMPP`.
- **BOT_LOG_LEVEL**: Change log level. Defaults to `INFO`.
- **BOT_USERNAME**: The UID for the bot user.
- **BOT_PASSWORD**: The corresponding password for the user.
- **BOT_TOKEN**: Token for HipChat and Slack backend.
- **BOT_SSL**: Use SSL for IRC backend. Default to `False`.
- **BOT_ENDPOINT**: HipChat endpoint for hosted HipChat.
- **BOT_NICKNAME**: Nickname for IRC backend.
- **BOT_ADMINS**: Bot admins separated with comma. Defaults to `admin@localhost`. Count should be less than 3.
- **CHATROOM_PRESENCE**: Chatrooms your bot should join on startup.
- **CHATROOM_FN**: The FullName, or nickname, your bot should use. Defaults to `Err`.
- **BOT_PREFIX**: Command prefix for the bot. Default to `!`.
- **BOT_PREFIX_OPTIONAL_ON_CHAT**: Optional prefix for normal chat. Default to `False`.
- **BOT_ALT_PREFIXES**: Alternative prefixes.
- **BOT_ALT_PREFIX_SEPARATORS**: Alternative prefixes separators.
- **BOT_ALT_PREFIX_CASEINSENSITIVE**:  Require correct capitalization. Defaults to `False`.
- **HIDE_RESTRICTED_COMMANDS**: Hide the restricted commands from the help output. Defaults to `False`.
- **MESSAGE_SIZE_LIMIT**: Maximum length a single message may be. Defaults to `10000`.

# Persistence

For storage of the application data, you should mount a volume at

* `/srv`

Create the directories for the volume

```bash
mkdir /tmp/errbot /tmp/errbot/ssl /tmp/errbot/data /tmp/errbot/plugins
chmod -R 777 /tmp/errbot
```

# Use your own config file

```bash
curl -sL https://raw.githubusercontent.com/gbin/err/master/errbot/config-template.py -o /tmp/errbot/config.py
```

# Run Err with extra arguments

If you pass arguments to Errbot you have to set the `-c /srv/config.py` argument by your self to run with the default config.

## Alternative config file

```bash
docker run -it -v /tmp/errbot:/srv bipeens/Devops-errbot -c /srv/production.py
```

## Run with text debug backend

```bash
docker run -it -v /tmp/errbot:/srv bipeens/Devops-errbot -c /srv/config.py -T
```

# Exposed Ports

* 3142 (Webserver if configured)

# Get list of plugins

