from pydantic import BaseModel

__all__ = ("BasePokemon", "UserPokemon")


class BasePokemon(BaseModel):
    """A base class for the pokemon object."""

    _types: list[str]
    _region: str
    _catchable: str
    _name: str
    _height: float
    _weight: float
    _base_hp: int
    _base_attack: int
    _base_defense: int
    _base_sp_attack: int
    _base_sp_defense: int
    _base_speed: int


class UserPokemon(BasePokemon):
    nature: str
    # IV attributes
    hp: list[int]
    level: list[int]
    attack: list[int]
    defense: list[int]
    sp_attack: list[int]
    sp_defense: list[int]
    speed: list[int]

    @property
    def _iv(self):
        """Total iv property decided by quotient of sum of individual iv attributes, multiplied by 100"""

        return round(
            (
                self.hp[1]
                + self.attack[1]
                + self.defense[1]
                + self.sp_attack[1]
                + self.sp_defense[1]
                + self.speed[1]
            ),
            2,
        )
