# HalbVier

Plays the Song Deutschland by Alan Aztec on your discord Server at halb vier.

## Usage
###Docker
```docker run -e BOT_TOKEN=<token> -e VOICE_CHANNEL=<id> -e ANNOUNCEMENT_CHANNEL=<id> canonip/halbvier ```

Compose:

| Environment variable | Description                                              |   |   |   |
|----------------------|----------------------------------------------------------|---|---|---|
| BOT_TOKEN            | Token from your application account                      |   |   |   |
| VOICE_CHANNEL        | ID of the channel, where the music will be played        |   |   |   |
| ANNOUNCEMENT_CHANNEL | ID of the text-channel, where HalbVier will be announced |   |   |   |
|                      |                                                          |   |   |   |