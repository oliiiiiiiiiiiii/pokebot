from pydantic import BaseModel


class Pokemon(BaseModel):
    """A base class for the pokemon object."""

    _name: str
    _nature: str
    # IV attributes
    _level: int
    _attack: int
    _defense: int
    _sp_attack: int
    _sp_defense: int
    _speed: int

    @property
    def _iv(self):
        """Total iv property decided by quotient of sum of individual iv attributes, multiplied by 100"""

        return round(
            (
                self._attack
                + self._defense
                + self._sp_attack
                + self._sp_defense
                + self._speed
            ),
            2,
        )
