import irc.bot
import os
from datetime import datetime

SERVER = "irc.libera.chat"
PORT = 6667
CHANNEL = "#example"
NICK = "LogBot123"

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

class LoggerBot(irc.bot.SingleServerIRCBot):

    def __init__(self):
        super().__init__([(SERVER, PORT)], NICK, NICK)

    def on_welcome(self, connection, event):
        print("Connected")
        connection.join(CHANNEL)

    def on_pubmsg(self, connection, event):
        nick = event.source.nick
        message = event.arguments[0]

        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] <{nick}> {message}\n"

        logfile = os.path.join(LOG_DIR, f"{CHANNEL.strip('#')}.log")

        with open(logfile, "a") as f:
            f.write(line)

        print(line.strip())

bot = LoggerBot()
bot.start()
