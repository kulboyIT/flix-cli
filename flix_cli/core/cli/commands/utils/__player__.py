import platform
import subprocess

MPV_EXECUTABLE = "mpv"
IINA_EXECUTABLE = "iina"

VLC_INTENT = "am start -a \"android.intent.action.VIEW\""

def play(file, name, referer, subtitles):
    try:
        if(platform.system() == "Linux" or platform.system() == "Windows"):
            args = [
                MPV_EXECUTABLE,
                file,
                f"--referrer={referer}",
                f"--force-media-title=Playing {name}",
            ]
            args.extend(f"--sub-file={_}" for _ in subtitles)

            mpv_process = subprocess.Popen(args, stdout=subprocess.DEVNULL)

            mpv_process.wait()

        elif(platform.system() == "Darwin"):
            args = [
                IINA_EXECUTABLE,
                f"--mpv-referrer={referer}",
                file,
                f"--mpv-force-media-title=Playing {name}",
                "--keep-running"
            ]

            args.extend(f"--mpv-sub-files={_}" for _ in subtitles)
            
            iina_process = subprocess.Popen(args, stdout=subprocess.DEVNULL)

            iina_process.wait()

    except Exception as e:
        print("[!] no supported video player were found.")
        exit(1)

