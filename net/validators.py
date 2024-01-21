from rest_framework.serializers import ValidationError


class NetValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        net = dict(value).get(self.field[0])
        type = dict(value).get(self.field[1])

        if type == 'Завод' and net is not None:
            raise ValidationError(
                'У завода не может быть поставщика')
        if type == 'Индивидуальный предприниматель' and net.type == 'Индивидуальный предприниматель':
            raise ValidationError(
                'Индивидуальный предприниматель не может быть поставщиком Индивидуального предпринимателя')
        if type == 'Индивидуальный предприниматель' and net.type == 'Розничная сеть':
            raise ValidationError(
                'Розничная сеть не может быть поставщиком Индивидуального предпринимателя')
        if type == 'Розничная сеть' and net.type == 'Розничная сеть':
            raise ValidationError(
                'Розничная сеть не может быть поставщиком Розничной сети')
