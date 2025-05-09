import os
from pathlib import Path

__WEIGHTS_DIR = Path("weights")
OMNI_PARSER_DIR = os.path.join(__WEIGHTS_DIR, "AI-ModelScope", "OmniParser-v2___0") 
def download():
    from modelscope import snapshot_download
    # Create weights directory
    __WEIGHTS_DIR.mkdir(exist_ok=True)
    snapshot_download(
        'AI-ModelScope/OmniParser-v2.0',
        cache_dir='weights',
        )
    
if __name__ == "__main__":
    download()