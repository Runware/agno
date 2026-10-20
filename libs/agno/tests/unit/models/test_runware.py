import os
from unittest.mock import patch

import pytest

from agno.exceptions import ModelAuthenticationError
from agno.models.runware import Runware
from agno.models.utils import get_model, get_model_from_dict


def test_runware_initialization_with_api_key():
    model = Runware(id="openai-gpt-5-mini", api_key="test-api-key")
    assert model.id == "openai-gpt-5-mini"
    assert model.api_key == "test-api-key"
    assert model.base_url == "https://api.runware.ai/v1"


def test_runware_initialization_without_api_key():
    with patch.dict(os.environ, {}, clear=True):
        model = Runware(id="openai-gpt-5-mini")
        client_params = None
        with pytest.raises(ModelAuthenticationError):
            client_params = model._get_client_params()
        assert client_params is None


def test_runware_initialization_with_env_api_key():
    with patch.dict(os.environ, {"RUNWARE_API_KEY": "env-api-key"}):
        model = Runware(id="openai-gpt-5-mini")
        assert model.api_key == "env-api-key"


def test_runware_base_url_from_env():
    with patch.dict(os.environ, {"RUNWARE_BASE_URL": "http://localhost:8080/v1"}):
        model = Runware(id="openai-gpt-5-mini", api_key="test-api-key")
        assert model.base_url == "http://localhost:8080/v1"


def test_runware_client_params():
    model = Runware(id="openai-gpt-5-mini", api_key="test-api-key")
    client_params = model._get_client_params()
    assert client_params["api_key"] == "test-api-key"
    assert client_params["base_url"] == "https://api.runware.ai/v1"


def test_runware_default_values():
    model = Runware(api_key="test-api-key")
    assert model.id == "openai-gpt-5-mini"
    assert model.name == "Runware"
    assert model.provider == "Runware"


def test_runware_resolves_from_string_syntax():
    model = get_model("runware:openai-gpt-5-mini")
    assert isinstance(model, Runware)
    assert model.id == "openai-gpt-5-mini"


def test_runware_round_trips_through_dict():
    model = Runware(id="openai-gpt-5-mini", api_key="test-api-key")
    rebuilt = get_model_from_dict(model.to_dict())
    assert isinstance(rebuilt, Runware)
    assert rebuilt.id == "openai-gpt-5-mini"
