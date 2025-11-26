import sys
import os

def prepare_toml(platform_name):
    with open("gemini-extension.toml", "r") as f:
        content = f.read()

    if platform_name == "win32":
        # On Windows, we'll use telegram.exe
        # We replace "python src/client.py" with "telegram.exe"
        # Note: We might need ".\telegram.exe" if simple filename fails, 
        # but "telegram.exe" is usually fine if CWD is the dir.
        new_content = content.replace("python src/client.py", "telegram.exe")
    else:
        # On Unix, we need ./telegram
        new_content = content.replace("python src/client.py", "./telegram")

    # Write to dist folder
    os.makedirs("dist", exist_ok=True)
    with open("dist/gemini-extension.toml", "w") as f:
        f.write(new_content)
    
    print(f"Created dist/gemini-extension.toml for {platform_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python prepare_release.py <platform>")
        sys.exit(1)
    
    prepare_toml(sys.argv[1])

