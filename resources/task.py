from flask_restful import Resource, reqparse
from models.task import TaskModel
from flask_jwt_extended import jwt_required


class Tasks(Resource):

    def get(self):
        return {'tasks': [task.json() for task in TaskModel.query.all()]}  # Select * From


class Task(Resource):
    argumentos = reqparse.RequestParser()
    # argumentos.add_argument('task_id', type=str, required=True, help="The field 'task' cannot be left blank")
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
    argumentos.add_argument('descricao')
    argumentos.add_argument('tipo')
    argumentos.add_argument('dia')
    argumentos.add_argument('hora')
    argumentos.add_argument('local')
    argumentos.add_argument('participante')

    def get(self, task_id):
        task = TaskModel.find_task(task_id)
        if task:
            return task.json()
        return {'message': 'task not found'}, 404  # not found

    @jwt_required
    def post(self, task_id):
        if TaskModel.find_task(task_id):
            return {"message": "task if '{}' already exists.".format(task_id)}, 400  # Bad request
        dados = Task.argumentos.parse_args()
        task = TaskModel(task_id, **dados)
        try:
            task.save_task()
        except:
            return {'message': 'An internal error ocurred trying to save task.'}, 500
        return task.json()

    @jwt_required
    def put(self, task_id):
        dados = Task.argumentos.parse_args()
        task_encontrado = TaskModel.find_task(task_id)
        if task_encontrado:
            task_encontrado.update_task(**dados)
            task_encontrado.save_task()
            return task_encontrado.json(), 200
        task = Task(task_id, **dados)
        try:
            task.save_task()
        except:
            return {'message': 'An internal error ocurred trying to save task.'}, 500
        return task.json(), 201  # created

    @jwt_required
    def delete(self, task_id):
        task = TaskModel    .find_task(task_id)
        if task:
            try:
                task.delete_task()
            except:
                return {'message', 'An error ocurred trying to delete task'}, 500
            return {'message': 'task deleted.'}
        return {'message': 'task not found.'}, 404
