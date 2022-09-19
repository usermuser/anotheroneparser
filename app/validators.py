# We going to use chain responsibility pattern here.
# The idea is to pass our data through different validators

import typing as t
from abc import ABC, abstractmethod

from app.exceptions import EmptyValidatorsChain


class ValidatorsChain:
    """todo docstring missing"""

    def __init__(self, validators_chain: t.List['BaseValidator']) -> None:
        self._validators = list()
        if validators_chain is None:
            raise EmptyValidatorsChain
        self._validators.extend(validators_chain)

    def validate(self, url: str) -> bool:
        result = False
        for validator in self._validators:
            result = validator.validate(url)
        return result


class BaseValidator(ABC):
    """todo docstring missing"""

    @abstractmethod
    def validate(self, url: str) -> bool:
        """
        Validator should implement concrete validation logic here.
        Can raise Exceptions.
        """
        return NotImplemented


class SchemeValidator(BaseValidator):
    """todo docstring missing"""

    def validate(self, url: str) -> bool:
        """Must be at least http or https.
        for simplicity we omit such variants
        like ftp, sftp, git, etc...
        """
        raise NotImplementedError


class NetlocValidator(BaseValidator):
    """todo docstring missing"""

    def validate(self, url: str) -> bool:
        """todo docstring missing"""
        raise NotImplementedError


class PathValidator(BaseValidator):
    """todo docstring missing"""

    def validate(self, url: str) -> bool:
        """todo docstring missing"""
        raise NotImplementedError


if __name__ == '__main__':
    is_valid_scheme = SchemeValidator()
    is_valid_netloc = NetlocValidator()
    is_valid_path = PathValidator()

    url_validators = ValidatorsChain([
        is_valid_scheme,
        is_valid_netloc,
        is_valid_path,
    ])

    is_valid_url = url_validators.validate('https://peps.python.org/pep-0008/')