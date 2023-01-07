import subprocess


def disable_telemetry():

    subprocess.run(["sc", "stop", "DiagTrack"])

    subprocess.run(["sc", "config", "DiagTrack", "start=", "disabled"])

    subprocess.run(["reg", "add", "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection", "/v", "AllowTelemetry", "/t", "REG_DWORD", "/d", "0", "/f"])

disable_telemetry()