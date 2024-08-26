from colorlog import ColoredFormatter

formatter = ColoredFormatter(
    '[%(log_color)s%(levelname)s%(reset)s] [%(purple)s%(asctime)s%(reset)s] {{%(light_red)s%(name)s%(reset)s:%(light_cyan)s%(lineno)d%(reset)s}} %(light_black)s>%(reset)s> %(message)s',
 datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        "DEBUG": "green",
        "INFO": "light_green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red",
    },
 reset=True,
 secondary_log_colors={},
 style='%'
)