# -*- coding: utf-8 -*-

"""cernopendata base Invenio configuration."""

from __future__ import absolute_import, print_function

from invenio_marc21.config import \
    MARC21_REST_ENDPOINTS as RECORDS_REST_ENDPOINTS
from invenio_records_rest.facets import terms_filter


# Identity function for string extraction
def _(x):
    return x

# Default language and timezone
BABEL_DEFAULT_LANGUAGE = 'en'
BABEL_DEFAULT_TIMEZONE = 'Europe/Zurich'
I18N_LANGUAGES = [
    ('en', _('English')),
]

BASE_TEMPLATE = 'cernopendata/page.html'
HEADER_TEMPLATE = 'cernopendata/header.html'
COVER_TEMPLATE = 'invenio_theme/page_cover.html'
SETTINGS_TEMPLATE = 'invenio_theme/settings/content.html'

SECRET_KEY = 'changeme'

# Theme
THEME_SITENAME = _('CERN Open Data Portal')
THEME_LOGO = 'img/home/opendata_logo.svg'

# Static file
COLLECT_STORAGE = 'flask_collect.storage.file'

# Cache
CACHE_TYPE = 'redis'

# Celery
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']

# JSONSchemas
JSONSCHEMAS_ENDPOINT = '/schema'
JSONSCHEMAS_HOST = 'opendata.cern.ch'

# OAI Server
OAISERVER_RECORD_INDEX = 'marc21'
OAISERVER_ID_PREFIX = 'oai:cernopendata:recid/'

# Records
# Add tuple as array type on record validation
# http://python-jsonschema.readthedocs.org/en/latest/validate/#validating-types
RECORDS_VALIDATION_TYPES = {
    'array': (list, tuple),
}

RECORDS_UI_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        route='/record/<pid_value>',
        template='invenio_marc21/detail.html',
        permission_factory_imp=None,
    ),
)

RECORDS_REST_ENDPOINTS['recid']['search_index'] = '_all'

RECORDS_REST_FACETS = dict(
    _all=dict(
        aggs=dict(
            category=dict(terms=dict(field='collections.secondary')),
            collections=dict(terms=dict(field='collections.primary')),
            run=dict(terms=dict(
                field='production_publication_distribution_manufacture_and_'
                      'copyright_notice.'
                      'date_of_production_publication_distribution_'
                      'manufacture_or_copyright_notice'
            )),
        ),
        post_filters=dict(
            collections=terms_filter('collections.primary'),
            category=terms_filter('collections.category'),
            run=terms_filter(
                'production_publication_distribution_manufacture_and_'
                'copyright_notice.'
                'date_of_production_publication_distribution_'
                'manufacture_or_copyright_notice'
            ),
        )
    )
)
"""Facets per index for the default facets factory."""

# Search
# ======
#: Default API endpoint for search UI.
SEARCH_UI_SEARCH_API = "/api/records/"
#: Default template for search UI.
# SEARCH_UI_BASE_TEMPLATE = 'cernopendata/page.html'
#: Default template for search UI.
SEARCH_UI_SEARCH_TEMPLATE = "cernopendata/search.html"
#: Default Elasticsearch document type.
SEARCH_DOC_TYPE_DEFAULT = None
#: Do not map any keywords.
SEARCH_ELASTIC_KEYWORD_MAPPING = {}

# OAI-PMH
# =======
#: Default Elasticsearch index.
OAISERVER_RECORD_INDEX = '_all'
#: OAI ID prefix.
OAISERVER_ID_PREFIX = 'oai:opendata.cern.ch:recid/'

# Open Data Portal
# ================
#: Information on homepage.
OPENDATA_EXPERIMENTS = [
    'CMS', 'ALICE', 'ATLAS', 'LHCb',
]

OPENDATA_EDUCATION = [
    ('CMS',
     'The CMS (Compact Muon Solenoid) experiment is one of two large '
     'general-purpose particle physics detectors built on the Large Hadron '
     'Collider (LHC) at CERN in Switzerland and France. The goal of CMS is to '
     'investigate a wide range of physics, including properties of the '
     'recently discovered Higgs boson as well as searches for extra '
     'dimensions and particles that could make up dark matter.',
     True),
    ('ALICE',
     '<a href="http://aliceinfo.cern.ch/Public/Welcome.html">'
     '<span class="external-link-l"></span>ALICE</a> '
     '(A Large Ion Collider Experiment) is a heavy-ion '
     '<a href="http://home.web.cern.ch/about/how-detector-works">'
     '<span class="external-link-l"></span>detector</a> designed to study '
     'the physics of strongly interacting matter at extreme energy densities, '
     'where a phase of matter called <a href="http://home.web.cern.ch'
     '/about/physics/heavy-ions-and-quark-gluon-plasma">'
     '<span class="external-link-l"></span>quark-gluon plasma</a> forms.<br/>'
     'The ALICE collaboration uses the 10,000-tonne ALICE detector - 26 m '
     'long, 16 m high, and 16 m wide - to study quark-gluon plasma. '
     'The detector sits in a vast cavern 56 m below ground close to the '
     'village of Saint Genis-Pouilly in France, receiving beams from the LHC. '
     'More than 1000 scientists are part of the collaboration.',
     True),
    ('ATLAS',
     '',
     True),
    ('LHCb',
     '',
     True),
]

OPENDATA_RESEARCH = [
    ('CMS',
     'The CMS (Compact Muon Solenoid) experiment is one of two large '
     'general-purpose particle physics detectors built on the Large Hadron '
     'Collider (LHC) at CERN in Switzerland and France. The goal of CMS is to '
     'investigate a wide range of physics, including properties of the '
     'recently discovered Higgs boson as well as searches for extra '
     'dimensions and particles that could make up dark matter.',
     True),
    ('ALICE',
     '',
     False),
    ('ATLAS',
     '',
     False),
    ('LHCb',
     '',
     False),
]
