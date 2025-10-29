from datetime import datetime
import re
import os

def smart_log(*args, **kwargs) -> None:
   
    # kwargs
    level = str(kwargs.get("level", "info")).lower()
    timestamp_opt = bool(kwargs.get("timestamp", True))
    date_opt = bool(kwargs.get("date", False))
    save_to = kwargs.get("save_to", None)
    colored = bool(kwargs.get("color", kwargs.get("colored", True)))

    message = " ".join(map(str, args)) if args else ""

    # time / date 
    time_prefix = ""
    if timestamp_opt or date_opt:
        if timestamp_opt and date_opt:
            time_prefix = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elif timestamp_opt:
            time_prefix = datetime.now().strftime("%H:%M:%S")
        else:  
            time_prefix = datetime.now().strftime("%Y-%m-%d")
        time_prefix += " "

    # level 
    level_map = {
        "info": ("INFO", "\033[34m"),     # blue
        "debug": ("DEBUG", "\033[90m"),   # gray
        "warning": ("WARNING", "\033[33m"),# yellow
        "error": ("ERROR", "\033[31m"),   # red
    }
    label_text, color_code = level_map.get(level, ("INFO", "\033[34m"))
    label = f"[{label_text}]"


    if colored:
        reset = "\033[0m"
        printed = f"{time_prefix}{color_code}{label}{reset} {color_code}{message}{reset}".rstrip()
    else:
        printed = f"{time_prefix}{label} {message}".rstrip()


    print(printed)
    if save_to:
        try:
            with open(save_to, "a", encoding="utf-8") as f:
                ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
                clean_message = ansi_escape.sub('', printed)
                f.write(clean_message + "\n")
        except Exception as e:
            print(f"Failed to write log to {save_to}: {e}")
pass
smart_log("This is an info message.")
smart_log("This is a debug message.", level="debug", timestamp=True)
smart_log("This is a warning message with date.", level="warning", date=True)       
smart_log("This is an error message without color.", level="error", color=False)
smart_log("This message will be saved to a file.", save_to="log.txt")
