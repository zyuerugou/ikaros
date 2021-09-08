# -*- coding: utf-8 -*-
''' task
'''
from ..model.task import _Task, _AutoTask
from .. import db


class TaskService():

    def getTask(self, taskname):
        task = _Task.query.filter_by(name=taskname).first()
        if not task:
            task = _Task(taskname)
            db.session.add(task)
            db.session.commit()
        return task

    def updateTaskStatus(self, status, taskname):
        """ status
            0: wait
            1: finished
            2: runing
        """
        task = self.getTask(taskname)
        if task.status != status:
            task.status = status
            db.session.commit()

    def updateTaskTotal(self, num, taskname):
        """ Update total num
        """
        task = self.getTask(taskname)
        if task.total != num:
            task.total = num
            db.session.commit()

    def updateTaskFinished(self, num, taskname):
        """ Update finished num
        """
        task = self.getTask(taskname)
        if task.finished != num:
            task.finished = num
            db.session.commit()


class AutoTaskService():

    def getTasks(self):
        return _AutoTask.query.all()

    def getRunning(self):
        return _AutoTask.query.filter_by(status=1).first()

    def getPath(self, path):
        return _AutoTask.query.filter_by(status=1).first()

    def commit(self):
        db.session.commit()


taskService = TaskService()
autoTaskService = AutoTaskService()
