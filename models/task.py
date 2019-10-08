from sql_alchemy import banco


class TaskModel(banco.Model):
    __tablename__ = 'tasks'

    task_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

    def __init__(self, task_id, nome, estrelas, diaria, cidade):
        self.task_id = task_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'task_id': self.task_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
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

    def update_task(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def delete_task(self):
        banco.session.delete(self)
        banco.session.commit()