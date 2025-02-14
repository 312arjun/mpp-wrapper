from .cli_wrapper import CLIWrapper

cli = CLIWrapper()

connect = cli.connect
disconnect = cli.disconnect

__all__ = ["connect", "disconnect"]
