from sql_alchemy import banco


class TaskModel(banco.Model):
    __tablename__ = 'tasks'

    task_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    descricao = banco.Column(banco.String(80))
    tipo = banco.Column(banco.String(80))
    dia = banco.Column(banco.String(40))
    hora = banco.Column(banco.String(40))
    local = banco.Column(banco.String(40))
    participante = banco.Column(banco.String(40))

    def __init__(self, task_id, nome, descricao, tipo, dia, hora, local, participante):
        self.task_id = task_id
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.dia = dia
        self.hora = hora
        self.local = local
        self.participante = participante

    def json(self):
        return {
            'task_id': self.task_id,
            'nome': self.nome,
            'descricao': self.descricao,
            'tipo': self.tipo,
            'dia': self.dia,
            'hora': self.hora,
            'local': self.local,
            'participante': self.participante
        }

    @classmethod
    def find_task(cls, task_id):
        task = cls.query.filter_by(task_id=task_id).first()  # Select * From tasks Where task_id = $task_if
        if task:
            return task
        return None

    def save_task(self):
        banco.session.add(self)
        banco.session.commit()

    def update_task(self, nome, descricao, tipo, dia, hora, local, participante):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.dia = dia
        self.hora = hora
        self.local = local
        self.participante = participante

    def delete_task(self):
        banco.session.delete(self)
        banco.session.commit()