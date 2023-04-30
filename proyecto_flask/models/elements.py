from datetime import date, time

class elements():
    def __init__(self,ID_elemento,referencia,nombres,cantidad,valor,estado,lugar, fecha_reg, hora_reg, Observaciones,ID_categorias) -> None:
        self.ID_elemento = ID_elemento
        self.referencia = referencia
        self.nombres = nombres
        self.cantidad = cantidad
        self.valor= valor
        self.estado = estado
        self.lugar = lugar
        self.fecha_reg = fecha_reg
        self.hora_reg = hora_reg
        self.Observaciones = Observaciones
        self.ID_categorias = ID_categorias
