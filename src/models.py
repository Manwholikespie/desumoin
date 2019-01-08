"""
Place classes you make here.
"""

import uuid

# Just an example of what you might put here.
class Author(object):
    def __init__(self, name, author_id=None):
        name = name.strip()
        self.name = name

        if author_id:
            self.id = author_id
        else:
            # generate one
            self.id = str(uuid.uuid5(uuid.NAMESPACE_URL, name.lower()))
