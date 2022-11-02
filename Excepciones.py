class ConsecionarioError:
    pass

class VehiculoNoExiste(ConsecionarioError):
    pass

class MotoNoexiste(ConsecionarioError):
    pass


class OpcionIncorrecta(ConsecionarioError):
    pass

class DatoIncorrecto(ConsecionarioError):
    pass