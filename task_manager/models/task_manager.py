from odoo import fields, models,api


class Task(models.Model):
    _name = 'task'

    title=fields.Char('Title')
    Description=fields.Text('Description')
    Deadline=fields.Date('Deadline')
    Completed=fields.Boolean('Completed')


    @api.model
    def create(self, vals_list):
        return super(Task, self).create(vals_list)


    def write(self, vals):
        return super(Task, self).write(vals)

    
    def unlink(self):
        return super(Task, self).unlink()


