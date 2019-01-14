# DesuMoin

Hello. For starters, this will be just a simple website that I can use to record and organize quotes made by my friends. Maybe some day it will turn into a wiki-inspired service.

## Installation Requirements

This project uses elasticsearch (6.5) for its database. You might want to disable the disk space watermark:

```json
PUT desumoin/_settings
{
    "index": {
        "blocks": {
            "read_only_allow_delete": "false"
        }
    }
}
```