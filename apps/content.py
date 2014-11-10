from superdesk.resource import Resource


metadata_schema = {
    'guid': {
        'type': 'string',
        'unique': True
    },
    'unique_id': {
        'type': 'integer',
        'unique': True
    },
    'unique_name': {
        'type': 'string',
        'unique': True
    },
    'parent_id': {
        'type': 'string',
        'unique': True
    },
    'version': {
        'type': 'integer'
    },
    'original_creator': Resource.rel('users', True),
    'version_creator': Resource.rel('users', True),
    'firstcreated': {
        'type': 'datetime'
    },
    'versioncreated': {
        'type': 'datetime'
    },
    'ingest_provider': Resource.rel('ingest_providers', True),
    'source': {     # The value is copied from the ingest_providers vocabulary
        'type': 'string'
    },
    'original_source': {    # This value is extracted from the ingest
        'type': 'string'
    },
    'ingest_provider_sequence': {
        'type': 'string'
    },
    'usageterms': {
        'type': 'string'
    },
    'type': {
        'type': 'string',
        'required': True,
        'allowed': ['text', 'audio', 'video', 'picture', 'graphic', 'composite'],
        'default': 'text'
    },
    'mimetype': {
        'type': 'string'
    },
    'pubstatus': {
        'type': 'string'
    },
    'language': {
        'type': 'string'
    },
    'place': {
        'type': 'list'
    },
    'subject': {
        'type': 'list'
    },
    'byline': {
        'type': 'string'
    },
    'headline': {
        'type': 'string'
    },
    'located': {
        'type': 'string'
    },
    'renditions': {
        'type': 'dict'
    },
    'slugline': {
        'type': 'string'
    },
    'creditline': {
        'type': 'string'
    },
    'description_text': {
        'type': 'string',
        'nullable': True
    },
    'filemeta': {
        'type': 'dict'
    },
    'urgency': {
        'type': 'integer'
    },
    'groups': {
        'type': 'list'
    },
    'keywords': {
        'type': 'list'
    },
    'body_html': {
        'type': 'string'
    },
    'media_file': {
        'type': 'string'
    },
    'contents': {
        'type': 'list'
    },
    'task_id': {
        'type': 'string'
    },
    'lock_user': Resource.rel('users', True),
    'lock_time': {
        'type': 'datetime'
    },
    'lock_session': Resource.rel('auth', True),
    'is_spiked': {
        'type': 'boolean'
    },
    'expiry': {
        'type': 'datetime'
    }
}
