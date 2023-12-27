import os

from typing import Final
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY: Final = os.environ["OPENAI_API_KEY"]
TOKEN: Final = os.environ["TELEGRAM_KEY"]


BOT_USERNAME: Final = "KhargolGroBogukBot"
FAIS_STORAGE: Final = "chat_index_fais-23-chunk-100"
