import os
import subprocess

class CLIWrapper:
    def __init__(self):
        """Find the executable inside the installed package."""
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.cli_path = os.path.join(base_path, "bin", "mpp.exe")

        if not os.path.exists(self.cli_path):
            raise FileNotFoundError(f"Executable not found at {self.cli_path}")

    def _run_command(self, command):
        """Run the CLI command and print logs."""
        cmd = [self.cli_path, command]
        print(f"Executing: {cmd}")

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        for line in process.stdout:
            print(line, end="")

        process.stdout.close()
        return_code = process.wait()

        if return_code != 0:
            error_output = process.stderr.read().strip()
            raise RuntimeError(f"Error: {error_output}")
