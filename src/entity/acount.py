from dataclasses import dataclass
from typeEnum.Typecompte import TypeCompte
from typeEnum.devise import Devise
@dataclass
class Account:
    typeCompte: TypeCompte 
    money : int 
    devise : Devise