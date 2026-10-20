from dataclasses import dataclass, field
from os import getenv
from typing import Any, Dict, Optional

from agno.exceptions import ModelAuthenticationError
from agno.models.openai.like import OpenAILike


@dataclass
class Runware(OpenAILike):
    """
    A class for interacting with Runware's OpenAI-compatible API.

    Runware exposes an OpenAI-compatible chat completions endpoint at
    https://api.runware.ai/v1 alongside its native media-generation API.

    Attributes:
        id (str): The id of the Runware model to use. Default is "openai-gpt-5-mini".
        name (str): The name of this chat model instance. Default is "Runware".
        provider (str): The provider of the model. Default is "Runware".
        api_key (str): The api key to authorize request to Runware.
        base_url (str): The base url to which the requests are sent.
            Defaults to "https://api.runware.ai/v1".
    """

    id: str = "openai-gpt-5-mini"
    name: str = "Runware"
    provider: str = "Runware"
    api_key: Optional[str] = field(default_factory=lambda: getenv("RUNWARE_API_KEY"))
    base_url: str = field(default_factory=lambda: getenv("RUNWARE_BASE_URL", "https://api.runware.ai/v1"))

    def _get_client_params(self) -> Dict[str, Any]:
        """
        Returns client parameters for API requests, checking for RUNWARE_API_KEY.

        Returns:
            Dict[str, Any]: A dictionary of client parameters for API requests.
        """
        if not self.api_key:
            self.api_key = getenv("RUNWARE_API_KEY")
            if not self.api_key:
                raise ModelAuthenticationError(
                    message="RUNWARE_API_KEY not set. Please set the RUNWARE_API_KEY environment variable.",
                    model_name=self.name,
                )
        return super()._get_client_params()
