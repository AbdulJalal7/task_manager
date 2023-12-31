from odoo import fields, models,api
from datetime import datetime,date,timedelta


class Task(models.Model):
    _name = 'task'

    title=fields.Char('Title')
    Description=fields.Text('Description')
    Deadline=fields.Date('Deadline')
    Completed=fields.Boolean('Completed')
    remaining_days=fields.Integer('Days Left',compute='_compute_left_days')

    @api.depends('Deadline')
    def _compute_left_days(self):
        for rec in self:
            current=date.today()
            if rec.Deadline:
                remaining=rec.Deadline-current
                print("RRRRRRRR : ",remaining)

                rec.remaining_days=3
            else:
                rec.remaining_days=0




    def action_complete(self):
        self.Completed=True


    @api.model
    def create(self, vals_list):
        return super(Task, self).create(vals_list)


    def write(self, vals):
        return super(Task, self).write(vals)

    
    def unlink(self):
        return super(Task, self).unlink()


