import subprocess
import os

class CLIWrapper:
    def __init__(self):
        """Initialize the CLI wrapper with the bundled executable."""
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.cli_path = os.path.join(base_path, "bin", "mpp.exe")
        self.connected = False

    def _run_command(self, command):
        """Helper function to run a CLI command and stream logs."""
        cmd = [self.cli_path, command]
        print(f"Executing: {' '.join(cmd)}")

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        for line in process.stdout:
            print(line, end="")  # Print CLI output in real-time

        process.stdout.close()
        return_code = process.wait()

        if return_code != 0:
            error_output = process.stderr.read().strip()
            raise RuntimeError(f"Error: {error_output}")

    def connect(self):
        """Connect using the CLI (no arguments)."""
        if self.connected:
            print("Already connected.")
            return
        self._run_command("connect")
        self.connected = True

    def disconnect(self):
        """Disconnect using the CLI."""
        if not self.connected:
            print("Not connected.")
            return
        self._run_command("disconnect")
        self.connected = False
