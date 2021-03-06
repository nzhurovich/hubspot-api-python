import hubspot
from hubspot.crm.timeline import EventsApi, TemplatesApi, TokensApi


def test_is_discoverable():
    apis = hubspot.Client.create().crm.timeline
    assert isinstance(apis.events_api, EventsApi)
    assert isinstance(apis.templates_api, TemplatesApi)
    assert isinstance(apis.tokens_api, TokensApi)
